"""
Split downloaded speechgen batch MP3s into one file per word,
named audio/<word id>.mp3 — ready for the Masri SRS app.

HOW IT WORKS
Each batch_XX.txt you pasted into speechgen separates words with a
2-second pause. This script finds those silences in your downloaded
batch_XX.mp3, cuts the audio between them, checks that the number of
pieces matches the number of words in that batch, and saves each piece
under the right word id (from batches.json).

SETUP (one time)
- Install ffmpeg:
    Mac:      brew install ffmpeg
    Windows:  winget install ffmpeg      (or download from ffmpeg.org)
    Linux:    sudo apt install ffmpeg
- No Python packages needed.

USE
1) Put your downloaded files next to this script, named to match their
   text files: batch_01.mp3, batch_02.mp3, ... (any that exist).
2) Run:   python3 split_audio.py
3) It fills the audio/ folder. Already-split batches are skipped, so
   run it again any time you download more.

If a batch can't be split cleanly (count mismatch), it's reported and
skipped — nothing wrong is saved. Re-download that batch and try again.
"""

import json, pathlib, re, shutil, subprocess, sys

HERE = pathlib.Path(__file__).resolve().parent
AUDIO = HERE / "audio"
PAD = 0.12  # seconds of padding kept around each word

def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True)

def ffmpeg_ok():
    return shutil.which("ffmpeg") is not None

def detect_silences(mp3: pathlib.Path, noise_db: int, min_len: float):
    r = run(["ffmpeg", "-i", str(mp3), "-af",
             f"silencedetect=noise={noise_db}dB:d={min_len}", "-f", "null", "-"])
    text = r.stderr
    starts = [float(m) for m in re.findall(r"silence_start:\s*([0-9.]+)", text)]
    ends = [float(m) for m in re.findall(r"silence_end:\s*([0-9.]+)", text)]
    dur_m = re.search(r"Duration:\s*(\d+):(\d+):([0-9.]+)", text)
    dur = None
    if dur_m:
        h, m, s = dur_m.groups()
        dur = int(h) * 3600 + int(m) * 60 + float(s)
    return starts, ends, dur

def segments_from_silences(starts, ends, dur):
    # Speech segments are the gaps BETWEEN silences.
    segs = []
    pos = 0.0
    for s, e in zip(starts, ends + [None] * (len(starts) - len(ends))):
        if s - pos > 0.15:
            segs.append((pos, s))
        pos = e if e is not None else s
    if dur and dur - pos > 0.15:
        segs.append((pos, dur))
    return segs

def split_batch(mp3: pathlib.Path, ids: list) -> str:
    want = len(ids)
    # Try several detection settings until the piece count matches the word count.
    for noise in (-40, -45, -35, -30, -50):
        for min_len in (1.2, 1.0, 1.5, 0.8):
            starts, ends, dur = detect_silences(mp3, noise, min_len)
            if dur is None:
                return "could not read file (is it a valid MP3?)"
            segs = segments_from_silences(starts, ends, dur)
            if len(segs) == want:
                for (a, b), wid in zip(segs, ids):
                    a = max(0.0, a - PAD)
                    b = min(dur, b + PAD)
                    out = AUDIO / f"{wid}.mp3"
                    r = run(["ffmpeg", "-y", "-ss", f"{a:.3f}", "-to", f"{b:.3f}",
                             "-i", str(mp3), "-c:a", "libmp3lame", "-q:a", "4", str(out)])
                    if r.returncode != 0:
                        return f"ffmpeg failed cutting {wid}"
                return "ok"
    return f"couldn't split into exactly {want} pieces (last try found {len(segs)}) — re-download this batch and make sure the break tags were pasted along with the words"

def main():
    if not ffmpeg_ok():
        sys.exit("ffmpeg not found — see the SETUP notes at the top of this file.")
    manifest = json.loads((HERE / "batches.json").read_text(encoding="utf-8"))
    AUDIO.mkdir(exist_ok=True)
    done = skipped = missing = failed = 0
    for name, ids in manifest.items():
        mp3 = HERE / f"{name}.mp3"
        if not mp3.exists():
            missing += 1
            continue
        if all((AUDIO / f"{wid}.mp3").exists() for wid in ids):
            skipped += 1
            continue
        print(f"{name}: splitting {len(ids)} words...", end=" ", flush=True)
        result = split_batch(mp3, ids)
        if result == "ok":
            done += 1
            print("ok")
        else:
            failed += 1
            print(f"SKIPPED — {result}")
    total_files = len(list(AUDIO.glob("*.mp3")))
    # Write the manifest the app uses to mark words that have recorded audio (🎙).
    ids = sorted(p.stem for p in AUDIO.glob("*.mp3"))
    (HERE / "audio_manifest.json").write_text(json.dumps(ids), encoding="utf-8")
    print(f"\nBatches split now: {done} · already done: {skipped} · not downloaded yet: {missing} · failed: {failed}")
    print(f"audio/ now contains {total_files} word files. audio_manifest.json updated ({len(ids)} entries).")
    print("Push anytime — the app uses whatever exists.")

if __name__ == "__main__":
    main()

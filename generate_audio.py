"""
Generate real Egyptian Arabic audio for every word in Masri SRS.

Uses Microsoft Azure Speech, which has genuine Egyptian voices
(ar-EG-SalmaNeural / ar-EG-ShakirNeural — very likely the same voices
speechgen.io resells). The free tier (F0) includes 500,000 characters
per month; the whole dictionary is only ~10,000 characters, so this
costs nothing.

ONE-TIME SETUP
1) Create a free Azure account: https://azure.microsoft.com/free
2) In the Azure portal: Create a resource -> "Speech" -> pick the free
   F0 tier and a region (e.g. southeastasia). Open the resource and
   copy KEY 1 and the Region.
3) Install the one dependency:   pip install requests

RUN (from your masri-srs repo folder, with words.json next to this file)
   AZURE_KEY=your_key AZURE_REGION=southeastasia python3 generate_audio.py

It creates audio/<id>.mp3 for every word, skips files that already
exist (safe to re-run), then you just:
   git add .
   git commit -m "add recorded Egyptian audio"
   git push
"""

import json, os, sys, time, pathlib

try:
    import requests
except ImportError:
    sys.exit("Please run:  pip install requests")

KEY = os.environ.get("AZURE_KEY")
REGION = os.environ.get("AZURE_REGION", "southeastasia")
VOICE = os.environ.get("AZURE_VOICE", "ar-EG-SalmaNeural")  # or ar-EG-ShakirNeural (male)
RATE = os.environ.get("AZURE_RATE", "-10%")  # slightly slower for learners

if not KEY:
    sys.exit("Set AZURE_KEY (and AZURE_REGION) environment variables first — see the header of this file.")

URL = f"https://{REGION}.tts.speech.microsoft.com/cognitiveservices/v1"
HEADERS = {
    "Ocp-Apim-Subscription-Key": KEY,
    "Content-Type": "application/ssml+xml",
    "X-Microsoft-OutputFormat": "audio-24khz-48kbitrate-mono-mp3",
    "User-Agent": "masri-srs-audio",
}

def ssml(text: str) -> str:
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (
        f"<speak version='1.0' xml:lang='ar-EG'>"
        f"<voice name='{VOICE}'><prosody rate='{RATE}'>{text}</prosody></voice></speak>"
    )

def main():
    here = pathlib.Path(__file__).resolve().parent
    words = json.loads((here / "words.json").read_text(encoding="utf-8"))
    outdir = here / "audio"
    outdir.mkdir(exist_ok=True)

    done = skipped = failed = 0
    for i, w in enumerate(words, 1):
        out = outdir / f"{w['id']}.mp3"
        if out.exists() and out.stat().st_size > 0:
            skipped += 1
            continue
        try:
            r = requests.post(URL, headers=HEADERS, data=ssml(w["ar"]).encode("utf-8"), timeout=30)
            if r.status_code == 200 and r.content:
                out.write_bytes(r.content)
                done += 1
                print(f"[{i}/{len(words)}] {w['id']}  ({w['tr']})  ok")
            else:
                failed += 1
                print(f"[{i}/{len(words)}] {w['id']}  HTTP {r.status_code}: {r.text[:120]}")
                if r.status_code == 429:  # rate limited — breathe and continue
                    time.sleep(5)
        except Exception as e:
            failed += 1
            print(f"[{i}/{len(words)}] {w['id']}  ERROR: {e}")
        time.sleep(0.25)  # stay well under free-tier rate limits

    print(f"\nDone: {done} generated, {skipped} already existed, {failed} failed.")
    if failed:
        print("Just run the script again — it only retries the missing ones.")

if __name__ == "__main__":
    main()

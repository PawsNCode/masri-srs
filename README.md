# Masri SRS 🌙

A web app for learning **Egyptian Arabic (Masri)** — spaced-repetition vocabulary,
typed-Arabic quizzes, a full alphabet trainer, and a progress dashboard. The whole
thing is a single self-contained HTML file you can run anywhere or install to your
home screen.

🔗 **Live app:** https://pawsncode.github.io/masri-srs/

## Features

### Vocabulary (WaniKani-style)
- **1,639 items across 87 levels** — words, phrases, and full sentences, grouped by
  theme and difficulty (greetings → grammar → daily life → dialogues → slang), with
  **male and female forms side by side**: every gendered word, phrase, and sentence
  (adjectives, commands, questions, endearments) appears in both forms, the feminine
  directly after the masculine, so you always learn and compare the pair together
  (taʿbaan/taʿbaana, rooH/rooHi, esmak eh/esmik eh…). Where the two forms are spelled
  identically in bare script, the feminine carries a small vowel mark (عندَك → عندِك)
  so you can see and hear the difference.
- **Instant level unlock** — the next level opens the moment you've **learned every
  item** in your current level (no need to master them first). Learn the last word of
  a level and its successor is immediately available in Lessons.
- **SRS stages** — every item climbs Apprentice → Guru → Master → Enlightened →
  Burned, resurfacing right before you'd forget it. (Scheduling still drives *when*
  things come back; **mastery %** is a separate, simpler score — see below.)
- **Half-back on a miss** — get a review wrong and the item loses **half its SRS
  progress** (the 50% setback), so its next due date pulls back in. Honest mistakes
  cost you, so you really learn it.
- **Mastery = your run of correct answers** — an item's mastery % is your **current
  streak of correct answers across every quiz type** (typing, multiple choice,
  tracing, marks, reviews — all of it). Each correct answer adds **1%**; a single miss
  resets it to **0**. Answer it right **100 times in a row** and it's **100% mastered**.
- **Five mastery tiers, color-coded** — every word, letter shape, and mark shows a
  colored bar by tier: **Learning 0–19%** (red), **Shaky 20–44%** (orange),
  **Familiar 45–69%** (yellow), **Strong 70–89%** (light green), **Mastered 90–100%**
  (green), plus a live % per item.
- **Greener, clearer answer feedback** — in **every** quiz and review, the moment you
  answer the screen shows a bold **CORRECT ✓** in green (or **NOT QUITE ✗** in red),
  the right choice is highlighted **green**, and a wrong pick is highlighted **red** —
  so there's no mistaking how you did.
- **Lessons hub** — the Lessons tab opens to a small menu: **learn a batch of new
  words** (3/5/7/10, your choice) and then quiz them to lock them in, **quiz all the
  words you've learned** in one shuffled drill, or **start a custom quiz** of words you
  hand-picked with the ★ in Items.
- **Word detail & letter breakdown** — tap any Arabic word in Items, **or the correct
  answer shown after a quiz/review question**, to open a detail page: the full word,
  romanization, English, sound, and a **letter-by-letter breakdown** showing the exact
  shape each letter takes in that word (isolated / initial / medial / final). Tap any
  letter to jump straight to its **trace guide and practice — opened on the exact shape
  it had in the word** (tap a final-form letter, land on its final-form guide). There's a
  **try-typing box with a Check button** to test yourself, plus a **"Try writing it"
  pad** where you can finger-trace the whole word over a faint guide.
- **Answer your way** — each quiz/review lets you **Type** the Arabic or answer by
  **Multiple choice**. The on-screen Arabic keyboard is **hidden by default everywhere**
  (type with your phone keyboard) and pops up only when you tap **Show in-app keys**. The
  **Check button sits right under the input** so it's visible without scrolling, and the
  in-app keys (when shown) drop in below it. When you get a typed answer checked, the
  result shows the correct spelling *and* its letter-by-letter breakdown (tap a letter for
  its trace guide), and the **Next button stays pinned to the bottom** so it's always in reach.
- **Richer lessons** — when learning a new word you now see everything at once: the
  word, romanization, English, sound, the same tappable letter breakdown, a
  type-it-yourself Check box, and a **"Try writing it" pad** to finger-trace the whole
  word — so you read it, hear it, see how it's built, type it, and physically write it
  before tapping **Learn it**. (Learning a new letter has its own "Now write it" trace
  pad in the same spot.)
- **Universal mnemonics on everything you learn** — a 🧠 **Memory hook** appears
  wherever you learn something, using proven memory techniques:
  - **Letters** get a *looks-like* + *sounds-like* hook (e.g. ب is “a boat with one
    dot below — B for Boat”; ح is “a hippo mid-yawn — a breathy H from the throat”),
    shown in the alphabet reference and on every trace guide.
  - **Marks (harakat)** get their own hook (e.g. kasra “sits low, like the i in *sit*”).
  - **Words** get a keyword/link hook — the pronunciation broken into easy **beats**
    plus a sound-alike English word to picture together with the meaning.
  - **Phrases & sentences** get a chunk-and-story hook to chain the beats into one scene.
- **Auto-play pronunciation** — a toggle in Home → settings speaks each word
  automatically as you learn it or when an answer is revealed. Turn it off for a quiet
  session.
- **Drill to mastery** — every quiz and review (words *and* script shapes) keeps going
  until you answer **each item correctly twice in a row**. Miss one and its streak
  resets, and it comes back later in the same session — the quiz never ends, and never
  congratulates you, until everything is cleared. Each item still updates the SRS just
  once per session (counted as a miss if you slipped on it at all), so spacing stays
  intact. The finish screen offers a one-tap **Retake**.

### Arabizi (Franco-Arabic)
- **Every item now carries its Arabizi** — the way Egyptians actually text, with
  numbers standing in for the sounds Latin letters don't have: **3** = ع, **7** = ح,
  **5** = خ, **2** = the glottal stop. It shows on lesson cards, quiz feedback, the
  Items list and every detail page (صباح الخير → *sabaa7 el-5eer*, قهوة → *2ahwa*).
- **Generated, not hand-typed** — the Arabizi is derived from each card's Arabic
  spelling and transliteration, so **when you correct a card, its Arabizi updates with
  it**. You can still override it by hand in the edit form; leave that field blank and
  the app keeps generating it for you.
- **Type in Arabizi** — the "try typing it" box on every lesson and detail page has an
  **العربية Arabic / 🔤 Arabizi** toggle, so you can practise either script.
- **Quiz in Arabizi** — quizzes and reviews now offer three answer modes:
  **✍️ Arabic**, **🔤 Arabizi**, and **🔘 Choice**. In Arabizi mode the input switches
  to a normal Latin keyboard (the Arabic keys stay out of the way).
- **Forgiving grading** — Franco spelling is personal, so anything that's genuinely
  the same word counts: `7` or `h`, `5` or `kh`, `3'` or `gh`, an optional `2`, doubled
  vowels, `e`/`i` and `o`/`u` all fold together. *7abibi*, *habibi* and *habeebi* are
  all accepted.
- **Search by Arabizi too** — typing `7abibi` in the Items search finds حبيبي.

### Verbs
- **A third category alongside Vocabulary and Conversations** — **30 core Egyptian
  verbs** (Lessons → ⚡ Verb lessons, or the Verbs row in the Items filter): akal,
  raaH, ʿamal, shaaf, ʾaal, khad, fataH, ʿeref, Habb, etkallem and more.
- **Three example sentences per verb — 90 in all** — every verb links to three short,
  practical sentences that put it to work (أكل → *ana akalt feTaar* / *betaakol eh?* /
  *ʿaayez aakol Haaga*). The sentences live in the **Conversations** category
  (Conversations: Verbs in Action), so they browse and filter with everything else.
- **Learn them from the verb itself** — open a verb and its three sentences are right
  there with sound, transliteration, Arabizi and a **Learn this sentence ✓** button.
  Tap it and the sentence **joins your normal reviews immediately**, on the same SRS
  schedule as everything else — no separate system.
- **Progress at a glance** — the Verbs hub shows each verb's SRS stage plus an
  **x/3 sentences** counter, and a **Quiz verbs + sentences** drill mixes the verbs
  together with whichever of their sentences you've picked up.

### Reviews hub
- Choose **what** to review: **letters (script), words, phrases, sentences, or all
  vocabulary** — each with its own due count.
- **Trouble words** — anything you miss twice in a row is flagged and can be
  drilled on its own.
- **Pick your own** — select specific words (Items) or letters (Script) to quiz.
- **Custom quiz** — tap the ★ on any word or letter to save it to a personal quiz
  you can run anytime; your picks persist across sessions. In Items the **Start custom
  quiz** button now sticks to the top of the list, so it's one tap away no matter how
  far you've scrolled. **Starring an item instantly unlocks it** — if you hadn't
  learned it yet, it's added as learned right away so it's quizzable on the spot (no
  more 🔒 on things you've hand-picked).
- **Add to custom quiz by mastery level** — a panel in Items lets you pick one or
  more **SRS levels** (Apprentice / Guru / Master / Enlightened / Burned) and drop
  **every learned item at those levels** into your custom quiz in one tap. Want to
  drill everything that's still Apprentice *and* everything at Guru? Select both and
  add them all at once.

### Script / alphabet
- **Train** — learn letters in batches with real **SRS scheduling**. Every letter is
  tracked and quizzed **per shape** — isolated, initial, medial, and final — so the
  six one-way letters have two shapes and the rest have four (100 shapes in all). The
  due count, drills, and quizzes all work at the shape level. Three quiz styles: *see
  shape → pick sound*, *hear sound → type the letter*, and *hear sound → **write** the
  shape*, each showing which position is being tested.
- **Focus a shape** — a filter (All / Iso / Init / Med / Fin) at the top of the script
  menu lets you aim every quiz and drill at just one positional form, so you can grind
  the shape you find hardest. The trace guide has the same filter, so you can practice
  tracing only initials, only medials, and so on (one-way letters with no initial or
  medial form are skipped automatically).
- **Tracing quiz in the SRS** — the write-the-shape quiz is part of lessons and spaced
  review: write from memory, reveal, self-grade. A miss halves that shape's progress
  (same half-back rule as words) and re-queues it so you retake it.
- **Chart** — the full 28-letter reference with a pronunciation key and stroke-order
  guides. Every one of the four positional forms now shows **its own mastery % and a
  color bar** in the same five tiers (red → green as your correct-answer run grows;
  grey = not started), plus an overall % per letter — so you can see at a glance
  exactly which shapes still need drilling. **Each form cell (iso / init / med / fin)
  is tappable** and opens the trace guide right on that shape, so you can practice
  writing exactly the form you want.
- **Quiz** — match letters to sounds with live score, accuracy, and streaks.
- **Trace** — finger-trace letters over a soft ghost glyph on a 2×2 grid, with
  written stroke-order steps, plus a write-from-memory quiz mode.
- **Marks (harakat)** — a dedicated section that teaches the short-vowel and helper
  marks: **fatha, kasra, damma, sukun, shadda** and the **tanwin** endings (plus madda
  and dagger-alef in the reference). Flip through illustrated cards (each mark shown on
  a dotted circle and on a carrier letter, with a real example word), then take a
  **pronunciation quiz**: see a marked letter and choose how it's read (بَ → "ba"), or
  see a sound and choose how it's written ("ba" → بَ). The carrier letter varies and the
  same drill-to-mastery loop applies — twice in a row to clear each mark. Every mark now
  carries its **own mastery %** (a color bar on each reference card, plus an overall
  mastery figure for the section), so progress on the marks is tracked just like words
  and letter shapes.
- **Marks explained in context** — anywhere a word is broken into letters (Items
  detail, lessons, and the answer shown after a quiz question), letters that carry a
  mark are highlighted, and a **"Marks in this word"** panel explains each one. Tapping
  a marked letter opens its trace guide *and* the explanation of the mark sitting on it.

### Dictionary, stats & looks
- **Items** is a searchable dictionary (English / transliteration / Arabic /
  **Arabizi**) with a count for every level, organised into **Vocabulary**,
  **🗣 Conversations**, **⚡ Verbs** and **🔊 By audio** filter rows.
- **Your corrections apply everywhere, instantly** — edit a card's Arabic,
  transliteration, English or Arabizi from its detail page and the change shows up in
  every list, lesson, review and custom quiz **including a quiz you're in the middle
  of** — and the corrected spelling is what gets graded. An **↺ Reset to the original
  card** button puts it back the way it shipped. Corrections are saved with your data
  and travel in your backups.
- **Stats** dashboard: a **mastery-weighted Whole app %** (every item contributes
  its own mastery run, unlearned counting as 0 — so the number moves with every
  answer, not only when something crosses the 90% line), the current level's Guru
  ring, words learned/mastered/burned, and a review pipeline (due now / 24h / 7 days).
- **Progress by category** — a dedicated card for **📚 Vocabulary, 🗣 Conversations
  and ⚡ Verbs**: each shows how many you've learned (count *and* %), a **stacked bar
  of the whole category colored by mastery tier** (grey = not yet learned), per-tier
  counts with their share of what you've learned, and the category's own
  mastery-weighted %.
- **Progress by level, grouped by category** — the per-level list is organised under
  Vocabulary / Conversations / Verbs headings; every level shows **learned n/total**
  (the bar) plus its **mastery %, colored by tier**, and includes your own added
  cards. Plus the overall **mastery breakdown** across everything started (words,
  letter shapes, marks), a 14-day "new words" graph, a 14-day activity graph, and a
  **full-month activity calendar** you can page through month by month — each day
  shaded greener the more you studied, with today ringed.
- **Build a custom quiz from your audio** — alongside "add to custom quiz by mastery
  level", you can now build a listening set from what you can actually *hear*:
  **🎙 cards with recorded audio**, **🎤 cards in my own voice**, or **🎧 everything
  with any audio**. The Items browser has matching filter chips.
- **Themes** — six color themes (Rose, Violet, Bubblegum, Mint, Dark, Midnight),
  chosen at the bottom of the Home screen.
- **Record your own voice — in both languages** — every card's detail page has an
  **🎤 In my voice** panel with two recording slots (15 seconds each): **Masri**,
  your pronunciation of the Arabic, which is what the 🔊 buttons play app-wide when
  the card is set to "My voice"; and **English**, your own reading of the meaning,
  which the 🎧 playlist plays before your Masri in "English + Masri" mode. Each slot
  has play / re-record / delete. Cards with a Masri recording show a **🎤** in the
  Items list.
- **🎧 My Voice Playlist** (Lessons → Listening) — every card you've recorded,
  played back to back as a continuous listening drill. Filter the queue by
  **level** and/or **mastery tier** (including not-yet-learned cards), choose
  whether each track plays as **English + Masri** or **Masri only**, and toggle
  **loop forever** and **shuffle**. A **Repeat each card** setting plays every
  card **× 1**, **× 2 English + Masri** (the whole pair twice), or **× 2 Masri
  only** (meaning twice, said twice) — in both the live player and the stitched
  background track. In English + Masri mode the English part is
  **your own English recording** whenever the card has one (marked **EN** in the
  track list), with the device's English voice as the fallback. The player card shows the
  current word (Arabic, transliteration, Arabizi, English) with ⏮ ▶ ⏸ ⏭
  controls, and a tappable track list jumps anywhere in the queue. One shared
  audio element is unlocked by the Play tap and reused for every track, so
  auto-advance keeps working on iOS.
- **🌙 Background mode (lock-screen playback)** — the regular player stops when
  the phone locks, because iOS freezes a web app's JavaScript between tracks. Tap
  **Build & play in background** and the current queue (same filters, mode,
  shuffle and loop) is stitched into **one continuous audio track** — English
  recording (in English + Masri mode), then Masri, with natural gaps — which
  keeps playing with the **screen locked**, in **other apps**, and even if you
  leave the playlist screen, with **play/pause and the current card's name on
  the lock screen** (Media Session). A mini-player shows the moving now-playing
  card, position, pause/resume, a **⬇ save** button that downloads the stitched
  track as a .wav (play it from any music or files app), and discard; changing
  filters, mode or repeat discards the stale track. A **keep-alive** watches for
  the bare pause iOS sometimes fires on lock and nudges playback back within a
  second — while always respecting a pause *you* chose, on screen or from the
  lock screen. Playback also declares itself as media to iOS (Audio Session
  API), so it's treated like a music app: kept alive with the screen off and not
  muted by the ring/silent switch.
- **Home-screen version — what iPhone allows, and three ways around it.** iOS
  suspends *home-screen* web apps the moment the screen locks (script and audio
  alike; Safari tabs are exempt). The playlist detects this and shows the routes
  that genuinely work: **① ⬆ share / save** the stitched track → *Save to Files*
  and play it from the Files app, which is never interrupted; **② ☀️ Keep screen
  on** — a toggle that holds a screen wake lock while either player runs, so
  nothing gets suspended; **③ Open in Safari** (or copy the link) — a
  `?view=playlist` deep link that opens straight onto the playlist, where
  background audio just works (restore a *Voice only* backup there once, since
  the home-screen app and Safari keep separate storage). The playlist setup —
  filters, mode, repeat, loop, shuffle, keep-awake — is now saved and restored,
  and a small status line shows which mode you're running in and which platform
  hooks are available. Cards without an English recording play Masri only
  in this mode — the device's speech voice can't run in the background.
- **Recordings now live in IndexedDB** — they used to be stored inside the same
  localStorage blob as your progress, which has a hard ~5 MB limit. Once you'd
  recorded enough to cross it, **every save failed silently** and later changes
  (including card corrections) were quietly dropped. Audio has moved to IndexedDB,
  which has no practical size limit, so progress and recordings no longer compete for
  the same space. Existing recordings are migrated automatically the first time you
  open this version, and any future storage problem is now **reported in the Backup
  panel instead of being swallowed**.
- **Recorded Egyptian audio (best on iPhone)** — the app now plays a **real Egyptian
  recording** for any word that has one: drop MP3s named `audio/<word id>.mp3` into
  the repo (word ids are in `words.csv` / `words.json`) and every player button and
  auto-play uses them automatically, falling back to the speech engine for words
  without a file. The repo ships `generate_audio.py`, which builds all ~878 clips in
  one run using Azure's genuine Egyptian neural voices (free tier covers it easily) —
  see the script header for the 5-minute setup. This is the way to get true Masri
  audio on iOS, which has no Egyptian system voice.
- **Audio — Masri pronunciation engine** — tap-to-hear speech no longer reads the
  bare dictionary spelling (which browser voices pronounce with Standard-Arabic
  vowels). Instead, every word is spoken from a **fully vocalized Egyptian
  respelling** generated from its transliteration: the real Masri vowels, shaddas,
  and glottal stops (so قهوة is spoken *"ʔahwa"*, not *"qahwa"*), with the emphatic
  and throaty consonants (ح ص ط ض ظ ع) recovered from the true spelling. A settings
  toggle can switch back to plain reading.
- **Arabic voice picker** — Home → settings now lists every Arabic voice installed
  on your device with a ▶ test button. Most devices only ship Standard-Arabic
  voices; if yours offers an **Egyptian (ar-EG)** voice (marked ⭐), pick it — that
  plus the engine gets you closest to native Masri audio. The app auto-prefers an
  Egyptian voice when one exists.
- **App icon** — a rose-gradient ʿain (ع) with a crescent moon, used as the
  favicon and home-screen icon.
- **Backup & restore** — from the Home settings, **⬇ Download full backup** saves
  everything in one file: progress, **every correction you've made to a card**, your
  custom cards and quizzes, settings, **and all your voice recordings** (the button
  shows how many are included). There's also a **🎤 Voice only** export — a smaller
  file for moving recordings to another device, which restores your audio *without*
  touching your progress — and a **Progress only** option. Copy and Show text leave
  the audio out (it's far too big for the clipboard) and say so.
- **Progress saves on your device** and the app installs to your home screen.
- **Refresh app** — a card in the footer with a **"Refresh to latest version"** button
  that reloads the newest version of the app straight from the web, so the home-screen
  shortcut never gets stuck on an old build. It only refreshes the code — your progress,
  levels, custom quizzes, and settings are all kept (they live in your browser's storage,
  which the reload doesn't touch). The card also shows the **app version** and the
  **exact date and time** of the last update.

## How to use

- Open the live link above, or download `index.html` and open it in any browser.
- **On iPhone:** open the link in Safari → **Share** → **Add to Home Screen** for a
  full-screen, app-like icon.
- After the app is updated, just tap **Refresh to latest version** in the footer to pull
  the latest version — no need to delete and re-add the home-screen icon, and nothing
  you've learned is lost.

## Built with

- A single HTML file using React 18.3.1 + Babel Standalone 7.26.4, pinned and loaded from the jsDelivr CDN
- Pronunciation via the browser's Web Speech API (uses your device's Arabic voice)
- Progress, corrections and settings in localStorage; voice recordings in IndexedDB

---

*Last updated (v2.10.0 · 9/19/2026): **Background playback, addressed at the root.**
The app is installed as a *home-screen* web app, and iPhone suspends those the moment
the screen locks — script and audio together — while Safari tabs are exempt; no
keep-alive can run inside a suspended app, which is why the stitched track still
stopped. This release adds the one hook iOS does honour (the Audio Session API, so
playback is treated as media: alive with the screen off, immune to the silent switch)
and, when running as the home-screen app, a notice with three working routes:
**⬆ share / save** the stitched track to Files and play it from the Files app;
**☀️ Keep screen on**, a screen-wake-lock toggle that follows either player; and
**Open in Safari** / copy link, a `?view=playlist` deep link that lands on the
playlist. The playlist setup is now persisted (filters, mode, repeat, loop, shuffle,
keep-awake), and a status line reports the running mode and available hooks. Engine
suite: 42 scenarios.*

*Earlier (v2.9.0 · 9/19/2026): **Repeat each card + steadier background
playback.** New repeat setting in the playlist — **× 1**, **× 2 English + Masri**
(English, Masri, English, Masri) or **× 2 Masri only** (English once, Masri twice;
in Masri-only mode simply your Masri twice) — applied identically by the live
player and the stitched background track. Background playback is hardened for the
lock screen: iOS sometimes fires a bare pause on the audio element when the phone
locks, so a keep-alive now distinguishes a system pause from one you chose and
nudges the track back within a second, with a visibility handler that resumes the
moment the page runs again if the system froze it outright; the lock screen's
playback state now stays in sync too. The stitched track also gained a **⬇ save**
button — it's a real .wav, so you can drop it in a music or files app for
bulletproof background listening. Engine suite: 37 scenarios.*

*Earlier (v2.8.0 · 9/19/2026): **🌙 Background mode — the playlist keeps
playing with the screen locked or in another app.** iOS freezes a web app's
JavaScript on lock, which kills any playlist that advances track by track — so
background mode decodes your recordings with WebAudio, lays the whole queue out on
one timeline (English recording where the mode wants one, then Masri, with natural
gaps), renders it to a single WAV, and plays that through one continuous audio
element that media playback rules keep alive. It survives locking, app-switching
and leaving the playlist screen, loops if Loop is on, and puts play/pause plus the
current card's Arabic + English on the lock screen via the Media Session API. The
playlist screen gets a stitching progress bar and a mini-player whose now-playing
card follows the timeline. The engine suite grew to 29 scenarios, covering the
stitch layout, offsets, English inclusion, lock-screen metadata, mutual exclusion
with the regular player, and stale-track invalidation.*

*Earlier (v2.7.0 · 9/19/2026): **Record the English side too.** Every card's
🎤 In my voice panel now has two slots — **Masri** (drives the 🔊 buttons when a card
is set to "My voice", exactly as before) and **English** (your own reading of the
meaning). The 🎧 playlist's modes are now **English + Masri** — your English
recording first when the card has one (EN badge in the track list), the device's
English voice otherwise, then your Masri — and **Masri only**. Level and mastery
filters apply to both modes. English clips are stored in IndexedDB under their own
keys, ride along in full and voice-only backups, are pre-loaded for instant
playback, and existing recordings and backups are untouched (old backups restore
cleanly; new backups carry both voices). The playlist engine test suite grew to 17
scenarios, covering English-clip playback, TTS fallback, mode isolation, and the
badge.*

*Earlier (v2.6.0 · 9/19/2026): **🎧 My Voice Playlist** — a new Listening
section in Lessons that plays your own recordings back to back, all the time if you
want: loop-forever and shuffle toggles, filters by **level** and/or **mastery tier**
(with a "Not learned" tier for recorded-but-unlearned cards), and a per-track mode
choice of **English meaning + my voice** (the device says the English, then you say
the Masri) or **my voice only**. The player shows the current card in full — Arabic,
transliteration, Arabizi, English, tap to open the card — with prev/play/pause/next
controls and a track list you can tap into anywhere. Auto-advance is engineered for
iOS: one audio element is unlocked on the Play tap and reused for the whole session.
The whole engine was driven end to end in a test harness (14 scenarios: sequencing,
loop wrap-around, pause, English-then-voice chaining, and both filters), which also
caught and fixed a queue-staleness bug where changing filters while paused would
have resumed the old unfiltered queue.*

*Earlier (v2.5.2 · 7/30/2026): **Own-voice fix for manually added cards.** The
speaker buttons find a card's recording by looking its Arabic spelling up in a
spelling→id map — but custom cards only entered that map if they had a
transliteration, so a card added without one (stored as "—") was invisible to the
lookup: your recording saved fine and the ▶ My voice preview worked, yet every
speaker button in lessons, quizzes and lists fell back to TTS. Custom cards are now
always registered regardless of translit, and speak() gained a safety net: if the
mapped card isn't set to your voice, it checks whether any other card with the same
spelling is (covering manually added cards that duplicate a built-in spelling). All
five playback paths unit-tested, including the three pre-existing ones, which are
unchanged.*

*Earlier (v2.5.1 · 7/30/2026): **iPhone fix — own-voice playback.** Recordings
are stored (and backed up) as base64 `data:` URLs, and iOS Safari silently refuses to
play `data:` URIs in audio elements — so on the iPhone your voice saved fine but
played as nothing at all, both from the ▶ My voice button and when a card was set to
"Plays in app: My voice." Clips are now converted to Blob object URLs before playing
(synchronously, so it still counts as part of your tap); storage and backup formats
are unchanged. Verified byte-for-byte for both iOS (audio/mp4) and desktop
(audio/webm) recordings.*

*Earlier (v2.5.0 · 7/30/2026): **Daily Life Phrases** — a second video-lesson
category (Conversations: Daily Life Phrases, 41 items, 1,598 → 1,639) from the
"50 daily phrases" lesson: finding things (alaaʾi feen taksi/Saydaleyya?, feen
es-safaara betaʿti?, feen el-ʾonSoleyya?), understanding (yaʿni eh da?, momken
teʿiid/i?, ana mesh ʿaaref/ʿarfa), identity (da raʾami, da raʾam mobaayli, ana
ʿaazeb/aanesa, ana metgawwez/a), health (ana ʿayyaan/a, agzakhaana), transactions
(ana ʿaayez/ʿayza aHgez tarabeeza, adfaʿ kaash), opinions (ana motafaaʾel, ana mesh
mowaafeʾ/mowafʾa, da rawʿa), the idiom riiʾi neshef ("my spit dried up" = parched),
la moʾakhza, the casual aah, plus family words the app was missing (baaba, maama,
okhti, akhooya, osra) and momtaaz, meHtaag, mosaʿda. Ten phrases the lesson taught
were detected as already in the app (begad, es-saaʿa kaam, ʿandi Sodaaʿ, basboor,
ana mowaafeʾ/a, mafiish moshkela, khalli baalak/baalik…) and skipped. Two cards were
**enhanced** rather than duplicated: **باسبور now also accepts جواز سفر / gawaaz
safar** as a correct answer, and **ʿeila is clarified as the extended family** now
that osra (the immediate family) exists alongside it.*

*Earlier (v2.4.0 · 7/30/2026): **Survival Essentials** — a new always-unlocked
conversation category (Conversations: Survival Essentials, 54 items, 1,544 → 1,598)
built from two spoken-Egyptian survival-phrase lessons: thanks and their replies
(shokran gaziilan, motshakker/a, alf shokr, el-ʿafw), meeting people (tasharrafna →
leyya el-sharaf), courtesy pairs (mabrook → allah yebaarek fiik/i, salamtak/ik →
allah yesallimak), apologies (ana aasef/asfa, baʿd eznak/ik — with ʿan eznak accepted
as an alternate answer), the respectful hadretak/hadretik, communication lifesavers
(betetkallem ʿarabi?, ana mesh batkallem ʿarabi, mesh fahma, etkallem beshweesh law
samaHt), five language names (engliizi, faransaawi, almaani, esbaani, iTaali) plus
ʿarabi and maSri, and introduce-yourself Q&A (saaken feen?, ana saaken/sakna fi
maniila, ana men el-filibbiin, enta gayy mneen?, ana mesaafer bokra, el-esbooʿ
el-gayy…). Everything the lessons taught that the app already had (17 phrases, from
sabah en-noor to maʿlesh to enta minein) was detected and skipped, and every new card
follows the app's m/f side-by-side convention. Also fixed: the Arabizi grader now
reads ʿ-style marks as the Arabizi 3, so alternate answers written in transliteration
(like ʿan eznak) grade correctly — verified across all 1,639 items.*

*Earlier (v2.3.0 · 7/30/2026): **Stats overhaul.** The Whole-app ring is now
**mastery-weighted** — every item contributes its current mastery run (unlearned = 0),
so the percentage climbs with every correct answer instead of only when an item
crosses 90%. New **Progress by category** card for Vocabulary / Conversations / Verbs:
learned count + %, a stacked bar of the entire category colored by mastery tier (grey
for unlearned), per-tier counts with percentages, and each category's own
mastery-weighted %. **Progress by level** is regrouped under those three category
headings, shows learned n/total plus each level's tier-colored mastery %, and now
counts your own added cards (all stats do).*

*Earlier (v2.2.0 · 7/30/2026): a big one — **corrections that actually stick,
Arabizi everywhere, and a new Verbs category.*

*The bug behind disappearing edits is fixed at the root. Voice recordings were being
base64'd into the same localStorage blob as your progress; once that blob crossed the
browser's ~5 MB cap, **every save threw an error that the app caught and ignored**, so
corrections looked saved but were silently discarded. Recordings have moved to
**IndexedDB** (migrated automatically on first launch), the state blob stays small, and
storage failures are now surfaced in the Backup panel. Two smaller causes are fixed
too: lessons and quizzes froze their card list when the session started, so mid-session
edits never showed — every card is now re-resolved live at render time — and Custom
Quiz and "Quiz all learned words" were reading the original data instead of your edited
version.*

*New: **Arabizi / Franco-Arabic on all 1,639 items** (3 = ع, 7 = ح, 5 = خ, 2 = glottal
stop), generated from each card so it follows your corrections; a **🔤 Arabizi answer
mode** in every quiz and an Arabic/Arabizi toggle in the try-typing boxes, with
forgiving grading that accepts any common Franco spelling; Arabizi search in Items.
**⚡ Verbs** — 30 core Egyptian verbs, each with **three example sentences** (90 new
sentences, filed under Conversations: Verbs in Action) that you can learn straight from
the verb's page and that then flow into your normal reviews. **Backups now carry your
corrections and your recordings**, with a separate 🎤 Voice-only export/restore. And you
can **build a custom quiz from your audio** — studio recordings, your own voice, or
both. Cards also gained an editable Arabizi field and an ↺ Reset to original button.*

*Earlier (v2.1.0 · 7/27/2026): **grouped Vocabulary vs Conversations
everywhere** — the Lessons menu now has clear "Vocabulary" and "Conversations"
sections, and the Items filter is reorganized into an All chip, a **Vocabulary row**
(all vocabulary + Lv 1–79) and a **Conversations row** with each category by name
(no more "Lv 80"). Plus, tapping **Learn new** in a Conversation category now jumps
straight into the first item — no intermediate menu.*

*Earlier (v2.0.1 · 7/27/2026): **Conversations now lives inside Lessons** —
the Lessons menu has a "🗣 Conversation lessons" card (the Home shortcut is gone).
Each conversation category gained a **"View all items"** button that jumps straight
to the Items list filtered to that category — every conversation line shows there
with its mastery tier & %, sound button, ★, 🎙/🎤 marks, and tap-to-edit detail,
exactly like vocabulary. Items also gained a **🗣 Conv filter chip** to browse all
400 conversation lines at once.*

*Earlier (v2.0.0 · 7/25/2026): a huge one. **Conversations** — a new
always-unlocked section (Home → 🗣 Conversations) with four themed categories of 100
real exchanges each (Greetings & Small Talk, Meeting New People, Restaurant & Café,
Shopping & Bargaining; 400 new items, 1,024 → 1,424), learned and reviewed with the
exact same SRS, mastery tiers, audio, recording, and stats as everything else.
**Choose which voice plays** — on any word with an own-voice recording, pick
"Original" or "My voice" and the app plays your choice everywhere (no repo changes;
the GitHub-commit feature was removed). **Edit any item** — ✎ Edit on the detail page
corrects Arabic/transliteration/English app-wide, saved with your data. **Reorder
items** — a reorder mode in Items moves items up/down within their level to set your
learning priority (lessons follow your order). **Add cards to any level** — the
add-card form now has a level picker, including Conversation categories. Audio for
the new items: batches 31–47.*

*Earlier (v1.7.0 · 7/25/2026): **make your own recording the official audio,
straight from the app** — after recording your voice on a word, a "⬆ Make official"
button converts it to MP3 in the browser and commits it to `audio/<id>.mp3` in the
GitHub repo (updating the audio manifest too), replacing the pushed file. Needs a
fine-grained GitHub token pasted once into Home → settings; the token stays on the
device and is never included in backups.*

*Earlier (v1.6.1 · 7/25/2026): every word's detail page now shows its **exact
audio filename** (e.g. `audio/shokran.mp3`), so replacing an individual recording
with a better one is a simple overwrite-and-push.*

*Earlier (v1.6.0 · 7/25/2026): **record your own pronunciation** — a 🎤
recorder on every word's detail page saves your voice beside the original audio,
marks the word with 🎤 in Items, and rides along in backup export/import.*

*Earlier (v1.5.1 · 7/25/2026): the footer's "App updated" line now shows the
release date only — the exact time of the newest push (app or audio) comes from the
live GitHub line beneath it, which is always accurate.*

*Earlier today (v1.5.0 · 7/25/2026): **146 feminine forms added** —
every gendered item now exists in both masculine and feminine, placed side by side
(878 → 1,024 items). Existing progress, custom quizzes, and audio are untouched; the
new words get audio via five new batch files (batch_26–30) using the same routine.*

*Earlier (v1.4.2): 🎙 marks on words with recorded audio, via an auto-generated
audio manifest.*

*Earlier (v1.4.0): recorded-audio support (`audio/<id>.mp3` with automatic fallback),
word list exports, and audio-generation tooling.*

*Earlier (v1.3.0): Masri pronunciation engine (fully vocalized Egyptian respelling
for speech) and an Arabic voice picker with test button.*

*Earlier (v1.2.0): instant level unlock once a level is fully learned; starring an
item instantly unlocks it; "Add to custom quiz by mastery level" panel.*

*Earlier (v1.1.0): mastery became your run of consecutive correct answers (100 in a
row = full mastery) with five color-coded tiers; every quiz shows a bold green
**CORRECT**; Stats gained a mastery breakdown and a navigable full-month activity
calendar; and learning anything now comes with a 🧠 Universal Memory hook.*

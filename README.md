# Masri SRS 🌙

A web app for learning **Egyptian Arabic (Masri)** — spaced-repetition vocabulary,
typed-Arabic quizzes, a full alphabet trainer, and a progress dashboard. The whole
thing is a single self-contained HTML file you can run anywhere or install to your
home screen.

🔗 **Live app:** https://pawsncode.github.io/masri-srs/

## Features

### Vocabulary (WaniKani-style)
- **878 items across 79 levels** — words, phrases, and full sentences, grouped by
  theme and difficulty (greetings → grammar → daily life → dialogues → slang).
- **Level gating** — a level unlocks only after you reach **Guru** on 90% of the
  previous level, so you master each step before moving on.
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

### Reviews hub
- Choose **what** to review: **letters (script), words, phrases, sentences, or all
  vocabulary** — each with its own due count.
- **Trouble words** — anything you miss twice in a row is flagged and can be
  drilled on its own.
- **Pick your own** — select specific words (Items) or letters (Script) to quiz.
- **Custom quiz** — tap the ★ on any word or letter to save it to a personal quiz
  you can run anytime; your picks persist across sessions. In Items the **Start custom
  quiz** button now sticks to the top of the list, so it's one tap away no matter how
  far you've scrolled.

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
- **Items** is a searchable dictionary (English / transliteration / Arabic) with a
  count for every level.
- **Stats** dashboard: % of the whole app and current level mastered, words
  learned/mastered/burned, a review pipeline (due now / 24h / 7 days), a **mastery
  breakdown** counting how many of everything you've started sit in each tier
  (Learning / Shaky / Familiar / Strong / Mastered), a 14-day "new words" graph, a
  14-day activity graph, a **full-month activity calendar** you can page through
  month by month — each day shaded greener the more you studied, with today ringed —
  and per-level progress bars.
- **Themes** — six color themes (Rose, Violet, Bubblegum, Mint, Dark, Midnight),
  chosen at the bottom of the Home screen.
- **Audio** — tap-to-hear pronunciation via the browser's Arabic voice.
- **App icon** — a rose-gradient ʿain (ع) with a crescent moon, used as the
  favicon and home-screen icon.
- **Backup & restore** — from the Home settings you can export all your progress
  (download a file, copy it, or show it as text) and import it back on any device,
  so your data is never stuck on one phone.
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
- Progress stored locally in your browser (localStorage)

---

*Last updated (v1.1.0 · 6/30/2026, 2:15 PM Manila): **mastery is now your run of
correct answers** — each correct answer across any quiz type adds 1%, a miss resets
to 0, and 100 in a row earns full mastery; items are color-coded into five tiers
(Learning / Shaky / Familiar / Strong / Mastered). Every quiz and review now shows a
bold green **CORRECT** (and highlights the right answer green, wrong picks red).
Stats gains a **mastery breakdown** and a navigable **full-month activity calendar**.
And learning anything — letters, marks, words, phrases, sentences — now comes with a
🧠 **Universal Memory hook** to make it stick.*

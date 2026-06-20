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
  Burned, resurfacing right before you'd forget it.
- **Half-back on a miss** — get a review wrong and the item loses **half its
  progress** (e.g. correct three times then wrong once drops it from ~44% back to
  ~22% mastery), then comes due again soon. Honest mistakes cost you, so you really
  learn it.
- **Mastery colors** — every word in the Items list shows its state at a glance:
  **green = solid** (never missed), **amber = improving** (missed before, recovering),
  **red = needs work** (missed twice), plus a live mastery % per item.
- **Lessons hub** — the Lessons tab opens to a small menu: **learn a batch of new
  words** (3/5/7/10, your choice) and then quiz them to lock them in, **quiz all the
  words you've learned** in one shuffled drill, or **start a custom quiz** of words you
  hand-picked with the ★ in Items.
- **Word detail & letter breakdown** — tap any Arabic word in Items to open a detail
  page: the full word, romanization, English, sound, and a **letter-by-letter
  breakdown** showing the exact shape each letter takes in that word (isolated /
  initial / medial / final). Tap any letter to jump straight to its **trace guide and
  practice**, and there's a **try-typing box with a Check button** to test yourself.
- **Richer lessons** — when learning a new word you now see everything at once: the
  word, romanization, English, sound, the same tappable letter breakdown, and a
  type-it-yourself Check box — so you read it, hear it, see how it's built, and write
  it before moving on.
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
  color bar** (green = solid, amber = improving, red = needs work, grey = not started),
  plus an overall % per letter — so you can see at a glance exactly which shapes still
  need drilling.
- **Quiz** — match letters to sounds with live score, accuracy, and streaks.
- **Trace** — finger-trace letters over a soft ghost glyph on a 2×2 grid, with
  written stroke-order steps, plus a write-from-memory quiz mode.

### Dictionary, stats & looks
- **Items** is a searchable dictionary (English / transliteration / Arabic) with a
  count for every level.
- **Stats** dashboard: % of the whole app and current level mastered, words
  learned/mastered/burned, a review pipeline (due now / 24h / 7 days), a 14-day
  "new words" graph, a 14-day activity graph, an 8-week activity calendar heatmap,
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

## How to use

- Open the live link above, or download `index.html` and open it in any browser.
- **On iPhone:** open the link in Safari → **Share** → **Add to Home Screen** for a
  full-screen, app-like icon.
- After updating the site, you can append `?v=2` to the URL in Safari to bypass the
  cache, or re-add the home-screen icon to refresh it.

## Built with

- A single HTML file using React 18.3.1 + Babel Standalone 7.26.4, pinned and loaded from the jsDelivr CDN
- Pronunciation via the browser's Web Speech API (uses your device's Arabic voice)
- Progress stored locally in your browser (localStorage)

---

*Last updated: you can now focus the script on one positional shape — a new All / Iso / Init / Med / Fin filter on the script quiz menu aims every review, drill and custom quiz at just that form, and the trace guide has the same filter so you can practice tracing a single shape (initials only, medials only, etc.). One-way letters with no initial/medial form are skipped automatically.*

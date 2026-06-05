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
- **Learning phase** — learn a batch of new words (3/5/7/10, your choice), then a
  quiz on that batch locks them in.
- **Typed-Arabic reviews** — read the English, type the Arabic using the built-in
  on-screen Arabic keyboard or your device keyboard. Grading is forgiving about
  short vowels and alef/hamza spelling.

### Reviews hub
- Choose **what** to review: **letters (script), words, phrases, sentences, or all
  vocabulary** — each with its own due count.
- **Trouble words** — anything you miss twice in a row is flagged and can be
  drilled on its own.
- **Pick your own** — select specific words (Items) or letters (Script) to quiz.
- **Custom quiz** — tap the ★ on any word or letter to save it to a personal quiz
  you can run anytime; your picks persist across sessions.

### Script / alphabet
- **Train** — learn letters in batches with real **SRS scheduling** and due-based
  letter reviews; two quiz styles: *see letter → pick sound* and *hear sound →
  type the letter*; streaks and trouble-letter tracking.
- **Chart** — the full 28-letter reference with a pronunciation key, the four
  positional forms, and stroke-order guides.
- **Quiz** — match letters to sounds with live score, accuracy, and streaks.
- **Trace** — finger-trace letters over a guide with a "start" dot, plus a
  write-from-memory quiz mode.

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
- **Progress saves on your device** and the app installs to your home screen.

## How to use

- Open the live link above, or download `index.html` and open it in any browser.
- **On iPhone:** open the link in Safari → **Share** → **Add to Home Screen** for a
  full-screen, app-like icon.
- After updating the site, you can append `?v=2` to the URL in Safari to bypass the
  cache, or re-add the home-screen icon to refresh it.

## Built with

- A single HTML file using React + Babel (loaded from a CDN)
- Pronunciation via the browser's Web Speech API (uses your device's Arabic voice)
- Progress stored locally in your browser (localStorage)

---

*Last updated: 878 items / 79 levels — added the everyday conversational layer (terms of endearment like حبيبي/حبيبتي, reactions & slang, filler words, catching-up greetings, love & affection, common phrases, agreeing/declining, exclamations, compliments, and spoken commands).*

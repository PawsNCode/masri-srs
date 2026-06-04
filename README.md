# Masri SRS 🌙

A small web app for learning **Egyptian Arabic (Masri)** — spaced-repetition
flashcards, an alphabet quiz, and a handwriting trainer. The whole thing is a
single self-contained HTML file.

🔗 **Live app:** https://pawsncode.github.io/masri-srs/

## Features

- **Spaced-repetition flashcards** (SM-2 scheduling) for high-frequency Egyptian
  Arabic — each card shows the Arabic script, transliteration, English meaning,
  and tap-to-hear audio.
- **Script reference** — the full 28-letter alphabet with a pronunciation key,
  the four positional letter forms, and stroke-order guides.
- **Alphabet quiz** — match letters to sounds, with live score, accuracy, and streaks.
- **Handwriting trainer** — trace letters with your finger over a guide and a
  "start" dot, plus a Quiz mode that asks you to write a letter from memory.
- **Progress saves on your device** and the app installs to your home screen.

## How to use

- Open the live link above, or download `index.html` and open it in any browser.
- **On iPhone:** open the link in Safari → **Share** → **Add to Home Screen**
  for a full-screen, app-like icon.

## Built with

- A single HTML file using React + Babel (loaded from a CDN)
- Pronunciation via the browser's Web Speech API (uses your device's Arabic voice)
- Progress

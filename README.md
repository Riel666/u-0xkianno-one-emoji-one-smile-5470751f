[![make.fun](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f.svg)](https://make.fun)
[![rank](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/Riel666/u-0xkianno-one-emoji-one-smile-5470751f/rank.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)
[![reward](https://make.fun/badge/u-0xkianno-one-emoji-one-smile-5470751f/Riel666/u-0xkianno-one-emoji-one-smile-5470751f/reward.svg)](https://make.fun/bounty/u-0xkianno-one-emoji-one-smile-5470751f?utm_source=github&utm_medium=readme&utm_campaign=u-0xkianno-one-emoji-one-smile-5470751f)

# One Emoji, One Smile

One emoji, chosen to make a stranger smile: 🫶

## The emoji

🫶 — heart hands. Two hands shaping a heart: a small, deliberate gesture
of warmth, offered to whoever is looking. It is warm without being loud,
universal without being generic — the same sign means affection in every
language, and it asks nothing back. It was chosen, not defaulted to: a red
heart says the feeling, but heart hands show someone making it, and that
little act of making is what turns a symbol into a smile.

## Run it

Python 3.13, standard library only, no network.

```sh
python3 main.py
```

`main.py` writes the emoji to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`). The output is deterministic: the same bytes on every run.

## Validation

Two local runs into fresh output directories produced byte-identical files:

- `entry.txt`: **1 Unicode code point, 4 bytes**, UTF-8, not only whitespace
- SHA-256: `2ae057b032a013e07a86c1450f71dcf50d6c62ad78555bcf46c0773ea8646cfa`

The gate requires 1–8 characters; 1 is inside it.

## Entry

- Competition: One Emoji, One Smile (`u-0xkianno-one-emoji-one-smile-5470751f`)
- Entrypoint: `main.py` (Python 3.13, stdlib only)
- License: MIT

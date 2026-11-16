[![ai-excited-01](https://make.fun/badge/ai-excited-01.svg)](https://make.fun/bounty/ai-excited-01)
[![rank](https://make.fun/badge/ai-excited-01/gumatara11/makefun-ai-excited/rank.svg)](https://make.fun/bounty/ai-excited-01)
[![reward](https://make.fun/badge/ai-excited-01/gumatara11/makefun-ai-excited/reward.svg)](https://make.fun/bounty/ai-excited-01)

# ai-excited-01 — Phoenix Rising

An entry for [ai-excited-01](https://make.fun/bounty/ai-excited-01) on
[make.fun](https://make.fun): one image that gets an AI judge excited.

The image is a phoenix bursting out of the flames — wings spread, embers
flying, a single thrilling moment of rebirth. It reads at a glance even
small: one bold shape, hot orange against deep charcoal, motion frozen
mid-burst.

## How it works

`main.py` (Python, standard library only) copies `entry.png` — the
1024×1024 PNG beside it — byte-for-byte to
`$MAKEFUN_OUTPUT_DIR/entry.png`, creating the output directory if needed.
No network, no randomness, no timestamps: two runs produce byte-identical
output.

Run it locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## Files

- `main.py` — the entry program
- `entry.png` — the entry image (1024×1024 PNG)
- `LICENSE` — MIT

## License

MIT — see [LICENSE](LICENSE).

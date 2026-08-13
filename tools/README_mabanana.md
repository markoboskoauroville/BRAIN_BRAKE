# mabanana, Nano Banana Pro straight from Termux

## Why

`imgtoimg.ai` serves Google's `gemini-3-pro-image`. Going direct removes the daily
quota, costs about $0.134 an image, and above all **gives a real error instead of a
silent stall at 95%**.

The 95% stall on 13.8.2026 cost two credits and an hour of guessing. Direct, the same
failure prints `BLOCKED BEFORE GENERATING: SAFETY` and the exact category. That alone
is the reason to switch.

**Going direct does not remove the filter.** Same model, same Google, same rules. What
changes is that you find out immediately what tripped, and can rewrite the one sentence
that did it instead of rewriting the whole prompt blind.

## Setup, once

    pkg install python
    curl -o $PREFIX/bin/mabanana https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/tools/mabanana
    chmod +x $PREFIX/bin/mabanana
    echo YOUR_KEY > ~/.mabanana_key && chmod 600 ~/.mabanana_key

Free key at https://aistudio.google.com/apikey

## Use

    mabanana "a photograph of ..." -r MANAN_DESK.jpg -o 4_4_phone

    mabanana -f prompt.txt \
      -r https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/REFERENCES/MANAN_DESK.jpg \
      -a 16:9 -s 2K -o 7_3_white

References take local paths or raw GitHub URLs, so every prompt already written for
this film works unchanged. Output lands in `~/mabanana` and the path is printed on
stdout, so it pipes.

## Costs on this film

1K and 2K are the same price, so 2K is the default. The whole remaining film is
somewhere between five and eight dollars.

| | |
|---|---|
| $0.134 | one 1K or 2K image, Standard |
| $0.24 | one 4K image, Standard |
| half that | Batch and Flex, if 24 hours is acceptable |

## What it does not do

No queue, no gallery, no Android UI. That is on purpose. Finish the film first.

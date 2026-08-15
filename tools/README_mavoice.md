# mavoice, Hume Octave voices for the film

## Getting the key, five steps

1. Go to **https://app.hume.ai** and sign in or create an account.
   Not `hume.ai`, not `beta.hume.ai`. The portal is `app.hume.ai`.
2. Left sidebar, click **API keys**, or go straight to **https://app.hume.ai/keys**
3. You will see an **API key** and a **Secret key**. Only the API key is needed.
4. Copy it. No card, no billing setup. The free tier is live immediately.
5. `echo YOUR_KEY > ~/.mavoice_key && chmod 600 ~/.mavoice_key`

## The trap

**Octave 2 does not support acting instructions yet.** Hume's own version table lists
them as coming soon. Acting instructions are the entire reason we chose Hume, so this
tool sends `"version": "1"` and uses Octave 1.

If a reading comes back flat, check that first.

## Use

    mavoice --list                     what voices this account can use
    mavoice --test                     one Coach Brain line in three voices, pick one
    mavoice --script assets/voice/lines_characters.json
    mavoice --say "One line." --desc "warm, amused" --voice "Ava Song"

WAVs land in `~/mavoice`.

## What matters

**The acting instruction does the work, not the text.** Octave reads the instruction
and performs accordingly. `"Warm, amused, entirely unembarrassed. A teacher pleased to
have been found."` produces a completely different reading from the same words with no
instruction. Write the direction the way you would say it to an actor.

**One WAV per line, never one long file.** Every line gets cut to picture separately,
and a single long render cannot be retimed.

**Endpoint.** `POST /v0/tts/file` returns the audio file directly. `format: {"type":"wav"}`.
Supported formats are MP3, WAV and PCM. Maximum 5,000 characters per utterance.

## What we actually need

Only the characters are synthesised. **Manan speaks in his own voice**, recorded on the
shooting day, for everything he says and for the narration. That is the point of the
film and it is what the competition is judging.

The synthetic voices are Coach Brain, four lines, and the factory worker, one line.
Roughly 300 characters in total for the whole film, against 10,000 free a month.

# THE VOICES

Everything needed to record new character lines exactly as the existing ones.

## THE ACCOUNT

Hume AI, Octave. Key at `~/.hume_key`. Free tier gives 10,000 characters a month. The whole film's
synthetic dialogue is about 300 characters, so cost is not a constraint.

Helper: `tools/hume_helper.py` (same as `gen/hv.py` in the working directory).

## TWO THINGS THAT WILL WASTE AN HOUR IF FORGOTTEN

**1. Cloudflare blocks the default Python user agent.** Every endpoint, including auth, returns
`403  error code: 1010` with a bare body and no JSON. It looks exactly like a dead API key. Send a
normal browser User-Agent and it works immediately. Without a key the same request returns a proper
`401` with a JSON message, which is how you tell a real auth failure from this.

**2. Use Octave version 1.** Set `"version": "1"` in the payload. Octave 2 does not support acting
instructions yet, and the acting instruction is the entire reason for using Hume.

## THE CAST, LOCKED

| character | voice name | provider | notes |
|---|---|---|---|
| **COACH BRAIN** | `Male English Actor` | HUME_AI | British RP. Warm teacher. Never sly, never a villain. |
| **FACTORY WORKER** | `Classical Film Actor` | HUME_AI | American. Flat, resigned, end of a shift. |
| **MANAN** | none | — | **He records himself.** Hume refuses to synthesise child voices. |

The contrast is deliberate: a British teacher against an American working man. You know instantly
they are different people from different worlds, and it quietly reinforces that Coach Brain is the
explanation while the factory is the old theory.

## MANAN IS NEVER SYNTHESISED

Asking for a fourteen year old returns
`400  Sorry, we detected a request for a child voice, which violates our acceptable use policy.`

This is the right outcome. He speaks every one of his own lines and all the narration himself,
recorded on the day. It is what the competition is judging.

## HOW TO RECORD A NEW LINE

```python
import sys; sys.path.insert(0, '/home/claude/gen')
from hv import say

say("The line exactly as written in the script.",
    "COACH_4_6",                       # becomes COACH_4_6.wav in /home/claude/voice
    voice="Male English Actor",
    desc="the acting instruction, written the way you would say it to an actor")
```

## THE ACTING INSTRUCTION DOES THE WORK

Octave reads the direction and performs it. The same sentence with and without a direction produces
completely different readings. This is why Hume and not a cheaper engine.

Write it as direction, not as adjectives. What the character wants, how they feel, where to slow
down. Examples that produced the takes now in the film:

- **4.1** "A warm, generous teacher. Amused, entirely unembarrassed, never sly and never a villain.
  He is pleased to have been found. Delighted, a little teasing, as if he has been waiting a long
  time. Ends with a small chuckle."
- **4.3a** "Brisk and practical, ticking five things off. Even rhythm, no drama, slight lift on the
  last one."
- **4.3b** "Slowing right down. Direct and quiet, looking straight at the boy. The question is
  genuine, not rhetorical."
- **4.6** "A warm, generous teacher. Kind and completely without apology, explaining something he
  considers obvious, with affection. Quiet and slow on the last three words."
- **6.1** "Quiet, deciding out loud. A small generous choice. Slight smile, unhurried."
- **2.4 worker** "A tired factory worker at the end of a long shift. Flat, resigned, matter of fact.
  Not frightened and not dramatic, just finished. American accent."

The gear change between 4.3a and 4.3b is the clearest proof the directions are working: the same
voice ticks off five sensors like a machine, then becomes a person asking something real.

## AFTER RECORDING, ALWAYS

**Retime the frame from the measured audio, never from a word count estimate.** Word counts were out
by more than two seconds on one line, which forced a rewrite. Measure it:

```python
import wave, contextlib
with contextlib.closing(wave.open(path)) as w:
    frames_at_25fps = round(w.getnframes() / w.getframerate() * 25)
```

Then set `fr = frames_at_25fps + hold` in `assets/train/frames_v4.json`, mark the frame
`"measured": true`, re-run the timings, and **rebuild all eight scene packages**, because changing one
line moves every timecode after it.

Then check the total is still under 2:00. It is a hard competition limit.

## THE RECORDED FILES

All in `assets/voice/tests/`, copied into the scene packages by the build.

| file | frame | who |
|---|---|---|
| `BUB_4_1.wav` | 4.1 | Coach Brain |
| `BUB_4_3a.wav` | 4.3 | Coach Brain |
| `BUB_4_3b.wav` | 4.4 | Coach Brain |
| `COACH_4_6.wav` | 4.6 | Coach Brain |
| `COACH_6_1.wav` | 6.1 | Coach Brain |
| `WORKER_2_4.wav` | 2.4 | Factory worker |

48 kHz mono WAV, one file per line, never one long render. A single long file cannot be retimed.

`assets/voice/lines_characters.json` holds every line with its voice, direction and filename.

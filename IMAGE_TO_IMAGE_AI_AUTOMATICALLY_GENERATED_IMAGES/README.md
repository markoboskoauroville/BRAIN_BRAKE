# IMAGE_TO_IMAGE_AI_AUTOMATICALLY_GENERATED_IMAGES

**Where the automated Image to Image run puts what it makes, the moment it makes it.**

Created 2.9.2026, for the Hammerspoon driven batches. Nothing here is hand made and nothing here is
final.

---

## WHAT THIS FOLDER IS FOR

The automated run fills the form, waits, saves, and starts the next job. It must be able to put a
file down **immediately**, without asking anything, without deciding anything, and without waiting
for a person. This is that place.

**A delivery lands here under the exact filename from the batch file.** PNG, no rename, no suffix,
no subfolder per session. That is the whole contract.

---

## WHAT THIS FOLDER IS NOT

**It is not a second home for the originals.** There is one home and it is
`markoboskoauroville/BRAIN_BRAKE_ORIGINALS`: public, no Pages site, no 1 GB ceiling, raw links that
need no credential. On 2.9.2026 the project spent a long session pulling 160 originals out of two
places into that one, precisely so nobody would ever have to ask where a frame lives.

**So this folder is a doorstep, not a cupboard.** A file sits here between arriving and being filed.

**A frame is finished with this folder once it is in `BRAIN_BRAKE_ORIGINALS` and verified by
sha256.** Then it is removed from here. If files accumulate, something upstream stopped running and
that is worth saying out loud rather than letting the folder quietly become an archive.

---

## THE ORDER, AND THE ORDER IS THE POINT

    1  the run saves the delivery here under the batch filename
    2  somebody OPENS it, never judges it by its name, because a name records
       an intention and the content moves on
    3  a frame with gold in it is MEASURED, coloured pixels above 0.2 per cent.
       If the gold came back grey the prompt was wrong and the frame is
       regenerated. NEVER tint anything by hand
    4  it is pushed to BRAIN_BRAKE_ORIGINALS and verified by sha256 there
    5  ONLY THEN is it removed from here

**Never step 5 before step 4.** While a file is only here it is the only copy, and this repository
publishes nothing, so nothing else would notice it going missing.

---

## WHO WRITES WHAT

    the Hammerspoon run    saves here. Nothing else.
    the daemon             uploads and fills in drive_links.json, per STEP 86
    the chat session       owns catalog.json and the site

Three writers, three files, no overlap. That separation is why the sessions can run at the same time.

# THE STALE CACHE. 13.8.2026.

**A cache keyed on a file path serves the old file forever once you overwrite that path.**

This cost hours on this production and it cost trust, because Marko was right every single time he said
the document had not changed, and every single time he was told to refresh, clear his downloads, or wait
for a CDN. None of that was the problem. The problem was here.

---

## WHAT HAPPENED

The PDF builder passed every image through a helper that made a downscaled copy so the document stayed
small enough to send. The helper cached its output:

```python
# BROKEN
def small(p, maxdim=1400, q=78):
    h = hashlib.md5((p + str(maxdim)).encode()).hexdigest()[:12]
    o = f'{SD}/{h}.jpg'
    if not os.path.exists(o):
        ...build it...
    return o
```

The key is the **path**. Nothing else.

The workflow on this film is to regenerate a frame and write it back over the same filename, because
every document, every builder and every reference URL points at that name. So `V7_4_4_phone.jpg` was
replaced on disk with a completely different photograph, the path did not change, the cache hit, and the
PDF embedded the picture from an hour earlier.

Every rebuild after that silently re-embedded the stale copy. The build log said it had written a new
file. The file size even changed, because other things changed. Everything looked like it had worked.

**It hit exactly the frames that were fixed in place:** `4.4` the phone, `5.7` the wall, `2.1` the
blackboard. The frames that came out correct, `2.6` and `5.6`, were correct only by accident, because
those happened to be saved under new filenames.

---

## WHY IT WAS NOT CAUGHT FOR HOURS

Because the wrong thing was blamed, repeatedly, and each wrong explanation was plausible:

1. **"Your download is stale."** Reasonable, and false.
2. **"GitHub's raw CDN is caching."** Reasonable, and false. Renaming the file to `V2b` produced a new
   URL, a genuinely fresh download, and the same wrong picture, which should have ended that theory
   immediately and did not.
3. **"Your PDF viewer is caching."** Also false.

Every one of those put the fault on Marko's side. He said plainly, more than once, that the picture had
not changed. **He was reporting a measurement. It should have been treated as one.**

---

## THE RULE

**When somebody says the output did not change, verify the artefact, not their setup.**

Do not explain. Do not suggest a refresh. Open the file that was actually produced, extract the actual
bytes of the actual image, and compare them to the source. Two commands:

```python
# is the embedded picture the same as the source picture?
a = np.array(Image.open(cached_or_embedded).convert('L').resize((64,64))).astype(float)
b = np.array(Image.open(source).convert('L').resize((64,64))).astype(float)
print(np.abs(a-b).mean())        # near 0 means same image, 58 means a different one entirely
```

That check took under a minute and would have found this at the first complaint.

---

## THE FIX

Key the cache on **content identity**, never on name alone:

```python
# CORRECT
def small(p, maxdim=1400, q=78):
    st = os.stat(p)
    key = "%s|%d|%d|%d" % (p, st.st_size, int(st.st_mtime), maxdim)
    h = hashlib.md5(key.encode()).hexdigest()[:16]
    ...
```

Size and modification time both change when a frame is replaced, so overwriting a file always busts its
cache entry. An md5 of the file contents is stricter and also fine; size plus mtime is cheaper and
sufficient here.

---

## THE STANDING RULES THAT COME OUT OF THIS

**Any cache in any tool on this production keys on content, never on a name.** Paths on this film are
deliberately stable, so a name-keyed cache is guaranteed to go wrong eventually.

**After building a deliverable, download it back from where it was published and diff a page against
the local build.** Not the local file, the published one. This is three lines and it converts "it should
be fine" into "it is fine":

```bash
curl -sL -o /tmp/check.pdf "$RAW_URL"
pdftoppm -r 80 -png -f "$PAGE" -l "$PAGE" /tmp/check.pdf /tmp/dl
# then compare /tmp/dl-NN.png against the locally rendered page
```

**Bump the version letter on every rebuild.** `V2`, `V2b`, `V2c`. A new link means a new file and
nobody has to wonder which one they are holding. This does not fix caching, but it removes an entire
category of doubt.

**Never tell somebody their download is stale until the artefact has been checked.** The person looking
at the picture is the measurement. The build log is not.

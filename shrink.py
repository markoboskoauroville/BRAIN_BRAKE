import os, hashlib
from PIL import Image
SD='/home/claude/small'
os.makedirs(SD, exist_ok=True)
def small(p, maxdim=1400, q=78):
    st = os.stat(p)
    # key on path AND size AND mtime, so replacing a file at the same name busts the cache
    key = "%s|%d|%d|%d" % (p, st.st_size, int(st.st_mtime), maxdim)
    h = hashlib.md5(key.encode()).hexdigest()[:16]
    o = f'{SD}/{h}.jpg'
    if not os.path.exists(o):
        im = Image.open(p).convert('RGB')
        if max(im.size) > maxdim:
            im.thumbnail((maxdim, maxdim), Image.LANCZOS)
        im.save(o, quality=q, optimize=True)
    return o

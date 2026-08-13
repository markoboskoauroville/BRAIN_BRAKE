import os, hashlib
from PIL import Image
SD='/home/claude/small'
os.makedirs(SD, exist_ok=True)
def small(p, maxdim=1400, q=78):
    h=hashlib.md5((p+str(maxdim)).encode()).hexdigest()[:12]
    o=f'{SD}/{h}.jpg'
    if not os.path.exists(o):
        im=Image.open(p).convert('RGB')
        if max(im.size)>maxdim: im.thumbnail((maxdim,maxdim), Image.LANCZOS)
        im.save(o, quality=q, optimize=True)
    return o

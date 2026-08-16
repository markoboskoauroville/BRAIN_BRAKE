import base64, json, os, time, urllib.request, urllib.error
import os as _os
_CAND = [_os.path.expanduser('~/.gemini_key'), _os.path.expanduser('~/.mabanana_key'),
         '/home/claude/.gemini_key']
_K = _os.environ.get('GEMINI_API_KEY')
if not _K:
    for _p in _CAND:
        if _os.path.exists(_p):
            _K = open(_p).read().strip(); break
if not _K:
    raise SystemExit('no key: set $GEMINI_API_KEY or write one to ~/.gemini_key')
KEY = _K
URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image:generateContent"
OUT = _os.environ.get("NB_OUT") or _os.path.expanduser("~/gen")

def ref(src):
    if src.startswith("http"):
        with urllib.request.urlopen(src, timeout=90) as r:
            return {"inline_data": {"mime_type": "image/jpeg", "data": base64.b64encode(r.read()).decode()}}
    d = open(src, "rb").read()
    m = "image/png" if src.lower().endswith(".png") else "image/jpeg"
    return {"inline_data": {"mime_type": m, "data": base64.b64encode(d).decode()}}

def gen(prompt, refs=(), aspect="16:9", size="2K", name=None):
    parts = [ref(r) for r in refs] + [{"text": prompt}]
    body = json.dumps({"contents": [{"role": "user", "parts": parts}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"],
            "imageConfig": {"aspectRatio": aspect, "imageSize": size}}}).encode()
    req = urllib.request.Request(URL, data=body,
        headers={"Content-Type": "application/json", "x-goog-api-key": KEY})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=420) as r:
            res = json.load(r)
    except urllib.error.HTTPError as e:
        print("HTTP", e.code, e.read().decode()[:500]); return None
    pf = res.get("promptFeedback") or {}
    if pf.get("blockReason"):
        print("BLOCKED:", pf["blockReason"], pf.get("safetyRatings")); return None
    c = (res.get("candidates") or [{}])[0]
    fr = c.get("finishReason")
    for p in c.get("content", {}).get("parts", []):
        d = p.get("inline_data") or p.get("inlineData")
        if d:
            img = base64.b64decode(d["data"])
            path = os.path.join(OUT, (name or time.strftime("%H%M%S")) + ".png")
            open(path, "wb").write(img)
            tok = res.get("usageMetadata", {}).get("candidatesTokenCount", 0)
            print("OK %.0fs  %.0fKB  $%.3f  %s" % (time.time()-t0, len(img)/1024, tok/1e6*12, path))
            return path
    print("NO IMAGE  finishReason:", fr, c.get("safetyRatings"))
    return None

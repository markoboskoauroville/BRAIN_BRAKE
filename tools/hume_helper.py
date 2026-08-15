import json, os, time, urllib.request, urllib.error
KEY = open('/home/claude/.hume_key').read().strip()
UA  = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
H   = {"Content-Type":"application/json","X-Hume-Api-Key":KEY,"User-Agent":UA,"Accept":"*/*"}
OUT = "/home/claude/voice"; os.makedirs(OUT, exist_ok=True)

def voices(page=0):
    req=urllib.request.Request("https://api.hume.ai/v0/tts/voices?provider=HUME_AI&page_size=100&page_number=%d"%page, headers=H)
    with urllib.request.urlopen(req, timeout=60) as r: return json.load(r)

def say(text, name, desc=None, voice=None, speed=None, trailing=None, version="1"):
    utt = {"text": text}
    if voice: utt["voice"] = {"name": voice, "provider":"HUME_AI"}
    if desc:  utt["description"] = desc
    if speed is not None: utt["speed"]=speed
    if trailing is not None: utt["trailing_silence"]=trailing
    p = {"utterances":[utt], "format":{"type":"wav"}, "num_generations":1}
    if not voice: p["instant_mode"]=False
    if version: p["version"]=version
    req=urllib.request.Request("https://api.hume.ai/v0/tts/file", data=json.dumps(p).encode(), headers=H)
    t0=time.time()
    try:
        with urllib.request.urlopen(req, timeout=300) as r: b=r.read()
    except urllib.error.HTTPError as e:
        print("  FAIL %s  HTTP %s  %s" % (name, e.code, e.read().decode('utf8','replace')[:200].replace('\n',' ')))
        return None
    path=os.path.join(OUT, name+".wav"); open(path,"wb").write(b)
    print("  OK  %-22s %5.0fs %6.0f KB" % (name, time.time()-t0, len(b)/1024))
    return path

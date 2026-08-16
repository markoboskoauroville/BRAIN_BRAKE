#!/usr/bin/env python3
"""Rebuild the animator's scene packages and the animation site cards.

WHY THIS EXISTS
Kristijan works from animation/downloads/SCENE_xx_*.zip. Each zip carries every
frame of that scene at full size, the character audio, a TIMECODE.csv and an
INFO.txt with the lines and the transition notes. All of that is derived from
assets/train/frames_v4.json.

Before this script existed the packages were built by hand in a chat working
directory, so when the film changed they silently went stale and the animator
could have worked to timecodes that no longer existed. Never build these by
hand again. Run this.

USAGE
    python3 25-lines-manan.py      # Manan's lines, for the acting guide
    python3 27-scene-packages.py   # this file: zips + the site cards

The script also rewrites the download cards in animation/index.html so the
frame counts, durations and file sizes on the page always match the zips.
"""
import json, os, csv, io, zipfile, shutil, re, sys

sys.path.insert(0, '/home/claude')
from tc import tc, FPS

REPO = os.path.dirname(os.path.abspath(__file__))
FRAMES = os.path.join(REPO, 'assets/train/frames_v4.json')
IMGDIRS = [os.path.join(REPO, 'assets/V7'), os.path.join(REPO, 'assets/V3A'),
           os.path.join(REPO, 'assets/V6/panels'), '/home/claude/train/img']
VOICE = os.path.join(REPO, 'assets/voice/final')
OUT = os.path.join(REPO, 'animation/downloads')
INDEX = os.path.join(REPO, 'animation/index.html')

# Scene folder names. These are also the zip names and they are linked from the
# site, so do not rename one without rewriting index.html in the same commit.
SCENES = {
 1: "THE_MYSTERY", 2: "THE_OLD_THEORY", 3: "THE_FULL_TANK", 4: "THE_GATEKEEPER",
 5: "THE_EXPERIMENT", 6: "THE_RELEASE", 7: "THE_VERDICT", 8: "THE_INVITATION",
}

# Which recorded take belongs to which frame. This map is the authority. If it
# and assets/voice/final ever disagree, the map is right and something moved.
AUD = {
 "2.4": "WORKER_2_4.wav", "4.1": "BUB_4_1.wav", "4.3": "BUB_4_3a.wav",
 "4.4": "BUB_4_3b.wav", "4.6": "COACH_4_6.wav", "6.1": "COACH_6_1.wav",
}


def find_img(fn):
    for d in IMGDIRS:
        p = os.path.join(d, fn)
        if os.path.exists(p):
            return p
    return None


def build():
    frames = json.load(open(FRAMES))
    total = sum(f['fr'] for f in frames)
    os.makedirs(OUT, exist_ok=True)
    cards, missing = [], []

    for sc in sorted(SCENES):
        name = "SCENE_%02d_%s" % (sc, SCENES[sc])
        rows = [f for f in frames if f['scene'] == sc]
        if not rows:
            continue
        zpath = os.path.join(OUT, name + ".zip")
        first, last = rows[0], rows[-1]

        # ---- timecode csv
        sio = io.StringIO()
        w = csv.writer(sio, lineterminator="\r\n")
        w.writerow(["frame", "layer", "in", "out", "frames", "timing",
                    "mode", "who", "line", "note"])
        for f in rows:
            w.writerow([f['id'], f['layer'], tc(f['in'] / float(FPS)),
                        tc(f['out'] / float(FPS)), f['fr'],
                        "measured" if f['measured'] else "estimated",
                        f['mode'], f['who'], f['text'], f['trans']])

        # ---- info txt
        info = [name, "",
                "IN %s   OUT %s   %s   %d frames"
                % (tc(first['in'] / float(FPS)), tc(last['out'] / float(FPS)),
                   tc((last['out'] - first['in']) / float(FPS)),
                   last['out'] - first['in']),
                ""]
        for f in rows:
            info.append("%-5s %s - %s  %3d fr  %s%s"
                        % (f['id'], tc(f['in'] / float(FPS)), tc(f['out'] / float(FPS)),
                           f['fr'], f['layer'],
                           "" if f['measured'] else "   (timing estimated, will move)"))
            if f['text'].strip():
                info.append('      %s: "%s"' % (f['who'], f['text']))
            if f['trans'].strip():
                info.append("      NOTE: " + f['trans'])
        info += ["", "TIMING",
                 "Frames marked estimated are timed from a word count and will move once",
                 "Manan's narration is recorded. Frames marked measured are cut to a real",
                 "take and will not move. The film is %s and must never grow past 2:00." % tc(total / float(FPS)),
                 "", "PLATES",
                 "A frame listed here with no image in FRAMES is shot on the day and does",
                 "not exist yet. It is in the package so the timing is complete."]

        with zipfile.ZipFile(zpath, 'w', zipfile.ZIP_DEFLATED) as z:
            z.writestr(name + "/FRAMES/", "")
            z.writestr(name + "/AUDIO/", "")
            for f in rows:
                p = find_img(f['img'])
                if p:
                    z.write(p, "%s/FRAMES/%s_%s.jpg" % (name, name, f['id'].replace('.', '_')))
                else:
                    missing.append("%s  %s" % (f['id'], f['img']))
                a = AUD.get(f['id'])
                if a and os.path.exists(os.path.join(VOICE, a)):
                    z.write(os.path.join(VOICE, a), "%s/AUDIO/%s" % (name, a))
            z.writestr("%s/%s_TIMECODE.csv" % (name, name), sio.getvalue())
            z.writestr("%s/%s_INFO.txt" % (name, name), "\n".join(info) + "\n")

        nframes = len(rows)
        dur = tc((last['out'] - first['in']) / float(FPS))[3:]
        mb = os.path.getsize(zpath) / 1048576.0
        cards.append((sc, SCENES[sc].replace("_", " "), nframes, dur, mb))
        print("%-28s %2d frames  %s  %5.1f MB" % (name, nframes, dur, mb))

    # ---- rewrite the download cards on the site
    html = open(INDEX).read()
    block = "".join(
        '<article>\n  <div class="sc">\n    <span class="num">%02d</span>\n    <div>\n'
        '      <h3>%s</h3>\n      <div class="meta">%d frames &middot; %s &middot; %.1f MB</div>\n'
        '    </div>\n    <a class="dl" href="downloads/SCENE_%02d_%s.zip" download>download</a>\n'
        '  </div>\n</article>' % (sc, nm, nf, du, mb, sc, SCENES[sc])
        for sc, nm, nf, du, mb in cards)
    new, n = re.subn(r'<article>\s*<div class="sc">.*?</article>(?=\s*(<h2|<footer|</main|<article>))',
                     '', html, flags=re.S)
    html = re.sub(r'(<h2 id="downloads">.*?</p>)', lambda m: m.group(1) + "\n" + block, new, flags=re.S)
    html = re.sub(r'1:5\d with [\d.]+ seconds of margin',
                  '%s with %.1f seconds of margin' % (tc(total / float(FPS))[3:8].lstrip('0'),
                                                      (3000 - total) / 25.0), html)
    open(INDEX, 'w').write(html)

    # The layer example is not a scene and is not derived from frames_v4.json,
    # so the card rewrite above deletes it. Put it back.
    LAYER = ('<article><div class="sc"><span class="num">&mdash;</span>\n'
             '<div><h3>Layer example, one frame</h3>\n'
             '<div class="meta">background, characters, bubble, voice, preview</div></div>\n'
             '<a class="dl" href="downloads/LAYER_EXAMPLE_ONE_FRAME.zip" download>download</a>'
             '</div></article>\n')
    html = open(INDEX).read()
    if 'LAYER_EXAMPLE_ONE_FRAME.zip' not in html:
        html = html.replace(block, block + LAYER, 1)
        open(INDEX, 'w').write(html)

    print("\ntotal %d frames, %s, margin %.2f s" % (len(frames), tc(total / float(FPS)),
                                                    (3000 - total) / 25.0))
    if missing:
        print("\nFRAMES WITH NO PLATE YET (shot on the day, listed for timing only):")
        for m in missing:
            print("   " + m)


if __name__ == '__main__':
    build()

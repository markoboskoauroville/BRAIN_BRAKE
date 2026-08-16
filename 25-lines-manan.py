#!/usr/bin/env python3
"""Derive assets/train/lines_manan.json from frames_v4.json.

Manan's acting guide builds from this file. This file builds from the film.
So his lines can never drift from the film's lines. Run this after any change
to frames_v4.json and before rebuilding the guide.
"""
import json, os

REPO = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(REPO, 'assets/train/frames_v4.json')
DST = os.path.join(REPO, 'assets/train/lines_manan.json')

frames = json.load(open(SRC))
lines = [
    {'scene': f['scene'], 'id': f['id'], 'mode': f['mode'], 'text': f['text']}
    for f in frames
    if f['who'] == 'MANAN' and f['text'].strip()
]
json.dump(lines, open(DST, 'w'), indent=1, ensure_ascii=False)
print('wrote %s  %d lines for Manan' % (DST, len(lines)))

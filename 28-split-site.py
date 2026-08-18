#!/usr/bin/env python3
"""Split the single page production site into one folder per section.

WHY THIS EXISTS
The site was one HTML file with JavaScript tabs. Everything lived at one URL, so
a screen reader or a read aloud tool like Speechify could only ever reach the
first pane. Marko reads this site by pasting a link into Speechify, so every
section now has its own folder, its own index.html and its own URL.

    /                     the hub, every link on one page
    /overview/            one folder per tab
    /script/
    /board/
    ...
    /marko/director/      the four sub tabs get their own folders too

Nothing is rewritten by hand. This reads index.html, lifts each section out with
its head and styles intact, fixes the asset paths for the extra folder depth,
and writes the lot. Run it again after any change to index.html.

    python3 28-split-site.py
"""
import os, re, shutil, sys

REPO = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(REPO, 'index.html')

TABS = [('overview', 'Overview', 'Where the film stands, in one page'),
        ('script', 'The Film', 'The script, scene by scene'),
        ('board', 'Storyboard', 'Every shot as a sheet'),
        ('chars', 'Characters', 'Model sheets, the single source of truth'),
        ('neha', 'Neha', 'Producer. Money, approvals, and the boy'),
        ('venkatesh', 'Venkatesh', 'Camera, sound and lighting'),
        ('kristijan', 'Kristijan', 'Animation and motion, in Croatian'),
        ('marko', 'Marko', 'Direction, edit, sound design and score'),
        ('docs', 'PDF', 'Every document, downloadable'),
        ('versions', 'Versions', 'How the film grew')]

SUBS = [('director', 'Director', 'Concept and cut'),
        ('editor', 'Editor', 'Picture'),
        ('sound', 'Sound', 'Design and mix'),
        ('music', 'Music', 'Original score')]


def depth_fix(html, up):
    """Rewrite asset paths for a page sitting `up` folders below the root."""
    p = '../' * up
    html = re.sub(r'(src|href)="(?!https?:|#|/|\.\./|mailto:)', r'\1="' + p, html)
    return html


def page(head, title, body, up, nav):
    return ('<!doctype html><html lang="en"><head>%s\n<title>%s</title></head>\n'
            '<body>\n<div id="app" style="display:block">\n%s\n%s\n%s\n</div>\n'
            '<div id="lb"><img id="lbi" alt=""></div>\n'
            '<script>(function(){var lb=document.getElementById("lb"),li=document.getElementById("lbi");'
            'document.addEventListener("click",function(e){var x=e.target;'
            'if(x&&x.classList&&x.classList.contains("board")){li.src=x.getAttribute("data-full")||x.src;'
            'lb.classList.add("on");}else if(x===lb||x===li){lb.classList.remove("on");li.src="";}});'
            'document.addEventListener("keydown",function(e){if(e.key==="Escape"){'
            'lb.classList.remove("on");li.src="";}});})();</script>\n'
            '</body></html>' % (head, title, nav, body, nav))


def navbar(up, current):
    p = '../' * up
    out = ['<nav class="splitnav"><p class="eyebrow">The Brain Brake</p><ul>',
           '<li><a href="%sindex.html">All sections</a></li>' % p]
    for k, label, _ in TABS:
        out.append('<li>%s</li>' % (('<b>%s</b>' % label) if k == current
                                    else '<a href="%s%s/">%s</a>' % (p, k, label)))
    out.append('</ul></nav>')
    return '\n'.join(out)


EXTRA_CSS = """
<style>
.splitnav{margin:26px 0;padding:16px 0;border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.splitnav ul{list-style:none;padding:0;margin:8px 0 0;display:flex;flex-wrap:wrap;gap:6px 18px}
.splitnav li{font-size:14px}
.splitnav a{color:var(--cy);text-decoration:none}
.splitnav a:hover{text-decoration:underline}
.splitnav b{color:var(--paper)}
.hub{max-width:760px;margin:0 auto;padding:56px 22px}
.hub h1{font-size:32px;margin:0 0 6px}
.hub .lede{color:var(--dim);margin:0 0 34px}
.hub ol{list-style:none;padding:0;margin:0}
.hub li{border-top:1px solid var(--rule);padding:16px 0}
.hub li a{font-size:19px;color:var(--paper);text-decoration:none;display:block}
.hub li a:hover{color:var(--cy)}
.hub li span{display:block;color:var(--dim);font-size:14px;margin-top:3px}
.hub .sub li a{font-size:16px}
.hub .note{margin-top:34px;color:var(--dim);font-size:14px;line-height:1.6}
</style>
"""


def build():
    src = open(SRC).read()
    head = src[src.index('<head>') + 6: src.index('</head>')]
    head = re.sub(r'<title>.*?</title>', '', head, flags=re.S) + EXTRA_CSS

    def grab(cls, key):
        m = re.search(r'<section class="%s"[^>]*id="%s"[^>]*>' % (cls, key), src)
        if not m:
            return None
        i = m.end()
        depth = 1
        for t in re.finditer(r'</?section\b', src[i:]):
            depth += 1 if t.group(0) == '<section' else -1
            if depth == 0:
                return src[m.start(): i + t.end() + len('>')]
        return None

    written = []
    for k, label, blurb in TABS:
        body = grab('pane', 'p-' + k)
        if not body:
            print('MISSING pane', k); continue
        if k == 'marko':                      # strip the js subtabs, they get folders
            body = re.sub(r'<div class="subtabs">.*?</div>', '', body, flags=re.S)
            for sk, slabel, _ in SUBS:
                sub = grab('sub', 's-' + sk)
                if sub:
                    body = body.replace(sub, '')
                    d = os.path.join(REPO, 'marko', sk)
                    os.makedirs(d, exist_ok=True)
                    open(os.path.join(d, 'index.html'), 'w').write(
                        page(depth_fix(head, 2), 'Marko, %s - The Brain Brake' % slabel,
                             depth_fix(sub.replace('class="sub"', 'class="sub on"'), 2),
                             2, navbar(2, 'marko')))
                    written.append('marko/%s/' % sk)
            links = ('<nav class="splitnav"><p class="eyebrow">The four roles</p><ul>' +
                     ''.join('<li><a href="%s/">%s</a></li>' % (sk, sl) for sk, sl, _ in SUBS) +
                     '</ul></nav>')
            body = body + links
        d = os.path.join(REPO, k)
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, 'index.html'), 'w').write(
            page(depth_fix(head, 1), '%s - The Brain Brake' % label,
                 depth_fix(body.replace('class="pane"', 'class="pane on"'), 1),
                 1, navbar(1, k)))
        written.append(k + '/')

    # ---- the hub
    items = ''.join('<li><a href="%s/">%s</a><span>%s</span></li>' % (k, l, b) for k, l, b in TABS)
    subs = ''.join('<li><a href="marko/%s/">Marko, %s</a><span>%s</span></li>' % (k, l, b)
                   for k, l, b in SUBS)
    hub = ('<!doctype html><html lang="en"><head>%s\n<title>The Brain Brake</title></head><body>'
           '<div class="hub"><h1>The Brain Brake</h1>'
           '<p class="lede">Breakthrough Junior Challenge 2026. Every section has its own page, '
           'so each one can be opened, linked and read aloud on its own.</p>'
           '<ol>%s</ol><ol class="sub">%s</ol>'
           '<p class="note">The single page version, with tabs, is still at '
           '<a href="all.html">all.html</a>.</p>'
           '</div></body></html>' % (head, items, subs))

    shutil.copyfile(SRC, os.path.join(REPO, 'all.html'))
    open(os.path.join(REPO, 'index.html'), 'w').write(hub)
    print('written %d section pages' % len(written))
    for w in written:
        print('   /' + w)
    print('   /all.html   (the old single page, kept)')


if __name__ == '__main__':
    build()

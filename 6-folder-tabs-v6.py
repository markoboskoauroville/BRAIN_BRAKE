import re

p = 'index.html'
h = open(p, encoding='utf-8').read()

h = h.replace('<div class="ver">4 (a)</div>', '<div class="ver">5 (a)</div>')

# ---------- favicon links ----------
h = h.replace('<link rel="preconnect" href="https://fonts.googleapis.com">',
 '<link rel="icon" href="favicon.svg" type="image/svg+xml">\n'
 '<link rel="alternate icon" href="favicon-32.png" sizes="32x32">\n'
 '<link rel="apple-touch-icon" href="apple-touch-icon.png">\n'
 '<meta name="theme-color" content="#0b0e13">\n'
 '<link rel="preconnect" href="https://fonts.googleapis.com">')

# ---------- replace rail CSS with folder-tab CSS ----------
old_css_start = h.index('.wrap{display:flex;align-items:flex-start;min-height:calc(100vh - 60px)}')
old_css_end = h.index('/* ---------- STAGE ---------- */')
new_nav_css = """.wrap{display:block}
body{overflow-x:hidden}

/* ---------- FOLDER TABS ---------- */
.tabbar{
  background:var(--panel);
  border-bottom:3px solid var(--paper);
  padding:14px 22px 0;
  display:flex;flex-wrap:wrap;align-items:flex-end;gap:3px;
  position:sticky;top:59px;z-index:35;
}
.tab{
  position:relative;
  background:#3b3a35;
  color:#b9b2a2;
  border:0;border-bottom:0;
  padding:7px 15px 9px;
  cursor:pointer;
  text-align:left;
  border-radius:7px 7px 0 0;
  box-shadow:inset 0 1px 0 rgba(255,255,255,.07);
  top:3px;
  min-width:92px;
}
.tab:hover{background:#4d4b43;color:#e2dbc9}
.tab:focus-visible{outline:2px solid var(--signal);outline-offset:-3px}
.tab.on{
  background:var(--paper);
  color:var(--graphite);
  top:0;
  padding-bottom:12px;
  box-shadow:0 -1px 0 var(--paper-2);
  z-index:2;
}
.tab .rl{
  display:block;
  font-family:'Barlow Condensed',sans-serif;font-weight:600;
  font-size:16px;line-height:1;letter-spacing:.06em;text-transform:uppercase;
  white-space:nowrap;
}
.tab .who{
  display:block;
  font-family:'IBM Plex Mono',monospace;font-size:8.5px;
  letter-spacing:.14em;text-transform:uppercase;
  margin-top:4px;opacity:.72;white-space:nowrap;
}
.tab.on .who{opacity:.62}
.tab .led{
  position:absolute;top:6px;right:7px;
  width:5px;height:5px;border-radius:50%;background:#6a675e;
}
.tab .led.go{background:var(--live)}
.tab .led.hold{background:var(--lever)}
.tab.on .led{box-shadow:0 0 0 1.5px rgba(0,0,0,.15)}
.tabgap{width:16px;flex:0 0 16px}

/* lever strip under the tabs */
.lever-box{
  display:flex;align-items:center;gap:16px;flex-wrap:wrap;
  padding:11px 24px;border-bottom:1px solid var(--rule);background:var(--void);
}
.lever-lbl{
  font-family:'IBM Plex Mono',monospace;font-size:9px;
  letter-spacing:.2em;text-transform:uppercase;color:var(--dim);
  display:flex;align-items:baseline;gap:9px;
}
.lever-lbl b{font-size:17px;color:var(--lever);font-weight:600;letter-spacing:0}
.track{
  flex:1;min-width:150px;max-width:340px;height:8px;
  background:var(--panel);border:1px solid var(--rule);position:relative;
}
.fill{height:100%;background:var(--lever);width:31%}
.notch{position:absolute;top:-3px;bottom:-3px;width:1px;background:var(--rule)}
.lever-note{
  font-family:'Caveat',cursive;font-size:15px;color:var(--dim);line-height:1.2;
}

"""
h = h[:old_css_start] + new_nav_css + h[old_css_end:]

# ---------- responsive block ----------
h = re.sub(r'@media\(max-width:880px\)\{\n  \.wrap\{display:block\}.*?\n\}', """@media(max-width:880px){
  .tabbar{padding:10px 10px 0;top:0;position:static}
  .tab{min-width:0;padding:6px 11px 8px}
  .tab .rl{font-size:14px}
  .tab .who{display:none}
  .tabgap{display:none}
  .lever-box{padding:10px 14px}
  .lever-note{display:none}
  .fr{flex-direction:column;gap:8px}
  .fr-id{flex:none}
  .board{max-width:100%}
  .stage{padding:24px 18px 70px}
  .sheet{padding:22px 19px}
  .slate{padding:12px 16px}
  .slate-meta{width:100%;margin-left:0;gap:14px}
}""", h, flags=re.S)

# ---------- stage widths ----------
h = h.replace('.stage{flex:1;min-width:0;padding:34px 40px 90px;max-width:1080px}',
              '.stage{padding:34px 40px 100px;max-width:1060px;margin:0 auto}')

# ---------- markup: rail -> tabbar ----------
TABS = [
 ('overview','Overview','All','go'),
 ('script','The Film','Script','hold'),
 ('board','Storyboard','35 shots','hold'),
 ('chars','Characters','Design','go'),
 ('GAP',None,None,None),
 ('neha','Neha','Client','go'),
 ('venkatesh','Venkatesh','Camera','hold'),
 ('kristijan','Kristijan','Animation','hold'),
 ('GAP',None,None,None),
 ('director','Director','Marko','go'),
 ('editor','Editor','Marko',''),
 ('sound','Sound','Marko',''),
 ('music','Music','Marko',''),
 ('GAP',None,None,None),
 ('versions','Versions','Archive',''),
]
nav = '  <nav class="tabbar" aria-label="Sections">\n'
for pid, role, who, led in TABS:
    if pid == 'GAP':
        nav += '    <span class="tabgap"></span>\n'; continue
    nav += (f'    <button class="tab" data-p="{pid}"><span class="led {led}"></span>'
            f'<span class="rl">{role}</span><span class="who">{who}</span></button>\n')
nav += '  </nav>\n'
nav += """  <div class="lever-box">
    <div class="lever-lbl"><span>Power output</span><b>31%</b></div>
    <div class="track"><div class="fill"></div>
      <span class="notch" style="left:25%"></span>
      <span class="notch" style="left:50%"></span>
      <span class="notch" style="left:75%"></span>
    </div>
    <div class="lever-note">not maximum. never maximum. we save some for the finish.</div>
  </div>

"""
start = h.index('  <div class="wrap">')
end = h.index('    <!-- STAGE -->')
h = h[:start] + nav + '  <div class="wrap">\n' + h[end:]

# close: the old </div> that closed .wrap sibling structure still balances (nav removed, wrap kept)
open(p, 'w', encoding='utf-8').write(h)
print('rewritten', len(h))

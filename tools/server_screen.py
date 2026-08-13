# --- the server screen -----------------------------------------------------
# The standing terminal screen for every one of my Flask apps, Termux or macOS
# Terminal. Measured off MA Reader v26. See SERVER_SCREEN.md, which is the
# rule; this file is only the way of obeying it.
#
# Standard library only, no Flask import, so it drops into anything.
#
#   from server_screen import ServerScreen, pick_port, quiet_flask
#
# Two ways in. Either call the painting functions yourself (boot, screen), or
# hand the whole thing to ServerScreen and let it run the server as its child.

import os, sys, time, socket, shutil, signal, subprocess

MARGIN = 2      # two spaces on every line, always
WIDTH  = 46     # content width: the rules, and the widest block
LABEL  = 9      # a facts label is padded to this, so values line up
GAP    = 4      # spaces between items in the key row

# ---------------------------------------------------------------- palette --
# startup block: plain ANSI, so a dumb terminal still reads it
A_NAME  = None   # set below, once the terminal has been asked what it can do
A_DIM   = A_UP = A_DOWN = A_TEXT = None
# dashboard: 256 colour, NEVER 24-bit.
# Marko's terminal does not do truecolour: a 38;2;r;g;b escape comes out as
# literal rubbish and breaks the screen. So every colour here is 256 colour,
# with the basic eight underneath for a terminal that has no 256 either.
def _pal(n256, n8):
    return "\033[38;5;%dm" % n256 if COLOURS >= 256 else (
           "\033[%sm" % n8 if COLOURS >= 8 else "")

def _colours():
    if not sys.stdout.isatty():
        return 0
    try:
        import curses
        curses.setupterm()
        return max(0, curses.tigetnum("colors"))
    except Exception:
        t = os.environ.get("TERM", "")
        return 256 if "256" in t else (8 if t and t != "dumb" else 0)

COLOURS = _colours()

D_ART1  = _pal(209, "0;33")   # was #FF8A3C
D_ART2  = _pal(166, "0;31")   # was #D65C30
D_OM    = _pal(208, "1;33")   # #FF8700
D_INK   = _pal(245, "0;37")   # was #788092, the blue tint is not survivable
D_VAL   = _pal(252, "1;37")   # was #CDD0D6
OFF     = "\033[0m" if COLOURS else ""

A_NAME  = _pal(203, "1;31")   # #FF5F5F ember red
A_DIM   = _pal(244, "0;37")   # #7F7F7F grey
A_UP    = _pal(10,  "1;32")   # green, the only state colour on this screen
A_DOWN  = _pal(131, "1;31")   # red, an address that is not answering
A_TEXT  = _pal(15,  "1;37")   # white

def _tty():
    return sys.stdout.isatty()

def _c(colour, text):
    return (colour + text + OFF) if (COLOURS and _tty()) else text

def _cols():
    try:
        return shutil.get_terminal_size((56, 24)).columns
    except Exception:
        return 56

def _w():
    return min(WIDTH, max(20, _cols() - 2 * MARGIN))

def _pad():
    return " " * MARGIN

def _line(s=""):
    print((_pad() + s) if s else "")

def rule():
    _line(_c(D_INK, "\u2500" * _w()))

# ------------------------------------------------------------------ ports --
def port_free(port, host="0.0.0.0"):
    """Test bind. Asking the kernel is the only answer that is ever true."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        return True
    except Exception:
        return False
    finally:
        try:
            s.close()
        except Exception:
            pass

def pick_port(base, portfile=None, span=40):
    """Never a fixed port. Start at the app's base and walk up to the first
    free one, then write it down so everything else can find it."""
    chosen = base
    for p in range(base, base + span):
        if port_free(p):
            chosen = p
            break
    if portfile:
        try:
            os.makedirs(os.path.dirname(portfile), exist_ok=True)
            with open(portfile, "w") as f:
                f.write(str(chosen))
        except Exception:
            pass
    return chosen

def port_up(port, host="127.0.0.1", timeout=0.4):
    """Is something answering there. This is what colours the marker."""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        return True
    except Exception:
        return False
    finally:
        try:
            s.close()
        except Exception:
            pass

def lan_ip():
    """The address the phone across the room should type. None if no network."""
    s = None
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("10.255.255.255", 1))
        ip = s.getsockname()[0]
        return ip if ip and not ip.startswith("127.") else None
    except Exception:
        return None
    finally:
        try:
            s.close()
        except Exception:
            pass

def quiet_flask():
    """No red development server warning. It is alarming and says nothing."""
    try:
        import logging
        logging.getLogger("werkzeug").setLevel(logging.ERROR)
    except Exception:
        pass
    try:
        import flask.cli
        flask.cli.show_server_banner = lambda *a, **k: None
    except Exception:
        pass

# ------------------------------------------------------------------ boot ---
def boot(name, tagline, port, om=True, up=True):
    """What the server prints as it comes up. `up` is the one piece of state
    on this screen: green when the address answers, red when it does not."""
    _line(_c(A_NAME, name))
    _line(_c(A_DIM, tagline))
    _line()
    rows = [("on this phone", "http://127.0.0.1:%d" % port)]
    ip = lan_ip()
    if ip:
        rows.append(("on Wi-Fi", "http://%s:%d" % (ip, port)))
    for label, url in rows:
        _line("%s %s%s" % (_c(A_UP if up else A_DOWN, "\u25ba"),
                           _c(A_TEXT, label.ljust(15)), _c(A_TEXT, url)))
    _line()
    _line(_c(A_DIM, "Ctrl+C to stop"))
    if om:
        print(" " * max(0, _cols() - 2) + _c(D_OM, "\u0950"))
    _line()

# ---------------------------------------------------------------- screen ---
def art(rows):
    """figlet small, four rows, light on top and ember below."""
    for i, row in enumerate(rows[:4]):
        _line(_c(D_ART1 if i < 2 else D_ART2, row.rstrip()))

def facts(pairs):
    for label, value in pairs[:6]:
        _line(_c(D_INK, str(label).ljust(LABEL)) + _c(D_VAL, str(value)))

def keys(items):
    """items: [('q', 'quit'), ('o', 'open the page'), ('b', 'background')]"""
    _line(_c(D_INK, (" " * GAP).join("%s %s" % (k, w) for k, w in items)))

def screen(art_rows, tagline, pairs, key_items, clear=True):
    if clear and _tty():
        print("\033[2J\033[H", end="")
    art(art_rows)
    _line(" " * 5 + _c(D_INK, tagline))
    _line()
    rule()
    facts(pairs)
    rule()
    keys(key_items)
    _line()

# ------------------------------------------------------------------ input --
def getkey():
    """One raw keypress, no Enter. An unknown key is the caller's problem and
    the caller's answer is to do nothing at all."""
    try:
        import termios, tty
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)
        return ch.lower()
    except Exception:
        return (sys.stdin.readline()[:1] or "").lower()

def open_page(url):
    for cmd in (["termux-open-url", url], ["open", url], ["xdg-open", url]):
        try:
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)
            return True
        except Exception:
            continue
    return False

# ----------------------------------------------------------------- runner --
class ServerScreen(object):
    """The screen, with the server running underneath it as its own child.

    q stops both. b lets the server go and leaves the screen. Anything the app
    adds is handled by on_key, which returns True if it wants a redraw."""

    def __init__(self, app_name, tagline, tagline2, banner, base_port, app_dir,
                 version, serve, facts=None, keys=None, on_key=None,
                 host="127.0.0.1", wait=20.0):
        self.app_name = app_name
        self.tagline = tagline
        self.tagline2 = tagline2
        self.banner = banner
        self.base_port = base_port
        self.app_dir = app_dir
        self.version = version
        self.serve = serve                 # argv of the bare server
        self.extra_facts = list(facts or [])
        self.extra_keys = list(keys or [])
        self.on_key = on_key
        self.host = host
        self.wait = wait
        self.port = base_port
        self.child = None
        self.up = False

    # -- the four rows the facts block always answers first
    def _facts(self):
        rows = [("version", self.version),
                ("address", "http://localhost:%d" % self.port),
                ("port", "%d  (base %d)" % (self.port, self.base_port))]
        return (rows + self.extra_facts)[:6]

    def _keys(self):
        return ([("q", "quit"), ("o", "open the page"), ("b", "background")]
                + self.extra_keys)

    def _paint(self):
        boot(self.app_name, self.tagline, self.port, up=self.up)
        screen(self.banner, self.tagline2, self._facts(), self._keys(),
               clear=False)

    def _start(self):
        env = dict(os.environ)
        env["PORT"] = str(self.port)
        env["APP_DIR"] = self.app_dir
        self.child = subprocess.Popen(self.serve, env=env,
                                      start_new_session=True)
        deadline = time.time() + self.wait
        while time.time() < deadline:
            if port_up(self.port, self.host):
                self.up = True
                break
            if self.child.poll() is not None:
                break
            time.sleep(0.25)

    def _stop(self):
        if not self.child or self.child.poll() is not None:
            return
        try:
            os.killpg(os.getpgid(self.child.pid), signal.SIGTERM)
        except Exception:
            try:
                self.child.terminate()
            except Exception:
                pass
        try:
            self.child.wait(timeout=5)
        except Exception:
            try:
                os.killpg(os.getpgid(self.child.pid), signal.SIGKILL)
            except Exception:
                pass

    def run(self):
        self.port = pick_port(self.base_port,
                              os.path.join(self.app_dir, "port"))
        self._start()
        if _tty():
            print("\033[2J\033[H", end="")
        self._paint()
        try:
            while True:
                k = getkey()
                if k == "q":
                    self._stop()
                    return 0
                if k == "b":
                    self.child = None      # let it go, it is already its own
                    _line(_c(D_INK, "still serving on port %d" % self.port))
                    _line()
                    return 0
                if k == "o":
                    open_page("http://127.0.0.1:%d" % self.port)
                    continue
                if k == "c":
                    self.up = port_up(self.port, self.host)
                    self._paint()
                    continue
                if k in ("\x03", "\x04"):
                    self._stop()
                    return 0
                if self.on_key and self.on_key(k, self):
                    self.up = port_up(self.port, self.host)
                    self._paint()
                # an unknown key does nothing at all
        except KeyboardInterrupt:
            self._stop()
            return 0

# ------------------------------------------------------------------ usage --
if __name__ == "__main__":
    # NOTE: a raw string may not END in a backslash, and this art is full of
    # them. So every row carries one trailing space and art() trims it.
    MA_READER = [
        r" __  __   _     ___ ___   _   ___  ___ ___ ",
        r"|  \/  | /_\   | _ \ __| /_\ |   \| __| _ \ ",
        r"| |\/| |/ _ \  |   / _| / _ \| |) | _||   / ",
        r"|_|  |_/_/ \_\ |_|_\___/_/ \_\___/|___|_|_\ ",
    ]
    PORT = 8081
    boot("MA READER", "Fire | the Word", PORT)
    screen(MA_READER, "Fire | the Word, the MA ecosystem",
           [("version", "v26 (a)"),
            ("address", "http://localhost:%d" % PORT),
            ("port", "%d  (base %d)" % (PORT, PORT)),
            ("library", "~/.maread/library")],
           [("q", "quit"), ("o", "open the page"), ("b", "background")],
           clear=False)

FPS = 25

def tc(seconds, fps=FPS):
    """seconds -> HH:MM:SS:FF, 25fps, two digit padding"""
    total = int(round(seconds * fps))
    f = total % fps
    s = (total // fps) % 60
    m = (total // (fps*60)) % 60
    h = total // (fps*3600)
    return "%02d:%02d:%02d:%02d" % (h, m, s, f)

def frames(seconds, fps=FPS):
    return int(round(seconds * fps))

def wav_seconds(path):
    import wave, contextlib
    with contextlib.closing(wave.open(path)) as w:
        return w.getnframes() / float(w.getframerate())

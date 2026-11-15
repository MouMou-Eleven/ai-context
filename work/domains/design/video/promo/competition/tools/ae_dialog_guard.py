# Resident AE dialog guard: auto-clicks known AE pop-ups so no human is needed.
# Runs forever (single instance via lock file), logs next to this script (aeguard.log).
# Start: pythonw ae_dialog_guard.py   (needs: pip install pywinauto psutil)
import time, os, sys, psutil, ctypes
from pywinauto import Desktop

HERE = os.path.dirname(os.path.abspath(__file__))
LOG = os.path.join(HERE, 'aeguard.log')
LOCK = os.path.join(HERE, 'aeguard.pid')

def log(s):
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write(time.strftime('%m-%d %H:%M:%S ') + s + '\n')

# single instance
if os.path.exists(LOCK):
    try:
        pid = int(open(LOCK).read().strip())
        if psutil.pid_exists(pid) and 'python' in psutil.Process(pid).name().lower():
            sys.exit(0)
    except Exception:
        pass
open(LOCK, 'w').write(str(os.getpid()))
log('guard start pid %d' % os.getpid())

# button captions to press, in priority order (never "安全模式"/"重置首选项"/"取消")
PREFER = ['继续', 'Continue', '确定', 'OK', '关闭', 'Close']
AVOID = ['安全模式', 'Safe', '重置', 'Reset', '管理增效', 'Manage']

while True:
    try:
        ae = [p.pid for p in psutil.process_iter(['name']) if (p.info['name'] or '').lower() in ('afterfx.exe', 'aerender.exe')]
        wer = [p for p in psutil.process_iter(['name', 'cmdline']) if (p.info['name'] or '').lower() == 'werfault.exe']
        if wer and ae:
            # AE crashed: the crash reporter blocks forever -> kill it and the dead AE
            for p in wer:
                try: p.kill()
                except Exception: pass
            log('WerFault killed (AE crashed)')
        if ae:
            for w in Desktop(backend='win32').windows(visible_only=True):
                try:
                    if w.process_id() not in ae: continue
                    r = w.rectangle()
                    if r.width() > 1300 or r.height() > 900: continue   # main AE window / panels
                    if r.width() < 150 or r.height() < 80: continue
                    title = w.window_text()
                    kids = w.descendants()
                    texts = [c.window_text() for c in kids]
                    btn = None
                    for cap in PREFER:
                        for c in kids:
                            t = (c.window_text() or '').replace('&', '').strip()
                            if t == cap and c.is_visible() and c.is_enabled():
                                btn = c; break
                        if btn: break
                    if btn is None and title not in ('After Effects', '崩溃修复选项', '解析字体', 'Adobe After Effects'):
                        continue   # unknown non-dialog window, leave it
                    desc = (title + ' | ' + ' '.join(t for t in texts if t)[:120])
                    if ('保存' in desc or 'Save' in desc or 'save' in desc):
                        # never risk saving over a project: cancel (ESC); scripts always save to new versions themselves
                        w.set_focus(); w.type_keys('{ESC}'); log('ESC (save prompt) on: ' + desc); time.sleep(0.5); continue
                    if btn is not None:
                        btn.click(); log('click [%s] on: %s' % (btn.window_text(), desc))
                    else:
                        w.set_focus(); w.type_keys('{ENTER}'); log('ENTER on: ' + desc)
                    time.sleep(0.5)
                except Exception as e:
                    pass
    except Exception as e:
        log('loop err ' + repr(e)[:100])
    time.sleep(1)

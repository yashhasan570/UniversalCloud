#!/usr/bin/env python3
"""Reapply the Universal Cloud rebrand after an upstream sync."""
from pathlib import Path
import os, shutil

SKIP_DIRS = {'.git', '.github', 'scripts'}

def newpath(s):
    return s.replace('CasaOS', 'UniversalCloud').replace('casaos', 'universalcloud')

def sweep():
    code_ext = {'.go', '.py', '.sh', '.mod', '.sum', '.list', '.service'}
    pairs_code = [
        ('github.com/IceWhaleTech/CasaOS', 'github.com/yashhasan570/UniversalCloud'),
        ('casaos.io', 'universalcloud.app'),
        ('casaOS.db', 'universalcloud.db'),
        ('Casaos', 'UniversalCloud'),
        ('CasaOS', 'UniversalCloud'),
        ('casaos', 'universalcloud'),
    ]
    pairs_text = [
        ('github.com/IceWhaleTech/CasaOS', 'github.com/yashhasan570/UniversalCloud'),
        ('casaos.io', 'universalcloud.app'),
        ('casaos.app', 'universalcloud.app'),
        ('Casaos', 'UniversalCloud'),
        ('CasaOS', 'Universal Cloud'),
        ('casaos', 'universalcloud'),
    ]
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            p = Path(root) / f
            if p.name == '.gitmodules':
                continue
            try: t = p.read_text(encoding='utf-8')
            except Exception: continue
            orig = t
            if p.suffix in code_ext:
                for old, new in pairs_code: t = t.replace(old, new)
            else:
                for old, new in pairs_text: t = t.replace(old, new)
            if t != orig: p.write_text(t)

def merge(src, dst):
    for child in list(src.iterdir()):
        ct = Path(newpath(str(child)))
        ct.parent.mkdir(parents=True, exist_ok=True)
        if ct.exists():
            if child.is_dir() and ct.is_dir():
                merge(child, ct)
                try: child.rmdir()
                except OSError: pass
            elif child.is_dir():
                shutil.rmtree(ct, ignore_errors=True)
                shutil.move(str(child), str(ct))
            else:
                if ct.is_dir(): shutil.rmtree(ct, ignore_errors=True)
                else: ct.unlink()
                shutil.move(str(child), str(ct))
        else:
            shutil.move(str(child), str(ct))
    try: src.rmdir()
    except OSError: pass

def renames():
    targets = []
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in dirs + files:
            if 'casaos' in name.lower():
                targets.append(Path(root) / name)
    targets.sort(key=lambda p: len(p.parts), reverse=True)
    for p in targets:
        if not p.exists(): continue
        tgt = Path(newpath(str(p)))
        if p == tgt: continue
        tgt.parent.mkdir(parents=True, exist_ok=True)
        if p.is_dir() and tgt.exists() and tgt.is_dir():
            merge(p, tgt)
        elif tgt.exists():
            if p.is_dir(): shutil.rmtree(p, ignore_errors=True)
            else:
                if tgt.is_dir(): shutil.rmtree(tgt, ignore_errors=True)
                else: tgt.unlink()
                shutil.move(str(p), str(tgt))
        else:
            shutil.move(str(p), str(tgt))

def cleanup():
    for item in ['.all-contributorsrc', 'CHANGELOG.md', 'CODE_OF_CONDUCT.md', 'DEVELOPING.md', 'SECURITY.md']:
        p = Path(item)
        if p.exists(): p.unlink()

def readme():
    Path('README.md').write_text("""# Universal Cloud

A simple, elegant personal cloud system for your devices. Run it on a PC, NAS, or Raspberry Pi to manage Docker apps, files, and storage from a clean dashboard.

## Contact

Telegram: [@johnconstantine570](https://t.me/johnconstantine570)
""")

if __name__ == '__main__':
    sweep(); renames(); cleanup(); readme()
    print('rebrand reapplied')

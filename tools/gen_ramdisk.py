"""Catalog a mounted restore ramdisk: every file, and for each Mach-O its linked libraries,
entitlements, Objective-C classes, IOKit/DriverKit personalities and strings; for each plist, its keys.

usage: gen_ramdisk.py <mount point> <label> reference/ramdisk
"""
import os
import plistlib
import re
import subprocess
import sys

mnt, label, out = sys.argv[1:4]
os.makedirs(out, exist_ok=True)
MAX_STR = 2500


def run(*a, timeout=120):
    try:
        return subprocess.run(a, capture_output=True, timeout=timeout).stdout.decode('utf-8', 'replace')
    except subprocess.TimeoutExpired:
        return ''


def is_macho(p):
    try:
        with open(p, 'rb') as f:
            m = f.read(4)
        return m in (b'\xcf\xfa\xed\xfe', b'\xca\xfe\xba\xbe', b'\xce\xfa\xed\xfe')
    except OSError:
        return False


def slug(rel):
    return re.sub(r'[^A-Za-z0-9_.,+-]', '_', rel.strip('/').replace('/', '__'))


def fmt_plist(v, depth=0, limit=[0]):
    pad = '  ' * depth
    out = []
    if isinstance(v, dict):
        for k in sorted(v, key=str):
            x = v[k]
            if isinstance(x, (dict, list)) and x:
                out.append(f'{pad}- `{k}`:')
                out += fmt_plist(x, depth + 1)
            else:
                out.append(f'{pad}- `{k}`: `{str(x)[:200]}`')
    elif isinstance(v, list):
        for x in v[:200]:
            if isinstance(x, (dict, list)):
                out.append(f'{pad}-')
                out += fmt_plist(x, depth + 1)
            else:
                out.append(f'{pad}- `{str(x)[:200]}`')
    return out


files = []
for dp, dn, fn in os.walk(mnt):
    dn.sort()
    for f in sorted(fn):
        p = os.path.join(dp, f)
        if os.path.islink(p):
            continue
        files.append(p)

index = []
for p in files:
    rel = '/' + os.path.relpath(p, mnt)
    try:
        size = os.path.getsize(p)
    except OSError:
        continue
    kind = 'file'
    page = None
    if is_macho(p):
        kind = 'Mach-O'
        L = [f'# `{rel}`', '', f'From the {label}. {size:,} bytes.', '']
        hdr = run('ipsw', 'macho', 'info', p, '-d')
        L += ['## Header', '', '```'] + [l for l in hdr.splitlines() if l.strip()][:20] + ['```']
        libs = run('otool', '-L', p).splitlines()[1:]
        if libs:
            L += ['', f'## Linked libraries ({len(libs)})', ''] + [f'- `{l.strip()}`' for l in libs]
        ent = run('ipsw', 'macho', 'info', p, '-e')
        ent_lines = [l for l in ent.splitlines() if l.strip()]
        if ent_lines:
            L += ['', '## Entitlements', '', '```xml'] + ent_lines[:300] + ['```']
        objc = run('ipsw', 'macho', 'info', p, '--objc')
        cls = sorted(set(re.findall(r'@interface (\S+)', objc)))
        prots = sorted(set(re.findall(r'@protocol (\S+)', objc)))
        if cls or prots:
            L += ['', f'## Objective-C ({len(cls)} classes, {len(prots)} protocols)', '']
            if cls:
                L.append('Classes: ' + ', '.join(f'`{c}`' for c in cls[:600]))
            if prots:
                L.append('')
                L.append('Protocols: ' + ', '.join(f'`{c}`' for c in prots[:300]))
            meth = [l.strip() for l in objc.splitlines() if re.match(r'\s*[-+] \(', l)]
            if meth:
                L += ['', f'### Methods ({len(meth)})', '', '```'] + meth[:3000] + ['```']
        strs = run('ipsw', 'macho', 'info', p, '--strings')
        sl = [m.group(1) for m in (re.match(r'0x[0-9a-f]+: "(.*)"$', l) for l in strs.splitlines()) if m]
        L += ['', f'## Strings ({len(sl):,})', '']
        if len(sl) > MAX_STR:
            L.append(f'First {MAX_STR:,} of {len(sl):,}.')
        L += ['```'] + [s[:240] for s in sl[:MAX_STR]] + ['```']
        page = slug(rel) + '.md'
        open(os.path.join(out, page), 'w').write('\n'.join(L) + '\n')
    elif p.endswith('.plist') or os.path.basename(p) == 'Info.plist':
        try:
            pl = plistlib.load(open(p, 'rb'))
            kind = 'plist'
            L = [f'# `{rel}`', '', f'From the {label}. {size:,} bytes.', ''] + fmt_plist(pl)
            page = slug(rel) + '.md'
            open(os.path.join(out, page), 'w').write('\n'.join(L[:20000]) + '\n')
        except Exception:
            pass
    else:
        head = open(p, 'rb').read(64)
        if head[:4] == b'0\x84' or b'IM4P' in head[:16]:
            kind = 'IM4P'
        elif head[:4] in (b'bplist'[:4],):
            kind = 'plist'
    index.append((rel, size, kind, page))

L = [f'# {label}: file catalog', '', f'{len(index):,} files. Mach-O binaries and property lists have their own pages.', '',
     '| Path | Size | Kind |', '|---|---|---|']
for rel, size, kind, page in index:
    name = f'[`{rel}`]({page})' if page else f'`{rel}`'
    L.append(f'| {name} | {size:,} | {kind} |')
open(os.path.join(out, 'README.md'), 'w').write('\n'.join(L) + '\n')
print(len(index), 'files;', sum(1 for i in index if i[3]), 'pages')

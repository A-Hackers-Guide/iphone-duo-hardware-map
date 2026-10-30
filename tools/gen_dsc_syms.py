"""One symbols page per dyld-cache image: exported symbols, imported (undefined) symbols, and Swift-demangled
names where present. Worker pool, resumable. Writes reference/userland-symbols/.

usage: gen_dsc_syms.py <dyld_shared_cache> reference/userland-symbols [workers]
"""
import multiprocessing as mp
import os
import re
import subprocess
import sys

dsc, out = sys.argv[1], sys.argv[2]
workers = int(sys.argv[3]) if len(sys.argv) > 3 else 3
MAX_PUBLIC = 3000
MAX_PRIVATE = 1000
MAX_UNDEF = 1000
os.makedirs(out, exist_ok=True)


def run(*a, timeout=600):
    try:
        return subprocess.run(a, capture_output=True, timeout=timeout).stdout.decode('utf-8', 'replace')
    except subprocess.TimeoutExpired:
        return ''


def slug(p):
    return re.sub(r'[^A-Za-z0-9_.,+-]', '_', p.strip('/').replace('/', '__'))


SYM = re.compile(r'^\s*(0x[0-9a-f]+)?:?\s*(?:<([^>]+)>|\(([^)]+)\))?\s*(\S.*)$')


def page(path):
    dest = os.path.join(out, slug(path) + '.md')
    if os.path.exists(dest):
        return
    txt = run('ipsw', 'dyld', 'macho', '--no-color', '--demangle', dsc, path, '-n')
    exported, local, undefined = [], [], []
    for line in txt.splitlines():
        m = re.match(r'\s*(0x[0-9a-fA-F]+):\s*(?:\(([^)]*)\))?\s*([^\t]*)\t([^\t]+)', line)
        if not m:
            continue
        addr, sect, vis, name = m.groups()
        vis = vis.strip()
        if int(addr, 16) == 0 or 'undefined' in vis:
            undefined.append((addr, vis, name.strip()))
        elif vis.startswith('external') or vis == 'exported':
            exported.append((addr, sect or '', name.strip()))
        else:
            local.append((addr, sect or '', name.strip()))
    L = [f'# Symbols: `{path}`', '', 'Symbol table of this image in the iOS 27.2 dyld shared cache (`ipsw dyld macho -n --demangle`). '
         f'The class-level view is on the [image page](../userland/{slug(path)}.md). **[DSC]**', '',
         f'{len(exported):,} public symbols, {len(local):,} private symbols, {len(undefined):,} undefined (imported).', '']
    for title, rows, cap in (('Public (external)', exported, MAX_PUBLIC), ('Private', local, MAX_PRIVATE)):
        if rows:
            L += [f'## {title}', '', '```'] + [f'{a}  {k + "  " if k else ""}{n[:300]}' for a, k, n in rows[:cap]] + ['```']
            if len(rows) > cap:
                L.append(f'First {cap:,} of {len(rows):,}.')
            L.append('')
    if undefined:
        L += ['', '## Undefined (imports)', '', '```'] + [n[:300] for _, _, n in undefined[:MAX_UNDEF]] + ['```']
    open(dest + '.tmp', 'w').write('\n'.join(L) + '\n')
    os.replace(dest + '.tmp', dest)


if __name__ == '__main__':
    listing = run('ipsw', 'dyld', 'info', '-l', '--no-color', dsc)
    imgs, seen = [], set()
    for line in listing.splitlines():
        m = re.search(r'(/(?:System|usr|Library|private|AppleInternal)\S+)', line)
        if m and m.group(1) not in seen:
            seen.add(m.group(1))
            imgs.append(m.group(1))
    todo = [p for p in imgs if not os.path.exists(os.path.join(out, slug(p) + '.md'))]
    print(len(imgs), 'images,', len(todo), 'to do', flush=True)
    with mp.Pool(workers) as pool:
        for n, _ in enumerate(pool.imap_unordered(page, todo, chunksize=4), 1):
            if n % 200 == 0:
                print(n, flush=True)
    I = ['# Userland symbols', '', f'Symbol tables for {len(imgs):,} images of the iOS 27.2 dyld shared cache. **[DSC]**', '', '| Image | Symbols page |', '|---|---|']
    for p in imgs:
        f = slug(p) + '.md'
        I.append(f'| `{p}` | ' + (f'[symbols]({f})' if os.path.exists(os.path.join(out, f)) else '') + ' |')
    open(os.path.join(out, 'README.md'), 'w').write('\n'.join(I) + '\n')
    print('index written')

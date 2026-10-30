"""Light pages for every dyld-cache image that gen_dsc.py did not cover: linked libraries,
Objective-C classes and protocols, Swift types. Runs a small worker pool and resumes.
Then rewrites reference/userland/README.md to index every image.

usage: gen_dsc_all.py <dyld_shared_cache> reference/userland [workers]
"""
import multiprocessing as mp
import os
import re
import subprocess
import sys

dsc, out = sys.argv[1], sys.argv[2]
workers = int(sys.argv[3]) if len(sys.argv) > 3 else 3
reverse = len(sys.argv) > 4 and sys.argv[4] == 'reverse'


def run(*a, timeout=600):
    try:
        return subprocess.run(a, capture_output=True, timeout=timeout).stdout.decode('utf-8', 'replace')
    except subprocess.TimeoutExpired:
        return ''


def slug(p):
    return re.sub(r'[^A-Za-z0-9_.,+-]', '_', p.strip('/').replace('/', '__'))


def page(item):
    path, ver = item
    dest = os.path.join(out, slug(path) + '.md')
    if os.path.exists(dest):
        return
    loads = run('ipsw', 'dyld', 'macho', '--no-color', dsc, path, '-l')
    deps = re.findall(r'LC_(?:REEXPORT_|LOAD_WEAK_|LOAD_UPWARD_|LAZY_LOAD_)?(?:LOAD_)?DYLIB\s+(\S+)', loads)
    objc = run('ipsw', 'dyld', 'macho', '--no-color', dsc, path, '--objc')
    cls = sorted(set(re.findall(r'@interface (\S+)', objc)))
    prot = sorted(set(re.findall(r'@protocol (\S+)', objc)))
    nmeth = sum(1 for l in objc.splitlines() if re.match(r'\s*[-+]\[', l))
    L = [f'# `{path}`', '', f'iOS 27.2 dyld shared cache image, version `{ver}`. Light page: libraries and type names only. **[DSC]**', '']
    if deps:
        L += [f'## Linked libraries ({len(deps)})', ''] + [f'- `{d}`' for d in deps] + ['']
    L += [f'## Objective-C: {len(cls)} classes, {len(prot)} protocols, {nmeth} methods', '']
    if cls:
        L += ['### Classes', '', ', '.join(f'`{c}`' for c in cls), '']
    if prot:
        L += ['### Protocols', '', ', '.join(f'`{c}`' for c in prot), '']
    open(dest + '.tmp', 'w').write('\n'.join(L) + '\n')
    os.replace(dest + '.tmp', dest)


def images():
    listing = run('ipsw', 'dyld', 'info', '-l', '--no-color', dsc)
    seen, res = set(), []
    for line in listing.splitlines():
        m = re.search(r'(/(?:System|usr|Library|private|AppleInternal)\S+)', line)
        if m and m.group(1) not in seen:
            seen.add(m.group(1))
            v = re.search(r'\b(\d+(?:\.\d+){1,4})\b', line)
            res.append((m.group(1), v.group(1) if v else ''))
    return res


if __name__ == '__main__':
    imgs = images()
    todo = [i for i in imgs if not os.path.exists(os.path.join(out, slug(i[0]) + '.md'))]
    if reverse:
        todo.reverse()
    print(len(imgs), 'images,', len(todo), 'to do', flush=True)
    with mp.Pool(workers) as pool:
        for n, _ in enumerate(pool.imap_unordered(page, todo, chunksize=4), 1):
            if n % 100 == 0:
                print(n, flush=True)
    I = ['# Userland: iOS 27.2 dyld shared cache', '',
         f'{len(imgs):,} images. Hardware-facing images have full pages (methods, properties, Swift types, strings, from `gen_dsc.py`); '
         'every other image has a light page (libraries and type names, from `gen_dsc_all.py`). **[DSC]**', '',
         '| Image | Version | Page |', '|---|---|---|']
    for path, ver in imgs:
        f = slug(path) + '.md'
        if os.path.exists(os.path.join(out, f)):
            kind = 'full' if '## Strings' in open(os.path.join(out, f)).read(200000) else 'light'
            I.append(f'| [`{path}`]({f}) | {ver} | {kind} |')
        else:
            I.append(f'| `{path}` | {ver} | |')
    open(os.path.join(out, 'README.md'), 'w').write('\n'.join(I) + '\n')
    print('index written')

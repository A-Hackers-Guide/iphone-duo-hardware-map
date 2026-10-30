"""One page per kernel C++ class (OSMetaClass registration): size, superclass chain, direct and total
subclasses, metaclass/vtable addresses, owning kext, the IOKit personalities that instantiate it and the
device-tree nodes it binds to, plus the kext strings that mention the class by name.

usage: gen_kclasses.py data/kernel-cpp-classes.txt data/kexts-full.json data/adt-nodes.json reference/kexts reference/kclasses
"""
import json
import os
import re
import sys

cpp_path, kexts_path, nodes_path, kext_pages, out = sys.argv[1:6]
os.makedirs(out, exist_ok=True)
CPP = re.compile(r'init=(\S+) size=(\S+) parent=(\S+) meta=(\S+) metavtab=(\S+)(?: vtab=(\S+))? (\S+)\t\((\S+)\)')
cls, by_name = {}, {}
for line in open(cpp_path):
    m = CPP.search(line)
    if m:
        init, size, parent, meta, metavtab, vtab, name, bundle = m.groups()
        cls[meta] = dict(name=name, size=int(size, 16), parent=parent, meta=meta, metavtab=metavtab, vtab=vtab, init=init, bundle=bundle)
        by_name.setdefault(name, meta)
kids = {}
for meta, c in cls.items():
    kids.setdefault(c['parent'], []).append(meta)

pers = {}
for k in json.load(open(kexts_path)):
    for pname, p in (k.get('IOKitPersonalities') or {}).items():
        if isinstance(p, dict) and p.get('IOClass'):
            pers.setdefault(p['IOClass'], []).append((k.get('CFBundleIdentifier'), pname, p))
binds = {}
for n in json.load(open(nodes_path)):
    for d in n['drivers']:
        binds.setdefault(d['class'], []).append((n['path'], d['matched_on']))

# strings per kext page, to find mentions of each class
mentions = {}
for f in os.listdir(kext_pages):
    if f.endswith('.md') and f != 'README.md':
        txt = open(os.path.join(kext_pages, f)).read()
        part = txt.split('## Strings', 1)
        mentions[f[:-3]] = part[1] if len(part) > 1 else ''


def fname(name):
    return re.sub(r'[^A-Za-z0-9_.,+-]', '_', name) + '.md'


def link(meta):
    c = cls[meta]
    return f'[`{c["name"]}`]({fname(c["name"])})'


def node_slug(p):
    s = p.replace('device-tree', 'root').strip('/').replace('/', '__')
    return re.sub(r'[^A-Za-z0-9_.,-]', '_', s)


def descendants(meta):
    out, stack = 0, list(kids.get(meta, []))
    while stack:
        x = stack.pop()
        out += 1
        stack += kids.get(x, [])
    return out


for meta, c in cls.items():
    chain, p, seen = [], c['parent'], set()
    while p in cls and p not in seen:
        seen.add(p)
        chain.append(p)
        p = cls[p]['parent']
    owner = '`com.apple.kernel` (kernel core)' if c['bundle'] == 'com.apple.kernel' else f'[`{c["bundle"]}`](../kexts/{c["bundle"]}.md)'
    L = [f'# `{c["name"]}`', '', 'Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**', '',
         f'- Owner: {owner}', f'- Object size: `{c["size"]:#x}` ({c["size"]:,} bytes)',
         f'- Metaclass: `{c["meta"]}`; metaclass vtable `{c["metavtab"]}`' + (f'; class vtable `{c["vtab"]}`' if c['vtab'] else ' (abstract: no class vtable recorded)'),
         f'- Registration (init): `{c["init"]}`',
         '- Superclasses: ' + (' → '.join(link(x) for x in chain) if chain else 'none registered (derives from a kernel-core root such as OSObject)')]
    k = sorted(kids.get(meta, []), key=lambda m: cls[m]['name'])
    if k:
        L += ['', f'## Direct subclasses ({len(k)}; {descendants(meta)} in total)', ''] + [f'- {link(x)} — `{cls[x]["bundle"]}`' for x in k]
    pp = pers.get(c['name'], [])
    if pp:
        L += ['', f'## IOKit personalities that instantiate it ({len(pp)})', '']
        for bid, pname, p in pp:
            keys = ', '.join(f'`{x}` = `{str(p[x])[:80]}`' for x in ('IOProviderClass', 'IONameMatch', 'IOPropertyMatch', 'IOPCIMatch', 'IOResourceMatch', 'IOMatchCategory', 'IOProbeScore') if x in p)
            L.append(f'- `{pname}` in [`{bid}`](../kexts/{bid}.md): {keys}')
    b = binds.get(c['name'], [])
    if b:
        L += ['', f'## Device-tree nodes it binds ({len(b)}) [DT]', ''] + [f'- [`{p.replace("device-tree", "")}`](../devicetree/{node_slug(p)}.md) on `{on}`' for p, on in b]
    txt = mentions.get(c['bundle'], '')
    hits = [l for l in txt.splitlines() if c['name'] in l][:60]
    if hits:
        L += ['', f'## Strings in its kext that name it ({len(hits)})', ''] + hits
    open(os.path.join(out, fname(c['name'])), 'w').write('\n'.join(L) + '\n')

roots = sorted([m for m, c in cls.items() if c['parent'] not in cls], key=lambda m: cls[m]['name'])
I = ['# Kernel C++ classes', '', f'{len(cls):,} classes, one page each. The [class tree](../maps/kernel-class-tree.md) shows the hierarchy. **[KC]**', '',
     '| Class | Owner | Size | Subclasses | Bound DT nodes |', '|---|---|---|---|---|']
for meta in sorted(cls, key=lambda m: cls[m]['name']):
    c = cls[meta]
    I.append(f'| {link(meta)} | `{c["bundle"]}` | {c["size"]:#x} | {descendants(meta)} | {len(binds.get(c["name"], []))} |')
open(os.path.join(out, 'README.md'), 'w').write('\n'.join(I) + '\n')
print(len(cls), 'class pages')

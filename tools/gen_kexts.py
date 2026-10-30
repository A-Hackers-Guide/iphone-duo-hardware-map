"""Write one Markdown page per kext: plist, personalities, C++ classes, Mach-O layout, strings,
and the device-tree nodes it binds.

usage: gen_kexts.py <decompressed kernelcache> data/kexts-full.json data/kernel-cpp-classes.txt
                    data/devicetree-nodes.json reference/kexts
"""
import json
import os
import re
import subprocess
import sys

kc, full_path, cpp_path, nodes_path, out = sys.argv[1:6]
kexts = json.load(open(full_path))
nodes = json.load(open(nodes_path))
os.makedirs(out, exist_ok=True)
MAX_STRINGS = 3000

# C++ classes: meta address -> name, and per-kext lists
CPP = re.compile(r'init=(\S+) size=(\S+) parent=(\S+) meta=(\S+) metavtab=(\S+)(?: vtab=(\S+))? (\S+)\t\((\S+)\)')
classes, by_meta = {}, {}
for line in open(cpp_path):
    m = CPP.search(line)
    if not m:
        continue
    init, size, parent, meta, metavtab, vtab, name, bundle = m.groups()
    c = dict(name=name, size=int(size, 16), parent=parent, meta=meta, vtab=vtab, bundle=bundle)
    by_meta[meta] = c
    classes.setdefault(bundle, []).append(c)


def chain(c):
    seen, names = set(), []
    while c and c['parent'] in by_meta and c['parent'] not in seen:
        seen.add(c['parent'])
        c = by_meta[c['parent']]
        names.append(c['name'])
    return names


def node_slug(path):
    s = path.replace('device-tree', 'root').strip('/').replace('/', '__')
    return re.sub(r'[^A-Za-z0-9_.,-]', '_', s)


binds = {}
for n in nodes:
    for d in n['drivers']:
        binds.setdefault(d['kext'], []).append((n['path'], d['class'], d['matched_on']))


def ipsw(*args):
    try:
        return subprocess.run(['ipsw', 'macho', 'info', kc, *args], capture_output=True, text=True, timeout=120).stdout
    except subprocess.TimeoutExpired:
        return ''


def fmt(v, depth=0):
    pad = '  ' * depth
    if isinstance(v, dict):
        out = []
        for k in sorted(v):
            x = v[k]
            if isinstance(x, (dict, list)) and x:
                out.append(f'{pad}- `{k}`:')
                out += fmt(x, depth + 1)
            else:
                out.append(f'{pad}- `{k}`: `{x}`')
        return out
    if isinstance(v, list):
        out = []
        for x in v:
            if isinstance(x, (dict, list)):
                out.append(f'{pad}-')
                out += fmt(x, depth + 1)
            else:
                out.append(f'{pad}- `{x}`')
        return out
    return [f'{pad}- `{v}`']


index = []
for k in sorted(kexts, key=lambda k: k.get('CFBundleIdentifier', '')):
    bid = k.get('CFBundleIdentifier', '?')
    L = [f'# `{bid}`', '']
    L.append(f'- Name: {k.get("CFBundleName", "")}')
    L.append(f'- Version: `{k.get("CFBundleVersion", "")}`')
    loads = ipsw('-t', bid, '-l')
    uuid = re.search(r'LC_UUID\s+(\S+)', loads)
    src = re.search(r'LC_SOURCE_VERSION\s+(\S+)', loads)
    if uuid:
        L.append(f'- UUID: `{uuid.group(1)}`')
    if src:
        L.append(f'- Source version: `{src.group(1)}`')
    libs = k.get('OSBundleLibraries') or {}
    if libs:
        L.append('- Depends on: ' + ', '.join(f'[`{x}`]({x}.md) {v}' for x, v in sorted(libs.items())))
    b = binds.get(bid, [])
    L += ['', f'## Device-tree nodes it binds ({len(b)}) [DT][KC]', '']
    if b:
        L += ['| Node | IOClass | matched on |', '|---|---|---|']
        for p, cls, on in b:
            L.append(f'| [`{p.replace("device-tree", "")}`](../devicetree/{node_slug(p)}.md) | `{cls}` | `{on}` |')
    else:
        L.append('None by name match. It matches on a provider class, a property, or is a library.')
    pers = k.get('IOKitPersonalities') or {}
    L += ['', f'## IOKit personalities ({len(pers)}) [KC]', '']
    for name in sorted(pers):
        L.append(f'### {name}')
        L += fmt(pers[name])
        L.append('')
    cl = sorted(classes.get(bid, []), key=lambda c: c['name'])
    L += ['', f'## C++ classes ({len(cl)}) [KC]', '', 'Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).', '',
          '| Class | Size | Superclasses |', '|---|---|---|']
    for c in cl:
        L.append(f'| `{c["name"]}` | {c["size"]:#x} | {" → ".join(chain(c))} |')
    L += ['', '## Mach-O layout [KC]', '', '```']
    L += [l for l in loads.splitlines() if l.strip()][:120]
    L += ['```']
    other = {x: v for x, v in k.items() if x not in ('IOKitPersonalities', 'OSBundleLibraries')}
    L += ['', '## Info.plist keys [KC]', '']
    L += fmt(other)
    strs = ipsw('-t', bid, '--strings')
    sl = []
    section = ''
    for line in strs.splitlines():
        if line.startswith('[') and line.endswith(']'):
            section = line
            sl.append('')
            sl.append(f'**{line}**')
            sl.append('')
            continue
        m = re.match(r'0x[0-9a-f]+: "(.*)"$', line)
        if m:
            sl.append('- `' + m.group(1).replace('`', "'")[:300] + '`')
    n_str = sum(1 for x in sl if x.startswith('- '))
    L += ['', f'## Strings ({n_str}) [KC]', '', 'C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.']
    if n_str > MAX_STRINGS:
        L.append(f'First {MAX_STRINGS} of {n_str}.')
    kept = 0
    for x in sl:
        if x.startswith('- '):
            kept += 1
            if kept > MAX_STRINGS:
                break
        L.append(x)
    open(os.path.join(out, f'{bid}.md'), 'w').write('\n'.join(L) + '\n')
    index.append((bid, k.get('CFBundleVersion', ''), len(b), len(pers), len(cl), n_str))

I = ['# Kernel extension pages', '', f'{len(index)} kexts in `kernelcache.release.v6x-pandia`.', '',
     '| kext | version | DT nodes bound | personalities | C++ classes | strings |', '|---|---|---|---|---|---|']
for bid, v, nb, npers, ncl, ns in index:
    I.append(f'| [`{bid}`]({bid}.md) | {v} | {nb} | {npers} | {ncl} | {ns} |')
open(os.path.join(out, 'README.md'), 'w').write('\n'.join(I) + '\n')
print(len(index), 'kext pages')

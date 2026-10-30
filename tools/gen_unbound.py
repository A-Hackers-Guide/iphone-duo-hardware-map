"""List every device-tree node that has a compatible string but no kernel driver by name match, with what
references it and which chapters discuss it. Writes reference/maps/unbound-nodes.md.

usage: gen_unbound.py data/adt-nodes.json docs reference/maps/unbound-nodes.md
"""
import json
import os
import re
import struct
import sys

nodes_path, docs, out = sys.argv[1:4]
nodes = json.load(open(nodes_path))
ph = {n['phandle']: n['path'] for n in nodes if n['phandle'] is not None}
chapters = {f: open(os.path.join(docs, f)).read() for f in sorted(os.listdir(docs)) if re.match(r'\d\d-.*\.md$', f)}


def slug(p):
    s = p.replace('device-tree', 'root').strip('/').replace('/', '__')
    return re.sub(r'[^A-Za-z0-9_.,-]', '_', s)


refs = {}
for n in nodes:
    for k, p in n['props'].items():
        if k.startswith('function-') and p['len'] >= 8:
            w = struct.unpack('<I', bytes.fromhex(p['hex'])[:4])[0]
            if w in ph:
                refs.setdefault(ph[w], set()).add(n['path'].replace('device-tree', ''))
    ip = n['props'].get('interrupt-parent', {}).get('u32')
    if ip in ph:
        refs.setdefault(ph[ip], set()).add(n['path'].replace('device-tree', ''))

L = ['# Unbound nodes', '', 'Device-tree nodes with a `compatible` string that no kernel personality names. Each is bound some other way '
     '(by its parent driver, a property or provider-class match, a DriverKit extension, an exclave or a co-processor) or not at all. '
     'The chapters column links every chapter that names the node; that is where the explanation is. **[DT][KC]**', '',
     '| Node | compatible | Referenced by | Chapters that discuss it |', '|---|---|---|---|']
count = 0
for n in nodes:
    if not n['compatible'] or n['drivers']:
        continue
    count += 1
    short = n['path'].replace('device-tree', '')
    name = n['name']
    hits = [f for f, t in chapters.items() if short in t or re.search(rf'`{re.escape(name)}`', t)]
    r = sorted(refs.get(n['path'], []))
    L.append(f'| [`{short}`](../devicetree/{slug(n["path"])}.md) | `{", ".join(n["compatible"])}` | '
             f'{", ".join(f"`{x}`" for x in r[:6])}{" …" if len(r) > 6 else ""} | {", ".join(f"[{f[:2]}](../../docs/{f})" for f in hits) or "—"} |')
L.insert(3, f'{count} nodes.')
open(out, 'w').write('\n'.join(L) + '\n')
print(count)

"""Property dictionary: every distinct device-tree property name, how many nodes carry it, the value shapes seen,
and up to five example nodes with values. Writes reference/maps/property-index.md.

usage: gen_propindex.py data/adt-nodes.json reference/maps/property-index.md
"""
import collections
import json
import re
import sys

nodes = json.load(open(sys.argv[1]))
idx = collections.defaultdict(list)
for n in nodes:
    for k, p in n['props'].items():
        idx[k].append((n['path'], p))


def slug(p):
    s = p.replace('device-tree', 'root').strip('/').replace('/', '__')
    return re.sub(r'[^A-Za-z0-9_.,-]', '_', s)


def shape(p):
    if 'str' in p and not (p['len'] == 4 and isinstance(p['str'], str) and len(p['str']) < 3):
        return 'string'
    if p['len'] == 0:
        return 'empty'
    if p['len'] == 4:
        return 'u32'
    if p['len'] == 8:
        return 'u64'
    return f'{p["len"]} B'


def val(p):
    if 'str' in p and not (p['len'] == 4 and isinstance(p['str'], str) and len(p['str']) < 3):
        s = p['str']
        return (', '.join(s) if isinstance(s, list) else s)[:60]
    if 'u32' in p:
        return f'{p["u32"]:#x}'
    if 'u64' in p:
        return f'{p["u64"]:#x}'
    return p['hex'][:32] + ('…' if p['len'] > 16 else '')


L = ['# Device-tree property dictionary', '', f'{len(idx):,} distinct property names across {len(nodes)} nodes. '
     'Shapes are inferred from length and content (string, u32, u64, empty or N bytes). **[DT]**', '',
     '| Property | Nodes | Shapes | Examples |', '|---|---|---|---|']
for k in sorted(idx, key=lambda x: x.lower()):
    rows = idx[k]
    shapes = collections.Counter(shape(p) for _, p in rows)
    ex = '<br>'.join(f'[`{path.replace("device-tree", "") or "/"}`](../devicetree/{slug(path)}.md) = `{val(p).replace("|", "/")}`' for path, p in rows[:5])
    L.append(f'| `{k}` | {len(rows)} | {", ".join(f"{s}×{c}" if c > 1 else s for s, c in shapes.most_common(3))} | {ex} |')
open(sys.argv[2], 'w').write('\n'.join(L) + '\n')
print(len(idx))

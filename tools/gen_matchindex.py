"""Inverse match table: every IONameMatch string in the kernelcache, the driver class and kext that match it, and the
V68 device-tree nodes that carry it. Strings with no node mark drivers shipped for hardware this board does not have.
Writes reference/maps/driver-matches.md.

usage: gen_matchindex.py data/kexts-full.json data/adt-nodes.json reference/maps/driver-matches.md
"""
import json
import re
import sys

kexts = json.load(open(sys.argv[1]))
nodes = json.load(open(sys.argv[2]))
by_str = {}
for n in nodes:
    for s in n['compatible'] + [n['name']]:
        by_str.setdefault(s, []).append(n['path'])
rows = []
for k in kexts:
    for pname, p in (k.get('IOKitPersonalities') or {}).items():
        if not isinstance(p, dict) or 'IONameMatch' not in p:
            continue
        nm = p['IONameMatch']
        for s in nm if isinstance(nm, list) else [nm]:
            rows.append((s, p.get('IOClass', ''), k.get('CFBundleIdentifier', ''), sorted(set(by_str.get(s, [])))))


def slug(p):
    s = p.replace('device-tree', 'root').strip('/').replace('/', '__')
    return re.sub(r'[^A-Za-z0-9_.,-]', '_', s)


present = [r for r in rows if r[3]]
absent = [r for r in rows if not r[3]]
L = ['# Driver match table', '', f'{len(rows):,} `IONameMatch` entries ({len({r[0] for r in rows}):,} distinct strings) in top-level kext personalities. '
     f'{len(present):,} entries ({len({r[0] for r in present}):,} distinct strings) match a node on the Duo; '
     f'{len(absent):,} match nothing on this board — drivers shipped in the shared kernelcache for hardware the Duo does not have '
     '(or that is matched another way). **[KC][DT]**', '',
     '## Matched on the Duo', '', '| Match string | IOClass | kext | Nodes |', '|---|---|---|---|']
for s, c, k, ns in sorted(present):
    L.append(f'| `{s}` | `{c}` | [`{k}`](../kexts/{k}.md) | {", ".join(f"[`{x.replace('device-tree', '') or '/'}`](../devicetree/{slug(x)}.md)" for x in ns[:6])}{" …" if len(ns) > 6 else ""} |')
L += ['', '## No node on the Duo', '', '| Match string | IOClass | kext |', '|---|---|---|']
L += [f'| `{s}` | `{c}` | [`{k}`](../kexts/{k}.md) |' for s, c, k, _ in sorted(absent)]
open(sys.argv[3], 'w').write('\n'.join(L) + '\n')
print(len(present), 'present', len(absent), 'absent')

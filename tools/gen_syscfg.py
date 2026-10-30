"""syscfg key map: every device-tree property whose value points at factory data (syscfg/, macaddr/, zeroes/ and
similar provider strings), grouped by key. These are filled in by iBoot from the device's factory-written syscfg
store at boot. Writes reference/maps/syscfg-keys.md.

usage: gen_syscfg.py data/adt-nodes.json reference/maps/syscfg-keys.md
"""
import collections
import json
import re
import sys

nodes = json.load(open(sys.argv[1]))
keys = collections.defaultdict(list)
for n in nodes:
    for k, p in n['props'].items():
        s = p.get('str')
        for v in (s if isinstance(s, list) else [s] if s else []):
            for m in re.finditer(r'(syscfg(?:-mismatch)?|macaddr|zeroes)/([^,/\s]+)(?:/([^,\s]+))?', v):
                keys[(m.group(1), m.group(2))].append((n['path'].replace('device-tree', '') or '/', k, v))


def slug(p):
    s = ('device-tree' + p if p != '/' else 'device-tree').replace('device-tree', 'root').strip('/').replace('/', '__')
    return re.sub(r'[^A-Za-z0-9_.,-]', '_', s)


nsys = sum(1 for (src, _) in keys if src == 'syscfg')
nother = {s: sum(1 for (src, _) in keys if src == s) for s in ('macaddr', 'syscfg-mismatch', 'zeroes')}
L = ['# syscfg key map', '', f'{nsys} syscfg keys are referenced by the device tree ({len(keys)} entries in all, counting {nother["macaddr"]} `macaddr/` aliases, {nother["syscfg-mismatch"]} `syscfg-mismatch/` fallbacks and {nother["zeroes"]} `zeroes/` length fillers, which are not keys). A value like `syscfg/WMac/6` means '
     '"fill this property from syscfg key `WMac`, 6 bytes"; iBoot does the fill at boot. The keys themselves are written at the factory '
     '(see [chapter 13](../../docs/13-lifecycle.md)). **[DT]**', '', '| Source | Key | Consumer node | Property | Full value |', '|---|---|---|---|---|']
for (src, key), uses in sorted(keys.items(), key=lambda x: (x[0][0], x[0][1].lower())):
    for path, prop, v in uses:
        L.append(f'| `{src}` | `{key}` | [`{path}`](../devicetree/{slug(path)}.md) | `{prop}` | `{v[:120]}` |')
open(sys.argv[2], 'w').write('\n'.join(L) + '\n')
print(len(keys), 'keys', sum(len(v) for v in keys.values()), 'uses')

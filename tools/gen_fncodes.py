"""Catalog every four-character function code used in device-tree function-* properties: provider, the function
names that use it, how many consumers, and example arguments. Writes reference/maps/function-codes.md.

usage: gen_fncodes.py data/adt-nodes.json reference/maps/function-codes.md
"""
import json
import re
import struct
import sys

nodes = json.load(open(sys.argv[1]))
ph = {n['phandle']: n['path'] for n in nodes if n['phandle'] is not None}
codes = {}
for n in nodes:
    for k, p in n['props'].items():
        if not k.startswith('function-') or p['len'] < 8:
            continue
        b = bytes.fromhex(p['hex'])
        w = struct.unpack(f'<{len(b) // 4}I', b[:len(b) // 4 * 4])
        code = struct.pack('<I', w[1])[::-1].decode('latin-1')
        prov = ph.get(w[0], f'phandle {w[0]}').replace('device-tree', '') or '/'
        e = codes.setdefault((code, prov), {'names': set(), 'consumers': set(), 'args': []})
        e['names'].add(k[9:])
        e['consumers'].add(n['path'].replace('device-tree', ''))
        if len(e['args']) < 3 and len(w) > 2:
            e['args'].append(' '.join(f'{x:#x}' for x in w[2:6]))


def slug(p):
    s = ('device-tree' + p).replace('device-tree', 'root').strip('/').replace('/', '__')
    return re.sub(r'[^A-Za-z0-9_.,-]', '_', s)


L = ['# Function codes', '', 'Every four-character code used in `function-*` properties, grouped by provider. The provider driver implements '
     'the code; consumers call it with the arguments shown (first three examples). Codes are shown in readable byte order. **[DT]**', '',
     f'{len(codes)} distinct (code, provider) pairs.', '',
     '| Code | Provider | Function names | Consumers | Example arguments |', '|---|---|---|---|---|']
for (code, prov), e in sorted(codes.items(), key=lambda x: (x[0][1], x[0][0])):
    pl = f'[`{prov}`](../devicetree/{slug(prov)}.md)' if not prov.startswith('phandle') else prov
    L.append(f'| `{code}` | {pl} | {", ".join(f"`{x}`" for x in sorted(e["names"])[:8])} | {len(e["consumers"])} | '
             f'{"; ".join(f"`{a}`" for a in e["args"])} |')
open(sys.argv[2], 'w').write('\n'.join(L) + '\n')
print(len(codes))

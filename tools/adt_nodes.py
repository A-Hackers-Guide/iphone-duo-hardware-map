"""Flatten adt.py output into one record per node and match each node to kext personalities.

usage: adt_nodes.py adt.json data/kexts.json data/adt-nodes.json
"""
import json
import sys

tree = json.load(open(sys.argv[1]))
kexts = json.load(open(sys.argv[2]))

match = {}
for k in kexts:
    for p in k['personalities'].values():
        nm = p.get('IONameMatch')
        if nm is None:
            continue
        for s in nm if isinstance(nm, list) else [nm]:
            match.setdefault(s, []).append({'kext': k['id'], 'class': p.get('IOClass'), 'provider': p.get('IOProviderClass')})

nodes = []


def strs(p):
    if not p:
        return []
    s = p.get('str')
    return s if isinstance(s, list) else ([s] if s else [])


def walk(n, path, parent):
    name = strs(n['props'].get('name'))
    name = name[0] if name else '?'
    path = f'{path}/{name}' if path else 'device-tree'
    comp = strs(n['props'].get('compatible'))
    drv = []
    for s in comp + [name]:
        drv += [dict(x, matched_on=s) for x in match.get(s, [])]
    nodes.append({'path': path, 'parent': parent, 'name': name, 'compatible': comp,
                  'device_type': (strs(n['props'].get('device_type')) or [None])[0],
                  'phandle': n['props'].get('AAPL,phandle', {}).get('u32'),
                  'props': n['props'], 'drivers': drv})
    for c in n['children']:
        walk(c, path, path)


walk(tree, '', None)
json.dump(nodes, open(sys.argv[3], 'w'), indent=0)
print(len(nodes), 'nodes', sum(1 for n in nodes if n['drivers']), 'with drivers')

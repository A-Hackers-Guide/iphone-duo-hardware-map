"""Print the whole device tree as indented text, every property exact (string, integer, or full hex).

usage: adt_dump.py data/adt-nodes.json > data/devicetree-exact.txt
"""
import json
import sys

nodes = json.load(open(sys.argv[1]))
for n in nodes:
    depth = n['path'].count('/')
    pad = '  ' * depth
    print(f'{pad}{n["name"]}:')
    for k in sorted(n['props']):
        p = n['props'][k]
        flag = '  [placeholder]' if p.get('placeholder') else ''
        if 'str' in p and not (p['len'] == 4 and isinstance(p['str'], str) and len(p['str']) < 3):
            s = p['str']
            v = ' | '.join(f'"{x}"' for x in s) if isinstance(s, list) else f'"{s}"'
        elif 'u32' in p:
            v = f'{p["u32"]:#x}'
        elif 'u64' in p:
            v = f'{p["u64"]:#x} (u64)'
        elif p['len'] == 0:
            v = '<empty>'
        else:
            v = f'<{p["len"]} bytes> {p["hex"]}'
        print(f'{pad}  {k} = {v}{flag}')

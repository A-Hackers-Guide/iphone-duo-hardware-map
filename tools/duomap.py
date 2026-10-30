#!/usr/bin/env python3
"""duomap: query the iPhone Duo hardware map from the command line.

  duomap.py node <name-or-path>        every property of a node, decoded
  duomap.py find <regex>               nodes whose path, compatible or property names match
  duomap.py driver <IOClass|kext>      which nodes a driver binds, and through which compatible
  duomap.py who <compatible>           which driver binds a compatible string
  duomap.py irq <number>               which nodes use an interrupt line
  duomap.py addr <hex address>         which register window contains a physical address
  duomap.py fn <function-name|code>    which nodes call a function, on which provider
  duomap.py refs <name-or-path>        what references a node (functions, interrupts, phandles)
  duomap.py fw <regex>                 firmware images whose name matches
  duomap.py unbound                    nodes with a compatible string but no kernel driver

Reads data/adt-nodes.json, data/kexts.json and data/firmware-inventory.tsv relative to the repo root.
"""
import json
import os
import re
import struct
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load():
    nodes = json.load(open(os.path.join(ROOT, 'data', 'adt-nodes.json')))
    return nodes, {n['path']: n for n in nodes}, {n['phandle']: n['path'] for n in nodes if n['phandle'] is not None}


def short(p):
    return p.replace('device-tree', '') or '/'


def raw(p):
    return bytes.fromhex(p['hex'])


def resolve(by_path, q):
    if q in by_path:
        return by_path[q]
    for cand in ('device-tree' + q, 'device-tree/' + q.lstrip('/')):
        if cand in by_path:
            return by_path[cand]
    hits = [n for n in by_path.values() if n['name'] == q]
    if len(hits) == 1:
        return hits[0]
    if hits:
        sys.exit('ambiguous: ' + ', '.join(short(h['path']) for h in hits))
    sys.exit(f'no node {q!r}')


def value(p):
    if 'str' in p and not (p['len'] == 4 and isinstance(p['str'], str) and len(p['str']) < 3):
        return p['str']
    if 'u32' in p:
        return f'{p["u32"]} ({p["u32"]:#x})'
    if 'u64' in p:
        return f'{p["u64"]:#x}'
    if p['len'] == 0:
        return '(empty)'
    if 'u32s' in p and p['len'] <= 128:
        return ' '.join(f'{x:#x}' for x in p['u32s'])
    return f'{p["len"]} bytes: {p["hex"][:96]}{"…" if p["len"] > 48 else ""}'


def functions(n, ph):
    for k, p in n['props'].items():
        if k.startswith('function-') and p['len'] >= 8:
            w = struct.unpack(f'<{p["len"] // 4}I', raw(p)[:p['len'] // 4 * 4])
            code = struct.pack('<I', w[1])[::-1].decode('latin-1')
            yield k[9:], ph.get(w[0]), code, w[2:]


def irqs(n, ph):
    p = n['props'].get('interrupts')
    if not p or p['len'] % 4:
        return [], None
    return list(struct.unpack(f'<{p["len"] // 4}I', raw(p))), ph.get(n['props'].get('interrupt-parent', {}).get('u32'))


def main(argv):
    if len(argv) < 2 or argv[1] in ('-h', '--help'):
        print(__doc__)
        return
    cmd, args = argv[1], argv[2:]
    nodes, by_path, ph = load()
    if cmd == 'node':
        n = resolve(by_path, args[0])
        print(short(n['path']), '|', ', '.join(n['compatible']))
        for d in n['drivers']:
            print(f'  driver: {d["class"]} ({d["kext"]})')
        for k in sorted(n['props']):
            print(f'  {k} = {value(n["props"][k])}')
    elif cmd == 'find':
        rx = re.compile(args[0], re.I)
        for n in nodes:
            if rx.search(n['path']) or any(rx.search(c) for c in n['compatible']) or any(rx.search(k) for k in n['props']):
                print(short(n['path']), '|', ', '.join(n['compatible']))
    elif cmd == 'driver':
        q = args[0]
        for n in nodes:
            for d in n['drivers']:
                if q in (d['class'], d['kext']) or q in d['kext']:
                    print(f'{short(n["path"])}  ← {d["class"]} ({d["kext"]}) on {d["matched_on"]!r}')
    elif cmd == 'who':
        for n in nodes:
            if args[0] in n['compatible']:
                print(short(n['path']), '→', ', '.join(f'{d["class"]} ({d["kext"]})' for d in n['drivers']) or 'no kernel driver')
    elif cmd == 'irq':
        want = int(args[0], 0)
        for n in nodes:
            ir, par = irqs(n, ph)
            if want in ir:
                print(f'{short(n["path"])} index {ir.index(want)} on {short(par) if par else "?"}')
    elif cmd == 'addr':
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        want = int(args[0], 16)
        table = os.path.join(ROOT, 'reference', 'maps', 'physical-address-map.md')
        for line in open(table):
            m = re.match(r'\| `(0x[0-9a-f]+)` \| `(0x[0-9a-f]+)` \| `[^`]*` \| \[`([^`]+)`\]', line)
            if m and int(m.group(1), 16) <= want <= int(m.group(2), 16):
                print(m.group(3), m.group(1), '-', m.group(2))
    elif cmd == 'fn':
        q = args[0]
        for n in nodes:
            for name, prov, code, a in functions(n, ph):
                if q in (name, code) or re.search(q, name):
                    print(f'{short(n["path"])}  {name} [{code}] → {short(prov) if prov else "?"} {" ".join(f"{x:#x}" for x in a)}')
    elif cmd == 'refs':
        t = resolve(by_path, args[0])['path']
        for n in nodes:
            for name, prov, code, a in functions(n, ph):
                if prov == t:
                    print(f'{short(n["path"])} calls function-{name} [{code}]')
            ir, par = irqs(n, ph)
            if par == t and ir:
                print(f'{short(n["path"])} uses interrupts {ir}')
    elif cmd == 'fw':
        rx = re.compile(args[0], re.I)
        for line in open(os.path.join(ROOT, 'data', 'firmware-inventory.tsv')):
            if rx.search(line):
                print(line.rstrip())
    elif cmd == 'unbound':
        for n in nodes:
            if n['compatible'] and not n['drivers']:
                print(short(n['path']), '|', ', '.join(n['compatible']))
    else:
        sys.exit(f'unknown command {cmd!r}; see --help')


if __name__ == '__main__':
    main(sys.argv)

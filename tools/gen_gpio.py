"""GPIO pin map: every function-* reference whose provider is a GPIO controller, sorted by controller and pin.
The first argument after the function code is the pin number; the rest are flags/config words.
Also lists GPIO interrupts (nodes whose interrupt-parent is a GPIO controller). Writes reference/maps/gpio-pins.md.

usage: gen_gpio.py data/adt-nodes.json reference/maps/gpio-pins.md
"""
import json
import re
import struct
import sys

nodes = json.load(open(sys.argv[1]))
ph = {n['phandle']: n['path'] for n in nodes if n['phandle'] is not None}
gpio = {n['path'] for n in nodes if (any(c.startswith('gpio') for c in n['compatible']) or n['name'].endswith('gpio')) and n['name'] != 'gpio-canary'}


def slug(p):
    s = p.replace('device-tree', 'root').strip('/').replace('/', '__')
    return re.sub(r'[^A-Za-z0-9_.,-]', '_', s)


def short(p):
    return p.replace('device-tree', '')


pins, irqs = {}, {}
for n in nodes:
    for k, p in n['props'].items():
        if k.startswith('function-') and p['len'] >= 12:
            b = bytes.fromhex(p['hex'])
            w = struct.unpack(f'<{len(b) // 4}I', b[:len(b) // 4 * 4])
            prov = ph.get(w[0])
            if prov in gpio:
                code = struct.pack('<I', w[1])[::-1].decode('latin-1')
                pins.setdefault(prov, []).append((w[2], n['path'], k[9:], code, w[3:]))
    ip = n['props'].get('interrupt-parent', {}).get('u32')
    if ph.get(ip) in gpio and 'interrupts' in n['props'] and n['props']['interrupts']['len'] % 4 == 0:
        b = bytes.fromhex(n['props']['interrupts']['hex'])
        irqs.setdefault(ph[ip], []).append((n['path'], struct.unpack(f'<{len(b) // 4}I', b)))

L = ['# GPIO pin map', '', 'GPIO pins assigned through `function-*` references and GPIO interrupts, per controller. `gpio-*` properties are decoded separately in the section "Pins named by `gpio-*` properties" below. For `function-*` references the first argument is read '
     'as the pin number and the remaining words as configuration/flags; for GPIO interrupts the interrupt words are shown raw '
     '(pin, then trigger flags). Physical pad names and board routing are not in the evidence. **[DT]**', '']
for g in sorted(gpio):
    p = sorted(pins.get(g, []))
    q = irqs.get(g, [])
    if not p and not q:
        continue
    L += ['', f'## [`{short(g)}`](../devicetree/{slug(g)}.md)', '']
    if p:
        L += [f'{len(p)} pin functions.', '', '| Pin | Device | Function | Code | Config words |', '|---|---|---|---|---|']
        L += [f'| {pin} | [`{short(d)}`](../devicetree/{slug(d)}.md) | `{fn}` | `{code}` | `{" ".join(f"{x:#x}" for x in rest)}` |' for pin, d, fn, code, rest in p]
    if q:
        L += ['', f'{len(q)} devices take interrupts from this controller.', '', '| Device | Interrupt words |', '|---|---|']
        L += [f'| [`{short(d)}`](../devicetree/{slug(d)}.md) | `{" ".join(str(x) for x in w)}` |' for d, w in q]
# controller sizes
L += ['', '## Controller sizes', '', '| Controller | `#gpio-pins` | `#gpio-int-groups` |', '|---|---|---|']
for n in nodes:
    if '#gpio-pins' in n['props']:
        L.append(f'| [`{short(n["path"])}`](../devicetree/{slug(n["path"])}.md) | {n["props"]["#gpio-pins"].get("u32")} | {n["props"].get("#gpio-int-groups", {}).get("u32", "")} |')
# gpio-<name> properties: <pin u32> <flags u32> <controller tag>
L += ['', '## Pins named by `gpio-*` properties', '', 'Layout: pin number, a flags word, then a controller tag (`AP` = the AP GPIO block, `AOP` = the always-on block).', '',
      '| Device | Property | Controller tag | Pin | Flags |', '|---|---|---|---|---|']
for n in nodes:
    for k, p in sorted(n['props'].items()):
        if k.startswith('gpio-') and p['len'] == 12:
            b = bytes.fromhex(p['hex'])
            pin, flags = struct.unpack('<II', b[:8])
            tag = b[8:].split(b'\0')[0].decode('latin-1')
            L.append(f'| [`{short(n["path"])}`](../devicetree/{slug(n["path"])}.md) | `{k}` | `{tag}` | {pin} | `{flags:#010x}` |')
# PMU GPIO event names
ev = [(n['path'], k, p.get('str')) for n in nodes for k, p in n['props'].items() if k.startswith('event_name-gpio')]
if ev:
    L += ['', '## PMU GPIO event names', '', '| Device | GPIO | Event |', '|---|---|---|']
    L += [f'| [`{short(d)}`](../devicetree/{slug(d)}.md) | {k.split("gpio")[-1]} | `{v}` |' for d, k, v in sorted(ev, key=lambda x: int(re.sub(r'\D', '', x[1]) or 0))]
open(sys.argv[2], 'w').write('\n'.join(L) + '\n')
print(sum(len(v) for v in pins.values()), 'pin functions,', sum(len(v) for v in irqs.values()), 'gpio interrupts')

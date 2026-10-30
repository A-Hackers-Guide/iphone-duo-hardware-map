"""Cross-cutting maps built from the device tree and kernelcache: MMIO address map, interrupt map,
function (power/clock/reset/GPIO) references, bus device map, and the kernel C++ class tree.

usage: gen_maps.py data/devicetree-nodes.json data/kernel-cpp-classes.txt reference/maps
"""
import base64
import json
import os
import re
import struct
import sys

nodes_path, cpp_path, out = sys.argv[1:4]
nodes = json.load(open(nodes_path))
os.makedirs(out, exist_ok=True)
by_path = {n['path']: n for n in nodes}
phandle = {}
for n in nodes:
    ph = n['props'].get('AAPL,phandle')
    try:
        phandle[int(ph)] = n['path']
    except (TypeError, ValueError):
        pass


def short(p):
    return p.replace('device-tree', '') or '/'


def slug(p):
    s = p.replace('device-tree', 'root').strip('/').replace('/', '__')
    return re.sub(r'[^A-Za-z0-9_.,-]', '_', s)


def link(p):
    return f'[`{short(p)}`](../devicetree/{slug(p)}.md)'


def blob(v):
    if not isinstance(v, str) or len(v) % 4 or len(v) < 4:
        return None
    try:
        return base64.b64decode(v, validate=True)
    except Exception:
        return None


def drivers(n):
    return ', '.join(sorted({d['class'] for d in n['drivers']}))


# ---------------- MMIO map ----------------
arm = by_path['device-tree/arm-io']['props']
rb = blob(arm.get('ranges'))
ranges = []
if rb:
    for i in range(0, len(rb) - 23, 24):
        c, p, s = struct.unpack_from('<QQQ', rb, i)
        ranges.append((c, p, s))


def to_abs(a):
    for c, p, s in ranges:
        if c <= a < c + s:
            return p + (a - c)
    return None


rows = []
for n in nodes:
    reg = n['props'].get('reg')
    if not (isinstance(reg, list) and reg and isinstance(reg[0], dict)):
        continue
    under_arm = n['path'].startswith('device-tree/arm-io/') and n['path'].count('/') == 2
    for i, r in enumerate(reg):
        a, s = r.get('addr', 0), r.get('size', 0)
        ab = to_abs(a) if under_arm else None
        rows.append((ab if ab is not None else a, s, n, i, ab is not None))
rows.sort(key=lambda r: r[0])
L = ['# MMIO address map', '',
     'Every `reg` range in the device tree, sorted by address. For direct children of `/arm-io`, addresses are translated '
     'to CPU physical addresses through `/arm-io`\'s `ranges` property; others are shown in their parent bus\'s address space '
     '(e.g. an I2C or SPMI device address packed into the field). **[DT]**', '',
     f'`/arm-io` ranges ({len(ranges)} windows):', '', '| Child base | CPU physical base | Size |', '|---|---|---|']
for c, p, s in ranges:
    L.append(f'| `{c:#x}` | `{p:#x}` | `{s:#x}` ({s / 2**20:,.0f} MiB) |')
L += ['', f'{len(rows)} register windows.', '', '| Address | End | Size | Node | # | Translated | Driver |', '|---|---|---|---|---|---|---|']
for a, s, n, i, tr in rows:
    L.append(f'| `{a:#x}` | `{a + s - 1 if s else a:#x}` | `{s:#x}` | {link(n["path"])} | {i} | {"yes" if tr else "bus-local"} | {drivers(n)} |')
open(os.path.join(out, 'mmio-map.md'), 'w').write('\n'.join(L) + '\n')

# ---------------- interrupt map ----------------
irqs = []
for n in nodes:
    b = blob(n['props'].get('interrupts'))
    par = n['props'].get('interrupt-parent')
    try:
        parp = phandle.get(int(par))
    except (TypeError, ValueError):
        parp = None
    if b and len(b) % 4 == 0:
        for j, w in enumerate(struct.unpack(f'<{len(b) // 4}I', b)):
            irqs.append((w, n, j, parp))
    elif isinstance(n['props'].get('interrupts'), int):
        irqs.append((n['props']['interrupts'], n, 0, parp))
irqs.sort(key=lambda x: (x[3] or '', x[0]))
L = ['# Interrupt map', '', 'Every interrupt line a node declares, grouped by interrupt controller (`interrupt-parent` phandle), '
     'sorted by number. Lines under the AIC are SoC interrupts; lines under a GPIO controller are GPIO pin interrupts. **[DT]**', '']
cur = object()
for w, n, j, parp in irqs:
    if parp != cur:
        cur = parp
        L += ['', f'## Controller: {link(parp) if parp else "(none / unresolved)"}', '', '| IRQ | Node | Index | Driver |', '|---|---|---|---|']
    L.append(f'| {w} (`{w:#x}`) | {link(n["path"])} | {j} | {drivers(n)} |')
open(os.path.join(out, 'interrupt-map.md'), 'w').write('\n'.join(L) + '\n')

# ---------------- function references ----------------
fn = []
for n in nodes:
    for k, v in n['props'].items():
        if not k.startswith('function-'):
            continue
        vals = v if isinstance(v, list) else [v]
        ph = None
        try:
            ph = phandle.get(int(vals[0]))
        except (TypeError, ValueError, IndexError):
            pass
        fn.append((k[9:], n, ph, vals))
fn.sort(key=lambda x: (x[0], x[1]['path']))
L = ['# Function references (power, clock, reset, GPIO, PMU and other cross-node calls)', '',
     'Apple device trees express "this device needs that controller to do X" as `function-<name>` properties: a provider '
     'phandle, a four-character function code (stored byte-reversed, e.g. `Grwp` = `pwrG`), and arguments. This table lists '
     'every one, which is the closest thing in the evidence to the board\'s control wiring. **[DT]**', '',
     f'{len(fn)} references.', '', '| Function | Consumer node | Provider node | Raw value |', '|---|---|---|---|']
for name, n, ph, vals in fn:
    raw = ', '.join(str(x) for x in vals)
    L.append(f'| `{name}` | {link(n["path"])} | {link(ph) if ph else "?"} | `{raw[:160].replace("|", "/")}` |')
open(os.path.join(out, 'function-references.md'), 'w').write('\n'.join(L) + '\n')

# ---------------- bus devices ----------------
BUS = re.compile(r'/(i2c\d*|spi\d*|spmi\d*|uart\d*|[a-z]*-spmi\d*|nub-spmi\d*|aop-spmi\d*|.*i2c.*|.*spi.*)$')
L = ['# Bus device map', '', 'Every child of an I2C, SPI, SPMI or UART controller: the chips the SoC talks to over a serial bus. '
     'The `reg` field is the device\'s bus address (packed by the dump; shown raw). **[DT]**', '']
for n in nodes:
    if n['path'].count('/') != 2 or not BUS.search(n['path']):
        continue
    kids = [m for m in nodes if m['parent'] == n['path']]
    L += ['', f'## {link(n["path"])} — {", ".join(n["compatible"])} — {drivers(n)}', '']
    if not kids:
        L.append('No child devices.')
        continue
    L += ['| Device | compatible | reg (raw) | Driver | Notable properties |', '|---|---|---|---|---|']
    for m in kids:
        notable = [k for k in m['props'] if not k.startswith(('AAPL', 'function-', 'compatible', 'name', 'reg', 'interrupt'))][:12]
        L.append(f'| {link(m["path"])} | {", ".join(m["compatible"])} | `{str(m["props"].get("reg"))[:40]}` | {drivers(m)} | {", ".join("`" + x + "`" for x in notable)} |')
open(os.path.join(out, 'bus-devices.md'), 'w').write('\n'.join(L) + '\n')

# ---------------- kernel class tree ----------------
CPP = re.compile(r'size=(\S+) parent=(\S+) meta=(\S+) .*? (\S+)\t\((\S+)\)')
cls = {}
for line in open(cpp_path):
    m = CPP.search(line)
    if m:
        size, parent, meta, name, bundle = m.groups()
        cls[meta] = (name, parent, int(size, 16), bundle)
kids = {}
for meta, (name, parent, size, bundle) in cls.items():
    kids.setdefault(parent if parent in cls else None, []).append(meta)
L = ['# Kernel C++ class tree', '', f'All {len(cls)} OSMetaClass-registered classes in the kernelcache, as an inheritance tree, '
     'with object size and owning kext. Roots are classes whose superclass is in the kernel core (not registered here) or OSObject. **[KC]**', '']


def walk(meta, depth):
    name, parent, size, bundle = cls[meta]
    owner = f'`{bundle}` (kernel core)' if bundle == 'com.apple.kernel' else f'[`{bundle}`](../kexts/{bundle}.md)'
    L.append('  ' * depth + f'- `{name}` ({size:#x} bytes) — {owner}')
    for k in sorted(kids.get(meta, []), key=lambda m: cls[m][0]):
        walk(k, depth + 1)


for r in sorted(kids.get(None, []), key=lambda m: cls[m][0]):
    walk(r, 0)
open(os.path.join(out, 'kernel-class-tree.md'), 'w').write('\n'.join(L) + '\n')
print('maps written', len(rows), 'mmio', len(irqs), 'irqs', len(fn), 'functions', len(cls), 'classes')

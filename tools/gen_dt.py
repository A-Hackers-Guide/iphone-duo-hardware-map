"""Generate the device-tree reference from the exact parse (adt_nodes.py output):
one page per node, plus the MMIO, interrupt, function-reference, phandle and bus maps.

usage: gen_dt.py data/adt-nodes.json data/firmware-inventory.tsv reference
"""
import json
import os
import re
import struct
import sys

nodes_path, fw_path, ref = sys.argv[1:4]
nodes = json.load(open(nodes_path))
firmware = [l.split('\t') for l in open(fw_path).read().splitlines()]
DT, MAPS = os.path.join(ref, 'devicetree'), os.path.join(ref, 'maps')
os.makedirs(DT, exist_ok=True)
os.makedirs(MAPS, exist_ok=True)

by_path = {n['path']: n for n in nodes}
kids = {}
for n in nodes:
    kids.setdefault(n['parent'], []).append(n['path'])
ph = {n['phandle']: n['path'] for n in nodes if n['phandle'] is not None}


def short(p):
    return p.replace('device-tree', '') or '/'


def slug(p):
    s = p.replace('device-tree', 'root').strip('/').replace('/', '__')
    return re.sub(r'[^A-Za-z0-9_.,-]', '_', s)


def link(p, up=False):
    pre = '../devicetree/' if up else ''
    return f'[`{short(p)}`]({pre}{slug(p)}.md)'


def drivers(n):
    return ', '.join(sorted({d['class'] for d in n['drivers']}))


def raw(p):
    return bytes.fromhex(p['hex'])


def cells(path, key, default):
    n = by_path.get(path)
    if n and key in n['props'] and 'u32' in n['props'][key]:
        return n['props'][key]['u32']
    return default


def fourcc(w):
    """Apple stores four-character codes little-endian; show both byte orders."""
    b = struct.pack('<I', w)
    if all(32 <= c < 127 for c in b):
        return b.decode(), b[::-1].decode()
    return None


# ----- address translation: walk up through every 'ranges' -----
def parse_ranges(path):
    n = by_path.get(path)
    if not n or 'ranges' not in n['props'] or not n['props']['ranges']['len']:
        return None
    b = raw(n['props']['ranges'])
    ca = cells(path, '#address-cells', 2)
    pa = cells(n['parent'], '#address-cells', 2) if n['parent'] else 2
    sc = cells(path, '#size-cells', 2)
    step = 4 * (ca + pa + sc)
    out = []
    for i in range(0, len(b) - step + 1, step):
        w = struct.unpack_from(f'<{ca + pa + sc}I', b, i)

        def num(ws):
            v = 0
            for x in reversed(ws):
                v = (v << 32) | x
            return v
        out.append((num(w[:ca]), num(w[ca:ca + pa]), num(w[ca + pa:])))
    return out


RANGES = {}


def translate(path, addr):
    """Translate an address in node `path`'s parent bus to a CPU physical address, if every hop has ranges."""
    p = by_path[path]['parent']
    while p and p != 'device-tree':
        if p not in RANGES:
            RANGES[p] = parse_ranges(p)
        r = RANGES[p]
        if r is None:
            return None
        for c, pa, s in r:
            if c <= addr < c + s:
                addr = pa + (addr - c)
                break
        else:
            return None
        p = by_path[p]['parent']
    return addr


def regs(n):
    if 'reg' not in n['props']:
        return []
    b = raw(n['props']['reg'])
    par = by_path.get(n['parent'])
    if par is None or '#address-cells' not in par['props']:
        # bus children (I2C, SPI, SPMI...) pack their own layout; show the words, not a guess
        return [('raw', ' '.join(f'{w:#x}' for w in struct.unpack(f'<{len(b) // 4}I', b[:len(b) // 4 * 4])))]
    ac = cells(n['parent'], '#address-cells', 2)
    sc = cells(n['parent'], '#size-cells', 2)
    if ac > 2 or sc > 2:
        # Apple buses such as SPI use extra 'size' cells as per-device configuration words
        return [('raw', ' '.join(f'{w:#x}' for w in struct.unpack(f'<{len(b) // 4}I', b[:len(b) // 4 * 4])))]
    step = 4 * (ac + sc)
    out = []
    if step == 0 or len(b) % step:
        return [('raw', ' '.join(f'{w:#x}' for w in struct.unpack(f'<{len(b) // 4}I', b[:len(b) // 4 * 4])))]
    for i in range(0, len(b), step):
        w = struct.unpack_from(f'<{ac + sc}I', b, i)
        a = 0
        for x in reversed(w[:ac]):
            a = (a << 32) | x
        s = 0
        for x in reversed(w[ac:]):
            s = (s << 32) | x
        out.append((a, s))
    return out


def irqs(n):
    p = n['props'].get('interrupts')
    if not p or p['len'] % 4:
        return [], None
    par = n['props'].get('interrupt-parent', {}).get('u32')
    return list(struct.unpack(f'<{p["len"] // 4}I', raw(p))), ph.get(par)


def functions(n):
    out = []
    for k, p in n['props'].items():
        if not k.startswith('function-') or p['len'] < 8:
            continue
        b = raw(p)
        w = struct.unpack(f'<{len(b) // 4}I', b[:len(b) // 4 * 4])
        fc = fourcc(w[1])
        out.append((k[9:], ph.get(w[0]), w[0], fc[1] if fc else f'{w[1]:#x}', list(w[2:])))
    return out


def hexdump(b, limit=2048):
    L = []
    for i in range(0, min(len(b), limit), 16):
        c = b[i:i + 16]
        L.append(f'{i:06x}  {" ".join(f"{x:02x}" for x in c):<47}  {"".join(chr(x) if 32 <= x < 127 else "." for x in c)}')
    if len(b) > limit:
        L.append(f'… {len(b) - limit} more bytes')
    return L


PH_KEYS = re.compile(r'(parent|phandle|-ref$|^iommu|^dart|controller$|^gpio|^pmu$|^spmi)')


def describe(k, p):
    L = []
    b = raw(p)
    flag = ' *(placeholder, filled in by iBoot at boot)*' if p.get('placeholder') else ''
    if 'str' in p and not (p['len'] == 4 and isinstance(p['str'], str) and len(p['str']) < 3):
        s = p['str']
        L.append(f'- **`{k}`**: ' + (', '.join(f'`{x}`' for x in s) if isinstance(s, list) else f'`{s}`') + flag)
        return L
    if p['len'] == 0:
        L.append(f'- **`{k}`**: (present, empty){flag}')
        return L
    if 'u32' in p:
        v = p['u32']
        extra = ''
        if v in ph and (PH_KEYS.search(k) or k.endswith('-parent')):
            extra = f' → phandle of {link(ph[v])}'
        fc = fourcc(v)
        if fc and not extra and v > 0x20202020:
            extra = f' (four-char code `{fc[1]}`)'
        L.append(f'- **`{k}`**: `{v}` (`{v:#x}`){extra}{flag}')
        return L
    if 'u64' in p:
        L.append(f'- **`{k}`**: `{p["u64"]:#x}` (u64; as two u32: `{struct.unpack("<II", b)[0]:#x}`, `{struct.unpack("<II", b)[1]:#x}`){flag}')
        return L
    L.append(f'- **`{k}`**: {p["len"]} bytes{flag}')
    if 'u32s' in p and p['len'] <= 512:
        L.append(f'  - u32: `{" ".join(f"{x:#x}" for x in p["u32s"])}`')
    strs_in = [s.decode('latin-1') for s in re.findall(rb'[\x20-\x7e]{4,}', b)]
    if strs_in:
        L.append('  - text inside: ' + ', '.join(f'`{s}`' for s in strs_in[:30]))
    L.append('  ```')
    L += ['  ' + x for x in hexdump(b)]
    L.append('  ```')
    return L


def related_firmware(n):
    toks = {t for t in re.split(r'[^a-z0-9]+', n['name'].lower()) if len(t) >= 3}
    toks -= {'gpio', 'dart', 'proxy', 'exclave', 'mailbox', 'controller', 'ioreporting', 'sac', 'ced', 'ssw'}
    return [r for r in firmware if any(re.search(rf'(^|[/_.\-]){re.escape(t)}', r[1].lower()) for t in toks)][:20]


# referenced-by index
refby = {}
for n in nodes:
    for name, prov, _, code, _ in functions(n):
        if prov:
            refby.setdefault(prov, []).append((n['path'], f'function-{name} `{code}`'))
    ir, par = irqs(n)
    if par and ir:
        refby.setdefault(par, []).append((n['path'], f'interrupts {", ".join(map(str, ir[:6]))}'))
    for k, p in n['props'].items():
        if k.startswith('function-') or k in ('AAPL,phandle', 'interrupt-parent'):
            continue
        if p.get('u32') in ph and (PH_KEYS.search(k) or k.endswith('-parent')):
            refby.setdefault(ph[p['u32']], []).append((n['path'], f'`{k}`'))

# ----- per-node pages -----
for n in nodes:
    p = n['path']
    L = [f'# `{short(p)}`', '', f'- Name: `{n["name"]}`', f'- Parent: {link(n["parent"]) if n["parent"] else "none (root)"}']
    if n['phandle'] is not None:
        L.append(f'- phandle: `{n["phandle"]}`')
    if n['compatible']:
        L.append('- compatible: ' + ', '.join(f'`{c}`' for c in n['compatible']))
    if n['device_type']:
        L.append(f'- device_type: `{n["device_type"]}`')
    ch = kids.get(p, [])
    if ch:
        L.append(f'- Children ({len(ch)}): ' + ', '.join(link(c) for c in ch))
    L += ['', '## Kernel driver [KC]', '']
    if n['drivers']:
        L += ['| IOClass | Provider | kext | matched on |', '|---|---|---|---|']
        L += [f'| `{d["class"]}` | `{d["provider"]}` | [`{d["kext"]}`](../kexts/{d["kext"]}.md) | `{d["matched_on"]}` |' for d in n['drivers']]
    else:
        L.append('No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.')
    rg = regs(n)
    if rg:
        L += ['', '## Register windows [DT]', '', '| # | Bus address | Size | CPU physical |', '|---|---|---|---|']
        for i, r in enumerate(rg):
            if r[0] == 'raw':
                L.append(f'| {i} | raw `{r[1]}` | | |')
                continue
            a, s = r
            t = translate(p, a)
            L.append(f'| {i} | `{a:#x}` | `{s:#x}` ({s:,} B) | {f"`{t:#x}`–`{t + max(s, 1) - 1:#x}`" if t is not None else "not memory-mapped (bus address)"} |')
    ir, par = irqs(n)
    if ir:
        L += ['', '## Interrupts [DT]', '', f'Controller: {link(par) if par else "unresolved"}', '', '`' + ', '.join(str(x) for x in ir) + '`']
    fs = functions(n)
    if fs:
        L += ['', '## Functions it calls on other nodes [DT]', '', '| Function | Provider | Code | Arguments |', '|---|---|---|---|']
        L += [f'| `{a}` | {link(b) if b else f"phandle {c}"} | `{d}` | `{" ".join(f"{x:#x}" for x in e)}` |' for a, b, c, d, e in fs]
    rb = refby.get(p, [])
    if rb:
        L += ['', f'## Referenced by ({len(rb)}) [DT]', '']
        L += [f'- {link(a)}: {b}' for a, b in rb]
    fw = related_firmware(n)
    if fw:
        L += ['', '## Firmware with a matching name [FW]', '']
        L += [f'- [`{r[1]}`](../firmware/{r[1].replace("/", "__")}.md) ({int(r[0]):,} B) {r[2].strip() if len(r) > 2 else ""}' for r in fw]
    L += ['', f'## All properties ({len(n["props"])}) [DT]', '']
    for k in sorted(n['props']):
        L += describe(k, n['props'][k])
    open(os.path.join(DT, slug(p) + '.md'), 'w').write('\n'.join(L) + '\n')

idx = ['# Device tree', '', f'{len(nodes)} nodes of `DeviceTree.v68ap.im4p`, parsed byte-exact by `tools/adt.py`.', '']
for n in nodes:
    d = drivers(n)
    idx.append('  ' * n['path'].count('/') + f'- {link(n["path"])}' + (f' — {", ".join(n["compatible"][:2])}' if n['compatible'] else '') + (f' → **{d}**' if d else ''))
open(os.path.join(DT, 'README.md'), 'w').write('\n'.join(idx) + '\n')

# ----- maps -----
rows = []
for n in nodes:
    for i, r in enumerate(regs(n)):
        if r[0] == 'raw':
            continue
        t = translate(n['path'], r[0])
        if t is not None and not (t == 0 and r[1] == 0):
            rows.append((t, r[1], n, i))
rows.sort(key=lambda x: x[0])
L = ['# Physical address map', '', 'Every register window that translates to a CPU physical address through the `ranges` of each '
     'parent bus, sorted by address. This is the SoC\'s memory map as the kernel sees it. **[DT]**', '',
     f'{len(rows)} windows.', '', '| Start | End | Size | Node | # | Driver |', '|---|---|---|---|---|---|']
prev_end = None
for t, s, n, i in rows:
    overlap = ' ⚠ overlaps previous' if prev_end is not None and t <= prev_end else ''
    L.append(f'| `{t:#011x}` | `{t + max(s, 1) - 1:#011x}` | `{s:#x}` | {link(n["path"], True)}{overlap} | {i} | {drivers(n)} |')
    prev_end = max(prev_end or 0, t + max(s, 1) - 1)
open(os.path.join(MAPS, 'physical-address-map.md'), 'w').write('\n'.join(L) + '\n')

L = ['# Interrupt map', '', 'Every interrupt a node declares, grouped by its controller (`interrupt-parent`), sorted by number. **[DT]**']
allirq = []
for n in nodes:
    ir, par = irqs(n)
    allirq += [(par or '', x, n, j) for j, x in enumerate(ir)]
allirq.sort(key=lambda x: (x[0], x[1]))
cur = None
for par, x, n, j in allirq:
    if par != cur:
        cur = par
        L += ['', f'## {link(par, True) if par else "No controller"}', '', '| Line | Node | Index | Driver |', '|---|---|---|---|']
    L.append(f'| {x} (`{x:#x}`) | {link(n["path"], True)} | {j} | {drivers(n)} |')
open(os.path.join(MAPS, 'interrupt-map.md'), 'w').write('\n'.join(L) + '\n')

L = ['# Function references', '', 'Apple device trees wire one block to another with `function-<name>` properties: '
     '`<provider phandle> <four-char code> <args…>`. Codes are stored little-endian; the readable order is shown. '
     'This is the board\'s control wiring as software sees it: which PMU rail, GPIO, reset or power gate each device uses. **[DT]**', '',
     '| Consumer | Function | Provider | Code | Arguments |', '|---|---|---|---|---|']
cnt = 0
by_prov = {}
for n in nodes:
    for a, b, c, d, e in functions(n):
        cnt += 1
        by_prov.setdefault(b or f'phandle {c}', []).append((n['path'], a, d, e))
        L.append(f'| {link(n["path"], True)} | `{a}` | {link(b, True) if b else f"phandle {c}"} | `{d}` | `{" ".join(f"{x:#x}" for x in e)}` |')
L += ['', '## Grouped by provider', '']
for prov in sorted(by_prov):
    L += ['', f'### {link(prov, True) if prov in by_path else prov} ({len(by_prov[prov])} consumers)', '']
    L += [f'- {link(c, True)} `{a}` `{d}` {" ".join(f"{x:#x}" for x in e)}' for c, a, d, e in by_prov[prov]]
open(os.path.join(MAPS, 'function-references.md'), 'w').write('\n'.join(L) + '\n')

L = ['# phandle table', '', 'Every node handle and what refers to it. **[DT]**', '', '| phandle | Node | Referenced by |', '|---|---|---|']
for v in sorted(ph):
    r = refby.get(ph[v], [])
    L.append(f'| {v} | {link(ph[v], True)} | {len(r)} |')
open(os.path.join(MAPS, 'phandles.md'), 'w').write('\n'.join(L) + '\n')

BUSRE = re.compile(r'(i2c|spi|spmi|uart|dockchannel|serial)', re.I)
L = ['# Serial-bus device map', '', 'Every device that sits on an I2C, SPI, SPMI or UART controller, with its bus address, interrupt and driver. **[DT]**']
for n in nodes:
    if n['path'].count('/') != 2 or not BUSRE.search(n['name']):
        continue
    ch = [by_path[c] for c in kids.get(n['path'], [])]
    L += ['', f'## {link(n["path"], True)} — `{", ".join(n["compatible"])}` — {drivers(n) or "no direct driver"}', '']
    if not ch:
        L.append('No child devices.')
        continue
    L += ['| Device | compatible | Bus address | IRQ (controller) | Driver |', '|---|---|---|---|---|']
    for m in ch:
        rg = regs(m)
        ad = ', '.join(f'`{r[0]:#x}`' for r in rg if r[0] != 'raw') or '—'
        ir, par = irqs(m)
        L.append(f'| {link(m["path"], True)} | `{", ".join(m["compatible"])}` | {ad} | {", ".join(map(str, ir[:4]))} {f"({short(par)})" if par else ""} | {drivers(m)} |')
open(os.path.join(MAPS, 'bus-devices.md'), 'w').write('\n'.join(L) + '\n')

print(len(nodes), 'node pages;', len(rows), 'mapped windows;', len(allirq), 'irqs;', cnt, 'function refs')

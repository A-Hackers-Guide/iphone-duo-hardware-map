"""Write one Markdown page per device-tree node, with every property decoded.

usage: gen_nodes.py data/devicetree-nodes.json data/kexts.json data/firmware-inventory.tsv reference/devicetree
"""
import base64
import json
import os
import re
import struct
import sys

nodes_path, kexts_path, fw_path, out = sys.argv[1:5]
nodes = json.load(open(nodes_path))
kexts = json.load(open(kexts_path))
firmware = [l.split('\t') for l in open(fw_path).read().splitlines()]
os.makedirs(out, exist_ok=True)

by_path = {n['path']: n for n in nodes}
children = {}
for n in nodes:
    children.setdefault(n['parent'], []).append(n['path'])
kext_by_id = {k['id']: k for k in kexts}
phandles = {n['props'].get('AAPL,phandle'): n['path'] for n in nodes if isinstance(n['props'].get('AAPL,phandle'), int)}

B64 = re.compile(r'^[A-Za-z0-9+/]{4,}={0,2}$')


def slug(path):
    s = path.replace('device-tree', 'root').strip('/').replace('/', '__')
    return re.sub(r'[^A-Za-z0-9_.,-]', '_', s)


def link(path, frm_dir=True):
    return f'[`{short(path)}`]({slug(path)}.md)'


def short(path):
    return path.replace('device-tree', '') or '/'


def decode_blob(v):
    """Return (raw bytes or None) for a base64-looking string."""
    if not isinstance(v, str) or len(v) < 4 or len(v) % 4 or not B64.match(v):
        return None
    try:
        return base64.b64decode(v, validate=True)
    except Exception:
        return None


def hexdump(b, limit=4096):
    lines = []
    for i in range(0, min(len(b), limit), 16):
        chunk = b[i:i + 16]
        hx = ' '.join(f'{c:02x}' for c in chunk)
        asc = ''.join(chr(c) if 32 <= c < 127 else '.' for c in chunk)
        lines.append(f'{i:06x}  {hx:<47}  {asc}')
    if len(b) > limit:
        lines.append(f'… {len(b) - limit} more bytes')
    return lines


def describe(k, v):
    out = []
    b = decode_blob(v)
    if b is not None:
        out.append(f'- **`{k}`**: {len(b)} bytes')
        if len(b) % 4 == 0 and len(b) <= 4096:
            words = struct.unpack(f'<{len(b) // 4}I', b)
            out.append(f'  - as little-endian u32: `{" ".join(f"0x{w:x}" for w in words)}`')
            if k in ('interrupts',):
                out.append(f'  - interrupt numbers (decimal): `{", ".join(str(w) for w in words)}`')
            refs = [phandles[w] for w in words if w in phandles and k.endswith(('-parent', 'parent', 'phandle', 'parents')) ]
            if refs:
                out.append('  - phandle references: ' + ', '.join(link(r) for r in refs))
        if len(b) % 8 == 0 and len(b) <= 2048 and len(b) >= 8:
            q = struct.unpack(f'<{len(b) // 8}Q', b)
            out.append(f'  - as little-endian u64: `{" ".join(f"0x{w:x}" for w in q)}`')
        txt = b.split(b'\0')
        strs = [t.decode('latin-1') for t in txt if len(t) >= 3 and all(32 <= c < 127 for c in t)]
        if strs:
            out.append(f'  - embedded strings: {", ".join("`" + s + "`" for s in strs[:40])}')
        out.append('  ```')
        out += ['  ' + l for l in hexdump(b)]
        out.append('  ```')
        return out
    if isinstance(v, int):
        extra = ''
        if k in ('interrupt-parent', 'iommu-parent', 'clock-parent') or k.endswith('-parent'):
            if v in phandles:
                extra = f' → {link(phandles[v])}'
        out.append(f'- **`{k}`**: `{v}` (`0x{v:x}`){extra}')
        return out
    if isinstance(v, list) and v and isinstance(v[0], dict) and 'addr' in v[0]:
        out.append(f'- **`{k}`**: {len(v)} range(s)')
        for r in v:
            a, s = r.get('addr', 0), r.get('size', 0)
            out.append(f'  - `0x{a:x}`–`0x{a + s - 1:x}` ({s:#x} bytes, {s / 1024:.0f} KiB)')
        return out
    if v is None:
        out.append(f'- **`{k}`**: (empty / boolean present)')
        return out
    out.append(f'- **`{k}`**: `{str(v)[:400]}`')
    return out


def related_firmware(n):
    toks = {t for t in re.split(r'[^a-z0-9]+', n['name'].lower()) if len(t) >= 3}
    toks -= {'gpio', 'dart', 'proxy', 'exclave', 'mailbox', 'controller', 'ioreporting'}
    hits = []
    for row in firmware:
        p = row[1].lower()
        if any(re.search(rf'(^|[/_.\-]){re.escape(t)}', p) for t in toks):
            hits.append(row)
    return hits[:20]


count = 0
for n in nodes:
    p = n['path']
    L = [f'# `{short(p)}`', '']
    L.append(f'- Name: `{n["name"]}`')
    L.append(f'- Parent: {link(n["parent"]) if n["parent"] else "none (root)"}')
    if n['compatible']:
        L.append(f'- compatible: {", ".join("`" + c + "`" for c in n["compatible"])}')
    if n.get('device_type'):
        L.append(f'- device_type: `{n["device_type"]}`')
    kids = children.get(p, [])
    if kids:
        L.append(f'- Children ({len(kids)}): ' + ', '.join(link(c) for c in kids))
    L += ['', '## Kernel driver binding [KC]', '']
    if n['drivers']:
        L += ['| IOClass | Provider class | kext | matched on |', '|---|---|---|---|']
        for d in n['drivers']:
            L.append(f'| `{d["class"]}` | `{d["provider"]}` | [`{d["kext"]}`](../kexts/{d["kext"]}.md) | `{d["matched_on"]}` |')
    else:
        L.append('No kext personality names this node directly. It is either bound by a parent driver, by property matching, by DriverKit or an exclave, or it is a structural node.')
    fw = related_firmware(n)
    if fw:
        L += ['', '## Firmware images with a matching name [FW]', '', '| Size | File | IM4P |', '|---|---|---|']
        for r in fw:
            L.append(f'| {int(r[0]):,} | [`{r[1]}`](../firmware/{r[1].replace("/", "__")}.md) | {r[2].strip() if len(r) > 2 else ""} |')
    L += ['', f'## Properties ({len(n["props"])}) [DT]', '']
    for k in sorted(n['props']):
        L += describe(k, n['props'][k])
    open(os.path.join(out, slug(p) + '.md'), 'w').write('\n'.join(L) + '\n')
    count += 1

idx = ['# Device tree node pages', '', f'{count} pages, one per node of `DeviceTree.v68ap.im4p`.', '']
for n in nodes:
    depth = n['path'].count('/')
    drv = ', '.join(sorted({d['class'] for d in n['drivers']}))
    idx.append('  ' * depth + f'- {link(n["path"])}' + (f' — {drv}' if drv else ''))
open(os.path.join(out, 'README.md'), 'w').write('\n'.join(idx) + '\n')
print(count, 'node pages')

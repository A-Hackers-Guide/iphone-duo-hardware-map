"""Exact parser for Apple's flattened device tree (the IM4P 'dtre' payload).

Format: node = u32 property count, u32 child count, properties, children.
property = name (32 bytes, NUL padded), u32 length (bit 31 = placeholder flag), value padded to 4 bytes.

Writes JSON with every property's exact bytes (hex), plus decoded forms where they are unambiguous.

usage: adt.py <raw devicetree payload> out.json
"""
import json
import struct
import sys


def decode(name, b):
    d = {'len': len(b), 'hex': b.hex()}
    if b and b[-1] == 0 and all(32 <= c < 127 or c == 0 for c in b) and any(c for c in b):
        parts = [p.decode() for p in b.split(b'\0') if p]
        d['str'] = parts if len(parts) > 1 else parts[0]
    if len(b) == 4:
        d['u32'] = struct.unpack('<I', b)[0]
    elif len(b) == 8:
        d['u64'] = struct.unpack('<Q', b)[0]
    if len(b) % 4 == 0 and 4 < len(b) <= 8192:
        d['u32s'] = list(struct.unpack(f'<{len(b) // 4}I', b))
    return d


def parse(buf, off=0):
    nprops, nkids = struct.unpack_from('<II', buf, off)
    off += 8
    props = {}
    for _ in range(nprops):
        name = buf[off:off + 32].split(b'\0')[0].decode('latin-1')
        ln, = struct.unpack_from('<I', buf, off + 32)
        placeholder = bool(ln & 0x80000000)
        ln &= 0x7fffffff
        val = buf[off + 36:off + 36 + ln]
        off += 36 + ((ln + 3) & ~3)
        d = decode(name, val)
        if placeholder:
            d['placeholder'] = True
        props[name] = d
    kids = []
    for _ in range(nkids):
        k, off = parse(buf, off)
        kids.append(k)
    return {'props': props, 'children': kids}, off


if __name__ == '__main__':
    raw = open(sys.argv[1], 'rb').read()
    tree, end = parse(raw)
    json.dump(tree, open(sys.argv[2], 'w'))
    print(f'parsed {end} of {len(raw)} bytes')

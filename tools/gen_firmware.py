"""Write one Markdown page per firmware image: IM4P metadata, payload format, ftab sections,
RTKit/Mach-O identity, and its readable strings.

Payloads are extracted one at a time into a temp dir and deleted right after, to keep disk use low.

usage: gen_firmware.py <ipsw extract dir> data/firmware-inventory.tsv data/buildmanifest-components.json reference/firmware
"""
import json
import os
import re
import shutil
import struct
import subprocess
import sys
import tempfile

root, inv_path, bm_path, out = sys.argv[1:5]
os.makedirs(out, exist_ok=True)
rows = [l.split('\t') for l in open(inv_path).read().splitlines()]
bm = json.load(open(bm_path))
by_file = {}
for comp, v in bm.items():
    if v.get('path'):
        by_file.setdefault(v['path'], []).append(comp)
MAX_STRINGS = 4000
MIN_LEN = 6


def run(*a, timeout=300):
    try:
        return subprocess.run(a, capture_output=True, timeout=timeout).stdout.decode('utf-8', 'replace')
    except subprocess.TimeoutExpired:
        return ''


def strings(data):
    for m in re.finditer(rb'[\x20-\x7e]{%d,}' % MIN_LEN, data):
        yield m.start(), m.group().decode('ascii')


def ftab(data):
    """Apple 'ftab' container: header then (tag, offset, size) entries."""
    if data[32:36] != b'ftab':
        return None
    n = struct.unpack_from('<I', data, 40)[0]
    ents = []
    for i in range(n):
        tag, off, size, _ = struct.unpack_from('<4sIII', data, 48 + 16 * i)
        ents.append((tag.decode('latin-1'), off, size))
    return ents


def ident(data):
    if data[:4] in (b'\xcf\xfa\xed\xfe',):
        return 'Mach-O 64-bit'
    if data[:4] == b'\xca\xfe\xba\xbe':
        return 'Mach-O universal'
    if data[32:36] == b'ftab':
        return 'ftab container'
    if data[:4] == b'bvx2' or data[:4] == b'bvx-':
        return 'LZFSE (not decompressed)'
    if data[:2] == b'0\x82' or data[:2] == b'0\x83':
        return 'DER / ASN.1'
    if data[:5] == b'<?xml' or data[:6] == b'bplist':
        return 'property list'
    return 'raw binary'


def interesting(s):
    return bool(re.search(r'[a-z]{3}', s, re.I)) and not re.fullmatch(r'[A-Za-z0-9+/=]{20,}', s)


pages = []
tmp = tempfile.mkdtemp(prefix='fwx-')
for row in rows:
    size, rel = int(row[0]), row[1]
    meta = row[2].strip() if len(row) > 2 else ''
    src = os.path.join(root, rel)
    L = [f'# `{rel}`', '', f'- File size: {size:,} bytes']
    if meta:
        L.append(f'- IM4P: {meta}')
    comps = by_file.get(rel, [])
    if comps:
        L.append('- BuildManifest components that use it: ' + ', '.join(f'`{c}`' for c in comps))
    payload = None
    if rel.endswith('.im4p'):
        info = run('ipsw', 'img4', 'im4p', 'info', src)
        L += ['', '## IM4P header [FW]', '', '```'] + [l for l in info.splitlines() if l.strip()][:40] + ['```']
        outp = os.path.join(tmp, 'payload')
        run('ipsw', 'img4', 'im4p', 'extract', src, '-o', outp)
        if os.path.exists(outp):
            payload = open(outp, 'rb').read()
            os.remove(outp)
    else:
        payload = open(src, 'rb').read()
    if payload is not None:
        kind = ident(payload)
        L += ['', '## Payload [FW]', '', f'- Size after IM4P unwrap / decompression: {len(payload):,} bytes', f'- Format: {kind}']
        ents = ftab(payload)
        if ents:
            L += ['', '### ftab sections', '', '| Tag | Offset | Size | First strings |', '|---|---|---|---|']
            for tag, off, sz in ents:
                sub = payload[off:off + sz]
                first = [s for _, s in strings(sub[:65536]) if interesting(s)][:3]
                L.append(f'| `{tag}` | {off:#x} | {sz:,} | {"; ".join("`" + f.replace("|", "/")[:80] + "`" for f in first)} |')
        # identity strings: RTKit versions, build tags, project names
        ids = sorted({s for _, s in strings(payload) if re.search(r'(RTKit|RTBuddy|@\(#\)|PROGRAM:|PROJECT:|Apple Inc|iBoot-|BuildVersion|_RELEASE|-[0-9]+\.[0-9]+(\.[0-9]+)*~)', s)})
        if ids:
            L += ['', '## Identity strings (versions, build tags) [FW]', ''] + [f'- `{s[:300]}`' for s in ids[:200]]
        allstr = [(o, s) for o, s in strings(payload) if interesting(s)]
        L += ['', f'## Strings ({len(allstr):,}) [FW]', '',
              f'Printable runs of {MIN_LEN}+ characters with at least three letters, in file order, with payload offset. '
              'For RTKit co-processor firmware these are the log formats, task names, endpoint names and assertions that '
              'describe what the processor does.']
        if len(allstr) > MAX_STRINGS:
            L.append(f'First {MAX_STRINGS:,} of {len(allstr):,}.')
        L.append('')
        L.append('```')
        for o, s in allstr[:MAX_STRINGS]:
            L.append(f'{o:08x}  {s[:240]}')
        L.append('```')
        nstr = len(allstr)
    else:
        nstr = 0
        L += ['', 'Payload could not be extracted (encrypted or unsupported).']
    name = rel.replace('/', '__')
    open(os.path.join(out, name + '.md'), 'w').write('\n'.join(L) + '\n')
    pages.append((rel, size, meta, len(payload) if payload is not None else 0, nstr))
    payload = None
shutil.rmtree(tmp, ignore_errors=True)

I = ['# Firmware pages', '', f'{len(pages)} firmware images from the iPhone19,4 iOS 27.2 restore image.', '',
     '| Firmware | File size | IM4P | Payload size | Strings |', '|---|---|---|---|---|']
for rel, size, meta, psz, ns in pages:
    I.append(f'| [`{rel}`]({rel.replace("/", "__")}.md) | {size:,} | {meta} | {psz:,} | {ns:,} |')
open(os.path.join(out, 'README.md'), 'w').write('\n'.join(I) + '\n')
print(len(pages), 'firmware pages')

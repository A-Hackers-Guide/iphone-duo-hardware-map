"""Co-processor matrix: every ASC-wrapped processor in the SoC with its role, firmware image, the OS/version
strings found in that firmware, its BuildManifest component, and the kernel drivers on it and its nub.

usage: gen_coproc.py data/adt-nodes.json data/buildmanifest-components.json reference/firmware reference/maps/coprocessors.md
"""
import json
import os
import re
import sys

nodes_path, bm_path, fwdir, out = sys.argv[1:5]
nodes = json.load(open(nodes_path))
bm = json.load(open(bm_path))
by_file = {}
for comp, v in bm.items():
    if v.get('path'):
        by_file.setdefault(v['path'], []).append(comp)

# role → firmware file, from the IPSW layout (documented in the chapters)
FW = {
    'AOP': 'Firmware/AOP/aopfw-v68aop.RELEASE.im4p', 'AOP2': 'Firmware/AOP2/aop2fw-v68aop2.RELEASE.im4p',
    'PMP': 'Firmware/pmp/t8160pmp.im4p', 'SEP': 'Firmware/all_flash/sep-firmware.v68.RELEASE.im4p',
    'SIO': 'Firmware/SmartIOFirmware_ASCv8.im4p', 'ANS2': 'Firmware/ansf.t8160.release.im4p',
    'MTP': 'Firmware/V68_MtpFirmware.im4p', 'DCP': 'Firmware/dcp/t8160dcp.im4p', 'DCPSEC': 'Firmware/dcp/t8160dcp.im4p',
    'DCPEXT': 'Firmware/dcp/t8160dcp.im4p', 'ISP': 'Firmware/isp_bni/adc-boreas-v68.im4p',
    'ANE': 'Firmware/ane/h19_ane0_fw_perses_v6x.im4p', 'ANE1': 'Firmware/ane/h19_ane1_fw_perses_v6x.im4p',
    'GFX': 'Firmware/agx/armfw_g19p.im4p', 'GFX1': 'Firmware/agx/armfw1_g19p.im4p',
}
VER = re.compile(r'(RTKit[_-]?[\w.\-~]*\d|pitayaOS[\w.\-]*|AppleStorageFirmware-[\w.~\-]+|PROJECT:[\w.\-]+|@\(#\)[^`]*|'
                 r'SEPOS[\w.\-]*|BUILD_TAG[^`]*|iBoot-\d[\w.]*|[A-Za-z]+-\d+\.\d+(?:\.\d+)*(?:~\d+)?)')


def slug(p):
    s = p.replace('device-tree', 'root').strip('/').replace('/', '__')
    return re.sub(r'[^A-Za-z0-9_.,-]', '_', s)


def versions(rel):
    page = os.path.join(fwdir, rel.replace('/', '__') + '.md')
    if not os.path.exists(page):
        return []
    txt = open(page).read()
    sec = txt.split('## Identity strings', 1)
    body = sec[1].split('\n## ', 1)[0] if len(sec) > 1 else ''
    found = []
    for m in VER.finditer(body):
        v = m.group(1).strip()
        if v not in found:
            found.append(v)
    return found[:4]


kids = {}
for n in nodes:
    kids.setdefault(n['parent'], []).append(n)


def drivers_under(n, depth=2):
    out, stack = set(), [(n, 0)]
    while stack:
        x, d = stack.pop()
        out |= {f'`{dr["class"]}`' for dr in x['drivers']}
        if d < depth:
            stack += [(c, d + 1) for c in kids.get(x['path'], [])]
    return sorted(out)


L = ['# Co-processor matrix', '',
     'Every firmware-running processor wrapped by Apple\'s ASC block in the t8160 SoC: what role the device tree gives it, '
     'which firmware image it runs, the OS and version strings inside that image, which signed BuildManifest component '
     'carries it, and the kernel drivers that bind to it and its nub. **[DT][FW][KC]** '
     'SMC has no firmware image in the IPSW (see [chapter 06](../../docs/06-power-battery-thermal.md)).', '',
     '| Node | Role | Firmware | Version strings | Manifest component | Kernel drivers (node, nub and nub children) |', '|---|---|---|---|---|---|']
for n in nodes:
    if n['path'].count('/') != 2 or not any('ascwrap' in c for c in n['compatible']):
        continue
    role = n['props'].get('role', {}).get('str', '?')
    fw = FW.get(role)
    fwcell = f'[`{os.path.basename(fw)}`](../firmware/{fw.replace("/", "__")}.md)' if fw else '—'
    ver = ', '.join(f'`{v[:60]}`' for v in versions(fw)) if fw else ''
    comps = ', '.join(f'`{c}`' for c in by_file.get(fw, [])) if fw else ''
    L.append(f'| [`{n["path"].replace("device-tree", "")}`](../devicetree/{slug(n["path"])}.md) | {role} | {fwcell} | {ver} | {comps} | {", ".join(drivers_under(n))} |')
L += ['', 'Firmware for role names is matched by the IPSW\'s file layout, which every chapter uses; DCP, DCPSEC and DCPEXT share one image.']
open(out, 'w').write('\n'.join(L) + '\n')
print(len(L) - 8, 'rows')

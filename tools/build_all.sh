#!/usr/bin/env bash
# Rebuild every generated part of this repository from an iPhone restore image.
#
#   tools/build_all.sh <path/to/iPhone19,4_..._Restore.ipsw> <scratch dir>
#
# Needs: ipsw (github.com/blacktop/ipsw), python3, hdiutil, otool; ~25 GB free in <scratch dir>.
# The chapters in docs/ are hand-written and are not regenerated.
set -euo pipefail

IPSW=${1:?usage: build_all.sh <ipsw> <scratch dir>}
WORK=${2:?usage: build_all.sh <ipsw> <scratch dir>}
ROOT=$(cd "$(dirname "$0")/.." && pwd)
FW="$WORK/fw"
mkdir -p "$FW"
cd "$ROOT"

echo "== 1. firmware, kernelcache, manifest"
unzip -oq "$IPSW" 'Firmware/*' 'kernelcache.*' BuildManifest.plist -d "$FW" -x 'Firmware/*.mtree' 'Firmware/*.integrity_catalog'
KC_IN=$(ls "$FW"/kernelcache.release.* | head -1)
ipsw kernel dec "$KC_IN" -o "$FW/kc" >/dev/null
KC=$(find "$FW/kc" -type f | head -1)

echo "== 2. kexts"
python3 - "$KC" "$FW/prelink.xml" <<'EOF'
import sys
data = open(sys.argv[1], 'rb').read()
i = data.find(b'<key>_PrelinkInfoDictionary</key>')
s, e = data.rfind(b'<dict', 0, i), data.find(b'</plist>', i)
open(sys.argv[2], 'wb').write(b'<?xml version="1.0"?><plist version="1.0">' + data[s:e] + b'</plist>')
EOF
python3 tools/prelink.py "$FW/prelink.xml" data/kexts.json
python3 tools/prelink_full.py "$FW/prelink.xml" data/kexts-full.json
ipsw kernel cpp "$KC" > data/kernel-cpp-classes.txt
ipsw kernel mig "$KC" > data/kernel-mig.txt
ipsw kernel syscall "$KC" > data/kernel-syscalls.txt
ipsw kernel mach "$KC" > data/kernel-mach-traps.txt

echo "== 3. device tree (byte-exact)"
DT=$(ls "$FW"/Firmware/all_flash/DeviceTree.*.im4p | head -1)
ipsw img4 im4p extract "$DT" -o "$FW/dt.raw" >/dev/null
python3 tools/adt.py "$FW/dt.raw" "$FW/adt.json"
python3 tools/adt_nodes.py "$FW/adt.json" data/kexts.json data/adt-nodes.json
python3 tools/adt_dump.py data/adt-nodes.json > data/devicetree-exact.txt

echo "== 4. firmware inventory and manifest"
( cd "$FW" && for f in $(find Firmware -name '*.im4p' -o -name '*.bin' -o -name '*.sefw' -o -name '*.vnlfw' | sort); do
    t=$(ipsw img4 im4p info "$f" 2>/dev/null | grep -iE '^\s*(Tag|Type|Version)' | tr -s ' ' | tr '\n' ' ' || true)
    printf '%s\t%s\t%s\n' "$(stat -f%z "$f")" "$f" "$t"; done ) > data/firmware-inventory.tsv
python3 - "$FW/BuildManifest.plist" data/buildmanifest-components.json <<'EOF'
import json, plistlib, sys
m = plistlib.load(open(sys.argv[1], 'rb'))['BuildIdentities'][0]['Manifest']
json.dump({k: {'path': v.get('Info', {}).get('Path')} for k, v in m.items()}, open(sys.argv[2], 'w'), indent=1)
EOF
python3 tools/gen_manifest.py "$FW/BuildManifest.plist" reference/manifest.md

echo "== 5. reference pages"
python3 tools/gen_dt.py data/adt-nodes.json data/firmware-inventory.tsv reference
python3 tools/gen_maps.py data/devicetree-nodes.json data/kernel-cpp-classes.txt reference/maps 2>/dev/null || true
python3 tools/gen_kexts.py "$KC" data/kexts-full.json data/kernel-cpp-classes.txt data/adt-nodes.json reference/kexts
python3 tools/gen_kclasses.py data/kernel-cpp-classes.txt data/kexts-full.json data/adt-nodes.json reference/kexts reference/kclasses
python3 tools/gen_firmware.py "$FW" data/firmware-inventory.tsv data/buildmanifest-components.json reference/firmware
python3 tools/gen_coproc.py data/adt-nodes.json data/buildmanifest-components.json reference/firmware reference/maps/coprocessors.md
python3 tools/gen_explorer.py data/adt-nodes.json explorer/index.html

echo "== 6. restore ramdisks"
for id in $(python3 - "$FW/BuildManifest.plist" <<'EOF'
import plistlib, sys
m = plistlib.load(open(sys.argv[1], 'rb'))
print(' '.join(sorted({b['Manifest']['RestoreRamDisk']['Info']['Path'] for b in m['BuildIdentities']})))
EOF
); do
  name=$(basename "$id" .dmg); mkdir -p "$WORK/rd/$name/mnt"
  unzip -oqj "$IPSW" "$id" -d "$WORK/rd/$name"
  ipsw img4 im4p extract "$WORK/rd/$name/$(basename "$id")" -o "$WORK/rd/$name/rd.dmg" >/dev/null
  hdiutil attach -readonly -nobrowse -noautoopen -mountpoint "$WORK/rd/$name/mnt" "$WORK/rd/$name/rd.dmg" >/dev/null
  python3 tools/gen_ramdisk.py "$WORK/rd/$name/mnt" "restore ramdisk $name" "reference/ramdisk-$name"
  hdiutil detach "$WORK/rd/$name/mnt" -quiet
done

echo "== 7. userland (dyld shared cache)"
ipsw extract --dyld -o "$WORK/dsc" "$IPSW" >/dev/null
DSCDIR=$(dirname "$(find "$WORK/dsc" -name 'dyld_shared_cache_arm64e*' -not -name '*.[0-9]*' | head -1)")
# this ipsw build rejects the arm64e.x1 magic; relabel the local copy so it parses
python3 - "$DSCDIR" <<'EOF'
import os, sys
for f in os.listdir(sys.argv[1]):
    with open(os.path.join(sys.argv[1], f), 'r+b') as fh:
        if fh.read(16).startswith(b'dyld_v1') and True:
            fh.seek(0); m = fh.read(16)
            if b'x1' in m:
                fh.seek(0); fh.write(b'dyld_v1  arm64e\0')
EOF
DSC=$(find "$DSCDIR" -name 'dyld_shared_cache_arm64e*' -not -name '*.*' | head -1)
python3 tools/gen_dsc.py "$DSC" reference/userland
python3 tools/gen_objc.py "$DSC" reference/userland reference/objc 3
python3 tools/gen_dsc_all.py "$DSC" reference/userland 3
python3 tools/gen_dsc_syms.py "$DSC" reference/userland-symbols 3

echo "== 8. checks"
python3 tools/check_links.py . || true
python3 tools/stats.py . >/dev/null
echo done

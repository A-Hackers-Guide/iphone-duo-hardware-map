# 00: Method and evidence

## The sources

| Source | What it is | What it tells us |
|---|---|---|
| `iPhone19,4_27.2_24B91020_Restore.ipsw` | Apple's restore image for the Duo, 13.4 GB | Everything below |
| `Firmware/all_flash/DeviceTree.v68ap.im4p` | The device tree iBoot hands to the kernel | Every hardware block Apple describes: name, `compatible`, register ranges, interrupts, IOMMU, power domain, bus parent, and board-specific properties |
| `kernelcache.release.v6x-pandia` | XNU plus 322 prelinked kexts | Which driver class binds to which node, using `IONameMatch` against `compatible` |
| `Firmware/**/*.im4p`, `ftab.bin` | Co-processor firmware: AOP, AOP2, DCP, GPU, ANE, ISP, ANS, SEP, PMP, PMC, multitouch, haptics, wireless, baseband | What each co-processor runs; RTKit images carry readable strings |
| `BuildManifest.plist` | Every component that gets personalized and signed per device | Which processor consumes which signed blob |
| `dyld_shared_cache_arm64e_x1` | iOS 27.2 userland, 4,776 images | Daemons, frameworks and the classes or symbols that own each subsystem |
| [vphone-duo](https://github.com/A-Hackers-Guide/vphone-duo) research | Runtime findings from running Duo userland in a VM | How the hinge HID service, pose and display arbitration behave at runtime |
| Apple spec page, newsroom, iFixit teardown | Public | Physical specs and mechanics, cited by URL |

## How the device tree became the driver map

`tools/dtmap.py` walks the device tree. For every node, it lists each kext personality whose `IONameMatch` equals one of the node's `compatible` strings or its name.

`tools/prelink.py` reads the kernelcache's `__PRELINK_INFO` XML. The script resolves the `ID`/`IDREF` back-references XNU uses, then emits every personality's `IOClass`, `IOProviderClass` and match keys.

Of 552 nodes:
- **318 have a direct kernel driver** (byte-exact parse; the lossy `ipsw dtree` data gave 317).
- **37 have a `compatible` string with no direct match** (`tools/duomap.py unbound`). These are usually bound by property match, by a parent driver, by DriverKit, by an exclave, or not in the kernel at all. Each chapter accounts for the ones in its scope.
- **The rest are structural**, such as `/chosen`, `/memory`, and per-port children.

## Reproduce it

```bash
ipsw dtree Firmware/all_flash/DeviceTree.v68ap.im4p --json > dt.json
```

```bash
ipsw kernel dec kernelcache.release.v6x-pandia -o kc
```

The prelink XML is the `<dict>` that contains `_PrelinkInfoDictionary` in the decompressed kernelcache. Save it as `prelink.xml`, then:

```bash
python3 tools/prelink.py prelink.xml data/kexts.json
```

```bash
python3 tools/dtmap.py dt.json data/kexts.json data/devicetree-nodes.json
```

## Data files

- `data/adt-nodes.json` and `data/devicetree-exact.txt` are the byte-exact parse (`tools/adt.py`, `adt_nodes.py`, `adt_dump.py`). Use these.
- `data/devicetree.txt` and `data/devicetree-nodes.json` are `ipsw dtree` output. They render some binary properties (phandles, interrupts, function references) as text and are kept only because early chapters cite them.

## Limits

- **No silicon-level data.** Transistor counts, gate layouts, cell libraries and netlists are not in any of these sources. Neither are board schematics or the register-level programming model of Apple's blocks. The deepest this map goes is the boundary Apple itself draws in the device tree: a block, its MMIO window, its interrupt lines, and the driver that owns it.
- **Encrypted firmware.** SEP is encrypted, and so are parts of the cellular and other firmware. Chapters say when a payload could not be read.
- **One build, one variant.** Everything is observed for iOS 27.2 24B91020 on V68AP. Addresses and offsets are observations of this build, not constants.
- **No device on the bench.** Nothing here comes from probing real hardware. The only runtime evidence is from the vphone-duo VM, which differs from a real Duo, most notably by having one display instead of two.

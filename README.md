# iPhone Duo: hardware ↔ software map

A map of how every part of Apple's iPhone Duo (`iPhone19,4`, board `V68AP`, SoC `t8160` / A20 Pro) is wired to, and driven by, software in iOS 27.2 (build `24B91020`). It runs from silicon block, bus, interrupt and IOMMU, through co-processor firmware, kernel driver, exclave and daemon, to the API an app calls.

The map is built from primary evidence: the device's own restore image, read with [`ipsw`](https://github.com/blacktop/ipsw). Public sources fill in the rest, and every claim is labelled with where it came from.

**At a glance:** 43,258 Markdown pages, 3,518,632 lines. Tooling: 2,806 lines of Python in `tools/`. Every claim is labelled with its evidence; four fact-check passes re-checked 150 claims and corrected 35. Full breakdown: [STATS](STATS.md).

## Chapters

| # | Chapter | Covers |
|---|---|---|
| 00 | [Method and evidence](docs/00-method-and-evidence.md) | Where every fact comes from, how to reproduce it, and what cannot be known |
| 01 | [SoC, CPU, memory, storage](docs/01-soc-cpu-memory-storage.md) | CPU clusters, AIC, PMGR/DVFS, MCC/DRAM, DARTs, NVMe/APFS, buses |
| 02 | [Boot and security](docs/02-boot-and-security.md) | SecureROM to kernel, Image4, SEP, SPTM/TXM, exclaves, Secure Element, Touch ID |
| 03 | [GPU and displays](docs/03-gpu-and-displays.md) | AGX G19P GPU, DCP, both OLED panels, ProMotion, DisplayPort |
| 04 | [Camera, media, Neural Engine](docs/04-camera-media-neural-engine.md) | ISP, sensors, AVE/AVD codecs, JPEG, dual ANE |
| 05 | [Sensors, touch, audio, haptics](docs/05-sensors-touch-audio-haptics.md) | AOP/AOP2, motion and hinge sensors, multitouch on two panels, audio, Taptic |
| 06 | [Power, battery, thermal](docs/06-power-battery-thermal.md) | PMUs on SPMI, two batteries, charging, MagSafe/Qi2, thermals |
| 07 | [Networking and connectivity](docs/07-networking-and-connectivity.md) | C2 modem, N1 Wi-Fi 7 / BT 6 / Thread, UWB, NFC, GNSS, USB-C, the network stack |
| 08 | [The foldable system and chassis](docs/08-foldable-system-and-chassis.md) | Hinge, what crosses it, fold handling at every layer, emulation findings |
| 09 | [What makes it a Duo](docs/09-what-makes-it-a-duo.md) | Device-tree diff against an iPhone 18 Pro and the virtual iPhone: the 51 Duo-only nodes |
| 10 | [Userland: display, fold, touch](docs/10-userland-display-fold-touch.md) | Daemons and frameworks from IOMFB/HID up to UIKit for both panels and the hinge |
| 11 | [Userland: radios, power, sensors](docs/11-userland-radios-power-sensors.md) | CommCenter, Wi-Fi/BT/Thread/UWB/NFC daemons, power and battery UI, CoreMotion, MobileGestalt |
| 12 | [Userland: camera, ANE, audio, security](docs/12-userland-camera-ane-audio-security.md) | Capture stack, Neural Engine clients, audio/haptics, Touch ID, keybags, Secure Element |
| 13 | [Lifecycle](docs/13-lifecycle.md) | Factory, first restore and per-chip updaters, activation, OTA, repair, recovery, erase |
| 14 | [Power button to home screen](docs/14-power-button-to-home-screen.md) | A time-ordered cold boot across every processor, to the first frame on whichever panel is live and the first tap |

**[Architecture](docs/ARCHITECTURE.md)**: one diagram of every processor, bus and major chip. **[Tour](docs/TOUR.md)**: start here; worked examples of answering questions with the repo. **[MAP](docs/MAP.md)**: the master table, 148 components from silicon block to public API, one row each. **[Findings](docs/FINDINGS.md)**: the surprises and contradictions with the public specs, in one table. **[Fact-check](docs/FACTCHECK.md)** and **[second](docs/FACTCHECK-2.md)** and **[third](docs/FACTCHECK-3.md)** and **[fourth](docs/FACTCHECK-4.md)** passes: 150 claims re-derived from the raw evidence, with corrections. **[Open questions](docs/OPEN-QUESTIONS.md)**: the 200+ things the evidence could not settle, as one research agenda. **[Glossary](docs/GLOSSARY.md)**: every codename (Mesa, Crane, Becketts, Centauri, Stockholm…) and what it is.

## Reference (generated, one page per item)

| Section | What | Generator |
|---|---|---|
| [Device tree](reference/devicetree/README.md) | All 552 nodes, parsed byte-exact: every property decoded, register windows translated to physical addresses, interrupts, function wiring, who references each node, matching driver and firmware | `tools/adt.py`, `adt_nodes.py`, `gen_dt.py` |
| [Maps](reference/maps/) | [Co-processor matrix](reference/maps/coprocessors.md), [unbound nodes](reference/maps/unbound-nodes.md), [function codes](reference/maps/function-codes.md), [GPIO pins](reference/maps/gpio-pins.md), [property dictionary](reference/maps/property-index.md), [driver match table](reference/maps/driver-matches.md), [kext dependencies](reference/maps/kext-dependencies.md), [syscfg keys](reference/maps/syscfg-keys.md), [firmware SBOM](reference/maps/firmware-sbom.md), [physical address map](reference/maps/physical-address-map.md), [interrupt map](reference/maps/interrupt-map.md), [function wiring](reference/maps/function-references.md), [serial-bus devices](reference/maps/bus-devices.md), [phandles](reference/maps/phandles.md), [kernel C++ class tree](reference/maps/kernel-class-tree.md) | `gen_dt.py`, `gen_maps.py` |
| [Kernel extensions](reference/kexts/README.md) | All 322 kexts: full personalities, C++ classes with superclass chains, Mach-O layout, Info.plist, strings | `prelink_full.py`, `gen_kexts.py` |
| [Kernel entry points](reference/kernel/) | [BSD syscalls](reference/kernel/syscalls.md), [Mach traps](reference/kernel/mach-traps.md), [MIG routines](reference/kernel/mig.md) | `ipsw kernel` |
| [BuildManifest](reference/manifest.md) | Every signed component per build identity: path, digest, trust flags, info keys | `gen_manifest.py` |
| [Kernel C++ classes](reference/kclasses/README.md) | All 3,388 classes, one page each: size, superclass chain, subclasses, vtables, owning kext, personalities, bound device-tree nodes, strings naming it | `gen_kclasses.py` |
| [Firmware](reference/firmware/README.md) | All 56 firmware images: IM4P header, payload format, ftab sections, version strings, all strings with offsets | `gen_firmware.py` |
| [Ramdisk firmware](reference/ramdisk-firmware/README.md) | All 277 standalone firmware files in the restore ramdisk (USB-C/DisplayPort controllers, NFC controller RF/firmware, storage tunables and more): format, version strings, all strings | `gen_firmware.py` |
| [Upgrade ramdisk](reference/ramdisk/README.md) | The upgrade-install restore ramdisk (141-29011-104, `restored_update`), all 1,517 files: DriverKit drivers, hardware updaters, standalone firmware, libraries (linked libs, entitlements, ObjC, strings) | `gen_ramdisk.py` |
| [Erase/recovery ramdisk](reference/ramdisk-erase/README.md) | The erase-install and recovery restore ramdisk (141-28940-105, `restored_external`), every file | `gen_ramdisk.py` |
| [Small APFS image 141-28395](reference/image-141-28395/README.md) | The Safari/web cryptex image | `gen_ramdisk.py` |
| [Userland](reference/userland/README.md) | All 4,776 dyld-cache images, with full pages for the hardware-facing ones | `gen_dsc.py` |
| [Comparisons](reference/compare/) | [Duo vs iPhone19,2 (18 Pro)](reference/compare/duo-vs-iphone19-2.md), [Duo vs vphone600 VM](reference/compare/duo-vs-vphone600.md) | `dt_diff.py` |
| [Objective-C classes](reference/objc/README.md) | 33,249 classes and protocols from the hardware-facing frameworks, one page each: superclass, protocols, ivars, properties, every class and instance method | `gen_objc.py` |
| [`data/`](data/) | Raw and structured inputs: device tree, kext plists, kernel MIG/syscall/trap tables, firmware inventory, BuildManifest, per-chapter evidence | |

## What "every one and zero" can and cannot mean

The map goes as deep as the evidence goes. Below that point, it says it stops rather than guessing.

- **Covered:** every hardware node Apple describes to the kernel, every driver that binds to it, every firmware image and which processor runs it, and the userland frameworks and daemons that own each subsystem.
- **Not covered:**
  - **Transistor-level and gate-level layouts, schematics and board netlists.** These are not public. The A20 Pro has tens of billions of transistors, and only die-shot analysis by a lab could say anything about their arrangement.
  - **Apple's internal register specifications.**
  - **The contents of encrypted firmware.** This includes most of SEP and parts of the baseband.

  Where a chapter reasons beyond its evidence, it says so with **[INF]**.

## Tools

- **[`explorer/index.html`](explorer/index.html)**: a single-file browser for the device tree. Download it and open it; it searches all 552 nodes and shows drivers, function wiring, interrupt controller, references and every property.
- **[`tools/duomap.py`](tools/duomap.py)**: command-line queries, for example:
  ```bash
  python3 tools/duomap.py node display1       # every property of the inner panel node
  python3 tools/duomap.py who gpu,t8160       # which driver binds a compatible string
  python3 tools/duomap.py irq 1226            # which block owns an interrupt line
  python3 tools/duomap.py addr 0x2a8000000    # which block owns a physical address
  python3 tools/duomap.py fn mesa_pwr         # who calls a function, on which provider
  python3 tools/duomap.py unbound             # nodes with no kernel driver
  ```
- **[`tools/build_all.sh`](tools/build_all.sh)** rebuilds every generated page from a restore image in one run (`tools/build_all.sh <ipsw> <scratch dir>`; syntax-checked, but not yet run end to end, and it names the ramdisk folders by image ID); the individual generators are in [`tools/`](tools/).

## Evidence labels

| Label | Source |
|---|---|
| **[DT]** | Device tree `DeviceTree.v68ap.im4p` |
| **[KC]** | Kernelcache `kernelcache.release.v6x-pandia` |
| **[FW]** | A firmware image in the IPSW |
| **[DSC]** | iOS 27.2 dyld shared cache |
| **[PUB]** | A public source, with URL |
| **[RD]** | A restore ramdisk file (`reference/ramdisk*`) |
| **[INF]** | Inference: reasoned, not observed |

Apple firmware and binaries are not included in this repository. Only derived tables, short excerpts and analysis are.

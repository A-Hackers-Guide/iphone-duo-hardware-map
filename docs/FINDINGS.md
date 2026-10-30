# Findings

These were fact-checked against the raw evidence on 2026-10-30; see [FACTCHECK](FACTCHECK.md), [FACTCHECK-2](FACTCHECK-2.md) and [FACTCHECK-3](FACTCHECK-3.md) and [FACTCHECK-4](FACTCHECK-4.md) for the 150 checked claims and the corrections applied.

The notable results across all chapters. Each item links to the chapter that has the evidence; the labels say what kind of evidence it is.

## Things the public specs don't say

| Finding | Evidence | Chapter |
|---|---|---|
| The SoC device tree serves **two chip bins**, `h19p` and `h19a`. On `h19p` the L2 caches are 8 MB (E) / 16 MB (P), with 29 thermal sensors and the second Neural Engine; on `h19a` they are 4 / 8 MB with 22 sensors. | [DT] `/borneo` options | [01](01-soc-cpu-memory-storage.md), [06](06-power-battery-thermal.md) |
| **LLB, iBoot, iBSS and iBEC are byte-identical** (one payload, `mBoot-20457.52.7`), and `/product single-stage-boot = 1`. | [FW] [DT] | [02](02-boot-and-security.md) |
| The hinge angle is not read from a dedicated sensor. **Each half has its own IMU** (accelerometer, gyro, high-g accelerometer, compass), and the AOP fuses the two into an angle. A Hall-effect sensor ("Crane") detects closed. | [DT] [FW] AOP strings | [05](05-sensors-touch-audio-haptics.md), [08](08-foldable-system-and-chassis.md) |
| **The inner panel is 1878 px wide (crease at row 1335, so 2670 high) at 430 ppi, but iOS renders into a 2007 × 2853 canvas** at the outer panel's 460 ppi, and the display pipe scales it down by ≈0.936. Both are real numbers. | [DT] `/arm-io/dispsec`, `/product/display1` | [03](03-gpu-and-displays.md) |
| **Three display controllers**, each with its own firmware co-processor and IOMMU: outer panel, inner panel, USB-C DisplayPort. The two panel controllers also have an exclave mailbox and a Mogul authentication chip each; the DisplayPort one has neither. | [DT] [KC] | [03](03-gpu-and-displays.md) |
| **The display firmware reads the hinge angle** and applies an angle-indexed correction. This is probably colour/luminance compensation for the folding OLED **[INF]**. | [FW] DCP strings | [03](03-gpu-and-displays.md) |
| **Two NFC controllers**: `stockholm` (primary, with the Secure Element) and `hammerfest` (secondary), each with its own antenna. | [DT] | [02](02-boot-and-security.md), [07](07-networking-and-connectivity.md) |
| **Two gas gauges and two PMUs.** BMU and BMU2 are the same chip, signed separately, and the kernel **feeds a per-pack impedance model to the SMC's charge rebalancer** (the rebalancer itself being in the SMC is inference). | [FW] BuildManifest, [DT], [KC] | [06](06-power-battery-thermal.md) |
| **GPS and satellite messaging live inside the C2 modem.** There is no discrete GNSS chip, and the "Stewie" satellite stack is in the modem firmware. | [FW] C2 ftab | [07](07-networking-and-connectivity.md) |
| **AOP2 has its own TCP/IP and TLS stack** and keeps push-notification connections alive while the main processor sleeps. | [FW] AOP2 strings, [KC] `RTKitNet` | [05](05-sensors-touch-audio-haptics.md), [07](07-networking-and-connectivity.md) |
| **Wi-Fi and Bluetooth have no in-kernel driver.** N1 ("Proxima/Centauri") is driven by three DriverKit extensions. | [KC] | [07](07-networking-and-connectivity.md) |
| **The nine video-encoder slice firmwares are RISC-V**, not ARM. | [FW] Mach-O CPU type `0x18` | [04](04-camera-media-neural-engine.md) |
| **Secure M3**, a camera-side ARM microcontroller, drives the camera sensor buses and the camera indicator light monitor, and talks to the ISP and exclaves. | [FW] [KC] | [02](02-boot-and-security.md), [04](04-camera-media-neural-engine.md) |
| The camera sensors are **not in the device tree**. The ISP firmware names four: WIDE, SWIDE, FCAM, INTCAM (the under-display inner one). | [FW] | [04](04-camera-media-neural-engine.md) |
| The Touch ID sensor's node **calls power functions on both Neural Engines**, and its driver logs the cover's closed state. | [DT] [KC] | [02](02-boot-and-security.md) |
| **Mando** is firmware for the touch processor's `nova` sensor, probably the Camera Control **[INF]**. | [FW] | [05](05-sensors-touch-audio-haptics.md) |
| AOP, AOP2, DCP and the C2 modem run a **pitayaOS 1223.40.8** roottask, with RTKit libraries linked in. | [FW] | [05](05-sensors-touch-audio-haptics.md), [07](07-networking-and-connectivity.md) |
| **SPTM sits between the kernel and the storage controller**, with NVMe-specific violation codes and protected ranges. | [FW] [DT] | [01](01-soc-cpu-memory-storage.md) |
| **The inner camera ("Reno") is fold-aware**: capture reads the hinge angle and drops or blacks out frames inside an angle "drop zone". It has its own public device type, `AVCaptureDeviceTypeBuiltInInnerUltraWideCamera`. | [DSC] CMCapture, AVFoundation | [12](12-userland-camera-ane-audio-security.md) |
| **The fold has a public API**: `UIHinge` / `UIHingeInteraction` (iOS 27.1+) report Closed / PartiallyOpen / FullyOpen and the angle in radians. WebKit uses it for `navigator.devicePosture`. | iOS 27.2 SDK headers, [DSC] UIKitCore, WebKit | [10](10-userland-display-fold-touch.md) |
| **Auto-brightness is fold-aware**: CoreBrightness drops ALS samples below 20° and re-weights three ALS channels between 20° and 70°. | [DSC] CoreBrightness | [10](10-userland-display-fold-touch.md) |
| locationd's cached hinge calibration is **discarded when IMU-related parts are repaired** (`AngleRepairState.plist`). | locationd strings from a vphone-duo guest (`data/08-foldable/`); locationd is not in the shared cache | [08](08-foldable-system-and-chassis.md) |

| **51 device-tree nodes exist only on the Duo** compared with the iPhone 18 Pro: a second display controller, second panel EEPROMs and auth chip, an extra I²C bus, a second touch sensor, a second IMU, two angle-aware light sensors, a second PMU, Touch ID on SPI1, and `secure-repair`. The 18 Pro has `pearl-sep` (Face ID) and `apr`, which the Duo lacks. | [DT] diff | [09](09-what-makes-it-a-duo.md) |
| **No ringer/Action button** and no Reachability; `supports-apple-pencil = 1`; `bmu-num-supported = 3`. | [DT] `/product` | [09](09-what-makes-it-a-duo.md) |

| **The Duo's FDR sealing map has 57 entries against the 18 Pro's 47** (42 distinct class tags on both; the Duo repeats several), including a secondary-screen certificate, two battery-pack certificates and the inner front camera. | [FW] ramdisk strings | [13](13-lifecycle.md) |
| **Firmware updates fall into three phases around FDR**: before recovery, between recovery and sealing, and after sealing. Each Duo chip has a named updater (battery gauges via `libT200Updater`, C2 via `libBBUpdaterDynamic`, N1 via `libCentauriUpdater`, NFC via `libnfrestore`, …). AOP, DCP and touch firmware is never flashed; it is loaded into RAM at every boot. | [FW] ramdisk | [13](13-lifecycle.md) |
| **No hinge calibration is stored at the factory.** Each half's IMU has its own syscfg keys; the hinge calibration is learned at runtime and thrown away after a repair. | [FW] [DSC] | [13](13-lifecycle.md), [08](08-foldable-system-and-chassis.md) |

| **The cellular stack is fold-aware**: `libBasebandManager` subscribes to the hinge angle, maps it into three "Osiris" states that switch antenna tuning and SAR selection, and kernel telemetry buckets the angle at 0/45/57/92/135/177/180/183°. | [DSC] | [11](11-userland-radios-power-sensors.md) |
| **N1's Bluetooth runs over shared-memory PCIe rings** (hci, acl, sco, le, lea), and Wi-Fi exposes six virtual interfaces (STA, AWDL, LowLatency, SoftAP, NAN, NAN-data). | [RD] dexts | [11](11-userland-radios-power-sensors.md) |

## Things that contradict, or don't match, the public specs

| Item | Detail | Chapter |
|---|---|---|
| Face ID material in a Touch ID phone | The manifest, device tree, exclave bundle and kernel all carry Pearl/Face ID components. Userland gates them on MobileGestalt `PearlIDCapability`, and the board has no IR camera channel, projector or Pearl SEP endpoint, so they are unreachable leftovers **[DSC][INF, strong]**. | [02](02-boot-and-security.md), [12](12-userland-camera-ane-audio-security.md) |
| Ambient light sensors | Apple says four. The device tree has three display ALS, plus a `grimaldi` flicker detector. | [05](05-sensors-touch-audio-haptics.md) |
| Inner peak brightness | The tables top out at 2,175 nits on the inner panel, against 3,000 on the outer. A second inner tuning reaches 3,000. | [03](03-gpu-and-displays.md) |
| Outer "Dynamic Island" | The outer cut-out is a 111 px circle whose centre is at x = 1254.5 px (frame 1199, 88, 111, 111), about 90% across the panel's public 1398 px width: an off-centre punch-hole. The inner cut-out is called `BlankableRR`. | [03](03-gpu-and-displays.md), [08](08-foldable-system-and-chassis.md) |
| Hinge HID usage | Three usages appear: 0xFF0C/0x21, 0xFF0C/0x1C ("Crane") and 0x20/0xE4 ("Hinge Angle"). Resolved in [10](10-userland-display-fold-touch.md): CoreMotion opens 0x21 always and reads 0x20/0xE4 on real hardware; nothing in userland consumes 0x1C. | [05](05-sensors-touch-audio-haptics.md), [08](08-foldable-system-and-chassis.md) |
| SMC firmware | The device tree names `t8160smc`, but no such image is in the IPSW or the manifest. | [05](05-sensors-touch-audio-haptics.md), [06](06-power-battery-thermal.md) |
| Action button | An SMC PMU `action` event exists; no action button is in the device tree or the specs. | [05](05-sensors-touch-audio-haptics.md) |
| ProRes | A ProRes power state, plug-ins and a kext (`AppleProResHW`) exist, but no device-tree node, so hardware ProRes is unavailable and software codecs remain. | [04](04-camera-media-neural-engine.md), [12](12-userland-camera-ane-audio-security.md) |

## Not knowable from these sources

The restore image's device tree is a template. RAM size and vendor, the DRAM carveout map, clock values, panel timing, rail voltages and the SMC key map are all zero, empty or absent. Also out of reach:

- **Encrypted payloads:** SEP OS, SepStage1, the Secure Element and the eUICC.
- **Physical layout:** schematics, which half holds which part, and anything at transistor level.

Each chapter's "Gaps and limits" section lists its own.

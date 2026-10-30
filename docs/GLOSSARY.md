# Glossary: codenames and acronyms

Apple's firmware, device tree and binaries name parts by codename. This table says what each one is on the Duo and which chapters discuss it. A meaning marked **[INF]** is inferred; the chapter has the evidence and the caveats.

## Parts and chips

| Name | What it is | Chapters |
|---|---|---|
| **Sawtooth** / **Everest** | The A20 Pro's efficiency (`apple,sawtooth`, cpu0–3) and performance (`apple,everest`, cpu4–5) CPU cores. | [01](01-soc-cpu-memory-storage.md), [02](02-boot-and-security.md) |
| **H19 / H19P / H19A**, `t8160` | The SoC generation and its two bins; `t8160` is the SoC. One device tree carries both bins: `/:borneo` lists the options, and `:borneo_h19p_N` / `:borneo_h19a_N` overlay children sit under the CPU, PMP and USB nodes they patch. | [01](01-soc-cpu-memory-storage.md), [06](06-power-battery-thermal.md) |
| **Borneo** | The device-tree node that holds per-bin options (`h19p`, `h19a`). | [01](01-soc-cpu-memory-storage.md), [06](06-power-battery-thermal.md) |
| **AGX G19P** | The GPU and its kext family (`AGXG19P`). | [03](03-gpu-and-displays.md) |
| **Perses** | The Neural Engine firmware line (`h19_ane*_fw_perses_v6x`). | [04](04-camera-media-neural-engine.md) |
| **Mesa** / **SandDollar** | The Touch ID fingerprint sensor in the side button (`biosensor,mesa`) and its driver classes. | [02](02-boot-and-security.md), [05](05-sensors-touch-audio-haptics.md), [09](09-what-makes-it-a-duo.md), [12](12-userland-camera-ane-audio-security.md) |
| **Pearl**, **Rosaline**, **JasmineIR** | Face ID components (sensor, calibration, IR). Present in software, not reachable on the Duo. | [02](02-boot-and-security.md), [09](09-what-makes-it-a-duo.md), [12](12-userland-camera-ane-audio-security.md) |
| **Crane** | The fold subsystem: the Hall-effect sensor (`crane_hes`) and its HID driver ("Apple Crane Driver"). | [05](05-sensors-touch-audio-haptics.md), [08](08-foldable-system-and-chassis.md) |
| **Medina** | A fold state machine in AOP firmware that combines the Hall sensor with the angle. | [05](05-sensors-touch-audio-haptics.md), [08](08-foldable-system-and-chassis.md) |
| **cypher2** | The two touch controllers (Cortex-M), one per panel. | [05](05-sensors-touch-audio-haptics.md) |
| **Nova** / **Mando** | The touch processor's `nova` sensor, i.e. the Camera Control, and its firmware (`V68_MandoFirmware`). | [04](04-camera-media-neural-engine.md), [05](05-sensors-touch-audio-haptics.md), [12](12-userland-camera-ane-audio-security.md) |
| **LEAP** | The haptics engine block; its firmware is loaded by AOP audio firmware. | [05](05-sensors-touch-audio-haptics.md), [12](12-userland-camera-ane-audio-security.md) |
| **Grimaldi** | A photon / flicker detector near the display ALS. | [05](05-sensors-touch-audio-haptics.md) |
| **Jindo** | The outer panel's cut-out region type. The inner one is `BlankableRR`. | [03](03-gpu-and-displays.md), [08](08-foldable-system-and-chassis.md) |
| **Hilo** | A child node of each display pipe (`/arm-io/disp0/hilo`, `/arm-io/dispsec/hilo`); the second is Duo-only. | [09](09-what-makes-it-a-duo.md) |
| **Mogul** | `mogul,a1222` authentication chips: one per panel on I²C3, one for the main board on I²C4. | [03](03-gpu-and-displays.md), [09](09-what-makes-it-a-duo.md) |
| **Reno** / **Omaha** | The inner (under-display) camera in userland, and the "Omaha Reno Angle Drop Zone" fold range where its frames are dropped. | [04](04-camera-media-neural-engine.md), [12](12-userland-camera-ane-audio-security.md) |
| **WIDE / SWIDE / FCAM / INTCAM** | The ISP firmware's names for the main, ultra-wide, outer front and inner cameras. | [04](04-camera-media-neural-engine.md) |
| **Boreas** | The ISP firmware (`adc-boreas-v68`). | [04](04-camera-media-neural-engine.md) |
| **Glenbrook** / **Lakeville** | Front camera module tunings; their `YonkersIR1/2` patch sets live in the firmware folder. | [04](04-camera-media-neural-engine.md), [12](12-userland-camera-ane-audio-security.md) |
| **Yonkers** / **Savage** | Camera-module security chips and their updaters (`YonkersUtil`, `SavageUtil`). Not Touch ID and not IR sensors. | [02](02-boot-and-security.md), [04](04-camera-media-neural-engine.md), [12](12-userland-camera-ane-audio-security.md) |
| **Secure M3** | A camera-side secure microcontroller (`securem3fw`) that drives the camera buses and the indicator-light monitor. | [02](02-boot-and-security.md), [04](04-camera-media-neural-engine.md) |
| **ABDNet** | The neural network that cleans up the under-display camera's image, run on the bonded ANEs. | [04](04-camera-media-neural-engine.md), [12](12-userland-camera-ane-audio-security.md) |
| **RDLC** | The display firmware's hinge-angle-indexed correction. | [03](03-gpu-and-displays.md) |
| **Becketts** / **Fairmont** | The main PMU and the secondary PMU behind its serial-GPIO bridge. | [06](06-power-battery-thermal.md), [09](09-what-makes-it-a-duo.md) |
| **Volchok**, **BMU/BMU2** | The battery gas-gauge firmware (BAT8193) and the two gauges it runs on. | [06](06-power-battery-thermal.md) |
| **Stonehenge** | A battery-protection IC node (driver `AppleStonehengeBPIC` exists, nothing binds). | [06](06-power-battery-thermal.md) |
| **Shamisen** | An SPMI device node with no known driver. | [06](06-power-battery-thermal.md) |
| **CLPC**, **PPM**, **CPMS** | The CPU performance controller, the peak power manager and the power-management service in the kernel. | [01](01-soc-cpu-memory-storage.md), [06](06-power-battery-thermal.md) |
| **Lifetime servo** | PMP firmware loop that caps voltage and temperature to limit long-term silicon wear. | [01](01-soc-cpu-memory-storage.md), [06](06-power-battery-thermal.md) |
| **C2**, **c4020**, **Leda**, **Ganymede** | The cellular modem, its chip ID, its PCIe endpoint (`baseband-pcie-leda`) and its RF recipe file (`Ganymede_HWID_0038`). | [07](07-networking-and-connectivity.md) |
| **Stewie** | The satellite messaging stack inside the C2 firmware. | [07](07-networking-and-connectivity.md), [11](11-userland-radios-power-sensors.md) |
| **Vinyl** | The eUICC (eSIM) firmware, by Giesecke+Devrient. | [02](02-boot-and-security.md), [07](07-networking-and-connectivity.md) |
| **N1**, **Proxima** / **Centauri** | The Wi-Fi 7 / Bluetooth 6 / Thread chip and its codenames; driven by the `AppleCentauri{Control,Alpha,Beta}` DriverKit extensions. | [07](07-networking-and-connectivity.md), [11](11-userland-radios-power-sensors.md) |
| **Fillmore** | The device-tree node holding the Thread radio's address. | [07](07-networking-and-connectivity.md) |
| **Rose** | The Ultra Wideband chip (`Firmware/Rose/r2p1`). | [07](07-networking-and-connectivity.md) |
| **Stockholm** / **Hammerfest** | The primary NFC controller with the Secure Element, and the secondary NFC controller. | [02](02-boot-and-security.md), [07](07-networking-and-connectivity.md) |
| **ULPN** | AOP2's ultra-low-power push networking: it keeps Apple Push connections alive while the AP sleeps. | [05](05-sensors-touch-audio-haptics.md), [07](07-networking-and-connectivity.md) |
| **pitayaOS** | The roottask OS of AOP, AOP2, DCP and the C2 modem (RTKit libraries are linked in). | [05](05-sensors-touch-audio-haptics.md), [07](07-networking-and-connectivity.md) |
| **Osiris** | Three cellular fold states that `libBasebandManager` derives from the hinge angle; they drive antenna tuning ("State A/B") and SAR selection. | [11](11-userland-radios-power-sensors.md) |
| **Darwin / Cairns / Brisbane** | The ambient-light-sensor channels CoreBrightness re-weights between 20° and 70° of fold. | [10](10-userland-display-fold-touch.md) |
| **D76 / D77** | Home-screen layout classes in SpringBoardHome; the cover display resolves to D76. | [08](08-foldable-system-and-chassis.md), [10](10-userland-display-fold-touch.md) |
| **Atlantis** | `AtlantisFirmware-57.0.0`: a program linked into the AOP firmware in trusted and untrusted builds. | [firmware SBOM](../reference/maps/firmware-sbom.md) |
| **Veridian / T200** | The battery-gauge updater (`libT200Updater`) that flashes BMU and BMU2 by `PackIndex` during restore. | [13](13-lifecycle.md) |
| **AFK / AppleFirmwareKit** | The framework DCP and AOP2 firmware is built on; `AFKFirmwareService` is the kernel class behind the DCP firmware personalities. | [03](03-gpu-and-displays.md), [FACTCHECK-2](FACTCHECK-2.md) |
| **FDR sealing map** | The factory list of sealed component certificates: 57 entries on the Duo, 47 on the 18 Pro. | [13](13-lifecycle.md) |

## Software and security terms

| Name | What it is | Chapters |
|---|---|---|
| **RTKit** / **RTBuddy** | Apple's co-processor RTOS and the kernel-side mailbox protocol to it. | [01](01-soc-cpu-memory-storage.md), [03](03-gpu-and-displays.md) |
| **SPTM** | Secure Page Table Monitor: owns page tables and memory types below the kernel. | [01](01-soc-cpu-memory-storage.md), [02](02-boot-and-security.md) |
| **TXM** | Trusted Execution Monitor: code-signing and trust-cache enforcement below the kernel. | [02](02-boot-and-security.md) |
| **cL4** / **exclaves** / **ExclaveOS** | The isolated microkernel and its compartments that own secure paths (indicator lights, display, camera, audio). | [02](02-boot-and-security.md) |
| **Tightbeam** | The IPC system used between exclaves, co-processors and the kernel. | [02](02-boot-and-security.md), [04](04-camera-media-neural-engine.md) |
| **xART** | The storage-backed replacement for effaceable storage, holding key material. | [01](01-soc-cpu-memory-storage.md), [02](02-boot-and-security.md), [12](12-userland-camera-ane-audio-security.md) |
| **DART** / **SART** | Apple's IOMMUs (per device) and the storage controller's address filter. | [01](01-soc-cpu-memory-storage.md) |
| **DCP** / **DCPSEC** / **DCPEXT** | The display co-processors: outer panel, inner panel, USB-C DisplayPort. | [03](03-gpu-and-displays.md) |
| **AOP** / **AOP2** | The two always-on processors: sensors and audio; always-on networking and GNSS. | [05](05-sensors-touch-audio-haptics.md) |
| **MTP** | The multitouch co-processor driving both touch controllers. | [05](05-sensors-touch-audio-haptics.md) |
| **ANS** | The NVMe storage controller co-processor. | [01](01-soc-cpu-memory-storage.md) |
| **AVE** / **AVD** | The video encoder (with nine RISC-V slice firmwares) and decoder. | [04](04-camera-media-neural-engine.md) |
| **FDR** | Factory data restore: the factory-provisioned calibration and pairing data. | [13](13-lifecycle.md) |

# 14: Power button to home screen: a cold boot of the Duo, end to end

This chapter follows one cold boot of the iPhone Duo (`iPhone19,4`, `V68AP`, SoC `t8160`, iOS 27.2 `24B91020`) in time order. It starts with the side button pressed on a phone that is off. It ends with the first home-screen frame on the live panel (folded: outer; open: inner) and the first tap delivered to an app.

**Nothing here is new evidence.** Every step is assembled from chapters [01](01-soc-cpu-memory-storage.md), [02](02-boot-and-security.md), [03](03-gpu-and-displays.md), [05](05-sensors-touch-audio-haptics.md), [06](06-power-battery-thermal.md), [08](08-foldable-system-and-chassis.md), [10](10-userland-display-fold-touch.md) and [13](13-lifecycle.md), the [MAP](MAP.md), the [co-processor matrix](../reference/maps/coprocessors.md) and the [function references](../reference/maps/function-references.md). Node facts were rechecked with `tools/duomap.py`. The evidence labels are the ones the chapters use (legend in [MAP](MAP.md); sources in [00-method-and-evidence.md](00-method-and-evidence.md)), and each keeps the meaning its source chapter gave it:

| Label | Meaning |
|---|---|
| **[DT]** | Device tree in the IPSW (a template; iBoot fills `/chosen` at boot) |
| **[KC]** | Kernelcache (kext personalities, strings) |
| **[FW]** | Firmware images, BuildManifest, iBoot/SPTM strings |
| **[DSC]** | dyld shared cache (userland frameworks) |
| **[RD]** | Restore ramdisk (not needed on the normal boot path; no step here uses it) |
| **[PUB]** | Public sources (Apple Platform Security guide, teardowns) |
| **[INF]** | Inference, not shown directly by the sources |

A `?` in a cell means the chapters do not establish that fact. Where only the **order** between two steps is unknown, the step is kept and its position is marked **[INF]**.

---

## Contents

0. [How to read the trace](#0-how-to-read-the-trace)
1. [Sequence diagram](#1-sequence-diagram)
2. [The trace, step by step](#2-the-trace-step-by-step)
   - [Phase A: side button to SoC power-up](#phase-a-side-button-to-soc-power-up)
   - [Phase B: SecureROM and mBoot (LLB = iBoot)](#phase-b-securerom-and-mboot-llb--iboot)
   - [Phase C: SPTM, TXM, exclaves, XNU](#phase-c-sptm-txm-exclaves-xnu)
   - [Phase D: the kernel brings up the co-processors](#phase-d-the-kernel-brings-up-the-co-processors)
   - [Phase E: userland up to SpringBoard](#phase-e-userland-up-to-springboard)
   - [Phase F: which panel is live at boot](#phase-f-which-panel-is-live-at-boot)
   - [Phase G: the first home-screen frame](#phase-g-the-first-home-screen-frame)
   - [Phase H: the first tap reaches an app](#phase-h-the-first-tap-reaches-an-app)
3. [Which co-processors are running by the time SpringBoard draws](#3-which-co-processors-are-running-by-the-time-springboard-draws)
4. [Gaps](#4-gaps)

---

## 0. How to read the trace

Each step in §2 gives:

- **#**: time order. Steps inside one phase follow each other in the order shown. Where a source only lists names (for example a string table) and not a sequence, the row says so.
- **Who acts**: the processor or core doing the work.
- **Running**: the firmware or software on that core.
- **Hardware touched**: device-tree nodes, linked to their page in `../reference/devicetree/`.
- **Hands to next**: what this step produces for the following one.
- **Source**: the chapter section the row rests on, and its evidence labels.

Two things the chapters state about the boot as a whole frame everything below:

- **Single-stage boot.** LLB, iBoot, iBSS and iBEC are one byte-identical "mBoot" image (`mBoot-20457.52.7`), and `/product single-stage-boot = 1`. There is no separate second-stage iBoot on the normal path **[FW][DT]**; that SecureROM loads it once and it goes on to load the kernel is **[INF]** ([02 §1, "Single-stage boot"](02-boot-and-security.md#single-stage-boot-llb-is-iboot)).
- **Firmware is RAM-loaded on every boot.** AOP/AOP2, DCP, ISP, GPU, ANE, PMP, SIO, Multitouch, Mando, haptics and Secure M3 are never flashed. iBoot or the kernel loads them from Preboot/FUD on each boot **[FW]** ([13 §2.4](13-lifecycle.md#24-chip-by-chip-order-updater-and-evidence), [13 §4.3](13-lifecycle.md#43-firmware-that-updates-outside-a-restore)).

---

## 1. Sequence diagram

Arrows between participants are hand-offs from §2. A `?` in a note marks an order or a step the chapters do not establish.

```mermaid
sequenceDiagram
    autonumber
    actor U as User
    participant PMU as PMU becketts (pmu-main)
    participant AP as AP cpu0: SecureROM, then mBoot
    participant SEP as SEP (Boot ROM, then SEP OS)
    participant MON as SPTM / TXM / cL4 (AP)
    participant XNU as XNU + IOKit (AP)
    participant IOP as RTKit IOPs (ANS, PMP, AOP, AOP2, DCP, DCPSEC, MTP, GFX, SMC)
    participant UL as Userland (launchd?, backboardd, locationd, SpringBoard)
    participant PNL as Panel (disp0 outer / dispsec inner)

    U->>PMU: Press side button ("hold") with the phone off
    Note over PMU: Which o2ws wake source the button raises: ?
    PMU->>AP: Rails up, SoC out of reset (sequence: ? / INF)
    AP->>AP: SecureROM: fuses, load + verify LLB (= mBoot) [PUB/FW]
    AP->>PMU: mBoot: PMU over SPMI, battery checks, PMU fw update possible [FW]
    AP->>AP: DRAM init (DCS/AMCC), syscfg v3, NVRAM, boot-args [FW]
    AP->>PNL: Apple logo from EAN (AppleLogo, DCP image) - which panel: ?
    AP->>SEP: sep-patches (SepStage1) + sep-firmware [FW/DT]
    AP->>AP: Load FUD firmware (AOP, AOP2, SIO, PMP, ANE, GFX, ISP, SecureM3, MTP, PMC) [FW]
    Note over AP,IOP: Whether iBoot starts these cores or only stages them: ?
    AP->>AP: Load DT, trust caches, SPTM, TXM, cL4, root_hash, kernelcache; fill /chosen; lock CTRR [FW/DT]
    AP->>MON: Jump to SPTM
    MON->>MON: SPTM -> TXM -> cL4 (order INF)
    MON->>XNU: "Bootstrapping XNU..." [FW]
    XNU->>IOP: AppleASCWrapV8 -> RTBuddy per IOP; PMGR/PMP drivers [KC]
    XNU->>SEP: AppleSEPManager boots SEP OS; AppleKeyStore [KC]
    XNU->>IOP: ANS2 -> NVMe -> APFS (SPTM in NVMe submission path) [KC/DT]
    XNU->>IOP: AOP (SPU HID), DCP/DCPSEC (AppleCLCD2), MTP (touch fw download + auth) [KC]
    Note over XNU,IOP: Relative order of these matches: ? (IOKit matching, INF)
    XNU->>UL: Start userland (launchd: not covered by the chapters, ?)
    UL->>UL: backboardd: CA render server opens both IOMFBs; HID system binds digitizers per display [DSC]
    IOP->>UL: AOP hinge angle + HES -> IOHIDEvent 0x2C -> locationd CLAngleNotifier [FW/KC/DSC]
    UL->>UL: SpringBoard: SBFDevicePoseProvider -> content-mode resolver [DSC]
    alt folded (FullyClosed)
        UL->>PNL: primary = .cover -> DCP -> disp0 (outer)
    else open (FoldingDual)
        UL->>PNL: primary = .inner -> DCPSEC -> dispsec (inner); .cover = passive shield
    end
    Note over UL,PNL: First home-screen frame (GPU render -> CA composite -> IOMFB swap -> DCP)
    U->>IOP: Tap on live panel -> touch ASIC -> MTP
    IOP->>XNU: MTPEndpoint1 mailbox -> AppleMultitouchHIDService [KC]
    XNU->>UL: IOHIDEvent -> backboardd (displayUUID) -> SpringBoard (home screen) or app -> UITouch [DSC/INF]
```

---

## 2. The trace, step by step

### Phase A: side button to SoC power-up

| # | Who acts | Running | Hardware touched | Hands to next | Source |
|---|---|---|---|---|---|
| A1 | User; side button | none | [`/buttons`](../reference/devicetree/root__buttons.md) declares `hold` (priority 1, `button-delay_hold 75000`) with `function-button_hold` → phandle 0x9f = [`smc-pmu`](../reference/devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md), whose `event_name-btn1 = hold` | A button event at the PMU side. The `/buttons` → `smc-pmu` path is the **running-OS** path (drivers `AppleM68Buttons`, `AppleSMCPMU`); what carries the press while the SoC is off is **?** | [05 §6](05-sensors-touch-audio-haptics.md#6-buttons-sidetouch-id-camera-control-volume), [06 §2](06-power-battery-thermal.md#2-the-smc--owner-of-charging-gauges-and-power-telemetry) **[DT][KC]**; `duomap node /buttons` |
| A2 | Primary PMU "becketts" | PMU firmware `ApplePMUFirmware-743.40.11~956.release` (shipped inside iBoot; resident in the PMU **[INF]**) | [`/arm-io/nub-spmi0/pmu-main`](../reference/devicetree/root__arm-io__nub-spmi0__pmu-main.md) (`is-primary 1`, `has-fw 1`, `info-off2wake_source`, 15 `info-o2ws_name-N` wake causes, including `gcb_off_wakeup`, `rtc_alarm_wakeup`, `auto_wakeup`) | An off-to-wake transition. **Which o2ws name the side button maps to is not stated** (none of the 15 wake causes names a button; the button names, `btn_shdn`, `btn_rst,*` and `sstate,button_dfu_recover`, are in the separate `info-fault_name-N` list of shutdown/reset causes) → **?** | [06 §1.1](06-power-battery-thermal.md#11-pmu-main--becketts-primary-pmu) **[DT][FW]** |
| A3 | PMU(s) → SoC rails | PMU firmware | `pmu-main` and [`pmu-secondary`](../reference/devicetree/root__arm-io__nub-spmi0.md) ("fairmont") on `nub-spmi0`; both batteries feed `VDD_MAIN` | SoC rails (DCS / SOC / DISP / AVE / CPU / GPU) powered; AP released from reset. **Rail order, voltages and the reset release are not in the sources → ?** | [06 §0](06-power-battery-thermal.md#0-one-screen-summary), [06 §13](06-power-battery-thermal.md#13-gaps-and-limits) **[DT][INF]** |
| A3′ | (alternative branch) AP running AppleLPM | `Ap,LowPowerMode` (`alpm`, RTKit armv8, iBoot-EAN) | Both display pipes ("DCP workloop" / "DCP2 workloop"); PMU scratch `info-scrpad_lpm_ctrl` 0xa7dc | If the battery is too low for iOS, iBoot can boot this small OS instead and show a clock/charging screen; it has a "System reboot to OS" state. How iBoot chooses is **?** | [06 §6](06-power-battery-thermal.md#6-applelpm-lpem-and-power-reserve) **[FW][DT][INF]** |

### Phase B: SecureROM and mBoot (LLB = iBoot)

| # | Who acts | Running | Hardware touched | Hands to next | Source |
|---|---|---|---|---|---|
| B1 | AP `cpu0` (E-core, `apple,sawtooth`) | SecureROM (mask ROM, not in the IPSW) | [`/cpus/cpu0`](../reference/devicetree/root__cpus__cpu0.md) (template `state "waiting"`); root `/` `device_type "bootrom"`; fuses (ECID, security domain, prod/dev) | That boot runs on `cpu0` and the other cores stay parked is **[INF]** | [02 §1 "Who runs what"](02-boot-and-security.md#who-runs-what) **[DT][PUB][INF]** |
| B2 | AP `cpu0` | SecureROM | NAND via storage. **How SecureROM reads NAND before the kernel's ANS stack exists is not shown**: the `ANS` component is `IsLoadedByiBoot: false`; the chapter calls the normal-boot path "the boot chain's storage path" **[INF]** | Verified LLB image (`illb`, payload = mBoot-20457.52.7), checked against the IM4M (APTicket). DFU alternative: iBSS then iBEC over USB | [02 §1 steps 1–2](02-boot-and-security.md#the-sequence), [01 §8.1](01-soc-cpu-memory-storage.md#81-hardware-and-firmware) **[FW][PUB][INF]** |
| B3 | AP | mBoot | DRAM: [`/arm-io/mcc`](../reference/devicetree/root__arm-io__mcc.md) (`DCS Init`, AMCC density, DRAM fuse reads) | Working DRAM | [02 §1 step 3](02-boot-and-security.md#the-sequence) **[FW]** |
| B4 | AP | mBoot | SPMI masters `NUB_SPMI0..2`, `AOP_SPMI0/1`; [`pmu-main`](../reference/devicetree/root__arm-io__nub-spmi0__pmu-main.md) | PMU configured; PMU firmware can be updated by iBoot; `battery voltage %d mV`, `precharge-battery-state`, `boot-battery-state` checked. Both PMUs' firmware is loaded over the `fw-mcom` mailbox **[INF]** | [02 §1 step 3](02-boot-and-security.md#the-sequence), [06 §1.1](06-power-battery-thermal.md#11-pmu-main--becketts-primary-pmu), [13 §4.3](13-lifecycle.md#43-firmware-that-updates-outside-a-restore) **[FW][INF]** |
| B5 | AP | mBoot | syscfg on NVMe (`nvme_syscfg%d`, v3 with HMAC), NVRAM banks | `boot-args`, `auto-boot`, early keybags (`syscfg-erly-kbgs`), real calibration pointers for the `syscfg/…` DT properties | [02 §1 step 4](02-boot-and-security.md#the-sequence), [13 §3](13-lifecycle.md#3-activation-and-first-boot) **[FW][DT]** |
| B6 | AP | mBoot | NVMe "EAN" area (`nvme_ean`, `/defaults ean-storage-present`) holding the six `IsiBootEANFirmware` images: `AppleLogo`, `RecoveryMode`, `Liquid`, `DCP`, `Ap,LowPowerMode`, `WCHFirmwareUpdater` | Apple logo on a panel; `Liquid` / `RecoveryMode` images if needed. That iBoot reads EAN before APFS exists is **[INF]**. **Which panel shows the logo, whether the fold state decides it, and whether iBoot runs the DCP firmware itself are all ?** (iBoot does name "ALPM Display" / "ALPM Display Sec" for AppleLPM, so it knows both pipes **[FW]**) | [02 §1 step 3](02-boot-and-security.md#the-sequence), [02 §5](02-boot-and-security.md#5-every-buildmanifest-component-and-who-consumes-it), [03 §2.3](03-gpu-and-displays.md#23-dcp-firmware-t8160dcpim4p), [06 §6](06-power-battery-thermal.md#6-applelpm-lpem-and-power-reserve) **[FW][DT][INF]** |
| B6a | ? | `Ap,AudioBootChime` (`aubt`, PCM, `IsiBootNonEssentialFirmware`) | speaker path; `audio-speaker iboot-audio-volume 0x7fff`; `/product has-boot-chime = 1` | A boot chime. **Which stage plays it (iBoot or the kernel audio driver) was not found → ?** | [05 §7.4](05-sensors-touch-audio-haptics.md#74-boot-chime), [02 §1 step 3](02-boot-and-security.md#the-sequence) **[FW][DT][KC]** |
| B7 | AP → SEP | mBoot hands over; SEP Boot ROM patched by `SepStage1` | [`/arm-io/sep`](../reference/devicetree/root__arm-io__sep.md); `/chosen sepfw-load-at-boot = 1` | `sep-patches.img4` and `sep-firmware.img4` (GID-wrapped `sepi`). The SEP verifies and decrypts its own firmware **[PUB]** | [02 §1 step 5](02-boot-and-security.md#the-sequence), [02 §10](02-boot-and-security.md#10-secure-enclave-sep) **[FW][DT][PUB]** |
| B8 | AP | mBoot | Preboot/FUD: `AOP`, `AOP2`, `SIO`, `PMP`, `ANE`, `Ap,ANE1`, `GFX`, `Ap,GFX1Firmware`, `ISP`, `AVE`, `Ap,AVD`, `Ap,AppleVideoEncoder0..8`, `Ap,MSRFirmware`, `Ap,SecureM3Firmware`, `MtpFirmware`; also `Ap,ApplePMCFirmware` | Each image verified and placed in memory (e.g. AOP region `0x290c00000`). **Whether iBoot also starts each core, or only stages the image for the kernel, is not stated → ?** One hint: PMP firmware has "PMP started!!!", "PMC Keep Alive" and "SEP UP" strings **[FW]** | [02 §1 step 6](02-boot-and-security.md#the-sequence), [06 §7.1–7.2](06-power-battery-thermal.md#71-pmp--power-manager-processor), [01 §5.1](01-soc-cpu-memory-storage.md#51-pmgr-arm-iopmgr-and-arm-iopmgr-child) **[FW][DT]** |
| B9 | AP | mBoot | — | DeviceTree, iBootData, `StaticTrustCache`, ExclaveOS trust cache + integrity catalog, `Ap,cL4`, `Ap,SecurePageTableMonitor`, `Ap,TrustedExecutionMonitor`, `root_hash.img4` (sealed system volume), kernelcache | [02 §1 step 7](02-boot-and-security.md#the-sequence) **[FW]** |
| B10 | AP | mBoot (`lay_out_sptm_objects`, `lay_out_opaque_kernelcache`) | [`/chosen`](../reference/devicetree/root__chosen.md), [`/chosen/lock-regs/amcc`](../reference/devicetree/root__chosen__lock-regs__amcc.md) (`amcc-ctrr-a..d`) | `/chosen` filled (`boot-manifest-hash`, `boot-nonce`, `effective-*`, `cl4-entropy`, `random-seed`, …); kernel read-only regions locked (CTRR); the SoC-bin thermal table (`h19p`/`h19a`) chosen **[INF]** | [02 §1 step 8](02-boot-and-security.md#the-sequence), [02 §3](02-boot-and-security.md#3-chosen-what-iboot-tells-the-kernel), [06 §0 item 7](06-power-battery-thermal.md#0-one-screen-summary) **[FW][DT][INF]** |

### Phase C: SPTM, TXM, exclaves, XNU

| # | Who acts | Running | Hardware touched | Hands to next | Source |
|---|---|---|---|---|---|
| C1 | AP | SPTM (`sptm.t8160.release.im4p`) | MMIO allow-lists `sptm-allow-reg` on e.g. [`/arm-io/mtp`](../reference/devicetree/root__arm-io__mtp.md), [`/arm-io/smc/iop-smc-nub`](../reference/devicetree/root__arm-io__smc__iop-smc-nub.md); [`/defaults`](../reference/devicetree/root__defaults.md) `pmap-io-ranges`, `nvme-iboot-sptm-security` | Page-type tracking; control of what XNU can map | [02 §1 step 9](02-boot-and-security.md#the-sequence), [02 §8](02-boot-and-security.md#8-sptm-and-txm) **[FW][DT]** |
| C2 | AP | TXM (`txm.iphoneos.release.im4p`) | TXM↔SEP channel in [`/arm-io/dart-sep`](../reference/devicetree/root__arm-io__dart-sep.md) (`txm-secure-channel-base`); `/chosen txm-secure-channel = 1` | Code-signing monitor running ("TXM-entry") | [02 §8](02-boot-and-security.md#8-sptm-and-txm) **[FW][DT][KC]** |
| C3 | AP | cL4 / ExclaveCore + roottask | `exclave-memory-map`, `cL4-kernel/asc`; exclave mailboxes (e.g. `aop-exclave-mailbox`, `dcp-exclave-mailbox`) | Exclave world ready for XNU to enter through `sk_enter` | [02 §1 step 9](02-boot-and-security.md#the-sequence), [02 §9](02-boot-and-security.md#9-exclaves) **[FW][KC][DT]** |
| C4 | AP | XNU `xnu-13432.52.2~7/RELEASE_ARM64_T8160` | — | "Bootstrapping XNU...". The order SPTM → TXM → cL4 → XNU is **[INF]** from strings. That XNU then starts `cpu1`–`cpu5` is **[INF]** | [02 §1 steps 9–10](02-boot-and-security.md#the-sequence) **[FW][KC][INF]** |

### Phase D: the kernel brings up the co-processors

IOKit matching is concurrent. The chapters give the driver chain for each block but **no order between blocks**, so the rows below are grouped by dependency, and their relative order is **[INF]** unless a row says otherwise.

| # | Who acts | Running | Hardware touched | Hands to next | Source |
|---|---|---|---|---|---|
| D1 | AP (XNU) + PMP + PMC | `ApplePMGRv2`, `AppleT8160PMGR`; `ApplePMPFirmware` → `ApplePMPv2`, `ApplePMPThermal` (PMP fw `t8160pmp`, RTKit; PMC fw `t8160pmcfw`, ARMv7-M) | [`/arm-io/pmgr`](../reference/devicetree/root__arm-io__pmgr.md), [`/arm-io/pmgr-child`](../reference/devicetree/root__arm-io__pmgr-child.md), [`/arm-io/pmp`](../reference/devicetree/root__arm-io__pmp.md) (nub `firmware-name t8160pmp`) | Power gates, clocks and DVFS under kernel control; PMP control loops (DCS/SOC/DISP/AVE) running | [01 §5.1–5.2](01-soc-cpu-memory-storage.md#52-pmp-power-manager-processor), [06 §7](06-power-battery-thermal.md#7-pmp-pmc-pmgr-rails-and-clpc) **[DT][KC][FW]** |
| D2 | SEP | SEP OS (booted by `AppleSEPManager`) | [`/arm-io/sep/iop-sep-nub`](../reference/devicetree/root__arm-io__sep__iop-sep-nub.md); [`/arm-io/esm`](../reference/devicetree/root__arm-io__esm.md) → `ExclaveSEPManagerProxy` | `AppleKeyStore`, `AppleCredentialManager`, AMFI, `AppleImage4` ready; "keybag unlock path ready" | [02 §1 step 10 and diagram](02-boot-and-security.md#the-sequence), [02 §10](02-boot-and-security.md#10-secure-enclave-sep) **[KC][DT]** |
| D3 | ANS2 (ASP) | `ansf.t8160` (`AppleStorageFirmware-3975.40.15~303`, RTKit) under `AppleASCWrapV8` → `RTBuddy` → `AppleANS*NVMe…Controller` (winner by `probe()`) | [`/arm-io/ans`](../reference/devicetree/root__arm-io__ans.md), [`/arm-io/ans/iop-ans-nub`](../reference/devicetree/root__arm-io__ans__iop-ans-nub.md), [`/arm-io/sart-ans`](../reference/devicetree/root__arm-io__sart-ans.md); NVMe IRQ 1280 | `IONVMeBlockStorageDevice` → `IOMedia` → APFS container/volumes; `NVMeSEPNotifier` ← `AppleSEPManager`. SPTM sits in the NVMe submission path **[INF]**; the sealed system volume is checked against `root_hash` **[FW]**. **Who loads the ANS firmware on a normal boot is ? (manifest: `ANS` not loaded by iBoot)** | [01 §8.1–8.2](01-soc-cpu-memory-storage.md#82-kernel-driver-chain), [02 §5](02-boot-and-security.md#5-every-buildmanifest-component-and-who-consumes-it) **[DT][KC][FW][INF]** |
| D4 | SMC | SMC firmware `t8160smc` (`pre-loaded = 0`; **source image not found**) | [`/arm-io/smc`](../reference/devicetree/root__arm-io__smc.md), [`smc-pmu`](../reference/devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) → `AppleSMCPMU` | Button events (`btn1 hold`), charger and gauges via SMC keys, available to the OS | [06 §2](06-power-battery-thermal.md#2-the-smc--owner-of-charging-gauges-and-power-telemetry), [coprocessors](../reference/maps/coprocessors.md) **[DT][KC]**; firmware **?** |
| D5 | AOP | `aopfw-v68aop` (pitayaOS roottask: `SPUMotion8160v68`, ALS, prox, audio, voice trigger) | [`/arm-io/aop`](../reference/devicetree/root__arm-io__aop.md), [`iop-aop-nub`](../reference/devicetree/root__arm-io__aop__iop-aop-nub.md) (`firmware-name v68aop`) with `accel`/`gyro` and `accel_1`/`gyro_1` children, [`dcp-control`](../reference/devicetree/root__arm-io__aop__iop-aop-nub__dcp-control.md), [`/arm-io/aon-ptd`](../reference/devicetree/root__arm-io__aon-ptd.md) | `AppleSPUFirmwareService-AOP`, SPU HID services (`Transport = SPU`), including the Crane (0xFF0C/0x1C) and Hinge Angle (0x20/0xE4) `IOHIDEventDriver` personalities. Hinge angle (two-IMU fusion) and HES closure state computed in AOP firmware; angle written to the PTD **[FW]** | [05 §2.2](05-sensors-touch-audio-haptics.md#22-aop-always-on-processor-the-sensor-hub), [05 §4.1–4.2](05-sensors-touch-audio-haptics.md#41-what-is-physically-sensed), [08 §5.1, §5.3, §6.1](08-foldable-system-and-chassis.md#61-firmware--kernel) **[DT][KC][FW]** |
| D6 | AOP2 | `aop2fw-v68aop2` (AFK, pitayaOS) | [`/arm-io/aop2`](../reference/devicetree/root__arm-io__aop2.md) (nub `no-firmware-service`) → `AFKFirmwareService`, `AppleAOP2SystemDriver` | IMU/motion relays from AOP, always-on networking. Not on the path to the first frame **[INF]** | [05 §2.3](05-sensors-touch-audio-haptics.md#23-aop2-the-second-always-on-processor) **[DT][KC][FW]** |
| D7 | DCP and DCPSEC | `t8160dcp` (one image for all three DCPs; `AppleDCP-1317.40.16`, RTKit cl4) | [`/arm-io/dcp`](../reference/devicetree/root__arm-io__dcp.md) + [`/arm-io/disp0`](../reference/devicetree/root__arm-io__disp0.md) (outer); [`/arm-io/dcpsec`](../reference/devicetree/root__arm-io__dcpsec.md) + [`/arm-io/dispsec`](../reference/devicetree/root__arm-io__dispsec.md) (inner); [`/arm-io/i2c3/mogul-display`](../reference/devicetree/root__arm-io__i2c3__mogul-display.md) (panel auth) | `AppleASCWrapV8` → `RTBuddy`; `AppleDCPExpert` waits for `mogul-auth-key = "auth-passed"`; `AppleCLCD2` / `IOMobileFramebufferAP` per pipe. Two framebuffers, `primary` 0 (outer) and 1 (inner). **Whether the kernel reloads DCP firmware or takes over the instance iBoot used for the logo is ?** | [03 §2, §2.1, §2.3](03-gpu-and-displays.md#2-display-controllers-three-dcps) **[DT][KC][FW]** |
| D8 | MTP, then touch ASICs | MTP: `V68_MtpFirmware` (RTKit, `SensingAlgsCodexV68`, loaded by iBoot). ASICs: `V68_Multitouch` (`cypher2_v68ps_*` / `_v68ss_*`, Cortex-M, **not** loaded by iBoot); Mando FlatPack for `nova` | [`/arm-io/mtp`](../reference/devicetree/root__arm-io__mtp.md); [`multi-touch`](../reference/devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) (`service-display` → `disp0`); [`multi-touch2`](../reference/devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) (→ `dispsec`) | `AppleHIDTransportDeviceMailbox` downloads and authenticates each panel's controller firmware over HCCKit/SPI 16 MHz (`Boot Timeout` 500 ms), merges personality `V68PS1` / `V68SS1` (or `non-auth`), then two `AppleMultitouchHIDService`s. Ordering inside this chain is **[INF]** | [05 §5.1–5.4](05-sensors-touch-audio-haptics.md#54-kernel-driver-chain-touch) **[DT][FW][KC][INF]** |
| D9 | GFX / GFX1 | `armfw_g19p` / `armfw1_g19p` (RTKit) | [`/arm-io/gfx-asc`](../reference/devicetree/root__arm-io__gfx-asc.md), [`/arm-io/gfx1-asc`](../reference/devicetree/root__arm-io__gfx1-asc.md), [`/arm-io/sgx`](../reference/devicetree/root__arm-io__sgx.md) → `AGXAcceleratorG19P` | GPU ready for Metal/QuartzCore | [03 §1.2–1.4](03-gpu-and-displays.md#12-gpu-firmware-co-processors-gfx-asc-and-gfx1-asc) **[DT][FW][KC]** |

### Phase E: userland up to SpringBoard

The chapters do not trace userland start-up itself: **launchd, the order in which daemons launch, the data-volume mount and the first-unlock path are not covered**. Only the daemons below, and what each one opens, are established.

| # | Who acts | Running | Hardware touched | Hands to next | Source |
|---|---|---|---|---|---|
| E1 | AP | launchd and the daemon order | — | **?** | not in the chapters |
| E2 | AP: backboardd | QuartzCore render server (`CA::WindowServer::IOMFBServer`), IOMobileFramebuffer.framework | Both framebuffers (`disp0`, `dispsec`; `dispext0` if connected) via `IOServiceMatching("IOMobileFramebuffer")` | One `CADisplay` per panel: `uniqueId` = `IOMFBUUID` = DT `framebuffer-identifier` ([`display0`](../reference/devicetree/root__product__display0.md) `1C896A2B-…` outer, [`display1`](../reference/devicetree/root__product__display1.md) `BF0DC480-…` inner); `DeviceSurfaceType` 1 (cover) / 2 (inner) read from MobileGestalt `DisplayExtendedProperties` | [10 §1.1–1.3](10-userland-display-fold-touch.md#11-chain), [03 §4.2](03-gpu-and-displays.md#42-userland-pieces) **[DSC][DT]**; 1/2 mapping from vphone-duo runtime |
| E3 | AP: backboardd | `BKSDisplayService` (traits), `BKHIDDirectTouchEventProcessor`, `BKIOHIDService`, `MultitouchHID.plugin` + SensingAlgs `BinaryFilters` | Both `AppleMultitouchHIDService`s | Each digitizer bound to its display (`BKIOHIDService.displayUUID`); host state pushed to the touch controller ("cover closed", "display off"). **The key `displayUUID` is filled from is not found** | [10 §1.5, §5](10-userland-display-fold-touch.md#5-touch-on-two-panels-userland-dsc), [08 §6.2](08-foldable-system-and-chassis.md#62-backboardd) **[DSC][INF]** |
| E4 | AP: CoreBrightness | `CBDisplayContaineriOS` per panel | Reads `IODeviceTree:/core-brightness`, `/backlight`, `/arm-io/aop/iop-aop-nub` | Brightness per DCP/DCPSEC framebuffer | [10 §1.4](10-userland-display-fold-touch.md#14-corebrightness-dsc) **[DSC]** |
| E5 | AP: locationd | CoreMotion `CLAngleNotifier`, `CLSPUAngleServiceControl` | Opens the hinge HID service (0xFF0C/0x21 and, on hardware, Hinge Angle 0x20/0xE4); AOP angle service | `cmAngle` and `cmMagicPose` to SpringBoard over XPC. On first boot after restore there is no cached `AngleRepairState.plist`, so it reconverges **[INF]** | [08 §6.3](08-foldable-system-and-chassis.md#63-locationd-and-coremotion-locationd-binarydsc), [10 §2](10-userland-display-fold-touch.md#2-the-hinge-angle-kernel-service--coremotion--consumers), [13 §3](13-lifecycle.md#3-activation-and-first-boot) **[DSC][INF]** |
| E6 | AP: SpringBoard | SpringBoard, SpringBoardFoundation, FrontBoard | — | `SBFDevicePoseProvider` created (runs on a `UIUpdateLink` heartbeat); `SBFDisplayProxy` for `.cover` and `.inner` (`coverIntegratedDisplayWithIdentifier:`, `innerIntegratedDisplayWithIdentifier:`) | [08 §6.4](08-foldable-system-and-chassis.md#64-springboardfoundation-sbfdeviceposeprovider-dsc), [10 §3](10-userland-display-fold-touch.md#3-springboard-pose--content-mode--displays-dsc) **[DSC]** |

### Phase F: which panel is live at boot

| # | Who acts | Running | Hardware touched | Hands to next | Source |
|---|---|---|---|---|---|
| F1 | AOP | `CMAngleEstimator`, `CMSPUHES`, `MedinaState` in `aopfw-v68aop` | IMU0/IMU1 (`accel`/`gyro`, `accel_1`/`gyro_1` under [`iop-aop-nub`](../reference/devicetree/root__arm-io__aop__iop-aop-nub.md)); Hall sensor `crane_hes` (**no DT node; location unknown**) | Angle (FIR-filtered), HES closed/not closed, Medina fold state | [05 §4.1](05-sensors-touch-audio-haptics.md#41-what-is-physically-sensed), [08 §5.1, §5.3](08-foldable-system-and-chassis.md#53-closed-detection-the-hall-effect-sensor-hes-crane-fwkc) **[FW]** |
| F2 | AOP → AP kernel | AppleSPU → `IOHIDEventDriver` | SPU HID transport | `IOHIDEvent` type 0x2C (angle, mechanicalAngle, velocity, state). backboardd drops it ("destinations for Unknown event"); locationd consumes it | [05 §4.2](05-sensors-touch-audio-haptics.md#42-kernel-from-spu-report-to-iohidevent), [08 §6.2](08-foldable-system-and-chassis.md#62-backboardd) **[KC][DSC]**; runtime from vphone-duo |
| F3 | AP: SpringBoard | `SBFDevicePoseProvider` | — | `devicePose` with hinge region (`fullyClosed` … `openFlat`). Its `internal` struct has `isInitialized` and `hingeRegionsAreDefault`, and it keeps defaults `SBFDevicePoseLastKnownCMAngle` / `…CMMagicPose`. **Whether the boot pose is seeded from those defaults before the first live angle arrives is ? / [INF]** | [08 §6.4](08-foldable-system-and-chassis.md#64-springboardfoundation-sbfdeviceposeprovider-dsc), [05 §4.3](05-sensors-touch-audio-haptics.md#43-userland) **[DSC][INF]** |
| F4 | AP: SpringBoard | `SBFDisplayContentModeResolver` (+ `SBDisplayContentModeCoordinator`) | — | **Folded:** `SBFFullyClosedDisplay…` policy → `.cover` primary. **Open:** `SBFFoldingDualDisplay…` → `.inner` primary, `.cover` gets `.passiveShield` (vphone-duo log `keeping .cover inactive for .passiveShield`). `ForceCoverDisplayOnly` can pin the cover | [03 §4.1–4.2](03-gpu-and-displays.md#41-the-chain), [10 §3](10-userland-display-fold-touch.md#3-springboard-pose--content-mode--displays-dsc) **[DSC]** |
| F5 | DCP / DCPSEC | `t8160dcp` (`IOMFBHinge`, `read_hinge_angle_from_ptd`, `AppleClamshellState`) | [`aon-ptd`](../reference/devicetree/root__arm-io__aon-ptd.md); AOP [`dcp-control`](../reference/devicetree/root__arm-io__aop__iop-aop-nub__dcp-control.md) | The DCP gets the hinge angle and a clamshell state for angle-dependent correction and for powering the hidden panel down **[INF]**. Whether this happens before or independently of SpringBoard's decision at boot is **?** | [03 §4.3](03-gpu-and-displays.md#43-the-dcps-own-use-of-the-hinge-angle-fw), [08 §6.1](08-foldable-system-and-chassis.md#61-firmware--kernel) **[FW][KC][INF]** |

### Phase G: the first home-screen frame

The chapters trace a frame to photons only for an app on the inner panel ([03 §7](03-gpu-and-displays.md#7-end-to-end-a-metal-frame-to-photons-on-the-inner-panel)). The home screen uses the same chain with SpringBoard as the client **[INF]**; the folded case swaps DCPSEC/`dispsec` for DCP/`disp0`.

| # | Who acts | Running | Hardware touched | Hands to next | Source |
|---|---|---|---|---|---|
| G1 | AP: SpringBoard / FrontBoard | Home-screen scene on the primary `CADisplay` (`FBSDisplayConfiguration.hardwareIdentifier` = panel UUID); D76 cover layout via `SBSCurrentCoverDisplaySize` when folded | — | Layer tree for the live display | [08 §6.6](08-foldable-system-and-chassis.md#66-frontboard-uikit-and-the-app-dsc), [10 §1.6, §3](10-userland-display-fold-touch.md#16-frontboard-dsc) **[DSC][INF]** |
| G2 | GPU via GFX / GFX1 | AGX driver, `armfw_g19p` kicks VDM/PDM/CDM | [`/arm-io/sgx`](../reference/devicetree/root__arm-io__sgx.md), [`gfx-asc`](../reference/devicetree/root__arm-io__gfx-asc.md) | Rendered surfaces in DRAM. That the home screen is GPU-rendered is **[INF]** | [03 §7 steps 2–5](03-gpu-and-displays.md#7-end-to-end-a-metal-frame-to-photons-on-the-inner-panel) **[KC][FW][INF]** |
| G3 | AP: backboardd | CA render server; `IOMobileFramebufferSwapBegin/SetLayer/SwapEnd` | Framebuffer `primary` 0 (folded) or 1 (open) | Swap to the kernel `AppleCLCD2` / `IOMobileFramebufferAP` → `DCPLink` EPIC → DCP (mailbox 9) or DCPSEC (mailbox 11) | [03 §7 steps 6–7](03-gpu-and-displays.md#7-end-to-end-a-metal-frame-to-photons-on-the-inner-panel), [03 §2](03-gpu-and-displays.md#2-display-controllers-three-dcps) **[DSC][KC][DT]** |
| G4 | DCP (folded) or DCPSEC (open) | `t8160dcp` (VRR, brightness/EDR, hinge RDLC, subpixel compensation) | **Folded:** [`disp0`](../reference/devicetree/root__arm-io__disp0.md) (460 ppi, rotation 0). **Open:** [`dispsec`](../reference/devicetree/root__arm-io__dispsec.md) (430 ppi, canvas 2007×2853 scaled to 1878×2670, rotation 270) | Pixels to the panel's TCON over the panel link; "on glass" signal back. **First home-screen frame** | [03 §7 steps 8–11](03-gpu-and-displays.md#7-end-to-end-a-metal-frame-to-photons-on-the-inner-panel), [03 §3.1](03-gpu-and-displays.md#31-what-the-device-tree-says-about-each) **[FW][DT][INF]** |
| G5 | Other panel | `.passiveShield` / blanked (`CAWindowServerDisplay setBlanked:`) | the other pipe | Hidden panel dark or showing auxiliary content **[INF]** | [10 §1.3](10-userland-display-fold-touch.md#13-quartzcore-the-render-server-in-backboardd-dsc), [03 §4.2](03-gpu-and-displays.md#42-userland-pieces) **[DSC][INF]** |

### Phase H: the first tap reaches an app

The home screen belongs to SpringBoard, so the first tap on it is delivered to SpringBoard's UIKit (an app in the UIKit sense). A tap on an app icon then launches an app, and the next tap reaches that app through the same path. The launch itself (FrontBoard creating the app's scene) is not traced in the chapters → **?**.

| # | Who acts | Running | Hardware touched | Hands to next | Source |
|---|---|---|---|---|---|
| H1 | Touch ASIC of the live panel | `cypher2_v68ps_*` (outer, `PS`, LocationId 544) or `cypher2_v68ss_*` (inner, `SS`, LocationId 545), 120 Hz scan | [`multi-touch`](../reference/devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) or [`multi-touch2`](../reference/devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) | Frame over SPI 16 MHz, HCCKit, report 234 "touch" | [05 §9.1 steps 1–2](05-sensors-touch-audio-haptics.md#91-a-finger-tap-on-the-inner-panel--uitouch) **[FW][DT]** |
| H2 | MTP | `V68_MtpFirmware` (SensingAlgsCodexV68) | [`/arm-io/mtp`](../reference/devicetree/root__arm-io__mtp.md), DART `mapper-mtp` | Contacts as a mailbox message on `MTPEndpoint1`. MTP/host split of the algorithms is **[INF]** | [05 §9.1 step 3](05-sensors-touch-audio-haptics.md#91-a-finger-tap-on-the-inner-panel--uitouch) **[FW][DSC][INF]** |
| H3 | AP kernel | `AppleHIDTransportDeviceMailbox` → `AppleMultitouchHIDService` | — | Digitizer `IOHIDEvent` | [05 §9.1 step 4](05-sensors-touch-audio-haptics.md#91-a-finger-tap-on-the-inner-panel--uitouch) **[KC]** |
| H4 | AP: backboardd | `BKHIDDirectTouchEventProcessor`, SensingAlgs filters | — | Event routed to the display named by the service, hit-tested to a client context. Touches on an inactive (passive-shield) display can be dropped; `SBHingeMotionUnintendedInteractionMonitor` suppresses touches while the hinge moves | [05 §9.1 step 5](05-sensors-touch-audio-haptics.md#91-a-finger-tap-on-the-inner-panel--uitouch), [10 §3, §5](10-userland-display-fold-touch.md#5-touch-on-two-panels-userland-dsc) **[DSC][INF]** |
| H5 | AP: the target process | UIKit: `UIApplication sendEvent` → `UIWindow` → `UIView` | — | `UITouch` phase `began`; on the inner panel, coordinates rotated for `display-rotation 270` (**where the rotation happens is [INF]**) | [05 §9.1 step 6](05-sensors-touch-audio-haptics.md#91-a-finger-tap-on-the-inner-panel--uitouch) **[DT][INF]** |

---

## 3. Which co-processors are running by the time SpringBoard draws

"Running" means the chapters show the processor's driver chain in use for something on the boot-to-first-frame path, or show it must be up for a step in §2. A `?` means the image is loaded on every boot but nothing establishes whether the core is executing at first-frame time; power-gating on demand is plausible for several of these but is not shown.

| Co-processor | Node | Firmware | Loaded by | Running at first SpringBoard frame? | Why / evidence |
|---|---|---|---|---|---|
| PMU "becketts" (+ "fairmont") | [`pmu-main`](../reference/devicetree/root__arm-io__nub-spmi0__pmu-main.md) | `ApplePMUFirmware-743.40.11` inside iBoot | iBoot can update it **[FW]**; resident **[INF]** | **Yes** | Powers the SoC since A2 **[DT][INF]** |
| SEP | [`/arm-io/sep`](../reference/devicetree/root__arm-io__sep.md) | `sep-firmware.v68` + `sep-patches` | iBoot hands over; `AppleSEPManager` boots SEP OS | **Yes** | Keybag path, AMFI/Image4 security services matched in D2 **[KC][FW]** |
| PMP | [`/arm-io/pmp`](../reference/devicetree/root__arm-io__pmp.md) | `t8160pmp` | iBoot (`IsLoadedByiBoot`) | **Yes** **[INF]** | PMGR has a direct line to it (`function-pmp_control`); DVFS/bandwidth loops for DCS/SOC/DISP **[DT][KC]** |
| PMC | (inside `pmgr`; `pmc = 1`) | `t8160pmcfw` | iBoot | **Yes** **[INF]** | Arbitrates voter/boost/BWR/LTR; PMP sends "PMC Keep Alive" **[FW][DT]** |
| ANS2 (ASP) | [`/arm-io/ans`](../reference/devicetree/root__arm-io__ans.md) | `ansf.t8160` | **?** (not by iBoot on a normal boot) | **Yes** | SpringBoard and its assets are read from APFS on NVMe **[KC][INF]** |
| SMC | [`/arm-io/smc`](../reference/devicetree/root__arm-io__smc.md) | `t8160smc` (image not found) | **?** | **Yes** **[INF]** | Owns charger, gauges and button events (`smc-pmu`); `no-shutdown = 1` **[DT][KC]** |
| AOP | [`/arm-io/aop`](../reference/devicetree/root__arm-io__aop.md) | `aopfw-v68aop` | iBoot | **Yes** | Hinge angle and HES feed the pose that picks the panel (F1–F4) **[FW][KC][DSC]** |
| DCP (outer) | [`/arm-io/dcp`](../reference/devicetree/root__arm-io__dcp.md) | `t8160dcp` | iBoot-EAN image; kernel-time loader **?** | **Yes when folded**; open: driving the passive-shield/blanked state **[INF]** | Owns `disp0` **[DT][KC]** |
| DCPSEC (inner) | [`/arm-io/dcpsec`](../reference/devicetree/root__arm-io__dcpsec.md) | `t8160dcp` | as DCP | **Yes when open**; folded: **?** (powered down for the hidden panel **[INF]**) | Owns `dispsec` **[DT][KC]** |
| GFX / GFX1 | [`gfx-asc`](../reference/devicetree/root__arm-io__gfx-asc.md), [`gfx1-asc`](../reference/devicetree/root__arm-io__gfx1-asc.md) | `armfw_g19p`, `armfw1_g19p` | iBoot | **Yes** **[INF]** | CA composites and SpringBoard renders on the GPU (G2) |
| MTP | [`/arm-io/mtp`](../reference/devicetree/root__arm-io__mtp.md) | `V68_MtpFirmware` | iBoot | **Yes** **[INF]** | Needed for the first tap; touch firmware download and auth happen in kernel bring-up (D8). Whether it finishes before the first frame is **?** |
| Touch ASICs `cypher2` PS / SS | `multi-touch`, `multi-touch2` | `V68_Multitouch` | Kernel (`AppleHIDTransport`), not iBoot | **?** | Both have firmware; whether the hidden panel's controller is scanning is not shown ("cover closed", "display off" host state, [10 §5](10-userland-display-fold-touch.md#5-touch-on-two-panels-userland-dsc)) |
| AOP2 | [`/arm-io/aop2`](../reference/devicetree/root__arm-io__aop2.md) | `aop2fw-v68aop2` | iBoot | **?** | Not on the first-frame path |
| SIO | [`/arm-io/sio`](../reference/devicetree/root__arm-io__sio.md) | `SmartIOFirmware_ASCv8` | iBoot | **?** | Not on the first-frame path in the chapters |
| ISP, Secure M3 | [`/arm-io/ispRtb`](../reference/devicetree/root__arm-io__ispRtb.md) | `adc-boreas-v68`, `securem3fw-v68` | iBoot | **?** | Camera path only |
| ANE0 / ANE1 | [`ane0`](../reference/devicetree/root__arm-io__ane0.md), [`ane1`](../reference/devicetree/root__arm-io__ane1.md) | `h19_ane{0,1}_fw_perses_v6x` | iBoot | **?** | Not on the first-frame path |
| DCPEXT | [`/arm-io/dcpext0`](../reference/devicetree/root__arm-io__dcpext0.md) | `t8160dcp` | as DCP | **?** (only with a USB-C display) | [03 §5](03-gpu-and-displays.md#5-external-display-usb-c-displayport) |
| Exclave world (cL4) on the AP | — | `exclavecore_bundle.v68` | iBoot | **Yes** (entered by XNU in C3) | Display, AOP and SEP all have exclave routes **[DT][FW][KC]** |

---

## 4. Gaps

- **Button to power-up.** Which PMU wake source the side button raises from off, what carries the press while the SoC is off, and the rail and reset sequence are not in the sources. The `/buttons` → `smc-pmu` path is only shown for the running OS.
- **Which panel shows the Apple logo**, and whether iBoot reads the fold state at all, are unknown. So is whether the kernel restarts the DCP from FUD or takes over iBoot's running instance.
- **Who starts the IOPs.** iBoot loads most IOP images, but whether it starts the cores or only stages the images for `AppleASCWrapV8`/`RTBuddy` is not stated. The ANS firmware's normal-boot loader and the SMC firmware's source are both unknown.
- **Kernel order.** IOKit matching order between SEP, ANS, AOP, DCP, MTP and GPU is not established; Phase D is grouped, not sequenced.
- **Userland start-up** (launchd, daemon order, data-volume mount, first-unlock and keybag handling before SpringBoard) is not covered by any chapter.
- **Boot pose.** Whether SpringBoard's first pose comes from a live AOP angle or the `SBFDevicePoseLastKnown*` defaults, and how long hinge convergence takes on a cold boot, are not shown.
- **Boot chime.** Which stage plays `Ap,AudioBootChime` was not found.
- **Timing.** No step has a measured time; the trace is ordered, not timed.
- **Verification.** None of this was observed on a running Duo. The vphone-duo runtime results the chapters cite come from a VM.

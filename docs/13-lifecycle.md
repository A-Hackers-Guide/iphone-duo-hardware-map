# 13: Lifecycle: the Duo as software sees it, from factory to erase

This chapter follows one iPhone Duo (`iPhone19,4`, `V68AP`, `t8160`, iOS 27.2 `24B91020`) through its life:

1. the factory,
2. the first restore,
3. activation,
4. daily updates,
5. repair,
6. recovery,
7. the final erase.

For each stage it names the hardware involved, the software that acts on it, and the evidence. The labels are defined in [00-method-and-evidence.md](00-method-and-evidence.md).

Chapter 02 covers the boot chain, Image4, `/chosen` and the OS environments. This chapter reuses that material and does not repeat it. Most of the new evidence here comes from two places:

- **The restore daemon of the erase-install ramdisk**, `restored_external`. The repo's [`reference/ramdisk/`](../reference/ramdisk/README.md) documents only the *upgrade* ramdisk.
- **The FDR sealing maps** in `System/Library/FDR/`.

---

## Contents

0. [Sources for this chapter](#0-sources-for-this-chapter)
1. [Factory](#1-factory)
2. [First restore and personalization](#2-first-restore-and-personalization)
3. [Activation and first boot](#3-activation-and-first-boot)
4. [Daily life: OTA, cryptexes, firmware outside the OS](#4-daily-life-ota-cryptexes-firmware-outside-the-os)
5. [Repair](#5-repair)
6. [Recovery and DFU](#6-recovery-and-dfu)
7. [End of life: erase-all](#7-end-of-life-erase-all)
8. [Summary table](#8-summary-table)
9. [Gaps](#9-gaps)

---

## 0. Sources for this chapter

| Source | What it gives | Label |
|---|---|---|
| `BuildManifest.plist` → [`reference/manifest.md`](../reference/manifest.md) | The three build identities and every signed component | **[FW]** |
| **Erase** ramdisk `141-28940-105.dmg` | Extracted for this chapter with `ipsw img4 im4p extract` and mounted read-only. `/usr/local/bin/restored_external` (13,365 strings ≥ 6 chars) holds the restore step names | **[FW]** |
| **Upgrade** ramdisk `141-29011-104.dmg` → [`reference/ramdisk/`](../reference/ramdisk/README.md) | `restored_update`, the updater dylibs, libFDR, the FDR plists, the astris flashers | **[FW]** |
| [`reference/devicetree/`](../reference/devicetree/README.md), [`data/devicetree.txt`](../data/devicetree.txt) | `syscfg/…` property references, `/chosen`, `/arm-io/secure-repair`, `/osenvironments` | **[DT]** |
| [`reference/kexts/`](../reference/kexts/README.md) | `AppleSecureRepair`, `AppleEffaceableStorage` | **[KC]** |
| Chapters 02, 08, 12 | locationd `AngleRepairState` (strings from a vphone-duo guest; locationd is not in the shared cache), MobileKeyBag xART strings | **[DSC]** for MobileKeyBag (cited from those chapters, since the shared cache was not re-extracted) |
| Apple support pages, iFixit coverage, repair-manual coverage | Repair process, parts history, teardown | **[PUB]** with URL |

**Ramdisks: what differs.** The erase and upgrade ramdisks have almost the same file list. One difference is the restore daemon:

- The erase ramdisk has `restored_external` and `com.apple.restored_external.plist`.
- The upgrade ramdisk has `restored_update` and `com.apple.restored_update.plist`.

The other differences in the file lists are a few AppleInternal and accessory frameworks (for example `AppleRestoreUtils` and parts of `CoreAccessories`), which only the upgrade ramdisk carries. Both ramdisks carry the same 13 updater dylibs in `/usr/lib/updaters/` **[FW]**.

`restored_external` runs as a launchd job with `RunAtLoad`, logging to `/dev/console` **[FW]**.

**On step order.** Step names are read in their `__cstring` order. That order usually follows the order of the step tables in the source. Many firmware steps also have an `await_*` twin, so they run in parallel. Where this chapter gives an order, it is **[FW]** for the names and **[INF]** for the strict sequence.

---

## 1. Factory

### 1.1 Hardware involved

Every part that carries an identity or calibration:

- both panels and their cover glass,
- the three display ALS,
- both IMU sets (`accel`/`gyro`/`compass`/`hgaccel` and their `_1` twins),
- the cameras with their authentication chips (`YonkersIR1`, `YonkersIR2`, and the rear camera auth IC),
- Mesa (Touch ID),
- the Mando/Tritium sensor,
- both battery packs,
- the PMU follower,
- the Ace3 USB-C controller,
- the Secure Element and NFC,
- C2 (baseband), N1 ("Proxima"), Rose ("Arrow"),
- the Lynx chip.

### 1.2 syscfg: the factory's write-once record

iBoot parses **syscfg v3**, which has per-entry HMACs and an optional manifest. Chapter 02 §1 and §17 cover this **[FW]**.

The device tree does not hold calibration values. Instead, it holds **pointers** of the form `syscfg/<key>[/len,fallback]`. iBoot resolves these at boot. The template IPSW sometimes carries a hex fallback after the comma. Every syscfg reference in the Duo's tree is listed below **[DT]** ([`data/devicetree.txt`](../data/devicetree.txt)):

| Group | Keys (node) |
|---|---|
| Identity | `SrNm` serial, `MLB#`, `Mod#`, `CFG#`, `MdlC`, `Regn`, `RMd#`, `Coor` (country of origin), `RSKU` (`/baseband` region SKU), `SwBh`/`MkBS`/`MkBH`/`SBVr` (software and marketing behaviour) |
| Materials and colours | `CLHS`, `CLBG`, `CLCG`, `EnMt`, `CGMt`, `BGMt` |
| Radios | `WMac`, `BMac`, `EMac`, `EMc2`, `TMac` (`/fillmore`, Thread), `WSKU` and `RFEM` (`/centauri` antenna SKU / RF front end) |
| **IMU, half 1** (`accel`, `gyro`, `hgaccel`) | `AICl`, `AROC`, `ARXC`, `ARNC`, `ARXN`, `ARSC`, `ASCl`, `ARot`, `LTAO`; `GICl`, `GRXC`, `GRNC`, `GRXN`, `GRSC`, `GSCl`, `GRot`, `GYTT`; `AhXN` |
| **IMU, half 2** (`accel_1`, `gyro_1`, `hgaccel_1`) | `A2CL`, `A2oC`, `A2XC`, `A2NC` (+ shared `ARXN`, `ARSC`, `ASCl`, `ARot`, `LTAO`); `G2CL`, `G2XC`, `G2NC`, `G2TT` (+ shared `GRXN`, `GRSC`, `GSCl`, `GRot`); `AhXN` |
| Compass ×2 | `CPAS`, `CSCM`, **`CSCa`** (`compass-sens-calibration-closed`), `CRot` (two orientations, including `compass-orientation-p2`), `JRot` (`compass_1`), `MDCC`, `CDCC`, `CMOC`, `CVCC` |
| Other AOP sensors | `PxCl` (prox), `PRTT`/`SPPO` (pressure) |
| Touch / Mando | `NvTh`, `NvFc` (`/arm-io/mtp/…/nova`) |
| Display | `DTCl` (`/product display-temp-compensation`), `DPCl`, `DBCl` |
| Camera | `STRB`, `RACa`/`RACm` (photon detector), `BCAR` (back-camera AF recal), `PrCL`/`RxCL` (Pearl residue; see chapter 02 §19) |
| Audio and haptics | `SpGH`, `SpPH`, `MiGH`, `MiGT`, `CLCL`, `PSCl` (`halle-calibration = "syscfg/PSCl,syscfg-mismatch/PSCl"`), `TCal` |
| Repair | `RCHL` (`/chosen repair-history`), `rpcp` (`/chosen repair-status`) |

Some of these properties sit outside the node the table names. For example, `DPCl` (`primary-calibration-matrix`) and `DBCl` (`display-backlight-compensation`) are properties of `/product` itself, not of a display node. The table groups keys by function.

**Duo-specific reading.**

- **Each half's IMU has its own interrupt and range calibration**: `AICl`/`A2CL`, `GICl`/`G2CL`, `ARNC`/`A2NC`, and so on.
- **Some keys are shared by both halves**: `ARot`, `GRot` and the nominal-extrinsic `ARXN`/`GRXN`.
- **The compass has a separate "closed" sensitivity calibration**, `CSCa`.
- **There is no hinge-angle calibration key.** No syscfg key names a hinge, an angle or the relative pose of the two halves **[DT]**.

**[INF, strong]** The hinge angle's calibration is **not a factory constant**. It is learned at runtime by the AOP estimator and cached by locationd in `AngleRepairState.plist` ([§5.4](#54-calibration-after-repair)). That fits the per-half extrinsic keys feeding a runtime solver.

### 1.3 FDR: factory data, sealed by Apple's server

**Factory Data Restore (FDR)** is how factory data survives an erase. The calibration blobs and component identities are uploaded to Apple, sealed, and recovered at every restore.

- `BuildManifest` Info `FDRSupport = True` **[FW]**.
- **`libFDR.dylib`** (1.35 MB) is the client. Its `AMFDRSealingMap*` and `AMFDRSealedData*` APIs have two back ends **[FW]**:
  - a local data store, `/mnt1/System/Library/Caches/com.apple.factorydata`;
  - a remote one (`amfdrRemote`, `AMFDRDataHTTPSign`, `…HTTPMultiSign`), with the strings "Remote FDR Data sealing successful" and "verification success against test station signature".
- `libFDRDecode.dylib` decodes FDR blobs, and `/System/Library/FDR/fdrtrustobject` is the trust root **[FW]**. `libFDR` checks it with the strings "Remote trust object digest still doesn't match apTicket" and "Skipping trust root check (trustobject unset)".
- **The sealing map** `/System/Library/FDR/FDRSealingMap.plist` maps each product type to an entry list. **`iPhone19,4` → 57 data-class entries** **[FW]**. The table below lists every class in the Duo's map.

| Tag(s) | Identifier | Attributes (abridged) | Hardware |
|---|---|---|---|
| `bbcl`, `bbpv`, `bbpc`, `scrt` | `BasebandUniqueId` | `bbpv` DeviceOnlySigning + GeneratedByRestore; `scrt` ServerOnlySigning | C2 modem |
| `vcrt` ×2 | `BatterySerialNumberPack0` / `Pack1` + `BatteryIDSNPack0/1` | RequiredToSeal | **Two battery packs** |
| `appv`, `pcrt`, `SCfT`, `PEid`, `ecrt`, `scrt`, `seal` | `UniqueDeviceID` | GeneratedByRestore; `seal` is ManifestVersion2, DeprecateGIDSigning | AP / device |
| `ycrt`, `prpc` | `YonkersIR1` / `YonkersIR2` ChipID + UID | GeneratedByRestore | Camera-module auth chips (inner and outer front) |
| `prpc` | `RearCameraAuthIC` ChipID + UID | GeneratedByRestore | Rear camera auth chip |
| `CmCl`, `CmPM` (→ `DPCd`, `DPCm`, `CALm`) | `RearFacingCameraModuleSerialNumber`, `BackSuperWideCameraSerialNumber` | RequiredToSeal | Rear cameras and their calibration |
| `iCCl` (→ `FCCl`) | `InternalFrontCameraModuleSerialNumber` | RequiredToSeal | **Inner (under-display) camera** |
| `FSC2` (→ `FSCl`, `hop0`), `MSRk` | `MesaSensorIDSensorSN` | `MSRk` ServerOnlySigning | Touch ID sensor (Mesa) |
| `AlsB` ×2 (→ `HmCn`) | `AmbientLightSensorTBSensorFlexSerialNumber`, `…MDMLBSerialNumber` | RequiredToSeal | Two ALS on flexes or MLB |
| `HmCl`, `IfCl`, `AlsH` ×3 sets | Cover glass + one of three ALS | One set RequiredToSeal (primary cover glass + `MDSensorFlex` ALS); two sets **NonPoR** (secondary cover glass) | **Display ALS calibration, three combinations** |
| `tcrt` ×2 | `ScreenSerialNumber18d` + `MogulIDSNTopModule`, and **`…Secondary`** | GeneratedByRestore | **Two panels**, each with a Mogul ID chip |
| `DspB` ×2 (secondary → `HmD2`, `HmD3`) | `CoverglassSerialNumber`, `CoverGlassSerialNumberSecondary` | RequiredToSeal | Per-panel display calibration |
| `dCfg`, `3Dp2` | Primary / secondary cover glass | EarlyAccess, EarlyAccessConsistencyRequired | Display config, readable before the OS |
| `3Bg3` | `BackglassMagnetometerSerialNumber` | EarlyAccess | Back-glass magnetometer |
| `mCfg`, `TBCl` (→ `MdTh`, `NvFc`) | `TritiumMandoUID` | EarlyAccess | Mando / Camera Control sensor |
| `xCfg` | `PMUFollowerSerialNumber` | EarlyAccess | **Second PMU** |
| `eCfg`, `fCfg` | `UniqueDeviceID` | EarlyAccess | Device config |
| `mcrt` | `MogulIDSNAce3` | GeneratedByRestore | Ace3 USB-C controller ID chip |
| `lcrt` | `LynxSerialNumber` | MultiSealing | Lynx **[INF: an authentication or identity chip; role not shown]** |
| `rMC2` (→ `rMUB`, `rMNB`), `rSCl`, `rcrt`, `UwbB` (→ `rSyA`, `rSyB`) | `ArrowChipID` + `ArrowUniqueChipID` | `rcrt` GeneratedByRestore | Rose UWB ("Arrow") |
| `scrt`, `BWC3` (→ `WFCS`, `BTCS`, `W2CS`) | `ProximaChipID` + `ProximaECID` | `scrt` ServerOnlySigning | N1 Wi-Fi/BT calibration |
| `sePk` | `SecureElementID` | GeneratedByRestore | Secure Element key |
| `NfcB` (→ `ShSA`, `ShSB`), `ShSC` | `NFCUniqueChipID` + `UniqueDeviceID` | `ShSC` NonPoR | NFC ("Stockholm") calibration |

The attribute names explain the lifecycle directly:

- **`GeneratedByRestore`**: the restore creates the class, for example a fresh certificate.
- **`RequiredToSeal`**: sealing fails without it.
- **`ServerOnlySigning`** vs **`DeviceOnlySigning`**: who signs it.
- **`EarlyAccess`**: readable early in boot.
- **`NonPoR`**: not part of the proof of record **[INF from name]**.
- **`StoreCombined`**, **`MultiSealing`**: storage and sealing variants.

**[INF]** The `*crt` tags (`tcrt`, `ycrt`, `vcrt`, `mcrt`, `rcrt`, `lcrt`, `pcrt`, `ecrt`, `scrt`) are per-component certificates, issued per device and per part.

**Comparison with the iPhone 18 Pro (`iPhone19,2`)** **[FW]**:

- The 18 Pro's sealing map has 47 entries, against the Duo's 57.
- Its repair configuration has **one** `tcrt`, **one** battery class and **no** `xCfg` (PMU follower).
- Of every product in `FDRSealingMap.plist`, only `iPhone19,4` has these classes (checked by searching all entries):
  - two `tcrt` (`ScreenSerialNumber18dSecondary`),
  - two `vcrt` (`Pack0`, `Pack1`),
  - `iCCl` `InternalFrontCameraModuleSerialNumber`,
  - `xCfg` `PMUFollowerSerialNumber`.

  These are the foldable's extra parts, expressed as factory data.

### 1.4 Astris and SWD flashing

The ramdisk carries **Astris "booster pack" SWD flashers**: `arm_adi`, `arm_cypress_ccg2`, `arm_nrf`, `arm_nxp`, `arm_stm32` and `arm_stm32l15xc` (bundle IDs `com.apple.coreos.astris.*-swdflasher`) **[FW]**. Astris is Apple's debug-probe stack, and SWD is Arm Serial Wire Debug.

- `libAppleHIDSWDFlash.dylib` (6,806 strings: `dpr`/`dpw`/`apr`/`apw` debug-port primitives, `armcpu-r/w`) flashes a microcontroller over SWD tunnelled through a HID device **[FW]**.
- `libMantaMCUUpdater` has the same `armcpu`/`apr` primitives **[FW]**.
- `restored_external` has the option `IgnoreSWDFailures` **[FW]**.

**[INF]** On the factory line, Astris drives these flashers over a probe. On a customer restore, the same code paths flash small accessory MCUs (for example a USB-C or Cypress CCG2 controller) through an on-board bridge. Which chips on the Duo, if any, are SWD-flashed is not shown. None of the vendor names maps to a Duo device-tree node.

### 1.5 Component pairing at the factory

Pairing means binding a part's own identity to this logic board. Three mechanisms are visible:

1. **FDR certificates.** Each paired part gets a `*crt` class in the sealing map ([§1.3](#13-fdr-factory-data-sealed-by-apples-server)). The class is generated at restore and sealed against the part's ChipID/UID or serial **[FW]**.
2. **Auth-chip provisioning.** `YonkersUtil` reads, per sensor, `ChipID`, `UID`, `ECPubKey`, `ProvPubKey`, `*Hmac`, `MNS`, `certData` and `provCertData` from `AppleH10/H13/H16CamIn` **[FW]**. `SavageUtil` is its sibling.
3. **Touch ID.** The SEP pairs the Mesa module (chapter 02 §13; `_invalidModuleSerialNumber` **[KC]**). FDR records it as `FSC2`/`MSRk` **[FW]**.

**[PUB]** Apple's repair tooling ("System Configuration") "transfers factory calibration values" for displays, cameras and ALS, and links biometric parts to the Secure Enclave:

- <https://support.apple.com/ar-bh/125146>
- <https://www.ithinkdiff.com/iphone-duo-repair-manual/>

---

## 2. First restore and personalization

### 2.1 Identities and what is signed

| Identity | RestoreBehavior | Ramdisk | Restore daemon | Components |
|---|---|---|---|---|
| Customer Erase Install (IPSW) | `Erase` | `141-28940-105.dmg` | `restored_external` | 172 |
| Customer Upgrade Install (IPSW) | `Update` | `141-29011-104.dmg` | `restored_update` | 172 |
| Recovery Customer Install | `Erase` | `141-28940-105.dmg` (same as erase) | `restored_external` | 79 |

All **[FW]**. Identities 0 and 1 differ in **only two** component rows: `RestoreRamDisk` and `RestoreTrustCache`. Every firmware digest is identical. The `Info` dicts differ only in `RestoreBehavior` and `Variant`.

### 2.2 TSS and the IM4M

The host (Finder or Apple Configurator) collects device identity from iBoot or the ramdisk and requests an **IM4M (APTicket)** from Apple's TSS. The request covers:

- ECID, `ApChipID 0x8160`, `ApBoardID 0x0E`, `ApSecurityDomain 0x01`,
- the AP nonce (`RequiresNonceSlot = True`),
- the SEP nonce,
- the digest of every component in the identity.

The manifest side is **[FW]**. The host flow is **[PUB]**, from the [Apple Platform Security guide](https://support.apple.com/guide/security/welcome/web), "Secure software updates".

The restore daemon handles nonces and attestation **[FW]**:

- `ramrod_load_ap_nonce_slot_from_data`, `ramrod_load_sep_nonce_slot_from_data`,
- `GenerateNonces`, `AppleMobileApNonce`, "AP nonce consumed", `ramrod_clear_ap_nonce`,
- `ramrod_kill_sep_nonce` (`seputil --kill-nonce`),
- `attest_restore` and "Failed to attest DFU boot".

`RestoreAttestationMode = 8` **[FW]**.

**Co-processors get their own tickets.** Each has a manifest namespace with its own ChipID: `Cellular1` (16416), `Wireless1` (8230), `Rap` (8228), `SE` (0x91), `eUICC` (32), `BMU`/`BMU2` (58629), `YonkersIR1/2` (2325/2326) **[FW]**. For each one, the updater dylib builds a **per-chip TSS request** from that chip's nonce and identity. The host then sends it. Examples:

- `libT200Updater`: `@BMU,Ticket`, `BMU,BoardID`, `BMU,CertificateEpoch`.
- `libPS190Updater`: `PS190BootNonceHash`.
- `libAppleTconUARPUpdater`: `UARPMetaDataPersonalizationChipID/Epoch/FdrRootCaDigest`.

All **[FW]**. Two `restored_external` strings show that some tickets are made on the device rather than the host: `Device Side RestoreInfo not enabled for this updater, will do RestoreInfo on host` and `ramrod_update_needs_ap_receipt` **[FW]**.

### 2.3 The restore, step by step

`restored_external` runs one checkpoint engine (`ramrod_checkpoint.c`). Its named steps are listed below in string order **[FW]**. Steps that touch hardware are in bold.

1. **Setup.** `client_protocol_version`, `copy_restore_options`, `usbcretimer_dfucheck_enforce`, `is_host_compatible`, `set_device_time`, `update_ticket`.
2. **Storage.** `wait_for_storage`, **`update_NAND_firmware`**, `clear_remap_variable`, `asp_nand_set_writable`, `find_filesystem_partitions`, `verify_storage_for_update`.
3. **SEP.** **`load_sep_os`**, `preload_keys_for_fsck`, `fsck_filesystems`, `mount_system_partition`.
4. **Preserve.** `read_previous_os_build_version`, `downgrade_check`, `copy_hardware_info`, **`fdr_create`**, **`fdr_save_data`**, `store_baseband_migration`, `read_persistent_files`.
5. **Wipe.** `clean_nand`, **`format_effaceable_storage`**, **`format_ean_storage`**, `create_filesystem_partitions`.
6. **Main OS prepare.** `update_partitions_for_apfs`, `delete_recovery_partition`, `format_media`, `prepare_for_system_image`, `baseband_migration_data`, `init_gigalocker`, `init_permanent_update_volume`, `mount_filesystem`, `write_persistent_files`.
7. **Lay down the OS.** `restore_system_image` (ASR), then `install_kernel_cache`, `install_device_tree`, `install_root_hash`, `write_ticket`.
8. **Restore installing.**
   - `fdr_restore_saved_data`, then **`update_device_firmware_pre_fdr`**.
   - `fdr_prepare`, `clear_fips_data_file`, `fdr_recover`, `fdr_auto_challenge_claim`.
   - **`update_device_firmware`**.
   - `verify_fdr_data`, then **`update_firmware_post_sealing`**, then `fdr_verify_sealed_manifest`.
   - **`commit_sep_os`**, `create_protected_filesystems`, `create_production_dcrt`, `reserve_overprov_space`.
   - **`install_splat`**, `attest_restore`, `set_one_time_boot_command`, `set_nvram_variables`, `persistent_boot_args`, `set_tdm`, `populate_preboot_volume`.
9. **recoveryOS.** `recovery_os_restore`: `create_recovery_container` … `write_recovery_os_ticket`, `write_recovery_firmware`, `get_recovery_iboot_files`.
10. **Finish.** `set_boot_command`, `seal_system_volume`, `create_system_snapshot`, `prepare_data_split`, `convert_eds_volumes`, `split_data_volume`, `commit_temporary_checkpoint`, `write_os_info_for_nerd`, `set_autoboot_delay`, `unmount_filesystems`.

**The FDR bracket around firmware updates is the key structural fact.** Firmware runs in three places relative to FDR:

- **Before FDR is recovered**: `update_device_firmware_pre_fdr`.
- **After recovery but before sealing**: `update_device_firmware`.
- **After sealing**: `update_firmware_post_sealing`.

**[INF]** Parts whose certificates are `GeneratedByRestore` in the sealing map (Yonkers, the panels' `tcrt`, Rose `rcrt`, the SE `sePk`) must be updated or provisioned before `fdr_verify_sealed_manifest`. Their post-seal steps (`update_savage_postseal`, `update_rose_postseal`) then finish the provisioning.

### 2.4 Chip by chip: order, updater and evidence

The firmware stage names, in `restored_external` order **[FW]**, are:

- **Pre-FDR:** `update_aht`.
- **Main stage:** `update_veridian`, `update_manta_mcu`, `update_iBoot`, `update_ean`, `install_fud`, `update_stockholm`, `update_baseband_legacy`, `update_baseband`, `update_rose`, `update_se`, `update_vinyl`, `update_ir_mcu`, `update_tcon`, `update_appletcon`, `update_orion`, `update_madea`, `update_peppy`, `update_nitrogen`, `update_centauri`, `update_canary`, `update_savage`, `update_ace3`, `update_usbcretimer`, `update_appletconnuarp`, `update_banyan`.
- **Async waits:** `await_update_*` for tcon, appletcon, orion, peppy, nitrogen, usbc, manta_mcu, stockholm, baseband, rose, se, vinyl and veridian.
- **Post-seal:** `update_savage_postseal`, `decompress_pearl_data`, `update_rose_postseal`, `stage_fdr_ean`, `ensure_fdr_ean`, `update_fdr_ean`, `update_fillmore`, `baseband_postseal`.

One ordering is stated outright: `firmware_update_se: Waiting for Rose To Finish` **[FW]**.

The table maps each Duo chip to its stage and updater. A chip appears only if the Duo's manifest, device tree or sealing map shows it is present.

| # (string order) | Chip on the Duo | Restore step | Software that acts | Image source | Evidence |
|---|---|---|---|---|---|
| 0 | **NVMe / ANS storage controller** | `update_NAND_firmware` (setup) | `/usr/bin/nvmefwupdater` (`AppleEmbeddedNVMeController`, `/usr/standalone/firmware/{BFH,M9,S4E,Turks}/…loader.bin`, `storagetunables/`). Messages such as "Update NAND - FTL version mismatch. Erase install required" | Ramdisk standalone firmware (not in manifest); `ANS`/`RestoreANS` are the ANS co-processor firmware | **[FW]** |
| 0 | **SEP** | `load_sep_os`, then `commit_sep_os` | `seputil`; `ramrod_load_sep_os`, `ramrod_commit_sep_hash_with_options`; `update_sep` | `RestoreSEP`/`SEP` (`sepi`), `SepStage1` | **[FW]** |
| 1 | **AP boot chain in NVMe/EAN** | `update_iBoot`, `update_ean`, `install_fud` | `restored_external` built-in: `MSUBootFirmwareUpdater`, `NVMEiBootUpdater` (`_copyIBICFromPath`), `ASPStorageiBootUpdater` | `LLB`/`iBoot`; EAN images `AppleLogo`, `RecoveryMode`, `Liquid`, `DCP`, `Ap,LowPowerMode`, `WCHFirmwareUpdater`; FUD (`IsFUDFirmware`) to Preboot | **[FW]** |
| 2 | **BMU and BMU2 gas gauges** (two packs) | `update_veridian` (`com.apple.restored.veridian`) | `libT200Updater.dylib` (Veridian; `BatFWUpdater`, `NumEnabledBMU`/`NumSupportedBMU from IODT`, `PackIndex`, `AppleGasGaugeUpdate`, `/usr/standalone/firmware/Veridian/FirmwareMap.plist`) | `BMU,FirmwareMap`/`DigestMap`, `BMU2,*` | **[FW]**; `/product bmu-num-supported = 3` **[DT]** |
| 3 | **NFC controller (Stockholm, SN450)** | `update_stockholm` | `libnfrestore.dylib` with `/usr/standalone/firmware/nfrestore/` (`fw-hashes/SN450V-hashes.plist`, `rf/SN450V_FW_A1_01_01_00A…`) | Ramdisk standalone firmware | **[FW]**; `sn450WithLoadSwitch` **[DT]** |
| 4 | **C2 baseband** | `update_baseband` (`com.apple.restored.basebandupdaters`) | `libBBUpdaterDynamic.dylib` (`BasebandUpdater`, `perform_manifest_check_baseband`); post-seal `baseband_postseal`, `ramrod_baseband_verify_sealed_manifest` | `Cellular1,*` (10 components) | **[FW]** |
| 5 | **Rose UWB** | `update_rose` (`com.apple.restored.roseupdater`) and `update_rose_postseal` | `libRoseUpdater.dylib`, `libRoseBooter.dylib`, `RoseControllerLib.plugin`. Option `IgnoreRoseFailures` | `Rap,RTKitOS`, `Rap,RTKitIOConfig`, `Rap,SoftwareBinaryDsp1` | **[FW]** |
| 6 | **Secure Element** | `update_se` (waits for Rose) | `libSEUpdater.dylib`, `libAppleSSE.dylib`; option `SkipJCOP` | `SE,UpdatePayload` (Stockholm91.sefw); `SE,RapRTKitOS`/`SE,RapSwBinDsp` | **[FW]** |
| 7 | **eUICC** | `update_vinyl` | `libVinylUpdater.dylib` ("Vinyl updaterSupported missing or returned not supported"); `libVinylNonUpdater.dylib` | `eUICC,Gold`, `eUICC,Main` (`vinyl_20.vnlfw`) | **[FW]** |
| 8 | **Camera auth chips YonkersIR1/IR2** | `update_savage` and `update_savage_postseal` | `libSavageUpdater_iOS.dylib` + `libSavageRestoreInfo_iOS.dylib` (`YonkersIRxIsPresent[%d]`, `/usr/standalone/firmware/Yonkers/YonkersPatch*.DER`, "Loading PSPC from FDR", `FDRDataEncryptionKey`, "Auth challenge received from libFDR"); `YonkersUtil` | `YonkersIR1,SysTopPatch0..F`, `YonkersIR2,SysTopPatch0..F` | **[FW]** |
| 9 | **N1 Wi-Fi/BT ("Centauri"/"Proxima")** | `update_centauri` | `libCentauriUpdater.dylib` (`ramrod_device_has_centauri`) | `Wireless1,*` (38 components) | **[FW]**; `/centauri` **[DT]** |
| 10 | **Ace3 USB-C controller (HPM)** | `update_ace3` / `update_usbc` | `libAce3Updater.dylib` (`Ace3UpdateController`, `AppleHPMDeviceHALType3`, "HPM in ADFU in OTA Stage 1/2", "boot-nonce found to be all 0s, blocking SFWi"). Also `TiSerialFlasher` with `USB-C_HPM,*.bin` | Ramdisk standalone (`USB-C_HPM,<n>.bin`), not in manifest | **[FW]**; FDR `mcrt MogulIDSNAce3` **[FW]** |
| 11 | **Thread radio ("Fillmore")** | `update_fillmore` (post-seal) | `restored_external` (`hw.features.fillmore`, `FillmoreBypassOTDataPersist`) | — | **[FW]**; `/fillmore` **[DT]** |
| — | **Multitouch (both panels), Mando, Leap haptics, AOP/AOP2, DCP, ISP, GPU, ANE, PMP, SIO, Secure M3** | `install_fud` only | Nothing is flashed. These are RAM-loaded firmware that iBoot or the kernel load on every boot from Preboot/FUD | `Multitouch`, `MtpFirmware`, `Ap,MandoFW`, `LeapHaptics`, `AOP*`, … | **[FW]** flags `IsLoadedByiBoot`/`IsFUDFirmware` |
| — | **Display TCON, DP retimer, PS190, Manta MCU, Banyan, Orion, Peppy, Nitrogen, Canary, Madea** | Steps exist but should skip | `libAppleTCONUpdater` (`AppleTCONDP835Device`), `libAppleTconUARPUpdater`, `libAppleTypeCRetimerUpdater`, `libPS190Updater`, `libMantaMCUUpdater` | **No manifest component** for any of them on V68 | **[FW]** absence; **[INF]** shared ramdisk code for other products |

Two caveats on the last two rows:

- **Display TCON.** No TCON component is signed for V68, and the device tree has no TCON node. The FDR map still seals `tcrt` against `ScreenSerialNumber18d` + `MogulIDSNTopModule` for both panels. **[INF]** Panel identity on the Duo is checked through the Mogul ID chip and DCP, not through a field-updatable TCON.
- **`canary`.** The device tree has 4 `canary` hits. Chapter 01 places them under SoC and storage, so `update_canary` may target something else. That is not resolved here.

**Failure handling** **[FW]**:

- "Updater (Stage 1) failed, but this is bestEffort - returning success".
- Two-stage updaters: `UpdaterIsTwoStageSupported`, "%s Updater configured for two-stage update. DeferredCommit: %s".
- "%s Updater: Forcing Repersonalization due to restore option".

---

## 3. Activation and first boot

| Step | Hardware | Software | Evidence |
|---|---|---|---|
| Boot into the new OS | AP, SEP | `set_boot_command`, `set_autoboot_delay`. Then the boot chain of chapter 02 §1. iBoot reads syscfg, so the `syscfg/…` device-tree pointers are filled from the real calibration | **[FW]** **[DT]** |
| Device certificates | SEP, AP | `create_production_dcrt` / `CreateFactoryDcrt`: "DCRT public key does not match DAK public key", "Failed to attest RK to %@", "Failed to attest UIK to SIK". **[INF]** A device certificate (DCRT) bound to the SEP's Device Attestation Key, issued at restore | **[FW]** |
| Activation record | AP storage | `/private/var/hardware/MobileActivation` sits on the **Hardware** volume (role 320, `/private/var/hardware`), which restore preserves: "Successfully persisted hardware folder contents" | **[FW]** **[DT]** fstab |
| Activation Lock / server activation | Baseband, Wi-Fi | `mobileactivationd` and Apple's activation server **[PUB]** ([Platform Security guide](https://support.apple.com/guide/security/welcome/web), "Activation Lock"). The daemon is on the root filesystem, which was not extracted | **[PUB]** |
| Keybag creation | SEP, xART | `create_system_key_bag`, `create_protected_filesystems`, `/private/xarts`. MobileKeyBag `KeybagxART` (chapter 12) | **[FW]** **[DSC]** |
| Cellular | eUICC, C2 | Profile download through CommCenter / CellularPlanManager (chapter 02 §16) | **[DSC]** **[INF]** |
| Calibration go-live | AOP, DCP, ISP | AOP reads the IMU, compass and prox keys. DCP reads `DTCl`/`DBCl`/`DPCl`. The camera exclave checks FDR (`ExclaveFDRDecodeTrustEvaluationService`, chapter 02 §17) | **[DT]** **[FW]** |
| Hinge first convergence | Both IMUs, Hall sensor | **[INF]** locationd `CLSPUAngleServiceControl` starts with no cached `AngleRepairState.plist` and reconverges, just as after a repair. It reports `timeToAngleConvergence` | **[DSC]** (chapter 08 §5.5) **[INF]** |

---

## 4. Daily life: OTA, cryptexes, firmware outside the OS

### 4.1 OTA vs restore

- **The IPSW's Upgrade identity** is a *tethered* update. The firmware set is the same as erase, run by `restored_update`. Its upgrade-specific strings include:
  - "Data volume access is restricted and this is a upgrade install. Jump to end of checkpoint",
  - "No active FDR bank found. Will stage.", "Wrote staged FDR EAN key",
  - "No System partition to delete during Update Install",
  - `PreserveCryptexCacheOnUpgrade`.

  **[FW]**
- **Over-the-air updates** do not use this IPSW. They use a separate OTA payload that MobileSoftwareUpdate stages into the **Update** volume (`/private/var/MobileSoftwareUpdate`, role 192 **[DT]**). The device then reboots into the same `restored_update` ramdisk path.
  - **[PUB]** The [Platform Security guide](https://support.apple.com/guide/security/welcome/web), "Secure software updates", covers this.
  - **[FW]** supporting strings: `MSUBootFirmwareUpdater`, `MASoftwareUpdate copyDCRTWithError:`, `Update partition is mounted`, `submit_update_stats`, "HPM in ADFU in OTA Stage 1/2".
- **Erase vs upgrade:**

| | Erase | Upgrade |
|---|---|---|
| Data volume | Formatted (`format_media`, `format_effaceable_storage`, `format_ean_storage`) | Kept; may be split or migrated (`split_data_volume`, `convert_eds_volumes`) |
| FDR | Recovered from Apple (`fdr_recover`) | Staged locally (`stage_fdr_ean`) |
| Device firmware | Full `update_device_firmware` | Same updaters, but `SkipSameVersion` / `ramrod_skip_same_version` skip unchanged chips |
| Ramdisk | 141-28940-105 | 141-29011-104 |

All **[FW]**.

### 4.2 Cryptexes and Rapid Security Responses

- **Cryptex1 components** are `Cryptex1,SystemOS`/`SystemTrustCache`/`SystemVolume` (141-28400-098) and `Cryptex1,AppOS`/… (141-28395-106, the Safari/web cryptex) **[FW]**.
- **The device-tree crypto suite** is `cryptex1-certificate-format "x509"` and `cryptex1-key-scheme "rsa4096"` **[DT]**.
- **The kernel's chip environments** are `CHIP_CRYPTEX1_BOOT_AP`, `…GENERIC_AP`, `…MOBILE_ASSET_*` **[KC]**.
- **RSR / "splat."** `restored_external` has `install_splat`, "prerolling splat nonce", "rolling splat nonce", `ramrod_splat_enabled` and `ramrod_splat_local_policy_supported` **[FW]**.
  - **[INF]** "splat" is Apple's internal name for the Rapid Security Response cryptex layer.
  - A restore installs it with its own nonce. That nonce is rolled so a revoked response cannot be replayed.
  - RSRs patch the Cryptex1 SystemOS / AppOS and do not touch device firmware.

### 4.3 Firmware that updates outside a restore

| Chip | How it updates in normal life | Evidence |
|---|---|---|
| AOP/AOP2, DCP, ISP, GPU, ANE, PMP, SIO, Multitouch, Mando, haptics, Secure M3 | Nothing is flashed. A new OS ships new FUD images, and these are RAM-loaded every boot | **[FW]** flags |
| AirPods, Pencil, MagSafe and other accessories | UARP (`libAppleTconUARPUpdater` shows the UARP framework). Accessory updates run from the OS, not the restore | **[FW]** **[INF]** |
| Battery gauges BMU/BMU2 | Only through restore or OTA (`update_veridian`); `/usr/standalone/firmware/Veridian` | **[FW]** **[INF]** |
| PMU | iBoot can update it: `ApplePMUFirmware-743.40.11~956.release` | **[FW]** iBoot (chapter 02 §1) |
| C2 baseband, N1, Rose, SE, eUICC, NFC, USB-C HPM | Only during restore or OTA, through the updaters in §2.4 | **[FW]** |

---

## 5. Repair

### 5.1 Hardware hooks

- **`/arm-io/secure-repair`** **[DT]**:
  - `compatible "secure-repair,1"`, `#gpio-pins 95`, 7 GPIO interrupt groups (AIC 456–462).
  - `gpio-repair_en = <0x5a 0x101 "AOP">`. **[INF]** That reads as GPIO pin 90 on the AOP controller. Its `reg 0x90824000` is the AOP GPIO window.
- **`AppleSecureRepair`** (`com.apple.driver.AppleSecureRepair`) **[KC]**:
  - It has a user client.
  - Its methods are `assertRepair` and `getRepairState`.
  - The entitlement `com.apple.private.AppleSecureRepair.allow` gates it.
  - It has `no-resume-restore`.

  **[INF]** A privileged repair tool asserts a hardware "repair enable" line, and the kernel exposes its state.
- **`/chosen repair-history = "syscfg/RCHL"`** and **`repair-status = "syscfg/rpcp"`** **[DT]**. The `repair-environment` OS environment sets `repair-environment = 1` (chapter 02 §18) **[DT]**.

### 5.2 What a repair changes in software

- **FDR repair configuration.** `FDRSealingMapRepairConfiguration.plist` maps **`iPhone19,4` → ASID `f770f02d…`, with 10 repairable assemblies** and 2 exceptions **[FW]**.

| Assembly key (`RepairConfigurationAsidMetadata`) | Data classes that move with it |
|---|---|
| `tcrt` [`ScreenSerialNumber18dSecondary`, `MogulIDSNTopModuleSecondary`] (**inner/secondary panel**) | `3Dp2`, `DspB` (secondary cover glass) |
| `tcrt` [`ScreenSerialNumber18d`, `MogulIDSNTopModule`] (**primary panel**) | `AlsH`, `dCfg`, `DspB`, `IfCl`, `HmCl` (with the `MDSensorFlex` ALS) |
| `3Bg3` `BackglassMagnetometerSerialNumber` | — |
| `TBCl` `TritiumMandoUID` | `mCfg` |
| `prpc` `YonkersIR2` | `ycrt`, `iCCl` `InternalFrontCameraModuleSerialNumber` |
| `prpc` `YonkersIR1` | `ycrt` |
| `xCfg` `PMUFollowerSerialNumber` | `AlsB` (`MDMLB` ALS) |
| `MSRk` `MesaSensorIDSensorSN` | `FSC2` |
| `prpc` `RearCameraAuthIC` | `CmPM` (super-wide), `CmCl` |
| `AlsB` `AmbientLightSensorTBSensorFlexSerialNumber` | — |
| **Exceptions** (`RepairConfigurationAsidExceptionList`) | `vcrt` **Battery Pack0** and **Battery Pack1** |

  Reading the table:
  - **Batteries are the exception.** Their certificates are excluded from repair-configuration matching. **[INF]** A battery swap re-seals the `vcrt` class but does not need a full assembly match. That fits Apple's separate "Battery" parts-history entry **[PUB]** <https://support.apple.com/en-ch/102658>.
  - **[INF]** The `xCfg` → `AlsB (MDMLB)` grouping suggests the PMU follower and one ALS sit on the same replaceable board in one half.
- **libFDR on the repair path** **[FW]**:
  - `AMFDRSealingMapCreateRepairConfigurationAsidMetadataInternalBlob`,
  - `AMFDRSealingMapCopyRepairConfigurationComponentTypeForClassAndInstance`,
  - `AMFDRSealingMapAutoChallengeClaim`,
  - "Remote verification pass and unsealed data is allowed. Skip Auto Challenge Claim by Server".

  **[INF]** After a part swap, the next restore or System Configuration session claims the new part's data classes on Apple's server (`fdr_auto_challenge_claim`) and re-seals. The relevant restore options are `FDRClaimAllData`, `FDRClaimDataForRecover`, `FDRRevertData` and `FDRSkipSealing`.
- **Parts and Service History.** iOS shows each part as Genuine / Used / Unknown, and "only the most recent service for a given part is shown" **[PUB]**:
  - <https://support.apple.com/en-ch/102658>
  - <https://macmyths.com/how-to-see-parts-and-service-history-on-iphone-ios-26/> (secondary)

  **[INF]** That status is computed from `RCHL`/`rpcp` and the FDR verification result.

### 5.3 Repair manual and Self Service Repair

**[PUB]** Apple published the Duo repair manual (ID **FPZKLK**) on 23 October 2026 ([ithinkdiff](https://www.ithinkdiff.com/iphone-duo-repair-manual/), [newsbytes](https://www.newsbytesapp.com/news/science/apple-releases-diy-repair-guides-for-iphone-duo/story)).

- **Contents:** 22 procedures, including:
  - cover layer, outer display, inner display / inner display assembly, back glass;
  - rear, FaceTime and outer-front cameras;
  - **Battery 1 and Battery 2**;
  - logic board, I/O board, USB-C;
  - both speakers, microphone, Taptic Engine, enclosure;
  - **Touch ID/camera control buttons**;
  - a "Hinge Issues" troubleshooting page.
- **System Configuration** is "required at the end of every logic board repair". It transfers factory calibration and links biometric parts to the Secure Enclave.
- **Parts:** at publication, parts were not yet in the Self Service Repair Store.

**[INF]** The manual's parts list matches the FDR assemblies one to one:

| Manual part | FDR assembly |
|---|---|
| Outer and inner display | Two `tcrt` |
| Two batteries | Two `vcrt` |
| Touch ID button | `MSRk` |
| Camera control | `TBCl` Tritium/Mando |
| Rear / front / inner cameras | `prpc` RearCameraAuthIC / YonkersIR1 / YonkersIR2 |

### 5.4 Calibration after repair

| Calibration | Where it lives | After a repair | Evidence |
|---|---|---|---|
| **Hinge angle** (relative pose of the two IMUs) | Runtime: AOP estimator, cached by locationd in `AngleRepairState.plist` (`rotation`, `relativeGyroBias`, `offsetAngle`, `accelBias`, `temperature`) | **Discarded**. `repairStateForComponentsAffectingIMUExtrinsics()`, `BootAfterRepair`, `hasBeenRepaired`; then it reconverges | **[DSC]** (chapter 08 §5.5) |
| IMU per-half (`AICl`/`A2CL`, `GICl`/`G2CL`, `ARot`/`GRot`, …) | syscfg | **[INF]** Moves with the logic board; no FDR class covers it. Board-only replacement needs System Configuration to transfer it | **[DT]** **[INF]** |
| Compass (`CPAS`, `CSCM`, `CSCa` closed) | syscfg; FDR `3Bg3` for the back-glass magnetometer | Back-glass magnetometer data re-seals with its assembly | **[DT]** **[FW]** |
| Display (per panel) | FDR `DspB` (+ `HmD2`/`HmD3` on the secondary), `dCfg`/`3Dp2`; syscfg `DTCl`/`DBCl` | Moves with the panel's `tcrt` assembly | **[FW]** **[DT]** |
| ALS ×3 | FDR `AlsB`, `AlsH`, `IfCl`, `HmCl` (each tied to a cover glass + ALS pair) | Moves with the panel or flex that holds it | **[FW]** |
| Cameras | FDR `CmCl`/`CmPM` (→ `DPCd`, `CALm`), `iCCl`/`FCCl`; syscfg `BCAR` | Moves with the module; auth chip re-certified (`ycrt`/`prpc`) | **[FW]** **[DT]** |
| Touch ID | FDR `FSC2` (→ `FSCl`, `hop0`), `MSRk` (ServerOnlySigning) | Re-paired to the SEP by System Configuration | **[FW]** **[PUB]** |
| Mando / Camera Control | FDR `TBCl` (→ `MdTh`, `NvFc`), `mCfg`; syscfg `NvTh`/`NvFc` | Moves with the module | **[FW]** **[DT]** |
| Wi-Fi/BT, UWB, NFC RF | FDR `BWC3`, `UwbB`, `NfcB` | Tied to the chip on the logic board | **[FW]** |

### 5.5 iFixit's view

**[PUB]** Chapter 08 §2 has the full summary and URLs.

- **Score:** provisional **5/10**, the best iFixit score for a foldable.
- **Batteries:** two cells with electrically released adhesive.
- **Board:** a single-layer logic board.
- **Inner screen:** the hardest repair (glue in 21 pockets). US$999 out of warranty.
- **Cracks:** iFixit's hinge-stress hypothesis for inner-screen cracks.

Sources:

- <https://www.iphoneincanada.ca/2026/10/26/ifixit-iphone-duo-teardown-repairability-score/>
- <https://winbuzzer.com/2026/10/27/iphone-duo-teardown-finds-easier-battery-swaps-xcxwbn/>
- <https://www.techradar.com/phones/iphone/ifixit-tears-down-the-iphone-duo-and-awards-it-the-highest-repair-score-yet-for-a-foldable-but-replacing-the-inner-screen-and-hinge-takes-a-lot-of-work>

**[INF]** Software makes the hinge repair costlier than the hardware alone. Replacing any part that holds an IMU invalidates the hinge calibration (§5.4). Replacing the inner panel re-seals two FDR assemblies' worth of data: secondary `tcrt` plus `DspB`/`3Dp2`. iFixit's general position on parts pairing (<https://www.ifixit.com/News/66879/iphone-14-parts-pairing-results-apple-is-still-trying-to-monopolise-repair>) applies to every `*crt` class above.

---

## 6. Recovery and DFU

| Mode | Entered by | What runs | Evidence |
|---|---|---|---|
| **DFU** | SecureROM, when no valid LLB is found or on a button combo | SecureROM loads `iBSS` over USB. iBoot strings show "Apple Mobile Device (DFU Mode)" | **[FW]** **[PUB]** |
| **Recovery (iBoot)** | `auto-boot=false`, `recovery-boot-mode`, a failed boot | `iBEC` (identical payload to LLB/iBoot/iBSS, `mBoot-20457.52.7`; iBEC IM4P `iocv = 2`). Shows the `RecoveryMode` EAN image | **[FW]** **[DT]** `single-stage-boot` |
| **Restore** | iBEC loads the ramdisk | `RestoreRamDisk` + `RestoreKernelCache`/`RestoreDeviceTree`/`RestoreSEP`/`Ap,Restore*` (types `rkrn`, `rdtr`, `rsep`, `rspt`, `rtrx`, `rxcl`, `rsm3`, `ran1`, `rdcp`) | **[FW]** |
| **recoveryOS** | `recover-system`, `recover-once`, `recover-fallback` (restored strings) | The **Recovery Customer Install** identity: 79 components; OS `141-28683-104.dmg.aea`; erase ramdisk; `iBSS`, `iBEC`, `AOP*`, `GFX`, `ISP`, `PMP`, `SIO`, `RestoreANS`, `RestoreDCP`, `Ap,Restore*`, **all `Cellular1,*` and `Wireless1,*`** | **[FW]** |
| **NeRD** (network recovery) | `AllowNeRDBoot` in the recovery identity; `write_os_info_for_nerd` | recoveryOS on its own APFS container (`create_recovery_container`, `write_recovery_os_ticket`, `restore_and_invert_recovery_os`). Option `RetainRecoveryOS` | **[FW]** |

**What recoveryOS cannot reach** **[FW]** **[DT]**:

- The recovery identity has **no `SEP`, `LLB`, `iBoot`, `Ap,cL4`** and no SE, eUICC, BMU, Rose, Yonkers or Multitouch firmware.
- `recovery-environment` sets `sepfw-load-at-boot = 0`, `protected-data-access = 0` and `disable-accessory-firmware`.

**[INF]** recoveryOS has radios, because NeRD needs Wi-Fi or cellular to fetch an OS. It has the display and touch path. It has no access to user data and does not touch any paired part. That is consistent with Apple's description of recoveryOS **[PUB]** ([Platform Security guide](https://support.apple.com/guide/security/welcome/web)).

---

## 7. End of life: erase-all

### 7.1 What is destroyed

| Target | Mechanism | Evidence |
|---|---|---|
| **Class keys / Data volume** | Keybags are **xART-based** on this device (`/defaults no-effaceable-storage`). Destroying the xART-held keybag secret makes the Data volume unreadable. Strings: "Failed to open EANService to wipe xART keys", `ramrod_notify_sep_for_erase`, `AppleVirtualPlatformXART FORCE_RELOAD` | **[DT]** **[FW]**; MobileKeyBag `KeybagxART`, `aks_delete_xart_leak` **[DSC]** (chapter 12) |
| Effaceable storage | `format_effaceable_storage` runs, but "Device does not support effaceable storage. Skipping effaceable format." applies here (`no-effaceable-storage`). `EraseEFS` option | **[FW]** **[DT]** **[INF]** that the skip branch runs on the Duo |
| EAN area | `format_ean_storage`, `SkipEANClean` | **[FW]** |
| NAND | `clean_nand`, `format_media` | **[FW]** |
| SEP state | `ramrod_kill_sep_nonce`, `commit_sep_os`; xART anti-replay counters (SEP endpoints `xarm`/`xars`/`artr`/`arts`, chapter 02 §12) | **[FW]** **[KC]** |
| Nonces | `ramrod_clear_ap_nonce` ("Device does not support clearing of AP nonce" is a fallback) | **[FW]** |

Two paths lead here:

- **On device**, "Erase All Content and Settings" goes through the OS's obliteration path. That binary is not in either ramdisk, so it is out of reach **[PUB]** **[INF]**.
- **A host erase-restore** runs exactly the steps above **[FW]**.

**[PUB]** The Platform Security guide describes erase as destroying the keys, not overwriting the data.

### 7.2 What survives an erase

| Survives | Why | Evidence |
|---|---|---|
| **syscfg** (serial, MACs, all calibration, `RCHL` repair history, `rpcp`) | Not on the APFS container. iBoot reads it from `nvme_syscfg` | **[FW]** iBoot; **[DT]** |
| **FDR sealed data** | Saved before the wipe (`fdr_create`, `fdr_save_data`), recovered from Apple after (`fdr_recover`); local cache `/FactoryData/System/Library/Caches/com.apple.factorydata` | **[FW]** |
| **Hardware volume** (`/private/var/hardware`, incl. `MobileActivation`) | `write_persistent_files` / "Committed %lu persistent files to NAND" | **[FW]** |
| **Baseband data** | `store_baseband_migration`, `baseband_migration_data` | **[FW]** |
| **Battery data** | "%d battery data files were unable to be preserved". **[INF]** Cycle and health data for both packs is preserved | **[FW]** |
| **recoveryOS** | `RetainRecoveryOS` | **[FW]** |
| **Activation Lock** | Server-side. Survives any erase while Find My is on | **[PUB]** |
| **Paired-part identity and co-processor firmware** | On the parts themselves (SE applets aside), and re-sealed rather than reset | **[FW]** **[INF]** |
| **eSIM profiles** | Kept or deleted by user choice in Erase All Content and Settings | **[PUB]** **[INF]** |

**Not surviving:** the Data volume and its keybags, the Update volume, xART entries, the cached hinge calibration (`AngleRepairState.plist` is user-side on `/private/var` **[INF]**), the Secure Element's payment applets (**[INF]**: wallet deprovisioning is separate) and the NVRAM boot-args (`persistent_boot_args`, `print_nvram_variables`).

---

## 8. Summary table

| Stage | Hardware | Software | Key evidence |
|---|---|---|---|
| Factory | All calibrated and paired parts | Factory station, Astris SWD flashers, syscfg writer, FDR upload | **[DT]** syscfg pointers; **[FW]** sealing map (57 classes), astris boosters |
| First restore | AP, SEP, NVMe, BMU×2, NFC, C2, Rose, SE, eUICC, Yonkers×2, N1, Ace3 | `restored_external` + `/usr/lib/updaters/*`, `nvmefwupdater`, `libBBUpdaterDynamic`, `libnfrestore`, `libFDR` | **[FW]** step strings, manifest |
| Activation | SEP, Hardware volume, radios | DCRT issuance, mobileactivationd, keybag creation | **[FW]** **[PUB]** |
| Daily | Everything RAM-loaded; flashed chips on OTA | MobileSoftwareUpdate → `restored_update`; Cryptex1 + splat | **[FW]** **[KC]** **[DT]** |
| Repair | Panels, batteries, cameras, Mesa, Mando, PMU follower, ALS | `AppleSecureRepair`, libFDR repair configuration, System Configuration, locationd | **[DT]** **[KC]** **[FW]** **[DSC]** **[PUB]** |
| Recovery | AP, radios, display | iBSS/iBEC, recoveryOS identity, NeRD | **[FW]** **[DT]** |
| Erase | SEP, xART, NAND | `restored_external` format steps, EANService xART wipe | **[FW]** **[DT]** **[DSC]** |

---

## 9. Gaps

- **Factory tooling is not in the IPSW.** The station software, the syscfg writer and the FDR upload client are absent. The factory stage is reconstructed from what restore *reads back* (the sealing map, syscfg pointers and the astris boosters). Which Duo chips, if any, are SWD-flashed is unknown.
- **Values are absent.** The IPSW device tree is a template, so no real calibration, `RCHL` or `rpcp` value is visible. The format of `RCHL` (the repair-history record) is not decoded.
- **Restore order is not proven.** Step order comes from `__cstring` order plus the `await_*` pairs. That is strong evidence of grouping, but not a trace. A real restore log (`restored_external` console output) would settle it.
- **Updaters were not disassembled.** Which ones actually run on V68 is inferred from manifest presence and device-tree nodes. The TCON, retimer, PS190, Manta, Banyan, Orion, Peppy, Nitrogen, Madea and Canary steps are assumed to skip on the Duo. `update_ir_mcu` and `update_aht` (`libAHTRestore`, `AHTLoader`) were not identified. The secondary NFC controller (`hammerfest`) has no updater identified.
- **`restored_external` is not in `reference/ramdisk/`.** The repo's ramdisk pages document the upgrade ramdisk only. The erase-ramdisk strings used here were extracted ad hoc and are not checked in.
- **The OTA payload is not examined.** Only the tethered Upgrade identity was. MobileSoftwareUpdate, `mobileactivationd`, the obliteration daemon and System Configuration's client run from the root filesystem or dyld cache, which were not available for this chapter.
- **Some FDR terms are undefined.** The exact meanings of `NonPoR`, `EarlyAccess`, `StoreCombined`, `Lynx` and most four-character data-class tags are inferred from names.
- **Hinge calibration after repair** rests on chapter 08's locationd strings. Whether Apple's repair flow also runs an explicit hinge or IMU calibration step (the manual's "Hinge Issues" page) is not documented in these sources.
- **Erase internals.** The xART wipe is shown by one restored string and MobileKeyBag strings. The SEP side is encrypted, so the key hierarchy that is destroyed is **[PUB]**/**[INF]** only.
- **Public sources are thin.** The Duo repair manual itself (FPZKLK) was not read directly, only press coverage of it.

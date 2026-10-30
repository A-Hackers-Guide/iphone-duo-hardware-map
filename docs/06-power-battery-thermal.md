# 06 — Power, batteries, charging and thermal

Device: iPhone Duo (iPhone19,4, board V68AP, SoC t8160 / A20 Pro), iOS 27.2 build 24B91020.

This chapter covers how power reaches the SoC and how the phone measures, budgets, charges and cools itself. That means the SPMI PMUs, the two battery packs and their gas gauges, the wired (USB-C PD) and wireless (MagSafe/Qi2) charge paths, the SMC, PMP and PMC co-processors, the pmgr rails/domains, CLPC, the peak-power manager (PPM/CPMS) and brownout handling, thermal sensors and throttling, and the userland that publishes a battery percentage.

Evidence labels: **[DT]** device tree (`Firmware/all_flash/DeviceTree.v68ap.im4p`, parsed from the raw payload, not the lossy text dump), **[KC]** kernelcache `kernelcache.release.v6x-pandia` (kext personalities + strings), **[FW]** firmware images in the IPSW, **[DSC]** iOS 27.2 dyld shared cache, **[PUB]** public source, **[INF]** my inference.

Raw evidence extracted for this chapter (raw-payload DT dumps, Volchok summary) is in [`data/06-power-battery-thermal/`](../data/06-power-battery-thermal/).

Related chapters: USB-C data/DisplayPort and the HPM port controller as a *data* device belong to the I/O chapter; AOP sensors are covered in [the sensors chapter](05-sensors-touch-audio-haptics.md); the fold/hinge pose service is in the prior research `iphone_duo_fold.md`. Here those blocks appear only where they carry power or thermal data.

---

## 0. One-screen summary

```mermaid
flowchart LR
  subgraph Sources
    USBC[USB-C receptacle<br/>/port-usb-c-1] 
    MS[MagSafe/Qi2 coil<br/>/port-magsafe-1]
  end
  USBC --> HPM[HPM port controller<br/>spmi-hpm0 'usbc,cbtl1702,spmi'<br/>nub-spmi2 SID 0xC]
  HPM -- PD contract / VBUS --> CHG
  MS --> WCH[Wireless-power controller<br/>fw WirelessPower.v68 'wchf'<br/>RTKit armv7em]
  WCH --> CHG
  CHG[Charger(s) — owned by SMC<br/>smc-charger / smc-ext-charger<br/>'ChargerCount', 'ChargerVBus0/1'] --> P1[Battery pack 1 + BMU<br/>Volchok BAT8193]
  CHG --> P2[Battery pack 2 + BMU2<br/>Volchok BAT8193]
  P1 <-. rebalance .-> P2
  P1 & P2 --> VDDMAIN[VDD_MAIN]
  VDDMAIN --> PMU1[PMU 'becketts'<br/>nub-spmi0 SID 0xE, primary]
  VDDMAIN --> PMU2[PMU 'fairmont'<br/>SID 0x1 via SGPIO bridge]
  PMU1 & PMU2 --> RAILS[SoC rails: DCS / SOC / DISP / AVE / CPU / GPU …]
  RAILS --> SOC[t8160 A20 Pro]
  SMC[SMC ASC 't8160smc'] --- CHG
  SMC --- PMU1
  PMP[PMP ASC 't8160pmp'] --- RAILS
  PPM[ApplePPMCPMSv2 + AppleBTM] --- SMC
  PPM --- PMP
  CLPC[AppleCLPC] --- PMP
```

Main findings:

1. **Two batteries, two gas-gauge controllers ("BMU"/"BMU2"), both personalized and updated from the same image set.** The BuildManifest has `BMU,BoardID = BMU2,BoardID = 33171 (0x8193)` and `BMU,ChipID = BMU2,ChipID = 58629 (0xE505)`. Both point to `Firmware/Volchok/BAT8193/{DigestMap.der,FirmwareMap.plist}` with identical digests **[FW]**. The DT says the same thing three ways: `btm` has `number-of-batteries = 2` and `number-of-PMUs = 2`, and `ppm` has `number-of-battery-packs = 2` **[DT]**.
2. **"Volchok" is the battery-management-unit (gas gauge) firmware family. BAT8193 is the pack product ID.** The FirmwareMap holds a 96 KiB Cortex-M firmware (version 209210031), a 24 KiB `su_crypto` image (secure-update/authentication), and 25 chemistry-specific `configuration` (8 KiB) plus `dnvd` (4 KiB) blobs, keyed by cell chemistry ID **[FW]**. The kernel drives it through the SMC with `AppleGasGaugeUpdate`, `AppleGasGaugeBeadsUpdate`, `AppleBatteryAuth` and `AppleBeadsBatteryAuth` **[KC]**.
3. **Cell balancing between the two packs is a first-class kernel feature.** `AppleSmartBatteryPack::updateRebalanceData` calls the PPM (`kPPMInterfaceAPIReq`, `kPPMTempInReq`, `kPPMDODInReq`, `kPPMChemIdReq`), gets back an impedance array (`kPPMOutImpdDataR0`) and writes it to SMC keys. The kernel publishes `RebalanceData`, `RebalanceHWBypassFETStatus`, `RebalanceInrushCurrentDebug`, `OPDDualChargerState`, `IPDRatio`, `ChargerVBus0/1`, `BatteryPackCount` and `ChargerCount` **[KC]**.
4. **There is no separate gas-gauge node on any I²C/SPMI bus in the DT.** The gauges sit behind the SMC (`smc-charger`, SMC key traffic). The only SPMI battery-adjacent nodes are `btm` (a function of the main PMU at SID 0xE) and the unbound `stonehenge` (SID 0xF on nub-spmi1). The kernel has an `AppleStonehengeBPIC` battery-protection-IC driver for `stonehenge` (VCELL/ICELL warn/err, boost-error interrupts), but this DT node has no `compatible`, so nothing binds by name **[DT][KC]**.
5. **The PMU firmware ships inside iBoot** (`ApplePMUFirmware-743.40.11~956.release` string in the decompressed iBoot) **[FW]**. The AppleLPM firmware (`Ap,LowPowerMode`, IM4P `alpm`) is an RTKit armv8 image that renders a display. iBoot passes it `alpm-24h-mode`, `alpm-dst-offset` and `alpm-language-direction`, and its strings include "Device Charging", "System shutdown to OFF" and "DCP workloop" **[FW]**. This is consistent with a clock/charging screen shown while iOS is not running **[INF]**.
6. **SMC firmware was not found as a separate image.** The DT names it (`iop-smc-nub/firmware-name = "t8160smc"`, `pre-loaded = 0`), but no BuildManifest component or IPSW file carries that name. See Gaps.
7. **The DT carries thermal tables for two SoC bins**, `:borneo_h19a_*` and `:borneo_h19p_*`. The h19p `temp-sensor` table lists 29 entries, 28 Ta/Te/Tp die sensors plus `MTR_TOP_AGX` (28 is the `sochot-sensors` count; corrected by [FACTCHECK](FACTCHECK.md)); the h19a table lists 22 **[DT]**. iBoot presumably keeps the one matching the fused part **[INF]**.

---

## 1. SPMI buses and every PMU-class node on them

The t8160 has five SPMI masters in this DT, all `compatible = "aapl,spmi"`, `gen = 4`, driven by `AppleSPMIController` (`com.apple.driver.AppleSPMI`) **[DT][KC]**. Each master is also an interrupt controller for its followers. Each has three MMIO windows **[DT]**:

| Master | MMIO (`reg`, 0x4000 each) | Followers (SPMI SID from `reg[0]`) |
|---|---|---|
| `/arm-io/nub-spmi0` | 0x88714000, 0x88704000, 0x88700000 | `pmu-main` (0xE), `pmu-secondary` (0x1, behind SGPIO bridge), `btm` (0xE, same SID as pmu-main) |
| `/arm-io/nub-spmi1` | 0x88614000, 0x88604000, 0x88600000 | `shamisen` (0xC), `stonehenge` (0xF) |
| `/arm-io/nub-spmi2` | 0x88914000, 0x88904000, 0x88900000 | `spmi-hpm0` (0xC) |
| `/arm-io/aop-spmi0` | 0x90914000, 0x90904000, 0x90900000 | `wlan-heb` (0xE), `baseband-heb` (0xD), `stockholm-spmi` (0x8, NFC), `hammerfest-spmi` (0xC, NFC #2), `uwb0` (0xF) |
| `/arm-io/aop-spmi1` | 0x90b14000, 0x90b04000, 0x90b00000 | `uwb` (0xF), `wlan-idc` (0xE), `baseband-idc` (0xD) |

`reg` on a follower is six u32s, for example `pmu-main reg = [0xe 3 0 4 0 0]`. I read word 0 as the SPMI slave ID **[INF, consistent across all nodes]**.

The `aop-spmi*` buses carry radio coexistence and SAR "billboards" (`baseband,heb`, `wlan,idc`), not power. They are covered in the wireless chapter. The `NUB_SPMI0/1_THROTTLE_IRQ_SELECTED0..7` and `ORED_SPMI0/1_THROTTLE_VWS0/1` perf-counters in `pmgr-child` show that PMU interrupts on nub-spmi0/1 can be routed straight into the SoC throttle network **[DT]**. See §8.

### 1.1 `pmu-main` — "becketts" (primary PMU)

Path `/arm-io/nub-spmi0/pmu-main`. Compatible `["pmu,spmi", "pmu,becketts"]`, `hw-name = "becketts"`, `is-primary = 1`, `has-fw = 1`, `has-lpem-fw-scc = 1`. Drivers are `AppleDialogSPMIPMU` (`com.apple.driver.AppleSPMIPMU`, with child `AppleDialogSPMIPMURTC`) and `ApplePMUFirmwareDriver` (`com.apple.driver.ApplePMUFirmwareDriver`), both matched on `pmu,spmi` **[DT][KC]**. The class name keeps the historical "Dialog" prefix. Who makes the current silicon is not stated anywhere in these sources **[INF]**.

All properties (raw DT payload) **[DT]**:

| Property | Value | Meaning (my reading) |
|---|---|---|
| `reg` | `[0xe 3 0 4 0 0]` | SID 0xE |
| `interrupt-parent` | 0xc5 (= nub-spmi0) | |
| `interrupts` | `0x3e` (+0x2 type word) | |
| `fw-mcom-address` | bytes `60 2b` = 0x2b60 | PMU firmware mailbox ("mcom") |
| `fw-mcom-int-index` | 1 | |
| `fw-host-irq-address` | 0x2b08 | |
| `general-config` | 0x4000000c800 | |
| `info-id` | 0xa00000000 | |
| `info-clock_offset` | 0x600002100 | |
| `info-rtc` / `info-rtc_scrpad` / `info-rtc_alarm_*` | 0x2002 / 0x21 / alarm @0x2008, IRQ mask @0x200e, ctrl 0x20, masks 1/2/0x40 | PMU RTC (feeds `AppleDialogSPMIPMURTC`) |
| `info-scrpad` | 0x280000008000 | Scratchpad |
| `info-scrpad_socd` | 0x80000008b00 | SoC-debug scratch |
| `info-scrpad_lpm_ctrl` / `info-scrpad_lpm_log` | 0xa7dc / 0xa780 | Low-power-mode control and log in PMU scratch (AppleLPM, §6) |
| `info-leg_scrpad` | 0xf800 | |
| `info-fault_log` | 0x900001000 | Fault log location |
| `info-off2wake_source` | 0x20000281b | |
| `info-has_phra` | 1 | |
| `ptmu-region-0..15-data`, `ptmu-secure-region-0..4-data` | 0x400000c000 … 0x4000000cc00; secure 0x4000000b000 … 0x2000000be00 | PMU telemetry ("PTMU") windows; the secure ones are for a secure client |
| `function-get_vbus_detect` | `<0x9f 'keyR' 'VBUS'>` | Read SMC key `VBUS` via `smc-pmu` (phandle 0x9f) |
| `function-get_pdod` | `<0x9f 'keyR' 'BDD1'>` | Read SMC key `BDD1` (pack depth-of-discharge, **[INF]**) |
| `function-external_standby` | `<0x9f 'keyW' 'MBSE'>` | Write SMC key `MBSE` |
| `upo-shutdown-delay` | 0 | UPO = unexpected power-off |

**Fault and wake vocabulary.** The node lists 53 `info-fault_name-N` and 15 `info-o2ws_name-N` strings **[DT]**. They are the PMU's shutdown and wake causes, and they define the brownout and over-temperature vocabulary:

- Undervoltage: `uv,vddmain_uvlo`, `uv,vdd_boost_uvlo`, `uv,cp_uvlo`, `uv,ldo9_uv`, `uv,ldo9b_uv`.
- Overvoltage: `ov,vddmain_ovlo`, `ov,vdd_boost_ovlo`, `ov,cp_ovlo`, `ov,ldo9_ov`, `ov,ldo9b_ov`, `ov,ldo_ana_ovp`, `ov,ldo_dig_ovp`, `ov,cpneg_dvc`.
- Thermal: `ot,overtemp`, `ot,tdie_overtemp`, `ot,tdie_overtemp_idx0..4`, `temp_abs_buck0`, `temp_abs_buck1`, `ntc_shdn` (battery NTC thermistor shutdown).
- SoC-hot / reset inputs: `sochot,reset_in_3`, `wdog,reset_in_1`, `dbg_rst,reset_in_2`, `crash,crash0_in`, `crash,crash1_in`, `crash,metis_hw_crash`, `crash,metis_fw_crash`.
- Buttons: `btn_rst,two_finger_rst`, `btn_rst,btn_seq_reset`, `btn_rst,sec_btn_seq`, `btn_shdn`, `sstate,button_dfu_recover`, `sstate,dfu_btn_seq_reset`.
- Timeouts: `timeout,watchdog_timeout`, `timeout,wdog_fw_timeout`, `timeout,target_st_wdog_timeout`, `timeout,dblclick_timeout`, `xtal_wdog_expiry`, `cp_wdog_expiry`.
- Other: `emerg_shdn`, `target_off_shutdown`, `target_off_restart`, `target_off_conflict`, `otp_crc`, `spmi,spmi_fault`, `sgpio`, `mfsm_sgpio`, `por`, `rst`.
- Wake sources: `gcb_wakeup`, `gcb_off_wakeup`, `gcb_crash_wakeup`, `rtc_alarm_wakeup`, `auto_wakeup`, `hw_wdog_wakeup`, `fw_wdog_wakeup`, `pgood_wdog_to_off_wakeup`, `pgood_wdog_to_error_wakeup`, `target_state_wdog_timeout`, `fw_req_auto_wakeup`, `fw_nonsec_off_wakeup_csr`, `fw_nonsec_off_wakeup_wdog`, `dft_ctrl2_wakeup`, `wake2lf_negedge`.

"metis" appears only as a crash source. Which block it names is not stated **[INF: likely the PMU's internal controller]**.

The **buck and LDO list** is limited to what the fault names reveal. There are at least two bucks with absolute-temperature monitors (buck0, buck1), LDO9 and LDO9b, analog and digital LDOs, a charge pump (CP and its negative rail), a boost stage (VDD_BOOST) and VDD_MAIN **[DT]**. Per-rail voltages, currents and buck counts are not in the DT (see Gaps). AOP firmware contains `RailEnergyBecketts: SMC service not found!` **[FW: aopfw-v68aop]**, so per-rail energy telemetry from this PMU is read through the SMC.

**PMU firmware.** iBoot contains the string `ApplePMUFirmware-743.40.11~956.release` three times **[FW: iBoot.v68.RELEASE]**. No separate PMU image exists in the BuildManifest. iBoot also references `pmu-secondary`, `pmu-follower-serial-number`, `pmu-arc-reset` and `pmu-btmspk-reset`. So iBoot loads both PMUs' firmware over the `fw-mcom` mailbox, and the kernel's `ApplePMUFirmwareDriver` talks to it after boot **[INF]**.

### 1.2 `pmu-secondary` — "fairmont"

Path `/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`. Compatible `["pmu,spmi", "pmu,fairmont"]`, `hw-name = "fairmont"`, SID 0x1, `has-fw = 1`, `fw-mcom-address = 0x2b60`, `fw-mcom-int-index = 0`, `fw-host-irq-address = 0x2b08`, `info-leg_scrpad = 0xf800`, `interrupts = 0x7e`. Its parent is `sgpio-bridge-pmu-main` (`compatible = "sgpio-bridge"`, `sgpio-bus-id = 0`, `bridge-offset = 0xdd10`), driven by `AppleSGPIOHostBridgeController` (`com.apple.driver.AppleSGPIO`, provider `AppleDialogSPMIPMUNub`) **[DT][KC]**.

So the second PMU is not a direct SPMI follower of the SoC. It is reached through the main PMU's serial-GPIO bridge. Two PMUs are typical for large Apple designs. I also infer that `number-of-PMUs = 2` in `btm` means BTM collects battery-side data from both **[INF]**.

### 1.3 `btm` — battery telemetry/transient monitor

`/arm-io/nub-spmi0/btm`, `compatible = "btm,phone"`, SID 0xE (a function inside the becketts PMU), `interrupt-parent = 0xa6` (`/arm-io/aon-ptd`, see §8), `interrupts = "btm0".."btm3"` (stored reversed as `0mtb1mtb2mtb3mtb`) **[DT]**. Other properties: `number-of-batteries = 2`, `number-of-PMUs = 2`, `btm-pmu-type = 0xf`, `battery-data-collection = 1`, `battery-data-clients = 1`, `config-vddmain-data-read = 1`, `config-duty-cycle-data-read = 1`, `config-auto-rate-change-flag = 1`, `pack-format-enabled = 1`, `function_ptd_read_mult = <aon-ptd 'RMtp'>`.

Driver: `AppleBTM` (`com.apple.driver.ApplePhoneBTM`, provider `AppleARMSPMIDevice`, match `btm,phone`) **[KC]**. Its internal agents are `AppleBTMPMUAgent`, `AppleBTMAONPMUAgent`, `AppleBTMBPICAgent`, `AppleBTMBatteryDataAgent` (reads `PresentDOD` per pack from `AppleSmartBatteryManager`: "ASBM arrival success", "Pack %d failed to get PresentDOD"), `AppleBTMDataClientPPM` and `AppleBTMDataClientSMC`. Its errors include "unable to config new Vthreshold proportional target" and "unable to config new Duty Cycler threshold value" **[KC]**.

BTM therefore sets the PMU's voltage-threshold and duty-cycle limits from battery state, and feeds the PPM. The PPM calls into it through `function-btm-config`, `-config-battfw`, `-start`, `-stop` and `-vthr`, all pointing at phandle 0xc9 = `btm` **[DT]**. Apple does not expand "BTM" in these sources. "Battery transient monitor" is my reading **[INF]**.

### 1.4 `shamisen` and `stonehenge` (nub-spmi1)

Both have only `name`, `reg` and `AAPL,phandle`. `shamisen` is SID 0xC; `stonehenge` is SID 0xF. Neither has a `compatible` and no kext matches either by name **[DT]**.

- **stonehenge.** The kernel ships `AppleStonehengeBPIC`, a subclass created by `AppleBPIC` (`withParent(AppleBPIC*, …)`). Its interrupt handlers are `VCELL_WARN`, `VCELL_ERR`, `ICELL_WARN`, `ICELL_ERR`, `BP_VCELL_DUTY`, `BP_ORFUNCT1_TEMP` and `BST_ERR`. `AppleBPIC` matches `btm,bpic` **[KC]**. Stonehenge is therefore a battery-protection/pack-interface IC that monitors cell voltage, cell current and temperature, and has a boost stage. On this unit's DT it is not bound by name-match. Either iBoot adds `compatible` at runtime or the BPIC path is unused on V68 **[INF]**.
- **shamisen.** No kernel or firmware string references this name in the images I searched. Its function is unknown. Given its bus neighbour, a second pack-side or charger-side power IC is plausible **[INF, low confidence]**.

### 1.5 `spmi-hpm0` — USB-C port controller (power role)

`/arm-io/nub-spmi2/spmi-hpm0`, `compatible = "usbc,cbtl1702,spmi"`, SID 0xC. Other properties: `hpm-class-type = 0xf`, `port-type = 2`, `port-number = 1`, `rid = 0`, `features-supported = [1 2 5]`, `transports-supported = [1 2 3 5]`, `feature-ldcm-hw-version = 4`, `feature-ldcm-arch-version = 5`, `interrupts = [0xb 0x11 0x13]` with `interrupt-type = [0 2 3]`, `dock = 0x1c5` (`/port-usb-c-1`), `aod = 0x1b6` (`/arm-io/aod2`), `function-ignore_vbus_drop = <port-usb-c-1 'bvgi'>` **[DT]**.

Driver: `AppleHPMARMSPMI` (`com.apple.driver.AppleHPM` 3.4.4) **[KC]**. "LDCM" is liquid-detection/corrosion mitigation **[INF; the kernel counts `NumLDCMCollisions`, `PortControllerIrqCntldcm`]**. PD negotiation telemetry is surfaced through the SMC battery driver (`PortControllerActiveContractRdo`, `PortControllerPortPDO`, `PortControllerNPDOs`, `PortControllerNEprPDOs`, `PortControllerPwrRoleSwapCount`, `PortControllerHardResetCount` …) **[KC]**. The part designator `cbtl1702` is Apple-internal and the vendor is not stated **[INF]**.

---

## 2. The SMC — owner of charging, gauges and power telemetry

`/arm-io/smc` is an ASC co-processor: `compatible = "iop,ascwrap-v8"`, `role = "SMC"`. Its `reg` windows start at 0x8c600000 (size 0x74000), 0x8c050000 (0x4000), 0x96020000 (0x10000) and 0x8c810000 (0x100). It has `msgbox-mailbox-num = 2` (post-office mailbox), `interrupts = [0xc4 0x9c 0x74]`, `aot-power = 1` and `timers-reg-index = 3` **[DT]**. Driver: `AppleASCWrapV8` (`com.apple.driver.AppleA7IOP-ASCWrap-v8`) → `RTBuddy` on `iop-smc-nub` → `AppleSMCKeysEndpoint` on `SMCEndpoint1` (`com.apple.driver.AppleSMC` 3.1.9) **[KC]**.

`iop-smc-nub` properties: `firmware-name = "t8160smc"`, `pre-loaded = 0`, `region-base = 0x28de00000`, `region-size = 0x140000` (1.25 MiB carve-out, also in `sptm-allow-reg`), `no-shutdown = 1`, `user-power-managed = 1`, `no-hibernate-sleep`, `cold-boot-after-hibernate`, `continuous-time`, `watchdog-enable`, `coredump-enable` **[DT]**. Its GPIO block is `/arm-io/smc-gpio` (`gpio,t8101`, MMIO 0x8c820000, 6 pins, 7 IRQ groups, `role = "SMC"`) **[DT]**.

SMC child nubs (all under `/arm-io/smc/iop-smc-nub`) **[DT][KC]**:

| Node | Key properties | Driver (kext) |
|---|---|---|
| `smc-pmu` | `compatible "smc-pmu"`. Interrupt controller whose events are named `btn1=hold`, `btn3=action`, `btn4=capture`, `gpio11=charger`, `gpio16=wifibt`, `gpio6=baseband`. `function-pmu_button = <buttons 'BtuD'>` | `AppleSMCPMU` (AppleSMC) |
| `smc-charger` | `device_type smc-charger`, `port-type 2` (USB-C), `port-number 1`, `dock-num 1`, `function-dock_parent = <port-usb-c-1 'Pcca'>`, `battery-id` (8×u32, filled by iBoot), `boot-adapter-id`, `boot-voltage` | `AppleSMCCharger`; parent of `AppleSmartBatteryManager` |
| `smc-ext-charger` | `port-type 9` (MagSafe), `function-dock_parent = <port-magsafe-1>`, `function-dock_wired = <port-usb-c-1>`, `has-ironman-charging 1`, `has-espresso 1`, `has-ironman-camera-cloak 1`, `has-ironbull-camera-cloak 1`, `hd-mic-coex 1`, `extended-otp-cal 1`, `has-peripheral-logs 4`, `audio-driver "AppleCS42L79Audio"`, `camera-driver "AppleCamera"`, `backlight-detection 0` | `AppleSMCWirelessCharger` (`com.apple.driver.AppleSMCWirelessCharger`) |
| `smc-charger-util` | `port-type 2`, `report-port-event 1` | `AppleSMCChargerUtil` |
| `smc-power-out` | `ioport-client 1` | `AppleSMCPowerOut` (reverse/accessory power out) |
| `smc-aop` | `function-link-data_enable/param_get/param_set` → phandle 0x63, `link-tx_config` | `AppleAOPSMC` |
| `smc-acam` | `compatible smc-acam` | `AppleSMCACAMDriver` |

The SMC also feeds the thermal sensor dispatcher `/arm-io/smctempsensor0` (`smc-tempsensor`, `sensor = "mTPLmTLLmETW"`, which is three 4-char SMC sensor keys stored byte-reversed, `timerInterval = 1000` ms) → `AppleSMCSensorDispatcher` **[DT][KC]**. On the AOP side, `/arm-io/aop/iop-aop-nub/smc-control` carries `smc-aop-charge-config = [0x10640000 3 4 0x2a]` → `AppleAOPSMCDriver` (`com.apple.driver.AppleSPU`) **[DT][KC]**. AOP firmware has an SMC key client (`SMCKeyService.cpp`, `SMCSensorExchange`, `smcReadWriteKey`) and reports charge status ("SENSOR,[GBE],charge status") **[FW: aopfw-v68aop]**.

**Why the SMC matters here.** On this platform the kernel never talks to a charger IC or a gas gauge directly. Every battery and charger read (`AppleSmartBattery*`, `AppleChargerData`, `AppleGasGauge*Update`, `AppleBatteryAuth`) is an SMC key read or write ("failed to read key '%c%c%c%c'") **[KC]**. The SMC is the battery/charger host. The physical charger and gauge buses hang off the SMC, not the AP **[INF from the absence of AP-side gauge or charger nodes]**.

---

## 3. The two batteries, BMU/BMU2 and Volchok

### 3.1 Physical **[PUB]**

Two cells. Teardowns and Apple's EU energy label give 2,962 mAh (11.56 Wh) and 1,921 mAh (7.5 Wh), 4,883 mAh total, in steel cases, removed with electrically released adhesive ([MacRumors teardown roundup](https://macrumors.com/2026/10/24/iphone-duo-teardown-videos/), [iClarified](https://www.iclarified.com/103014/iphone-duo-teardowns-reveal-dual-battery-design-and-repair-challenges-video), [Android Headlines](https://www.androidheadlines.com/2026/10/iphone-duo-dual-battery-capacity-specs.html)). The brief's 11.567 Wh + 7.506 Wh match those to rounding. One pack sits in each half of the fold, so pack-to-pack current crosses the hinge **[PUB teardown layout; the exact hinge conductor is not visible in software]**.

### 3.2 Personalization: `BMU`, `BMU2` **[FW: BuildManifest.plist]**

| Field | BMU | BMU2 |
|---|---|---|
| `*,BoardID` | 33171 (0x8193) | 33171 (0x8193) |
| `*,ChipID` | 58629 (0xE505) | 58629 (0xE505) |
| `*,DigestMap` | `Firmware/Volchok/BAT8193/DigestMap.der`, digest a217a7c5… | same |
| `*,FirmwareMap` | `Firmware/Volchok/BAT8193/FirmwareMap.plist`, digest b87e1891… | same |
| Info | `Personalize = True`; not loaded by iBoot | same |

So both gauges are the same chip and board and receive the same image set. Each is still a distinct personalization target, meaning each gets its own TSS-signed ticket during restore **[INF from the separate manifest identities]**. Board ID 0x8193 is literally the "8193" in `BAT8193`.

### 3.3 What is inside Volchok/BAT8193 **[FW]**

`FirmwareMap.plist` (437 KiB) contains `product_id = "BAT8193"`, `board_id = 33171`, `digest_der` (2016 B) and `hw_version → "21"`. Under `hw_version "21"`:

- `firmware`: version 209210031, 98,304 B. The payload begins with an ARM Cortex-M vector table (initial SP 0x20006000, reset vector 0xc4d5). Its strings include ARM-compiler runtime messages (`SIGRTMEM: Out of heap memory`, `SIGABRT`) and task names `vPRCTsk` and `vUPDTsk`, so it is an RTOS-style Cortex-M gauge firmware with a protection task and an update task **[FW; task meaning INF]**.
- `su_crypto`: version 172502, 24,576 B. This is the secure-update/authentication component **[INF from name; it pairs with `AppleBatteryAuth` / `AppleBeadsBatteryAuth` in KC]**.
- `chemistry`: 25 cell-chemistry IDs (1017722617 … 1019533277), each with an 8 KiB `configuration` (set_id 2630) and a 4 KiB `dnvd` (set_id 1073744424) at its own versions. A 26th ID (12144171) has `cell_id_skip = true`.
- `DigestMap.der` is a DER structure starting `BAT8193`, 0x8193, then a list of (4-byte id, 32-byte hash, 32-byte hash) records. It is the hash manifest the gauge checks before accepting an update **[FW; purpose INF]**.

Full listing: [`data/06-power-battery-thermal/volchok_bat8193_firmwaremap_summary.txt`](../data/06-power-battery-thermal/volchok_bat8193_firmwaremap_summary.txt).

What **Volchok** is: the directory name for the battery-gauge ("BMU", battery management unit) firmware family. Its payload is a cell-chemistry-aware gauge plus a crypto module. The per-chemistry configs mean one firmware supports cells from several suppliers or lots, selected by the cell ID the gauge reads from the pack **[INF from structure]**.

### 3.4 Kernel side **[KC]**

`AppleSmartBatteryManager` (`com.apple.driver.AppleSmartBatteryManagerEmbedded`, provider `AppleSMC`) builds this object tree:

```
AppleSmartBatteryManager            (user client: AppleSmartBatteryManagerUserClient, "batman")
 └─ AppleSmartBattery               (IOPMPowerSource; the system battery seen by IOKit/powerd)
     ├─ AppleSmartBatteryPack  ID 0  ── AppleSmartBatteryBank ── AppleSmartBatteryCell
     ├─ AppleSmartBatteryPack  ID 1  ── AppleSmartBatteryBank ── AppleSmartBatteryCell
     ├─ AppleChargerData       (per charger: ChargerID, ChargingCurrent/Voltage, ChargerVBUS/IBUS, ChargerEfficiency, RebalanceHWBypassFETStatus …)
     ├─ AppleGasGaugeUpdate / AppleGasGaugeBeadsUpdate  (+UserClients; entitlement com.apple.private.gasgauge-update)
     ├─ AppleBatteryAuth / AppleBeadsBatteryAuth          (trusted-battery path)
     └─ AppleSmartBatteryHFDataClient / AppleSmartBatteryUserClient (high-frequency data queue; entitlement com.apple.private.applesmartbattery-smcdatastream)
```

The hierarchy is inferred from class names and log strings such as "AppleSmartBatteryPack: ID: %d …", "AppleSmartBatteryBank: Pack ID: %d Bank ID: %d" and properties `PackID`, `BankID`, `CellID`, `BankCount` **[INF]**.

Published properties seen as strings (selection) **[KC]**:

- **Aggregate (AppleSmartBattery):** `CurrentCapacity`, `MaxCapacity`, `DesignCapacity`, `NominalChargeCapacity`, `AppleRawCurrentCapacity`, `AppleRawMaxCapacity`, `Voltage`, `Amperage`, `InstantAmperage`, `CycleCount`, `IsCharging`, `FullyCharged`, `ExternalConnected`, `AdapterDetails`, `BatteryPackCount`, `ChargerCount`, `uiSOC`/`UISoc`, `ChargerPathSelected`, `ChargerVBus0`, `ChargerVBus1`, `ChargerIBus0`, `OPDDualChargerState`, `IPDChargingAllowed`, `IPDInputCurrent`, `IPDInputPower`, `IPDRatio`, `IPDRatioOverride`, `IPDWattageOverride`, `NotChargingReason`, `SlowChargingReason`, `TimeChargingThermallyLimited`, `ChargeLimitTBATMAX50`, `AppleChargeRateLimitIndex`, `ShipChargeLimit*`, `PowerTelemetryData` (`SystemPowerIn`, `SystemLoad`, `WallEnergyEstimate` …), `BatteryHealthData` (`BatteryHealthMaxCapacity`, `BatteryHealthServiceOption`, `BatteryHealthServiceFlags`).
- **Per pack:** `Qmax`, `RaTableRaw`, `PresentDOD`, `ChemID`, `AlgoChemID`, `GasGaugeFirmwareVersion`, `PermanentFailureStatus`, `CellVoltage`, `VoltageCell0..3`, `QmaxCell0..2`, `CellCurrent`, `CellCurrentRatio`, `CellDisconnect`, `BatteryCellDisconnectCount`, `BatteryTemperatureBmuTs1/2/3`, `LifetimeData` (min/max temperatures, voltages, currents, `TotalOperatingTime`, `SafetyFaultCounter` …), `FailureCounters` (`OverVoltage`, `ChargingOverCurrentHW`, `DischargingShortCircuitHW`, `FETOverTemperature` …), `ShutDown*` (data from the last UPO), `KioskMode*`, `CarrierMode*`, `LPEMData`, `IPDBatteryDemand`.
- **Rebalance:** `RebalanceData`, `RebalanceEnableStatus`, `RebalanceNotRebalancingReason`, `RebalanceTimeSeconds`, `RebalanceErrorFlags`, `RebalanceInrushCurrentDebug`, `RebalanceOutputStruct`, `RebalanceHWBypassFETStatus`.

**How the halves are balanced.** This is the most specific evidence in the image. `AppleSmartBatteryPack::updateRebalanceData` reads each pack's temperature and DOD SMC keys. It then calls the PPM driver function `ApplePPMInterfaceAPIFunction` with `kPPMInterfaceAPIReq` + `kPPMTempInReq` + `kPPMDODInReq` + `kPPMChemIdReq`, receives `kPPMOutImpdDataR0` (an impedance array), and writes it back to an SMC "impedance key". It skips the write if PPM returns all zeros **[KC strings]**. So the SMC-side rebalancer (which moves charge between packs, with a hardware bypass FET and inrush monitoring) is parameterized by the AP's battery model of each pack's impedance. The `IPD*` fields (input power distribution: what share of charger input goes to each pack, `IPDRatio`) and `OPDDualChargerState` (output/dual-charger state) show two charger paths, one per pack **[INF from names]**.

**Battery authentication.** `AppleBatteryAuth[%d]` (one per pack) runs `GetInfo` → `GetCertSerial` → `GetCert` → `SetChallenge` → `PollAuthStatus` → `GetNonce` → `GetSignature` → `SetAuthStatus`, all as SMC commands, then publishes `TrustedBatteryEnabled`, `BatteryAuthPassed` and a trusted-data nonce **[KC]**. `AppleBeadsBatteryAuth` is the newer "Beads" protocol variant (TraceID, public key, signed data indices, `wrdc_bank1..3`) **[KC]**. This is what powers the "Genuine Apple Part" and "Unknown part" battery messages in Settings **[INF]**.

---

## 4. Wired charging: USB-C PD, 60 W

**Hardware chain:** `/port-usb-c-1` (`compatible "dock,usb-c"`, `port-type 2`, `primary-port-id 2`) ← `spmi-hpm0` (PD/Type-C controller, nub-spmi2) → `smc-charger` (`function-dock_parent` = port-usb-c-1) **[DT]**. `smc-pmu` names `gpio11 = charger`, which is the charger interrupt into the SMC **[DT]**.

**Kernel chain:** `AppleHPMARMSPMI` ↔ `IOAccessoryManager`/`IOPortTransport` (USB-C port object) **[KC]**. `AppleSMCCharger` / `AppleSMCChargerUtil` (`dockNum`, `magSafeAuth`, `reportPortEvents`) → `AppleSmartBattery::readAdapterInfo` ("Port:%d nominalV", "current", "Family Code", "AdapterID", "power tier", "UsbHvcMenu"/"UsbHvcHvcIndex" = PD PDO list) **[KC]**.

The 60 W rating is public **[PUB, brief]**. The DT and KC only show that EPR-capable messages are tracked (`PortControllerNEprPDOs`). The max contract is decided by charger firmware and policy, not visible here.

**Hinge path [INF].** The USB-C port and the two packs are in different halves, at least for one pack. Software sees two charger channels (`ChargerVBus0/1`, `ChargerCount`, `IPDRatio`). I infer a charger near each pack, with power crossing the hinge either as VBUS or as a battery-voltage bus. Which one cannot be determined from software.

---

## 5. Wireless: MagSafe / Qi2 25 W and the WCH firmware

**Port:** `/port-magsafe-1` (`compatible "dock,0pin"`, `device_type "port-magsafe"`, `port-type 9`, `primary-port-id 0x200`, `transports-supported 0xf`, `features-supported 1`) → `IOAccessoryDock0PinBuiltin` (`com.apple.iokit.IOAccessoryManager`) **[DT][KC]**.

**Controller and firmware:** BuildManifest component `WCHFirmwareUpdater` → `Firmware/WirelessPower/WirelessPower.v68.im4p`, IM4P type `wchf`, version "1.0" **[FW]**. The payload is an `rkosftab` (RTKit OS file table) with four segments **[FW]**:

| Tag | Offset | Size |
|---|---|---|
| `DORX` | 0x70 | 0x1a348 |
| `DOHB` | 0x1a3b8 | 0x1e748 |
| `BOOT` | 0x38b00 | 0x62c |
| `DOTX` | 0x3912c | 0x1f080 |

Build string `AppleWirelessPower-756.52.1~3`, `RTKit_armv7em_Oz_floatabihard-3514.40.18.release` (Cortex-M4F/M7-class) **[FW]**. I read RX/TX/HB as a receive-mode image, a transmit (reverse/accessory power-out) image and a third mode, plus a bootloader **[INF from tags]**. iBoot contains `WCHF` and "wchf image too large - 0x%zx", so iBoot stages this image to the controller rather than restore-only **[FW: iBoot; INF on timing]**.

**Kernel:** `AppleSMCWirelessCharger` (on `smc-ext-charger`) **[KC]**. Notable behaviour from strings:

- "Puck classifier": `Apple MagSafe Charger`, `Apple MagSafe Duo Charger`, `MagSafe Battery Pack`, `chg-mpp` (MPP = magnetic power profile, the Qi2/MagSafe profile), with `Inductive2PPPromotionState`.
- In-band comms "Espresso" (`kInBandCommsEventEspressoInfoUpdated`, `com.apple.espressotool`).
- Coexistence "cloaking": wireless power is paused around camera and audio use (`has-ironman-camera-cloak`, `hd-mic-coex`, `EngageCloak`, `CloakReason`, `HostRequestedCloak`, `_audioNotificationCallout`, `_displayNotificationCallout`).
- Thermal back-off ("too hot !!!", `ThermalPowerBudget`, `CPMSPowerBudget`).
- Telemetry: `RectifierVoltage`, `RectifierCurrent`, `Frequency`, `SignalStrength`, `FODetected`, `QiPacketResult`, `PTxType`, `AuthFodStatus`, `3PPAuthFailCount`.

**Accessory identification:** MagSafe accessory ID and auth uses `AppleC26Charger` (`AppleQiAuthProtocol`, `AppleC26AuthProtocol`, `AppleB237DockInfo`) over `AppleC26DeviceStream` **[KC]**. The NFC path for MagSafe accessories ("NFC accessory ID") uses the `stockholm`/`hammerfest` NFC controllers on aop-spmi0 and the `NFC.transport` CoreAccessories plug-in **[DT][DSC]**. Details are in the NFC/wireless chapter. The 25 W Qi2 rating is public only **[PUB]**.

---

## 6. AppleLPM, LPEM and "power reserve"

- **AppleLPM** (`Ap,LowPowerMode` → `Firmware/AppleLPM/AppleLPM.v68.release.im4p`, IM4P `alpm`, 1.9 MB). Manifest flags: `Trusted = False`, `IsiBootEANFirmware = True`, `Personalize = True` **[FW]**. The payload is an AArch64 RTKit image (`RTKit_armv8_chinook_Oz_flto_pac-3514.40.18.release`) with MMU, page-table, PPL-handoff and `uat_handoff` code, an inflater, an AFK client (`[ALPM|AFK_client:%s]`), `disp0-service`, "DCP workloop"/"DCP2 workloop", `set_framebuffer`, and states "AppleLPM Main System Start", "Device Charging", "Silent Check", "System reboot to OS" and "System shutdown to OFF" **[FW]**. iBoot passes it `alpm-24h-mode`, `alpm-dst-offset`, `alpm-next-dst`, `alpm-language-direction` and `alpm-number-system`, and draws "ALPM Display"/"ALPM Display Sec" **[FW: iBoot]**.

  Conclusion **[INF]**: AppleLPM is a small OS that iBoot can boot instead of iOS on AP cores. It drives both display pipes (DCP and DCP2, which fits the two panels) to show a localized clock and charging state while the phone is "off" or too depleted for iOS. "EAN" firmware lives in iBoot's EAN storage. The PMU scratch locations `info-scrpad_lpm_ctrl` (0xa7dc) and `info-scrpad_lpm_log` (0xa780) are its handshake and log with the PMU **[DT]**.
- **LPEM** ("low-power ... mode", Apple's term for the post-shutdown reserve that keeps Express Cards / Find My working) **[INF]**. Evidence: `has-lpem-fw-scc = 1` on the PMU, `cpms-use-lpem-data = 1` in PPM **[DT]**; `LPEMData`, `ShutDownLPEMMode` and `ShutDownLpemSocfThresh` in the battery kext **[KC]**; separate `Wireless1,ACIBTLPEM`, `RTKitOSLPEM` and `ScanBTLPEM` firmware for the N1 radio **[FW: BuildManifest]**.
- **iOS Low Power Mode** (the user toggle) is a userland policy. See §10.

---

## 7. PMP, PMC, pmgr, rails and CLPC

### 7.1 PMP — power manager processor

`/arm-io/pmp`: ASC (`iop,ascwrap-v8`, `role "PMP"`), `reg` at 0x80e00000/0x74000, 0x80850000, 0x96020000, 0x80500000/0xb0000, 0x803d0000. Other properties: `msgbox-mailbox-num 4`, `interrupts [0xc6 0x9e 0x76]`, `iommu-parent 0x93` (= `/arm-io/dart-sbr/mapper-pmp`, DART-SBR stream 6), `power-gates`/`clock-gates`/`service-gates = [0x97 0x98]`, `pio-vm-base 0xc0000000`, `ptd-update-reg-index 4` **[DT]**.

`iop-pmp-nub`: `firmware-name "t8160pmp"`, `region-base 0x280500000`, `region-size 0xb0000`, `no-shutdown 1` **[DT]**. Drivers: `AppleASCWrapV8` → `RTBuddy` → `ApplePMPFirmware`, plus `ApplePMPv2` (`PMPEndpoint1`/`PMP0Endpoint1`/`PMP1Endpoint1`) and `ApplePMPThermal` (`PMPEndpoint2`), each with user clients; ApplePMP logs "Connected to AppleCLPC" **[KC]**.

**Firmware:** `PMP` → `Firmware/pmp/t8160pmp.im4p` (IM4P `pmpf`, `IsLoadedByiBoot`, `IsFUDFirmware`) **[FW]**. It is a Mach-O arm64 preload binary built on `RTKit_armv8_chinook_Oz_flto-3514.40.18.release`. Its strings include "PMP started!!!", "PMC Keep Alive", "SEP UP", `LTS_CTRL: Fast Die Throttling %s.`, `LIFETIME-SERVO`, `die%d-temp-sensor-%s-%s`, `die%d-fast-die-loop-%s-%s`, `THROT-GPU-SUM`, "Volt-Temp HM", `lts-acsk-tddb-config` and `LS: %s TDDB …` **[FW]**.

PMP controllers (from `iop-pmp-nub/controller`) **[DT]**: `DIE-TEMP`, `DCS-BW`, `DCS-WR-BW`, `AGX-DCS-BW`, `AGX-AF-RD-BW`, `AGX-AF-WR-BW`, `ANE-DCS-BW`, `ANE0/1-DCS-BW`, `ANE0/1-AF-BW`, `ANE0/1-LINK0/1-AF-BW`, `SOC-NI0..3-BW`, `AFI-TOP-BW`, `MEM-CACHE`, `LIFETIME-SERVO`.

So PMP runs the fast die-temperature loop and the memory/fabric bandwidth-driven DVFS. It also runs a **lifetime servo**: TDDB (time-dependent dielectric breakdown) aware voltage and temperature capping (`lts-config`, `lts-voltage` for clusters `PACC` and `AGX`) **[DT][FW]**. PMP DVFS domains: `DCS`, `SOC`, `DISP`, `AVE` (`dvfs-domain`) **[DT]**.

### 7.2 PMC

`Ap,ApplePMCFirmware` → `Firmware/pmc/t8160pmcfw.im4p` (IM4P `pmcf`, `IsLoadedByiBoot`, `IsFUDFirmware`, `Trusted`) **[FW]**. The payload is a 36 KiB Mach-O for ARMv7-M (Cortex-M) with stripped symbols and UUID 1B4AF228-4164-3D69-9F2F-A0528D1F3454. It has no readable strings **[FW]**. `pmgr` has `pmc = 1`, `pmc-pmgr = 0x1f`, `pmc-ltr-ka = 1`, `pmc-sac-dcs-offset` **[DT]**, and iBoot has `IPCE_PMC_PS_SAVE/RESTORE_IBOOT2`, `IPCE_PMC_PS_FW_TELEM_DATA_SAVE_IBOOT2` and `pmgr_disable_pmp_pmc` **[FW: iBoot]**. PMP firmware sends a "PMC Keep Alive" **[FW]**. So PMC is a tiny pmgr-embedded microcontroller that sequences power states (save/restore across sleep, LTR keep-alive) under PMP supervision **[INF]**.

### 7.3 pmgr, voter agents and rails

`/arm-io/pmgr` (`pmgr2,arch` → `ApplePMGRv2`) has `pmp = 2`, `clpc = 3`, `pmc = 1`, `chiplet-count = 1`. `/arm-io/pmgr-child` (`pmgr2,t8160` → `AppleT8160PMGR`) **[DT][KC]** holds:

- `voter-agent`: agents `PMP`, `CLPC`, `GFX`, `AP`, each with weight 0x280.
- `voter-rail-data`: rails **DCS** (agent mask 0x1), **SOC** (0x2), **DISP** (0x4), **AVE** (0x8). These are the shared voltage rails whose level is the max of the voters' requests **[DT; voting semantics INF]**.
- `clusters = 4 (ECPU) / 2 (PCPU)`, `acc-clusters` `EACC`/`PACC`, `perf-domains` (SOC, ECPU, DCS, PCPU, …), `cluster-dvfs-devices`.
- `mtr-sensor` (per-cluster MTR temperature sensors `Te00005i`, `Te0000ai`, `Tp00002i`, `Tp00005i`, `Tp00007i` …).
- `boost-agent` (display/ANS/AVE/ISP/… boost voters), `ptd-*` offsets.
- `function-pmp_control = <pmp-nub 'CPMP'>`.

The PMP `soc-device` table maps SoC power islands to owners: `DCS`, `AMCC`, `SOC-NI0..3`, `SOC-AON`, `SOC-REST`, `EACC0`, `PACC0`, `AGX` (`GFX_`), `ANE0`, `ANE1`, `ISP`, `DISP0`, `DISP1`, `DISPEXT`, `AVE`, `AVD`, `MSR`, `JPEG`, `PRORES`, `SMC` (`SMC_`), `SEP`, `ANS`, `PCIE`, `SBR`, `SIO`, `ATC`, `GFXC` **[DT]**. `DISP0` and `DISP1` are the two panel pipes. The mapping from these SoC rails to physical PMU bucks is not in the DT **[gap]**.

### 7.4 CLPC

`/arm-io/pmgr/clpc` (`clpc,t8160` → `AppleCLPC`, `com.apple.driver.AppleT8160CLPC`, build `AppleCLPC-1794.40.23.0.1`) **[DT][KC]**. It holds 197 properties. Power-relevant ones:

- `pkg-lpm-power-target` / `-B` = 0x2000000. Low Power Mode package power target, fixed-point **[INF on units]**.
- `pkg-sustainable-power-target` = 0x36666 and `-B` = 0x4b333. Two sustained-power targets, "B" variant **[INF: A/B correspond to configurations such as folded vs unfolded or the two SoC bins; not stated]**.
- `pkg-avg-max-power` / `pkg-lowpeak-max-power` = 0x38d9db; `pkg-peak-power-target-tc`; `pkg-avg-therm-power-target-tc`.
- `pkg-power-limit-spl-*` and `dram-power-limit-spl-*` (per-tier limits for CPU and GPU).
- `cpu-low-power-frequency-max` = 0x96c (2412 MHz) and `cpu-upo-frequency-min-e` = 0x45c (1116 MHz) **[DT; MHz units INF]**.
- `carplay-power-limit`, `thermal-interval-ms = 12`, `sampling-interval-ms = 4`.
- CLPC's PTD interrupt lanes: `aon-ptd` IRQs `RT0p`, `PCR2/3/4`, `DCR0/1/2` (`interrupts` 4ccs), and `function-lostperf_report_write = <aon-ptd 'WdtpPLSO' 2>`.

ApplePMP calls `AppleCLPC setAETSMaxControlEffortFunction` **[KC]**.

---

## 8. Peak power, brownout and the PTD fabric

### 8.1 aon-ptd

`/arm-io/aon-ptd` (`compatible "ptd,v1"`, 32 IRQs 0x269–0x288, MMIO 0x8c840000/0x8c850000/0x8c858000/0x8c860000) is an always-on interrupt and message lane block **[DT]**. The PMP's `ptd-range` names lanes for `SMC-TO-PPM`, `PPM-TO-SMC`, `PMU-TO-CLPC`, `CLPC-TO-SMC`, `GFX-TO-SMC`, `FAST-DIE-TO-SMC`, `MEMC-TO-SMC`, `PMU-TO-GFX`, `LTS-TO-GFX`, `LTS-VOLT-CAP`, `DVFS-CEIL`, `FAST-DIE-CE`, `SOC-DEV-*`, `PMS-*`, `AVD-NRG`, `SOC-AON-NRG` and `SOC-REST-NRG` **[DT]**. This is the hardware path that lets the PMU, SMC, PPM, CLPC and GPU exchange power budgets and droop warnings without waking the AP. BTM's `btm0..3` interrupts and CLPC's lanes land here **[DT]**.

### 8.2 PPM / CPMS

`/arm-io/pmgr/ppm`: `compatible "ppm,iphoneacsk"`, `acsk-subtarget = 6` → `ApplePPMCPMSv2` (`com.apple.driver.AppleiPhoneACSKPPM` 3.0) **[DT][KC]**. Properties **[DT]**:

- **Batteries:** `number-of-battery-packs = 2`, `btm-enabled = 1`, `battery-data-input-source = 0`, `enable-aging-model = 1`, `model-param-max-Qmax`, `model-param-max-resistance`, `model-param-temp-coeff-thresh = -40000`, and `cpms-batt-model-1ms/100ms/1s-fallback` (880-byte tables) with `fallback-table-low-temp = -15`, `fallback-table-row-count = 11`.
- **Peak power:** `en-peak-power-envelope = 1`, `predictive-horizon-pmax`, `flag-pmax-ilim = 1`, `dynamic-Pmax-Vcut-enabled = 1`, `dynamic-PMU-Vthr-enabled = 1`, `delta-voltage-target-Vdroop = 25`, `delta-voltage-target-Pmax = 75`, `current-limit-threshold`, `enable-IR-compensation = 1`, `rdc-cap-enabled = 1`, `cpms-pmax-computed-rdc = 1`, `PMU-pmax-sampling-enabled = 1`, `auto-rate-change = 1`.
- **CPMS inputs:** `cpms-input-Ps/Pu-cutoff-voltage = 0x34000`, `cpms-policy-type = 2`, `cpms-use-centralized-data = 1`, `cpms-use-lpem-data = 1`.
- **Clients:** `clients_extra` names a `strobe` client (camera flash) with budget/power extras. `separate-thermal-budget-adds = [1 7 9 0xa]`.
- **SMC link:** `smc-interface-comm-enabled = 1`, `continuous-NAND-client = 1`.
- **BTM hooks:** `function-btm-config/-config-battfw/-start/-stop/-vthr`.

Kernel classes: `ApplePPMCPMS`, `ApplePPMCPMSPeakPowerEnvelope`, `ApplePPMDroopController`, `AppleSetDroopUtilizationControlEffortFunction`, `ApplePMUFWDSetCPMSVDDDroopThreshold`, `BrownoutRiskEngaged`, `AverageUPOAvoidance`. There is a `peakpowermanagerd` user client ("Failed to send telemetry to the peakpowermanagerd", shared memory via `IOConnectMapMemory`). `AGXPeakPowerManager` and `AHSFunctionSetPeakPowerBudget` let the GPU and haptics/audio take budgets **[KC]**.

**How brownout prevention works (synthesized)** **[INF from all of the above]**:

1. PPM keeps an impedance and Qmax model per pack (fed by BTM and gas-gauge data, aged by `enable-aging-model`).
2. From that model it computes how much power the batteries can deliver over 1 ms, 100 ms and 1 s horizons before VDD_MAIN would fall to the cutoff (`Ps`, `Pu`).
3. It hands those budgets to CLPC, GPU, camera strobe and audio/haptics through PTD lanes.
4. It programs the PMU's fast droop threshold (`Vthr`) through BTM. If the threshold trips, the PMU raises a throttle IRQ that pmgr routes straight to CPU/GPU throttle triggers (`NUB_SPMI0_THROTTLE_IRQ_SELECTED*`, `PCPU_THROTTLE_EXT_TRIG*`) within microseconds.
5. Only if that fails does the PMU's own `uv,vddmain_uvlo` cut power, which shows up later as a UPO with `ShutDown*` data in the battery kext.

"Peak performance capability" in Settings → Battery Health is the user-visible face of this model **[PUB/INF]**.

---

## 9. Thermal: sensors, loops, throttling, vapor chamber

**Sensors**:

- **SoC die**: PMP-owned temperature sensors listed per SoC bin in `:borneo_h19p_2/temp-sensor` (28 entries: `Ta00000i … Ta00118i`, `Te00005i`, `Te0000ai`, `Tp00002i … Tp00018i`, `MTR_TOP_AGX`) and `:borneo_h19a_2/temp-sensor` (22 entries) **[DT]**. `sochot-sensors` lists 28 (h19p) or 22 (h19a) sensor indices that can assert SOCHOT. `fast-die-ctrl-ts`, `fast-die-ctrl-ts-avg-temp` and `lts-ctrl-ts` set loop rates **[DT]**. TVM (thermal voltage monitor) perf counters exist for SOC, AVE, DCS, DISP and LOW regions **[DT pmgr perf-counters]**. The `AppleEmbeddedTempSensor` kext carries families up to t8030 only. None of its names match a t8160 node here, so die temperature reaches the kernel through PMP (`ApplePMPThermal`) **[KC/DT; INF]**.
- **Board/skin**: `smctempsensor0` (three SMC keys, 1 s poll) → `AppleSMCSensorDispatcher` **[DT][KC]**. The battery kext publishes `SkinTemperature`, `SkinTemperatureVirtual`, `VirtualTemperature`, `SKTMData` **[KC]**.
- **Battery**: three BMU thermistors per pack (`BatteryTemperatureBmuTs1/2/3`), plus `ntc_shdn` at the PMU **[KC][DT]**.
- **PMU die**: `ot,tdie_overtemp_idx0..4`, `temp_abs_buck0/1` **[DT]**.
- **Haptics**: `audio-haptic/function-thermal_budget`, `thermal-budget-range` **[DT]**.
- **Baseband**: `smc-thermal-report-version = 3` **[DT]**.

**Control layers**, fast to slow:

1. PMU hard limits.
2. SOCHOT0/1 pins (`SOCHOT0_L`, `SOCHOT1_L` perf counters).
3. PMP fast-die loop (`LTS_CTRL: Fast Die Throttling`).
4. CLPC thermal budget (`thermal-interval-ms 12`, `pkg-avg-therm-power-target-tc`).
5. SMC thermal management of charging (`TimeChargingThermallyLimited`, wireless "too hot").
6. Userland `thermalmonitord`, which sets thermal pressure levels and backlight/charging mitigations.

The throttle trigger matrix in `pmgr-child` covers PCPU, ECPU, GPU, ANE, DRAM, SOC and C1PPT, each with `SW`/`HW`/`ADCLK`/`DITHER`/`PPT`/`EXT0-3` triggers **[DT]**.

**Vapor chamber**: Apple says the Duo has a custom-designed vapor chamber, with the A20 Pro on the main board on that side. Coverage claims about 35% better sustained performance than iPhone 17 Pro ([ithinkdiff](https://www.ithinkdiff.com/iphone-duo-vapor-chamber-thermal-design/), [MacRumors](https://macrumors.com/2026/10/24/iphone-duo-teardown-videos/)) **[PUB]**. It is passive and invisible to software. Its effect appears only as the CLPC sustained-power constants (`pkg-sustainable-power-target`) **[INF]**.

---

## 10. Userland

The iOS daemons themselves are not in the shared cache; their executables live on the system volume, which is not part of this evidence. Daemon names below come from strings in frameworks and the kernel.

| Component | Evidence | Role |
|---|---|---|
| `powerd` | Not verified in this evidence. The cache search was interrupted when the cache was deleted. | Conventionally the IOPS / `IOPMPowerSource` consumer: battery state, sleep/wake, Low Power Mode assertions **[INF]** |
| `thermalmonitord` | Name string present in DSC subcaches `.01` and `.79.dyldlinkedit` (raw byte search; owning image not resolved) | Thermal pressure / `ProcessInfo.thermalState` **[DSC name only; role INF]** |
| `peakpowermanagerd` | KC user-client strings ("Failed to send telemetry to the peakpowermanagerd"); name also in DSC subcaches `.01`/`.42` | Userland side of PPM telemetry and budgets **[KC][DSC]** |
| `batteryintelligenced` | Name in DSC subcaches `.01`/`.48`; `BatteryIntelligence.framework` in image list | Charging-habit / time-to-full modelling (optimized charging, charge limits) **[DSC name; role INF]** |
| (unknown images) | `RebalanceData`, `OPDDualChargerState`, `IPDRatio` byte-found in DSC subcaches `.34`, `.44`, `.63` (owning images not resolved) | Userland already consumes the dual-pack/dual-charger keys **[DSC; INF]** |
| `BatteryKit`, `BatteryAlgorithms`, `BatteryCenter`, `BatteryCenterUI`, `BatteryDischarge`, `PowerUI`, `PowerExperience`, `LowPowerMode`, `LowPowerModule` (Control Center), `PowerLog*`, `PerfPowerServices*` | DSC image list **[DSC]** | Battery UI, widget, Settings → Battery, CC toggle, powerlog |
| PowerlogCore / PowerlogLite/HelperdOperators | `BatteryPackCount` string; `-[PLBatteryAgent setBatteryPackCount:]` **[DSC]** | Powerlog already models multiple packs |

Public APIs: `UIDevice.batteryLevel` / `batteryState`, `ProcessInfo.isLowPowerModeEnabled` + `NSProcessInfoPowerStateDidChange`, `ProcessInfo.thermalState`, `IOPSCopyPowerSourcesInfo` (IOKit, limited on iOS). None of these expose per-pack data. The two packs are merged into one percentage below the API surface **[INF]**.

Kernel gates: `com.apple.private.powersource-read`, `com.apple.private.powersource-write(-all)`, `com.apple.private.gasgauge-update`, `com.apple.private.applesmartbattery-smcdatastream` **[KC]**.

---

## 11. End to end: plug in a 60 W USB-C PD charger → two cells charge → UI percentage

```mermaid
sequenceDiagram
  participant Ch as 60W PD charger
  participant HPM as spmi-hpm0 (port ctrl)
  participant SMC as SMC (t8160smc)
  participant PMU as PMU becketts/fairmont
  participant G1 as BMU (pack 1)
  participant G2 as BMU2 (pack 2)
  participant K as AppleSmartBattery (kernel)
  participant PPM as ApplePPMCPMSv2 / BTM
  participant U as powerd → SpringBoard / BatteryCenter
  Ch->>HPM: VBUS 5V, CC attach
  HPM->>SMC: attach / VBUS detect (SMC key VBUS, smc-pmu gpio11 "charger")
  HPM->>Ch: PD: Source_Capabilities ← Request (RDO) → Accept/PS_RDY
  HPM-->>K: AppleHPMARMSPMI port event; PortController* telemetry via SMC
  SMC->>SMC: pick charger path(s), IPD ratio between pack chargers
  SMC->>G1: read SOC/temp/Vcell (SMC-side bus)
  SMC->>G2: read SOC/temp/Vcell
  SMC->>PMU: adjust input limit / VDD_MAIN
  SMC-->>K: notify (adapter details, ChargerVBus0/1, IsCharging)
  K->>PPM: per-pack temp/DOD/chem → impedance (kPPMOutImpdDataR0)
  PPM-->>K: impedance array
  K->>SMC: write impedance key → rebalance between packs
  K-->>U: IOPMPowerSource property change (CurrentCapacity, IsCharging, uiSOC)
  U->>U: battery icon / lightning bolt / % on both displays
```

Step by step, with confidence:

1. **Attach.** The CC pins and VBUS reach the USB-C controller `spmi-hpm0`. The PMU learns VBUS through `function-get_vbus_detect` = SMC key `VBUS` **[DT]**. The SMC sees the charger event on its PMU GPIO 11 (`event_name-gpio11 = "charger"`) **[DT]**.
2. **PD negotiation** runs in the port controller's firmware. Contract details (`PortControllerActiveContractRdo`, PDO counts, EPR PDOs) are mirrored into SMC keys and read by `AppleSmartBattery::readPortControllerInfo` / `readAdapterInfo` **[KC]**. The 60 W figure itself is **[PUB]**.
3. **Charge control.** The SMC decides charge current per path. Evidence: `ChargerCount`, `ChargerVBus0/1`, `IPDRatio`, `ChargerPathSelected`, `OPDDualChargerState`, `NotChargingReason`, `SlowChargingReason`, and thermal limiting `TimeChargingThermallyLimited` **[KC]**. The PMU is told new input limits **[INF]**.
4. **Gas gauging.** Each pack's BMU (Volchok firmware for the detected chemistry) measures voltage, current and temperature and computes Qmax, RSS and SOC. The SMC polls both and exposes them as keys **[FW/KC; transport INF]**.
5. **Rebalancing.** `AppleSmartBatteryPack::updateRebalanceData` asks PPM for each pack's impedance and writes it back to the SMC. The SMC's rebalancer moves charge between halves through a bypass FET (`RebalanceHWBypassFETStatus`) with inrush monitoring **[KC]**.
6. **Kernel publish.** `AppleSmartBattery` (the `IOPMPowerSource`) polls ("Starting poll type %d") and publishes `CurrentCapacity`, `MaxCapacity`, `IsCharging`, `ExternalConnected`, `AdapterDetails` and `uiSOC` **[KC]**.
7. **UI.** `powerd` and IOPS clients see the property change. SpringBoard / BatteryCenter renders the percentage and charging glyph on whichever panel is active, and the iOS public APIs fire `UIDeviceBatteryLevelDidChange` **[INF; daemon binaries not in evidence]**. The displayed percentage is the merged, smoothed `UISoc`, not either pack's raw SOC (`AppleRawCurrentCapacity` vs `CurrentCapacity`; `iMaxAndSocSmoothTable`) **[KC; INF]**.

---

## 12. Battery health

- **Data sources:** per-pack `Qmax`, `NominalChargeCapacity`, `CycleCount`, `LifetimeData`, `BatteryHealthMetric`, `BatteryHealthData` (`BatteryHealthMaxCapacity`, `BatteryHealthServiceOption`, `BatteryHealthServiceFlags`), `PermanentFailureStatus` ("Permanent Battery Failure"), and error conditions "Vbatt Fault", "Ibatt MinFault", "Charger Communication Failure", "Cell Check Fault", "Charged Too Long" **[KC]**.
- **Authenticity:** `AppleBatteryAuth` / `AppleBeadsBatteryAuth` per pack **[KC]**.
- **Updates:** `AppleGasGaugeUpdate` (`read UID`, `read nonce`, `start update`, signature1/2, `commit image`) carries the personalized Volchok images to each BMU through SMC data and control keys **[KC][FW]**.
- **UI:** Settings → Battery → Battery Health (BatteryCenter / BatteryKit / PowerUI) **[DSC]**. How Apple merges two packs' health into one "Maximum Capacity" is not visible in these sources **[gap]**.

---

## 13. Gaps and limits

- **SMC firmware** `t8160smc` (DT `firmware-name`, `pre-loaded = 0`) is not present under that name in the IPSW, the BuildManifest, the kernelcache or iBoot strings that I checked. Its location (embedded compressed in another image, or in a component I did not decompress) is unresolved. So the SMC key map (which keys carry pack, charger and rebalance data) is not recoverable here. The kernel log formats print keys as `%c%c%c%c`, so the names are runtime-only.
- **Charger and gauge physical buses:** behind the SMC, so not in the AP device tree. Chip vendors and part numbers for the charger(s), gauges, BPIC (`stonehenge`), `shamisen`, PMUs (`becketts`, `fairmont`) and port controller (`cbtl1702`) are Apple code names only.
- **Rail map:** the DT gives SoC rails (DCS/SOC/DISP/AVE plus CPU/GPU domains) and PMU fault names for some LDOs and bucks. It gives no voltages, current limits, or buck-to-rail assignments. Those live in PMU firmware (inside iBoot) and Apple-internal schematics.
- **Hinge power path:** which conductors cross the hinge (VBUS vs VBAT bus vs flex) is not knowable from software. Teardown photos are the only source.
- **Units:** many CLPC and PPM constants are fixed-point. I give raw values and do not convert, except where noted as **[INF]**.
- **Userland daemons** (`powerd`, `thermalmonitord`, `batteryintelligenced`, `peakpowermanagerd`) are outside the shared cache. Their logic is not analysed here. The shared cache was deleted mid-session, so the [DSC] facts here are limited to the image list, the `BatteryPackCount` hits (PowerlogCore, PowerlogLiteOperators, PowerlogHelperdOperators, `-[PLBatteryAgent setBatteryPackCount:]`) and raw subcache byte matches. Which framework consumes `RebalanceData`/`IPDRatio`, how BatteryCenter shows one merged percentage for two packs, and how Low Power Mode maps to CLPC `pkg-lpm-power-target` are not determined.
- **SoC bin:** whether this unit uses the `h19p` or `h19a` thermal tables is decided by iBoot at boot and is not in the static DT.
- **Two "B" CLPC targets** (`pkg-sustainable-power-target-B`, `pkg-lpm-power-target-B`): the selection condition is not stated.
- Nothing here is register-level. No PMU register addresses beyond those the DT itself exposes are given or implied.

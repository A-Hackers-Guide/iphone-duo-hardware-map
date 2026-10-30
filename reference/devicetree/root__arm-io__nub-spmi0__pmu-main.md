# `/arm-io/nub-spmi0/pmu-main`

- Name: `pmu-main`
- Parent: [`/arm-io/nub-spmi0`](root__arm-io__nub-spmi0.md)
- phandle: `198`
- compatible: `pmu,spmi`, `pmu,becketts`
- Children (1): [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main`](root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `ApplePMUFirmwareDriver` | `AppleARMSPMIDevice` | [`com.apple.driver.ApplePMUFirmwareDriver`](../kexts/com.apple.driver.ApplePMUFirmwareDriver.md) | `pmu,spmi` |
| `AppleDialogSPMIPMU` | `AppleARMSPMIDevice` | [`com.apple.driver.AppleSPMIPMU`](../kexts/com.apple.driver.AppleSPMIPMU.md) | `pmu,spmi` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x0` | `0x30000000e` (12,884,901,902 B) | not memory-mapped (bus address) |
| 1 | `0x0` | `0x400000000` (17,179,869,184 B) | not memory-mapped (bus address) |
| 2 | `0x0` | `0x0` (0 B) | not memory-mapped (bus address) |

## Interrupts [DT]

Controller: [`/arm-io/nub-spmi0`](root__arm-io__nub-spmi0.md)

`2, 62`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `get_pdod` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `keyR` | `0x42444431` |
| `get_vbus_detect` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `keyR` | `0x56425553` |
| `external_standby` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `keyW` | `0x4d425345` |

## Referenced by (1) [DT]

- [`/arm-io/pmgr/pmgrtools`](root__arm-io__pmgr__pmgrtools.md): function-pmuaccess_L1DY `pmuR`

## All properties (127) [DT]

- **`AAPL,phandle`**: `198` (`0xc6`) → phandle of [`/arm-io/nub-spmi0/pmu-main`](root__arm-io__nub-spmi0__pmu-main.md)
- **`compatible`**: `pmu,spmi`, `pmu,becketts`
- **`function-external_standby`**: 12 bytes
  - u32: `0x9f 0x6b657957 0x4d425345`
  - text inside: `WyekESBM`
  ```
  000000  9f 00 00 00 57 79 65 6b 45 53 42 4d              ....WyekESBM
  ```
- **`function-get_pdod`**: 12 bytes
  - u32: `0x9f 0x6b657952 0x42444431`
  - text inside: `Ryek1DDB`
  ```
  000000  9f 00 00 00 52 79 65 6b 31 44 44 42              ....Ryek1DDB
  ```
- **`function-get_vbus_detect`**: 12 bytes
  - u32: `0x9f 0x6b657952 0x56425553`
  - text inside: `RyekSUBV`
  ```
  000000  9f 00 00 00 52 79 65 6b 53 55 42 56              ....RyekSUBV
  ```
- **`fw-host-irq-address`**: `11016` (`0x2b08`)
- **`fw-mcom-address`**: `11104` (`0x2b60`)
- **`fw-mcom-int-index`**: `1` (`0x1`)
- **`general-config`**: `0x4000000c800` (u64; as two u32: `0xc800`, `0x400`)
- **`has-fw`**: `1` (`0x1`)
- **`has-lpem-fw-scc`**: `1` (`0x1`)
- **`hw-name`**: `becketts`
- **`info-clock_offset`**: `0x600002100` (u64; as two u32: `0x2100`, `0x6`)
- **`info-fault_log`**: `0x900001000` (u64; as two u32: `0x1000`, `0x9`)
- **`info-fault_name-10`**: `ot,overtemp`
- **`info-fault_name-11`**: `ov,vddmain_ovlo`
- **`info-fault_name-16`**: `btn_rst,two_finger_rst`
- **`info-fault_name-17`**: `crash,crash0_in`
- **`info-fault_name-18`**: `btn_rst,btn_seq_reset`
- **`info-fault_name-19`**: `btn_rst,sec_btn_seq`
- **`info-fault_name-20`**: `wdog,reset_in_1`
- **`info-fault_name-21`**: `dbg_rst,reset_in_2`
- **`info-fault_name-22`**: `sochot,reset_in_3`
- **`info-fault_name-23`**: `rst_in,reset_in_1_deassert`
- **`info-fault_name-24`**: `spmi,spmi_fault`
- **`info-fault_name-25`**: `ntc_shdn`
- **`info-fault_name-26`**: `timeout,dblclick_timeout`
- **`info-fault_name-28`**: `timeout,watchdog_timeout`
- **`info-fault_name-29`**: `sstate,button_dfu_recover`
- **`info-fault_name-3`**: `uv,vddmain_uvlo`
- **`info-fault_name-30`**: `crash,crash1_in`
- **`info-fault_name-31`**: `sstate,dfu_btn_seq_reset`
- **`info-fault_name-32`**: `temp_abs_buck0`
- **`info-fault_name-33`**: `temp_abs_buck1`
- **`info-fault_name-35`**: `otp_crc`
- **`info-fault_name-36`**: `sgpio`
- **`info-fault_name-37`**: `btn_shdn`
- **`info-fault_name-38`**: `xtal_wdog_expiry`
- **`info-fault_name-39`**: `mfsm_sgpio`
- **`info-fault_name-40`**: `crash,metis_fw_crash`
- **`info-fault_name-41`**: `crash,metis_hw_crash`
- **`info-fault_name-42`**: `timeout,target_st_wdog_timeout`
- **`info-fault_name-43`**: `timeout,wdog_fw_timeout`
- **`info-fault_name-44`**: `emerg_shdn`
- **`info-fault_name-5`**: `uv,vdd_boost_uvlo`
- **`info-fault_name-50`**: `target_off_restart`
- **`info-fault_name-51`**: `target_off_shutdown`
- **`info-fault_name-52`**: `target_off_conflict`
- **`info-fault_name-56`**: `ot,tdie_overtemp_idx0`
- **`info-fault_name-57`**: `ot,tdie_overtemp_idx1`
- **`info-fault_name-58`**: `ot,tdie_overtemp_idx2`
- **`info-fault_name-59`**: `ot,tdie_overtemp_idx3`
- **`info-fault_name-6`**: `ov,vdd_boost_ovlo`
- **`info-fault_name-60`**: `ot,tdie_overtemp_idx4`
- **`info-fault_name-61`**: `ot,tdie_overtemp`
- **`info-fault_name-62`**: `ov,ldo_ana_ovp`
- **`info-fault_name-63`**: `ov,ldo_dig_ovp`
- **`info-fault_name-64`**: `uv,cp_uvlo`
- **`info-fault_name-65`**: `ov,cp_ovlo`
- **`info-fault_name-66`**: `cp_wdog_expiry`
- **`info-fault_name-67`**: `uv,ldo9_uv`
- **`info-fault_name-68`**: `ov,ldo9_ov`
- **`info-fault_name-69`**: `uv,ldo9b_uv`
- **`info-fault_name-70`**: `ov,ldo9b_ov`
- **`info-fault_name-71`**: `ov,cpneg_dvc`
- **`info-fault_name-8`**: `por`
- **`info-fault_name-9`**: `rst`
- **`info-has_phra`**: `1` (`0x1`)
- **`info-id`**: `0xa00000000` (u64; as two u32: `0x0`, `0xa`)
- **`info-leg_scrpad`**: `63488` (`0xf800`)
- **`info-o2ws_name-0`**: `fw_nonsec_off_wakeup_csr`
- **`info-o2ws_name-1`**: `gcb_off_wakeup`
- **`info-o2ws_name-10`**: `target_state_wdog_timeout`
- **`info-o2ws_name-11`**: `pgood_wdog_to_error_wakeup`
- **`info-o2ws_name-12`**: `wake2lf_negedge`
- **`info-o2ws_name-13`**: `fw_nonsec_off_wakeup_wdog`
- **`info-o2ws_name-14`**: `fw_req_auto_wakeup`
- **`info-o2ws_name-2`**: `gcb_wakeup`
- **`info-o2ws_name-3`**: `rtc_alarm_wakeup`
- **`info-o2ws_name-4`**: `auto_wakeup`
- **`info-o2ws_name-5`**: `gcb_crash_wakeup`
- **`info-o2ws_name-6`**: `hw_wdog_wakeup`
- **`info-o2ws_name-7`**: `fw_wdog_wakeup`
- **`info-o2ws_name-8`**: `dft_ctrl2_wakeup`
- **`info-o2ws_name-9`**: `pgood_wdog_to_off_wakeup`
- **`info-off2wake_source`**: `0x20000281b` (u64; as two u32: `0x281b`, `0x2`)
- **`info-rtc`**: `8194` (`0x2002`)
- **`info-rtc_alarm_ctrl`**: `8192` (`0x2000`)
- **`info-rtc_alarm_ctrl_en_mask`**: `64` (`0x40`)
- **`info-rtc_alarm_event`**: `8192` (`0x2000`)
- **`info-rtc_alarm_event_mask`**: `2` (`0x2`)
- **`info-rtc_alarm_mask`**: `1` (`0x1`)
- **`info-rtc_alarm_monitor_mask`**: `1` (`0x1`)
- **`info-rtc_alarm_offset`**: `8200` (`0x2008`)
- **`info-rtc_irq_mask_offset`**: `8206` (`0x200e`)
- **`info-rtc_scrpad`**: `8448` (`0x2100`)
- **`info-scrpad`**: `0x280000008000` (u64; as two u32: `0x8000`, `0x2800`)
- **`info-scrpad_lpm_ctrl`**: `42972` (`0xa7dc`)
- **`info-scrpad_lpm_log`**: `42880` (`0xa780`)
- **`info-scrpad_socd`**: `0x80000008b00` (u64; as two u32: `0x8b00`, `0x800`)
- **`interrupt-parent`**: `197` (`0xc5`) → phandle of [`/arm-io/nub-spmi0`](root__arm-io__nub-spmi0.md)
- **`interrupts`**: `0x3e00000002` (u64; as two u32: `0x2`, `0x3e`)
- **`is-primary`**: `1` (`0x1`)
- **`name`**: `pmu-main`
- **`ptmu-region-0-data`**: `0x400000c000` (u64; as two u32: `0xc000`, `0x40`)
- **`ptmu-region-1-data`**: `0x400000c040` (u64; as two u32: `0xc040`, `0x40`)
- **`ptmu-region-10-data`**: `0x800000c300` (u64; as two u32: `0xc300`, `0x80`)
- **`ptmu-region-11-data`**: `0x800000c380` (u64; as two u32: `0xc380`, `0x80`)
- **`ptmu-region-12-data`**: `0x2000000c400` (u64; as two u32: `0xc400`, `0x200`)
- **`ptmu-region-13-data`**: `0x2000000c600` (u64; as two u32: `0xc600`, `0x200`)
- **`ptmu-region-14-data`**: `0x4000000c800` (u64; as two u32: `0xc800`, `0x400`)
- **`ptmu-region-15-data`**: `0x4000000cc00` (u64; as two u32: `0xcc00`, `0x400`)
- **`ptmu-region-2-data`**: `0x400000c080` (u64; as two u32: `0xc080`, `0x40`)
- **`ptmu-region-3-data`**: `0x400000c0c0` (u64; as two u32: `0xc0c0`, `0x40`)
- **`ptmu-region-4-data`**: `0x400000c100` (u64; as two u32: `0xc100`, `0x40`)
- **`ptmu-region-5-data`**: `0x400000c140` (u64; as two u32: `0xc140`, `0x40`)
- **`ptmu-region-6-data`**: `0x400000c180` (u64; as two u32: `0xc180`, `0x40`)
- **`ptmu-region-7-data`**: `0x400000c1c0` (u64; as two u32: `0xc1c0`, `0x40`)
- **`ptmu-region-8-data`**: `0x800000c200` (u64; as two u32: `0xc200`, `0x80`)
- **`ptmu-region-9-data`**: `0x800000c280` (u64; as two u32: `0xc280`, `0x80`)
- **`ptmu-secure-region-0-data`**: `0x4000000b000` (u64; as two u32: `0xb000`, `0x400`)
- **`ptmu-secure-region-1-data`**: `0x4000000b400` (u64; as two u32: `0xb400`, `0x400`)
- **`ptmu-secure-region-2-data`**: `0x4000000b800` (u64; as two u32: `0xb800`, `0x400`)
- **`ptmu-secure-region-3-data`**: `0x2000000bc00` (u64; as two u32: `0xbc00`, `0x200`)
- **`ptmu-secure-region-4-data`**: `0x2000000be00` (u64; as two u32: `0xbe00`, `0x200`)
- **`reg`**: 24 bytes
  - u32: `0xe 0x3 0x0 0x4 0x0 0x0`
  ```
  000000  0e 00 00 00 03 00 00 00 00 00 00 00 04 00 00 00  ................
  000010  00 00 00 00 00 00 00 00                          ........
  ```
- **`upo-shutdown-delay`**: `0` (`0x0`)

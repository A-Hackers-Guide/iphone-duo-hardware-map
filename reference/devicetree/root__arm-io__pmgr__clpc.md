# `/arm-io/pmgr/clpc`

- Name: `clpc`
- Parent: [`/arm-io/pmgr`](root__arm-io__pmgr.md)
- phandle: `50`
- compatible: `clpc,t8160`
- device_type: `clpc`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleCLPC` | `ApplePMGRNub` | [`com.apple.driver.AppleT8160CLPC`](../kexts/com.apple.driver.AppleT8160CLPC.md) | `clpc,t8160` |

## Interrupts [DT]

Controller: unresolved

`1063, 0, 1882215506, 1380143154, 1380143155, 1380143156, 1380140080, 1380140081, 1380140082`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `clpc_clvr_peek_0` | [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md) | `ptdP` | `0x70305452 0x1` |
| `ane_perf_ctr1` | [`/arm-io/ane1`](root__arm-io__ane1.md) | `ANCR` | `` |
| `lostperf_report_write` | [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md) | `ptdW` | `0x4f534c50 0x2` |
| `ptd_read_mult` | [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md) | `ptMR` | `` |
| `clpc_clvr_read_0` | [`/arm-io/aon-ptd`](root__arm-io__aon-ptd.md) | `ptdR` | `0x70305452 0x80000001` |
| `ane_perf_ctr` | [`/arm-io/ane0`](root__arm-io__ane0.md) | `ANCR` | `` |

## All properties (197) [DT]

- **`AAPL,phandle`**: `50` (`0x32`) → phandle of [`/arm-io/pmgr/clpc`](root__arm-io__pmgr__clpc.md)
- **`ane-utility-max-freq`**: `1404` (`0x57c`)
- **`ane-utilization-ki-down`**: `32768` (`0x8000`)
- **`ane-utilization-ki-up`**: `154009` (`0x25999`)
- **`ane-utilization-kp-down`**: `0` (`0x0`)
- **`ane-utilization-kp-up`**: `0` (`0x0`)
- **`ane-utilization-target`**: `52428` (`0xcccc`)
- **`aon-ptd-int-imm`**: `1380140080` (`0x52434430`) (four-char code `RCD0`)
- **`ca-client-cpu-work-dev-w-down`**: `1090519` (`0x10a3d7`)
- **`ca-client-cpu-work-high-dev`**: `524288` (`0x80000`)
- **`ca-client-cpu-work-high-floor`**: `6553` (`0x1999`)
- **`ca-client-cpu-work-typical-dev`**: `65536` (`0x10000`)
- **`ca-client-cpu-work-window`**: `1426063` (`0x15c28f`)
- **`carplay-power-limit`**: `98304` (`0x18000`)
- **`clpc-dev-intrs-timeout`**: `500000` (`0x7a120`)
- **`compatible`**: `clpc,t8160`
- **`cpu-amx-mem-llc-ld-e-ki-dn`**: `131072` (`0x20000`)
- **`cpu-amx-mem-llc-ld-e-ki-up`**: `1310720` (`0x140000`)
- **`cpu-amx-mem-llc-ld-e-target`**: `5243` (`0x147b`)
- **`cpu-amx-mem-llc-ld-max-rate-e`**: `2928` (`0xb70`)
- **`cpu-avg-limiter-input-tc`**: `248` (`0xf8`)
- **`cpu-avg-limiter-ki`**: `27515` (`0x6b7b`)
- **`cpu-avg-limiter-kp`**: `905970` (`0xdd2f2`)
- **`cpu-avg-limiter-target-tc`**: `0` (`0x0`)
- **`cpu-bg-limiter-enable`**: `1` (`0x1`)
- **`cpu-bg-limiter-target`**: `26214` (`0x6666`)
- **`cpu-core-mask-raise-holdoff`**: `10` (`0xa`)
- **`cpu-dither-res-e-ki-dn`**: `14562` (`0x38e2`)
- **`cpu-dither-res-e-ki-up`**: `43692` (`0xaaac`)
- **`cpu-dither-res-e-target`**: `6553` (`0x1999`)
- **`cpu-dither-res-p-ki-dn`**: `14562` (`0x38e2`)
- **`cpu-dither-res-p-ki-up`**: `43692` (`0xaaac`)
- **`cpu-dither-res-p-target`**: `6553` (`0x1999`)
- **`cpu-dynamic-control`**: `1` (`0x1`)
- **`cpu-dynamic-core-rotation-mode`**: `2` (`0x2`)
- **`cpu-e-step-down-delay-us`**: `500` (`0x1f4`)
- **`cpu-efficiency-ki-down`**: `13107` (`0x3333`)
- **`cpu-efficiency-ki-up`**: `6553` (`0x1999`)
- **`cpu-efficiency-kp-down`**: `0` (`0x0`)
- **`cpu-efficiency-kp-up`**: `0` (`0x0`)
- **`cpu-high-e-threshold-high-e`**: `131072` (`0x20000`)
- **`cpu-high-e-threshold-high-p`**: `720896` (`0xb0000`)
- **`cpu-high-e-threshold-low-e`**: `32768` (`0x8000`)
- **`cpu-high-e-threshold-low-p`**: `327680` (`0x50000`)
- **`cpu-high-epi-threshold-low-e`**: `3932` (`0xf5c`)
- **`cpu-iblm-mode`**: `3` (`0x3`)
- **`cpu-idle-time-grace-period`**: `100` (`0x64`)
- **`cpu-io-lim-min-freq`**: `4500` (`0x1194`)
- **`cpu-low-power-frequency-max`**: `2412` (`0x96c`)
- **`cpu-lowpeak-limiter-input-tc`**: `16` (`0x10`)
- **`cpu-lowpeak-limiter-ki`**: `466407` (`0x71de7`)
- **`cpu-lowpeak-limiter-kp`**: `117441` (`0x1cac1`)
- **`cpu-lowpeak-limiter-target-tc`**: `0` (`0x0`)
- **`cpu-migr-delta-clear-threshold`**: `0` (`0x0`)
- **`cpu-migr-delta-set-threshold`**: `1` (`0x1`)
- **`cpu-migr-mask-update-interval`**: `4` (`0x4`)
- **`cpu-migr-pref-eligible-mask`**: `3` (`0x3`)
- **`cpu-perf-cnt-filter-tc-down`**: `10` (`0xa`)
- **`cpu-perf-cnt-filter-tc-up`**: `10` (`0xa`)
- **`cpu-power-zone-filter-tc-0`**: `120000` (`0x1d4c0`)
- **`cpu-power-zone-target-0`**: `1638400` (`0x190000`)
- **`cpu-power-zone-target-offset-0`**: `6554` (`0x199a`)
- **`cpu-pref-mask-update-interval`**: `4` (`0x4`)
- **`cpu-rot-pwr-disengage-thresh`**: `98304` (`0x18000`)
- **`cpu-rot-pwr-engage-thresh`**: `163840` (`0x28000`)
- **`cpu-sched-lat-nonui-ki-down`**: `3604` (`0xe14`)
- **`cpu-sched-lat-nonui-ki-up`**: `6553` (`0x1999`)
- **`cpu-sched-lat-nonui-kp-down`**: `0` (`0x0`)
- **`cpu-sched-lat-nonui-kp-up`**: `2785` (`0xae1`)
- **`cpu-sched-lat-nonui-target`**: `4000` (`0xfa0`)
- **`cpu-sched-lat-ui-ki-down`**: `14417` (`0x3851`)
- **`cpu-sched-lat-ui-ki-up`**: `26214` (`0x6666`)
- **`cpu-sched-lat-ui-kp-down`**: `0` (`0x0`)
- **`cpu-sched-lat-ui-kp-up`**: `10485` (`0x28f5`)
- **`cpu-sched-lat-ui-target`**: `1000` (`0x3e8`)
- **`cpu-upo-frequency-min-e`**: `1116` (`0x45c`)
- **`cpu-util-sfi-min-on-percent`**: `16384` (`0x4000`)
- **`cpu-utility-limiter-enable`**: `1` (`0x1`)
- **`cpu-utilization-control-mode`**: `3` (`0x3`)
- **`cpu-utilization-ki-down`**: `3276` (`0xccc`)
- **`cpu-utilization-ki-up`**: `655360` (`0xa0000`)
- **`cpu-utilization-kp-down`**: `0` (`0x0`)
- **`cpu-utilization-kp-up`**: `0` (`0x0`)
- **`cpu-utilization-spl-ki-down-c0`**: `3932` (`0xf5c`)
- **`cpu-utilization-spl-ki-down-c1`**: `3932` (`0xf5c`)
- **`cpu-utilization-spl-ki-down-c2`**: `3604` (`0xe14`)
- **`cpu-utilization-spl-ki-down-c3`**: `3604` (`0xe14`)
- **`cpu-utilization-spl-ki-down-c4`**: `13107` (`0x3333`)
- **`cpu-utilization-spl-ki-down-t1`**: `13893` (`0x3645`)
- **`cpu-utilization-spl-ki-down-t2`**: `18219` (`0x472b`)
- **`cpu-utilization-spl-ki-down-t3`**: `52428` (`0xcccc`)
- **`cpu-utilization-spl-ki-up-c0`**: `1376256` (`0x150000`)
- **`cpu-utilization-spl-ki-up-c1`**: `64880` (`0xfd70`)
- **`cpu-utilization-spl-ki-up-c2`**: `1189937` (`0x122831`)
- **`cpu-utilization-spl-ki-up-c3`**: `208601` (`0x32ed9`)
- **`cpu-utilization-spl-ki-up-c4`**: `6553` (`0x1999`)
- **`cpu-utilization-spl-ki-up-t1`**: `12255` (`0x2fdf`)
- **`cpu-utilization-spl-ki-up-t2`**: `16384` (`0x4000`)
- **`cpu-utilization-spl-ki-up-t3`**: `52428` (`0xcccc`)
- **`cpu-utilization-target`**: `64880` (`0xfd70`)
- **`cpu-utilization-tier-mode`**: `2` (`0x2`)
- **`device-curr-used-timeout-ms`**: `5000` (`0x1388`)
- **`device_type`**: `clpc`
- **`dram-power-limit-spl-cpu-c0`**: `65536` (`0x10000`)
- **`dram-power-limit-spl-cpu-c1`**: `39321` (`0x9999`)
- **`dram-power-limit-spl-cpu-c2`**: `19660` (`0x4ccc`)
- **`dram-power-limit-spl-cpu-c3`**: `13107` (`0x3333`)
- **`dram-power-limit-spl-cpu-t1`**: `19660` (`0x4ccc`)
- **`dram-power-limit-spl-cpu-t2`**: `52428` (`0xcccc`)
- **`dram-power-limit-spl-gpu-c0`**: `65536` (`0x10000`)
- **`dram-power-limit-spl-gpu-c1`**: `39321` (`0x9999`)
- **`dram-power-limit-spl-gpu-c2`**: `19660` (`0x4ccc`)
- **`dram-power-limit-spl-gpu-c3`**: `13107` (`0x3333`)
- **`dram-power-limit-spl-gpu-t1`**: `19660` (`0x4ccc`)
- **`dram-power-limit-spl-gpu-t2`**: `52428` (`0xcccc`)
- **`dram-power-limit-spl-t0`**: `0` (`0x0`)
- **`dram-power-limit-spl-t3`**: `65536` (`0x10000`)
- **`fab-compute-power-ratio-high`**: `393216` (`0x60000`)
- **`fab-compute-power-ratio-low`**: `262144` (`0x40000`)
- **`fab-compute-power-target-high`**: `6553` (`0x1999`)
- **`fab-compute-power-target-low`**: `3276` (`0xccc`)
- **`fabric-mem-separation-max`**: `3` (`0x3`)
- **`fabric-perf-state-follows-accp`**: `0` (`0x0`)
- **`function-ane_perf_ctr`**: `0x414e43520000013e` (u64; as two u32: `0x13e`, `0x414e4352`)
- **`function-ane_perf_ctr1`**: `0x414e43520000014a` (u64; as two u32: `0x14a`, `0x414e4352`)
- **`function-clpc_clvr_peek_0`**: 16 bytes
  - u32: `0xa6 0x70746450 0x70305452 0x1`
  - text inside: `PdtpRT0p`
  ```
  000000  a6 00 00 00 50 64 74 70 52 54 30 70 01 00 00 00  ....PdtpRT0p....
  ```
- **`function-clpc_clvr_read_0`**: 16 bytes
  - u32: `0xa6 0x70746452 0x70305452 0x80000001`
  - text inside: `RdtpRT0p`
  ```
  000000  a6 00 00 00 52 64 74 70 52 54 30 70 01 00 00 80  ....RdtpRT0p....
  ```
- **`function-lostperf_report_write`**: 16 bytes
  - u32: `0xa6 0x70746457 0x4f534c50 0x2`
  - text inside: `WdtpPLSO`
  ```
  000000  a6 00 00 00 57 64 74 70 50 4c 53 4f 02 00 00 00  ....WdtpPLSO....
  ```
- **`function-ptd_read_mult`**: `0x70744d52000000a6` (u64; as two u32: `0xa6`, `0x70744d52`)
- **`gpu-unified-budget-interface`**: `1` (`0x1`)
- **`interrupt-parent`**: 36 bytes
  - u32: `0x2d 0x2d 0xa6 0xa6 0xa6 0xa6 0xa6 0xa6 0xa6`
  ```
  000000  2d 00 00 00 2d 00 00 00 a6 00 00 00 a6 00 00 00  -...-...........
  000010  a6 00 00 00 a6 00 00 00 a6 00 00 00 a6 00 00 00  ................
  000020  a6 00 00 00                                      ....
  ```
- **`interrupts`**: 36 bytes
  - u32: `0x427 0x0 0x70305452 0x52435032 0x52435033 0x52435034 0x52434430 0x52434431 0x52434432`
  - text inside: `RT0p2PCR3PCR4PCR0DCR1DCR2DCR`
  ```
  000000  27 04 00 00 00 00 00 00 52 54 30 70 32 50 43 52  '.......RT0p2PCR
  000010  33 50 43 52 34 50 43 52 30 44 43 52 31 44 43 52  3PCR4PCR0DCR1DCR
  000020  32 44 43 52                                      2DCR
  ```
- **`mem-compute-power-ratio-high`**: `393216` (`0x60000`)
- **`mem-compute-power-ratio-low`**: `262144` (`0x40000`)
- **`mem-compute-power-target-high`**: `14745` (`0x3999`)
- **`mem-compute-power-target-low`**: `8192` (`0x2000`)
- **`mem-cpu-stall-amx-thresh-p`**: `60000` (`0xea60`)
- **`mem-cpu-stall-min-effort-c1-p`**: `65536` (`0x10000`)
- **`mem-cpu-stall-min-effort-t1-p`**: `6553` (`0x1999`)
- **`mem-cpu-stall-r-ki-down-c1-p`**: `131072` (`0x20000`)
- **`mem-cpu-stall-r-ki-up-c0-e`**: `3276800` (`0x320000`)
- **`mem-cpu-stall-r-ki-up-c1-e`**: `32768` (`0x8000`)
- **`mem-cpu-stall-r-ki-up-c1-p`**: `19660` (`0x4ccc`)
- **`mem-cpu-stall-r-t1-e`**: `13107` (`0x3333`)
- **`mem-cpu-stall-r-t1-p`**: `42598` (`0xa666`)
- **`mem-cpu-stall-r-target-e`**: `1966` (`0x7ae`)
- **`mem-cpu-stall-r-target2-e`**: `19660` (`0x4ccc`)
- **`mem-cpu-stall-r-target2-p`**: `3276` (`0xccc`)
- **`mem-perf-state-follows-accp`**: `0` (`0x0`)
- **`name`**: `clpc`
- **`pkg-1s-spl-dcs-c0`**: `0` (`0x0`)
- **`pkg-1s-spl-dcs-c1`**: `16384` (`0x4000`)
- **`pkg-1s-spl-dcs-c2`**: `45875` (`0xb333`)
- **`pkg-1s-spl-dcs-c3`**: `65536` (`0x10000`)
- **`pkg-avg-limiter-input-tc`**: `900` (`0x384`)
- **`pkg-avg-limiter-ki`**: `3355` (`0xd1b`)
- **`pkg-avg-limiter-kp`**: `167772` (`0x28f5c`)
- **`pkg-avg-limiter-target-tc`**: `0` (`0x0`)
- **`pkg-avg-max-power`**: `3725787` (`0x38d9db`)
- **`pkg-avg-therm-power-target-tc`**: `250` (`0xfa`)
- **`pkg-dynamic-split-mode`**: `2` (`0x2`)
- **`pkg-dynamic-split-seed-on`**: `1` (`0x1`)
- **`pkg-low-power-target-tc`**: `100` (`0x64`)
- **`pkg-lowpeak-limiter-input-tc`**: `60` (`0x3c`)
- **`pkg-lowpeak-limiter-ki`**: `38588` (`0x96bc`)
- **`pkg-lowpeak-limiter-kp`**: `119118` (`0x1d14e`)
- **`pkg-lowpeak-limiter-target-tc`**: `0` (`0x0`)
- **`pkg-lowpeak-max-power`**: `3725787` (`0x38d9db`)
- **`pkg-lpm-power-target`**: `33554432` (`0x2000000`)
- **`pkg-lpm-power-target-B`**: `33554432` (`0x2000000`)
- **`pkg-peak-power-target-tc`**: `10` (`0xa`)
- **`pkg-power-limit-is-effort`**: `1` (`0x1`)
- **`pkg-power-limit-spl-cpu-c0`**: `0` (`0x0`)
- **`pkg-power-limit-spl-cpu-t1`**: `1530921` (`0x175c29`)
- **`pkg-power-limit-spl-cpu-t2`**: `1530921` (`0x175c29`)
- **`pkg-power-limit-spl-gpu-c0`**: `0` (`0x0`)
- **`pkg-power-limit-spl-gpu-t1`**: `1530921` (`0x175c29`)
- **`pkg-power-limit-spl-gpu-t2`**: `1530921` (`0x175c29`)
- **`pkg-power-limit-spl-t0`**: `204472` (`0x31eb8`)
- **`pkg-power-limit-spl-t3`**: `1530921` (`0x175c29`)
- **`pkg-power-zone-filter-tc-0`**: `60000` (`0xea60`)
- **`pkg-power-zone-target-0`**: `16711680` (`0xff0000`)
- **`pkg-power-zone-target-offset-0`**: `6554` (`0x199a`)
- **`pkg-sustainable-power-target`**: `222822` (`0x36666`)
- **`pkg-sustainable-power-target-B`**: `308019` (`0x4b333`)
- **`ptd-ranges`**: `0x410000001f` (u64; as two u32: `0x1f`, `0x41`)
- **`sampling-interval-ms`**: `4` (`0x4`)
- **`soc-devices`**: 16 bytes
  - u32: `0x3 0x4 0x6 0x7`
  ```
  000000  03 00 00 00 04 00 00 00 06 00 00 00 07 00 00 00  ................
  ```
- **`sptm-allow-reg`**: 48 bytes
  - u32: `0x8c840000 0x0 0x40000 0x0 0x80210000 0x0 0x10000 0x0 0x803c0000 0x0 0x40000 0x0`
  ```
  000000  00 00 84 8c 00 00 00 00 00 00 04 00 00 00 00 00  ................
  000010  00 00 21 80 00 00 00 00 00 00 01 00 00 00 00 00  ..!.............
  000020  00 00 3c 80 00 00 00 00 00 00 04 00 00 00 00 00  ..<.............
  ```
- **`system-utilization-gpu-in-en`**: `1` (`0x1`)
- **`system-utilization-gpu-out-en`**: `1` (`0x1`)
- **`thermal-interval-ms`**: `12` (`0xc`)
- **`ui-present-boost-constraint-us`**: `3000` (`0xbb8`)
- **`ui-present-constraint-min-us`**: `2000` (`0x7d0`)
- **`ui-present-cpu-work-high-floor`**: `6553` (`0x1999`)
- **`ui-present-util-target-l0s`**: `58982` (`0xe666`)
- **`ui-present-util-target-l1s`**: `58982` (`0xe666`)

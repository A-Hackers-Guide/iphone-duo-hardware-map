# Function references

Apple device trees wire one block to another with `function-<name>` properties: `<provider phandle> <four-char code> <args…>`. Codes are stored little-endian; the readable order is shown. This is the board's control wiring as software sees it: which PMU rail, GPIO, reset or power gate each device uses. **[DT]**

| Consumer | Function | Provider | Code | Arguments |
|---|---|---|---|---|
| [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) | `error_handler` | [`/arm-io`](../devicetree/root__arm-io.md) | `ErrH` | `0x0` |
| [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) | `enable_core` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `Core` | `0x1` |
| [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) | `cpu_idle` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `cpuI` | `` |
| [`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) | `error_handler` | [`/arm-io`](../devicetree/root__arm-io.md) | `ErrH` | `0x1` |
| [`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) | `enable_core` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `Core` | `0x2` |
| [`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) | `cpu_idle` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `cpuI` | `` |
| [`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) | `error_handler` | [`/arm-io`](../devicetree/root__arm-io.md) | `ErrH` | `0x2` |
| [`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) | `enable_core` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `Core` | `0x4` |
| [`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) | `cpu_idle` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `cpuI` | `` |
| [`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) | `error_handler` | [`/arm-io`](../devicetree/root__arm-io.md) | `ErrH` | `0x3` |
| [`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) | `enable_core` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `Core` | `0x8` |
| [`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) | `cpu_idle` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `cpuI` | `` |
| [`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) | `error_handler` | [`/arm-io`](../devicetree/root__arm-io.md) | `ErrH` | `0x6` |
| [`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) | `enable_core` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `Core` | `0x40` |
| [`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) | `cpu_idle` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `cpuI` | `` |
| [`/cpus/cpu5`](../devicetree/root__cpus__cpu5.md) | `error_handler` | [`/arm-io`](../devicetree/root__arm-io.md) | `ErrH` | `0x7` |
| [`/cpus/cpu5`](../devicetree/root__cpus__cpu5.md) | `enable_core` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `Core` | `0x80` |
| [`/cpus/cpu5`](../devicetree/root__cpus__cpu5.md) | `cpu_idle` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `cpuI` | `` |
| [`/arm-io`](../devicetree/root__arm-io.md) | `service_gate` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `SERV` | `` |
| [`/arm-io`](../devicetree/root__arm-io.md) | `service_state` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `SERG` | `` |
| [`/arm-io`](../devicetree/root__arm-io.md) | `service_reset` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `SRST` | `` |
| [`/arm-io`](../devicetree/root__arm-io.md) | `power_gate` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `pwrG` | `` |
| [`/arm-io`](../devicetree/root__arm-io.md) | `clock_gate` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `clkG` | `` |
| [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) | `pmp_control` | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) | `PMPC` | `` |
| [`/arm-io/pmgr/pmgrtools`](../devicetree/root__arm-io__pmgr__pmgrtools.md) | `pmuaccess_L1DY` | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) | `pmuR` | `` |
| [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) | `clpc_clvr_peek_0` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `ptdP` | `0x70305452 0x1` |
| [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) | `ane_perf_ctr1` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `ANCR` | `` |
| [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) | `lostperf_report_write` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `ptdW` | `0x4f534c50 0x2` |
| [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) | `ptd_read_mult` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `ptMR` | `` |
| [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) | `clpc_clvr_read_0` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `ptdR` | `0x70305452 0x80000001` |
| [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) | `ane_perf_ctr` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `ANCR` | `` |
| [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) | `btm-start` | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) | `BMST` | `` |
| [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) | `btm-config-battfw` | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) | `BMC1` | `` |
| [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) | `btm-stop` | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) | `BMSP` | `` |
| [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) | `btm-config` | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) | `BMCO` | `` |
| [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) | `btm-vthr` | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) | `BMVT` | `` |
| [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) | `panic_notify` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `GPIO` | `0x40 0x100` |
| [`/arm-io/error-handler`](../devicetree/root__arm-io__error-handler.md) | `amcc-sram-eventhandler` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | `M$DS` | `` |
| [`/arm-io/error-handler/sac-error-handler`](../devicetree/root__arm-io__error-handler__sac-error-handler.md) | `saca_dram` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x6472616d` |
| [`/arm-io/error-handler/sac-error-handler`](../devicetree/root__arm-io__error-handler__sac-error-handler.md) | `avoid_perf_state` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `APRF` | `` |
| [`/arm-io/spi1`](../devicetree/root__arm-io__spi1.md) | `spi_cs0` | [`/`](../devicetree/root.md) | `null` | `` |
| [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) | `ane1_power_func` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `ANPW` | `` |
| [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) | `ane0_power_func` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `ANPW` | `` |
| [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) | `over-current-detection` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `keyR` | `0x706d4f43` |
| [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) | `monitor-current-3v0` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKR8` | `0x61444352 0x4950646c 0x0` |
| [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) | `ane_power_func` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `ANPW` | `` |
| [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) | `hid_event_dispatch` | [`/buttons`](../devicetree/root__buttons.md) | `ButD` | `` |
| [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) | `mesa_pwr` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x70634c44 0x0 0xd0000` |
| [`/arm-io/aop/iop-aop-nub/prox`](../devicetree/root__arm-io__aop__iop-aop-nub__prox.md) | `saca` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x70726f78` |
| [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) | `rose_pwr` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x70634c44 0x0 0x80000` |
| [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) | `rose_reset` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x800000 0x70000` |
| [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) | `rd_rose_pwr` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKR8` | `0x70634c44 0x0 0x80000` |
| [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) | `rose_coredump` | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) | `GPIO` | `0xc 0x101` |
| [`/arm-io/aop/iop-aop-nub/gnss`](../devicetree/root__arm-io__aop__iop-aop-nub__gnss.md) | `gnss-time-mark` | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) | `GPIO` | `0x0 0x101` |
| [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) | `flicker_bias` | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `flbs` | `` |
| [`/arm-io/sep/iop-sep-nub`](../devicetree/root__arm-io__sep__iop-sep-nub.md) | `wait_for_power_gate` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `Wait` | `0xd 0x0 0x0` |
| [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) | `spi0_sclk_config` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `GPIO` | `0x16 0x10001` |
| [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) | `spi0_mosi_config` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `GPIO` | `0x15 0x10001` |
| [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pmu_button` | [`/buttons`](../devicetree/root__buttons.md) | `ButD` | `` |
| [`/arm-io/smc/iop-smc-nub/smc-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger.md) | `dock_parent` | [`/port-usb-c-1`](../devicetree/root__port-usb-c-1.md) | `accP` | `` |
| [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) | `dock_parent` | [`/port-magsafe-1`](../devicetree/root__port-magsafe-1.md) | `accP` | `` |
| [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) | `dock_wired` | [`/port-usb-c-1`](../devicetree/root__port-usb-c-1.md) | `accP` | `` |
| [`/arm-io/smc/iop-smc-nub/smc-aop`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-aop.md) | `link-data_param_set` | [`/arm-io/aop/iop-aop-nub/smc-control`](../devicetree/root__arm-io__aop__iop-aop-nub__smc-control.md) | `datS` | `` |
| [`/arm-io/smc/iop-smc-nub/smc-aop`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-aop.md) | `link-data_enable` | [`/arm-io/aop/iop-aop-nub/smc-control`](../devicetree/root__arm-io__aop__iop-aop-nub__smc-control.md) | `enbl` | `` |
| [`/arm-io/smc/iop-smc-nub/smc-aop`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-aop.md) | `link-data_param_get` | [`/arm-io/aop/iop-aop-nub/smc-control`](../devicetree/root__arm-io__aop__iop-aop-nub__smc-control.md) | `datG` | `` |
| [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) | `clock_enable` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x8000000 0x0` |
| [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) | `reset` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x0 0x1060000` |
| [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) | `power_1v2_core` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x70634c44 0x0 0xe0000` |
| [`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) | `clock_enable` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x8000000 0x0` |
| [`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) | `reset` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x0 0x1050000` |
| [`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) | `power_1v2_core` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x70634c44 0x0 0xe0000` |
| [`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) | `over-current-write` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `keyW` | `0x706d4d53` |
| [`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) | `over-current-read` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `keyR` | `0x706d4d53` |
| [`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) | `power` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x70634c44 0x0 0xa0000` |
| [`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) | `current-read` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKR8` | `0x70634853 0x22000000 0xa0000` |
| [`/arm-io/mtp/iop-mtp-nub/mtp`](../devicetree/root__arm-io__mtp__iop-mtp-nub__mtp.md) | `ptd_lookup_mult` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `ptML` | `` |
| [`/arm-io/mt-bt-timestamp-sync`](../devicetree/root__arm-io__mt-bt-timestamp-sync.md) | `timestamp_sync` | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) | `GPIO` | `0x9 0x2000002` |
| [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) | `tx` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `GPIO` | `0x42 0x102` |
| [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) | `rx` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `GPIO` | `0x43 0x102` |
| [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `Flicker_master` | [`/arm-io/iop-audio-controller/audio-flicker/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker__audio-flicker.md) | `AUD1` | `0x61703266` |
| [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `pdm_rx_control` | [`/arm-io/iop-audio-controller/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker.md) | `PDMi` | `` |
| [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `Receiver_master` | [`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md) | `AUD1` | `0x61703272` |
| [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `reset` | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) | `GPIO` | `0x57 0x10001` |
| [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) | `get_pdod` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `keyR` | `0x42444431` |
| [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) | `get_vbus_detect` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `keyR` | `0x56425553` |
| [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) | `external_standby` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `keyW` | `0x4d425345` |
| [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) | `ignore_vbus_drop` | [`/port-usb-c-1`](../devicetree/root__port-usb-c-1.md) | `igvb` | `` |
| [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) | `se_boot_measurements` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `GPIO` | `0x80 0x101` |
| [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) | `enable` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x800000 0x150000` |
| [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) | `boot_measurements` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `GPIO` | `0x69 0x101` |
| [`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) | `boot_measurements` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `GPIO` | `0x83 0x101` |
| [`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) | `enable` | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) | `GPIO` | `0x6 0x101` |
| [`/arm-io/atc-phy0`](../devicetree/root__arm-io__atc-phy0.md) | `dock_parent` | [`/port-usb-c-1`](../devicetree/root__port-usb-c-1.md) | `accP` | `` |
| [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) | `vote_force_wakeup_dram` | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) | `VFWD` | `0x0 0x0` |
| [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) | `dock_parent` | [`/port-usb-c-1`](../devicetree/root__port-usb-c-1.md) | `accP` | `` |
| [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) | `parrot_srst` | [`/port-usb-c-1`](../devicetree/root__port-usb-c-1.md) | `prst` | `` |
| [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) | `mcc_dataset` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | `M$DS` | `` |
| [`/arm-io/dcp-sac-controller`](../devicetree/root__arm-io__dcp-sac-controller.md) | `saca_lcd0` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x6c636430` |
| [`/arm-io/dcp-sac-controller`](../devicetree/root__arm-io__dcp-sac-controller.md) | `saca_lcd1` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x6c636431` |
| [`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) | `mcc_dataset` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | `M$DS` | `` |
| [`/arm-io/dcpsec-sac-controller`](../devicetree/root__arm-io__dcpsec-sac-controller.md) | `saca_lcd0` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x6c636432` |
| [`/arm-io/dcpsec-sac-controller`](../devicetree/root__arm-io__dcpsec-sac-controller.md) | `saca_lcd1` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x6c636433` |
| [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) | `send_disp_clock` | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) | `UPps` | `` |
| [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) | `get_valid_perf_states` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `PRFG` | `0x2d 0x2` |
| [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) | `device_reset` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `ARST` | `0x11` |
| [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) | `set_perf_state_floor` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `PRFS` | `0x2d 0x2` |
| [`/arm-io/jpeg`](../devicetree/root__arm-io__jpeg.md) | `get_valid_perf_states` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `PRFG` | `0x2c 0x2` |
| [`/arm-io/jpeg`](../devicetree/root__arm-io__jpeg.md) | `set_perf_state_floor` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `PRFS` | `0x2c 0x2` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `motion_data_param_set` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `datS` | `` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `ane_data_param_set` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `dSet` | `` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `ane_power_func` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `ANPW` | `` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `motion_state_set` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `mstS` | `` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca0` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d30` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `ane1_data_param_set` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `dSet` | `` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca1` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d31` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca2` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d36` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca3` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d42` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca4` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d44` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca5` | [`/sacm-jasper`](../devicetree/root__sacm-jasper.md) | `SACA` | `0x63616d47` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca0b` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d32` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca0c` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d34` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca0d` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d41` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca1b` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d33` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `ane1_ep_control` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `eCtl` | `` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca1c` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d35` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `mcc_dataset` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | `M$DS` | `` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca2b` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d37` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `ane1_data_param_get` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `dGet` | `` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca2c` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d38` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `motion_data_enable` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `enbl` | `` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca2d` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d39` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca3b` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d43` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca4b` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d45` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `saca4c` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d46` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `ane_data_param_get` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `dGet` | `` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `motion_data_param_get` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `datG` | `` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `ane1_power_func` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `ANPW` | `` |
| [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) | `ane_ep_control` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `eCtl` | `` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `conf_isp_ref0_clk_freq` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `ISPC` | `0x0 0x55c11a9e 0x551b9816` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `motion_data_param_set` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `datS` | `` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `ane_data_param_set` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `dSet` | `` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `ane_power_func` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `ANPW` | `` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `motion_state_set` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `mstS` | `` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca0` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d30` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `ane1_data_param_set` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `dSet` | `` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca1` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d31` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca2` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d36` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca3` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d42` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca4` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d44` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca5` | [`/sacm-jasper`](../devicetree/root__sacm-jasper.md) | `SACA` | `0x63616d47` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca0b` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d32` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca0c` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d34` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca0d` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d41` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca1b` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d33` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `ane1_ep_control` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `eCtl` | `` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca1c` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d35` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca2b` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d37` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `ane1_data_param_get` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `dGet` | `` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca2c` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d38` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `motion_data_enable` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `enbl` | `` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca2d` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d39` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca3b` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d43` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca4b` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d45` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `saca4c` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACA` | `0x63616d46` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `conf_isp_ref2_clk_freq` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `ISPC` | `0x2 0x55c11a9e 0x551b9816` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `ane_data_param_get` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `dGet` | `` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `motion_data_param_get` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `datG` | `` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `conf_isp_ref1_clk_freq` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `ISPC` | `0x1 0x55c11a9e 0x551b9816` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `ane1_power_func` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `ANPW` | `` |
| [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) | `ane_ep_control` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `eCtl` | `` |
| [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) | `get_valid_perf_states` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `PRFG` | `0x2f 0x102` |
| [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) | `clock_req_interrupt` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `CIRQ` | `0x73 0x23 0x1` |
| [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) | `mcc_dataset` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | `M$DS` | `` |
| [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) | `set_perf_state_floor` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `PRFS` | `0x2f 0x102` |
| [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) | `get_valid_perf_states` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `PRFG` | `0x2e 0x2` |
| [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) | `mcc_dataset` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | `M$DS` | `` |
| [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) | `set_perf_state_floor` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `PRFS` | `0x2e 0x2` |
| [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `mcc_dataset` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | `M$DS` | `` |
| [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `mcc_dataset` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | `M$DS` | `` |
| [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) | `mcc_dataset` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | `M$DS` | `` |
| [`/arm-io/iop-audio-controller/lp-mic-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-device.md) | `cm_power_change_notify` | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `lpsm` | `` |
| [`/arm-io/iop-audio-controller/siri-listening-device`](../devicetree/root__arm-io__iop-audio-controller__siri-listening-device.md) | `cm_power_change_notify` | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `lpls` | `` |
| [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) | `haptics_session` | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) | `hpsc` | `` |
| [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) | `hall_ctrl` | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `hall` | `` |
| [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) | `thermal_budget` | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) | `ther` | `` |
| [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) | `power_peak_budget` | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) | `pkpw` | `` |
| [`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) | `hall_ctrl` | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `hall` | `` |
| [`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) | `input-data-selectors` | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) | `hdis` | `` |
| [`/arm-io/admac-hp-mic-ec-proxy`](../devicetree/root__arm-io__admac-hp-mic-ec-proxy.md) | `iommu_handler` | [`/arm-io/audio-shared-dart-proxy`](../devicetree/root__arm-io__audio-shared-dart-proxy.md) | `sdpr` | `` |
| [`/arm-io/admac-speaker-tx-ec-proxy`](../devicetree/root__arm-io__admac-speaker-tx-ec-proxy.md) | `iommu_handler` | [`/arm-io/audio-shared-dart-proxy`](../devicetree/root__arm-io__audio-shared-dart-proxy.md) | `sdpr` | `` |
| [`/arm-io/admac-receiver-tx-ec-proxy`](../devicetree/root__arm-io__admac-receiver-tx-ec-proxy.md) | `iommu_handler` | [`/arm-io/audio-shared-dart-proxy`](../devicetree/root__arm-io__audio-shared-dart-proxy.md) | `sdpr` | `` |
| [`/arm-io/admac-sllb-ec-proxy`](../devicetree/root__arm-io__admac-sllb-ec-proxy.md) | `iommu_handler` | [`/arm-io/audio-shared-dart-proxy`](../devicetree/root__arm-io__audio-shared-dart-proxy.md) | `sdpr` | `` |
| [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | `debug_gpio` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `GPIO` | `0x40 0x101` |
| [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) | `dart_force_active` | [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) | `Fact` | `` |
| [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) | `dart_self` | [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) | `Self` | `` |
| [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) | `dart_release_sid` | [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) | `SRel` | `` |
| [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) | `warm_reset` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW4` | `0x62706c69 0x1000000` |
| [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) | `reset` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x800000 0x80000` |
| [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) | `pcie_port_control` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | `PrtC` | `0x19f` |
| [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) | `dart_request_sid` | [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) | `SReq` | `` |
| [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) | `perst` | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) | `GPIO` | `0x42 0x0` |
| [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) | `perst` | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) | `GPIO` | `0x40 0x0` |
| [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) | `dart_force_active` | [`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) | `Fact` | `` |
| [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) | `dart_request_sid` | [`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) | `SReq` | `` |
| [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) | `dart_release_sid` | [`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) | `SRel` | `` |
| [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) | `dart_self` | [`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) | `Self` | `` |
| [`/arm-io/aod2`](../devicetree/root__arm-io__aod2.md) | `aod_swclk` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `GPIO` | `0x68 0x101` |
| [`/arm-io/aod2`](../devicetree/root__arm-io__aod2.md) | `aod_swdio` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `GPIO` | `0x62 0x100` |
| [`/arm-io/aod3`](../devicetree/root__arm-io__aod3.md) | `aod_swclk` | [`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) | `GPIO` | `0x5 0x100` |
| [`/arm-io/aod3`](../devicetree/root__arm-io__aod3.md) | `aod_swdio` | [`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) | `GPIO` | `0x8 0x101` |
| [`/arm-io/aod4`](../devicetree/root__arm-io__aod4.md) | `aod_swclk` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `GPIO` | `0x68 0x101` |
| [`/arm-io/aod4`](../devicetree/root__arm-io__aod4.md) | `aod_swdio` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `GPIO` | `0x62 0x100` |
| [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) | `grimaldi-power-set` | [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) | `pwrS` | `` |
| [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) | `grimaldi-device-id` | [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) | `devI` | `` |
| [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) | `grimaldi-power-get` | [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) | `pwrG` | `` |
| [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) | `grimaldi-gain` | [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) | `gain` | `` |
| [`/arm-io/baseband-ptd`](../devicetree/root__arm-io__baseband-ptd.md) | `ptd_read_mult` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `ptMR` | `` |
| [`/arm-io/baseband-ptd`](../devicetree/root__arm-io__baseband-ptd.md) | `ptd_lookup_mult` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `ptML` | `` |
| [`/arm-io/baseband-ptd`](../devicetree/root__arm-io__baseband-ptd.md) | `ptd_peek_mult` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `ptMP` | `` |
| [`/buttons`](../devicetree/root__buttons.md) | `button_volup` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `btnR` | `0x62565550` |
| [`/buttons`](../devicetree/root__buttons.md) | `button_voldown` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `btnR` | `0x6256444e` |
| [`/buttons`](../devicetree/root__buttons.md) | `button_hold` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `btnR` | `0x62484c44` |
| [`/baseband`](../devicetree/root__baseband.md) | `pmu_exton_config` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x7800000 0x60000` |
| [`/baseband`](../devicetree/root__baseband.md) | `bb_on` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x7063494f 0x800000 0xe0000` |
| [`/baseband`](../devicetree/root__baseband.md) | `bb_warm_reset` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW4` | `0x62706c69 0x0` |
| [`/baseband`](../devicetree/root__baseband.md) | `pmu_exton` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKR8` | `0x7063494f 0x2000000 0x60000` |
| [`/baseband`](../devicetree/root__baseband.md) | `pcie_port_control` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | `PrtC` | `0x1a3` |
| [`/baseband`](../devicetree/root__baseband.md) | `sac` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACC` | `0x6c636430 0x6c636431 0x6c636432 0x6c636433 0x63616d30 0x63616d31 0x63616d32 0x63616d33 0x63616d34 0x63616d35 0x63616d36 0x63616d37 0x63616d38 0x63616d39 0x63616d41 0x63616d42 0x63616d43 0x63616d44 0x63616d45 0x63616d46 0x70726f78` |
| [`/baseband`](../devicetree/root__baseband.md) | `jasper-sac` | [`/sacm-jasper`](../devicetree/root__sacm-jasper.md) | `SACC` | `0x63616d47` |
| [`/baseband`](../devicetree/root__baseband.md) | `reset_det` | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) | `GPIO` | `0x10 0x0` |
| [`/centauri`](../devicetree/root__centauri.md) | `error_detect` | [`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) | `GPIO` | `0x16 0x100` |
| [`/centauri`](../devicetree/root__centauri.md) | `sac` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `SACC` | `0x6472616d` |

## Grouped by provider


### [`/`](../devicetree/root.md) (1 consumers)

- [`/arm-io/spi1`](../devicetree/root__arm-io__spi1.md) `spi_cs0` `null` 

### [`/arm-io`](../devicetree/root__arm-io.md) (6 consumers)

- [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) `error_handler` `ErrH` 0x0
- [`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) `error_handler` `ErrH` 0x1
- [`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) `error_handler` `ErrH` 0x2
- [`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) `error_handler` `ErrH` 0x3
- [`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) `error_handler` `ErrH` 0x6
- [`/cpus/cpu5`](../devicetree/root__cpus__cpu5.md) `error_handler` `ErrH` 0x7

### [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) (11 consumers)

- [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) `ane_perf_ctr` `ANCR` 
- [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) `ane0_power_func` `ANPW` 
- [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) `ane_power_func` `ANPW` 
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `ane_data_param_set` `dSet` 
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `ane_power_func` `ANPW` 
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `ane_data_param_get` `dGet` 
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `ane_ep_control` `eCtl` 
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `ane_data_param_set` `dSet` 
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `ane_power_func` `ANPW` 
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `ane_data_param_get` `dGet` 
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `ane_ep_control` `eCtl` 

### [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) (10 consumers)

- [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) `ane_perf_ctr1` `ANCR` 
- [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) `ane1_power_func` `ANPW` 
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `ane1_data_param_set` `dSet` 
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `ane1_ep_control` `eCtl` 
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `ane1_data_param_get` `dGet` 
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `ane1_power_func` `ANPW` 
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `ane1_data_param_set` `dSet` 
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `ane1_ep_control` `eCtl` 
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `ane1_data_param_get` `dGet` 
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `ane1_power_func` `ANPW` 

### [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) (8 consumers)

- [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) `clpc_clvr_peek_0` `ptdP` 0x70305452 0x1
- [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) `lostperf_report_write` `ptdW` 0x4f534c50 0x2
- [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) `ptd_read_mult` `ptMR` 
- [`/arm-io/pmgr/clpc`](../devicetree/root__arm-io__pmgr__clpc.md) `clpc_clvr_read_0` `ptdR` 0x70305452 0x80000001
- [`/arm-io/mtp/iop-mtp-nub/mtp`](../devicetree/root__arm-io__mtp__iop-mtp-nub__mtp.md) `ptd_lookup_mult` `ptML` 
- [`/arm-io/baseband-ptd`](../devicetree/root__arm-io__baseband-ptd.md) `ptd_read_mult` `ptMR` 
- [`/arm-io/baseband-ptd`](../devicetree/root__arm-io__baseband-ptd.md) `ptd_lookup_mult` `ptML` 
- [`/arm-io/baseband-ptd`](../devicetree/root__arm-io__baseband-ptd.md) `ptd_peek_mult` `ptMP` 

### [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) (8 consumers)

- [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) `rose_coredump` `GPIO` 0xc 0x101
- [`/arm-io/aop/iop-aop-nub/gnss`](../devicetree/root__arm-io__aop__iop-aop-nub__gnss.md) `gnss-time-mark` `GPIO` 0x0 0x101
- [`/arm-io/mt-bt-timestamp-sync`](../devicetree/root__arm-io__mt-bt-timestamp-sync.md) `timestamp_sync` `GPIO` 0x9 0x2000002
- [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) `reset` `GPIO` 0x57 0x10001
- [`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) `enable` `GPIO` 0x6 0x101
- [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) `perst` `GPIO` 0x42 0x0
- [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) `perst` `GPIO` 0x40 0x0
- [`/baseband`](../devicetree/root__baseband.md) `reset_det` `GPIO` 0x10 0x0

### [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) (4 consumers)

- [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) `grimaldi-power-set` `pwrS` 
- [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) `grimaldi-device-id` `devI` 
- [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) `grimaldi-power-get` `pwrG` 
- [`/arm-io/grimaldi`](../devicetree/root__arm-io__grimaldi.md) `grimaldi-gain` `gain` 

### [`/arm-io/aop/iop-aop-nub/smc-control`](../devicetree/root__arm-io__aop__iop-aop-nub__smc-control.md) (3 consumers)

- [`/arm-io/smc/iop-smc-nub/smc-aop`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-aop.md) `link-data_param_set` `datS` 
- [`/arm-io/smc/iop-smc-nub/smc-aop`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-aop.md) `link-data_enable` `enbl` 
- [`/arm-io/smc/iop-smc-nub/smc-aop`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-aop.md) `link-data_param_get` `datG` 

### [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) (8 consumers)

- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `motion_data_param_set` `datS` 
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `motion_state_set` `mstS` 
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `motion_data_enable` `enbl` 
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `motion_data_param_get` `datG` 
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `motion_data_param_set` `datS` 
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `motion_state_set` `mstS` 
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `motion_data_enable` `enbl` 
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `motion_data_param_get` `datG` 

### [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) (2 consumers)

- [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) `pcie_port_control` `PrtC` 0x19f
- [`/baseband`](../devicetree/root__baseband.md) `pcie_port_control` `PrtC` 0x1a3

### [`/arm-io/audio-shared-dart-proxy`](../devicetree/root__arm-io__audio-shared-dart-proxy.md) (4 consumers)

- [`/arm-io/admac-hp-mic-ec-proxy`](../devicetree/root__arm-io__admac-hp-mic-ec-proxy.md) `iommu_handler` `sdpr` 
- [`/arm-io/admac-speaker-tx-ec-proxy`](../devicetree/root__arm-io__admac-speaker-tx-ec-proxy.md) `iommu_handler` `sdpr` 
- [`/arm-io/admac-receiver-tx-ec-proxy`](../devicetree/root__arm-io__admac-receiver-tx-ec-proxy.md) `iommu_handler` `sdpr` 
- [`/arm-io/admac-sllb-ec-proxy`](../devicetree/root__arm-io__admac-sllb-ec-proxy.md) `iommu_handler` `sdpr` 

### [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) (4 consumers)

- [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) `dart_force_active` `Fact` 
- [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) `dart_self` `Self` 
- [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) `dart_release_sid` `SRel` 
- [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) `dart_request_sid` `SReq` 

### [`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) (4 consumers)

- [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) `dart_force_active` `Fact` 
- [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) `dart_request_sid` `SReq` 
- [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) `dart_release_sid` `SRel` 
- [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) `dart_self` `Self` 

### [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) (1 consumers)

- [`/arm-io/dispext0`](../devicetree/root__arm-io__dispext0.md) `send_disp_clock` `UPps` 

### [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) (13 consumers)

- [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) `panic_notify` `GPIO` 0x40 0x100
- [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) `spi0_sclk_config` `GPIO` 0x16 0x10001
- [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) `spi0_mosi_config` `GPIO` 0x15 0x10001
- [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) `tx` `GPIO` 0x42 0x102
- [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) `rx` `GPIO` 0x43 0x102
- [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) `se_boot_measurements` `GPIO` 0x80 0x101
- [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) `boot_measurements` `GPIO` 0x69 0x101
- [`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) `boot_measurements` `GPIO` 0x83 0x101
- [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) `debug_gpio` `GPIO` 0x40 0x101
- [`/arm-io/aod2`](../devicetree/root__arm-io__aod2.md) `aod_swclk` `GPIO` 0x68 0x101
- [`/arm-io/aod2`](../devicetree/root__arm-io__aod2.md) `aod_swdio` `GPIO` 0x62 0x100
- [`/arm-io/aod4`](../devicetree/root__arm-io__aod4.md) `aod_swclk` `GPIO` 0x68 0x101
- [`/arm-io/aod4`](../devicetree/root__arm-io__aod4.md) `aod_swdio` `GPIO` 0x62 0x100

### [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) (4 consumers)

- [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) `haptics_session` `hpsc` 
- [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) `thermal_budget` `ther` 
- [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) `power_peak_budget` `pkpw` 
- [`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) `input-data-selectors` `hdis` 

### [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) (5 consumers)

- [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) `flicker_bias` `flbs` 
- [`/arm-io/iop-audio-controller/lp-mic-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-device.md) `cm_power_change_notify` `lpsm` 
- [`/arm-io/iop-audio-controller/siri-listening-device`](../devicetree/root__arm-io__iop-audio-controller__siri-listening-device.md) `cm_power_change_notify` `lpls` 
- [`/arm-io/iop-audio-controller/audio-haptic`](../devicetree/root__arm-io__iop-audio-controller__audio-haptic.md) `hall_ctrl` `hall` 
- [`/arm-io/iop-audio-controller/audio-hpdbg`](../devicetree/root__arm-io__iop-audio-controller__audio-hpdbg.md) `hall_ctrl` `hall` 

### [`/arm-io/iop-audio-controller/audio-flicker/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker__audio-flicker.md) (1 consumers)

- [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) `Flicker_master` `AUD1` 0x61703266

### [`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md) (1 consumers)

- [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) `Receiver_master` `AUD1` 0x61703272

### [`/arm-io/iop-audio-controller/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker.md) (1 consumers)

- [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) `pdm_rx_control` `PDMi` 

### [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) (9 consumers)

- [`/arm-io/error-handler`](../devicetree/root__arm-io__error-handler.md) `amcc-sram-eventhandler` `M$DS` 
- [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) `mcc_dataset` `M$DS` 
- [`/arm-io/dispsec`](../devicetree/root__arm-io__dispsec.md) `mcc_dataset` `M$DS` 
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `mcc_dataset` `M$DS` 
- [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) `mcc_dataset` `M$DS` 
- [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) `mcc_dataset` `M$DS` 
- [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) `mcc_dataset` `M$DS` 
- [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) `mcc_dataset` `M$DS` 
- [`/arm-io/sgx`](../devicetree/root__arm-io__sgx.md) `mcc_dataset` `M$DS` 

### [`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) (3 consumers)

- [`/arm-io/aod3`](../devicetree/root__arm-io__aod3.md) `aod_swclk` `GPIO` 0x5 0x100
- [`/arm-io/aod3`](../devicetree/root__arm-io__aod3.md) `aod_swdio` `GPIO` 0x8 0x101
- [`/centauri`](../devicetree/root__centauri.md) `error_detect` `GPIO` 0x16 0x100

### [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) (5 consumers)

- [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) `btm-start` `BMST` 
- [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) `btm-config-battfw` `BMC1` 
- [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) `btm-stop` `BMSP` 
- [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) `btm-config` `BMCO` 
- [`/arm-io/pmgr/ppm`](../devicetree/root__arm-io__pmgr__ppm.md) `btm-vthr` `BMVT` 

### [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) (1 consumers)

- [`/arm-io/pmgr/pmgrtools`](../devicetree/root__arm-io__pmgr__pmgrtools.md) `pmuaccess_L1DY` `pmuR` 

### [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) (32 consumers)

- [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) `enable_core` `Core` 0x1
- [`/cpus/cpu0`](../devicetree/root__cpus__cpu0.md) `cpu_idle` `cpuI` 
- [`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) `enable_core` `Core` 0x2
- [`/cpus/cpu1`](../devicetree/root__cpus__cpu1.md) `cpu_idle` `cpuI` 
- [`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) `enable_core` `Core` 0x4
- [`/cpus/cpu2`](../devicetree/root__cpus__cpu2.md) `cpu_idle` `cpuI` 
- [`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) `enable_core` `Core` 0x8
- [`/cpus/cpu3`](../devicetree/root__cpus__cpu3.md) `cpu_idle` `cpuI` 
- [`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) `enable_core` `Core` 0x40
- [`/cpus/cpu4`](../devicetree/root__cpus__cpu4.md) `cpu_idle` `cpuI` 
- [`/cpus/cpu5`](../devicetree/root__cpus__cpu5.md) `enable_core` `Core` 0x80
- [`/cpus/cpu5`](../devicetree/root__cpus__cpu5.md) `cpu_idle` `cpuI` 
- [`/arm-io`](../devicetree/root__arm-io.md) `service_gate` `SERV` 
- [`/arm-io`](../devicetree/root__arm-io.md) `service_state` `SERG` 
- [`/arm-io`](../devicetree/root__arm-io.md) `service_reset` `SRST` 
- [`/arm-io`](../devicetree/root__arm-io.md) `power_gate` `pwrG` 
- [`/arm-io`](../devicetree/root__arm-io.md) `clock_gate` `clkG` 
- [`/arm-io/error-handler/sac-error-handler`](../devicetree/root__arm-io__error-handler__sac-error-handler.md) `avoid_perf_state` `APRF` 
- [`/arm-io/sep/iop-sep-nub`](../devicetree/root__arm-io__sep__iop-sep-nub.md) `wait_for_power_gate` `Wait` 0xd 0x0 0x0
- [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) `get_valid_perf_states` `PRFG` 0x2d 0x2
- [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) `device_reset` `ARST` 0x11
- [`/arm-io/scaler0`](../devicetree/root__arm-io__scaler0.md) `set_perf_state_floor` `PRFS` 0x2d 0x2
- [`/arm-io/jpeg`](../devicetree/root__arm-io__jpeg.md) `get_valid_perf_states` `PRFG` 0x2c 0x2
- [`/arm-io/jpeg`](../devicetree/root__arm-io__jpeg.md) `set_perf_state_floor` `PRFS` 0x2c 0x2
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `conf_isp_ref0_clk_freq` `ISPC` 0x0 0x55c11a9e 0x551b9816
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `conf_isp_ref2_clk_freq` `ISPC` 0x2 0x55c11a9e 0x551b9816
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `conf_isp_ref1_clk_freq` `ISPC` 0x1 0x55c11a9e 0x551b9816
- [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) `get_valid_perf_states` `PRFG` 0x2f 0x102
- [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) `clock_req_interrupt` `CIRQ` 0x73 0x23 0x1
- [`/arm-io/ave`](../devicetree/root__arm-io__ave.md) `set_perf_state_floor` `PRFS` 0x2f 0x102
- [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) `get_valid_perf_states` `PRFG` 0x2e 0x2
- [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) `set_perf_state_floor` `PRFS` 0x2e 0x2

### [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) (1 consumers)

- [`/arm-io/pmgr-child`](../devicetree/root__arm-io__pmgr-child.md) `pmp_control` `PMPC` 

### [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) (29 consumers)

- [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) `over-current-detection` `keyR` 0x706d4f43
- [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) `monitor-current-3v0` `pKR8` 0x61444352 0x4950646c 0x0
- [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) `mesa_pwr` `pKW8` 0x70634c44 0x0 0xd0000
- [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) `rose_pwr` `pKW8` 0x70634c44 0x0 0x80000
- [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) `rose_reset` `pKW8` 0x7063494f 0x800000 0x70000
- [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) `rd_rose_pwr` `pKR8` 0x70634c44 0x0 0x80000
- [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) `clock_enable` `pKW8` 0x7063494f 0x8000000 0x0
- [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) `reset` `pKW8` 0x7063494f 0x0 0x1060000
- [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch2.md) `power_1v2_core` `pKW8` 0x70634c44 0x0 0xe0000
- [`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) `clock_enable` `pKW8` 0x7063494f 0x8000000 0x0
- [`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) `reset` `pKW8` 0x7063494f 0x0 0x1050000
- [`/arm-io/mtp/iop-mtp-nub/multi-touch`](../devicetree/root__arm-io__mtp__iop-mtp-nub__multi-touch.md) `power_1v2_core` `pKW8` 0x70634c44 0x0 0xe0000
- [`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) `over-current-write` `keyW` 0x706d4d53
- [`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) `over-current-read` `keyR` 0x706d4d53
- [`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) `power` `pKW8` 0x70634c44 0x0 0xa0000
- [`/arm-io/mtp/iop-mtp-nub/nova`](../devicetree/root__arm-io__mtp__iop-mtp-nub__nova.md) `current-read` `pKR8` 0x70634853 0x22000000 0xa0000
- [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) `get_pdod` `keyR` 0x42444431
- [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) `get_vbus_detect` `keyR` 0x56425553
- [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) `external_standby` `keyW` 0x4d425345
- [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) `enable` `pKW8` 0x7063494f 0x800000 0x150000
- [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) `warm_reset` `pKW4` 0x62706c69 0x1000000
- [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) `reset` `pKW8` 0x7063494f 0x800000 0x80000
- [`/buttons`](../devicetree/root__buttons.md) `button_volup` `btnR` 0x62565550
- [`/buttons`](../devicetree/root__buttons.md) `button_voldown` `btnR` 0x6256444e
- [`/buttons`](../devicetree/root__buttons.md) `button_hold` `btnR` 0x62484c44
- [`/baseband`](../devicetree/root__baseband.md) `pmu_exton_config` `pKW8` 0x7063494f 0x7800000 0x60000
- [`/baseband`](../devicetree/root__baseband.md) `bb_on` `pKW8` 0x7063494f 0x800000 0xe0000
- [`/baseband`](../devicetree/root__baseband.md) `bb_warm_reset` `pKW4` 0x62706c69 0x0
- [`/baseband`](../devicetree/root__baseband.md) `pmu_exton` `pKR8` 0x7063494f 0x2000000 0x60000

### [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) (1 consumers)

- [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) `vote_force_wakeup_dram` `VFWD` 0x0 0x0

### [`/buttons`](../devicetree/root__buttons.md) (2 consumers)

- [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) `hid_event_dispatch` `ButD` 
- [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) `pmu_button` `ButD` 

### [`/port-magsafe-1`](../devicetree/root__port-magsafe-1.md) (1 consumers)

- [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) `dock_parent` `accP` 

### [`/port-usb-c-1`](../devicetree/root__port-usb-c-1.md) (6 consumers)

- [`/arm-io/smc/iop-smc-nub/smc-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-charger.md) `dock_parent` `accP` 
- [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-ext-charger.md) `dock_wired` `accP` 
- [`/arm-io/nub-spmi2/spmi-hpm0`](../devicetree/root__arm-io__nub-spmi2__spmi-hpm0.md) `ignore_vbus_drop` `igvb` 
- [`/arm-io/atc-phy0`](../devicetree/root__arm-io__atc-phy0.md) `dock_parent` `accP` 
- [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) `dock_parent` `accP` 
- [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) `parrot_srst` `prst` 

### [`/sacm-general`](../devicetree/root__sacm-general.md) (40 consumers)

- [`/arm-io/error-handler/sac-error-handler`](../devicetree/root__arm-io__error-handler__sac-error-handler.md) `saca_dram` `SACA` 0x6472616d
- [`/arm-io/aop/iop-aop-nub/prox`](../devicetree/root__arm-io__aop__iop-aop-nub__prox.md) `saca` `SACA` 0x70726f78
- [`/arm-io/dcp-sac-controller`](../devicetree/root__arm-io__dcp-sac-controller.md) `saca_lcd0` `SACA` 0x6c636430
- [`/arm-io/dcp-sac-controller`](../devicetree/root__arm-io__dcp-sac-controller.md) `saca_lcd1` `SACA` 0x6c636431
- [`/arm-io/dcpsec-sac-controller`](../devicetree/root__arm-io__dcpsec-sac-controller.md) `saca_lcd0` `SACA` 0x6c636432
- [`/arm-io/dcpsec-sac-controller`](../devicetree/root__arm-io__dcpsec-sac-controller.md) `saca_lcd1` `SACA` 0x6c636433
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca0` `SACA` 0x63616d30
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca1` `SACA` 0x63616d31
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca2` `SACA` 0x63616d36
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca3` `SACA` 0x63616d42
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca4` `SACA` 0x63616d44
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca0b` `SACA` 0x63616d32
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca0c` `SACA` 0x63616d34
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca0d` `SACA` 0x63616d41
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca1b` `SACA` 0x63616d33
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca1c` `SACA` 0x63616d35
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca2b` `SACA` 0x63616d37
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca2c` `SACA` 0x63616d38
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca2d` `SACA` 0x63616d39
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca3b` `SACA` 0x63616d43
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca4b` `SACA` 0x63616d45
- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca4c` `SACA` 0x63616d46
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca0` `SACA` 0x63616d30
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca1` `SACA` 0x63616d31
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca2` `SACA` 0x63616d36
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca3` `SACA` 0x63616d42
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca4` `SACA` 0x63616d44
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca0b` `SACA` 0x63616d32
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca0c` `SACA` 0x63616d34
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca0d` `SACA` 0x63616d41
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca1b` `SACA` 0x63616d33
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca1c` `SACA` 0x63616d35
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca2b` `SACA` 0x63616d37
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca2c` `SACA` 0x63616d38
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca2d` `SACA` 0x63616d39
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca3b` `SACA` 0x63616d43
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca4b` `SACA` 0x63616d45
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca4c` `SACA` 0x63616d46
- [`/baseband`](../devicetree/root__baseband.md) `sac` `SACC` 0x6c636430 0x6c636431 0x6c636432 0x6c636433 0x63616d30 0x63616d31 0x63616d32 0x63616d33 0x63616d34 0x63616d35 0x63616d36 0x63616d37 0x63616d38 0x63616d39 0x63616d41 0x63616d42 0x63616d43 0x63616d44 0x63616d45 0x63616d46 0x70726f78
- [`/centauri`](../devicetree/root__centauri.md) `sac` `SACC` 0x6472616d

### [`/sacm-jasper`](../devicetree/root__sacm-jasper.md) (3 consumers)

- [`/arm-io/ispRtb`](../devicetree/root__arm-io__ispRtb.md) `saca5` `SACA` 0x63616d47
- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) `saca5` `SACA` 0x63616d47
- [`/baseband`](../devicetree/root__baseband.md) `jasper-sac` `SACC` 0x63616d47

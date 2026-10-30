# Function codes

Every four-character code used in `function-*` properties, grouped by provider. The provider driver implements the code; consumers call it with the arguments shown (first three examples). Codes are shown in readable byte order. **[DT]**

92 distinct (code, provider) pairs.

| Code | Provider | Function names | Consumers | Example arguments |
|---|---|---|---|---|
| `null` | [`/`](../devicetree/root.md) | `spi_cs0` | 1 |  |
| `ErrH` | [`/arm-io`](../devicetree/root__arm-io.md) | `error_handler` | 6 | `0x0`; `0x1`; `0x2` |
| `ANCR` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `ane_perf_ctr` | 1 |  |
| `ANPW` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `ane0_power_func`, `ane_power_func` | 3 |  |
| `dGet` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `ane_data_param_get` | 2 |  |
| `dSet` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `ane_data_param_set` | 2 |  |
| `eCtl` | [`/arm-io/ane0`](../devicetree/root__arm-io__ane0.md) | `ane_ep_control` | 2 |  |
| `ANCR` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `ane_perf_ctr1` | 1 |  |
| `ANPW` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `ane1_power_func` | 3 |  |
| `dGet` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `ane1_data_param_get` | 2 |  |
| `dSet` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `ane1_data_param_set` | 2 |  |
| `eCtl` | [`/arm-io/ane1`](../devicetree/root__arm-io__ane1.md) | `ane1_ep_control` | 2 |  |
| `ptML` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `ptd_lookup_mult` | 2 |  |
| `ptMP` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `ptd_peek_mult` | 1 |  |
| `ptMR` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `ptd_read_mult` | 2 |  |
| `ptdP` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `clpc_clvr_peek_0` | 1 | `0x70305452 0x1` |
| `ptdR` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `clpc_clvr_read_0` | 1 | `0x70305452 0x80000001` |
| `ptdW` | [`/arm-io/aon-ptd`](../devicetree/root__arm-io__aon-ptd.md) | `lostperf_report_write` | 1 | `0x4f534c50 0x2` |
| `GPIO` | [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) | `enable`, `gnss-time-mark`, `perst`, `reset`, `reset_det`, `rose_coredump`, `timestamp_sync` | 8 | `0xc 0x101`; `0x0 0x101`; `0x9 0x2000002` |
| `devI` | [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) | `grimaldi-device-id` | 1 |  |
| `gain` | [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) | `grimaldi-gain` | 1 |  |
| `pwrG` | [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) | `grimaldi-power-get` | 1 |  |
| `pwrS` | [`/arm-io/aop/iop-aop-nub/grimaldi-control`](../devicetree/root__arm-io__aop__iop-aop-nub__grimaldi-control.md) | `grimaldi-power-set` | 1 |  |
| `datG` | [`/arm-io/aop/iop-aop-nub/smc-control`](../devicetree/root__arm-io__aop__iop-aop-nub__smc-control.md) | `link-data_param_get` | 1 |  |
| `datS` | [`/arm-io/aop/iop-aop-nub/smc-control`](../devicetree/root__arm-io__aop__iop-aop-nub__smc-control.md) | `link-data_param_set` | 1 |  |
| `enbl` | [`/arm-io/aop/iop-aop-nub/smc-control`](../devicetree/root__arm-io__aop__iop-aop-nub__smc-control.md) | `link-data_enable` | 1 |  |
| `datG` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `motion_data_param_get` | 2 |  |
| `datS` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `motion_data_param_set` | 2 |  |
| `enbl` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `motion_data_enable` | 2 |  |
| `mstS` | [`/arm-io/aop/iop-aop-nub/spherecontrol`](../devicetree/root__arm-io__aop__iop-aop-nub__spherecontrol.md) | `motion_state_set` | 2 |  |
| `PrtC` | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | `pcie_port_control` | 2 | `0x19f`; `0x1a3` |
| `sdpr` | [`/arm-io/audio-shared-dart-proxy`](../devicetree/root__arm-io__audio-shared-dart-proxy.md) | `iommu_handler` | 4 |  |
| `Fact` | [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) | `dart_force_active` | 1 |  |
| `SRel` | [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) | `dart_release_sid` | 1 |  |
| `SReq` | [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) | `dart_request_sid` | 1 |  |
| `Self` | [`/arm-io/dart-apcie0`](../devicetree/root__arm-io__dart-apcie0.md) | `dart_self` | 1 |  |
| `Fact` | [`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) | `dart_force_active` | 1 |  |
| `SRel` | [`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) | `dart_release_sid` | 1 |  |
| `SReq` | [`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) | `dart_request_sid` | 1 |  |
| `Self` | [`/arm-io/dart-apcie1`](../devicetree/root__arm-io__dart-apcie1.md) | `dart_self` | 1 |  |
| `UPps` | [`/arm-io/disp0`](../devicetree/root__arm-io__disp0.md) | `send_disp_clock` | 1 |  |
| `GPIO` | [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | `aod_swclk`, `aod_swdio`, `boot_measurements`, `debug_gpio`, `panic_notify`, `rx`, `se_boot_measurements`, `spi0_mosi_config` | 8 | `0x40 0x100`; `0x16 0x10001`; `0x15 0x10001` |
| `hdis` | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) | `input-data-selectors` | 1 |  |
| `hpsc` | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) | `haptics_session` | 1 |  |
| `pkpw` | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) | `power_peak_budget` | 1 |  |
| `ther` | [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) | `thermal_budget` | 1 |  |
| `flbs` | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `flicker_bias` | 1 |  |
| `hall` | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `hall_ctrl` | 2 |  |
| `lpls` | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `cm_power_change_notify` | 1 |  |
| `lpsm` | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `cm_power_change_notify` | 1 |  |
| `AUD1` | [`/arm-io/iop-audio-controller/audio-flicker/audio-flicker`](../devicetree/root__arm-io__iop-audio-controller__audio-flicker__audio-flicker.md) | `Flicker_master` | 1 | `0x61703266` |
| `AUD1` | [`/arm-io/iop-audio-controller/audio-receiver/audio-receiver`](../devicetree/root__arm-io__iop-audio-controller__audio-receiver__audio-receiver.md) | `Receiver_master` | 1 | `0x61703272` |
| `PDMi` | [`/arm-io/iop-audio-controller/audio-speaker`](../devicetree/root__arm-io__iop-audio-controller__audio-speaker.md) | `pdm_rx_control` | 1 |  |
| `M$DS` | [`/arm-io/mcc`](../devicetree/root__arm-io__mcc.md) | `amcc-sram-eventhandler`, `mcc_dataset` | 9 |  |
| `GPIO` | [`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) | `aod_swclk`, `aod_swdio`, `error_detect` | 2 | `0x5 0x100`; `0x8 0x101`; `0x16 0x100` |
| `BMC1` | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) | `btm-config-battfw` | 1 |  |
| `BMCO` | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) | `btm-config` | 1 |  |
| `BMSP` | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) | `btm-stop` | 1 |  |
| `BMST` | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) | `btm-start` | 1 |  |
| `BMVT` | [`/arm-io/nub-spmi0/btm`](../devicetree/root__arm-io__nub-spmi0__btm.md) | `btm-vthr` | 1 |  |
| `pmuR` | [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) | `pmuaccess_L1DY` | 1 |  |
| `APRF` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `avoid_perf_state` | 1 |  |
| `ARST` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `device_reset` | 1 | `0x11` |
| `CIRQ` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `clock_req_interrupt` | 1 | `0x73 0x23 0x1` |
| `Core` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `enable_core` | 6 | `0x1`; `0x2`; `0x4` |
| `ISPC` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `conf_isp_ref0_clk_freq`, `conf_isp_ref1_clk_freq`, `conf_isp_ref2_clk_freq` | 1 | `0x0 0x55c11a9e 0x551b9816`; `0x2 0x55c11a9e 0x551b9816`; `0x1 0x55c11a9e 0x551b9816` |
| `PRFG` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `get_valid_perf_states` | 4 | `0x2d 0x2`; `0x2c 0x2`; `0x2f 0x102` |
| `PRFS` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `set_perf_state_floor` | 4 | `0x2d 0x2`; `0x2c 0x2`; `0x2f 0x102` |
| `SERG` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `service_state` | 1 |  |
| `SERV` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `service_gate` | 1 |  |
| `SRST` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `service_reset` | 1 |  |
| `Wait` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `wait_for_power_gate` | 1 | `0xd 0x0 0x0` |
| `clkG` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `clock_gate` | 1 |  |
| `cpuI` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `cpu_idle` | 6 |  |
| `pwrG` | [`/arm-io/pmgr`](../devicetree/root__arm-io__pmgr.md) | `power_gate` | 1 |  |
| `PMPC` | [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) | `pmp_control` | 1 |  |
| `btnR` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `button_hold`, `button_voldown`, `button_volup` | 1 | `0x62565550`; `0x6256444e`; `0x62484c44` |
| `keyR` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `get_pdod`, `get_vbus_detect`, `over-current-detection`, `over-current-read` | 3 | `0x706d4f43`; `0x706d4d53`; `0x42444431` |
| `keyW` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `external_standby`, `over-current-write` | 2 | `0x706d4d53`; `0x4d425345` |
| `pKR8` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `current-read`, `monitor-current-3v0`, `pmu_exton`, `rd_rose_pwr` | 4 | `0x61444352 0x4950646c 0x0`; `0x70634c44 0x0 0x80000`; `0x70634853 0x22000000 0xa0000` |
| `pKW4` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `bb_warm_reset`, `warm_reset` | 2 | `0x62706c69 0x1000000`; `0x62706c69 0x0` |
| `pKW8` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `bb_on`, `clock_enable`, `enable`, `mesa_pwr`, `pmu_exton_config`, `power`, `power_1v2_core`, `reset` | 8 | `0x70634c44 0x0 0xd0000`; `0x70634c44 0x0 0x80000`; `0x7063494f 0x800000 0x70000` |
| `VFWD` | [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) | `vote_force_wakeup_dram` | 1 | `0x0 0x0` |
| `ButD` | [`/buttons`](../devicetree/root__buttons.md) | `hid_event_dispatch`, `pmu_button` | 2 |  |
| `accP` | [`/port-magsafe-1`](../devicetree/root__port-magsafe-1.md) | `dock_parent` | 1 |  |
| `accP` | [`/port-usb-c-1`](../devicetree/root__port-usb-c-1.md) | `dock_parent`, `dock_wired` | 4 |  |
| `igvb` | [`/port-usb-c-1`](../devicetree/root__port-usb-c-1.md) | `ignore_vbus_drop` | 1 |  |
| `prst` | [`/port-usb-c-1`](../devicetree/root__port-usb-c-1.md) | `parrot_srst` | 1 |  |
| `SACA` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `saca`, `saca0`, `saca0b`, `saca0c`, `saca0d`, `saca1`, `saca1b`, `saca1c` | 6 | `0x6472616d`; `0x70726f78`; `0x6c636430` |
| `SACC` | [`/sacm-general`](../devicetree/root__sacm-general.md) | `sac` | 2 | `0x6c636430 0x6c636431 0x6c636432 0x6c636433`; `0x6472616d` |
| `SACA` | [`/sacm-jasper`](../devicetree/root__sacm-jasper.md) | `saca5` | 2 | `0x63616d47`; `0x63616d47` |
| `SACC` | [`/sacm-jasper`](../devicetree/root__sacm-jasper.md) | `jasper-sac` | 1 | `0x63616d47` |

# `/arm-io/pmgr`

- Name: `pmgr`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `48`
- compatible: `pmgr2,arch`
- device_type: `pmgr`
- Children (3): [`/arm-io/pmgr/pmgrtools`](root__arm-io__pmgr__pmgrtools.md), [`/arm-io/pmgr/clpc`](root__arm-io__pmgr__clpc.md), [`/arm-io/pmgr/ppm`](root__arm-io__pmgr__ppm.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `ApplePMGRv2` | `AppleARMIODevice` | [`com.apple.driver.ApplePMGR`](../kexts/com.apple.driver.ApplePMGR.md) | `pmgr2,arch` |

## Referenced by (32) [DT]

- [`/cpus/cpu0`](root__cpus__cpu0.md): function-enable_core `Core`
- [`/cpus/cpu0`](root__cpus__cpu0.md): function-cpu_idle `cpuI`
- [`/cpus/cpu1`](root__cpus__cpu1.md): function-enable_core `Core`
- [`/cpus/cpu1`](root__cpus__cpu1.md): function-cpu_idle `cpuI`
- [`/cpus/cpu2`](root__cpus__cpu2.md): function-enable_core `Core`
- [`/cpus/cpu2`](root__cpus__cpu2.md): function-cpu_idle `cpuI`
- [`/cpus/cpu3`](root__cpus__cpu3.md): function-enable_core `Core`
- [`/cpus/cpu3`](root__cpus__cpu3.md): function-cpu_idle `cpuI`
- [`/cpus/cpu4`](root__cpus__cpu4.md): function-enable_core `Core`
- [`/cpus/cpu4`](root__cpus__cpu4.md): function-cpu_idle `cpuI`
- [`/cpus/cpu5`](root__cpus__cpu5.md): function-enable_core `Core`
- [`/cpus/cpu5`](root__cpus__cpu5.md): function-cpu_idle `cpuI`
- [`/arm-io`](root__arm-io.md): function-service_gate `SERV`
- [`/arm-io`](root__arm-io.md): function-service_state `SERG`
- [`/arm-io`](root__arm-io.md): function-service_reset `SRST`
- [`/arm-io`](root__arm-io.md): function-power_gate `pwrG`
- [`/arm-io`](root__arm-io.md): function-clock_gate `clkG`
- [`/arm-io/error-handler/sac-error-handler`](root__arm-io__error-handler__sac-error-handler.md): function-avoid_perf_state `APRF`
- [`/arm-io/sep/iop-sep-nub`](root__arm-io__sep__iop-sep-nub.md): function-wait_for_power_gate `Wait`
- [`/arm-io/scaler0`](root__arm-io__scaler0.md): function-get_valid_perf_states `PRFG`
- [`/arm-io/scaler0`](root__arm-io__scaler0.md): function-device_reset `ARST`
- [`/arm-io/scaler0`](root__arm-io__scaler0.md): function-set_perf_state_floor `PRFS`
- [`/arm-io/jpeg`](root__arm-io__jpeg.md): function-get_valid_perf_states `PRFG`
- [`/arm-io/jpeg`](root__arm-io__jpeg.md): function-set_perf_state_floor `PRFS`
- [`/arm-io/isp`](root__arm-io__isp.md): function-conf_isp_ref0_clk_freq `ISPC`
- [`/arm-io/isp`](root__arm-io__isp.md): function-conf_isp_ref2_clk_freq `ISPC`
- [`/arm-io/isp`](root__arm-io__isp.md): function-conf_isp_ref1_clk_freq `ISPC`
- [`/arm-io/ave`](root__arm-io__ave.md): function-get_valid_perf_states `PRFG`
- [`/arm-io/ave`](root__arm-io__ave.md): function-clock_req_interrupt `CIRQ`
- [`/arm-io/ave`](root__arm-io__ave.md): function-set_perf_state_floor `PRFS`
- [`/arm-io/avd`](root__arm-io__avd.md): function-get_valid_perf_states `PRFG`
- [`/arm-io/avd`](root__arm-io__avd.md): function-set_perf_state_floor `PRFS`

## All properties (11) [DT]

- **`AAPL,phandle`**: `48` (`0x30`) → phandle of [`/arm-io/pmgr`](root__arm-io__pmgr.md)
- **`chiplet-count`**: `1` (`0x1`)
- **`clpc`**: `3` (`0x3`)
- **`compatible`**: `pmgr2,arch`
- **`device_type`**: `pmgr`
- **`name`**: `pmgr`
- **`pmc`**: `1` (`0x1`)
- **`pmc-ltr-ka`**: `1` (`0x1`)
- **`pmc-pmgr`**: `31` (`0x1f`)
- **`pmgr-ver`**: `2` (`0x2`)
- **`pmp`**: `2` (`0x2`)

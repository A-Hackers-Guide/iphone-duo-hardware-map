# `/arm-io/smc/iop-smc-nub/smc-pmu`

- Name: `smc-pmu`
- Parent: [`/arm-io/smc/iop-smc-nub`](root__arm-io__smc__iop-smc-nub.md)
- phandle: `159`
- compatible: `smc-pmu`
- device_type: `interrupt-controller`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSMCPMU` | `AppleSMCInterface` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) | `smc-pmu` |
| `AppleSMCPMU` | `AppleSMCInterface` | [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md) | `smc-pmu` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `pmu_button` | [`/buttons`](root__buttons.md) | `ButD` | `` |

## Referenced by (29) [DT]

- [`/arm-io/spi1/mesa`](root__arm-io__spi1__mesa.md): function-over-current-detection `keyR`
- [`/arm-io/spi1/mesa`](root__arm-io__spi1__mesa.md): function-monitor-current-3v0 `pKR8`
- [`/arm-io/spi1/mesa`](root__arm-io__spi1__mesa.md): function-mesa_pwr `pKW8`
- [`/arm-io/aop/iop-aop-nub/rose`](root__arm-io__aop__iop-aop-nub__rose.md): function-rose_pwr `pKW8`
- [`/arm-io/aop/iop-aop-nub/rose`](root__arm-io__aop__iop-aop-nub__rose.md): function-rose_reset `pKW8`
- [`/arm-io/aop/iop-aop-nub/rose`](root__arm-io__aop__iop-aop-nub__rose.md): function-rd_rose_pwr `pKR8`
- [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](root__arm-io__mtp__iop-mtp-nub__multi-touch2.md): function-clock_enable `pKW8`
- [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](root__arm-io__mtp__iop-mtp-nub__multi-touch2.md): function-reset `pKW8`
- [`/arm-io/mtp/iop-mtp-nub/multi-touch2`](root__arm-io__mtp__iop-mtp-nub__multi-touch2.md): function-power_1v2_core `pKW8`
- [`/arm-io/mtp/iop-mtp-nub/multi-touch`](root__arm-io__mtp__iop-mtp-nub__multi-touch.md): function-clock_enable `pKW8`
- [`/arm-io/mtp/iop-mtp-nub/multi-touch`](root__arm-io__mtp__iop-mtp-nub__multi-touch.md): function-reset `pKW8`
- [`/arm-io/mtp/iop-mtp-nub/multi-touch`](root__arm-io__mtp__iop-mtp-nub__multi-touch.md): function-power_1v2_core `pKW8`
- [`/arm-io/mtp/iop-mtp-nub/nova`](root__arm-io__mtp__iop-mtp-nub__nova.md): function-over-current-write `keyW`
- [`/arm-io/mtp/iop-mtp-nub/nova`](root__arm-io__mtp__iop-mtp-nub__nova.md): function-over-current-read `keyR`
- [`/arm-io/mtp/iop-mtp-nub/nova`](root__arm-io__mtp__iop-mtp-nub__nova.md): function-power `pKW8`
- [`/arm-io/mtp/iop-mtp-nub/nova`](root__arm-io__mtp__iop-mtp-nub__nova.md): function-current-read `pKR8`
- [`/arm-io/nub-spmi0/pmu-main`](root__arm-io__nub-spmi0__pmu-main.md): function-get_pdod `keyR`
- [`/arm-io/nub-spmi0/pmu-main`](root__arm-io__nub-spmi0__pmu-main.md): function-get_vbus_detect `keyR`
- [`/arm-io/nub-spmi0/pmu-main`](root__arm-io__nub-spmi0__pmu-main.md): function-external_standby `keyW`
- [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md): function-enable `pKW8`
- [`/arm-io/apcie/pci-bridge0`](root__arm-io__apcie__pci-bridge0.md): function-warm_reset `pKW4`
- [`/arm-io/apcie/pci-bridge0`](root__arm-io__apcie__pci-bridge0.md): function-reset `pKW8`
- [`/buttons`](root__buttons.md): function-button_volup `btnR`
- [`/buttons`](root__buttons.md): function-button_voldown `btnR`
- [`/buttons`](root__buttons.md): function-button_hold `btnR`
- [`/baseband`](root__baseband.md): function-pmu_exton_config `pKW8`
- [`/baseband`](root__baseband.md): function-bb_on `pKW8`
- [`/baseband`](root__baseband.md): function-bb_warm_reset `pKW4`
- [`/baseband`](root__baseband.md): function-pmu_exton `pKR8`

## All properties (14) [DT]

- **`#address-cells`**: `0` (`0x0`)
- **`#interrupt-cells`**: `1` (`0x1`)
- **`AAPL,phandle`**: `159` (`0x9f`) → phandle of [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md)
- **`compatible`**: `smc-pmu`
- **`device_type`**: `interrupt-controller`
- **`event_name-btn1`**: `hold`
- **`event_name-btn3`**: `action`
- **`event_name-btn4`**: `capture`
- **`event_name-gpio11`**: `charger`
- **`event_name-gpio16`**: `wifibt`
- **`event_name-gpio6`**: `baseband`
- **`function-pmu_button`**: `0x42757444000001c4` (u64; as two u32: `0x1c4`, `0x42757444`)
- **`interrupt-controller`**: (present, empty)
- **`name`**: `smc-pmu`

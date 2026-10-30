# `/arm-io/spi1/mesa`

- Name: `mesa`
- Parent: [`/arm-io/spi1`](root__arm-io__spi1.md)
- phandle: `77`
- compatible: `biosensor,mesa`
- device_type: `mesa`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleMesa` | `AppleARMSPIDevice` | [`com.apple.driver.AppleBiometricSensor`](../kexts/com.apple.driver.AppleBiometricSensor.md) | `biosensor,mesa` |
| `AppleSandDollar` | `AppleARMSPIDevice` | [`com.apple.driver.AppleBiometricSensor`](../kexts/com.apple.driver.AppleBiometricSensor.md) | `biosensor,mesa` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x0 0x1f4 0x8010100 0x0 0x14 0x0 0x0 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/nub-gpio`](root__arm-io__nub-gpio.md)

`12, 83886083`

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `ane1_power_func` | [`/arm-io/ane1`](root__arm-io__ane1.md) | `ANPW` | `` |
| `ane0_power_func` | [`/arm-io/ane0`](root__arm-io__ane0.md) | `ANPW` | `` |
| `over-current-detection` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `keyR` | `0x706d4f43` |
| `monitor-current-3v0` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKR8` | `0x61444352 0x4950646c 0x0` |
| `ane_power_func` | [`/arm-io/ane0`](root__arm-io__ane0.md) | `ANPW` | `` |
| `hid_event_dispatch` | [`/buttons`](root__buttons.md) | `ButD` | `` |
| `mesa_pwr` | [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md) | `pKW8` | `0x70634c44 0x0 0xd0000` |

## All properties (30) [DT]

- **`AAPL,phandle`**: `77` (`0x4d`) → phandle of [`/arm-io/spi1/mesa`](root__arm-io__spi1__mesa.md)
- **`compatible`**: `biosensor,mesa`
- **`device_type`**: `mesa`
- **`function-ane0_power_func`**: `0x414e50570000013e` (u64; as two u32: `0x13e`, `0x414e5057`)
- **`function-ane1_power_func`**: `0x414e50570000014a` (u64; as two u32: `0x14a`, `0x414e5057`)
- **`function-ane_power_func`**: `0x414e50570000013e` (u64; as two u32: `0x13e`, `0x414e5057`)
- **`function-hid_event_dispatch`**: `0x42757444000001c4` (u64; as two u32: `0x1c4`, `0x42757444`)
- **`function-mesa_pwr`**: 20 bytes
  - u32: `0x9f 0x704b5738 0x70634c44 0x0 0xd0000`
  - text inside: `8WKpDLcp`
  ```
  000000  9f 00 00 00 38 57 4b 70 44 4c 63 70 00 00 00 00  ....8WKpDLcp....
  000010  00 00 0d 00                                      ....
  ```
- **`function-monitor-current-3v0`**: 20 bytes
  - u32: `0x9f 0x704b5238 0x61444352 0x4950646c 0x0`
  - text inside: `8RKpRCDaldPI`
  ```
  000000  9f 00 00 00 38 52 4b 70 52 43 44 61 6c 64 50 49  ....8RKpRCDaldPI
  000010  00 00 00 00                                      ....
  ```
- **`function-over-current-detection`**: 12 bytes
  - u32: `0x9f 0x6b657952 0x706d4f43`
  - text inside: `RyekCOmp`
  ```
  000000  9f 00 00 00 52 79 65 6b 43 4f 6d 70              ....RyekCOmp
  ```
- **`interrupt-parent`**: `115` (`0x73`) → phandle of [`/arm-io/nub-gpio`](root__arm-io__nub-gpio.md)
- **`interrupts`**: `0x50000030000000c` (u64; as two u32: `0xc`, `0x5000003`)
- **`invert-menu-key`**: `1` (`0x1`)
- **`max-scan-time`**: `78643` (`0x13333`)
- **`mesaType`**: `2` (`0x2`)
- **`monitor-current-3v0-count`**: `3` (`0x3`)
- **`monitor-current-3v0-threshold`**: `130` (`0x82`)
- **`monitor-current-avg-count`**: `1` (`0x1`)
- **`monitor-enable-power-down`**: `0` (`0x0`)
- **`monitor-power-avg-count`**: `20` (`0x14`)
- **`monitor-power-interval`**: `1000` (`0x3e8`)
- **`monitor-power-threshold`**: `190` (`0xbe`)
- **`name`**: `mesa`
- **`power-off-delay`**: `10` (`0xa`)
- **`power-on-delay`**: `7` (`0x7`)
- **`reg`**: 32 bytes
  - u32: `0x0 0x1f4 0x8010100 0x0 0x14 0x0 0x0 0x0`
  ```
  000000  00 00 00 00 f4 01 00 00 00 01 01 08 00 00 00 00  ................
  000010  14 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  ................
  ```
- **`scan-timer-reset-time`**: `39321` (`0x9999`)
- **`sensor-id`**: `13144` (`0x3358`)
- **`spi-frequency`**: `8000000` (`0x7a1200`)
- **`time-between-scans`**: `131072` (`0x20000`)

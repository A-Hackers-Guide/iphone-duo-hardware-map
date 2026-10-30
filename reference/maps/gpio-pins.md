# GPIO pin map

GPIO pins assigned through `function-*` references and GPIO interrupts, per controller. `gpio-*` properties are decoded separately in the section "Pins named by `gpio-*` properties" below. For `function-*` references the first argument is read as the pin number and the remaining words as configuration/flags; for GPIO interrupts the interrupt words are shown raw (pin, then trigger flags). Physical pad names and board routing are not in the evidence. **[DT]**


## [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md)

8 pin functions.

| Pin | Device | Function | Code | Config words |
|---|---|---|---|---|
| 0 | [`/arm-io/aop/iop-aop-nub/gnss`](../devicetree/root__arm-io__aop__iop-aop-nub__gnss.md) | `gnss-time-mark` | `GPIO` | `0x101` |
| 6 | [`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) | `enable` | `GPIO` | `0x101` |
| 9 | [`/arm-io/mt-bt-timestamp-sync`](../devicetree/root__arm-io__mt-bt-timestamp-sync.md) | `timestamp_sync` | `GPIO` | `0x2000002` |
| 12 | [`/arm-io/aop/iop-aop-nub/rose`](../devicetree/root__arm-io__aop__iop-aop-nub__rose.md) | `rose_coredump` | `GPIO` | `0x101` |
| 16 | [`/baseband`](../devicetree/root__baseband.md) | `reset_det` | `GPIO` | `0x0` |
| 64 | [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) | `perst` | `GPIO` | `0x0` |
| 66 | [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) | `perst` | `GPIO` | `0x0` |
| 87 | [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `reset` | `GPIO` | `0x10001` |

## [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md)

13 pin functions.

| Pin | Device | Function | Code | Config words |
|---|---|---|---|---|
| 21 | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) | `spi0_mosi_config` | `GPIO` | `0x10001` |
| 22 | [`/arm-io/ans`](../devicetree/root__arm-io__ans.md) | `spi0_sclk_config` | `GPIO` | `0x10001` |
| 64 | [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) | `debug_gpio` | `GPIO` | `0x101` |
| 64 | [`/arm-io/wdt`](../devicetree/root__arm-io__wdt.md) | `panic_notify` | `GPIO` | `0x100` |
| 66 | [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) | `tx` | `GPIO` | `0x102` |
| 67 | [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) | `rx` | `GPIO` | `0x102` |
| 98 | [`/arm-io/aod2`](../devicetree/root__arm-io__aod2.md) | `aod_swdio` | `GPIO` | `0x100` |
| 98 | [`/arm-io/aod4`](../devicetree/root__arm-io__aod4.md) | `aod_swdio` | `GPIO` | `0x100` |
| 104 | [`/arm-io/aod2`](../devicetree/root__arm-io__aod2.md) | `aod_swclk` | `GPIO` | `0x101` |
| 104 | [`/arm-io/aod4`](../devicetree/root__arm-io__aod4.md) | `aod_swclk` | `GPIO` | `0x101` |
| 105 | [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) | `boot_measurements` | `GPIO` | `0x101` |
| 128 | [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) | `se_boot_measurements` | `GPIO` | `0x101` |
| 131 | [`/arm-io/aop-spmi0/hammerfest-spmi/hammerfest`](../devicetree/root__arm-io__aop-spmi0__hammerfest-spmi__hammerfest.md) | `boot_measurements` | `GPIO` | `0x101` |

2 devices take interrupts from this controller.

| Device | Interrupt words |
|---|---|
| [`/arm-io/i2c2/audio-codec`](../devicetree/root__arm-io__i2c2__audio-codec.md) | `134 1` |
| [`/arm-io/aop-spmi0/stockholm-spmi/stockholm`](../devicetree/root__arm-io__aop-spmi0__stockholm-spmi__stockholm.md) | `142 2` |

## [`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md)

3 pin functions.

| Pin | Device | Function | Code | Config words |
|---|---|---|---|---|
| 5 | [`/arm-io/aod3`](../devicetree/root__arm-io__aod3.md) | `aod_swclk` | `GPIO` | `0x100` |
| 8 | [`/arm-io/aod3`](../devicetree/root__arm-io__aod3.md) | `aod_swdio` | `GPIO` | `0x101` |
| 22 | [`/centauri`](../devicetree/root__centauri.md) | `error_detect` | `GPIO` | `0x100` |

2 devices take interrupts from this controller.

| Device | Interrupt words |
|---|---|
| [`/arm-io/spi1/mesa`](../devicetree/root__arm-io__spi1__mesa.md) | `12 83886083` |
| [`/centauri`](../devicetree/root__centauri.md) | `22 100663300` |

## Controller sizes

| Controller | `#gpio-pins` | `#gpio-int-groups` |
|---|---|---|
| [`/arm-io/gpio0`](../devicetree/root__arm-io__gpio0.md) | 214 | 7 |
| [`/arm-io/aop-gpio`](../devicetree/root__arm-io__aop-gpio.md) | 95 | 7 |
| [`/arm-io/nub-gpio`](../devicetree/root__arm-io__nub-gpio.md) | 32 | 7 |
| [`/arm-io/smc-gpio`](../devicetree/root__arm-io__smc-gpio.md) | 6 | 7 |
| [`/arm-io/mtp-gpio`](../devicetree/root__arm-io__mtp-gpio.md) | 18 | 7 |
| [`/arm-io/secure-repair`](../devicetree/root__arm-io__secure-repair.md) | 95 | 7 |

## Pins named by `gpio-*` properties

Layout: pin number, a flags word, then a controller tag (`AP` = the AP GPIO block, `AOP` = the always-on block).

| Device | Property | Controller tag | Pin | Flags |
|---|---|---|---|---|
| [`/arm-io/i2c2`](../devicetree/root__arm-io__i2c2.md) | `gpio-iic_scl` | `AP` | 202 | `0x00010102` |
| [`/arm-io/i2c2`](../devicetree/root__arm-io__i2c2.md) | `gpio-iic_sda` | `AP` | 203 | `0x00010102` |
| [`/arm-io/i2c3`](../devicetree/root__arm-io__i2c3.md) | `gpio-iic_scl` | `AP` | 200 | `0x00010102` |
| [`/arm-io/i2c3`](../devicetree/root__arm-io__i2c3.md) | `gpio-iic_sda` | `AP` | 201 | `0x00010102` |
| [`/arm-io/i2c4`](../devicetree/root__arm-io__i2c4.md) | `gpio-iic_scl` | `AP` | 210 | `0x00010102` |
| [`/arm-io/i2c4`](../devicetree/root__arm-io__i2c4.md) | `gpio-iic_sda` | `AP` | 211 | `0x00010102` |
| [`/arm-io/secure-repair`](../devicetree/root__arm-io__secure-repair.md) | `gpio-repair_en` | `AOP` | 90 | `0x00000101` |

## PMU GPIO event names

| Device | GPIO | Event |
|---|---|---|
| [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | 6 | `baseband` |
| [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | 11 | `charger` |
| [`/arm-io/smc/iop-smc-nub/smc-pmu`](../devicetree/root__arm-io__smc__iop-smc-nub__smc-pmu.md) | 16 | `wifibt` |

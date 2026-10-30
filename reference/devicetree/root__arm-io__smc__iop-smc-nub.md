# `/arm-io/smc/iop-smc-nub`

- Name: `iop-smc-nub`
- Parent: [`/arm-io/smc`](root__arm-io__smc.md)
- phandle: `158`
- compatible: `iop-nub,rtbuddy-v2`
- Children (7): [`/arm-io/smc/iop-smc-nub/smc-pmu`](root__arm-io__smc__iop-smc-nub__smc-pmu.md), [`/arm-io/smc/iop-smc-nub/smc-charger`](root__arm-io__smc__iop-smc-nub__smc-charger.md), [`/arm-io/smc/iop-smc-nub/smc-ext-charger`](root__arm-io__smc__iop-smc-nub__smc-ext-charger.md), [`/arm-io/smc/iop-smc-nub/smc-aop`](root__arm-io__smc__iop-smc-nub__smc-aop.md), [`/arm-io/smc/iop-smc-nub/smc-power-out`](root__arm-io__smc__iop-smc-nub__smc-power-out.md), [`/arm-io/smc/iop-smc-nub/smc-acam`](root__arm-io__smc__iop-smc-nub__smc-acam.md), [`/arm-io/smc/iop-smc-nub/smc-charger-util`](root__arm-io__smc__iop-smc-nub__smc-charger-util.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `RTBuddy` | `AppleA7IOPNub` | [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md) | `iop-nub,rtbuddy-v2` |

## All properties (17) [DT]

- **`AAPL,phandle`**: `158` (`0x9e`) → phandle of [`/arm-io/smc/iop-smc-nub`](root__arm-io__smc__iop-smc-nub.md)
- **`cold-boot-after-hibernate`**: (present, empty)
- **`compatible`**: `iop-nub,rtbuddy-v2`
- **`continuous-time`**: (present, empty)
- **`coredump-active-only`**: (present, empty)
- **`coredump-enable`**: `64` (`0x40`)
- **`firmware-name`**: `t8160smc`
- **`name`**: `iop-smc-nub`
- **`no-hibernate-sleep`**: (present, empty)
- **`no-shutdown`**: `1` (`0x1`)
- **`pre-loaded`**: `0` (`0x0`)
- **`quiesced`**: (present, empty)
- **`region-base`**: `0x28de00000` (u64; as two u32: `0x8de00000`, `0x2`)
- **`region-size`**: `0x140000` (u64; as two u32: `0x140000`, `0x0`)
- **`sptm-allow-reg`**: 16 bytes
  - u32: `0x8de00000 0x2 0x140000 0x0`
  ```
  000000  00 00 e0 8d 02 00 00 00 00 00 14 00 00 00 00 00  ................
  ```
- **`user-power-managed`**: `1` (`0x1`)
- **`watchdog-enable`**: (present, empty)

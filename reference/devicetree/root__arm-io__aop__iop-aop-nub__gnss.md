# `/arm-io/aop/iop-aop-nub/gnss`

- Name: `gnss`
- Parent: [`/arm-io/aop/iop-aop-nub`](root__arm-io__aop__iop-aop-nub.md)
- phandle: `104`
- device_type: `gnss`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSPUGNSSDriver` | `AppleSPUAppInterface` | [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md) | `gnss` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `gnss-time-mark` | [`/arm-io/aop-gpio`](root__arm-io__aop-gpio.md) | `GPIO` | `0x0 0x101` |

## All properties (5) [DT]

- **`AAPL,phandle`**: `104` (`0x68`) → phandle of [`/arm-io/aop/iop-aop-nub/gnss`](root__arm-io__aop__iop-aop-nub__gnss.md)
- **`ap-time-mark-with-boot-arg`**: (present, empty)
- **`device_type`**: `gnss`
- **`function-gnss-time-mark`**: 16 bytes
  - u32: `0x72 0x4750494f 0x0 0x101`
  - text inside: `OIPG`
  ```
  000000  72 00 00 00 4f 49 50 47 00 00 00 00 01 01 00 00  r...OIPG........
  ```
- **`name`**: `gnss`

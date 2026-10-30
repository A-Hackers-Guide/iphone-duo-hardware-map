# `/arm-io/i2c3/mogul-display`

- Name: `mogul-display`
- Parent: [`/arm-io/i2c3`](root__arm-io__i2c3.md)
- phandle: `193`
- compatible: `mogul,a1222`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `MogulAuthI2CRelayInterface` | `AppleARMIICDevice` | [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md) | `mogul,a1222` |
| `MogulAuthSMCRelayInterface` | `AppleSMCInterface` | [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md) | `mogul,a1222` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x10 0x9c4 0x0 0x0` | | |

## All properties (8) [DT]

- **`AAPL,phandle`**: `193` (`0xc1`) → phandle of [`/arm-io/i2c3/mogul-display`](root__arm-io__i2c3__mogul-display.md)
- **`compatible`**: `mogul,a1222`
- **`component-index`**: `1` (`0x1`)
- **`iboot-auth`**: (present, empty)
- **`ic-auth-type`**: `196608` (`0x30000`)
- **`name`**: `mogul-display`
- **`reg`**: 16 bytes
  - u32: `0x10 0x9c4 0x0 0x0`
  ```
  000000  10 00 00 00 c4 09 00 00 00 00 00 00 00 00 00 00  ................
  ```
- **`wakeup-data`**: 12 bytes
  - u32: `0x0 0x2faf080 0xbb8`
  ```
  000000  00 00 00 00 80 f0 fa 02 b8 0b 00 00              ............
  ```

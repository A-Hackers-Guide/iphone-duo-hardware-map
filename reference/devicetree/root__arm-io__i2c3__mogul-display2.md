# `/arm-io/i2c3/mogul-display2`

- Name: `mogul-display2`
- Parent: [`/arm-io/i2c3`](root__arm-io__i2c3.md)
- phandle: `194`
- compatible: `mogul,a1222`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `MogulAuthI2CRelayInterface` | `AppleARMIICDevice` | [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md) | `mogul,a1222` |
| `MogulAuthSMCRelayInterface` | `AppleSMCInterface` | [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md) | `mogul,a1222` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x60 0x9c4 0x0 0x0` | | |

## All properties (8) [DT]

- **`AAPL,phandle`**: `194` (`0xc2`) → phandle of [`/arm-io/i2c3/mogul-display2`](root__arm-io__i2c3__mogul-display2.md)
- **`compatible`**: `mogul,a1222`
- **`component-index`**: `2` (`0x2`)
- **`iboot-auth`**: (present, empty)
- **`ic-auth-type`**: `196608` (`0x30000`)
- **`name`**: `mogul-display2`
- **`reg`**: 16 bytes
  - u32: `0x60 0x9c4 0x0 0x0`
  ```
  000000  60 00 00 00 c4 09 00 00 00 00 00 00 00 00 00 00  `...............
  ```
- **`wakeup-data`**: 12 bytes
  - u32: `0x0 0x2faf080 0xbb8`
  ```
  000000  00 00 00 00 80 f0 fa 02 b8 0b 00 00              ............
  ```

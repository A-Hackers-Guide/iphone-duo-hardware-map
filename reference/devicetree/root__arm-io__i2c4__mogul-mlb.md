# `/arm-io/i2c4/mogul-mlb`

- Name: `mogul-mlb`
- Parent: [`/arm-io/i2c4`](root__arm-io__i2c4.md)
- phandle: `196`
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

## All properties (6) [DT]

- **`AAPL,phandle`**: `196` (`0xc4`) → phandle of [`/arm-io/i2c4/mogul-mlb`](root__arm-io__i2c4__mogul-mlb.md)
- **`compatible`**: `mogul,a1222`
- **`ic-auth-type`**: `262144` (`0x40000`)
- **`name`**: `mogul-mlb`
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

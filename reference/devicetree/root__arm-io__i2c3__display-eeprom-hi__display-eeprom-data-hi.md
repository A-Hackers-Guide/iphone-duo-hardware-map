# `/arm-io/i2c3/display-eeprom-hi/display-eeprom-data-hi`

- Name: `display-eeprom-data-hi`
- Parent: [`/arm-io/i2c3/display-eeprom-hi`](root__arm-io__i2c3__display-eeprom-hi.md)
- phandle: `187`
- compatible: `diagnostic-data,format1`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleDiagnosticDataAccessReadOnly` | `AppleARMNORFlashDevice` | [`com.apple.driver.AppleDiagnosticDataAccessReadOnly`](../kexts/com.apple.driver.AppleDiagnosticDataAccessReadOnly.md) | `diagnostic-data,format1` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0x0` | `0xe280` (57,984 B) | not memory-mapped (bus address) |

## All properties (6) [DT]

- **`AAPL,phandle`**: `187` (`0xbb`) → phandle of [`/arm-io/i2c3/display-eeprom-hi/display-eeprom-data-hi`](root__arm-io__i2c3__display-eeprom-hi__display-eeprom-data-hi.md)
- **`compatible`**: `diagnostic-data,format1`
- **`diagnostic-data-partial-region`**: `1` (`0x1`)
- **`diagnostic-data-regions`**: `2` (`0x2`)
- **`name`**: `display-eeprom-data-hi`
- **`reg`**: `0xe28000000000` (u64; as two u32: `0x0`, `0xe280`)

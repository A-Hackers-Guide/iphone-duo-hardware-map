# `/arm-io/i2c3/display-eeprom-2-hi/display-eeprom-data-2-hi`

- Name: `display-eeprom-data-2-hi`
- Parent: [`/arm-io/i2c3/display-eeprom-2-hi`](root__arm-io__i2c3__display-eeprom-2-hi.md)
- phandle: `192`
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

- **`AAPL,phandle`**: `192` (`0xc0`) → phandle of [`/arm-io/i2c3/display-eeprom-2-hi/display-eeprom-data-2-hi`](root__arm-io__i2c3__display-eeprom-2-hi__display-eeprom-data-2-hi.md)
- **`compatible`**: `diagnostic-data,format1`
- **`diagnostic-data-partial-region`**: `1` (`0x1`)
- **`diagnostic-data-regions`**: `3` (`0x3`)
- **`name`**: `display-eeprom-data-2-hi`
- **`reg`**: `0xe28000000000` (u64; as two u32: `0x0`, `0xe280`)

# `/arm-io/i2c3/display-eeprom/display-eeprom-data`

- Name: `display-eeprom-data`
- Parent: [`/arm-io/i2c3/display-eeprom`](root__arm-io__i2c3__display-eeprom.md)
- phandle: `184`
- compatible: `diagnostic-data,format1`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleDiagnosticDataAccessReadOnly` | `AppleARMNORFlashDevice` | [`com.apple.driver.AppleDiagnosticDataAccessReadOnly`](../kexts/com.apple.driver.AppleDiagnosticDataAccessReadOnly.md) | `diagnostic-data,format1` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | `0xc80` | `0xf380` (62,336 B) | not memory-mapped (bus address) |

## All properties (6) [DT]

- **`AAPL,phandle`**: `184` (`0xb8`) → phandle of [`/arm-io/i2c3/display-eeprom/display-eeprom-data`](root__arm-io__i2c3__display-eeprom__display-eeprom-data.md)
- **`compatible`**: `diagnostic-data,format1`
- **`diagnostic-data-partial-region`**: `0` (`0x0`)
- **`diagnostic-data-regions`**: `2` (`0x2`)
- **`name`**: `display-eeprom-data`
- **`reg`**: `0xf38000000c80` (u64; as two u32: `0xc80`, `0xf380`)

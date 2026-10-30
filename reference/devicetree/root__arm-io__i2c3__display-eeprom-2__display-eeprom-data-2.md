# `/arm-io/i2c3/display-eeprom-2/display-eeprom-data-2`

- Name: `display-eeprom-data-2`
- Parent: [`/arm-io/i2c3/display-eeprom-2`](root__arm-io__i2c3__display-eeprom-2.md)
- phandle: `189`
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

- **`AAPL,phandle`**: `189` (`0xbd`) → phandle of [`/arm-io/i2c3/display-eeprom-2/display-eeprom-data-2`](root__arm-io__i2c3__display-eeprom-2__display-eeprom-data-2.md)
- **`compatible`**: `diagnostic-data,format1`
- **`diagnostic-data-partial-region`**: `0` (`0x0`)
- **`diagnostic-data-regions`**: `3` (`0x3`)
- **`name`**: `display-eeprom-data-2`
- **`reg`**: `0xf38000000c80` (u64; as two u32: `0xc80`, `0xf380`)

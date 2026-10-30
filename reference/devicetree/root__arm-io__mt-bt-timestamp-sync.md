# `/arm-io/mt-bt-timestamp-sync`

- Name: `mt-bt-timestamp-sync`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `177`
- compatible: `timestamp-sync`
- device_type: `timestamp-sync`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleMultitouchTimestampSync` | `IOService` | [`com.apple.driver.AppleMultitouchDriver`](../kexts/com.apple.driver.AppleMultitouchDriver.md) | `timestamp-sync` |

## Functions it calls on other nodes [DT]

| Function | Provider | Code | Arguments |
|---|---|---|---|
| `timestamp_sync` | [`/arm-io/aop-gpio`](root__arm-io__aop-gpio.md) | `GPIO` | `0x9 0x2000002` |

## All properties (5) [DT]

- **`AAPL,phandle`**: `177` (`0xb1`) → phandle of [`/arm-io/mt-bt-timestamp-sync`](root__arm-io__mt-bt-timestamp-sync.md)
- **`compatible`**: `timestamp-sync`
- **`device_type`**: `timestamp-sync`
- **`function-timestamp_sync`**: 16 bytes
  - u32: `0x72 0x4750494f 0x9 0x2000002`
  - text inside: `OIPG`
  ```
  000000  72 00 00 00 4f 49 50 47 09 00 00 00 02 00 00 02  r...OIPG........
  ```
- **`name`**: `mt-bt-timestamp-sync`

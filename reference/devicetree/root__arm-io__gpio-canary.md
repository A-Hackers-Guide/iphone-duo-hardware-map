# `/arm-io/gpio-canary`

- Name: `gpio-canary`
- Parent: [`/arm-io`](root__arm-io.md)
- phandle: `445`
- compatible: `gpio-canary,t8101`
- device_type: `canary`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleGPIOCanary` | `IOService` | [`com.apple.driver.AppleGPIOCanary`](../kexts/com.apple.driver.AppleGPIOCanary.md) | `gpio-canary,t8101` |

## All properties (4) [DT]

- **`AAPL,phandle`**: `445` (`0x1bd`) → phandle of [`/arm-io/gpio-canary`](root__arm-io__gpio-canary.md)
- **`compatible`**: `gpio-canary,t8101`
- **`device_type`**: `canary`
- **`name`**: `gpio-canary`

# `/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main`

- Name: `sgpio-bridge-pmu-main`
- Parent: [`/arm-io/nub-spmi0/pmu-main`](root__arm-io__nub-spmi0__pmu-main.md)
- phandle: `199`
- compatible: `sgpio-bridge`
- Children (1): [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md)

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleSGPIOHostBridgeController` | `AppleDialogSPMIPMUNub` | [`com.apple.driver.AppleSGPIO`](../kexts/com.apple.driver.AppleSGPIO.md) | `sgpio-bridge` |

## All properties (5) [DT]

- **`AAPL,phandle`**: `199` (`0xc7`) → phandle of [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main`](root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main.md)
- **`bridge-offset`**: `56592` (`0xdd10`)
- **`compatible`**: `sgpio-bridge`
- **`name`**: `sgpio-bridge-pmu-main`
- **`sgpio-bus-id`**: `0` (`0x0`)

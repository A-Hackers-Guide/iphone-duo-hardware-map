# `/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`

- Name: `pmu-secondary`
- Parent: [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main`](root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main.md)
- phandle: `200`
- compatible: `pmu,spmi`, `pmu,fairmont`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `ApplePMUFirmwareDriver` | `AppleARMSPMIDevice` | [`com.apple.driver.ApplePMUFirmwareDriver`](../kexts/com.apple.driver.ApplePMUFirmwareDriver.md) | `pmu,spmi` |
| `AppleDialogSPMIPMU` | `AppleARMSPMIDevice` | [`com.apple.driver.AppleSPMIPMU`](../kexts/com.apple.driver.AppleSPMIPMU.md) | `pmu,spmi` |

## Register windows [DT]

| # | Bus address | Size | CPU physical |
|---|---|---|---|
| 0 | raw `0x1 0x3 0x0 0x4 0x0 0x0` | | |

## Interrupts [DT]

Controller: [`/arm-io/nub-spmi0`](root__arm-io__nub-spmi0.md)

`126`

## All properties (12) [DT]

- **`AAPL,phandle`**: `200` (`0xc8`) → phandle of [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md)
- **`compatible`**: `pmu,spmi`, `pmu,fairmont`
- **`fw-host-irq-address`**: `11016` (`0x2b08`)
- **`fw-mcom-address`**: `11104` (`0x2b60`)
- **`fw-mcom-int-index`**: `0` (`0x0`)
- **`has-fw`**: `1` (`0x1`)
- **`hw-name`**: `fairmont`
- **`info-leg_scrpad`**: `63488` (`0xf800`)
- **`interrupt-parent`**: `197` (`0xc5`) → phandle of [`/arm-io/nub-spmi0`](root__arm-io__nub-spmi0.md)
- **`interrupts`**: `126` (`0x7e`)
- **`name`**: `pmu-secondary`
- **`reg`**: 24 bytes
  - u32: `0x1 0x3 0x0 0x4 0x0 0x0`
  ```
  000000  01 00 00 00 03 00 00 00 00 00 00 00 04 00 00 00  ................
  000010  00 00 00 00 00 00 00 00                          ........
  ```

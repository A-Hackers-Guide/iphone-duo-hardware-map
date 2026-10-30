# `/arm-io/apcie/pci-bridge0/centauri-alpha`

- Name: `centauri-alpha`
- Parent: [`/arm-io/apcie/pci-bridge0`](root__arm-io__apcie__pci-bridge0.md)
- phandle: `417`
- device_type: `pcie-device`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (13) [DT]

- **`#address-cells`**: `1` (`0x1`)
- **`#size-cells`**: `0` (`0x0`)
- **`AAPL,phandle`**: `417` (`0x1a1`) → phandle of [`/arm-io/apcie/pci-bridge0/centauri-alpha`](root__arm-io__apcie__pci-bridge0__centauri-alpha.md)
- **`AAPL,unit-string`**: `00000001`
- **`built-in`**: (present, empty)
- **`device_type`**: `pcie-device`
- **`iommu-parent`**: `423` (`0x1a7`) → phandle of [`/arm-io/dart-apcie0/mapper-apcie0-alpha`](root__arm-io__dart-apcie0__mapper-apcie0-alpha.md)
- **`local-mac-address`**: `macaddr/wifiaddr,syscfg/WMac/6,zeroes/6` *(placeholder, filled in by iBoot at boot)*
- **`name`**: `centauri-alpha`
- **`network-interface-unit-en`**: `0` (`0x0`)
- **`pci-aspm-default`**: `2` (`0x2`)
- **`pci-max-latency`**: `268963848` (`0x10081008`)
- **`pci-skip-rematch-reset`**: (present, empty)

# `/arm-io/apcie/pci-bridge0/centauri-beta`

- Name: `centauri-beta`
- Parent: [`/arm-io/apcie/pci-bridge0`](root__arm-io__apcie__pci-bridge0.md)
- phandle: `418`
- device_type: `pcie-device`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (11) [DT]

- **`#address-cells`**: `1` (`0x1`)
- **`#size-cells`**: `0` (`0x0`)
- **`AAPL,phandle`**: `418` (`0x1a2`) → phandle of [`/arm-io/apcie/pci-bridge0/centauri-beta`](root__arm-io__apcie__pci-bridge0__centauri-beta.md)
- **`AAPL,unit-string`**: `00000002`
- **`built-in`**: (present, empty)
- **`device_type`**: `pcie-device`
- **`iommu-parent`**: `424` (`0x1a8`) → phandle of [`/arm-io/dart-apcie0/mapper-apcie0-beta`](root__arm-io__dart-apcie0__mapper-apcie0-beta.md)
- **`name`**: `centauri-beta`
- **`pci-aspm-default`**: `2` (`0x2`)
- **`pci-max-latency`**: `268963848` (`0x10081008`)
- **`pci-skip-rematch-reset`**: (present, empty)

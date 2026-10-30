# `/arm-io/apcie/pci-bridge0/centauri-control`

- Name: `centauri-control`
- Parent: [`/arm-io/apcie/pci-bridge0`](root__arm-io__apcie__pci-bridge0.md)
- phandle: `416`
- device_type: `pcie-device`

## Kernel driver [KC]

No personality names this node. It is bound through its parent, by property match, by DriverKit or an exclave, or it is structural.

## All properties (14) [DT]

- **`#address-cells`**: `1` (`0x1`)
- **`#size-cells`**: `0` (`0x0`)
- **`AAPL,phandle`**: `416` (`0x1a0`) → phandle of [`/arm-io/apcie/pci-bridge0/centauri-control`](root__arm-io__apcie__pci-bridge0__centauri-control.md)
- **`AAPL,unit-string`**: `00000000`
- **`built-in`**: (present, empty)
- **`device_type`**: `pcie-device`
- **`iommu-parent`**: `422` (`0x1a6`) → phandle of [`/arm-io/dart-apcie0/mapper-apcie0-control`](root__arm-io__dart-apcie0__mapper-apcie0-control.md)
- **`mem-io-timeout`**: 12 bytes
  - u32: `0x0 0x2000000 0x4004e20`
  ```
  000000  00 00 00 00 00 00 00 02 20 4e 00 04              ........ N..
  ```
- **`name`**: `centauri-control`
- **`pci-aspm-default`**: `2` (`0x2`)
- **`pci-l1ss-enable`**: `1079312399` (`0x4055000f`)
- **`pci-max-latency`**: `268963848` (`0x10081008`)
- **`pci-skip-rematch-reset`**: (present, empty)
- **`system-events-required`**: `0` (`0x0`)

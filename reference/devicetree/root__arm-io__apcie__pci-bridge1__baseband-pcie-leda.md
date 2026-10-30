# `/arm-io/apcie/pci-bridge1/baseband-pcie-leda`

- Name: `baseband-pcie-leda`
- Parent: [`/arm-io/apcie/pci-bridge1`](root__arm-io__apcie__pci-bridge1.md)
- phandle: `420`
- device_type: `pcie-device`

## Kernel driver [KC]

| IOClass | Provider | kext | matched on |
|---|---|---|---|
| `AppleConvergedPCILedaBB` | `IOPCIDevice` | [`com.apple.driver.AppleConvergedIPCBBControl`](../kexts/com.apple.driver.AppleConvergedIPCBBControl.md) | `baseband-pcie-leda` |

## All properties (12) [DT]

- **`#address-cells`**: `1` (`0x1`)
- **`#size-cells`**: `0` (`0x0`)
- **`AAPL,phandle`**: `420` (`0x1a4`) → phandle of [`/arm-io/apcie/pci-bridge1/baseband-pcie-leda`](root__arm-io__apcie__pci-bridge1__baseband-pcie-leda.md)
- **`AAPL,unit-string`**: `00000000`
- **`device_type`**: `pcie-device`
- **`iommu-parent`**: `430` (`0x1ae`) → phandle of [`/arm-io/dart-apcie1/mapper-apcie1`](root__arm-io__dart-apcie1__mapper-apcie1.md)
- **`name`**: `baseband-pcie-leda`
- **`pci-aspm-default`**: `2` (`0x2`)
- **`pci-l1ss-enable`**: `1079312399` (`0x4055000f`)
- **`pci-max-latency`**: `268963848` (`0x10081008`)
- **`pci-msi-flags`**: `1` (`0x1`)
- **`pci-msi-limit`**: `8` (`0x8`)

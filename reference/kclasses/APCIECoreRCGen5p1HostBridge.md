# `APCIECoreRCGen5p1HostBridge`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md)
- Object size: `0x178` (376 bytes)
- Metaclass: `0xfffffe000b9d0bf8`; metaclass vtable `0xfffffe00082658a0`; class vtable `0xfffffe0008265178`
- Registration (init): `0xfffffe000988fee8`
- Superclasses: [`ApplePCIEHostBridge`](ApplePCIEHostBridge.md) → [`IOPCI2PCIBridge`](IOPCI2PCIBridge.md) → [`IOPCIBridge`](IOPCIBridge.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `APCIECoreRCGen5p1HostBridge` in [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md): `IOProviderClass` = `IOPCIDevice`, `IONameMatch` = `apcie-bridge`, `IOProbeScore` = `5000`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/apcie/pci-bridge0`](../devicetree/root__arm-io__apcie__pci-bridge0.md) on `apcie-bridge`
- [`/arm-io/apcie/pci-bridge1`](../devicetree/root__arm-io__apcie__pci-bridge1.md) on `apcie-bridge`

## Strings in its kext that name it (4)

- `APCIECoreRCGen5p1HostBridge`
- `site.APCIECoreRCGen5p1HostBridge`
- `APCIECoreRCGen5p1HostBridge.cpp`
- `virtual bool APCIECoreRCGen5p1HostBridge::start(IOService *)`

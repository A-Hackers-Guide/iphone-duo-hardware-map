# `AppleT8160PCIe`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md)
- Object size: `0x270` (624 bytes)
- Metaclass: `0xfffffe000b9d0bd0`; metaclass vtable `0xfffffe00082650e0`; class vtable `0xfffffe00082648b0`
- Registration (init): `0xfffffe000988ebc8`
- Superclasses: [`APCIECoreRCGen5p1`](APCIECoreRCGen5p1.md) → [`APCIECoreRCGen5`](APCIECoreRCGen5.md) → [`AppleEmbeddedPCIE`](AppleEmbeddedPCIE.md) → [`IOPCIHostBridge`](IOPCIHostBridge.md) → [`IOPCIBridge`](IOPCIBridge.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8160PCIe` in [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `apcie,t8160`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/apcie`](../devicetree/root__arm-io__apcie.md) on `apcie,t8160`

## Strings in its kext that name it (7)

- `virtual bool AppleT8160PCIe::configure(IOService *)`
- `site.AppleT8160PCIePort`
- `AppleT8160PCIe.cpp`
- `AppleT8160PCIePort`
- `AppleT8160PCIePort.cpp`
- `AppleT8160PCIe`
- `site.AppleT8160PCIe`

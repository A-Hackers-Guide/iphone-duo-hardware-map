# `APCIECoreRCGen5p1`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md)
- Object size: `0x250` (592 bytes)
- Metaclass: `0xfffffe000b9d0ce8`; metaclass vtable `0xfffffe0008267d00`; class vtable `0xfffffe00082674d0`
- Registration (init): `0xfffffe00098a3678`
- Superclasses: [`APCIECoreRCGen5`](APCIECoreRCGen5.md) → [`AppleEmbeddedPCIE`](AppleEmbeddedPCIE.md) → [`IOPCIHostBridge`](IOPCIHostBridge.md) → [`IOPCIBridge`](IOPCIBridge.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleT8160PCIe`](AppleT8160PCIe.md) — `com.apple.driver.AppleT8160PCIe`

## Strings in its kext that name it (13)

- `APCIECoreRCGen5p1`
- `APCIECoreRCGen5p1Port.cpp`
- `virtual IOReturn APCIECoreRCGen5p1Port::enableLinkTraining(bool)`
- `APCIECoreRCGen5p1HostBridge`
- `APCIECoreRCGen5p1Port`
- `site.APCIECoreRCGen5p1HostBridge`
- `APCIECoreRCGen5p1HostBridge.cpp`
- `virtual bool APCIECoreRCGen5p1HostBridge::start(IOService *)`
- `virtual void APCIECoreRCGen5p1Port::disableRootPort(bool, bool, uint32_t *)`
- `virtual bool APCIECoreRCGen5p1Port::initWithAPCIeAndRegistryEntry(AppleEmbeddedPCIE *, IORegistryEntry *)`
- `site.APCIECoreRCGen5p1Port`
- `virtual void APCIECoreRCGen5p1Port::handleLinkUp(bool)`
- `site.APCIECoreRCGen5p1`

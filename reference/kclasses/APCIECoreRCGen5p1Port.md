# `APCIECoreRCGen5p1Port`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md)
- Object size: `0x1f88` (8,072 bytes)
- Metaclass: `0xfffffe000b9d0ba8`; metaclass vtable `0xfffffe00082647f8`; class vtable `0xfffffe0008263e08`
- Registration (init): `0xfffffe000988ba3c`
- Superclasses: [`APCIECoreRCGen5Port`](APCIECoreRCGen5Port.md) → [`AppleEmbeddedPCIEPort`](AppleEmbeddedPCIEPort.md) → [`IOInterruptController`](IOInterruptController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleT8160PCIePort`](AppleT8160PCIePort.md) — `com.apple.driver.AppleT8160PCIe`

## Strings in its kext that name it (7)

- `APCIECoreRCGen5p1Port.cpp`
- `virtual IOReturn APCIECoreRCGen5p1Port::enableLinkTraining(bool)`
- `APCIECoreRCGen5p1Port`
- `virtual void APCIECoreRCGen5p1Port::disableRootPort(bool, bool, uint32_t *)`
- `virtual bool APCIECoreRCGen5p1Port::initWithAPCIeAndRegistryEntry(AppleEmbeddedPCIE *, IORegistryEntry *)`
- `site.APCIECoreRCGen5p1Port`
- `virtual void APCIECoreRCGen5p1Port::handleLinkUp(bool)`

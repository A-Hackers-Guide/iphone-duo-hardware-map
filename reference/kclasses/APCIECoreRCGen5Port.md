# `APCIECoreRCGen5Port`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md)
- Object size: `0x1f68` (8,040 bytes)
- Metaclass: `0xfffffe000b9d0d38`; metaclass vtable `0xfffffe0008269068`; class vtable `0xfffffe0008268680`
- Registration (init): `0xfffffe00098a5b9c`
- Superclasses: [`AppleEmbeddedPCIEPort`](AppleEmbeddedPCIEPort.md) → [`IOInterruptController`](IOInterruptController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 2 in total)

- [`APCIECoreRCGen5p1Port`](APCIECoreRCGen5p1Port.md) — `com.apple.driver.AppleT8160PCIe`

## Strings in its kext that name it (10)

- `void APCIECoreRCGen5Port::_initializeRootComplex()`
- `virtual void APCIECoreRCGen5Port::serializedConfigRegSpace()`
- `virtual void APCIECoreRCGen5Port::allocateConfigSpaceBuffer()`
- `virtual bool APCIECoreRCGen5Port::initWithAPCIeAndRegistryEntry(AppleEmbeddedPCIE *, IORegistryEntry *)`
- `virtual void APCIECoreRCGen5Port::_updateRIDToSIDMappings(uint32_t)`
- `APCIECoreRCGen5Port.cpp`
- `virtual void APCIECoreRCGen5Port::configMSIRange()`
- `APCIECoreRCGen5Port`
- `site.APCIECoreRCGen5Port`
- `virtual void APCIECoreRCGen5Port::linkDownRecovery()`

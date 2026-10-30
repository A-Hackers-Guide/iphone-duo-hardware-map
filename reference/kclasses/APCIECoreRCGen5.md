# `APCIECoreRCGen5`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md)
- Object size: `0x250` (592 bytes)
- Metaclass: `0xfffffe000b9d0d10`; metaclass vtable `0xfffffe00082685e8`; class vtable `0xfffffe0008267db8`
- Registration (init): `0xfffffe00098a3c24`
- Superclasses: [`AppleEmbeddedPCIE`](AppleEmbeddedPCIE.md) → [`IOPCIHostBridge`](IOPCIHostBridge.md) → [`IOPCIBridge`](IOPCIBridge.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 2 in total)

- [`APCIECoreRCGen5p1`](APCIECoreRCGen5p1.md) — `com.apple.driver.AppleT8160PCIe`

## Strings in its kext that name it (45)

- `APCIECoreRCGen5p1`
- `virtual uint32_t APCIECoreRCGen5PLCE::readScratchRegister(unsigned int)`
- `APCIECoreRCGen5.cpp`
- `void APCIECoreRCGen5Port::_initializeRootComplex()`
- `virtual void APCIECoreRCGen5PLCE::writeScriptRun(unsigned int, uint32_t)`
- `APCIECoreRCGen5p1Port.cpp`
- `virtual IOReturn APCIECoreRCGen5p1Port::enableLinkTraining(bool)`
- `site.APCIECoreRCGen5`
- `virtual void APCIECoreRCGen5Port::serializedConfigRegSpace()`
- `virtual void APCIECoreRCGen5Port::allocateConfigSpaceBuffer()`
- `APCIECoreRCGen5p1HostBridge`
- `APCIECoreRCGen5p1Port`
- `virtual bool APCIECoreRCGen5Port::initWithAPCIeAndRegistryEntry(AppleEmbeddedPCIE *, IORegistryEntry *)`
- `site.APCIECoreRCGen5p1HostBridge`
- `[PCIe:%u %llu ns] APCIECoreRCGen5PLCE[%u]::%s Link init1 script error\n`
- `virtual void APCIECoreRCGen5Port::_updateRIDToSIDMappings(uint32_t)`
- `APCIECoreRCGen5Port.cpp`
- `virtual void APCIECoreRCGen5Port::configMSIRange()`
- `virtual void APCIECoreRCGen5PLCE::writeScriptDone(unsigned int, uint32_t)`
- `APCIECoreRCGen5p1HostBridge.cpp`
- `APCIECoreRCGen5Port`
- `site.APCIECoreRCGen5Port`
- `virtual bool APCIECoreRCGen5p1HostBridge::start(IOService *)`
- `site.APCIECoreRCGen5PLCE`
- `virtual void APCIECoreRCGen5PLCE::writeScratchRegister(unsigned int, uint32_t)`
- `virtual uint32_t APCIECoreRCGen5PLCE::readScriptDone(unsigned int)`
- `virtual void APCIECoreRCGen5Port::linkDownRecovery()`
- `virtual bool APCIECoreRCGen5PLCE::start(IOService *)`
- `virtual bool APCIECoreRCGen5::configure(IOService *)`
- `virtual void APCIECoreRCGen5p1Port::disableRootPort(bool, bool, uint32_t *)`
- `virtual uint64_t APCIECoreRCGen5PLCE::getScratchPhysAddr(unsigned int)`
- `virtual bool APCIECoreRCGen5p1Port::initWithAPCIeAndRegistryEntry(AppleEmbeddedPCIE *, IORegistryEntry *)`
- `APCIECoreRCGen5PLCE.cpp`
- `APCIECoreRCGen5`
- `site.APCIECoreRCGen5p1Port`
- `virtual uint32_t APCIECoreRCGen5PLCE::readErrorStatus(unsigned int)`
- `[PCIe:%u %llu ns] APCIECoreRCGen5PLCE[%u]::%s Link restore script error\n`
- `virtual unsigned int APCIECoreRCGen5::dtRegMapPhyIndex(uint32_t) const`
- `virtual uint32_t APCIECoreRCGen5PLCE::readScriptRun(unsigned int)`
- `virtual bool APCIECoreRCGen5::start(IOService *)`
- `virtual void APCIECoreRCGen5p1Port::handleLinkUp(bool)`
- `APCIECoreRCGen5PLCE`
- `site.APCIECoreRCGen5p1`
- `[PCIe:%u %llu ns] APCIECoreRCGen5PLCE[%u]::%s Link restore script error\n`
- `[PCIe:%u %llu ns] APCIECoreRCGen5PLCE[%u]::%s Link init1 script error\n`

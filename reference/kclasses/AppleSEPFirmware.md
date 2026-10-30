# `AppleSEPFirmware`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000b99a728`; metaclass vtable `0xfffffe00081f2b90`; class vtable `0xfffffe00081f2618`
- Registration (init): `0xfffffe000962e100`
- Superclasses: [`IOSlaveFirmware`](IOSlaveFirmware.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Strings in its kext that name it (21)

- `static AppleSEPFirmware *AppleSEPFirmware::fromMemory(IOMemoryDescriptor *, const uint64_t *, IOMapper *, AppleSEPFirmwarePayloadType)`
- `void AppleSEPFirmware::_setupSepFirmwareMemoryRegion()`
- `void AppleSEPARTStorage::find_firmware_manifest(AppleSEPFirmware *, void **, vm_size_t *)`
- `void AppleSEPFirmware::_setupTbmMemoryRegions()`
- `void AppleSEPFirmware::_initFromPreload()`
- `virtual void AppleSEPFirmware::releaseFirmware()`
- `void AppleSEPFirmware::_mapMemoryToSEP()`
- `void AppleSEPFirmware::_releaseIbootRegion(IOMemoryDescriptor *, bool)`
- `void AppleSEPFirmware::_mapBuffer(IOMemoryDescriptor *, uint32_t, uint64_t *)`
- `uint64_t AppleSEPFirmware::getUstuffAddress()`
- `static AppleSEPFirmware *AppleSEPFirmware::fromPreload(IOMapper *, AppleSEPFirmwarePayloadType)`
- `void AppleSEPFirmware::_copyInData(IOMemoryDescriptor *)`
- `void AppleSEPFirmware::_allocateTbmMemoryRegions(const uint64_t *)`
- `AppleSEPFirmware.cpp`
- `void AppleSEPFirmware::_initFromMemory(IOMemoryDescriptor *, const uint64_t *)`
- `AppleSEPFirmware::NUM_PIECES + 1 == arguments->scalarInputCount`
- `site.AppleSEPFirmware`
- `uint64_t AppleSEPFirmware::getPatchAddress()`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPFirmware.cpp`
- `AppleSEPFirmware`
- `IOReturn AppleSEPBooter::bootSEP(AppleSEPFirmware *, bool, AppleSEPSharedMemoryBuffer *, uint8_t *)`

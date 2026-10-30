# `AGXArmFirmware`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md)
- Object size: `0x2080` (8,320 bytes)
- Metaclass: `0xfffffe000b92a748`; metaclass vtable `0xfffffe0007f72770` (abstract: no class vtable recorded)
- Registration (init): `0xfffffe00085a63e4`
- Superclasses: [`AGXFirmware`](AGXFirmware.md)

## Direct subclasses (1; 1 in total)

- [`AGXArmFirmwareASC`](AGXArmFirmwareASC.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (31)

- `AGXk: %s:%d:%s: !!! AGXArmFirmware:: Power State (%d) must be in external state\n`
- `virtual void AGXArmFirmware::blockForRingEmpty(uint32_t)`
- `virtual IOReturn AGXArmFirmwareMapper::iovmUnmapMemory(IOMemoryDescriptor *, IODMACommand *, uint64_t, uint64_t)`
- `AGXk: %s:%d:%s: !!! Setting AGXArmFirmwareMapper accelerator handle a second time (fAccelerator=0x%p accel=0x%p)!\n`
- `AGXArmFirmwareMapper`
- `virtual bool AGXArmFirmware::stopFirmwareForRecoveryInspection(const AGXRestartInfo &)`
- `AGXk: %s:%d:%s: !!! AGXArmFirmwareMapper::iovmUnmapMemory: unmapping different length than was mapped!\n`
- `virtual void AGXArmFirmware::resumeFirmwarePreRecovery()`
- `void AGXArmFirmwareMapper::setAccelerator(AGXAccelerator *const)`
- `AGXk: %s:%d:%s: !!! AGXArmFirmwareMapper::iovmInsert: insertion into previous mappings not supported!\n`
- `virtual IOReturn AGXArmFirmwareMapper::iovmInsert(uint32_t, uint64_t, uint64_t, uint64_t, uint64_t)`
- `virtual IOReturn AGXArmFirmwareMapper::iovmMapMemory(IOMemoryDescriptor *, uint64_t, uint64_t, uint32_t, const IODMAMapSpecification *, IODMACommand *, const IODMAMapPageList *, uint64_t *, uint64_t *)`
- `site.AGXArmFirmwareMapper`
- `virtual void AGXArmFirmware::submitCLChannel(AGXChannel *const, const AGXChannelSubmitInfo &, uint32_t, uint32_t, const bool)`
- `AGXk: %s:%d:%s: !!! AGXArmFirmwareMapper::stop: mapping list not empty!\n`
- `bool AGXArmFirmware::waitForFWAlive()`
- `virtual void AGXArmFirmware::submitTAChannel(AGXChannel *const, const AGXChannelSubmitInfo &, uint32_t, uint32_t, const bool)`
- `AGXArmFirmware`
- `virtual void AGXArmFirmware::kickFirmware(uint32_t, AGFAMessageType, bool)`
- `virtual void AGXArmFirmware::resumeFirmwarePostRecovery()`
- `AGXk: %s:%d:%s: !!! AGXArmFirmware::kickFirmware: Command submission is disabled!\n`
- `void AGXArmFirmware::insertNewMappingEntry(const AGFAMemDescriptorEntry &)`
- `AGXArmFirmwareASC`
- `site.AGXArmFirmware`
- `virtual void AGXArmFirmware::submit3DChannel(AGXChannel *const, const AGXChannelSubmitInfo &, uint32_t, uint32_t, const bool, const bool)`
- `virtual void AGXArmFirmware::powerTransitionStart(AGFIFirmwareRole, bool)`
- `AGXk: %s:%d:%s: !!! Failed to create matching dictionary for AGXArmFirmwareMapper!\n`
- `virtual void AGXArmFirmwareMapper::stop(IOService *)`
- `virtual void AGXArmFirmware::notifyNewMapping(GPUVirtualAddress, IOPhysicalAddress, bool)`
- `AGXk: %s:%d:%s: !!! AGXArmFirmwareMapper::iovmUnmapMemory: unmapping address that was never mapped!\n`
- `site.AGXArmFirmwareASC`

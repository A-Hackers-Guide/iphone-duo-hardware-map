# `AGXParameterManagement`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md)
- Object size: `0x240` (576 bytes)
- Metaclass: `0xfffffe000b92ba98`; metaclass vtable `0xfffffe0007f7b720`; class vtable `0xfffffe0007f7bda8`
- Registration (init): `0xfffffe00085cfed4`
- Superclasses: [`IOGPUObject`](IOGPUObject.md)

## Direct subclasses (1; 1 in total)

- [`AGXParameterManagementVirtual`](AGXParameterManagementVirtual.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (14)

- `void AGXFirmwareResourceStack<unsigned char, AGXParameterManagement>::releaseElement(ElementOwner *, uint32_t) [FWResourceManagerElement = unsigned char, ElementOwner = AGXParameterManagement, kL1WidthBits = 64, kL2WidthBits = 64]`
- `OSSharedPtr<AGXParameterBufferBlock> AGXParameterManagementVirtual::createParameterBufferBlock(bool)`
- `virtual bool AGXParameterManagement::checkForShrink(uint64_t)`
- `virtual void AGXParameterManagement::cleanup()`
- `virtual IOReturn AGXParameterManagement::prepareAndRetain(AGXTACommandDescriptor *, AGXParameterManagerStagedUpdates &)`
- `virtual void AGXParameterManagement::describeDriverAllocationsLocked(IOGPUAllocationInfo *, pid_t)`
- `AGXParameterManagement`
- `void AGXParameterManagement::updateAndValidateCookie(AGXHWParamBufferManager *, const AGXTACommandDescriptor *)`
- `site.AGXParameterManagementVirtual`
- `bool AGXParameterManagement::createNewHWPBManager()`
- `AGXParameterManagementState AGXParameterManagement::queryParameterState(uint32_t *, uint32_t *)`
- `virtual FirmwareVirtualAddress AGXParameterManagement::growImmediately()`
- `virtual bool AGXParameterManagement::buildPageList(AGXParameterManagerStagedUpdates &)`
- `AGXParameterManagementVirtual`

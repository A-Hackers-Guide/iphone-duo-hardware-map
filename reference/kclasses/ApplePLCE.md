# `ApplePLCE`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160PCIe`](../kexts/com.apple.driver.AppleT8160PCIe.md)
- Object size: `0x1c0` (448 bytes)
- Metaclass: `0xfffffe000b9d0c48`; metaclass vtable `0xfffffe00082665a0`; class vtable `0xfffffe0008265fc8`
- Registration (init): `0xfffffe000989243c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`APCIECoreRCGen5PLCE`](APCIECoreRCGen5PLCE.md) — `com.apple.driver.AppleT8160PCIe`

## Strings in its kext that name it (60)

- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Sent doorbell properties to RTKitPCIe, result=0x%08X\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Sequence table virtual  address: 0x%llx\n\n`
- `IOBufferMemoryDescriptor *ApplePLCE::createScriptIOMD(ApplePLCESequence **, unsigned int, bool)`
- `site.struct ApplePLCEDoorbell`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Updating %u:%u:%u's VID/DID check sequence\n`
- `void ApplePLCE::transmitDoorbellInformation()`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Fire-and-forget base PA:  %p\n\n`
- `uint64_t ApplePLCELinkScripts::calculateDoorbellAddress(IOPCIDevice *, struct ApplePLCEDoorbell *)`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s no property matching dict\n\n`
- `void ApplePLCE::installTightbeamClientMatchingNotification()_block_invoke_2`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s \n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Sent SMPL ready %u message to RTKitPCIe, response=0x%08X\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Reinstalling fire-and-forget script for doorbell %u\n`
- `void ApplePLCE::configureInterrupts(IOService *)`
- `bool ApplePLCELinkScripts::isTeardownSequenceInstalled(enum teardownSeqID)`
- `ApplePLCESequence *ApplePLCELinkScripts::getRestoreSequence(enum restoreSeqID)`
- `void ApplePLCELinkScripts::resetRestoreSequence(enum restoreSeqID)`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s MMIO doorbell %u using script %u\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Sequence table physical address: 0x%llx\n\n`
- `\"[ApplePLCELinkScripts::%s()] IOPCIDevice nub's expressCapability should always be non-zero\" @%s:%d`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s source address 0x%llx, destination address 0x%llx\n`
- `void ApplePLCE::allocateFireAndForgetBuffer()`
- `void ApplePLCE::_programSequenceTable(uint16_t)`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s base 0x%llx = 0x%x\n`
- `site.ApplePLCESequence`
- `ApplePLCE.cpp`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Fire-and-forget base DVA: %p\n\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Updating %u:%u:%u's restore sequence\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Installing script in PLCE slot %u\n`
- `bool ApplePLCELinkScripts::isRestoreSequenceInstalled(enum restoreSeqID)`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Resetting script in PLCE slot %u\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Installing restore sequence %u\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s no matching dict\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Script %u virtual address: %p\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s 0x%llx = 0x%x\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s aop2.smpl.doorbell's service cannot be cast to AFKSharedMemoryRegionBase\n\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s  Failed to get device memory for nub %s, bar %u\n`
- `void *ApplePLCESequence::getBytesNoCopy()`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s address 0x%llx, mask 0x%x, data 0x%x\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s MMIO doorbell %u: EP function %u, BAR%u, type %u, offset 0x%x\n`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s offset 0x%llx <- data 0x%x\n`
- `virtual bool ApplePLCE::start(IOService *)`
- `doorbellProp[i].type < kApplePLCENumDoorbellTypes`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s In the doorbell notifier handler\n\n`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s address 0x%llx, data 0x%x, mask 0x%x\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Constructing the teardown start sequence\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s AFKSharedMemoryRegionBase's IOMD is NULL\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Done status: 0x%x 0x%x 0x%x\n`
- `void ApplePLCE::restoreDARTMappings()`
- `void ApplePLCE::_installScript(uint16_t, ApplePLCESequence **, unsigned int, bool)`
- `void ApplePLCE::allocateDoorbellScripts()`
- `void ApplePLCELinkScripts::resetTeardownSequence(enum teardownSeqID)`
- `[PCIe:%u %llu ns] ApplePLCESequence[%u]::%s wrIndex %u, cpSrcIndex %u, cpDstIndex %u, dmaSrcIndex %u, dmaDstIndex %u\n`
- `[PCIe:%u %llu ns] ApplePLCELinkScripts[%u]::%s Invalid doorbell offset (0x%x, 0x%x)\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s RTKitPCIe tightbeam client init failed\n\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s No doorbell-cfg property found\n`
- `[PCIe:%u %llu ns] ApplePLCE[%u]::%s Script %u physical address: %p\n\n`
- `site.ApplePLCE`
- `ApplePLCE`
- `void ApplePLCELinkScripts::getRMWMaskOffset(uint32_t *, uint8_t, uint32_t *, uint32_t *)`

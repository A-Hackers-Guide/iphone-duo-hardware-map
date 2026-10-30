# `AGXSecureGart`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md)
- Object size: `0x340` (832 bytes)
- Metaclass: `0xfffffe000b92c300`; metaclass vtable `0xfffffe0007f7d620` (abstract: no class vtable recorded)
- Registration (init): `0xfffffe00085e57bc`
- Superclasses: [`AGXGart`](AGXGart.md) → [`IOGPUTask`](IOGPUTask.md) → [`IOGPUObject`](IOGPUObject.md)

## Direct subclasses (1; 2 in total)

- [`AGX·PI_400·P·A0·Gart`](AGX_PI_400_P_A0_Gart.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (18)

- `virtual OSSharedPtr<IOMemoryMap> AGXSecureGart::createRestrictedRangeMapping(IOMemoryDescriptor *, IOGPUNewResourceArgs *)`
- `virtual void AGXSecureGart::free()`
- `AGXk: %s:%d:%s: !!! AGXSecureGart::init\n`
- `bool AGXSecureGart::initInner(AGXAccelerator *, task_t, uint64_t, bool, AGFIFirmwareRole)`
- `virtual AGXGart *AGXSecureGart::getProtectedContext(uint64_t)`
- `AGXk: %s:%d:%s: !!! AGXSecureGart::unmap\n`
- `AGXk: %s:%d:%s: !!! AGXSecureGart::unmapWithAddress\n`
- `AGXk: %s:%d:%s: !!! AGXSecureGart::registerContextID\n`
- `virtual bool AGXSecureGart::unmapWithAddress(IOMemoryDescriptor *, GPUVirtualAddress, IOByteCount, eAGXProtectionOptions)`
- `AGXSecureGart`
- `bool AGXSecureGart::mapInThisGart(AGXSecureMemoryMap *, AGXPageTableEntryFlags)`
- `AGXk: %s:%d:%s: !!! AGXSecureGart::map\n`
- `bool AGXSecureGart::unmapFromThisGart(AGXSecureMemoryMap *)`
- `AGXk: %s:%d:%s: !!! AGXSecureGart::unmap Timed out waiting for FW to process secure unmap after %llu ns\n`
- `AGXk: %s:%d:%s: !!! AGXSecureGart::createRestrictedRangeMapping\n`
- `site.AGXSecureGart`
- `AGXk: %s:%d:%s: !!! AGXSecureGart::free\n`
- `virtual void AGXSecureGart::registerContextID(const int32_t)`

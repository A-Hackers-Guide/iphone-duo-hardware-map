# `AGXUSCPrivMemPool`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md)
- Object size: `0x240` (576 bytes)
- Metaclass: `0xfffffe000b92e528`; metaclass vtable `0xfffffe0007f7f468` (abstract: no class vtable recorded)
- Registration (init): `0xfffffe00085fdcc4`
- Superclasses: [`IOGPUObject`](IOGPUObject.md)

## Direct subclasses (1; 3 in total)

- [`AGXUSCPrivMemPoolSMA`](AGXUSCPrivMemPoolSMA.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (12)

- `site.AGXUSCPrivMemPoolSMAV1`
- `uint32_t AGXUSCPrivMemPool::getMaxParallelStreamsForDM(AGXIOFenceDataMasterType) const`
- `site.AGXUSCPrivMemPoolSMA`
- `AGXUSCPrivMemPoolSMAV2`
- `site.AGXUSCPrivMemPoolSMAV2`
- `AGXUSCPrivMemPoolSMAV1`
- `virtual IOByteCount AGXUSCPrivMemPool::getRequiredRTSize(const AGXUMADesc *)`
- `AGXUSCPrivMemPoolSMA`
- `void KernelCalculatedSMAFinalResults::snapShotEnvironment(const AGXAccelerator &, const AGXUSCPrivMemPoolSMA &, AGXIOFenceDataMasterType)`
- `AGXUSCPrivMemPool`
- `bool AGXUSCPrivMemPool::allocatePages(AGXCommandDescriptor *, AGXUMAData *, uint64_t)`
- `virtual IOByteCount AGXUSCPrivMemPool::getSelfReserveSize(const AGXUMADesc *)`

# `AGXIOFenceData`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md)
- Object size: `0x2c0` (704 bytes)
- Metaclass: `0xfffffe000b92b698`; metaclass vtable `0xfffffe0007f7ad18`; class vtable `0xfffffe0007f7ac88`
- Registration (init): `0xfffffe00085c4f10`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Strings in its kext that name it (8)

- `virtual void AGXWorkQueue::submitForFenceComplete(AGXIOFenceData *)`
- `AGXIOFenceData`
- `site.AGXIOFenceData`
- `uint32_t AGXUSCPrivMemPool::getMaxParallelStreamsForDM(AGXIOFenceDataMasterType) const`
- `virtual FSTPBitArray AGXAccelerator::convertFromGlobalToDmMask(AGXIOFenceDataMasterType, const FSTPBitArray &)`
- `virtual void AGXIOFenceData::free()`
- `void AGXIOFenceData::saveIOSurfaceInfo(IOSurface *, uint32_t)`
- `void KernelCalculatedSMAFinalResults::snapShotEnvironment(const AGXAccelerator &, const AGXUSCPrivMemPoolSMA &, AGXIOFenceDataMasterType)`

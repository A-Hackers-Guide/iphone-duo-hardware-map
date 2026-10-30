# `IOSARTMapper`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSART`](../kexts/com.apple.driver.AppleSART.md)
- Object size: `0x180` (384 bytes)
- Metaclass: `0xfffffe000b995840`; metaclass vtable `0xfffffe00081e4560`; class vtable `0xfffffe00081e3fd0`
- Registration (init): `0xfffffe00095845f8`
- Superclasses: [`IOMapper`](IOMapper.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOSARTMapper` in [`com.apple.driver.AppleSART`](../kexts/com.apple.driver.AppleSART.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `sart,t8015`

## Strings in its kext that name it (10)

- `/Library/Caches/com.apple.xbs/ABC41D5C-9587-4D9F-8BDB-FF041AED5BDF/TemporaryDirectory.lJvBpM/Sources/AppleSART/IOSARTMapper.cpp`
- `virtual bool IOSARTMapper::_setActive(bool)`
- `virtual IOReturn IOSARTMapper::iovmMapMemory(IOMemoryDescriptor *, uint64_t, uint64_t, uint32_t, const IODMAMapSpecification *, IODMACommand *, const IODMAMapPageList *, uint64_t *, uint64_t *)`
- `int IOSARTMapper::_addRegion(uintptr_t, uint32_t, bool)`
- `IOSARTMapper`
- `site.IOSARTMapper`
- `virtual IOReturn IOSARTMapper::iovmInsert(uint32_t, uint64_t, uint64_t, uint64_t, uint64_t)`
- `IOSARTMapper.cpp`
- `virtual bool IOSARTMapper::start(IOService *)`
- `virtual IOReturn IOSARTMapper::iovmUnmapMemory(IOMemoryDescriptor *, IODMACommand *, uint64_t, uint64_t)`

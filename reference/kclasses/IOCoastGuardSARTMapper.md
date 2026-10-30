# `IOCoastGuardSARTMapper`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSART`](../kexts/com.apple.driver.AppleSART.md)
- Object size: `0x120` (288 bytes)
- Metaclass: `0xfffffe000b9957f0`; metaclass vtable `0xfffffe00081e3948`; class vtable `0xfffffe00081e33c0`
- Registration (init): `0xfffffe000958320c`
- Superclasses: [`IOMapper`](IOMapper.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOCoastGuardSARTMapper` in [`com.apple.driver.AppleSART`](../kexts/com.apple.driver.AppleSART.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['sart,coastguard']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/sart-ans`](../devicetree/root__arm-io__sart-ans.md) on `sart,coastguard`

## Strings in its kext that name it (8)

- `virtual bool IOCoastGuardSARTMapper::start(IOService *)`
- `virtual IOReturn IOCoastGuardSARTMapper::iovmUnmapMemory(IOMemoryDescriptor *, IODMACommand *, uint64_t, uint64_t)`
- `/Library/Caches/com.apple.xbs/ABC41D5C-9587-4D9F-8BDB-FF041AED5BDF/TemporaryDirectory.lJvBpM/Sources/AppleSART/IOCoastGuardSARTMapper.cpp`
- `IOCoastGuardSARTMapper.cpp`
- `virtual IOReturn IOCoastGuardSARTMapper::iovmMapMemory(IOMemoryDescriptor *, uint64_t, uint64_t, uint32_t, const IODMAMapSpecification *, IODMACommand *, const IODMAMapPageList *, uint64_t *, uint64_t *)`
- `IOCoastGuardSARTMapper`
- `virtual IOReturn IOCoastGuardSARTMapper::callPlatformFunction(const OSSymbol *, bool, void *, void *, void *, void *)`
- `site.IOCoastGuardSARTMapper`

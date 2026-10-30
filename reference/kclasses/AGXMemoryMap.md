# `AGXMemoryMap`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md)
- Object size: `0x60` (96 bytes)
- Metaclass: `0xfffffe000b92c290`; metaclass vtable `0xfffffe0007f7b3f8` (abstract: no class vtable recorded)
- Registration (init): `0xfffffe00085c9354`
- Superclasses: [`IOGPUMemoryMap`](IOGPUMemoryMap.md) → [`IOGPUObject`](IOGPUObject.md)

## Direct subclasses (1; 1 in total)

- [`AGXSecureMemoryMap`](AGXSecureMemoryMap.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (7)

- `IOReturn AGXParameterMemoryVirtual::addMapping(AGXMemoryMap *)`
- `B16@?0^{sBlock=^{AGXMemoryMap}QQq{?=^{sBlock}^^{sBlock}}{IOGPUEvent={?=I[15I]}}}8`
- `static uint64_t AGXMemoryMap::encodeMappingOptions(const uint32_t, const bool, const uint64_t)`
- `virtual bool AGXMemoryMap::updateGPUPageTable()`
- `AGXMemoryMap`
- `site.AGXMemoryMap *`
- `AGXGrowableArray<AGXMemoryMap *>::~AGXGrowableArray() [T = AGXMemoryMap *]`

# `AppleSARTMarconi`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSART`](../kexts/com.apple.driver.AppleSART.md)
- Object size: `0xb0` (176 bytes)
- Metaclass: `0xfffffe000b995818`; metaclass vtable `0xfffffe00081e3f38`; class vtable `0xfffffe00081e39e0`
- Registration (init): `0xfffffe0009583998`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSARTMarconi` in [`com.apple.driver.AppleSART`](../kexts/com.apple.driver.AppleSART.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `sart-marconi,t8006`

## Strings in its kext that name it (7)

- `site.AppleSARTMarconi`
- `uint32_t AppleSARTMarconi::_makeRegionBase(uint64_t)`
- `/Library/Caches/com.apple.xbs/ABC41D5C-9587-4D9F-8BDB-FF041AED5BDF/TemporaryDirectory.lJvBpM/Sources/AppleSART/AppleSARTMarconi.cpp`
- `uint32_t AppleSARTMarconi::_makeRegion(uint64_t, bool)`
- `AppleSARTMarconi`
- `virtual bool AppleSARTMarconi::start(IOService *)`
- `AppleSARTMarconi.cpp`

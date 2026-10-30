# `AppleSoCMisc`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160`](../kexts/com.apple.driver.AppleT8160.md)
- Object size: `0x318` (792 bytes)
- Metaclass: `0xfffffe000b9a6778`; metaclass vtable `0xfffffe000823efb8`; class vtable `0xfffffe000823ea18`
- Registration (init): `0xfffffe00097a8ee4`
- Superclasses: [`AppleSoCMiscCommon`](AppleSoCMiscCommon.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSoCMisc` in [`com.apple.driver.AppleT8160`](../kexts/com.apple.driver.AppleT8160.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `soc-misc,t8160`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/soc-misc`](../devicetree/root__arm-io__soc-misc.md) on `soc-misc,t8160`

## Strings in its kext that name it (9)

- `site.AppleSoCMiscCommon`
- `AppleSoCMiscCommon`
- `AppleSoCMiscUserClient`
- `AppleSoCMisc`
- `site.AppleSoCMiscFunctionSubmitVoteForceWakeupDram`
- `site.AppleSoCMisc`
- `AppleSoCMiscCommon.cpp`
- `AppleSoCMiscFunctionSubmitVoteForceWakeupDram`
- `AppleSoCMiscT8160.cpp`

# `AppleSoCIOPSD`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160`](../kexts/com.apple.driver.AppleT8160.md)
- Object size: `0x140` (320 bytes)
- Metaclass: `0xfffffe000b9a6868`; metaclass vtable `0xfffffe00082569f0`; class vtable `0xfffffe00082563e0`
- Registration (init): `0xfffffe0009806018`
- Superclasses: [`AppleSoCIO`](AppleSoCIO.md) → [`AppleARMIO`](AppleARMIO.md) → [`IOPlatformIO`](IOPlatformIO.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSoCIO` in [`com.apple.driver.AppleT8160`](../kexts/com.apple.driver.AppleT8160.md): `IOProviderClass` = `IOPlatformDevice`, `IONameMatch` = `arm-io,t8160`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io`](../devicetree/root__arm-io.md) on `arm-io,t8160`

## Strings in its kext that name it (2)

- `AppleSoCIOPSD`
- `site.AppleSoCIOPSD`

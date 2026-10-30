# `AppleBasebandINT1`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleBasebandINT1`](../kexts/com.apple.driver.AppleBasebandINT1.md)
- Object size: `0x3e8` (1,000 bytes)
- Metaclass: `0xfffffe000b937808`; metaclass vtable `0xfffffe0007ff4eb8`; class vtable `0xfffffe0007ff4578`
- Registration (init): `0xfffffe00089c16b0`
- Superclasses: [`AppleBasebandPCIEDevice`](AppleBasebandPCIEDevice.md) → [`AppleBasebandPlatform`](AppleBasebandPlatform.md) → [`AppleBaseband`](AppleBaseband.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleBasebandINT1` in [`com.apple.driver.AppleBasebandINT1`](../kexts/com.apple.driver.AppleBasebandINT1.md): `IOProviderClass` = `IOPlatformDevice`, `IONameMatch` = `baseband,int1`, `IOMatchCategory` = `AppleBaseband`

## Device-tree nodes it binds (1) [DT]

- [`/baseband`](../devicetree/root__baseband.md) on `baseband,int1`

## Strings in its kext that name it (3)

- `site.AppleBasebandINT1`
- `AppleBasebandINT1.cpp`
- `AppleBasebandINT1`

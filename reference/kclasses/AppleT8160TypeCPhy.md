# `AppleT8160TypeCPhy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160TypeCPhy`](../kexts/com.apple.driver.AppleT8160TypeCPhy.md)
- Object size: `0xf00` (3,840 bytes)
- Metaclass: `0xfffffe000b9d3fc0`; metaclass vtable `0xfffffe0008299090`; class vtable `0xfffffe00082988d0`
- Registration (init): `0xfffffe0009a9e94c`
- Superclasses: [`AppleTypeCPhy`](AppleTypeCPhy.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8160TypeCPhy` in [`com.apple.driver.AppleT8160TypeCPhy`](../kexts/com.apple.driver.AppleT8160TypeCPhy.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `atc-phy,t8160`, `IOProbeScore` = `10000`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/atc-phy0`](../devicetree/root__arm-io__atc-phy0.md) on `atc-phy,t8160`

## Strings in its kext that name it (3)

- `site.AppleT8160TypeCPhy`
- `AppleT8160TypeCPhy.cpp`
- `AppleT8160TypeCPhy`

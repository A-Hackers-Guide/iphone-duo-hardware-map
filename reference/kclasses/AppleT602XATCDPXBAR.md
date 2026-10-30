# `AppleT602XATCDPXBAR`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md)
- Object size: `0xd0` (208 bytes)
- Metaclass: `0xfffffe000b941328`; metaclass vtable `0xfffffe0008058ee8`; class vtable `0xfffffe00080588c0`
- Registration (init): `0xfffffe0008b96f48`
- Superclasses: [`AppleATCDPXBAR`](AppleATCDPXBAR.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 2 in total)

- [`AppleT604XATCDPXBAR`](AppleT604XATCDPXBAR.md) — `com.apple.driver.AppleDisplayCrossbar`

## IOKit personalities that instantiate it (1)

- `AppleT602XATCDPXBAR` in [`com.apple.driver.AppleDisplayCrossbar`](../kexts/com.apple.driver.AppleDisplayCrossbar.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['atc-dpxbar,t602x']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/atc0-dpxbar`](../devicetree/root__arm-io__atc0-dpxbar.md) on `atc-dpxbar,t602x`

## Strings in its kext that name it (2)

- `site.AppleT602XATCDPXBAR`
- `AppleT602XATCDPXBAR`

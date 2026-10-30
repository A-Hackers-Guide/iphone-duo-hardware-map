# `AppleHapticsSupportLEAP`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHapticsSupportLEAP`](../kexts/com.apple.driver.AppleHapticsSupportLEAP.md)
- Object size: `0x240` (576 bytes)
- Metaclass: `0xfffffe000b94fc98`; metaclass vtable `0xfffffe000810bf48`; class vtable `0xfffffe000810b948`
- Registration (init): `0xfffffe0008fded74`
- Superclasses: [`AppleHapticsSupport`](AppleHapticsSupport.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleHapticsSupport` in [`com.apple.driver.AppleHapticsSupportLEAP`](../kexts/com.apple.driver.AppleHapticsSupportLEAP.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['haptics-support,leap']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/haptics-support-interface`](../devicetree/root__arm-io__haptics-support-interface.md) on `haptics-support,leap`

## Strings in its kext that name it (2)

- `site.AppleHapticsSupportLEAP`
- `AppleHapticsSupportLEAP`

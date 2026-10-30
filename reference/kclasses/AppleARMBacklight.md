# `AppleARMBacklight`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md)
- Object size: `0x370` (880 bytes)
- Metaclass: `0xfffffe000b934a88`; metaclass vtable `0xfffffe0007fc4fa8`; class vtable `0xfffffe0007fc4a48`
- Registration (init): `0xfffffe000873195c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleARMBacklight` in [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md): `IOProviderClass` = `IOPlatformDevice`, `IONameMatch` = `backlight`

## Device-tree nodes it binds (1) [DT]

- [`/backlight`](../devicetree/root__backlight.md) on `backlight`

## Strings in its kext that name it (9)

- `bool AppleARMBacklight::isDarkBoot()`
- `AppleARMBacklightFunction`
- `site.AppleARMBacklightFunction`
- `site.AppleARMBacklightPCCUpdateFunction`
- `AppleARMBacklightPCCUpdateFunction`
- `site.AppleARMBacklight`
- `%s::%s: ALS: AppleARMBacklight::handleMessageGated - framebufferState -> %d\n`
- `%s::%s: ALS: AppleARMBacklight::setBacklightEnableGated %d (set level to 0x%x)\n`
- `AppleARMBacklight`

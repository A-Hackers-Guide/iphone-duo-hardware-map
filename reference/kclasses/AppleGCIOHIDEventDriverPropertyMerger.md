# `AppleGCIOHIDEventDriverPropertyMerger`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md)
- Object size: `0x88` (136 bytes)
- Metaclass: `0xfffffe000b946688`; metaclass vtable `0xfffffe00080b83c8`; class vtable `0xfffffe00080b7e60`
- Registration (init): `0xfffffe0008d0f3f4`
- Superclasses: [`AppleGCHIDProviderPropertyMerger`](AppleGCHIDProviderPropertyMerger.md) → [`IOProviderPropertyMerger`](IOProviderPropertyMerger.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `Extended MFi Controller Driver Service` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDEventDriver`, `IOPropertyMatch` = `{'GameControllerType': 1}`, `IOProbeScore` = `10`
- `Standard MFi Controller Driver Service` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDEventDriver`, `IOPropertyMatch` = `{'GameControllerType': 0}`, `IOProbeScore` = `10`

## Strings in its kext that name it (3)

- `AppleGCIOHIDEventDriverPropertyMerger`
- `site.AppleGCIOHIDEventDriverPropertyMerger`
- `AppleGCIOHIDEventDriverPropertyMerger::probe(<IOHIDDevice %#010llx>)`

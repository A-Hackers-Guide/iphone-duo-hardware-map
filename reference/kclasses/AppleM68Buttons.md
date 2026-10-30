# `AppleM68Buttons`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleM68Buttons`](../kexts/com.apple.driver.AppleM68Buttons.md)
- Object size: `0x460` (1,120 bytes)
- Metaclass: `0xfffffe000b97c948`; metaclass vtable `0xfffffe00081670c8`; class vtable `0xfffffe0008166908`
- Registration (init): `0xfffffe00091f23d4`
- Superclasses: [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleM68Buttons` in [`com.apple.driver.AppleM68Buttons`](../kexts/com.apple.driver.AppleM68Buttons.md): `IOProviderClass` = `IOPlatformDevice`, `IONameMatch` = `buttons`

## Device-tree nodes it binds (2) [DT]

- [`/buttons`](../devicetree/root__buttons.md) on `buttons`
- [`/buttons`](../devicetree/root__buttons.md) on `buttons`

## Strings in its kext that name it (10)

- `AppleM68Buttons`
- `\"AppleM68Buttons::handleStart failed to allocate pressCountPairs\" @%s:%d`
- `AppleM68Buttons.cpp`
- `\"AppleM68Buttons::handleStart failed to allocate acm threadcall\" @%s:%d`
- `\"AppleM68Buttons::handleStart failed to allocate nvram sync threadcall\" @%s:%d`
- `\"AppleM68Buttons::handleStart failed to instantiate %s\" @%s:%d`
- `\"AppleM68Buttons::handleStart failed to allocate backlight threadcall\" @%s:%d`
- `\"AppleM68Buttons::handleStart failed to allocate state serializer\" @%s:%d`
- `site.AppleM68Buttons`
- `AppleM68Buttons: dispatching keyboard event up:0x%x u:0x%x state:%d`

# `AppleParrot`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleParrot`](../kexts/com.apple.driver.AppleParrot.md)
- Object size: `0x98` (152 bytes)
- Metaclass: `0xfffffe000b9884b0`; metaclass vtable `0xfffffe000819dbb0`; class vtable `0xfffffe000819d620`
- Registration (init): `0xfffffe000937b0a4`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleParrot` in [`com.apple.driver.AppleParrot`](../kexts/com.apple.driver.AppleParrot.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `parrot-i2c,a0`

## Strings in its kext that name it (3)

- `site.AppleParrot`
- `AppleParrot`
- `AppleParrot-debug`

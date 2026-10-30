# `AppleAuthCPDock`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md)
- Object size: `0xa0` (160 bytes)
- Metaclass: `0xfffffe000b937398`; metaclass vtable `0xfffffe0007ff0780`; class vtable `0xfffffe0007ff0190`
- Registration (init): `0xfffffe000899c250`
- Superclasses: [`AppleAuthCP`](AppleAuthCP.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAuthCPDock` in [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md): `IOProviderClass` = `IOAccessoryManager`, `IOPropertyMatch` = `{'IOAccessoryManagerPortAuthentication': True}`, `IOMatchCategory` = `AUDock`

## Strings in its kext that name it (2)

- `site.AppleAuthCPDock`
- `AppleAuthCPDock`

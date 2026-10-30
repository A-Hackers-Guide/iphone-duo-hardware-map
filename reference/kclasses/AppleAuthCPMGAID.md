# `AppleAuthCPMGAID`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md)
- Object size: `0xc8` (200 bytes)
- Metaclass: `0xfffffe000b9372a8`; metaclass vtable `0xfffffe0007fedd58`; class vtable `0xfffffe0007fed750`
- Registration (init): `0xfffffe0008994c74`
- Superclasses: [`AppleAuthCPAID`](AppleAuthCPAID.md) → [`AppleAuthCP`](AppleAuthCP.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAuthCPMGAID ` in [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md): `IOProviderClass` = `IOAccessoryDock9Pin`, `IOMatchCategory` = `AU`

## Strings in its kext that name it (3)

- `site.AppleAuthCPMGAID`
- `AppleAuthCPMGAID::%s: super::start failed\n`
- `AppleAuthCPMGAID`

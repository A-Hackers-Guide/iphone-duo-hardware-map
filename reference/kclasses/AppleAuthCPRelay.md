# `AppleAuthCPRelay`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md)
- Object size: `0xc8` (200 bytes)
- Metaclass: `0xfffffe000b9372d0`; metaclass vtable `0xfffffe0007fee3e0`; class vtable `0xfffffe0007feddf0`
- Registration (init): `0xfffffe0008997184`
- Superclasses: [`AppleAuthCP`](AppleAuthCP.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleAuthCPRelay` in [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md): `IOProviderClass` = `AppleAuthCPRelayInterface`, `IOMatchCategory` = `AppleAuthCP`

## Strings in its kext that name it (6)

- `site.AppleAuthCPRelay`
- `site.AppleAuthCPRelayInterface`
- `AppleAuthCPRelayInterface`
- `AppleAuthCPRelay`
- `AppleAuthCPRelay::start: provider has no IDSN\n`
- `%s: provider is not AppleAuthCPRelayInterface`

# `AppleSARInterface`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md)
- Object size: `0x160` (352 bytes)
- Metaclass: `0xfffffe000b9944c8`; metaclass vtable `0xfffffe00081c7788`; class vtable `0xfffffe00081c7810`
- Registration (init): `0xfffffe0009488a70`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleSARInterfaceSPMIIDC`](AppleSARInterfaceSPMIIDC.md) — `com.apple.driver.AppleSARService`
- [`AppleSARInterfaceSPMIWLANIDC`](AppleSARInterfaceSPMIWLANIDC.md) — `com.apple.driver.AppleSARService`

## Strings in its kext that name it (10)

- `site.AppleSARInterfaceSPMIWLANIDC`
- `static OSPtr<AppleSARInterface> AppleSARInterface::create(TransportType, AppleSARSPMI *)`
- `%s::%s:%d: Failed to initialize super class, AppleSARInterface`
- `AppleSARInterface`
- `AppleSARInterfaceSPMIIDC`
- `site.AppleSARInterface`
- `AppleSARInterfaceSPMIWLANIDC`
- `static OSSharedPtr<AppleSARConnectivityCellBoost> AppleSARConnectivityCellBoost::create(IOService *, AppleSARInterface *)`
- `site.AppleSARInterfaceSPMIIDC`
- `%s::%s:%d: Failed to initialize super class, AppleSARInterface`

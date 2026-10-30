# `AppleSARSPMI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSARService`](../kexts/com.apple.driver.AppleSARService.md)
- Object size: `0x190` (400 bytes)
- Metaclass: `0xfffffe000b9945e0`; metaclass vtable `0xfffffe00081cc330`; class vtable `0xfffffe00081cbd98`
- Registration (init): `0xfffffe00094fa770`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (3; 3 in total)

- [`AppleSARSPMIHEB`](AppleSARSPMIHEB.md) — `com.apple.driver.AppleSARService`
- [`AppleSARSPMIIDC`](AppleSARSPMIIDC.md) — `com.apple.driver.AppleSARService`
- [`AppleSARSPMIIDCWLAN`](AppleSARSPMIIDCWLAN.md) — `com.apple.driver.AppleSARService`

## Strings in its kext that name it (13)

- `static OSSharedPtr<AppleE85Mitigation> AppleE85Mitigation::create(IOService *, AppleSARSPMI *)`
- `static OSPtr<AppleSARInterface> AppleSARInterface::create(TransportType, AppleSARSPMI *)`
- `site.AppleSARSPMI`
- `AppleSARSPMIIDCWLAN`
- `site.AppleSARSPMIIDC`
- `static OSSharedPtr<AppleSARFusion> AppleSARFusion::create(IOService *, AppleSARSPMI *)`
- `AppleSARSPMIHEB`
- `site.AppleSARSPMIHEB`
- `AppleSARSPMI`
- `%s::%s:%d: AppleSARSPMI: Failed to create Logging instance!\n`
- `site.AppleSARSPMIIDCWLAN`
- `%s::%s:%d: Failed to initialize AppleSARSPMI\n`
- `AppleSARSPMIIDC`

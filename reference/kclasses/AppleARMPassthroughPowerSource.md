# `AppleARMPassthroughPowerSource`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPMU`](../kexts/com.apple.driver.AppleARMPMU.md)
- Object size: `0x258` (600 bytes)
- Metaclass: `0xfffffe000b9338b8`; metaclass vtable `0xfffffe0007fb1f10`; class vtable `0xfffffe0007fb1948`
- Registration (init): `0xfffffe00086ec7cc`
- Superclasses: [`AppleARMPMUPowerSource`](AppleARMPMUPowerSource.md) → [`IOPMPowerSource`](IOPMPowerSource.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleARMPassthroughPowerSource` in [`com.apple.driver.AppleARMPMU`](../kexts/com.apple.driver.AppleARMPMU.md): `IOProviderClass` = `IOService`, `IONameMatch` = `charger,passthrough`, `IOProbeScore` = `2000`

## Strings in its kext that name it (2)

- `AppleARMPassthroughPowerSource`
- `site.AppleARMPassthroughPowerSource`

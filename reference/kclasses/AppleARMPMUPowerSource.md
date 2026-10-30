# `AppleARMPMUPowerSource`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPMU`](../kexts/com.apple.driver.AppleARMPMU.md)
- Object size: `0x258` (600 bytes)
- Metaclass: `0xfffffe000b933850`; metaclass vtable `0xfffffe0007fb1860`; class vtable `0xfffffe0007fb1298`
- Registration (init): `0xfffffe00086ec6f4`
- Superclasses: [`IOPMPowerSource`](IOPMPowerSource.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleARMPMUCharger`](AppleARMPMUCharger.md) — `com.apple.driver.AppleARMPMU`
- [`AppleARMPassthroughPowerSource`](AppleARMPassthroughPowerSource.md) — `com.apple.driver.AppleARMPMU`

## Strings in its kext that name it (7)

- `AppleARMPMUPowerSource.cpp`
- `AppleARMPMUPowerSource`
- `site.AppleARMPMUPowerSource`
- `AppleARMPMUPowerSource::powerSupplyDebounce(%u)\n`
- `AppleARMPMUPowerSource::start`
- `%s::%s: %s:  kAppleARMPMUPowerSourceMaxPowerState (%x)\n`
- `AppleARMPMUPowerSource::handleInterrupt[%p] (count %d)\n`

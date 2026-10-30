# `ApplePMUFirmwareDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePMUFirmwareDriver`](../kexts/com.apple.driver.ApplePMUFirmwareDriver.md)
- Object size: `0xd0` (208 bytes)
- Metaclass: `0xfffffe000b9881a8`; metaclass vtable `0xfffffe000819bd40`; class vtable `0xfffffe000819b7e8`
- Registration (init): `0xfffffe0009370b80`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `ApplePMUFirmwareDriver` in [`com.apple.driver.ApplePMUFirmwareDriver`](../kexts/com.apple.driver.ApplePMUFirmwareDriver.md): `IOProviderClass` = `AppleARMSPMIDevice`, `IONameMatch` = `pmu,spmi`, `IOPropertyMatch` = `{'has-fw': '<data 22 chars>'}`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/nub-spmi0/pmu-main`](../devicetree/root__arm-io__nub-spmi0__pmu-main.md) on `pmu,spmi`
- [`/arm-io/nub-spmi0/pmu-main/sgpio-bridge-pmu-main/pmu-secondary`](../devicetree/root__arm-io__nub-spmi0__pmu-main__sgpio-bridge-pmu-main__pmu-secondary.md) on `pmu,spmi`

## Strings in its kext that name it (5)

- `ApplePMUFirmwareDriverUserClient`
- `com.apple.driver.ApplePMUFirmwareDriver.user-access`
- `ApplePMUFirmwareDriver`
- `site.ApplePMUFirmwareDriver`
- `site.ApplePMUFirmwareDriverUserClient`

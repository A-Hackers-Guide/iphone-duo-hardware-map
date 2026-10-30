# `AppleHPMAIDType1`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x1c8` (456 bytes)
- Metaclass: `0xfffffe000b94eff0`; metaclass vtable `0xfffffe00080ff750`; class vtable `0xfffffe00080ff0d8`
- Registration (init): `0xfffffe0008f8d8d8`
- Superclasses: [`IOPortAIDController`](IOPortAIDController.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleHPMAIDType1` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `IOService`, `IONameMatch` = `hpm-aid-controller`

## Strings in its kext that name it (3)

- `AppleHPMAIDType1::getHPMCommsBus - failed to get communication bus service, no messages will be sent`
- `AppleHPMAIDType1`
- `site.AppleHPMAIDType1`

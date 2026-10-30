# `AppleHPMBusController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b94ee60`; metaclass vtable `0xfffffe00080f9f70`; class vtable `0xfffffe00080f99c0`
- Registration (init): `0xfffffe0008f8241c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleHPMBusController` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `usbc,manager`

## Strings in its kext that name it (4)

- `AppleHPMBusController::setActiveHPMCount - Active HPM Counter Altered, new Active = 0x%x, expected = 0x%x\n`
- `AppleHPMBusController::start - being called\n`
- `AppleHPMBusController`
- `site.AppleHPMBusController`

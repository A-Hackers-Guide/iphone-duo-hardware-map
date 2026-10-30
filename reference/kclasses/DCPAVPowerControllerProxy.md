# `DCPAVPowerControllerProxy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md)
- Object size: `0x610` (1,552 bytes)
- Metaclass: `0xfffffe000b9df8d0`; metaclass vtable `0xfffffe00082d50d0`; class vtable `0xfffffe00082d4ad8`
- Registration (init): `0xfffffe0009c27d28`
- Superclasses: [`DCPAVProxy`](DCPAVProxy.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `DCPAVPowerControllerProxy` in [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md): `IOProviderClass` = `AFKEndpointInterface`, `IOPropertyMatch` = `{'EPICName': 'dcpav-power-epic'}`

## Strings in its kext that name it (3)

- `DCPAVPowerControllerProxy`
- `site.DCPAVPowerControllerProxy`
- `IOReturn DCPAVRemotePowerController::_setRemoteDevicePower(DCPAVPowerControllerProxy *, UInt32, UInt32)`

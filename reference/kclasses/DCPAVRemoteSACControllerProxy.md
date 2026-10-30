# `DCPAVRemoteSACControllerProxy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md)
- Object size: `0x618` (1,560 bytes)
- Metaclass: `0xfffffe000b9df6f0`; metaclass vtable `0xfffffe00082cfa38`; class vtable `0xfffffe00082cf450`
- Registration (init): `0xfffffe0009c1d9b8`
- Superclasses: [`DCPAVProxy`](DCPAVProxy.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `DCPAVRemoteSACControllerProxy` in [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md): `IOProviderClass` = `AFKEndpointInterface`, `IOPropertyMatch` = `{'EPICName': 'dcpav-sac-epic'}`

## Strings in its kext that name it (8)

- `site.DCPAVRemoteSACControllerProxy`
- `DCPAVRemoteSACControllerProxy failed to start\n`
- `static void DCPAVRemoteSACControllerProxy::handleRegisterSACAggressor(DCPAVRemoteSACControllerProxy * _Nonnull, const DCPAVIPC::Message * _Nonnull)`
- `IOReturn DCPAVRemoteSACControllerProxy::bootCompleteGated()`
- `DCPAVRemoteSACControllerProxy.cpp`
- `DCPAVRemoteSACControllerProxy`
- `IOReturn DCPAVRemoteSACControllerProxy::selectSACAggressorIndexGated(UInt32 * _Nonnull, UInt32 * _Nonnull)`
- `IOReturn DCPAVSACController::_registerSACAggressor(DCPAVRemoteSACControllerProxy *, UInt32, UInt32, const UInt64 *, const UInt32 *)`

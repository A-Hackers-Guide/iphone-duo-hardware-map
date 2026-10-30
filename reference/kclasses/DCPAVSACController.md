# `DCPAVSACController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md)
- Object size: `0x120` (288 bytes)
- Metaclass: `0xfffffe000b9df6c8`; metaclass vtable `0xfffffe00082cf388`; class vtable `0xfffffe00082cee30`
- Registration (init): `0xfffffe0009c1cf4c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `DCPAVSACController` in [`com.apple.driver.DCPAVFamilyProxy`](../kexts/com.apple.driver.DCPAVFamilyProxy.md): `IOProviderClass` = `IOService`, `IONameMatch` = `['dcp-sac-controller', 'dcp0-sac-controller', 'dcp1-sac-controller']`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/dcp-sac-controller`](../devicetree/root__arm-io__dcp-sac-controller.md) on `dcp-sac-controller`
- [`/arm-io/dcpsec-sac-controller`](../devicetree/root__arm-io__dcpsec-sac-controller.md) on `dcp-sac-controller`

## Strings in its kext that name it (5)

- `DCPAVSACController`
- `virtual bool DCPAVSACController::start(IOService *)`
- `DCPAVSACController.cpp`
- `IOReturn DCPAVSACController::_registerSACAggressor(DCPAVRemoteSACControllerProxy *, UInt32, UInt32, const UInt64 *, const UInt32 *)`
- `site.DCPAVSACController`

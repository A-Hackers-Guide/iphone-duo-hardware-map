# `PMGRDispCtrl`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md)
- Object size: `0xb0` (176 bytes)
- Metaclass: `0xfffffe000b9404e0`; metaclass vtable `0xfffffe000804b620`; class vtable `0xfffffe000804b0c8`
- Registration (init): `0xfffffe0008b5f8b0`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `PMGRDispCtrl` in [`com.apple.driver.AppleDCP`](../kexts/com.apple.driver.AppleDCP.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `pmgr-disp-ctrl`

## Strings in its kext that name it (6)

- `void PMGRDispCtrl::_setPmgrDispCtrlForceWake(bool, IOService * _Nonnull)`
- `PMGRDispCtrl.cpp`
- `site.PMGRDispCtrl`
- `void PMGRDispCtrl::_pollReg(IOLogicalAddress, UInt32, UInt32, UInt32, bool)`
- `virtual bool PMGRDispCtrl::start(IOService * _Nonnull)`
- `PMGRDispCtrl`

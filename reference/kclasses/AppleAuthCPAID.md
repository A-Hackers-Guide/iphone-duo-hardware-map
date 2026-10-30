# `AppleAuthCPAID`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md)
- Object size: `0xc8` (200 bytes)
- Metaclass: `0xfffffe000b937280`; metaclass vtable `0xfffffe0007fed588`; class vtable `0xfffffe0007fecf80`
- Registration (init): `0xfffffe0008994c3c`
- Superclasses: [`AppleAuthCP`](AppleAuthCP.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleAuthCPMGAID`](AppleAuthCPMGAID.md) — `com.apple.driver.AppleAuthCP`

## IOKit personalities that instantiate it (4)

- `AppleAuthCPAID` in [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md): `IOProviderClass` = `IOAccessoryDock9Pin`, `IOMatchCategory` = `AU`
- `AppleAuthCPAIDIOPort` in [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md): `IOProviderClass` = `IOPortTransportAIDBus`, `IOPropertyMatch` = `{'ComponentType': 'mogul,a1222'}`
- `AppleAuthCPAIDInternal` in [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md): `IOProviderClass` = `IOAccessoryIDBusTransport`, `IOMatchCategory` = `AU`
- `AppleAuthCPAIDOrion` in [`com.apple.driver.AppleAuthCP`](../kexts/com.apple.driver.AppleAuthCP.md): `IOProviderClass` = `IOAccessoryManagerOrion`, `IOMatchCategory` = `AU`

## Strings in its kext that name it (8)

- `AppleAuthCPAID: error 0x%x\n`
- `AppleAuthCPAID::_aidTransportLockAction: open failed: ret:%x\n`
- `AppleAuthCPAID::_aidTransportLockAction: GetAuthInfo: ret:%x\n`
- `AppleAuthCPAID::%s: super::start failed\n`
- `AppleAuthCPAID::_threadFunc\n`
- `AppleAuthCPAID::_getIDSN: _vendorId:%x, _productId:%x\n`
- `AppleAuthCPAID`
- `site.AppleAuthCPAID`

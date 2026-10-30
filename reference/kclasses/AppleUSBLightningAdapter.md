# `AppleUSBLightningAdapter`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBLightningAdapter`](../kexts/com.apple.driver.AppleUSBLightningAdapter.md)
- Object size: `0xe90` (3,728 bytes)
- Metaclass: `0xfffffe000b9d5890`; metaclass vtable `0xfffffe00082b2618`; class vtable `0xfffffe00082b1ea0`
- Registration (init): `0xfffffe0009b4cfe0`
- Superclasses: [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `A2868-PD` in [`com.apple.driver.AppleUSBLightningAdapter`](../kexts/com.apple.driver.AppleUSBLightningAdapter.md): `IOProviderClass` = `AppleUVDMEndpoint`, `IOPropertyMatch` = `{'Protocol ID': 9}`

## Strings in its kext that name it (6)

- `site.AppleUSBLightningAdapterBOS`
- `site.AppleUSBLightningAdapter`
- `AppleUSBLightningAdapterBOS`
- `[ERROR] %s::%s(): AppleUSBLightningAdapter: super::start failed\n`
- `AppleUSBLightningAdapter`
- `%s::%s(): AppleUSBLightningAdapter::startGated\n`

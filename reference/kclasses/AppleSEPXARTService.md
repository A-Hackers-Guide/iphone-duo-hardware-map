# `AppleSEPXARTService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000b99a8e0`; metaclass vtable `0xfffffe00081f5928`; class vtable `0xfffffe00081f53d0`
- Registration (init): `0xfffffe000963b6ac`
- Superclasses: [`AppleSEPEndpointService`](AppleSEPEndpointService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `xARTMasterDevice` in [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md): `IOProviderClass` = `AppleSEPDeviceService`, `IONameMatch` = `sep-endpoint,xarm`
- `xARTSlaveDevice` in [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md): `IOProviderClass` = `AppleSEPDeviceService`, `IONameMatch` = `sep-endpoint,xars`

## Strings in its kext that name it (3)

- `AppleSEPXARTService`
- `virtual bool AppleSEPXARTService::start(IOService *)`
- `site.AppleSEPXARTService`

# `AppleSEPDebugService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000b99a5b0`; metaclass vtable `0xfffffe00081f1db8`; class vtable `0xfffffe00081f1860`
- Registration (init): `0xfffffe000962b23c`
- Superclasses: [`AppleSEPEndpointService`](AppleSEPEndpointService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `DebugDevice` in [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md): `IOProviderClass` = `AppleSEPDeviceService`, `IONameMatch` = `sep-endpoint,debu`

## Strings in its kext that name it (3)

- `virtual bool AppleSEPDebugService::start(IOService *)`
- `AppleSEPDebugService`
- `site.AppleSEPDebugService`

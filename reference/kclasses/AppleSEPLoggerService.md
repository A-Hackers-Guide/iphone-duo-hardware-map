# `AppleSEPLoggerService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000b99a7f0`; metaclass vtable `0xfffffe00081f4ae0`; class vtable `0xfffffe00081f4588`
- Registration (init): `0xfffffe00096348e8`
- Superclasses: [`AppleSEPEndpointService`](AppleSEPEndpointService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `LoggingDevice` in [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md): `IOProviderClass` = `AppleSEPDeviceService`, `IONameMatch` = `sep-endpoint,log`

## Strings in its kext that name it (3)

- `site.AppleSEPLoggerService`
- `virtual bool AppleSEPLoggerService::start(IOService *)`
- `AppleSEPLoggerService`

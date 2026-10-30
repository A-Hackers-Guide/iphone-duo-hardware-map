# `IOHIDTranslationService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.IOHIDPowerSource`](../kexts/com.apple.driver.IOHIDPowerSource.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000b9f7230`; metaclass vtable `0xfffffe00083a1630`; class vtable `0xfffffe00083a10c0`
- Registration (init): `0xfffffe000a1fe40c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOHIDTranslationService` in [`com.apple.driver.IOHIDPowerSource`](../kexts/com.apple.driver.IOHIDPowerSource.md): `IOProviderClass` = `IOHIDInterface`, `IOPropertyMatch` = `{'PrimaryUsage': 88, 'PrimaryUsagePage': 65280, 'VendorID': 1452}`, `IOMatchCategory` = `IOHIDTranslationService`

## Strings in its kext that name it (5)

- `IOHIDTranslationServiceClient`
- `site.IOHIDTranslationServiceClient`
- `IOHIDTranslationService`
- `site.IOHIDTranslationService`
- `site.IOHIDTranslationService::IOHIDTranslationService_ivar`

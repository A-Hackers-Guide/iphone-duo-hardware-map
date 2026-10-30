# `AppleUSBALSService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHIDALSService`](../kexts/com.apple.driver.AppleHIDALSService.md)
- Object size: `0x98` (152 bytes)
- Metaclass: `0xfffffe000b94d218`; metaclass vtable `0xfffffe00080dd460`; class vtable `0xfffffe00080dcf08`
- Registration (init): `0xfffffe0008e79ca0`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (3)

- `AppleHIDALS` in [`com.apple.driver.AppleHIDALSService`](../kexts/com.apple.driver.AppleHIDALSService.md): `IOProviderClass` = `IOHIDInterface`
- `LG_HID_ALS` in [`com.apple.driver.AppleHIDALSService`](../kexts/com.apple.driver.AppleHIDALSService.md): `IOProviderClass` = `IOHIDInterface`
- `LG_HID_ALS_XXL` in [`com.apple.driver.AppleHIDALSService`](../kexts/com.apple.driver.AppleHIDALSService.md): `IOProviderClass` = `IOHIDInterface`

## Strings in its kext that name it (4)

- `com.apple.CoreBrightness.AppleUSBALSService`
- `AppleUSBALSService`
- `site.AppleUSBALSService`
- `AppleUSBALSService::start`

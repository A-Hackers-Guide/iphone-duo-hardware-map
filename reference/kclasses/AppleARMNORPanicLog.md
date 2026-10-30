# `AppleARMNORPanicLog`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md)
- Object size: `0x90` (144 bytes)
- Metaclass: `0xfffffe000b934b78`; metaclass vtable `0xfffffe0007fc65d0`; class vtable `0xfffffe0007fc6078`
- Registration (init): `0xfffffe0008734064`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleARMNORPanicLog` in [`com.apple.driver.AppleARMPlatform`](../kexts/com.apple.driver.AppleARMPlatform.md): `IOProviderClass` = `AppleARMNORFlashDevice`, `IONameMatch` = `paniclog`

## Strings in its kext that name it (9)

- `site.AppleARMNORPanicLogDevice`
- `AppleARMNORPanicLog`
- `virtual bool AppleARMNORPanicLogDevice::init(UInt64, OSDictionary *)`
- `%s: could not allocate a AppleARMNORPanicLogDevice\n`
- `bool AppleARMNORPanicLog::createBlockStorageDevice()`
- `virtual bool AppleARMNORPanicLog::start(IOService *)`
- `virtual bool AppleARMNORPanicLogDevice::attach(IOService *)`
- `AppleARMNORPanicLogDevice`
- `site.AppleARMNORPanicLog`

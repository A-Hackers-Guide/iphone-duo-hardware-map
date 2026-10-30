# `AppleARM64ErrorHandler`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEverestErrorHandler`](../kexts/com.apple.driver.AppleEverestErrorHandler.md)
- Object size: `0x38` (56 bytes)
- Metaclass: `0xfffffe000b944f78`; metaclass vtable `0xfffffe000809bb08`; class vtable `0xfffffe000809ba68`
- Registration (init): `0xfffffe0008ca781c`
- Superclasses: [`AppleARMFunction`](AppleARMFunction.md)

## IOKit personalities that instantiate it (1)

- `AppleARM64ErrorHandler` in [`com.apple.driver.AppleEverestErrorHandler`](../kexts/com.apple.driver.AppleEverestErrorHandler.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `cpu-error-handler,everest`

## Strings in its kext that name it (3)

- `site.AppleARM64ErrorHandler`
- `AppleARM64ErrorHandler: will %spanic on correctible ECC errors\n`
- `AppleARM64ErrorHandler`

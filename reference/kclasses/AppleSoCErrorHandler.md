# `AppleSoCErrorHandler`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleT8160`](../kexts/com.apple.driver.AppleT8160.md)
- Object size: `0x1d0f8` (119,032 bytes)
- Metaclass: `0xfffffe000b9a6840`; metaclass vtable `0xfffffe00082456e8`; class vtable `0xfffffe00082450f8`
- Registration (init): `0xfffffe0009805bdc`
- Superclasses: [`AppleSoCErrorHandlerCommon`](AppleSoCErrorHandlerCommon.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSoCErrorHandler` in [`com.apple.driver.AppleT8160`](../kexts/com.apple.driver.AppleT8160.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `error-handler,t8160`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/error-handler`](../devicetree/root__arm-io__error-handler.md) on `error-handler,t8160`

## Strings in its kext that name it (8)

- `AppleSoCErrorHandlerT8160.cpp`
- `site.AppleSoCErrorHandlerCommon`
- `AppleSoCErrorHandler`
- `AppleSoCErrorHandlerCommon.cpp`
- `AppleSoCErrorHandlerCommon`
- `AppleSoCErrorHandlerT8160AFX.cpp`
- `AppleSoCErrorHandlerT8160AMCC.cpp`
- `site.AppleSoCErrorHandler`

# `AppleProxHIDEventDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProxDriver`](../kexts/com.apple.driver.AppleProxDriver.md)
- Object size: `0x168` (360 bytes)
- Metaclass: `0xfffffe000b993b40`; metaclass vtable `0xfffffe00081c3508`; class vtable `0xfffffe00081c2da0`
- Registration (init): `0xfffffe0009472e54`
- Superclasses: [`AppleProxAbstractHIDEventDriver`](AppleProxAbstractHIDEventDriver.md) → [`IOHIDEventDriver`](IOHIDEventDriver.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleProxHIDEventDriver` in [`com.apple.driver.AppleProxDriver`](../kexts/com.apple.driver.AppleProxDriver.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `9000`

## Strings in its kext that name it (2)

- `AppleProxHIDEventDriver`
- `site.AppleProxHIDEventDriver`

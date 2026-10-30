# `AppleAtlantisProxHIDEventDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleProxDriver`](../kexts/com.apple.driver.AppleProxDriver.md)
- Object size: `0x148` (328 bytes)
- Metaclass: `0xfffffe000b993b90`; metaclass vtable `0xfffffe00081c3e80`; class vtable `0xfffffe00081c3728`
- Registration (init): `0xfffffe0009474ca4`
- Superclasses: [`AppleProxAbstractHIDEventDriver`](AppleProxAbstractHIDEventDriver.md) → [`IOHIDEventDriver`](IOHIDEventDriver.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `AppleAtlantisProxHIDEventDriver` in [`com.apple.driver.AppleProxDriver`](../kexts/com.apple.driver.AppleProxDriver.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `10000`
- `AppleStargateLProxHIDEventDriver` in [`com.apple.driver.AppleProxDriver`](../kexts/com.apple.driver.AppleProxDriver.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `10000`

## Strings in its kext that name it (2)

- `site.AppleAtlantisProxHIDEventDriver`
- `AppleAtlantisProxHIDEventDriver`

# `AppleSPUMesaDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md)
- Object size: `0x260` (608 bytes)
- Metaclass: `0xfffffe000b99d408`; metaclass vtable `0xfffffe0008222bb8`; class vtable `0xfffffe0008222378`
- Registration (init): `0xfffffe00096eceec`
- Superclasses: [`AppleSPUHIDDriver`](AppleSPUHIDDriver.md) → [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPUMesaDriver` in [`com.apple.driver.AppleSPU`](../kexts/com.apple.driver.AppleSPU.md): `IOProviderClass` = `IOHIDInterface`

## Strings in its kext that name it (2)

- `AppleSPUMesaDriver`
- `site.AppleSPUMesaDriver`

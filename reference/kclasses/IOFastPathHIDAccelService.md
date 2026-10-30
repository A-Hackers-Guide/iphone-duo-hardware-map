# `IOFastPathHIDAccelService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b9f6cf8`; metaclass vtable `0xfffffe00083983d0`; class vtable `0xfffffe0008397e60`
- Registration (init): `0xfffffe000a1ccae0`
- Superclasses: [`IOFastPathHIDService`](IOFastPathHIDService.md) → [`IOFastPathService`](IOFastPathService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `HID Accel IOFastPath` in [`com.apple.iokit.IOHIDEventDriver`](../kexts/com.apple.iokit.IOHIDEventDriver.md): `IOProviderClass` = `IOHIDEventService`, `IOPropertyMatch` = `{'SupportsAccelEvents': True, 'SupportsIOFastPath': True}`, `IOMatchCategory` = `IOFastPathHIDAccelService`, `IOProbeScore` = `1`

## Strings in its kext that name it (2)

- `site.IOFastPathHIDAccelService`
- `IOFastPathHIDAccelService`

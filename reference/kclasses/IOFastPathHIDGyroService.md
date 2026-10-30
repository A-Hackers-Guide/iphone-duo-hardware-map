# `IOFastPathHIDGyroService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md)
- Object size: `0xb8` (184 bytes)
- Metaclass: `0xfffffe000b9f6d20`; metaclass vtable `0xfffffe00083989d8`; class vtable `0xfffffe0008398468`
- Registration (init): `0xfffffe000a1ccb18`
- Superclasses: [`IOFastPathHIDService`](IOFastPathHIDService.md) → [`IOFastPathService`](IOFastPathService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `HID Gyro IOFastPath` in [`com.apple.iokit.IOHIDEventDriver`](../kexts/com.apple.iokit.IOHIDEventDriver.md): `IOProviderClass` = `IOHIDEventService`, `IOPropertyMatch` = `{'SupportsGyroEvents': True, 'SupportsIOFastPath': True}`, `IOMatchCategory` = `IOFastPathHIDGyroService`, `IOProbeScore` = `1`

## Strings in its kext that name it (2)

- `IOFastPathHIDGyroService`
- `site.IOFastPathHIDGyroService`

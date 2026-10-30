# `IOFastPathHIDLEDService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md)
- Object size: `0x120` (288 bytes)
- Metaclass: `0xfffffe000b9f6d70`; metaclass vtable `0xfffffe00083995f0`; class vtable `0xfffffe0008399078`
- Registration (init): `0xfffffe000a1ccb88`
- Superclasses: [`IOFastPathHIDService`](IOFastPathHIDService.md) → [`IOFastPathService`](IOFastPathService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `HID LED Constellation IOFastPath` in [`com.apple.iokit.IOHIDEventDriver`](../kexts/com.apple.iokit.IOHIDEventDriver.md): `IOProviderClass` = `IOHIDEventService`, `IOPropertyMatch` = `{'SupportsIOFastPath': True, 'SupportsLEDConstellation': True}`, `IOMatchCategory` = `IOFastPathHIDLEDService`, `IOProbeScore` = `1`

## Strings in its kext that name it (2)

- `site.IOFastPathHIDLEDService`
- `IOFastPathHIDLEDService`

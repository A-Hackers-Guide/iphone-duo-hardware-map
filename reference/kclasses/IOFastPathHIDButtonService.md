# `IOFastPathHIDButtonService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md)
- Object size: `0xb0` (176 bytes)
- Metaclass: `0xfffffe000b9f6d48`; metaclass vtable `0xfffffe0008398fe0`; class vtable `0xfffffe0008398a70`
- Registration (init): `0xfffffe000a1ccb50`
- Superclasses: [`IOFastPathHIDService`](IOFastPathHIDService.md) → [`IOFastPathService`](IOFastPathService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `HID Button IOFastPath` in [`com.apple.iokit.IOHIDEventDriver`](../kexts/com.apple.iokit.IOHIDEventDriver.md): `IOProviderClass` = `IOHIDEventService`, `IOPropertyMatch` = `{'SupportsButtonEvents': True, 'SupportsIOFastPath': True}`, `IOMatchCategory` = `IOFastPathHIDButtonService`, `IOProbeScore` = `1`

## Strings in its kext that name it (2)

- `site.IOFastPathHIDButtonService`
- `IOFastPathHIDButtonService`

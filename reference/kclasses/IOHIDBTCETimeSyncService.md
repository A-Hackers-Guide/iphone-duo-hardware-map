# `IOHIDBTCETimeSyncService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md)
- Object size: `0xc8` (200 bytes)
- Metaclass: `0xfffffe000b9f66d8`; metaclass vtable `0xfffffe0008392550`; class vtable `0xfffffe0008391fd8`
- Registration (init): `0xfffffe000a1993c0`
- Superclasses: [`IOHIDTimeSyncService`](IOHIDTimeSyncService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `IOHIDBTCETimeSyncService` in [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md): `IOProviderClass` = `IOHIDDevice`, `IOPropertyMatch` = `{'HIDTimeSyncProtocol': 3}`, `IOMatchCategory` = `IOHIDTimeSyncService`

## Strings in its kext that name it (3)

- `IOHIDBTCETimeSyncService.cpp`
- `site.IOHIDBTCETimeSyncService`
- `IOHIDBTCETimeSyncService`

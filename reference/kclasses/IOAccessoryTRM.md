# `IOAccessoryTRM`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000b9f1f98`; metaclass vtable `0xfffffe000833c3d0`; class vtable `0xfffffe000833be78`
- Registration (init): `0xfffffe0009fe3900`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `Transport Restricted Mode - 30pin` in [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md): `IOProviderClass` = `IOAccessoryManager`, `IOPropertyMatch` = `[{'PortType': 13}]`, `IOMatchCategory` = `IOAccessoryTRM`
- `Transport Restricted Mode - Lightning` in [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md): `IOProviderClass` = `IOAccessoryManager`, `IOPropertyMatch` = `[{'PortType': 12}]`, `IOMatchCategory` = `IOAccessoryTRM`

## Strings in its kext that name it (2)

- `IOAccessoryTRM`
- `site.IOAccessoryTRM`

# `IOHIDComplexEventDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md)
- Object size: `0x130` (304 bytes)
- Metaclass: `0xfffffe000b9f6930`; metaclass vtable `0xfffffe0008394eb8`; class vtable `0xfffffe00083947c0`
- Registration (init): `0xfffffe000a1a8b48`
- Superclasses: [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `Topological HID Driver` in [`com.apple.iokit.IOHIDEventDriver`](../kexts/com.apple.iokit.IOHIDEventDriver.md): `IOProviderClass` = `IOHIDInterface`, `IOPropertyMatch` = `{'SupportsHIDInputTopology': True}`, `IOProbeScore` = `3000`

## Strings in its kext that name it (3)

- `IOHIDComplexEventDriver.cpp`
- `site.IOHIDComplexEventDriver`
- `IOHIDComplexEventDriver`

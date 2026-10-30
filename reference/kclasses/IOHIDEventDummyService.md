# `IOHIDEventDummyService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md)
- Object size: `0xd0` (208 bytes)
- Metaclass: `0xfffffe000b9f6548`; metaclass vtable `0xfffffe000838f468`; class vtable `0xfffffe000838ed78`
- Registration (init): `0xfffffe000a184488`
- Superclasses: [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (3)

- `Apple Pencil DM IOService (wired)` in [`com.apple.driver.ApplePencilDriver`](../kexts/com.apple.driver.ApplePencilDriver.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Apple Pencil DM IOService (wireless)` in [`com.apple.driver.ApplePencilDriver`](../kexts/com.apple.driver.ApplePencilDriver.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Apple Pencil Motion IOService` in [`com.apple.driver.ApplePencilDriver`](../kexts/com.apple.driver.ApplePencilDriver.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`

## Strings in its kext that name it (2)

- `site.IOHIDEventDummyService`
- `IOHIDEventDummyService`

# `IOAccessoryDock0PinBuiltin`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md)
- Object size: `0xe20` (3,616 bytes)
- Metaclass: `0xfffffe000b9f2550`; metaclass vtable `0xfffffe0008348ac8`; class vtable `0xfffffe0008348350`
- Registration (init): `0xfffffe000a014be4`
- Superclasses: [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `Dock 0-pin` in [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md): `IOProviderClass` = `IOService`, `IONameMatch` = `['dock,0pin']`

## Device-tree nodes it binds (1) [DT]

- [`/port-magsafe-1`](../devicetree/root__port-magsafe-1.md) on `dock,0pin`

## Strings in its kext that name it (2)

- `site.IOAccessoryDock0PinBuiltin`
- `IOAccessoryDock0PinBuiltin`

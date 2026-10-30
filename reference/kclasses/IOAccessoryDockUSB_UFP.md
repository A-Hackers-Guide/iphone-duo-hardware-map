# `IOAccessoryDockUSB_UFP`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md)
- Object size: `0xe20` (3,616 bytes)
- Metaclass: `0xfffffe000b9f2088`; metaclass vtable `0xfffffe000833e5b0`; class vtable `0xfffffe000833de38`
- Registration (init): `0xfffffe0009fe7a04`
- Superclasses: [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleSMCDockUSB_UFP`](AppleSMCDockUSB_UFP.md) — `com.apple.driver.AppleSMC`

## IOKit personalities that instantiate it (1)

- `Dock USB UFP` in [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md): `IOProviderClass` = `IOService`, `IONameMatch` = `['dock,usb-ufp']`

## Strings in its kext that name it (3)

- `IOAccessoryDockUSB_UFP::handleAccessoryDetect`
- `IOAccessoryDockUSB_UFP`
- `site.IOAccessoryDockUSB_UFP`

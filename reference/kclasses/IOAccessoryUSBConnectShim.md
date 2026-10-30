# `IOAccessoryUSBConnectShim`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md)
- Object size: `0xe0` (224 bytes)
- Metaclass: `0xfffffe000b9f21d8`; metaclass vtable `0xfffffe00083419f0`; class vtable `0xfffffe0008341498`
- Registration (init): `0xfffffe0009ff1b3c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `USB Connect Shim - 30pin` in [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md): `IOProviderClass` = `IOAccessoryManager`, `IOPropertyMatch` = `[{'IOAccessoryPrimaryDevicePort': 1, 'PortType': 13}]`, `IOMatchCategory` = `IOAccessoryUSBConnectShim`
- `USB Connect Shim - Lightning` in [`com.apple.iokit.IOAccessoryManager`](../kexts/com.apple.iokit.IOAccessoryManager.md): `IOProviderClass` = `IOAccessoryManager`, `IOPropertyMatch` = `[{'IOAccessoryPrimaryDevicePort': 1, 'PortType': 12}]`, `IOMatchCategory` = `IOAccessoryUSBConnectShim`

## Strings in its kext that name it (3)

- `site.IOAccessoryUSBConnectShim`
- `IOAccessoryUSBConnectShim`
- `IOAccessoryUSBConnectShimEnableACSleepKey`

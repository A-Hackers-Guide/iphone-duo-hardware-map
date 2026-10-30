# `AppleT8006GPIOIC`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleGPIOICController`](../kexts/com.apple.driver.AppleGPIOICController.md)
- Object size: `0x178` (376 bytes)
- Metaclass: `0xfffffe000b9463e0`; metaclass vtable `0xfffffe00080b4350`; class vtable `0xfffffe00080b3cf8`
- Registration (init): `0xfffffe0008d059d8`
- Superclasses: [`AppleGPIOICController`](AppleGPIOICController.md) → [`IOInterruptController`](IOInterruptController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8006GPIOIC` in [`com.apple.driver.AppleGPIOICController`](../kexts/com.apple.driver.AppleGPIOICController.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `gpio,t8006`

## Strings in its kext that name it (4)

- `site.AppleT8006GPIOIC`
- `AppleT8006GPIOIC.cpp`
- `AppleT8006GPIOIC: wake event %d missing in device-tree\n`
- `AppleT8006GPIOIC`

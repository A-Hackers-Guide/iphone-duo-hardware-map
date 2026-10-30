# `AppleEmbeddedUSBArbitrator`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedUSB`](../kexts/com.apple.driver.AppleEmbeddedUSB.md)
- Object size: `0x1f0` (496 bytes)
- Metaclass: `0xfffffe000b944958`; metaclass vtable `0xfffffe0008094c10`; class vtable `0xfffffe0008094628`
- Registration (init): `0xfffffe0008c9a870`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleEmbeddedUSBArbitrator` in [`com.apple.driver.AppleEmbeddedUSB`](../kexts/com.apple.driver.AppleEmbeddedUSB.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `usb-complex,s5l8900x`

## Strings in its kext that name it (7)

- `AppleEmbeddedUSBArbitrator-force-usbhost`
- `%s::%s: unable to locate AppleEmbeddedUSBArbitrator service\n`
- `site.AppleEmbeddedUSBArbitrator`
- `AppleEmbeddedUSBArbitrator-force-usbdevice`
- `AppleEmbeddedUSBArbitrator`
- `AppleEmbeddedUSBArbitrator-debug`
- `AppleEmbeddedUSBArbitrator-force-usb3host`

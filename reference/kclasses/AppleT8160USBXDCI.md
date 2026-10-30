# `AppleT8160USBXDCI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md)
- Object size: `0x2798` (10,136 bytes)
- Metaclass: `0xfffffe000ba1e830`; metaclass vtable `0xfffffe0008442dd0`; class vtable `0xfffffe0008442478`
- Registration (init): `0xfffffe000a68b03c`
- Superclasses: [`AppleUSBXDCIARM`](AppleUSBXDCIARM.md) → [`AppleUSBXDCI`](AppleUSBXDCI.md) → [`IOUSBDeviceController`](IOUSBDeviceController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8160USBXDCI` in [`com.apple.driver.AppleUSBXDCIARM`](../kexts/com.apple.driver.AppleUSBXDCIARM.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `usb-drd,t8160`, `IOMatchCategory` = `usb-device`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) on `usb-drd,t8160`

## Strings in its kext that name it (3)

- `AppleT8160USBXDCI`
- `AppleT8160USBXDCI.cpp`
- `site.AppleT8160USBXDCI`

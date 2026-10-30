# `AppleT8160USBXHCI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md)
- Object size: `0x1010` (4,112 bytes)
- Metaclass: `0xfffffe000ba1f900`; metaclass vtable `0xfffffe000845d330`; class vtable `0xfffffe000845c8a0`
- Registration (init): `0xfffffe000a7b1c44`
- Superclasses: [`AppleUSBXHCIARM`](AppleUSBXHCIARM.md) → [`AppleUSBXHCI`](AppleUSBXHCI.md) → [`AppleUSBHostController`](AppleUSBHostController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8160USBXHCI` in [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `usb-drd,t8160`, `IOMatchCategory` = `usb-host`, `IOProbeScore` = `10001`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/usb-drd0`](../devicetree/root__arm-io__usb-drd0.md) on `usb-drd,t8160`

## Strings in its kext that name it (3)

- `AppleT8160USBXHCI.cpp`
- `site.AppleT8160USBXHCI`
- `AppleT8160USBXHCI`

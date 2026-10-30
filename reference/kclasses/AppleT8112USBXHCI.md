# `AppleT8112USBXHCI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md)
- Object size: `0x1008` (4,104 bytes)
- Metaclass: `0xfffffe000ba1f780`; metaclass vtable `0xfffffe000845ab38`; class vtable `0xfffffe000845a0a8`
- Registration (init): `0xfffffe000a7932e8`
- Superclasses: [`AppleUSBXHCIARM`](AppleUSBXHCIARM.md) → [`AppleUSBXHCI`](AppleUSBXHCI.md) → [`AppleUSBHostController`](AppleUSBHostController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8112USBXHCI` in [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `usb-drd,t8112`, `IOMatchCategory` = `usb-host`, `IOProbeScore` = `10000`

## Strings in its kext that name it (5)

- `AppleT8112USBXHCICommandRing`
- `AppleT8112USBXHCI`
- `site.AppleT8112USBXHCI`
- `AppleT8112USBXHCI.cpp`
- `site.AppleT8112USBXHCICommandRing`

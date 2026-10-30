# `AppleT8152USBXHCI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md)
- Object size: `0x1008` (4,104 bytes)
- Metaclass: `0xfffffe000ba1f640`; metaclass vtable `0xfffffe00084578c8`; class vtable `0xfffffe0008456e38`
- Registration (init): `0xfffffe000a75bb58`
- Superclasses: [`AppleUSBXHCIARM`](AppleUSBXHCIARM.md) → [`AppleUSBXHCI`](AppleUSBXHCI.md) → [`AppleUSBHostController`](AppleUSBHostController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8152USBXHCI` in [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `usb-drd,t8152`, `IOMatchCategory` = `usb-host`, `IOProbeScore` = `10001`

## Strings in its kext that name it (5)

- `AppleT8152USBXHCICommandRing`
- `site.AppleT8152USBXHCICommandRing`
- `AppleT8152USBXHCI`
- `site.AppleT8152USBXHCI`
- `AppleT8152USBXHCI.cpp`

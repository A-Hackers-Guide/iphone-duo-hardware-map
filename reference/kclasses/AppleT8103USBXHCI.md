# `AppleT8103USBXHCI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md)
- Object size: `0x1030` (4,144 bytes)
- Metaclass: `0xfffffe000ba1f7a8`; metaclass vtable `0xfffffe000845b6d0`; class vtable `0xfffffe000845ac18`
- Registration (init): `0xfffffe000a7a1840`
- Superclasses: [`AppleSynopsysDRDUSBXHCI`](AppleSynopsysDRDUSBXHCI.md) → [`AppleUSBXHCIARM`](AppleUSBXHCIARM.md) → [`AppleUSBXHCI`](AppleUSBXHCI.md) → [`AppleUSBHostController`](AppleUSBHostController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleT6000USBXHCI`](AppleT6000USBXHCI.md) — `com.apple.driver.usb.AppleSynopsysUSB40XHCI`

## IOKit personalities that instantiate it (1)

- `AppleT8103USBXHCI` in [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `usb-drd,t8103`, `IOMatchCategory` = `usb-host`, `IOProbeScore` = `10001`

## Strings in its kext that name it (5)

- `AppleT8103USBXHCI.cpp`
- `AppleT8103USBXHCI`
- `site.AppleT8103USBXHCI`
- `site.AppleT8103USBXHCICommandRing`
- `AppleT8103USBXHCICommandRing`

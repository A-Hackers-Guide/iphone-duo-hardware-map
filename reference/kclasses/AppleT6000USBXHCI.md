# `AppleT6000USBXHCI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md)
- Object size: `0x1030` (4,144 bytes)
- Metaclass: `0xfffffe000ba1f5a0`; metaclass vtable `0xfffffe0008455e58`; class vtable `0xfffffe00084553a0`
- Registration (init): `0xfffffe000a735840`
- Superclasses: [`AppleT8103USBXHCI`](AppleT8103USBXHCI.md) → [`AppleSynopsysDRDUSBXHCI`](AppleSynopsysDRDUSBXHCI.md) → [`AppleUSBXHCIARM`](AppleUSBXHCIARM.md) → [`AppleUSBXHCI`](AppleUSBXHCI.md) → [`AppleUSBHostController`](AppleUSBHostController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT6000USBXHCI` in [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `usb-drd,t6000`, `IOMatchCategory` = `usb-host`, `IOProbeScore` = `10002`

## Strings in its kext that name it (4)

- `AppleT6000USBXHCICommandRing`
- `site.AppleT6000USBXHCICommandRing`
- `AppleT6000USBXHCI`
- `site.AppleT6000USBXHCI`

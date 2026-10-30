# `AppleT8142USBXHCI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md)
- Object size: `0x1008` (4,104 bytes)
- Metaclass: `0xfffffe000ba1f5c8`; metaclass vtable `0xfffffe0008456980`; class vtable `0xfffffe0008455ef0`
- Registration (init): `0xfffffe000a747e2c`
- Superclasses: [`AppleUSBXHCIARM`](AppleUSBXHCIARM.md) → [`AppleUSBXHCI`](AppleUSBXHCI.md) → [`AppleUSBHostController`](AppleUSBHostController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8142USBXHCI` in [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `usb-drd,t8142`, `IOMatchCategory` = `usb-host`, `IOProbeScore` = `10001`

## Strings in its kext that name it (5)

- `AppleT8142USBXHCICommandRing`
- `AppleT8142USBXHCI.cpp`
- `AppleT8142USBXHCI`
- `site.AppleT8142USBXHCICommandRing`
- `site.AppleT8142USBXHCI`

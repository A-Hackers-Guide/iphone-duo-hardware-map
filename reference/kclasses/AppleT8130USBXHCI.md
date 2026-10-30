# `AppleT8130USBXHCI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md)
- Object size: `0x1000` (4,096 bytes)
- Metaclass: `0xfffffe000ba1fb58`; metaclass vtable `0xfffffe0008464668`; class vtable `0xfffffe0008463bd8`
- Registration (init): `0xfffffe000a7df390`
- Superclasses: [`AppleUSBXHCIARM`](AppleUSBXHCIARM.md) → [`AppleUSBXHCI`](AppleUSBXHCI.md) → [`AppleUSBHostController`](AppleUSBHostController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8130USBXHCI` in [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `usb-drd,t8130`, `IOMatchCategory` = `usb-host`, `IOProbeScore` = `10001`

## Strings in its kext that name it (5)

- `AppleT8130USBXHCICommandRing`
- `site.AppleT8130USBXHCI`
- `site.AppleT8130USBXHCICommandRing`
- `AppleT8130USBXHCI`
- `AppleT8130USBXHCI.cpp`

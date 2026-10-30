# `AppleT8027USBXHCI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md)
- Object size: `0xfe0` (4,064 bytes)
- Metaclass: `0xfffffe000ba1fa40`; metaclass vtable `0xfffffe0008460f58`; class vtable `0xfffffe00084604b0`
- Registration (init): `0xfffffe000a7bc8cc`
- Superclasses: [`AppleT8030USBXHCI`](AppleT8030USBXHCI.md) → [`AppleT8101USBXHCI`](AppleT8101USBXHCI.md) → [`AppleSynopsysDRDUSBXHCI`](AppleSynopsysDRDUSBXHCI.md) → [`AppleUSBXHCIARM`](AppleUSBXHCIARM.md) → [`AppleUSBXHCI`](AppleUSBXHCI.md) → [`AppleUSBHostController`](AppleUSBHostController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8027USBXHCI` in [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `usb-drd,t8027`, `IOMatchCategory` = `usb-host`, `IOProbeScore` = `9998`

## Strings in its kext that name it (5)

- `AppleT8027USBXHCI`
- `site.AppleT8027USBXHCICommandRing`
- `site.AppleT8027USBXHCI`
- `AppleT8027USBXHCICommandRing.cpp`
- `AppleT8027USBXHCICommandRing`

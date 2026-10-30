# `AppleT8030USBXHCI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md)
- Object size: `0xfe0` (4,064 bytes)
- Metaclass: `0xfffffe000ba1f9c8`; metaclass vtable `0xfffffe000845f9a8`; class vtable `0xfffffe000845ef00`
- Registration (init): `0xfffffe000a7ba0c8`
- Superclasses: [`AppleT8101USBXHCI`](AppleT8101USBXHCI.md) → [`AppleSynopsysDRDUSBXHCI`](AppleSynopsysDRDUSBXHCI.md) → [`AppleUSBXHCIARM`](AppleUSBXHCIARM.md) → [`AppleUSBXHCI`](AppleUSBXHCI.md) → [`AppleUSBHostController`](AppleUSBHostController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleT8027USBXHCI`](AppleT8027USBXHCI.md) — `com.apple.driver.usb.AppleSynopsysUSBXHCI`

## IOKit personalities that instantiate it (1)

- `AppleT8030USBXHCI` in [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `usb-drd,t8030`, `IOMatchCategory` = `usb-host`, `IOProbeScore` = `9999`

## Strings in its kext that name it (4)

- `site.AppleT8030USBXHCICommandRing`
- `AppleT8030USBXHCI`
- `AppleT8030USBXHCICommandRing`
- `site.AppleT8030USBXHCI`

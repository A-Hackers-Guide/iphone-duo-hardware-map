# `AppleT8140USBXHCI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md)
- Object size: `0xff8` (4,088 bytes)
- Metaclass: `0xfffffe000ba1fb80`; metaclass vtable `0xfffffe00084651d8`; class vtable `0xfffffe0008464748`
- Registration (init): `0xfffffe000a7ed154`
- Superclasses: [`AppleUSBXHCIARM`](AppleUSBXHCIARM.md) → [`AppleUSBXHCI`](AppleUSBXHCI.md) → [`AppleUSBHostController`](AppleUSBHostController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8140USBXHCI` in [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `usb-drd,t8140`, `IOMatchCategory` = `usb-host`, `IOProbeScore` = `10002`

## Strings in its kext that name it (3)

- `AppleT8140USBXHCI`
- `site.AppleT8140USBXHCI`
- `AppleT8140USBXHCI.cpp`

# `AppleT8132USBXHCI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md)
- Object size: `0xff8` (4,088 bytes)
- Metaclass: `0xfffffe000ba1f668`; metaclass vtable `0xfffffe0008458438`; class vtable `0xfffffe00084579a8`
- Registration (init): `0xfffffe000a76e394`
- Superclasses: [`AppleUSBXHCIARM`](AppleUSBXHCIARM.md) → [`AppleUSBXHCI`](AppleUSBXHCI.md) → [`AppleUSBHostController`](AppleUSBHostController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8132USBXHCI` in [`com.apple.driver.usb.AppleSynopsysUSB40XHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSB40XHCI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `usb-drd,t8132`, `IOMatchCategory` = `usb-host`, `IOProbeScore` = `10001`

## Strings in its kext that name it (5)

- `AppleT8132USBXHCICommandRing`
- `site.AppleT8132USBXHCICommandRing`
- `AppleT8132USBXHCI`
- `site.AppleT8132USBXHCI`
- `AppleT8132USBXHCI.cpp`

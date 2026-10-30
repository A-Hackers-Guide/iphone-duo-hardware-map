# `AppleT8101USBXHCI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md)
- Object size: `0xfd8` (4,056 bytes)
- Metaclass: `0xfffffe000ba1fae0`; metaclass vtable `0xfffffe0008462d78`; class vtable `0xfffffe00084622d8`
- Registration (init): `0xfffffe000a7c2e60`
- Superclasses: [`AppleSynopsysDRDUSBXHCI`](AppleSynopsysDRDUSBXHCI.md) → [`AppleUSBXHCIARM`](AppleUSBXHCIARM.md) → [`AppleUSBXHCI`](AppleUSBXHCI.md) → [`AppleUSBHostController`](AppleUSBHostController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 2 in total)

- [`AppleT8030USBXHCI`](AppleT8030USBXHCI.md) — `com.apple.driver.usb.AppleSynopsysUSBXHCI`

## IOKit personalities that instantiate it (1)

- `AppleT8101USBXHCI` in [`com.apple.driver.usb.AppleSynopsysUSBXHCI`](../kexts/com.apple.driver.usb.AppleSynopsysUSBXHCI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `usb-drd,t8101`, `IOMatchCategory` = `usb-host`, `IOProbeScore` = `10000`

## Strings in its kext that name it (2)

- `AppleT8101USBXHCI`
- `site.AppleT8101USBXHCI`

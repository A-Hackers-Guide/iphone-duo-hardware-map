# `AppleUSBNCMData`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.cdc.ncm`](../kexts/com.apple.driver.usb.cdc.ncm.md)
- Object size: `0x848` (2,120 bytes)
- Metaclass: `0xfffffe000b9d5b88`; metaclass vtable `0xfffffe00082b55b0`; class vtable `0xfffffe00082b4d80`
- Registration (init): `0xfffffe0009b59fa0`
- Superclasses: [`IOEthernetController`](IOEthernetController.md) → [`IONetworkController`](IONetworkController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleUSBNCM11Data`](AppleUSBNCM11Data.md) — `com.apple.driver.usb.cdc.ncm`

## IOKit personalities that instantiate it (2)

- `AppleUSBNCMData0` in [`com.apple.driver.usb.cdc.ncm`](../kexts/com.apple.driver.usb.cdc.ncm.md): `IOProviderClass` = `AppleUSBNCMControl`
- `AppleUSBNCMData13` in [`com.apple.driver.usb.cdc.ncm`](../kexts/com.apple.driver.usb.cdc.ncm.md): `IOProviderClass` = `AppleUSBNCMControl`

## Strings in its kext that name it (5)

- `site.AppleUSBNCMDataPoller`
- `AppleUSBNCMData.cpp`
- `AppleUSBNCMData`
- `site.AppleUSBNCMData`
- `AppleUSBNCMDataPoller`

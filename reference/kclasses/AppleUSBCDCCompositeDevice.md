# `AppleUSBCDCCompositeDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.cdc`](../kexts/com.apple.driver.usb.cdc.md)
- Object size: `0xd0` (208 bytes)
- Metaclass: `0xfffffe000b9d48d8`; metaclass vtable `0xfffffe00082a5728`; class vtable `0xfffffe00082a51c0`
- Registration (init): `0xfffffe0009b15794`
- Superclasses: [`AppleUSBHostCompositeDevice`](AppleUSBHostCompositeDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (4)

- `CDCCompositeDevice` in [`com.apple.driver.usb.cdc`](../kexts/com.apple.driver.usb.cdc.md): `IOProviderClass` = `IOUSBHostDevice`
- `CDCCompositeDevice Misc` in [`com.apple.driver.usb.cdc`](../kexts/com.apple.driver.usb.cdc.md): `IOProviderClass` = `IOUSBHostDevice`
- `CDCCompositeDevice Vendor` in [`com.apple.driver.usb.cdc`](../kexts/com.apple.driver.usb.cdc.md): `IOProviderClass` = `IOUSBHostDevice`
- `Medtronics HeartWare VAD Controller` in [`com.apple.driver.usb.cdc`](../kexts/com.apple.driver.usb.cdc.md): `IOProviderClass` = `IOUSBHostDevice`

## Strings in its kext that name it (2)

- `site.AppleUSBCDCCompositeDevice`
- `AppleUSBCDCCompositeDevice`

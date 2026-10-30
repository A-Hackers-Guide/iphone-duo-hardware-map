# `AppleUSB20Hub`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md)
- Object size: `0x258` (600 bytes)
- Metaclass: `0xfffffe000ba20340`; metaclass vtable `0xfffffe0008469c70`; class vtable `0xfffffe0008469620`
- Registration (init): `0xfffffe000a7fc2a8`
- Superclasses: [`AppleUSBHub`](AppleUSBHub.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (3; 3 in total)

- [`AppleUSB20AccessoryHub`](AppleUSB20AccessoryHub.md) — `com.apple.driver.AppleEmbeddedUSBHost`
- [`AppleUSB20CameraKitHub`](AppleUSB20CameraKitHub.md) — `com.apple.driver.usb.AppleUSBHub`
- [`AppleUSB20Hub_32789`](AppleUSB20Hub_32789.md) — `com.apple.driver.AppleEmbeddedUSBHost`

## IOKit personalities that instantiate it (2)

- `AppleUSB20Hub0` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`
- `AppleUSB20Hub1` in [`com.apple.driver.usb.AppleUSBHub`](../kexts/com.apple.driver.usb.AppleUSBHub.md): `IOProviderClass` = `IOUSBHostDevice`

## Strings in its kext that name it (5)

- `site.AppleUSB20Hub`
- `AppleUSB20HubPort`
- `AppleUSB20Hub`
- `site.AppleUSB20HubPort`
- `AppleUSB20HubPort.cpp`

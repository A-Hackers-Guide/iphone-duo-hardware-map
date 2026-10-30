# `IOUSBHostHIDDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.IOUSBHostHIDDevice`](../kexts/com.apple.driver.usb.IOUSBHostHIDDevice.md)
- Object size: `0x168` (360 bytes)
- Metaclass: `0xfffffe000ba209f0`; metaclass vtable `0xfffffe0008474470`; class vtable `0xfffffe0008473d78`
- Registration (init): `0xfffffe000a85c5c8`
- Superclasses: [`IOHIDDevice`](IOHIDDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleUSBHostBulkHIDDevice`](AppleUSBHostBulkHIDDevice.md) — `com.apple.driver.usb.IOUSBHostHIDDevice`
- [`AppleUSBTopCaseHIDDriver`](AppleUSBTopCaseHIDDriver.md) — `com.apple.driver.AppleUSBTopCaseDriver`

## IOKit personalities that instantiate it (4)

- `Generic Keyboard` in [`com.apple.driver.usb.IOUSBHostHIDDevice`](../kexts/com.apple.driver.usb.IOUSBHostHIDDevice.md): `IOProviderClass` = `IOUSBHostInterface`
- `IOUSBHostHIDDevice0` in [`com.apple.driver.usb.IOUSBHostHIDDeviceSafeBoot`](../kexts/com.apple.driver.usb.IOUSBHostHIDDeviceSafeBoot.md): `IOProviderClass` = `IOUSBHostInterface`
- `IOUSBHostHIDDevice1` in [`com.apple.driver.usb.IOUSBHostHIDDeviceSafeBoot`](../kexts/com.apple.driver.usb.IOUSBHostHIDDeviceSafeBoot.md): `IOProviderClass` = `IOUSBHostInterface`
- `SaitekP2500` in [`com.apple.driver.usb.IOUSBHostHIDDeviceSafeBoot`](../kexts/com.apple.driver.usb.IOUSBHostHIDDeviceSafeBoot.md): `IOProviderClass` = `IOUSBHostInterface`

## Strings in its kext that name it (2)

- `IOUSBHostHIDDevice`
- `site.IOUSBHostHIDDevice`

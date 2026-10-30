# `AppleUSBHostBulkHIDDevice`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.usb.IOUSBHostHIDDevice`](../kexts/com.apple.driver.usb.IOUSBHostHIDDevice.md)
- Object size: `0x170` (368 bytes)
- Metaclass: `0xfffffe000ba209c8`; metaclass vtable `0xfffffe0008473ce0`; class vtable `0xfffffe00084735e8`
- Registration (init): `0xfffffe000a856144`
- Superclasses: [`IOUSBHostHIDDevice`](IOUSBHostHIDDevice.md) → [`IOHIDDevice`](IOHIDDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (4)

- `AppleUSBHostBulkHIDDevice - TopCase - 666` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`, `IOProbeScore` = `100000`
- `AppleUSBHostBulkHIDDevice - TopCase - 671` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`, `IOProbeScore` = `100000`
- `AppleUSBHostBulkHIDDevice - TopCase - 801` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`, `IOProbeScore` = `100000`
- `AppleUSBHostBulkHIDDevice - TopCase - 802` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`, `IOProbeScore` = `100000`

## Strings in its kext that name it (2)

- `site.AppleUSBHostBulkHIDDevice`
- `AppleUSBHostBulkHIDDevice`

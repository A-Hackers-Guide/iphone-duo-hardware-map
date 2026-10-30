# `AppleUSBTopCaseHIDDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleUSBTopCaseDriver`](../kexts/com.apple.driver.AppleUSBTopCaseDriver.md)
- Object size: `0x168` (360 bytes)
- Metaclass: `0xfffffe000b9d3688`; metaclass vtable `0xfffffe0008295e58`; class vtable `0xfffffe0008295760`
- Registration (init): `0xfffffe0009a154a8`
- Superclasses: [`IOUSBHostHIDDevice`](IOUSBHostHIDDevice.md) → [`IOHIDDevice`](IOHIDDevice.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (24)

- `Magic Devices - AppleUSBTopCaseHIDDriver` in [`com.apple.driver.AppleUSBTopCaseDriver`](../kexts/com.apple.driver.AppleUSBTopCaseDriver.md): `IOProviderClass` = `IOUSBHostInterface`
- `Magic Keyboards - AppleUSBTopCaseHIDDriver, Device Management` in [`com.apple.driver.AppleUSBTopCaseDriver`](../kexts/com.apple.driver.AppleUSBTopCaseDriver.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Keyboard - DM - TopCase - 666` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Keyboard - DM - TopCase - 668` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Keyboard - DM - TopCase - 671` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Keyboard - DM - TopCase - 800` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Keyboard - DM - TopCase - 801` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Keyboard - DM - TopCase - 802` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Keyboard - TopCase - 666` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Keyboard - TopCase - 668` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Keyboard - TopCase - 671` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Keyboard - TopCase - 800` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Keyboard - TopCase - 801` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Keyboard - TopCase - 802` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Mouse - DM - TopCase - 617` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Mouse - DM - TopCase - 803` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Mouse - TopCase - 617` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Mouse - TopCase - 803` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Trackpad - DM - TopCase - 613` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Trackpad - DM - TopCase - 804` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Trackpad - MT - TopCase - 613` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Trackpad - MT - TopCase - 804` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Trackpad - TopCase - 613` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`
- `AppleUSBTopCaseHIDDriver Trackpad - TopCase - 804` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOUSBHostInterface`

## Strings in its kext that name it (2)

- `AppleUSBTopCaseHIDDriver`
- `site.AppleUSBTopCaseHIDDriver`

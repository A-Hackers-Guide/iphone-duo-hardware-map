# `ApplePMPFirmware`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePMPFirmware`](../kexts/com.apple.driver.ApplePMPFirmware.md)
- Object size: `0xf0` (240 bytes)
- Metaclass: `0xfffffe000b988080`; metaclass vtable `0xfffffe000819afa8`; class vtable `0xfffffe000819aa28`
- Registration (init): `0xfffffe000936e9b8`
- Superclasses: [`RTBuddyFirmwareService`](RTBuddyFirmwareService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (3)

- `ApplePMP0Firmware` in [`com.apple.driver.ApplePMPFirmware`](../kexts/com.apple.driver.ApplePMPFirmware.md): `IOProviderClass` = `RTBuddy`, `IOPropertyMatch` = `{'role': 'PMP0'}`, `IOMatchCategory` = `RTBuddyFirmwareService`
- `ApplePMP1Firmware` in [`com.apple.driver.ApplePMPFirmware`](../kexts/com.apple.driver.ApplePMPFirmware.md): `IOProviderClass` = `RTBuddy`, `IOPropertyMatch` = `{'role': 'PMP1'}`, `IOMatchCategory` = `RTBuddyFirmwareService`
- `ApplePMPFirmware` in [`com.apple.driver.ApplePMPFirmware`](../kexts/com.apple.driver.ApplePMPFirmware.md): `IOProviderClass` = `RTBuddy`, `IOPropertyMatch` = `{'role': 'PMP'}`, `IOMatchCategory` = `RTBuddyFirmwareService`

## Strings in its kext that name it (5)

- `\"ApplePMPFirmware: %s:%u REQUIRE failed: %s\" @%s:%d`
- `site.ApplePMPFirmware`
- `ApplePMPFirmware`
- `virtual bool ApplePMPFirmware::start(IOService *)`
- `ApplePMPFirmware.cpp`

# `AppleHPMSMCBridge`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x110` (272 bytes)
- Metaclass: `0xfffffe000b94f018`; metaclass vtable `0xfffffe00080ffeb8`; class vtable `0xfffffe00080ff7e8`
- Registration (init): `0xfffffe0008f8f058`
- Superclasses: [`AppleHPMEmbedded`](AppleHPMEmbedded.md) → [`AppleHPM`](AppleHPM.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleHPMSMCBridge` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleSMCInterface`, `IONameMatch` = `usbc,cd3217`

## Strings in its kext that name it (6)

- `AppleHPMSMCBridge<%p>::start - hpmlog boot-arg: 0x%X\n`
- `AppleHPMSMCBridge<%p>::start - hpmI2CRetries boot-arg: %u ms\n`
- `AppleHPMSMCBridge<%p>::start - Unable to read hpmlog boot-arg\n`
- `AppleHPMSMCBridge<%p>::start - hpmI2CRetryInterval boot-arg: %u ms\n`
- `AppleHPMSMCBridge`
- `site.AppleHPMSMCBridge`

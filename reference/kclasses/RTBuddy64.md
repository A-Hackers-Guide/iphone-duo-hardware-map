# `RTBuddy64`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md)
- Object size: `0x66a0` (26,272 bytes)
- Metaclass: `0xfffffe000ba23950`; metaclass vtable `0xfffffe0008490b10`; class vtable `0xfffffe0008490420`
- Registration (init): `0xfffffe000a91a55c`
- Superclasses: [`RTBuddy`](RTBuddy.md) → [`IOSlaveProcessor`](IOSlaveProcessor.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `RTBuddy64` in [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md): `IOProviderClass` = `AppleA7IOPNub`, `IONameMatch` = `iop-nub,rtbuddy`

## Strings in its kext that name it (4)

- `virtual IOReturn RTBuddy64::sendMessage(UInt32, void *, void *, bool)`
- `RTBuddy64.cpp`
- `RTBuddy64`
- `site.RTBuddy64`

# `AppleThunderboltHALType5`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltNHI`](../kexts/com.apple.driver.AppleThunderboltNHI.md)
- Object size: `0x468` (1,128 bytes)
- Metaclass: `0xfffffe000b9d27f8`; metaclass vtable `0xfffffe000828b760`; class vtable `0xfffffe000828af78`
- Registration (init): `0xfffffe00099c9c40`
- Superclasses: [`AppleThunderboltHALGenericACIO`](AppleThunderboltHALGenericACIO.md) → [`AppleThunderboltGenericHAL`](AppleThunderboltGenericHAL.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleThunderboltNHI` in [`com.apple.driver.AppleThunderboltNHI`](../kexts/com.apple.driver.AppleThunderboltNHI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `acio`, `IOProbeScore` = `4096`

## Strings in its kext that name it (6)

- `site.AppleThunderboltHALType5`
- `%lldus AppleThunderboltHALType5(%d)::setupRegisterRanges - ERROR: register range %d not found.\n`
- `%lldus AppleThunderboltHALType5(%d)::setupRegisterRanges - found %d register spaces, staring iteration\n`
- `%lldus AppleThunderboltHALType5(%d)::setupRegisterRanges - ERROR: EDT found %d register spaces but only %d allocated\n`
- `AppleThunderboltHALType5`
- `%lldus AppleThunderboltHALType5(%d)::setupRegisterRanges - found %d register spaces, staring iteration\n`

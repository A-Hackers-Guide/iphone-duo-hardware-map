# `AppleThunderboltHALType7`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltNHI`](../kexts/com.apple.driver.AppleThunderboltNHI.md)
- Object size: `0x470` (1,136 bytes)
- Metaclass: `0xfffffe000b9d2a00`; metaclass vtable `0xfffffe000828dc40`; class vtable `0xfffffe000828d450`
- Registration (init): `0xfffffe00099d88fc`
- Superclasses: [`AppleThunderboltHALGenericACIO`](AppleThunderboltHALGenericACIO.md) → [`AppleThunderboltGenericHAL`](AppleThunderboltGenericHAL.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleThunderboltNHI_v2` in [`com.apple.driver.AppleThunderboltNHI`](../kexts/com.apple.driver.AppleThunderboltNHI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `acio,v2`, `IOProbeScore` = `8192`

## Strings in its kext that name it (11)

- `AppleThunderboltHALType7`
- `%lldus AppleThunderboltHALType7(%d)::setupRegisterRanges - ERROR: EDT found %d register spaces but only %d allocated\n`
- `AppleThunderboltHALType7.cpp`
- `%lldus AppleThunderboltHALType7(%d)::setupRegisterRanges - ERROR: register range %d not found.\n`
- `%lldus AppleThunderboltHALType7(%d)::setupSRAMParityInterrupt\n`
- `%lldus AppleThunderboltHALType7(%d)::setupRegisterRanges - ERROR: EDT found %d registers but only %d were mapped.\n`
- `%lldus AppleThunderboltHALType7(%d)::setupRegisterRanges - found %d register spaces, staring iteration\n`
- `site.AppleThunderboltHALType7`
- `\"AppleThunderboltHALType7(%d)::handleSRAMParityInterrupt - SRAM parity error detected\\n\" @%s:%d`
- `%lldus AppleThunderboltHALType7(%d)::setupRegisterRanges - found %d register spaces, staring iteration\n`
- `%lldus AppleThunderboltHALType7(%d)::setupSRAMParityInterrupt\n`

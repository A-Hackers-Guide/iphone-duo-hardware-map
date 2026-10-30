# `AppleThunderboltDPOutAdapterOS2`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltDPOutAdapter`](../kexts/com.apple.driver.AppleThunderboltDPOutAdapter.md)
- Object size: `0x2c8` (712 bytes)
- Metaclass: `0xfffffe000b9d1b38`; metaclass vtable `0xfffffe0008280b80`; class vtable `0xfffffe000827fea0`
- Registration (init): `0xfffffe00099577f4`
- Superclasses: [`AppleThunderboltDPOutAdapterOS`](AppleThunderboltDPOutAdapterOS.md) → [`AppleThunderboltDPOutAdapterCM`](AppleThunderboltDPOutAdapterCM.md) → [`AppleThunderboltDPOutAdapterBase`](AppleThunderboltDPOutAdapterBase.md) → [`AppleThunderboltDPAdapterFamilyBase`](AppleThunderboltDPAdapterFamilyBase.md) → [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleThunderboltDPOutAdapterOS2` in [`com.apple.driver.AppleThunderboltDPOutAdapter`](../kexts/com.apple.driver.AppleThunderboltDPOutAdapter.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `11`

## Strings in its kext that name it (10)

- `%lldus AppleThunderboltDPOutAdapterOS2<%p>::probe - service = %p\n`
- `%lldus AppleThunderboltDPOutAdapterOS2<%p>[%u:0x%llx:0x%x]::doOpenSpecALPM - done, status = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterOS2<%p>[%u:0x%llx:0x%x]::doOpenSpecALPM - ALPM Support = %u\n`
- `AppleThunderboltDPOutAdapterOS2`
- `%lldus AppleThunderboltDPOutAdapterOS2<%p>[%u:0x%llx:0x%x]::doOpenSpecALPM - cl1_exit_time = %u\n`
- `AppleThunderboltDPOutAdapterOS2<%p>[%u:0x%llx:0x%x]::doOpenSpecALPM - ERROR: failed to write CL1 Exit Time! status = 0x%08x\n`
- `AppleThunderboltDPOutAdapterOS2<%p>[%u:0x%llx:0x%x]::doOpenSpecALPM - force enabling ALPM Support\n`
- `AppleThunderboltDPOutAdapterOS2<%p>[%u:0x%llx:0x%x]::doOpenSpecALPM - ERROR: failed to get DPI capabilities offset! status = 0x%08x\n`
- `site.AppleThunderboltDPOutAdapterOS2`
- `AppleThunderboltDPOutAdapterOS2<%p>[%u:0x%llx:0x%x]::doOpenSpecALPM - force disabling ALPM Support\n`

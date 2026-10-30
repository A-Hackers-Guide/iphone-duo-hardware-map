# `AppleSocHot`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md)
- Object size: `0x198` (408 bytes)
- Metaclass: `0xfffffe000b943fb0`; metaclass vtable `0xfffffe0008090ec8`; class vtable `0xfffffe0008090960`
- Registration (init): `0xfffffe0008c8ad40`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSocHot` in [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `sochot,s5l8955x`, `IOResourceMatch` = `IOKit`, `IOProbeScore` = `100`

## Strings in its kext that name it (24)

- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d, Ids %d/%d/%d/%d)\" @%s:%d`
- `AppleSocHot`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d)\" @%s:%d`
- `%s: Couldn't find AppleSocHot instance\n`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d, Ids %d/%d/%d/%d/%d/%d/%d/%d/%d)\" @%s:%d`
- `AppleSocHot::start _tempSensorSochotDebugHackEnabled\n`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d, Ids %d/%d/%d/%d/%d/%d/%d/%d/%d)\" @%s:%d`
- `%s: Couldn't match AppleSocHot service\n`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d, Ids %d/%d/%d/%d)\" @%s:%d`
- `AppleSocHot: Sochot0 using trip temp %d\n`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d, Ids %d/%d/%d/%d/%d/%d/%d/%d/%d)\" @%s:%d`
- `AppleSocHot: Disable sochot1\n`
- `AppleSocHot provider is not AppleARMIODevice\n`
- `AppleSocHot.cpp`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d, Ids %d/%d/%d)\" @%s:%d`
- `site.AppleSocHot`
- `AppleSocHot: Disable sochot0\n`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d, Ids %d/%d/%d/%d/%d/%d/%d/%d/%d)\" @%s:%d`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d, Ids %d/%d/%d/%d/%d/%d)\" @%s:%d`
- `AppleSocHot: provider missing function-clear_dither\n`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d)\" @%s:%d`
- `AppleSocHot: Sochot1 using trip temp %d\n`
- `\"AppleSocHot: Hot Hot Hot (%08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d %08X/%d)\" @%s:%d`
- `\"AppleSocHot: Hot Hot Hot source\" @%s:%d`

# `EXBrightKext`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.EXBrightKext`](../kexts/com.apple.EXBrightKext.md)
- Object size: `0x1b0` (432 bytes)
- Metaclass: `0xfffffe000b9e0120`; metaclass vtable `0xfffffe00082dcce0`; class vtable `0xfffffe00082dc5f0`
- Registration (init): `0xfffffe0009c4821c`
- Superclasses: [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `DeviceTreeName` in [`com.apple.EXBrightKext`](../kexts/com.apple.EXBrightKext.md): `IOProviderClass` = `IOService`, `IONameMatch` = `exbright`, `IOProbeScore` = `10000`

## Device-tree nodes it binds (1) [DT]

- [`/exbright`](../devicetree/root__exbright.md) on `exbright`

## Strings in its kext that name it (12)

- `EXBrightKext`
- `\"TB_ASSERT: \" \"(exbrightkextinterface_exbrightindicatordata__decode(msg, &item) == TB_ERROR_SUCCESS) && \\\"failed to decode type: EXBrightKextInterface.EXBrightIndicatorData\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `[%s] [ERR] EXBrightKextInterface.processALSSamplesAndFetchMIB failed! (%u)\n`
- `EXBrightKextUserClient`
- `EXBrightKext.cpp`
- `EXBrightKextInterface_c.c`
- `[%s] EXBrightKext::start\n`
- `site.EXBrightKext`
- `\"TB_FATAL: \" \"invalid tag in '[EXBrightKextInterface.EXBrightIndicatorData]' metadata: 0x%x\" @%s:%d`
- `\"TB_FATAL: \" \"invalid tag in '[EXBrightKextInterface.EXBrightMIBData]' metadata: 0x%x\" @%s:%d`
- `site.EXBrightKextUserClient`
- `[%s] [DEB] EXBrightKextUserClient::externalMethod - %u\n`

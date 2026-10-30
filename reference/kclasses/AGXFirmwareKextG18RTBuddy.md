# `AGXFirmwareKextG18RTBuddy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AGXFirmwareKextG19PRTBuddy`](../kexts/com.apple.AGXFirmwareKextG19PRTBuddy.md)
- Object size: `0x198` (408 bytes)
- Metaclass: `0xfffffe000b9284c0`; metaclass vtable `0xfffffe0007f6db00`; class vtable `0xfffffe0007f6d4f8`
- Registration (init): `0xfffffe000852b4ac`
- Superclasses: [`AGXFirmwareKextRTBuddy`](AGXFirmwareKextRTBuddy.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `Firmware-Power` in [`com.apple.AGXFirmwareKextG19PRTBuddy`](../kexts/com.apple.AGXFirmwareKextG19PRTBuddy.md): `IOProviderClass` = `RTBuddyService`, `IOPropertyMatch` = `{'role': 'GFX1'}`, `IOMatchCategory` = `AGXFirmwareKextG18RTBuddy`
- `Firmware-Sched` in [`com.apple.AGXFirmwareKextG19PRTBuddy`](../kexts/com.apple.AGXFirmwareKextG19PRTBuddy.md): `IOProviderClass` = `RTBuddyService`, `IOPropertyMatch` = `{'role': 'GFX'}`, `IOMatchCategory` = `AGXFirmwareKextG18RTBuddy`

## Strings in its kext that name it (11)

- `AGXFirmwareKextG18RTBuddy`
- `virtual uint32_t AGXFirmwareKextG18RTBuddy::getBootConfigOffset(AGFIFirmwareRole)`
- `virtual uint32_t AGXFirmwareKextG18RTBuddy::getFirmwareTextSectionBaseOffset(AGFIFirmwareRole)`
- `virtual const char *AGXFirmwareKextG18RTBuddy::getBuild(AGFIFirmwareRole)`
- `virtual uint64_t AGXFirmwareKextG18RTBuddy::getFirmwareTextSectionSize(AGFIFirmwareRole)`
- `virtual const char *AGXFirmwareKextG18RTBuddy::getVersion(AGFIFirmwareRole)`
- `virtual size_t AGXFirmwareKextG18RTBuddy::getRuntimeBinSize(AGFIFirmwareRole)`
- `virtual uint32_t AGXFirmwareKextG18RTBuddy::getFWResumeFlagOffset(AGFIFirmwareRole)`
- `site.AGXFirmwareKextG18RTBuddy`
- `virtual bool AGXFirmwareKextG18RTBuddy::requestFirmwareBinary(const uint8_t **, size_t *, const AGXGPUCoreConfig &, AGFIFirmwareRole)`
- `virtual uint32_t AGXFirmwareKextG18RTBuddy::getFWPdumpBinPatchDataOffset(AGFIFirmwareRole)`

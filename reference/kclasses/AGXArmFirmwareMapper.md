# `AGXArmFirmwareMapper`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md)
- Object size: `0x100` (256 bytes)
- Metaclass: `0xfffffe000b92a7b8`; metaclass vtable `0xfffffe0007f74590`; class vtable `0xfffffe0007f74008`
- Registration (init): `0xfffffe00085a8b4c`
- Superclasses: [`IOMapper`](IOMapper.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AGXArmFirmwareMapper` in [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `iommu-mapper,gfx`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/mapper-gfx-asc`](../devicetree/root__arm-io__mapper-gfx-asc.md) on `iommu-mapper,gfx`

## Strings in its kext that name it (13)

- `virtual IOReturn AGXArmFirmwareMapper::iovmUnmapMemory(IOMemoryDescriptor *, IODMACommand *, uint64_t, uint64_t)`
- `AGXk: %s:%d:%s: !!! Setting AGXArmFirmwareMapper accelerator handle a second time (fAccelerator=0x%p accel=0x%p)!\n`
- `AGXArmFirmwareMapper`
- `AGXk: %s:%d:%s: !!! AGXArmFirmwareMapper::iovmUnmapMemory: unmapping different length than was mapped!\n`
- `void AGXArmFirmwareMapper::setAccelerator(AGXAccelerator *const)`
- `AGXk: %s:%d:%s: !!! AGXArmFirmwareMapper::iovmInsert: insertion into previous mappings not supported!\n`
- `virtual IOReturn AGXArmFirmwareMapper::iovmInsert(uint32_t, uint64_t, uint64_t, uint64_t, uint64_t)`
- `virtual IOReturn AGXArmFirmwareMapper::iovmMapMemory(IOMemoryDescriptor *, uint64_t, uint64_t, uint32_t, const IODMAMapSpecification *, IODMACommand *, const IODMAMapPageList *, uint64_t *, uint64_t *)`
- `site.AGXArmFirmwareMapper`
- `AGXk: %s:%d:%s: !!! AGXArmFirmwareMapper::stop: mapping list not empty!\n`
- `AGXk: %s:%d:%s: !!! Failed to create matching dictionary for AGXArmFirmwareMapper!\n`
- `virtual void AGXArmFirmwareMapper::stop(IOService *)`
- `AGXk: %s:%d:%s: !!! AGXArmFirmwareMapper::iovmUnmapMemory: unmapping address that was never mapped!\n`

# `AGXChannel`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.AGXG19P`](../kexts/com.apple.AGXG19P.md)
- Object size: `0x1d0` (464 bytes)
- Metaclass: `0xfffffe000b92ddb8`; metaclass vtable `0xfffffe0007f6f6c0` (abstract: no class vtable recorded)
- Registration (init): `0xfffffe0008551d6c`
- Superclasses: [`IOGPUChannel`](IOGPUChannel.md)

## Direct subclasses (3; 12 in total)

- [`AGX3DChannel`](AGX3DChannel.md) — `com.apple.AGXG19P`
- [`AGXCLChannel`](AGXCLChannel.md) — `com.apple.AGXG19P`
- [`AGXTAChannel`](AGXTAChannel.md) — `com.apple.AGXG19P`

## Strings in its kext that name it (16)

- `uint32_t AGXChannel::prepareNopResources(IOGPUCommandDescriptor *, AGFIChannelCommandType)`
- `void AGXFirmwareResourceStack<_AGFIChannelState, AGXChannel, 64, 256>::releaseElement(ElementOwner *, uint32_t) [FWResourceManagerElement = _AGFIChannelState, ElementOwner = AGXChannel, kL1WidthBits = 64, kL2WidthBits = 256]`
- `void AGXChannel::addHostKickTraceToRing(uint64_t)`
- `void AGXFirmwareResourceStack<AGXCachedFWChannelMem, AGXChannel, 64, 256>::releaseElement(ElementOwner *, uint32_t) [FWResourceManagerElement = AGXCachedFWChannelMem, ElementOwner = AGXChannel, kL1WidthBits = 64, kL2WidthBits = 256]`
- `uint32_t AGXChannel::submitNop(IOGPUCommandDescriptor *, AGFIChannelCommandType, AGFIDataMasterType)`
- `virtual void AGXArmFirmware::submitCLChannel(AGXChannel *const, const AGXChannelSubmitInfo &, uint32_t, uint32_t, const bool)`
- `site.AGXChannel`
- `virtual void AGXArmFirmware::submitTAChannel(AGXChannel *const, const AGXChannelSubmitInfo &, uint32_t, uint32_t, const bool)`
- `void AGXFirmwareResourceStack<AGXUncachedFWChannelMem, AGXChannel, 64, 256>::releaseElement(ElementOwner *, uint32_t) [FWResourceManagerElement = AGXUncachedFWChannelMem, ElementOwner = AGXChannel, kL1WidthBits = 64, kL2WidthBits = 256]`
- `AGXChannel`
- `virtual void AGXChannel::writeChannelCommandPointer(FirmwareVirtualAddress, AGFIChannelCommandType *, uint64_t)`
- `uint32_t AGXChannel::encodeNops(int32_t, stamp_t)`
- `AGXk: %s:%d:%s: !!! getGuiltyChannel: Type confusion - invalid AGXChannel for firmware guilty_stamp_index %d\n`
- `AGXk: %s:%d:%s: !!! handleChannelErrorEvent: Type confusion - invalid AGXChannel for firmware stamp_idx %u\n`
- `virtual void AGXArmFirmware::submit3DChannel(AGXChannel *const, const AGXChannelSubmitInfo &, uint32_t, uint32_t, const bool, const bool)`
- `void AGXChannel::updateUMAPoolEvent(sIOGPUEvent *, UMAPoolMergeDirection)`

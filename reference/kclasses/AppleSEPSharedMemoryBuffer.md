# `AppleSEPSharedMemoryBuffer`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSEPManager`](../kexts/com.apple.driver.AppleSEPManager.md)
- Object size: `0x48` (72 bytes)
- Metaclass: `0xfffffe000b99af68`; metaclass vtable `0xfffffe00081f7b08`; class vtable `0xfffffe00081f7a50`
- Registration (init): `0xfffffe000964bfd0`
- Superclasses: [`IOSlaveMemoryBuffer`](IOSlaveMemoryBuffer.md) → [`IOSlaveMemory`](IOSlaveMemory.md)

## Strings in its kext that name it (17)

- `AppleSEPCoreBuffer::AppleSEPCoreBuffer(AppleSEPSharedMemoryBuffer *, bool)`
- `AppleSEPSharedMemoryBuffer`
- `virtual IOBufferMemoryDescriptor *AppleSEPSharedMemoryBuffer::getBuffer()`
- `unsigned int AppleSEPManager::_loadChannelObjectEntries(AppleSEPSharedMemoryBuffer::ChannelEntry *, unsigned int)`
- `virtual bool AppleSEPDebugArgs::initWithOwner(AppleSEPSharedMemoryBuffer *)`
- `site.AppleSEPSharedMemoryBuffer`
- `AppleSEPSharedMemoryBuffer.h`
- `bool AppleSEPSharedMemoryBuffer::initWithOptionsAligned(IOOptionBits, IOByteCount, IOByteCount, IOMapper *, uint8_t)`
- `AppleSEPSharedMemoryBuffer::isChannelStandalone(standalone_channels[i])`
- `virtual bool AppleSEPTraceBuffer::initWithOwner(AppleSEPSharedMemoryBuffer *)`
- `static AppleSEPSharedMemoryBuffer::ChannelEntry AppleSEPSharedMemoryBuffer::_mapStandaloneChannel(AppleSEPManager *, ChannelEntry)`
- `void AppleSEPSharedMemoryChannel::attachOwner(AppleSEPSharedMemoryBuffer *)`
- `void AppleSEPCoreBuffer::attachOwner(AppleSEPSharedMemoryBuffer *)`
- `void AppleSEPSharedMemoryBuffer::cleanEntryAt(int, bool)`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/AppleSEPSharedMemoryBuffer.cpp`
- `AppleSEPSharedMemoryBuffer.cpp`
- `IOReturn AppleSEPBooter::bootSEP(AppleSEPFirmware *, bool, AppleSEPSharedMemoryBuffer *, uint8_t *)`

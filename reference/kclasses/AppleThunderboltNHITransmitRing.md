# `AppleThunderboltNHITransmitRing`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltNHI`](../kexts/com.apple.driver.AppleThunderboltNHI.md)
- Object size: `0xd8` (216 bytes)
- Metaclass: `0xfffffe000b9d2730`; metaclass vtable `0xfffffe000828a118`; class vtable `0xfffffe0008289f60`
- Registration (init): `0xfffffe00099c6c78`
- Superclasses: [`IOThunderboltNHITransmitRing`](IOThunderboltNHITransmitRing.md)

## Direct subclasses (1; 3 in total)

- [`AppleThunderboltNHITransmitRingGenericACIO`](AppleThunderboltNHITransmitRingGenericACIO.md) — `com.apple.driver.AppleThunderboltNHI`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltNHITransmitRing(%d)::handleInterrupt\n`
- `%lldus AppleThunderboltNHITransmitRingManager::handleDedicatedInterrupt - interrupt for non-allocated TX ring %d\n`
- `site.AppleThunderboltNHITransmitRingManagerType7`
- `AppleThunderboltNHITransmitRing(%d)::writeNextdescriptor - ERROR - current frame (o=0x%x,l=0x%x) greater than descriptor length 0x%x\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules No Frame List Mid PDF - setting SOF to SOF - 0x%x\n`
- `AppleThunderboltNHITransmitRing`
- `%lldus AppleThunderboltNHITransmitRing(%d)::initWithNHI - hop id = %d\n`
- `AppleThunderboltNHITransmitRing.cpp`
- `%lldus AppleThunderboltNHITransmitRing(%d)::writeNextDescriptor - frame (o=0x%llx,l=0x%llx) total command (o=0x%llx,l=0x%llx)\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)::writeNextDescriptor - FrameList cache STORE: cmd=%p listIdx=%u frameIdx=%u addr=0x%llx details=0x%x\n`
- `AppleThunderboltNHITransmitRingManagerType7`
- `\"AppleThunderboltNHITransmitRing(%d)<%d>::shouldDoubleBuffer - \" \"double buffering detected (o=0x%x, l=0x%x, seg=0x%llx)\\n\" @%s:%d`
- `%lldus AppleThunderboltNHITransmitRing(%d)<%d>::start - always double buffer mode enabled.\n`
- `%lldus AppleThunderboltNHITransmitRingManager::allocateTransmitRing EDT property %s not found, no streaming trace ring allocated\n`
- `%lldus AppleThunderboltNHITransmitRingManager::enableInterrupt - hopID = %d enable = %d\n`
- `%lldus AppleThunderboltNHITransmitRingManager::allocateTransmitRing new ring (index from EDT: %u) allocated at 0x%p\n`
- `AppleThunderboltNHITransmitRingGenericACIO(%d)<%d>::shouldDoubleBuffer - current frame (o=0x%x,l=0x%x) not length aligned, offset = 0x%x\n`
- `%lldus AppleThunderboltNHITransmitRingGenericACIO(%d)<%d>::createDoubleBuffers - failed to create parent block\n`
- `%lldus AppleThunderboltNHITransmitRingManagerGenericACIO(%d)::allocateSharedBuffer - Tx 0: %d Tx 1-%d: %d\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)::configure - dedicated workloop\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)::configure - set dedicated interrupt status = 0x%08x\n`
- `AppleThunderboltNHITransmitRingType7`
- `%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules No Frame List EOF PDF - setting EOF to Mid EOF - 0x%x\n`
- `AppleThunderboltNHITransmitRingGenericACIO`
- `site.AppleThunderboltNHITransmitRing`
- `%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules EOF PDF - setting EOF to EOF index = 0x%llx - 0x%x\n`
- `site.AppleThunderboltNHITransmitRingManagerType5`
- `%lldus AppleThunderboltNHITransmitRing(%d)::submitCommandToNHI\n`
- `site.AppleThunderboltNHITransmitRingType7`
- `%lldus AppleThunderboltNHITransmitRingManagerGenericACIO(%d)::allocateSharedBuffer - total_allocated = %d out of %d\n`
- `%lldus AppleThunderboltNHITransmitRingGenericACIO(%d)<%d>::waitForRingDisableDone - took %lld microseconds - status = 0x%08x\n`
- `site.AppleThunderboltNHITransmitRingManagerGenericACIO`
- `AppleThunderboltNHITransmitRingGenericACIO(%d)<%d>::shouldDoubleBuffer - current frame (o=0x%x,l=0x%x) crosses a page boundary, buffer end offset 0x%x > page size 0x%x\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)::writeNextDescriptor - doubleBuffered = %d buffer_address = %llx segment_length = %lld frame_length = %lld\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)::checkForCompletedDescriptors - complete command %p\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)<%d>::start - ring table [0] 0x%08x\n`
- `%lldus AppleThunderboltNHITransmitRingManager::deallocateTransmitRing - deallocating Tx ring %p\n`
- `AppleThunderboltNHITransmitRingManagerGenericACIO`
- `%lldus AppleThunderboltNHITransmitRingGenericACIO(%d)<%d>::waitForRingDisableDone - data = 0x%08x\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)<%d>::stop\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)::writeNextDescriptor packet[%03d] = 0x%08x\n`
- `site.AppleThunderboltNHITransmitRingManager`
- `site.AppleThunderboltNHITransmitRingGenericACIO`
- `%lldus AppleThunderboltNHITransmitRing(%d)::writeNextDescriptor - frame (currentFrameListIndex=0x%x,fCurrentFrameListFrameIndex=0x%llx) frame_length=0x%x total command (o=0x%x,l=0x%x)\n`
- `AppleThunderboltNHITransmitRingManagerType5`
- `site.AppleThunderboltNHITransmitRingType5`
- `%lldus AppleThunderboltNHITransmitRing(%d)::free - hop id = %d\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)<%d>::start - ring desc 0x%08x 0x%08x 0x%08x 0x%08x\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules No Frame List EOF PDF - setting EOF to EOF - 0x%x\n`
- `%lldus AppleThunderboltNHITransmitRingGenericACIO(%d)<%d>::setSharedBufferAllocation - allocation = %d\n`
- `%lldus AppleThunderboltNHITransmitRingManager::allocateTransmitRing Flags: 0x%x\n`
- `AppleThunderboltNHITransmitRing(%d)<%d>::shouldDoubleBuffer - WARNING - current frame (o=0x%x,l=0x%x) not physically contiguous, segment len 0x%x < physical segment 0x%x\n`
- `%lldus AppleThunderboltNHITransmitRingManagerGenericACIO(%d)::allocateSharedBuffer - Tx 0: %d\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)::checkForCompletedDescriptors - desc[%d] 0x%08x 0x%08x 0x%08x 0x%08x, command = %p\n`
- `AppleThunderboltNHITransmitRingGenericACIO(%d)<%d>::shouldDoubleBuffer - current frame (o=0x%x,l=0x%x) not address aligned, offset = 0x%x\n`
- `%lldus AppleThunderboltNHITransmitRingManagerGenericACIO(%d)::enableInterrupt - hopID = %d interrupt throttling rate = 0x%04x\n`
- `AppleThunderboltNHITransmitRing(%d)::writeNextdescriptor - ERROR - current frame (o=0x%x,l=0x%x) greater than command length (o=0x%x,l=0x%x)\n`
- `%lldus AppleThunderboltNHITransmitRingManagerGenericACIO(%d)::allocateSharedBuffer - WARNING: rings = %d min allocation = %d total allocation = %d\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)<%d>::start - not ready.\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)::writeNextDescriptor\n`

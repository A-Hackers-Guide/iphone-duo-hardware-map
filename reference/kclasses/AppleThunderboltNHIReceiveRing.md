# `AppleThunderboltNHIReceiveRing`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltNHI`](../kexts/com.apple.driver.AppleThunderboltNHI.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000b9d28c0`; metaclass vtable `0xfffffe000828bf70`; class vtable `0xfffffe000828bdc0`
- Registration (init): `0xfffffe00099d2304`
- Superclasses: [`IOThunderboltNHIReceiveRing`](IOThunderboltNHIReceiveRing.md)

## Direct subclasses (1; 3 in total)

- [`AppleThunderboltNHIReceiveRingGenericACIO`](AppleThunderboltNHIReceiveRingGenericACIO.md) — `com.apple.driver.AppleThunderboltNHI`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltNHIReceiveRing(%d)::processInterrupt\n`
- `AppleThunderboltNHIReceiveRingManagerGenericACIO`
- `%lldus AppleThunderboltNHIReceiveRingGenericACIO(%d)<%d>::createDoubleBuffers - failed to create parent block\n`
- `%lldus AppleThunderboltNHIReceiveRing<%p>::checkForCompletedDescriptors packet[%03d] = 0x%02x%02x\n`
- `%lldus AppleThunderboltNHIReceiveRingManagerGenericACIO(%d)::enableInterrupt - write kRegisterInterruptStatusMask0 mask = 0x%08x\n`
- `%lldus AppleThunderboltNHIReceiveRingManager::deallocateReceiveRing - deallocating Rx ring %p\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::configure - dedicated workloop\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::checkForCompletedDescriptors - unbounce - offset = %lld, length = %lld, double_buffer = %p\n`
- `%lldus AppleThunderboltNHIReceiveRing<%p>::checkForCompletedDescriptors packet[%03d] = 0x%02x\n`
- `%lldus AppleThunderboltNHIReceiveRingGenericACIO(%d)<%d>::createDoubleBuffers - failed to create sub block\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::checkForCompletedDescriptors - desc[%d] 0x%08x 0x%08x 0x%08x 0x%08x, command = %p\n`
- `AppleThunderboltNHIReceiveRing(%d)<%d>::shouldDoubleBuffer - WARNING - current frame (o=0x%x,l=0x%x) crosses a page boundary, buffer end offset 0x%x > page size 0x%x\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)<%d>::start - not ready.\n`
- `site.AppleThunderboltNHIReceiveRingType5`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::unconfigure - fOwner = %p, fSoftInterruptEventSource = %p\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::writeNextDescriptor - frame (o=0x%llx,l=0x%llx) total command (o=0x%llx,l=0x%llx)\n`
- `AppleThunderboltNHIReceiveRingType5`
- `AppleThunderboltNHIReceiveRingGenericACIO(%d)<%d>::shouldDoubleBuffer - current frame (o=0x%x,l=0x%x) crosses a page boundary, buffer end offset 0x%x > page size 0x%x\n`
- `\"AppleThunderboltNHIReceiveRingGenericACIO(%d)<%d>::shouldDoubleBuffer - \" \"double buffering detected (o=0x%x, l=0x%x, seg=0x%llx)\\n\" @%s:%d`
- `%lldus AppleThunderboltNHIReceiveRingManager::allocateReceiveRing EDT property %s not found, no streaming trace ring allocated\n`
- `AppleThunderboltNHIReceiveRing(%d)<%d>::shouldDoubleBuffer - WARNING - current frame (o=0x%x,l=0x%x) not DWORD aligned, offset = 0x%x\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::writeNextDescriptor - doubleBuffered = %d buffer_address = %llx segment_length = %lld frame_length = %lld\n`
- `AppleThunderboltNHIReceiveRingGenericACIO(%d)<%d>::shouldDoubleBuffer - current frame (o=0x%x,l=0x%x) not length aligned, offset = 0x%x\n`
- `%lldus AppleThunderboltNHIReceiveRing<%p>::checkForCompletedDescriptors packet[%03d] = 0x%02x%02x%02x\n`
- `%lldus AppleThunderboltNHIReceiveRingManager::enableInterrupt - read mask = 0x%08x\n`
- `%lldus AppleThunderboltNHIReceiveRingManager::allocateReceiveRing no service to query EDT properties, no streaming trace ring allocated\n`
- `%lldus AppleThunderboltNHIReceiveRingGenericACIO(%d)<%d>::initWithNHI\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)<%d>::stop\n`
- `AppleThunderboltNHIReceiveRingGenericACIO(%d)<%d>::shouldDoubleBuffer - current frame (o=0x%x,l=0x%x) not address aligned, offset = 0x%x\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::initWithNHI - hop id = %d\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)<%d>::start - ring table [0] 0x%08x\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::writeNextdescriptor - desc[%d] 0x%08x 0x%08x 0x%08x 0x%08x, command = %p\n`
- `site.AppleThunderboltNHIReceiveRingManager`
- `site.AppleThunderboltNHIReceiveRingManagerType7`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::writeNextDescriptor\n`
- `%lldus AppleThunderboltNHIReceiveRingManager::handleInterrupt - interrupt for non-allocated RX ring %d\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::configure - set dedicated interrupt status = 0x%08x\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::start - ring table [0] 0x%08x\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::writeNextDescriptor (1)\n`
- `%lldus AppleThunderboltNHIReceiveRingManagerGenericACIO(%d)::enableInterrupt - hopID = %d interrupt throttling rate = 0x%04x\n`
- `site.AppleThunderboltNHIReceiveRingManagerType5`
- `%lldus AppleThunderboltNHIReceiveRingManager::enableInterrupt - mask quad = %d mask_bit = %d for hopID = %d\n`
- `site.AppleThunderboltNHIReceiveRingGenericACIO`
- `%lldus AppleThunderboltNHIReceiveRing(%d)<%d>::start - ring desc 0x%08x 0x%08x 0x%08x 0x%08x\n`
- `AppleThunderboltNHIReceiveRingGenericACIO.cpp`
- `AppleThunderboltNHIReceiveRingManager`
- `%lldus AppleThunderboltNHIReceiveRing<%p>::checkForCompletedDescriptors packet[%03d] = 0x%08x\n`
- `%lldus AppleThunderboltNHIReceiveRingGenericACIO(%d)<%d>::waitForRingDisableDone - took %lld microseconds - status = 0x%08x\n`
- `site.AppleThunderboltNHIReceiveRing`
- `site.AppleThunderboltNHIReceiveRingType7`
- `%lldus AppleThunderboltNHIReceiveRing(%d)<%d>::shutdown\n`
- `AppleThunderboltNHIReceiveRingManagerType5`
- `%lldus AppleThunderboltNHIReceiveRingType5(%d)<%d>::setPDFBitmasks - HI Port PDF Bitmask 0x%08x\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::checkForCompletedDescriptors - details = 0x%08x sof = 0x%x eof = 0x%x complete command %p\n`
- `AppleThunderboltNHIReceiveRing(%d)::writeNextdescriptor - ERROR - current frame (o=0x%x,l=0x%llx) greater than descriptor length 0x%x\n`
- `%lldus AppleThunderboltNHIReceiveRingManagerGenericACIO(%d)::enableInterrupt - hopID = %d enable = %d\n`
- `AppleThunderboltNHIReceiveRingGenericACIO(%d)<%d>::shouldDoubleBuffer - current frame (o=0x%x,l=0x%x) smaller than receive frame, segment len 0x%x < frame len 0x%x\n`
- `%lldus AppleThunderboltNHIReceiveRingGenericACIO(%d)<%d>::waitForRingDisableDone - data = 0x%08x\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)<%d>::start - always double buffer mode enabled.\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::configure - create soft interrupt for requesting more work status = 0x%08x\n`

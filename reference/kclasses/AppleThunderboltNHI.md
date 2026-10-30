# `AppleThunderboltNHI`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltNHI`](../kexts/com.apple.driver.AppleThunderboltNHI.md)
- Object size: `0xe8` (232 bytes)
- Metaclass: `0xfffffe000b9d26e0`; metaclass vtable `0xfffffe0008289648`; class vtable `0xfffffe0008288ea8`
- Registration (init): `0xfffffe00099b94ec`
- Superclasses: [`IOThunderboltNHI`](IOThunderboltNHI.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 3 in total)

- [`AppleThunderboltNHIGenericACIO`](AppleThunderboltNHIGenericACIO.md) — `com.apple.driver.AppleThunderboltNHI`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltNHITransmitRing(%d)::handleInterrupt\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::processInterrupt\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::resolvePHandle - phandle_object = %p\n`
- `%lldus AppleThunderboltNHITransmitRingManager::handleDedicatedInterrupt - interrupt for non-allocated TX ring %d\n`
- `AppleThunderboltNHIReceiveRingManagerGenericACIO`
- `site.AppleThunderboltNHIType7`
- `site.AppleThunderboltNHITransmitRingManagerType7`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::enableEmbeddedCPU - fw_state = 0x%x\n`
- `%lldus AppleThunderboltNHI::earlyWakeInternal - fStarted = %d fPMState = %d\n`
- `AppleThunderboltNHITransmitRing(%d)::writeNextdescriptor - ERROR - current frame (o=0x%x,l=0x%x) greater than descriptor length 0x%x\n`
- `%lldus AppleThunderboltNHI::message - unknown message type = 0x%08x\n`
- `%lldus AppleThunderboltNHI::processSetPMState - kThunderboltHALPMLateSleepState\n`
- `%lldus AppleThunderboltNHIReceiveRingGenericACIO(%d)<%d>::createDoubleBuffers - failed to create parent block\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::wake - waking after lateSleep, cable disconnected/powered off, run earlyWake\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::exitPDMode - mode = 0x%08x status = 0x%08x\n`
- `%lldus AppleThunderboltNHIGenericACIO::start - status = 0x%08x\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)<%d>::setMidPDFRules No Frame List Mid PDF - setting SOF to SOF - 0x%x\n`
- `%lldus AppleThunderboltNHIReceiveRing<%p>::checkForCompletedDescriptors packet[%03d] = 0x%02x%02x\n`
- `AppleThunderboltNHITransmitRing`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::applyTunables - ERROR: \"%s\" - length %d not a multiple of entry size %lu\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::checkForCableStateChange - enumerator busy - nothing to do\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::publishTunables\n`
- `%lldus AppleThunderboltNHIReceiveRingManagerGenericACIO(%d)::enableInterrupt - write kRegisterInterruptStatusMask0 mask = 0x%08x\n`
- `%lldus AppleThunderboltNHIGenericACIO::free\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setPhyState - global dispatch queue not found!\n`
- `%lldus AppleThunderboltNHI::doze\n`
- `%lldus AppleThunderboltNHIReceiveRingManager::deallocateReceiveRing - deallocating Rx ring %p\n`
- `AppleThunderboltNHIGenericACIO`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::destroyPowerDomainClientArray\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)::initWithNHI - hop id = %d\n`
- `AppleThunderboltNHITransmitRing.cpp`
- `%lldus AppleThunderboltNHITransmitRing(%d)::writeNextDescriptor - frame (o=0x%llx,l=0x%llx) total command (o=0x%llx,l=0x%llx)\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)::writeNextDescriptor - FrameList cache STORE: cmd=%p listIdx=%u frameIdx=%u addr=0x%llx details=0x%x\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::enableEmbeddedCPU - sleep lstx_level = 0x%08x\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::doze\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::configure - dedicated workloop\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::checkForCompletedDescriptors - unbounce - offset = %lld, length = %lld, double_buffer = %p\n`
- `AppleThunderboltNHITransmitRingManagerType7`
- `%lldus AppleThunderboltNHIGenericACIO::setupPowerSavings - status = 0x%08x\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::powerDomainShouldBeEnabled - disable domain = %d\n`
- `%lldus AppleThunderboltNHIReceiveRing<%p>::checkForCompletedDescriptors packet[%03d] = 0x%02x\n`
- `AppleThunderboltNHI::poweredStart() failed`
- `\"AppleThunderboltNHITransmitRing(%d)<%d>::shouldDoubleBuffer - \" \"double buffering detected (o=0x%x, l=0x%x, seg=0x%llx)\\n\" @%s:%d`
- `%lldus AppleThunderboltNHIReceiveRingGenericACIO(%d)<%d>::createDoubleBuffers - failed to create sub block\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setPhyState - PHY is suspended\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::enableEmbeddedCPU - CPU already disabled.\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::resolvePHandle - ERROR: failed to find service for \"%s\" phandle.\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::processWake\n`
- `%lldus AppleThunderboltNHIReceiveRing(%d)::checkForCompletedDescriptors - desc[%d] 0x%08x 0x%08x 0x%08x 0x%08x, command = %p\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::sleep\n`
- `AppleThunderboltNHIReceiveRing(%d)<%d>::shouldDoubleBuffer - WARNING - current frame (o=0x%x,l=0x%x) crosses a page boundary, buffer end offset 0x%x > page size 0x%x\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setPhyState - ERROR: error suspending the PHY, status = 0x%08x\n`
- `%lldus AppleThunderboltNHIGenericACIO<%p>::enableEmbeddedCPU - cable connected, set LSTX GPIO to output high\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::applyTunables - \"%s\" - tunable_data_length %d, entry size = %lu, tunable_entry_count %d\n`
- `%lldus AppleThunderboltNHIGenericACIO::forcePowerState %d\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::evaluatePowerDomains - return should_be_enabled = %d\n`
- `%lldus AppleThunderboltNHI::processSetPMState - kThunderboltHALPMWakeState\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setPhyState - %s\n`
- `%lldus AppleThunderboltNHI::processSetPMState - kThunderboltHALPMRestartState\n`
- `%lldus AppleThunderboltNHITransmitRing(%d)<%d>::start - always double buffer mode enabled.\n`

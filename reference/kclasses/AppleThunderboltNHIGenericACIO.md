# `AppleThunderboltNHIGenericACIO`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltNHI`](../kexts/com.apple.driver.AppleThunderboltNHI.md)
- Object size: `0x1a0` (416 bytes)
- Metaclass: `0xfffffe000b9d2688`; metaclass vtable `0xfffffe0008288630`; class vtable `0xfffffe0008287d78`
- Registration (init): `0xfffffe00099ae9c4`
- Superclasses: [`AppleThunderboltNHI`](AppleThunderboltNHI.md) → [`IOThunderboltNHI`](IOThunderboltNHI.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleThunderboltNHIType5`](AppleThunderboltNHIType5.md) — `com.apple.driver.AppleThunderboltNHI`
- [`AppleThunderboltNHIType7`](AppleThunderboltNHIType7.md) — `com.apple.driver.AppleThunderboltNHI`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltNHIGenericACIO(%d)::resolvePHandle - phandle_object = %p\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::enableEmbeddedCPU - fw_state = 0x%x\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::wake - waking after lateSleep, cable disconnected/powered off, run earlyWake\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::exitPDMode - mode = 0x%08x status = 0x%08x\n`
- `%lldus AppleThunderboltNHIGenericACIO::start - status = 0x%08x\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::applyTunables - ERROR: \"%s\" - length %d not a multiple of entry size %lu\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::checkForCableStateChange - enumerator busy - nothing to do\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::publishTunables\n`
- `%lldus AppleThunderboltNHIGenericACIO::free\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setPhyState - global dispatch queue not found!\n`
- `AppleThunderboltNHIGenericACIO`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::destroyPowerDomainClientArray\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::enableEmbeddedCPU - sleep lstx_level = 0x%08x\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::doze\n`
- `%lldus AppleThunderboltNHIGenericACIO::setupPowerSavings - status = 0x%08x\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::powerDomainShouldBeEnabled - disable domain = %d\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setPhyState - PHY is suspended\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::enableEmbeddedCPU - CPU already disabled.\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::resolvePHandle - ERROR: failed to find service for \"%s\" phandle.\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::processWake\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::sleep\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setPhyState - ERROR: error suspending the PHY, status = 0x%08x\n`
- `%lldus AppleThunderboltNHIGenericACIO<%p>::enableEmbeddedCPU - cable connected, set LSTX GPIO to output high\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::applyTunables - \"%s\" - tunable_data_length %d, entry size = %lu, tunable_entry_count %d\n`
- `%lldus AppleThunderboltNHIGenericACIO::forcePowerState %d\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::evaluatePowerDomains - return should_be_enabled = %d\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setPhyState - %s\n`
- `%lldus AppleThunderboltNHIGenericACIO::lateSleep\n`
- `%lldus AppleThunderboltNHIGenericACIO<%p>::enableEmbeddedCPU - armio_device->enableDeviceClock(on,4) status = 0x%08x\n`
- `%lldus AppleThunderboltNHIGenericACIO::shutdown - skipped fStarted = %d fPoweredOff = %d\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::start - status = 0x%x\n`
- `%lldus AppleThunderboltNHIGenericACIO<%p>::enableEmbeddedCPU - set LSTX GPIO to default\n`
- `%lldus AppleThunderboltNHIGenericACIO<%p>::enableEmbeddedCPU - no cable connected, set LSTX GPIO to output low\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::checkForCableStateChange - cable connected, bur power down requested (%d, %d), turn off and revaluate\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setPhyState - state = %d\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setPhyState - PHY is already on\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::powerStateChangeDone - B, D - fCableStateChangeInProgress = false\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::doze - sleeping with the cable is connected, run lateSleep\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::destroyPHY\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setARMIODevicePowerState - armio_device->setDevicePowerState( %d, %d )\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::powerDomainShouldBeEnabled - enable domain = %d\n`
- `%lldus AppleThunderboltNHIGenericACIO::earlyWakeInternal\n`
- `%lldus AppleThunderboltNHIGenericACIO::start\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::destroyCableStateTracking\n`
- `%lldus AppleThunderboltNHIGenericACIO<%p>::enableEmbeddedCPU - Current LSTX State = 0x%x set LSTX GPIO to output high\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setupPHY - fPHYService = %p\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setPhyState - PHY is off\n`
- `%lldus AppleThunderboltNHIGenericACIO<%p>::enableEmbeddedCPU - enable = %d\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::enableEmbeddedCPU - opening FW_READY took %lld milliseconds\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setPhyState - ERROR: error suspending the PHY, status = 0x%08x, turn off\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::checkForCableStateChange - we're on, but the cable has been unplugged, turn off\n`
- `%lldus AppleThunderboltNHIGenericACIO<%p>::enableEmbeddedCPU - fEmbeddedCPUEnabled = %d\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::ensurePowerDomainClientArrayCapacity - fPowerDomainClientArrayCapacity = %d\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setupCableStateTracking - status = 0x%08x\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::enableEmbeddedCPU - ERROR: Failed to start embedded CPU.\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::setPhyState - PHY is suspended, turn on\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::checkForCableStateChange - cable change in progress\n`
- `%lldus AppleThunderboltNHIGenericACIO::setHWState - state = %d\n`
- `%lldus AppleThunderboltNHIGenericACIO<%p>::enableEmbeddedCPU - fEmbeddedCPU->setPowerState(off) status = 0x%08x\n`
- `%lldus AppleThunderboltNHIGenericACIO(%d)::applyTunables - \"%s\" - size %d != %lu, skipping tunable: offset = 0x%08x mask = 0x%08llx value=0x%08llx\n`

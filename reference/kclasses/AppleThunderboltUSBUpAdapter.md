# `AppleThunderboltUSBUpAdapter`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltUSBUpAdapter`](../kexts/com.apple.driver.AppleThunderboltUSBUpAdapter.md)
- Object size: `0x138` (312 bytes)
- Metaclass: `0xfffffe000b9d3410`; metaclass vtable `0xfffffe00082931a0`; class vtable `0xfffffe0008292a90`
- Registration (init): `0xfffffe0009a0c830`
- Superclasses: [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (2)

- `AppleThunderboltUSBUpAdapter` in [`com.apple.driver.AppleThunderboltUSBUpAdapter`](../kexts/com.apple.driver.AppleThunderboltUSBUpAdapter.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `4096`
- `AppleThunderboltUSBUpAdapter,TR` in [`com.apple.driver.AppleThunderboltUSBUpAdapter`](../kexts/com.apple.driver.AppleThunderboltUSBUpAdapter.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `6000`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - our_switch = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - fTxPath->allocate() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setupPowerManagement - status = 0x%x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::wake\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - createPaths status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateSync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::destroyPaths\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - state = %ld\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMPauseState\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - fUSBDownPort = %p fUpSwitchUSBUpPort = %p status=0x%llx \n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendSync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateAsync fIsAsleep=0x%d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateAsync fUpSwitchUSBUpAdapter->fActivated=%d fStarted=%d status=0x%llx\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - fRxPath->activateSynchronous() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - deactivateAsync status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendInternal\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendInternal - suspend fRxPath\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateInternal - deactivate fRxPath\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateInternal - deactivate fTxPath\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - ERROR: fRxPath = NULL\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::destroyPowerManagement\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::lateSleep\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::finalize - success = %d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - fTxPath->activateSynchronous() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - fRxPath->allocate() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::sleep\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - the_switch->getPathsDisabledForUpdate() returned %d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - checkPathsDisabledByProtocol() returned %d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendInternal - suspend fTxPath\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - up_switch_up_adapter = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMSleepState\n`
- `%lldus AppleThunderboltUSBUpAdapter<%p>::message - type = 0x%x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - upstream_port = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - destroyPaths() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMWakeState\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::setPowerState - unkonwn power state %ld\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::earlyWake\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - parent_switch = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - down_adapter = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - status = 0x%x fUSBDownPort = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::finalize\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateSync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - enableAdapter( true ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x:%llx:%x)::requestTerminate\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateInternal - fUSBDownAdapter->enableAdapter( false )\n`
- `%lldus AppleThunderboltUSBUpAdapter<%p>::message - type = 0x%x calling activatesync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - fRxRequiredBandwidth = %d fRxMaximumBandwidth = %d fTxRequiredBandwidth = %d fTxMaximumBandwidth = %d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - before setting tunnel source and dest ports, status = 0x%x fUSBDownPort = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateAsync fActivated=%d\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::deactivateInternal\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::createPaths - ERROR: fTxPath = NULL\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::start - upstream_parent_port = %p\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - fActivated = true status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::free\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::suspendAsync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::enableAdapter - enable = %d status=0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter<%p>::message - type = 0x%x calling deactivateAsync\n`
- `%lldus AppleThunderboltUSBUpAdapter(%x@%llx:%x)::activateInternal - fUSBDownAdapter->enableAdapter( true ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBUpAdapter::createResources status = 0x%x\n`

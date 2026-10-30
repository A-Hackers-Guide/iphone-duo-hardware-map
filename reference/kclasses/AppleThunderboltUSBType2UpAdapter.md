# `AppleThunderboltUSBType2UpAdapter`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltUSBType2UpAdapter`](../kexts/com.apple.driver.AppleThunderboltUSBType2UpAdapter.md)
- Object size: `0x130` (304 bytes)
- Metaclass: `0xfffffe000b9d31f0`; metaclass vtable `0xfffffe0008292888`; class vtable `0xfffffe00082920f8`
- Registration (init): `0xfffffe0009a037c0`
- Superclasses: [`IOThunderboltTunnelDriverType2`](IOThunderboltTunnelDriverType2.md) → [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleThunderboltUSBType2UpAdapter` in [`com.apple.driver.AppleThunderboltUSBType2UpAdapter`](../kexts/com.apple.driver.AppleThunderboltUSBType2UpAdapter.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `4096`

## Strings in its kext that name it (60)

- `\"AppleThunderboltUSBType2UpAdapter(%x:%llx:%x)::requestTerminate - ERROR: terminatePhase1 on workloop thread not permitted.\\n\" @%s:%d`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal2 fUSBType2Port=0x%x status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - fActivated = true status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal - enableAdapter( false )\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::configureActiveLinkRate - data = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - fRxRequiredBandwidth = %d fRxMaximumBandwidth = %d fTxRequiredBandwidth = %d fTxMaximumBandwidth = %d\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal1 status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setBundleWeight - data = 0x%lx fPortCount = 0x%lx status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setupPowerManagement - status = 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - fTxPath->activateSynchronous() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::suspendInternal - suspend fTxPath\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal - deactivate fRxPath status = 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal - deactivate fTxPath status = 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - Rx path is using Dedicated FC\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - Rx path is using Shared FC\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - unkonwn power state %ld\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateSync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal-final status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setBundleWeight0 - status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter<%p>::message - type = 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter::createResources status = 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal - fUSBType2DownAdapter->enableAdapter( false )\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::configureLinkCommandsAggregation\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::enableAdapter - findCapability failed status=0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - down_adapter = %p\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - fRxPath->activateSynchronous() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateSync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - fRxPath->allocate() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::sleep\n`
- `AppleThunderboltUSBType2UpAdapter`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::finalize - success = %d\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - fUSBType2DownAdapter->enableAdapter( true ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - deactivateAsync status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::suspendInternal\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - fTxPath->allocate() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - destroyPaths() status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x:%llx:%x)::requestTerminate\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - enableAdapter( ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::enableAdapter - enable = %d status=0x%08x fCurrentPortIndex=0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::destroyPowerManagement\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::earlyWake waiting for all clients to be awake\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateAsync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - ERROR: fRxPath = NULL\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - return\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::free\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::suspendSync\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::suspendInternal - suspend fRxPath\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMWakeState\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - state = %ld\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::setPowerState - kThunderboltPMSleepState\n`
- `%lldus AppleThunderboltUSBType2UpAdapter<%p>::message - type = 0x%x calling activateSync with fUSBType2Port=0x%x\n`
- `site.AppleThunderboltUSBType2UpAdapter`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - parent_switch = %p\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateAsync status= 0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::activateInternal - configureActiveLinkRate( ) status = 0x%08x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::deactivateInternal fUSBType2Port=0x%x\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::getPortCount1 - status=0x%08x data=0x%lx\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::start - status = 0x%x fUSBType2DownPort = %p\n`
- `%lldus AppleThunderboltUSBType2UpAdapter(%x@%llx:%x)::createPaths - Tx path is using Dedicated FC\n`

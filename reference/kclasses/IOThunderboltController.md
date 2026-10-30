# `IOThunderboltController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOThunderboltFamily`](../kexts/com.apple.iokit.IOThunderboltFamily.md)
- Object size: `0x1a0` (416 bytes)
- Metaclass: `0xfffffe000ba1c3f0`; metaclass vtable `0xfffffe00084028a8`; class vtable `0xfffffe0008401f28`
- Registration (init): `0xfffffe000a433a70`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 3 in total)

- [`IOThunderboltControllerGenericACIO`](IOThunderboltControllerGenericACIO.md) — `com.apple.iokit.IOThunderboltFamily`

## Strings in its kext that name it (60)

- `%lldus IOThunderboltController<%p>::free\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::getRootSwitchStaticDataForKey - status = 0x%08x\n`
- `%lldus IOThunderboltController(%d)::updateCLxModeInternal - wakeCLxWaiters fSWObjectionCLxStates=0x%x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::earlyWake - terminatedAllClients\n`
- `%lldus IOThunderboltController<%p>::enableSleep - disable sleep - kIOPMDriverAssertionLevelOn\n`
- `%lldus IOThunderboltController<%p>::findCapability - had to retry findCap 0x%x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::createResources\n`
- `%lldus IOThunderboltController<%p>::start - fTBTFlags 0x%08x\n`
- `%lldus IOThunderboltController(%d)::updateTMUMode - switch_needs_tmu_mode_change = %d route_string = 0x%llx\n`
- `%lldus IOThunderboltController(%d)::updateTMUMode - current tmu mode = %d, new tmu mode = %d\n`
- `%lldus IOThunderboltController(%d)::updateTMUMode - switch_required_tmu_mode = %d route_string = 0x%llx\n`
- `%lldus IOThunderboltController<%p>::switchForRouteString - depth = %d, port = %d\n`
- `%lldus IOThunderboltController<%p>::configWriteDWord - WARNING: synchronous call on workloop thread not permitted.\n`
- `%lldus IOThunderboltController<%p>::start - fTBTOptions 0x%08x\n`
- `%lldus IOThunderboltController(%d)::getCountOfTraceHistories - statistics debug block count = %d\n`
- `%lldus IOThunderboltController<%p>::poweredStart - ERROR: status = 0x%08x\n`
- `%lldus IOThunderboltController<%p>::configModifyDWordWithMask - WARNING: synchronous call on workloop thread not permitted.\n`
- `%lldus IOThunderboltController<%p>::processSetPowerState - kThunderboltPMSleepState\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::checkPathsDisabledByPortType - protocol_flags = 0x%08x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::loadPortMap - fPortMap = %p fPortMapEntryCount = %d status = 0x%08x\n`
- `%lldus IOThunderboltController(%d)::updateCLxModeInternal - sw_clx_objection=0x%x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::earlyWake - ERROR: cable_state is NULL.\n`
- `%lldus IOThunderboltController<%p>::incrementScanCount - fScanCount = %d\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::createTunnelInterfaceManager - attach status = 0x%08x\n`
- `%lldus IOThunderboltController<%p>::shutdown\n`
- `%lldus IOThunderboltController<%p>::poweredStart\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::loadPortDefaults - simulate hidden dp out port - fPortDefaults last entry = %08x status = 0x%08x\n`
- `%lldus IOThunderboltController<%p>::didDecrementScanCount - fQuiesceMode changePowerStateToPriv( kThunderboltPMSleepState )\n`
- `%lldus IOThunderboltController<%p>::processSetPowerState - kThunderboltPMPauseState\n`
- `%lldus IOThunderboltControllerType5(%d)::createSwitchForDeviceHeader - Device ID=0x%04x Vendor ID=0x%04x\n`
- `%lldus IOThunderboltController<%p>::finalize\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::earlyWake - call super\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::getRootSwitchStaticDataForKey - hardware_service = %p status = 0x%08x\n`
- `%lldus IOThunderboltController(%d)::getCountOfTraceHistories - statistics + root switch debug block count = %d\n`
- `%lldus IOThunderboltController<%p>::processSetPowerState - unknown power state %d\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::createTunnelInterfaceManager\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::createTunnelInterfaceManager - hardware_service = %p status = 0x%08x\n`
- `%lldus IOThunderboltController<%p>::systemWillShutdown - kIOMessageSystemWillRestart\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::earlyWake - terminatedAllClients returned\n`
- `%lldus IOThunderboltController<%p>::updateDevicesConnectedStateContext - active user_client found\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::wake - fIsAsleep = %d power_on_allowed = %d\n`
- `%lldus IOThunderboltController<%p>::findCapability - ERROR: findCapability failed with 0x%x\n`
- `%lldus IOThunderboltController(%d)::getTraceHistory - debug block = %p\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::checkPathsDisabledByPortType - paths_disabled = %d\n`
- `%lldus IOThunderboltController(%d)<%p>::setPowerState processSetPowerState - return status = 0x%08x\n`
- `%lldus IOThunderboltController<%p>::configPollDWordWithMask - WARNING: synchronous call on workloop thread not permitted.\n`
- `%lldus IOThunderboltController<%p>::start - could not create NVRAM /options handle\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::createTunnelInterfaceManager - fTunnelInterfaceManager = %p status = 0x%08x\n`
- `%lldus IOThunderboltController(%d)<%p>::setPowerState -  dispatchAsync( processSetPowerState)\n`
- `%lldus IOThunderboltController<%p>::start - ERROR: success = %d\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::earlyWake - returnfIsAsleep = %d\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::processPlugEvent - invalidateAllClients\n`
- `%lldus IOThunderboltController(%d))::lateShutdown - fIsAsleep = %d\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::destroyResources\n`
- `%lldus IOThunderboltController(%d)::updateCLxModeInternal\n`
- `%lldus IOThunderboltController(%d)::getTraceHistory - root switch debug block = %p\n`
- `%lldus IOThunderboltController<%p>::start - IONVRAM not available\n`
- `%lldus IOThunderboltController<%p>::decrementClientScanCount - fClientScanCount = %d\n`
- `%lldus IOThunderboltController(%d)::updateCLxModeInternal enable=0x%x\n`
- `%lldus IOThunderboltControllerGenericACIO(%d)::setupStaticData - Found path disable boot-args = 0x%08x\n`

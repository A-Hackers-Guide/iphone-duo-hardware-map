# `AppleThunderboltDPOutAdapterBase`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltDPOutAdapter`](../kexts/com.apple.driver.AppleThunderboltDPOutAdapter.md)
- Object size: `0x280` (640 bytes)
- Metaclass: `0xfffffe000b9d1ac0`; metaclass vtable `0xfffffe000827e338`; class vtable `0xfffffe000827d6e8`
- Registration (init): `0xfffffe00099469f4`
- Superclasses: [`AppleThunderboltDPAdapterFamilyBase`](AppleThunderboltDPAdapterFamilyBase.md) → [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 3 in total)

- [`AppleThunderboltDPOutAdapterCM`](AppleThunderboltDPOutAdapterCM.md) — `com.apple.driver.AppleThunderboltDPOutAdapter`

## IOKit personalities that instantiate it (1)

- `AppleThunderboltDPOutAdapterBase` in [`com.apple.driver.AppleThunderboltDPOutAdapter`](../kexts/com.apple.driver.AppleThunderboltDPOutAdapter.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `10`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltDPOutAdapterBase<%p>::createPaths - can't read capabilities, using cached local capabilities\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::tmuInitDP - sscOffset = 0x%x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::setupNotifiers - found peer DPO port @ route = 0x%llx, port = 0x%x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::dpAdapterCallback - newService = %p, adapter_type = 0x%x, fWaitingForAdapterNotifications = %d\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::scheduleReactivation - fDPState = %d\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::startActivation - ERROR: fDPState = 0x%x, aborting\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::pollForHPDPropagationInternal - set DPI HPD Output Set bit\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::activationResolved - already resolved\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::hpdStateDetermined - HPD state = %d, fDPState = %d, fActivationRequested = %d, fDeactivationRequested = %d, but do nothing\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::waitForUpstreamAdapters - ERROR: addActivationWaiter failed with 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::deactivate - WARNING: enableDP failed with 0x%08x (hardware removed?)\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::verifyHPD - checking DPO HPD\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::pollForHPDPropagationInternal - clear DPI HPD Output Set bit\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::startActivation - reactivation port: 0x%x @ route 0x%llx\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::createDPTunnels - WARNING: open spec ALPM returned status = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::pollForHPDPropagationInternal - dpi_hpd_asserted = %d\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::activate - ERROR: path_count = %d\n`
- `site.AppleThunderboltDPOutAdapterBase`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::createPaths - attempting to build HBR paths on alternate lane, bandwidth = %d\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::setupNotifiers - found %d candidate DPI ports @ route 0x%llx\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::createDPTunnels - calling dpi->enableDP\n`
- `AppleThunderboltDPOutAdapterBase<%p>[%u:0x%llx:0x%x]::configureDPCapabilities - ERROR: DPI remote writeDPCapabilitiesRegister( 0x%08x ) failed with 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::verifyHPD - WARNING: status = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::activate - ERROR: fDPState != kDPStateActivationInProgress, aborting\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::createPaths - attempting to build HBR3 paths, bandwidth = %d\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::upstreamAdapterActivationResolved - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::waitForUpstreamAdapters - WARNING: DPO adapter %p has been terminated\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::deactivateReleaseDPIReservation - releasing reservation on DPI port 0x%x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::configureDPCapabilities - ERROR: DPO remote writeDPCapabilitiesRegister( 0x%08x ) failed with 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::createDPTunnelsDropSemaphoreHook - dropDPActivationSemaphoreSynchronous() returned 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::hpdStateDetermined - calling activationResolved\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::deactivate - commandWakeup( fFinalizeWaiting )\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::addActivationWaiter - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::hpdStateDetermined - kicking off state change thread\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::activate - fDPState = %d\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::scheduleReactivation - fReactivationRequestInProgress = %d, aborting\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::deactivate - calling destroyPaths\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::createPaths - WARNING: building HBR2 paths failed with 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::free\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::upstreamAdapterActivationResolved - waiting for upstream adapters (again)\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::finishActivation - deactivating: fFinalizeWaiting = %d, fLateSleep = %d, fDeactivationRequested = %d, fActivationRequested = %d, activationSuccess = %d\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::pollForHPDPropagationInternal - waiting for DPI HPD\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::setReactivationDPInPort - already set fReactivationDPInPort = %p\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::createPaths - DPO cached local caps = 0x%08x, DPI cached local caps = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::auxCallback(%cx) - WARNING: incomingStatus = 0x%08x\n`
- `AppleThunderboltDPOutAdapterBase<%p>::verifyHPD - ERROR: We're asleep!\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::createPaths - (3) begin path creation\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::upStreamCIOPort of switch <%p> is NULL, Unexpected!\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::deactivate - fActivationRequested = true, kicking off another activation\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::preEnableDPHook - disable auto link init on DPO port\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::controlPathListenerCallback - deactivated, waiting for upstream adapters\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::configureDPCapabilities - DPO remote writeDPCapabilitiesRegister( 0x%08x )\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::createDPTunnels - calling enableDP\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::createPaths - skip, at least one side does not support extended capabilities: dpo_extended_caps = %u, dpi_extended_caps = %u\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::setupNotifiers - find upstream DPO ports\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::finishActivation - WARNING: HPD state = %d but fDeactivationRequested = %d\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::spawnStateChangeThread - initiated = %d, waiting = %d, asleep = %d, early wake = %d, running = %d, request = %d\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::setupNotifiers - dpo_port->getPortNumber() < fProviderPortStruct.portNumber`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::createPaths - WARNING: building HBR3 paths failed with 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::message - type = 0x%x, state = 0x%x, fProcessDPStateChanges = %d, fInitiatedStateChange = %d, fTerminated = %d\n`

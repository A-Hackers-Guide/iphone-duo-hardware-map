# `AppleThunderboltDPOutAdapter`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltDPOutAdapter`](../kexts/com.apple.driver.AppleThunderboltDPOutAdapter.md)
- Object size: `0x2c0` (704 bytes)
- Metaclass: `0xfffffe000b9d1a98`; metaclass vtable `0xfffffe000827d650`; class vtable `0xfffffe000827cca0`
- Registration (init): `0xfffffe00099338f4`
- Superclasses: [`AppleThunderboltDPAdapterFamily`](AppleThunderboltDPAdapterFamily.md) → [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleThunderboltDPOutAdapter` in [`com.apple.driver.AppleThunderboltDPOutAdapter`](../kexts/com.apple.driver.AppleThunderboltDPOutAdapter.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `9`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltDPOutAdapter<%p>::setupPowerManagement - ERROR: status = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::dpAdapterCallback - ERROR: dispatchAsync( checkIfAllAdaptersFound ) failed with 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::createPaths - can't read capabilities, using cached local capabilities\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::doSynchronousEvaluation - failed to activate previously, trying again\n`
- `site.AppleThunderboltDPOutAdapter`
- `%lldus AppleThunderboltDPOutAdapter<%p>::finishActivation - WARNING: fHPDState = %d but fDeactivationRequested = %d\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::tmuInitDP - sscOffset = 0x%x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::setupNotifiers - found peer DPO port @ route = 0x%llx, port = 0x%x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::dpAdapterCallback - newService = %p, adapter_type = 0x%x, fWaitingForAdapterNotifications = %d\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::setPowerState - new state = %d\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::createPaths - WARNING: building HBR3 paths failed with 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::scheduleReactivation - fDPState = %d\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>::pollForHPDPropagationInternalVerifyDPIHPDOutputFlags - read DPI HPD Output Set and Clear bits\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::doOpenSpecBandwidthAllocationMode - requesting DPCM to broadcast update estimated bandwidth\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::startHPDRead Not ready - fHPDTimerCommand = %p\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::setReactivationDPInPort - ERROR: could not find a free DPI port\n`
- `\"AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::changeState - UNEXPECTED ERROR: we're terminated but we have the wrong desired state! desired_dp_state = %u\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::updateEstimatedBandwidth - done, fCachedEstimatedBW = %u, estimated_bandwidth = %u, status = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::free\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::waitForSNK0PathToActivate - fCandidateDPInAdapterSet is empty!\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::startActivation - ERROR: fDPState = 0x%x, aborting\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::pollForHPDPropagationInternal - set DPI HPD Output Set bit\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::activationResolved - already resolved\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>:deactivateAdapter - WARNING: dpi->clearHPD failed with 0x%08x (hardware removed?)\n`
- `%lldus AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::postCreateDPTunnels - updating video path\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::doOpenSpecBandwidthDowngrade - setting established fEstablishedDPBandwidth = %u, fEstablishedDPLinkRate = %u, fEstablishedDPLaneCount = %u\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::createDPTunnels - common_bandwidth = %d, allocated_bandwidth = %d\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::finalize - fFinalizeWaiting woke up\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::setupNotifiers - addMatchingNotification( kIOTBPortAdapterClientNameDPInLegacy )\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::hpdStateDetermined - HPD state = %d, fDPState = %d, fActivationRequested = %d, fDeactivationRequested = %d, but do nothing\n`
- `\"AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::dpInAdapterStateChange - UNEXPECTED ERROR: this function should not be called!\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterDelegateLegacy<%p>::pollForLocalDPCapsReady - poll kDPVSecConfigReg48: value = 0x%08x, mask = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::waitForUpstreamAdapters - ERROR: addActivationWaiter failed with 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::changeState - we're deactivated and we want to activate, activating\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::dpInAdapterStateChangeNeedReactivationDelegateOverrideHook - fCheckingHPDState = %d, HPD State = %d, fActivationRequested = %d, fFinalizeWaiting = %d\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::processFindHPDCapabilityResults - fHPDCapabilityOffset = 0x%x\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::earlyWake - fReactivateOnWake = %d, fPreserveDPInPort = %d\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::deactivate - WARNING: enableDP failed with 0x%08x (hardware removed?)\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::finishStateChange - (2) commandWakeup( &fEvaluationInProgress )\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::dpAdapterCallback - adding %p to fCandidateDPInAdapterSet\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::verifyHPD - checking DPO HPD\n`
- `AppleThunderboltDPOutAdapterOS<%p>[%u:0x%llx:0x%x]::doOpenSpecBandwidthAllocationMode - ERROR: failed to write CM_ID! status = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::shouldOverdrive - overdrive = %d\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::enableDP - disable auto link init on DPO port\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::enqueueHPDPlugInternal - begin, plug = %d, fHPDState = %d, fNextHPDState = %d, fNeedToProcessHPDState = %d, fNeedToProcessNextHPDState = %d\n`
- `\"AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::callActivationWaiters - WARNING: not valid\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapter<%p>::tmuInitDP - finishing Gen1 DFT workaround\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::createPaths - attempting to build HBR paths on alternate lane, bandwidth = %d\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::dispatchDeactivation - ERROR: dispatchAsync( deactivate ) failed with 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::pollForHPDPropagationInternal - clear DPI HPD Output Set bit\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::startActivation - reactivation port: 0x%x @ route 0x%llx\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::doOpenSpecCMHandshake - OpenSpec DP handshake - complete\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::deactivate - WARNING: fDPState != kDPStateDeactivationInProgress, aborting\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::createPaths - attempting to build HBR2 paths, bandwidth = %d\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::createDPTunnels - WARNING: open spec ALPM returned status = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterBase<%p>::pollForHPDPropagationInternal - dpi_hpd_asserted = %d\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::doOpenSpecBandwidthDowngrade - non_legacy = %d\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::configureDPCapabilities - ERROR: dpi->getLocalDPCapabilities failed with 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::doSynchronousEvaluation - check for higher priority evaluation\n`
- `%lldus AppleThunderboltDPOutAdapter<%p>::createDPTunnels - WARNING: configureDPCapabilities failed with 0x%08x\n`

# `AppleThunderboltDPOutAdapterDelegate`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltDPOutAdapter`](../kexts/com.apple.driver.AppleThunderboltDPOutAdapter.md)
- Object size: `0x68` (104 bytes)
- Metaclass: `0xfffffe000b9d1b60`; metaclass vtable `0xfffffe0008280de0`; class vtable `0xfffffe0008280c18`
- Registration (init): `0xfffffe000995aed0`
- Superclasses: none registered (derives from a kernel-core root such as OSObject)

## Direct subclasses (2; 2 in total)

- [`AppleThunderboltDPOutAdapterDelegateLegacy`](AppleThunderboltDPOutAdapterDelegateLegacy.md) — `com.apple.driver.AppleThunderboltDPOutAdapter`
- [`AppleThunderboltDPOutAdapterDelegateNonLegacy`](AppleThunderboltDPOutAdapterDelegateNonLegacy.md) — `com.apple.driver.AppleThunderboltDPOutAdapter`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::startHPDRead Not ready - fHPDTimerCommand = %p\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::doOpenSpecBandwidthDowngrade - setting established fEstablishedDPBandwidth = %u, fEstablishedDPLinkRate = %u, fEstablishedDPLaneCount = %u\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateLegacy<%p>::pollForLocalDPCapsReady - poll kDPVSecConfigReg48: value = 0x%08x, mask = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::processFindHPDCapabilityResults - fHPDCapabilityOffset = 0x%x\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::doOpenSpecCMHandshake - OpenSpec DP handshake - complete\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::doOpenSpecBandwidthDowngrade - non_legacy = %d\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::doOpenSpecCMHandshake - OpenSpec DP handshake -\u00a0begin\n`
- `AppleThunderboltDPOutAdapterDelegate<%p>::initialHPDPollTimerCommandCallback - ERROR: HPD TRACKING SHOULD BE DISABLED\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::doOpenSpecBandwidthDowngrade - (2) check if DP trained to a lower bandwidth than allocated\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::doOpenSpecCMHandshake - RMW DP_STATUS: value = 0x%08x, mask = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::shouldOverdrive - lc = %p\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::wakeOverrideHook - starting HPD tracking\n`
- `AppleThunderboltDPOutAdapterDelegate<%p>::checkHPDState - ERROR: HPD TRACKING SHOULD BE DISABLED\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::controlPathListenerCallbackNotDeactivatedDelegateOverrideHook - fDPState = %d, jumping to checkHPDState\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::doOpenSpecCMHandshake - non_legacy = %d\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::inheritPathsHPDTrackingDelegateHook - starting HPD tracking\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::doOpenSpecBandwidthDowngrade - (3) give back bandwidth\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::inheritPathsHPDTrackingDelegateHook - HPD tracking disabled, calling hpdStateDetermined()\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::shouldOverdrive - upstream_parent_port->getSwitch() = %p\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::setTMUConvergenceTimeout - Writing to reg 0x%x, tmu_convergence_timeout 0x%x, tmu_convergence_timeout_mask 0x%x, status 0x%x\n`
- `AppleThunderboltDPOutAdapterDelegate<%p>::startFindHPDCapability - ERROR: HPD TRACKING SHOULD BE DISABLED\n`
- `site.AppleThunderboltDPOutAdapterDelegateNonLegacy`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::shouldOverdrive - fDPInPortStruct.dpPort->getSwitch() = %p\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::shouldOverdrive - fProviderPortStruct.dpPort = %p\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::destroyResources\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::shouldOverdrive - fDPInPortStruct.dpPort = %p\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::stopHPDTracking - fHPDReadCommand woke up\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::startHPDTracking - checkHPDState()\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::hpdReadCommandCallback - sample limit (%d) reached: HPD State = %d, fRecheckHPDState = %d\n`
- `AppleThunderboltDPOutAdapterDelegateLegacy.cpp`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::doOpenSpecCMHandshake - CMHS poll timing: before = %llu, after = %llu, diff = %llu\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::createDPTunnelsCanResolveActivationEarlyAfterConfigureDPCapabilities - both DP ports are non-legacy, cannot resolve activation early\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::stopHPDTracking - commandSleep( fHPDReadCommand )\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::pollForCommonDPCapsReady - non_legacy = %d\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::startFindHPDCapability Not ready - fFindHPDCapabilityCommand = %p, fHPDTimerCommand = %p\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::pollForCommonDPCapsReady - Exit DPRX polling loop with status 0x%08x\n`
- `AppleThunderboltDPOutAdapterDelegateNonLegacy`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::hpdReadCommandCallback - commandWakeup( fHPDReadCommand )\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::pollForCommonDPCapsReady - ERROR: DPRX polling timed out\n`
- `site.AppleThunderboltDPOutAdapterDelegateLegacy`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::processFindHPDCapabilityResults - commandWakeup( fFindHPDCapabilityCommand )\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateLegacy<%p>::pollForLocalDPCapsReady - no extended caps\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::shouldOverdrive - status = 0x%08x DATA_STATUS = 0x%08x\n`
- `AppleThunderboltDPOutAdapterDelegateLegacy`
- `site.AppleThunderboltDPOutAdapterDelegate`
- `AppleThunderboltDPOutAdapterDelegate<%p>::stopHPDTracking - ERROR: HPD TRACKING SHOULD BE DISABLED\n`
- `AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::withDPOutAdapter - WARNING: Non-legacy delegate loaded for <TR!\n`
- `AppleThunderboltDPOutAdapterDelegate`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::doOpenSpecBandwidthDowngrade - (1) update DPO cached common capabilities\n`
- `AppleThunderboltDPOutAdapterDelegate<%p>::processFindHPDCapabilityResults - ERROR: HPD TRACKING SHOULD BE DISABLED\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateLegacy<%p>::pollForLocalDPCapsReady - ERROR: kDPVSecConfigReg48 polling failed with 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::waitForUpstreamAdaptersDelegateOverrideHook - nobody to wait for, starting HPD tracking\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::shouldOverdrive - overdrive = %d\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::pause - need HPD tracking, fHPDTracking = %d\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::doOpenSpecCMHandshake - poll CMHS: value = 0x%08x, mask = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::stopHPDTracking\n`
- `%lldus AppleThunderboltDPOutAdapterDelegateNonLegacy<%p>::shouldOverdrive - upstream_parent_port = %p\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::hpdReadCommandCallback - HPD changed during sampling: HPD State = %d\n`
- `%lldus AppleThunderboltDPOutAdapterDelegate<%p>::hpdStateDeterminedDelegateOverrideHook - retry count = %d, submitting timer\n`
- `AppleThunderboltDPOutAdapterDelegate<%p>::hpdTimerCommandCallback - ERROR: HPD TRACKING SHOULD BE DISABLED\n`

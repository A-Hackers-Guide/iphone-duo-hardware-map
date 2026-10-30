# `AppleThunderboltDPOutAdapterCM`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltDPOutAdapter`](../kexts/com.apple.driver.AppleThunderboltDPOutAdapter.md)
- Object size: `0x2b8` (696 bytes)
- Metaclass: `0xfffffe000b9d1ae8`; metaclass vtable `0xfffffe000827f090`; class vtable `0xfffffe000827e3d0`
- Registration (init): `0xfffffe000995219c`
- Superclasses: [`AppleThunderboltDPOutAdapterBase`](AppleThunderboltDPOutAdapterBase.md) → [`AppleThunderboltDPAdapterFamilyBase`](AppleThunderboltDPAdapterFamilyBase.md) → [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 2 in total)

- [`AppleThunderboltDPOutAdapterOS`](AppleThunderboltDPOutAdapterOS.md) — `com.apple.driver.AppleThunderboltDPOutAdapter`

## IOKit personalities that instantiate it (1)

- `AppleThunderboltDPOutAdapterCM` in [`com.apple.driver.AppleThunderboltDPOutAdapter`](../kexts/com.apple.driver.AppleThunderboltDPOutAdapter.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `11`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::doSynchronousEvaluation - failed to activate previously, trying again\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>::pollForHPDPropagationInternalVerifyDPIHPDOutputFlags - read DPI HPD Output Set and Clear bits\n`
- `\"AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::changeState - UNEXPECTED ERROR: we're terminated but we have the wrong desired state! desired_dp_state = %u\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>:deactivateAdapter - WARNING: dpi->clearHPD failed with 0x%08x (hardware removed?)\n`
- `\"AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::dpInAdapterStateChange - UNEXPECTED ERROR: this function should not be called!\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::changeState - we're deactivated and we want to activate, activating\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::finishStateChange - (2) commandWakeup( &fEvaluationInProgress )\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::enqueueHPDPlugInternal - begin, plug = %d, fHPDState = %d, fNextHPDState = %d, fNeedToProcessHPDState = %d, fNeedToProcessNextHPDState = %d\n`
- `\"AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::callActivationWaiters - WARNING: not valid\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::doSynchronousEvaluation - check for higher priority evaluation\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>(%u:0x%08llx:%u)::controlPathListenerCallback - WARNING: fTerminated = %u\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::message - notifying DP Connection Manager that we need evaluation\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::setHPDState - UNEXPECTED ERROR: CM adapters that don't need HPD tracking should not directly set HPD state!\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]:deactivateAdapter - calling destroyPaths\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::doSynchronousEvaluation - need immediate evaluation, calling dispatchChangeState()\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::finishStateChange - UNEXPECTED ERROR: we're terminated, but we're trying to reactivate! fDPState = %u, desired_dp_state = %u\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::requestTerminateInternal - notifying DP Connection Manager that we need evaluation\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::finishStateChangeComplete - HPD plug notification queued, notifying DP Connection Manager that we need re-evaluation\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::start - notifying DP Connection Manager that we need evaluation\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::finishStateChangeCompleteInternal - need to process DP connection up message, fDPState = %d\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::finishStateChange - desired state changed to deactivated, calling changeState()\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::activateAdapter - WARNING: createDPTunnels failed with 0x%08x\n`
- `AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::finishHPDStateDetermined - ERROR: dispatchChangeState() failed, status = 0x%08xn`
- `AppleThunderboltDPOutAdapterCM<%p>::pollForHPDPropagationInternalVerifyDPIHPDOutputFlags - ERROR: failed to write DPI HPD Output Set and Clear bits! status = 0x%08x\n`
- `\"AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::finishStateChange - UNEXPECTED ERROR: fDPState is not in a steady state! fDPState = %u\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::dispatchActivation - UNEXPECTED ERROR: this function should not be called!\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]:deactivateAdapter - ERROR: dpi->enableDP( false ) failed with 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::enqueueVerifiedHPDState - done\n`
- `\"AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::dpInAdapterStateChangeNeedReactivation - UNEXPECTED ERROR: this function should not be called!\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::finishStateChangeComplete\n`
- `\"AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::checkIfAllAdaptersFound - UNEXPECTED ERROR: this function should not be called!\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::finishStateChangeComplete - calling lateSleepComplete()\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>(%u:0x%08llx:%u)::controlPathListenerCallback - WARNING: fStarted = %u\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::doOpenSpecBandwidthDowngradeStatusOverride - WARNING: Open spec bandwidth downgrade flow returned status = 0x%08x\n`
- `\"AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::spawnStateChangeThread - UNEXPECTED ERROR: this function should not be called!\\n\" @%s:%d`
- `AppleThunderboltDPOutAdapterCM`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::controlPathListenerCallback - notifying DP Connection Manager that we need evaluation\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::activationResolved - UNEXPECTED ERROR: this function should not be called!\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::waitForUpstreamAdapters - UNEXPECTED ERROR: this function should not be called!\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::doOpenSpecBandwidthDowngradeStatusOverride - WARNING: Setting fFailedToLight = true\n`
- `\"AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::changeState - UNEXPECTED ERROR: desired DP state is invalid!\\n\" @%s:%d`
- `\"AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::requestTerminateInternal - UNEXPECTED ERROR: we're supposed to be terminating but we've settled into the wrong state! dp state = %u, desired dp state = %u (valid = %u)\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::changeState - calling finishStateChange()\n`
- `\"AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::stateChanged - UNEXPECTED ERROR: this function should not be called!\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::enqueueHPDPlugInternal - done, fHPDState = %d, fNextHPDState = %d, fNeedToProcessHPDState = %d, fNeedToProcessNextHPDState = %d\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::activateAdapter - ERROR: fReactivationDPInPort = NULL, aborting\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::changeState - UNEXPECTED ERROR: late sleep must be a deactivation! fDPState = %u, desired_dp_state = %u\n`
- `AppleThunderboltDPOutAdapterCM<%p>::setupNotifiers - ERROR: couldn't register with the DP connection manager! status = 0x%08x\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::checkWakeWorkPending - UNEXPECTED ERROR: wake work is pending but these flags should not be used, fDeactivationRequested = %d, fActivationRequested = %d\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::hpdStateDetermined - HPD state = %d, fDPState = %d\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::requestTerminateInternal - NE=%u NPBWAR=%u NPCU=%u NPHPDS=%u NPNHPDS=%u DDPSNE=%u HPDS=%u NHPDS=%u DPS=%u DDPS=%u T=%u FW=%u Slp=%u EWk=%u LSlp=%u FA=%u FL=%u HPDT=%u\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::doSynchronousEvaluation - we're in early wake, need immediate activation\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::hpdStateDetermined - HPD tracking flow did_override = %u, trying again\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::requestTerminateInternal - done, NE=%u NPBWAR=%u NPCU=%u NPHPDS=%u NPNHPDS=%u DDPSNE=%u HPDS=%u NHPDS=%u DPS=%u DDPS=%u T=%u FW=%u Slp=%u EWk=%u LSlp=%u FA=%u FL=%u HPDT=%u\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::dequeueHPDPlug - done, fHPDState = %d, fNextHPDState = %d, fNeedToProcessHPDState = %d, fNeedToProcessNextHPDState = %d\n`
- `\"AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::finishStateChange - UNEXPECTED ERROR: we're terminated, but we're trying to reactivate! fDPState = %u, desired_dp_state = %u\\n\" @%s:%d`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::activateAdapter - setting minimum TMU mode\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::addActivationWaiter - UNEXPECTED ERROR: this function should not be called!\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::dispatchDeactivation - UNEXPECTED ERROR: this function should not be called!\n`
- `%lldus AppleThunderboltDPOutAdapterCM<%p>[%u:0x%llx:0x%x]::enqueueVerifiedHPDState - begin, hpd = %d, fHPDState = %d\n`

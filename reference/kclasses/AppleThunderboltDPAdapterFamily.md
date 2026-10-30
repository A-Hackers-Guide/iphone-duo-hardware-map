# `AppleThunderboltDPAdapterFamily`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltDPAdapterFamily`](../kexts/com.apple.driver.AppleThunderboltDPAdapterFamily.md)
- Object size: `0x198` (408 bytes)
- Metaclass: `0xfffffe000b9d1518`; metaclass vtable `0xfffffe0008278008`; class vtable `0xfffffe0008277818`
- Registration (init): `0xfffffe00098e2c34`
- Superclasses: [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleThunderboltDPInAdapter`](AppleThunderboltDPInAdapter.md) — `com.apple.driver.AppleThunderboltDPInAdapter`
- [`AppleThunderboltDPOutAdapter`](AppleThunderboltDPOutAdapter.md) — `com.apple.driver.AppleThunderboltDPOutAdapter`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::registerWithDPConnectionManager\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::dispatchNotifyDPConnectionManagerNeedEvaluation - dispatchAsync( notifyDPConnectionManagerNeedEvaluation )\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getLocalDPCapabilities - data = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::unregisterFromDPConnectionManager\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - DP_REMOTE_CAP = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setRemoteDPCapabilities - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getLocalDPCapabilities - data = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - DP_LOCAL_CAP = 0x%08x, overwriting with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::enableDP - ERROR: enableDP failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setDPState - commandWakeup( &fDPState )\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::unregisterFromDPConnectionManager - ERROR: DP connection manager not found!\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::enableDP - disable video and aux\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::configHopIDs - configure video link\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getDPAdapterCapOffset - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::reserveDPPortInternal - ERROR: caller cannot release a reservation it does not hold\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::isAdapterAvailableForClient - client = %p, fReservedClient = %p, available = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - DP_LOCAL_CAP = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getMaxSupportedLinkRate - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::notifyDPConnectionManagerNeedEvaluation - ERROR: DP connection manager not found!\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<<<static>>>::calculateDPBandwidthFromLinkRateAndLaneCount - link_rate = %u, lane_count = %u, number_of_lanes = %u, bandwidth = %u\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::findOrCreateDPConnectionManager\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::dispatchRemoveNotifiers - ERROR: dispatchAsync( checkIfAllAdaptersFound ) failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::registerWithDPConnectionManager - ERROR: DP connection manager not found!\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::start - rid = 0x%x, route = 0x%llx, port = 0x%02x, fChipType = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::setRemoteDPCapabilities - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::finalize - commandSleep( fWaitingForNotifiers )\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::readDPCapabilitiesRegister - remote = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::finalize - fWaitingForNotifiers woke up\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::writeDPCapabilitiesRegister - remote = %d\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::setDPState - commandWakeup( &fDPState )\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getTMUCapOffset - fTMUCapOffset = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::earlyWake\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::reserveDPPortInternal - clearing fReservedClient\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::enableDP - enable = %d\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::enableDP - set adapter reset bit (0x%x)\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::readDPCapabilitiesRegister - DP_LOCAL_CAP = 0x%08x, overwriting with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::readDPCapabilitiesRegister - DP_LOCAL_CAP = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::determineMaxSupportedLinkRate - fMaxSupportedLinkRate = %d\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::reserveDPPortInternal - clearing fReservedClient\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getDFTCapOffset - ERROR: finding fDFTCapOffset failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::enableDP - enable video and aux\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::cleanup\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::needsEarlyWake\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - ERROR: failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::configHopIDs - configure aux link\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getDPAdapterCapOffset - fDPAdapterCapOffset = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::cleanup\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::isAdapterAvailableForClient - WARNING: fStarted = false\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getDFTCapOffset - fDFTCapOffset = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::start\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::setDPState - changing state from %d to %d\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::isAdapterAvailableForClient - client = %p, fReservedClient = %p, available = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::configHopIDs - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::getLocalDPCapabilities - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setDPState - changing state from %d to %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::postEnableDPHook - enable = %d\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::reserveDPPortInternal - ERROR: acquireDPAdapterSynchronous failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::setup\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::createResources\n`
- `%lldus AppleThunderboltDPAdapterFamily<%p>::configHopIDs - deconfigure aux link\n`

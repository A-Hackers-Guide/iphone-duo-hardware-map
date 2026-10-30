# `AppleThunderboltDPAdapterFamilyBase`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltDPAdapterFamily`](../kexts/com.apple.driver.AppleThunderboltDPAdapterFamily.md)
- Object size: `0x190` (400 bytes)
- Metaclass: `0xfffffe000b9d1540`; metaclass vtable `0xfffffe00082789d0`; class vtable `0xfffffe00082780a0`
- Registration (init): `0xfffffe00098ea344`
- Superclasses: [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 8 in total)

- [`AppleThunderboltDPInAdapterBase`](AppleThunderboltDPInAdapterBase.md) — `com.apple.driver.AppleThunderboltDPInAdapter`
- [`AppleThunderboltDPOutAdapterBase`](AppleThunderboltDPOutAdapterBase.md) — `com.apple.driver.AppleThunderboltDPOutAdapter`

## Strings in its kext that name it (60)

- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::registerWithDPConnectionManager\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::dispatchNotifyDPConnectionManagerNeedEvaluation - dispatchAsync( notifyDPConnectionManagerNeedEvaluation )\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getLocalDPCapabilities - data = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::unregisterFromDPConnectionManager\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - DP_REMOTE_CAP = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setRemoteDPCapabilities - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - DP_LOCAL_CAP = 0x%08x, overwriting with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::enableDP - ERROR: enableDP failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setDPState - commandWakeup( &fDPState )\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::unregisterFromDPConnectionManager - ERROR: DP connection manager not found!\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::configHopIDs - configure video link\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getDPAdapterCapOffset - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::reserveDPPortInternal - ERROR: caller cannot release a reservation it does not hold\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::isAdapterAvailableForClient - client = %p, fReservedClient = %p, available = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - DP_LOCAL_CAP = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::notifyDPConnectionManagerNeedEvaluation - ERROR: DP connection manager not found!\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<<<static>>>::calculateDPBandwidthFromLinkRateAndLaneCount - link_rate = %u, lane_count = %u, number_of_lanes = %u, bandwidth = %u\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::findOrCreateDPConnectionManager\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::registerWithDPConnectionManager - ERROR: DP connection manager not found!\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::start - rid = 0x%x, route = 0x%llx, port = 0x%02x, fChipType = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::finalize - commandSleep( fWaitingForNotifiers )\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::finalize - fWaitingForNotifiers woke up\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::writeDPCapabilitiesRegister - remote = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::earlyWake\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::reserveDPPortInternal - clearing fReservedClient\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::enableDP - enable = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::enableDP - enable video and aux\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::needsEarlyWake\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - ERROR: failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::configHopIDs - configure aux link\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getDPAdapterCapOffset - fDPAdapterCapOffset = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::cleanup\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::isAdapterAvailableForClient - WARNING: fStarted = false\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::start\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::configHopIDs - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setDPState - changing state from %d to %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::postEnableDPHook - enable = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::free\n`
- `site.AppleThunderboltDPAdapterFamilyBase`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - route = 0x%llx, tunnel flags = 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::postEnableDPHook - clear adapter reset bit (0x%x)\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::reserveDPPortInternal - WARNING: this port is already reserved\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::findOrCreateDPConnectionManager - ERROR: failed to attach the DP Connection Manager to the controller!\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::configHopIDs - enable = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::dispatchNotifyDPConnectionManagerNeedEvaluation - ERROR: dispatchAsync( notifyDPConnectionManagerNeedEvaluation ) failed with 0x%08x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getTMUCapOffset - fTMUCapOffset = 0x%x\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::removeNotifiers - commandWakeup( fWaitingForNotifiers )\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<<<static>>>::calculateDPBandwidthFromDPCapability - dp_capability = 0x%08x, link_rate = %d, lane_count = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::createResources - fDPConnectionManager = %p\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setRemoteDPCapabilities - no extended caps\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::getLocalDPCapabilities - no extended caps\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::dispatchRemoveNotifiers - dispatchAsync( removeNotifiers )\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::findOrCreateDPConnectionManager - allocated the DP Connection Manager!\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::setDPState - current = %d, new = %d --> change = %d\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::notifyDPConnectionManagerNeedEvaluation\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::createResources\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::postEnableDPHook - set adapter reset bit (0x%x)\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::writeDPCapabilitiesRegister - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::reserveDPPortInternal - WARNING: this port is already unreserved\n`
- `%lldus AppleThunderboltDPAdapterFamilyBase<%p>::readDPCapabilitiesRegister - WARNING: fTerminated = true\n`

# `AppleThunderboltDPInAdapter`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltDPInAdapter`](../kexts/com.apple.driver.AppleThunderboltDPInAdapter.md)
- Object size: `0x1d0` (464 bytes)
- Metaclass: `0xfffffe000b9d16b8`; metaclass vtable `0xfffffe000827a150`; class vtable `0xfffffe0008279920`
- Registration (init): `0xfffffe0009917ce4`
- Superclasses: [`AppleThunderboltDPAdapterFamily`](AppleThunderboltDPAdapterFamily.md) → [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleThunderboltDPInAdapter` in [`com.apple.driver.AppleThunderboltDPInAdapter`](../kexts/com.apple.driver.AppleThunderboltDPInAdapter.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `9`

## Strings in its kext that name it (60)

- `site.AppleThunderboltDPInAdapter`
- `%lldus AppleThunderboltDPInAdapter<%p>::start - ERROR: DP crossbar not found\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::setGPUIsMuxedAway - gpuIsMuxedAway = %d, fGPUIsMuxedAway = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::getDPAdapterCapOffset - WARNING: fTerminated = true\n`
- `AppleThunderboltDPInAdapterCM`
- `%lldus AppleThunderboltDPInAdapter<%p>::earlyWakeThread\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::earlyWakeThread - value = 0x%08x lc_hpd = true\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::lateSleep\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::reserveDPPortInternal - messageClients( kIOThunderboltMessageDPStateChange )\n`
- `AppleThunderboltDPInAdapterCM<%p>(%x:%llx:%x)::setupNotifiers - ERROR: couldn't register with the DP connection manager! status = 0x%08x\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::setTunnelProhibited - tunnelProhibited = %d, fTunnelProhibited = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::setTunnelProhibited - messageClients( kIOThunderboltMessageDPStateChange )\n`
- `AppleThunderboltDPInAdapterOS`
- `%lldus AppleThunderboltDPInAdapter<%p>::agcCallback - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::enableDP - WARNING: enableDP failed with 0x%08x (hardware removed?)\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::reserveDPPortInternal - reserve = %d, client = %p, fReservedClient = %p\n`
- `site.AppleThunderboltDPInAdapterOS`
- `AppleThunderboltDPInAdapter`
- `%lldus AppleThunderboltDPInAdapter<%p>::earlyWake\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::getGPUIsMuxedAway - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::getGPUIsMuxedAway - gpu_muxed_away = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::isAdapterAvailableForClient - client = %p\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::reserveDPPortInternal - messageClients( kIOThunderboltMessageDPStateChange )\n`
- `AppleThunderboltDPInAdapterBase<%p>::clearHPD - ERROR: failed to set DPI HPD Output Clear bit! status = 0x%08x\n`
- `%lldus AppleThunderboltDPInAdapterOS<%p>::probe - service = %p\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::start - fSinkNumber = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::earlyWake - inDPPMode = 1, spawning early wake thread\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::reserveDPPortInternal - reserve = %d, client = %p, fReservedClient = %p\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::enableDP - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapterCM<%p>::probe - service = %p\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::finalize\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::lateSleep - lc[%d]: data = 0x%08x, dpp_in_use = %d\n`
- `AppleThunderboltDPInAdapterBase`
- `%lldus AppleThunderboltDPInAdapter<%p>::enableDP - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::start - ERROR: fSinkNumber not found\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::earlyWakeThread - status = 0x%08x, lc_hpd = %d, dpi_hpd_unsuppressed = %d, took %d ms (%d ms propagation + %d ms suppression)\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::agcCallback - invoking fAGCThreadCall\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::enableDP - DPI HPD propagation workaround\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::probe - service = %p\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::clearHPD - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::setGPUIsMuxedAway - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapterOS2<%p>::probe - service = %p\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::isAdapterAvailableForClient - available = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::start\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::needsEarlyWake - needs_early_wake = %d\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::enableDP - enable = %d\n`
- `AppleThunderboltDPInAdapterBase<%p>::clearHPD - ERROR: failed to clear DPI HPD Output Clear bit! status = 0x%08x\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::agcThreadCall - messaging AGC: tunneled_dp_in_use = %p\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::isAdapterAvailableForClient - fArbitrateSNKUseWithLC = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::controlPathListenerCallback - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::start - fStarted = true, calling registerService\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::isAdapterAvailableForClient - dpp_in_use = %d\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::reserveDPPortInternal - WARNING: fTerminated = true, not invoking fAGCThreadCall\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::free\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::controlPathListenerCallback - WARNING: fTerminated = true\n`
- `site.AppleThunderboltDPInAdapterCM`
- `%lldus AppleThunderboltDPInAdapterOS<%p>[%u:0x%llx:0x%x]::processDPBandwidthNotification\n`
- `%lldus AppleThunderboltDPInAdapterOS<%p>[%u:0x%llx:0x%x]::processDPBandwidthNotification - status = %08x\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::earlyWakeThread - route = 0x%08llx, port = 0x%x, value = 0x%08x, dpi_hpd_unsuppressed = true\n`
- `%lldus AppleThunderboltDPInAdapter<%p>::agcCallback - ERROR: fIOGraphicsControl = %p, newService = %p\n`

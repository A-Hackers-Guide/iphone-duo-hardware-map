# `AppleThunderboltDPInAdapterBase`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltDPInAdapter`](../kexts/com.apple.driver.AppleThunderboltDPInAdapter.md)
- Object size: `0x198` (408 bytes)
- Metaclass: `0xfffffe000b9d16e0`; metaclass vtable `0xfffffe000827ab30`; class vtable `0xfffffe000827a1e8`
- Registration (init): `0xfffffe000991959c`
- Superclasses: [`AppleThunderboltDPAdapterFamilyBase`](AppleThunderboltDPAdapterFamilyBase.md) → [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 3 in total)

- [`AppleThunderboltDPInAdapterCM`](AppleThunderboltDPInAdapterCM.md) — `com.apple.driver.AppleThunderboltDPInAdapter`

## IOKit personalities that instantiate it (1)

- `AppleThunderboltDPInAdapterBase` in [`com.apple.driver.AppleThunderboltDPInAdapter`](../kexts/com.apple.driver.AppleThunderboltDPInAdapter.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `10`

## Strings in its kext that name it (21)

- `%lldus AppleThunderboltDPInAdapterBase<%p>::lateSleep\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::reserveDPPortInternal - messageClients( kIOThunderboltMessageDPStateChange )\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::reserveDPPortInternal - reserve = %d, client = %p, fReservedClient = %p\n`
- `AppleThunderboltDPInAdapterBase<%p>::clearHPD - ERROR: failed to set DPI HPD Output Clear bit! status = 0x%08x\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::enableDP - WARNING: fTerminated = true\n`
- `AppleThunderboltDPInAdapterBase`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::probe - service = %p\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::clearHPD - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::enableDP - enable = %d\n`
- `AppleThunderboltDPInAdapterBase<%p>::clearHPD - ERROR: failed to clear DPI HPD Output Clear bit! status = 0x%08x\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::free\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::controlPathListenerCallback - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::getDPInVSECOffset - ERROR: finding fDPInVSECOffset failed with 0x%08x\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::finalize\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::earlyWake\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::getDPInVSECOffset - fDPInVSECOffset = 0x%x\n`
- `site.AppleThunderboltDPInAdapterBase`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::needsEarlyWake - needs_early_wake = %d\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::start - fStarted = true, calling registerService\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::start - ERROR: failed to startup\n`
- `%lldus AppleThunderboltDPInAdapterBase<%p>::start\n`

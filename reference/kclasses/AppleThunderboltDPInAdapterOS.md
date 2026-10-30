# `AppleThunderboltDPInAdapterOS`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltDPInAdapter`](../kexts/com.apple.driver.AppleThunderboltDPInAdapter.md)
- Object size: `0x1a0` (416 bytes)
- Metaclass: `0xfffffe000b9d1730`; metaclass vtable `0xfffffe000827bef0`; class vtable `0xfffffe000827b5a8`
- Registration (init): `0xfffffe000991a760`
- Superclasses: [`AppleThunderboltDPInAdapterCM`](AppleThunderboltDPInAdapterCM.md) → [`AppleThunderboltDPInAdapterBase`](AppleThunderboltDPInAdapterBase.md) → [`AppleThunderboltDPAdapterFamilyBase`](AppleThunderboltDPAdapterFamilyBase.md) → [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleThunderboltDPInAdapterOS2`](AppleThunderboltDPInAdapterOS2.md) — `com.apple.driver.AppleThunderboltDPInAdapter`

## IOKit personalities that instantiate it (1)

- `AppleThunderboltDPInAdapterOS` in [`com.apple.driver.AppleThunderboltDPInAdapter`](../kexts/com.apple.driver.AppleThunderboltDPInAdapter.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `11`

## Strings in its kext that name it (9)

- `AppleThunderboltDPInAdapterOS`
- `site.AppleThunderboltDPInAdapterOS`
- `%lldus AppleThunderboltDPInAdapterOS<%p>::probe - service = %p\n`
- `%lldus AppleThunderboltDPInAdapterOS2<%p>::probe - service = %p\n`
- `%lldus AppleThunderboltDPInAdapterOS<%p>[%u:0x%llx:0x%x]::processDPBandwidthNotification\n`
- `%lldus AppleThunderboltDPInAdapterOS<%p>[%u:0x%llx:0x%x]::processDPBandwidthNotification - status = %08x\n`
- `AppleThunderboltDPInAdapterOS2`
- `site.AppleThunderboltDPInAdapterOS2`
- `%lldus AppleThunderboltDPInAdapterOS<%p>[%u:0x%llx:0x%x]::processDPBandwidthNotification - notifying dp adapter at [%u:0x%llx:0x%x] about DP BW request\n`

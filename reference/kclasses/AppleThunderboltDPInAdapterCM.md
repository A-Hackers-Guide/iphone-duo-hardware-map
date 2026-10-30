# `AppleThunderboltDPInAdapterCM`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleThunderboltDPInAdapter`](../kexts/com.apple.driver.AppleThunderboltDPInAdapter.md)
- Object size: `0x198` (408 bytes)
- Metaclass: `0xfffffe000b9d1708`; metaclass vtable `0xfffffe000827b510`; class vtable `0xfffffe000827abc8`
- Registration (init): `0xfffffe0009919e4c`
- Superclasses: [`AppleThunderboltDPInAdapterBase`](AppleThunderboltDPInAdapterBase.md) → [`AppleThunderboltDPAdapterFamilyBase`](AppleThunderboltDPAdapterFamilyBase.md) → [`IOThunderboltTunnelDriver`](IOThunderboltTunnelDriver.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 2 in total)

- [`AppleThunderboltDPInAdapterOS`](AppleThunderboltDPInAdapterOS.md) — `com.apple.driver.AppleThunderboltDPInAdapter`

## IOKit personalities that instantiate it (1)

- `AppleThunderboltDPInAdapterCM` in [`com.apple.driver.AppleThunderboltDPInAdapter`](../kexts/com.apple.driver.AppleThunderboltDPInAdapter.md): `IOProviderClass` = `IOThunderboltPort`, `IOProbeScore` = `11`

## Strings in its kext that name it (6)

- `AppleThunderboltDPInAdapterCM`
- `AppleThunderboltDPInAdapterCM<%p>(%x:%llx:%x)::setupNotifiers - ERROR: couldn't register with the DP connection manager! status = 0x%08x\n`
- `%lldus AppleThunderboltDPInAdapterCM<%p>::probe - service = %p\n`
- `site.AppleThunderboltDPInAdapterCM`
- `%lldus AppleThunderboltDPInAdapterCM<%p>(%x:%llx:%x)::controlPathListenerCallback - WARNING: fTerminated = true\n`
- `%lldus AppleThunderboltDPInAdapterCM<%p>(%x:%llx:%x)::setupNotifiers\n`

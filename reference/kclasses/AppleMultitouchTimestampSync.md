# `AppleMultitouchTimestampSync`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleMultitouchDriver`](../kexts/com.apple.driver.AppleMultitouchDriver.md)
- Object size: `0xd8` (216 bytes)
- Metaclass: `0xfffffe000b986530`; metaclass vtable `0xfffffe000817fd90`; class vtable `0xfffffe000817f818`
- Registration (init): `0xfffffe00092d2150`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleMultitouchTimestampSync` in [`com.apple.driver.AppleMultitouchDriver`](../kexts/com.apple.driver.AppleMultitouchDriver.md): `IOProviderClass` = `IOService`, `IONameMatch` = `['timestamp-sync']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/mt-bt-timestamp-sync`](../devicetree/root__arm-io__mt-bt-timestamp-sync.md) on `timestamp-sync`

## Strings in its kext that name it (6)

- `AppleMultitouchTimestampSyncLock`
- `AppleMultitouchTimestampSync`
- `site.AppleMultitouchTimestampSync`
- `site.AppleMultitouchTimestampSyncUC`
- `AppleMultitouchTimestampSyncUC`
- `site.AppleMultitouchTimestampSyncLock`

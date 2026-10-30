# `AppleSMCSensorDispatcher`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md)
- Object size: `0x288` (648 bytes)
- Metaclass: `0xfffffe000b99b618`; metaclass vtable `0xfffffe0008202718`; class vtable `0xfffffe00082021b8`
- Registration (init): `0xfffffe0009685eac`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSMCSensorDispatcher` in [`com.apple.driver.AppleSMC`](../kexts/com.apple.driver.AppleSMC.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['smc-tempsensor']`, `IOResourceMatch` = `IOKit`, `IOProbeScore` = `100`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/smctempsensor0`](../devicetree/root__arm-io__smctempsensor0.md) on `smc-tempsensor`

## Strings in its kext that name it (16)

- `AppleSMCSensorDispatcherUserClient::sGetMagnetKey: Error instance\n`
- `AppleSMCSensorDispatcher::%s: Found %u sensors from the device tree\n`
- `AppleSMCSensorDispatcher::%s: %d\n\n`
- `AppleSMCSensorDispatcher::%s: Found %u GPU sensor offsets from the device tree\n`
- `AppleSMCSensorDispatcher::getNfcStateKey: %d\n`
- `AppleSMCSensorDispatcher`
- `AppleSMCSensorDispatcher::%s: Start success\n\n`
- `site.AppleSMCSensorDispatcherUserClient`
- `AppleSMCSensorDispatcher::getPowerPauseKey: %d\n`
- `site.AppleSMCSensorDispatcher`
- `AppleSMCSensorDispatcher::%s: Could not find any sensors\n`
- `AppleSMCSensorDispatcher::%s: AppleSMCSensorDispatcher: too many sensors in the device tree\n`
- `AppleSMCSensorDispatcherUserClient::sGetPowerPauseKey: Error instance\n`
- `AppleSMCSensorDispatcherUserClient`
- `AppleSMCSensorDispatcherUserClient::sGetNfcStateKey: Error instance\n`
- `AppleSMCSensorDispatcher provider is not AppleARMIODevice`

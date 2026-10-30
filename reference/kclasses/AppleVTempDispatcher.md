# `AppleVTempDispatcher`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md)
- Object size: `0xa8` (168 bytes)
- Metaclass: `0xfffffe000b943df8`; metaclass vtable `0xfffffe000808c7b0`; class vtable `0xfffffe000808c258`
- Registration (init): `0xfffffe0008c7e75c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleVTempDispatcher` in [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['vtempctl,t8010', 'vtempctl,s8003', 'vtempctl,s8001', 'vtempctl,s8000', 'vtempc`, `IOResourceMatch` = `IOKit`, `IOProbeScore` = `100`

## Strings in its kext that name it (7)

- `AppleVTempDispatcher::%s: Empty setProperty\n`
- `site.AppleVTempDispatcher`
- `AppleVTempDispatcher::%s: Error could not find sensor %s in dictionary\n`
- `AppleVTempDispatcher`
- `AppleVTempDispatcher::%s: Could not add command gate to workloop\n`
- `AppleVTempDispatcher::%s: Could not init dict\n`
- `AppleVTempDispatcher::%s: AppleVTempDispatcher provider is not AppleARMIODevice\n`

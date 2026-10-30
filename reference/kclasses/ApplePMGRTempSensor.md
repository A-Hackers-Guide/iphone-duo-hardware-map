# `ApplePMGRTempSensor`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md)
- Object size: `0x138` (312 bytes)
- Metaclass: `0xfffffe000b943ee8`; metaclass vtable `0xfffffe000808f2a0`; class vtable `0xfffffe000808ed18`
- Registration (init): `0xfffffe0008c82510`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 3 in total)

- [`AppleT700XTempSensor`](AppleT700XTempSensor.md) — `com.apple.driver.AppleEmbeddedTempSensor`

## IOKit personalities that instantiate it (1)

- `ApplePMGRTempSensor` in [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `tempsensor,s5l8945x`, `IOResourceMatch` = `IOKit`, `IOProbeScore` = `100`

## Strings in its kext that name it (6)

- `ApplePMGRTempSensor::start: checking for expect-dietmpctl\n`
- `site.ApplePMGRTempSensor`
- `ApplePMGRTempSensor`
- `ApplePMGRTempSensor::start: past _fDieTempController init code with _fDieTempController %p\n`
- `ApplePMGRTempSensor provider is not AppleARMIODevice\n`
- `ApplePMGRTempSensor::start: useFastDieTempController %d\n`

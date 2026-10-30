# `AppleT700XTempSensor`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md)
- Object size: `0x198` (408 bytes)
- Metaclass: `0xfffffe000b943da8`; metaclass vtable `0xfffffe000808c088`; class vtable `0xfffffe000808bac8`
- Registration (init): `0xfffffe0008c7de78`
- Superclasses: [`ApplePMGRTempSensor`](ApplePMGRTempSensor.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 2 in total)

- [`AppleT8015TempSensor`](AppleT8015TempSensor.md) — `com.apple.driver.AppleEmbeddedTempSensor`

## IOKit personalities that instantiate it (1)

- `AppleT700XTempSensor` in [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['tempsensor,t7000', 'tempsensor,t7001', 'tempsensor,s8000', 'tempsensor,t8010',`, `IOResourceMatch` = `IOKit`, `IOProbeScore` = `100`

## Strings in its kext that name it (6)

- `AppleT700XTempSensorUserClient`
- `site.AppleT700XTempSensorDisableSensorFunction`
- `AppleT700XTempSensor`
- `site.AppleT700XTempSensorUserClient`
- `site.AppleT700XTempSensor`
- `AppleT700XTempSensorDisableSensorFunction`

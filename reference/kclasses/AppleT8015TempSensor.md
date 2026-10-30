# `AppleT8015TempSensor`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md)
- Object size: `0x1b8` (440 bytes)
- Metaclass: `0xfffffe000b943ec0`; metaclass vtable `0xfffffe000808ec80`; class vtable `0xfffffe000808e6c0`
- Registration (init): `0xfffffe0008c80748`
- Superclasses: [`AppleT700XTempSensor`](AppleT700XTempSensor.md) → [`ApplePMGRTempSensor`](ApplePMGRTempSensor.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleT8020MTRTempSensor`](AppleT8020MTRTempSensor.md) — `com.apple.driver.AppleEmbeddedTempSensor`

## IOKit personalities that instantiate it (1)

- `AppleT8015TempSensor` in [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['tempsensor,t8015', 'tempsensor,t8020', 'tempsensor,t8027', 'tempsensor,t8030']`, `IOResourceMatch` = `IOKit`, `IOProbeScore` = `100`

## Strings in its kext that name it (2)

- `site.AppleT8015TempSensor`
- `AppleT8015TempSensor`

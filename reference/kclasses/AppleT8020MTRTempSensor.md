# `AppleT8020MTRTempSensor`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md)
- Object size: `0x1d8` (472 bytes)
- Metaclass: `0xfffffe000b943d80`; metaclass vtable `0xfffffe000808ba30`; class vtable `0xfffffe000808b470`
- Registration (init): `0xfffffe0008c7c98c`
- Superclasses: [`AppleT8015TempSensor`](AppleT8015TempSensor.md) → [`AppleT700XTempSensor`](AppleT700XTempSensor.md) → [`ApplePMGRTempSensor`](ApplePMGRTempSensor.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleT8020MTRTempSensor` in [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['mtrtempsensor,t8020']`, `IOResourceMatch` = `IOKit`, `IOProbeScore` = `100`

## Strings in its kext that name it (2)

- `site.AppleT8020MTRTempSensor`
- `AppleT8020MTRTempSensor`

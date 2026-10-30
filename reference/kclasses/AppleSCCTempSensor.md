# `AppleSCCTempSensor`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md)
- Object size: `0x108` (264 bytes)
- Metaclass: `0xfffffe000b943fd8`; metaclass vtable `0xfffffe00080916b0`; class vtable `0xfffffe0008090f60`
- Registration (init): `0xfffffe0008c8b628`
- Superclasses: [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSCCTempSensor` in [`com.apple.driver.AppleEmbeddedTempSensor`](../kexts/com.apple.driver.AppleEmbeddedTempSensor.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `scctempsensor,s5l8950x`, `IOResourceMatch` = `IOKit`, `IOProbeScore` = `100`

## Strings in its kext that name it (4)

- `AppleSCCTempSensor`
- `AppleSCCTempSensor provider is not AppleARMIODevice\n`
- `site.AppleSCCTempSensor`
- `AppleSCCTempSensor: Missing Device Tree value\n`

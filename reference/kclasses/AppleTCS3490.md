# `AppleTCS3490`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleALSColorSensor`](../kexts/com.apple.driver.AppleALSColorSensor.md)
- Object size: `0x370` (880 bytes)
- Metaclass: `0xfffffe000b932620`; metaclass vtable `0xfffffe0007f9ccd8`; class vtable `0xfffffe0007f9c548`
- Registration (init): `0xfffffe000867f674`
- Superclasses: [`AppleALSColorSensor`](AppleALSColorSensor.md) → [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleTCS3490` in [`com.apple.driver.AppleALSColorSensor`](../kexts/com.apple.driver.AppleALSColorSensor.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `['als,tcs3490', 'als,ct709']`

## Strings in its kext that name it (4)

- `AppleTCS3490`
- `site.AppleTCS3490`
- `AppleTCS3490 - Probing hardware failed (%s) \n`
- `%d: AppleTCS3490::setPropertiesGated\n`

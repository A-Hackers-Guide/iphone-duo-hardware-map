# `AppleCT711`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleALSColorSensor`](../kexts/com.apple.driver.AppleALSColorSensor.md)
- Object size: `0x16b0` (5,808 bytes)
- Metaclass: `0xfffffe000b932698`; metaclass vtable `0xfffffe0007f9e750`; class vtable `0xfffffe0007f9dfc0`
- Registration (init): `0xfffffe0008683924`
- Superclasses: [`AppleALSColorSensor`](AppleALSColorSensor.md) → [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleCT711` in [`com.apple.driver.AppleALSColorSensor`](../kexts/com.apple.driver.AppleALSColorSensor.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `['als,ct711', 'als,tcs3490']`

## Strings in its kext that name it (5)

- `%d: AppleCT711::setPropertiesGated\n`
- `site.AppleCT711`
- `AppleCT711`
- `%d: AppleCT711::handleStart -- vers=%d.%d, size=%d, chksum=%d\n`
- `AppleCT711 - Probing hardware failed (%s) \n`

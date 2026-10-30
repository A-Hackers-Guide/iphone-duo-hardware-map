# `AppleISL29023`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md)
- Object size: `0x1a8` (424 bytes)
- Metaclass: `0xfffffe000b9433a0`; metaclass vtable `0xfffffe00080867d0`; class vtable `0xfffffe0008086020`
- Registration (init): `0xfffffe0008c41cd0`
- Superclasses: [`AppleEmbeddedI2CLightSensor`](AppleEmbeddedI2CLightSensor.md) → [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleISL29023` in [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `als,isl29023`

## Strings in its kext that name it (4)

- `AppleISL29023::handleStart -- Probing hardware failed (%s).\n`
- `AppleISL29023`
- `site.AppleISL29023`
- `AppleISL29023::_timerExpired -- couldn't read sensor data. Reason: %s\n`

# `AppleSPUCT709`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleALSColorSensor`](../kexts/com.apple.driver.AppleALSColorSensor.md)
- Object size: `0x3a8` (936 bytes)
- Metaclass: `0xfffffe000b932670`; metaclass vtable `0xfffffe0007f9df28`; class vtable `0xfffffe0007f9d6c8`
- Registration (init): `0xfffffe000868129c`
- Superclasses: [`AppleSPUALSColorDriver`](AppleSPUALSColorDriver.md) → [`AppleSPUHIDDriver`](AppleSPUHIDDriver.md) → [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPUCT709` in [`com.apple.driver.AppleALSColorSensor`](../kexts/com.apple.driver.AppleALSColorSensor.md): `IOProviderClass` = `IOHIDInterface`

## Strings in its kext that name it (3)

- `AppleSPUCT709::%s: Send calibration data (size = %d) to the AOP driver.\n`
- `site.AppleSPUCT709`
- `AppleSPUCT709`

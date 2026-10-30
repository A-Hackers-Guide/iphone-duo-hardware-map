# `AppleSPUCT724`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleALSColorSensor`](../kexts/com.apple.driver.AppleALSColorSensor.md)
- Object size: `0x3f0` (1,008 bytes)
- Metaclass: `0xfffffe000b9326c0`; metaclass vtable `0xfffffe0007f9f048`; class vtable `0xfffffe0007f9e7e8`
- Registration (init): `0xfffffe00086843ec`
- Superclasses: [`AppleSPUALSColorDriver`](AppleSPUALSColorDriver.md) → [`AppleSPUHIDDriver`](AppleSPUHIDDriver.md) → [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSPUCT724` in [`com.apple.driver.AppleALSColorSensor`](../kexts/com.apple.driver.AppleALSColorSensor.md): `IOProviderClass` = `IOHIDInterface`

## Strings in its kext that name it (6)

- `AppleSPUCT724`
- `AppleSPUCT724::handleStart`
- `AppleSPUCT724::%s: Send calibration data (size = %d) to the AOP driver.\n`
- `site.AppleSPUCT724`
- `AppleSPUCT724::probe`
- `AppleSPUCT724::loadCalibrationData`

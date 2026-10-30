# `AppleCT819`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md)
- Object size: `0x2d8` (728 bytes)
- Metaclass: `0xfffffe000b9433c8`; metaclass vtable `0xfffffe0008087018`; class vtable `0xfffffe0008086868`
- Registration (init): `0xfffffe0008c45868`
- Superclasses: [`AppleEmbeddedI2CLightSensor`](AppleEmbeddedI2CLightSensor.md) → [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleCT819` in [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `als,ct819`

## Strings in its kext that name it (25)

- `AppleCT819`
- `ALS: [AppleCT819] setPropertiesGated: newGain =%d\n`
- `AppleCT819::handleStart -- No LUX extrapolation curve information\n`
- `AppleCT819::probe - Probing hardware found (%d) \n`
- `AppleCT819::handleStart -- Too many curve segments.. \n`
- `AppleCT819::handleStart -- Insufficient ratioLimits.. \n`
- `AppleCT819::handleStart - gain for luxCurves reg= 0x%x\n`
- `ALS: [AppleCT819] setPropertiesGated: _alsRawMode=%d\n`
- `site.AppleCT819`
- `AppleCT819::handleStart -- Insufficient intercepts.. \n`
- `AppleCT819::Fudge factor = 0x%X\n`
- `AppleCT819::handleStart Could not find calibration data for placement: %d, orientation: %d\n`
- `AppleCT819::probe - ALS_INT is in proper state - result = %x (%s), and isINTasserted= %x \n`
- `AppleCT819::probe - ALS_INT is stuck low.. Disabling ALS. result = %x (%s), and isINTasserted= %x \n`
- `AppleCT819::handleStart\n`
- `AppleCT819::probe - Probing hardware failed (%s) \n`
- `AppleCT819::handleStart - Need at least header size bytes. Actual: %d, Expected: %ld\n`
- `ALS: [AppleCT819] setPropertiesGated: enableTestMode=%d\n`
- `AppleCT819::handleStart -- vers=%d.%d, size=%d, chksum=%d\n`
- `ALS: [AppleCT819] setPropertiesGated: _alsContinuousMode=%d\n`
- `ALS: [AppleCT819] _setALSReportingInterval: Requested: interval=%d mics, Setting: interval=%d mics\n`
- `AppleCT819::handleStart -- Clipping integration cycles (%d) to max allowed (%d).. \n`
- `AppleCT819::Overriding bad fudge factor 0x%X with 1.0 (0xFF)\n`
- `AppleCT819::handleStart - integCycles = %d\n`
- `AppleCT819::_calculateAmbient -- unknown _gainUsedForLuxCurves\n`

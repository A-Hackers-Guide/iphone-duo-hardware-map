# `AppleTSL2581`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md)
- Object size: `0x2e8` (744 bytes)
- Metaclass: `0xfffffe000b943350`; metaclass vtable `0xfffffe0008085740`; class vtable `0xfffffe0008084f90`
- Registration (init): `0xfffffe0008c3c680`
- Superclasses: [`AppleEmbeddedI2CLightSensor`](AppleEmbeddedI2CLightSensor.md) → [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleTSL2581` in [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `als,tsl2581`

## Strings in its kext that name it (26)

- `AppleTSL2581::handleStart - _blLeakageCh0 = %ld\n`
- `AppleTSL2581::handleStart -- vers=%d.%d, size=%d, chksum=%d\n`
- `AppleTSL2581::probe - Probing hardware failed (%s) \n`
- `AppleTSL2581::probe - Probing hardware found (%d) \n`
- `AppleTSL2581`
- `AppleTSL2581::probe - ALS_INT is in proper state - result = %x (%s), and isINTasserted= %x \n`
- `AppleTSL2581::handleStart - Too Many custom curve segments. Actual: %d, Expected: %d\n`
- `AppleTSL2581::handleStart - Using a single equation for ALS Lux translation\n`
- `AppleTSL2581::handleStart -- Too many curve segments.. \n`
- `ALS: [AppleTSL2581] _setALSReportingInterval: Requested: interval=%ld mics, Setting: interval=%ld mics\n`
- `AppleTSL2581::_calculateAmbient -- unknown _gainUsedForLuxCurves\n`
- `AppleTSL2581::handleStart -- Insufficient ratioLimits.. \n`
- `AppleTSL2581::handleStart -- Insufficient intercepts.. \n`
- `AppleTSL2581::handleStart wrong chksum for the ALS calibration data\n`
- `AppleTSL2581::handleStart - integCycles = %ld\n`
- `ALS: [AppleTSL2581] setPropertiesGated: _alsRawMode=%ld\n`
- `ALS: [AppleTSL2581] setPropertiesGated: newGain =%ld\n`
- `AppleTSL2581::handleStart - gain for luxCurves reg= 0x%lx\n`
- `AppleTSL2581::probe - ALS_INT is stuck low.. Disabling ALS. result = %x (%s), and isINTasserted= %x \n`
- `ALS: [AppleTSL2581] setPropertiesGated: _alsContinuousMode=%d\n`
- `site.AppleTSL2581`
- `ALS: [AppleTSL2581] setPropertiesGated: enableTestMode=%ld\n`
- `AppleTSL2581::handleStart - _blLeakageCh1 = %ld\n`
- `AppleTSL2581::handleStart -- No LUX extrapolation curve information\n`
- `AppleTSL2581::handleStart -- Clipping integration cycles (%ld) to max allowed (%d).. \n`
- `AppleTSL2581::handleStart - Too little calibration data. Actual: %d, Expected: %ld\n`

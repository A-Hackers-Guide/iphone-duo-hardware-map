# `AppleCT821`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md)
- Object size: `0x348` (840 bytes)
- Metaclass: `0xfffffe000b943378`; metaclass vtable `0xfffffe0008085f88`; class vtable `0xfffffe00080857d8`
- Registration (init): `0xfffffe0008c410e8`
- Superclasses: [`AppleEmbeddedI2CLightSensor`](AppleEmbeddedI2CLightSensor.md) → [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleCT821` in [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `als,ct821`

## Strings in its kext that name it (33)

- `ALS: [AppleCT821] setPropertiesGated: newGain =%d\n`
- `AppleCT821::handleStart -- Insufficient ratioLimits.. \n`
- `AppleCT821::handleStart -- vers=%d.%d, size=%d, chksum=%d\n`
- `ALS: [AppleCT821] %s: _blLeakageNits updated to: %d / 1000 | %d / 1000 | %d / 1000 \n`
- `site.AppleCT821`
- `AppleCT821::handleStart - gain for luxCurves reg= 0x%x\n`
- `AppleCT821::handleStart - Need at least header size bytes. Actual: %d, Expected: %ld\n`
- `AppleCT821::handleStart\n`
- `AppleCT821`
- `AppleCT821::handleStart -- Insufficient intercepts.. \n`
- `AppleCT821::handleStart -- Too many curve segments.. \n`
- `AppleCT821::handleStart -- Clipping integration cycles (%d) to max allowed (%d).. \n`
- `ALS: [AppleCT821] setPropertiesGated: ch0 override set to %d \n`
- `ALS: [AppleCT821] setPropertiesGated: channel override turned %s \n`
- `ALS: [AppleCT821] setPropertiesGated: _alsRawMode=%d\n`
- `ALS: [AppleCT821] _setALSReportingInterval: Requested: interval=%d mics, Setting: interval=%d mics\n`
- `ALS: [AppleCT821] setPropertiesGated: _alsContinuousMode=%d\n`
- `AppleCT821::probe - Probing hardware found (%d) \n`
- `ALS: [AppleCT821] setPropertiesGated: dynamic gain support turned %s \n`
- `AppleCT821::handleStart - integCycles = %d\n`
- `ALS: [AppleCT821] setPropertiesGated: low threshold cap set to %d percent \n`
- `AppleCT821::probe - ALS_INT is stuck low.. Disabling ALS. result = %x (%s), and isINTasserted= %x \n`
- `AppleCT821::_calculateAmbient -- unknown _gainUsedForLuxCurves\n`
- `ALS: [AppleCT821] setPropertiesGated: gain override to %d \n`
- `AppleCT821::handleStart -- No LUX extrapolation curve information\n`
- `AppleCT821::probe - Probing hardware failed (%s) \n`
- `AppleCT821::readSensorData: gain=%d orientation=%d data0=%u (%u) data1=%u (%u) lux=%u interval=%lld\n`
- `AppleCT821::%s gain changed to %d | low threshold(gap): %d(%d%%) | hight threshold(gap): %d(%d%%) \n`
- `ALS: [AppleCT821] setPropertiesGated: high threshold cap set to %d percent \n`
- `AppleCT821::handleStart Could not find calibration data for placement: %d, orientation: %d\n`
- `ALS: [AppleCT821] setPropertiesGated: enableTestMode=%d\n`
- `AppleCT821::probe - ALS_INT is in proper state - result = %x (%s), and isINTasserted= %x \n`
- `AppleCT821::_timerExpired -- couldn't read sensor data. Reason: %s\n`

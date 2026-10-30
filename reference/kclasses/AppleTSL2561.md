# `AppleTSL2561`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md)
- Object size: `0x210` (528 bytes)
- Metaclass: `0xfffffe000b943328`; metaclass vtable `0xfffffe0008084ef8`; class vtable `0xfffffe0008084748`
- Registration (init): `0xfffffe0008c390dc`
- Superclasses: [`AppleEmbeddedI2CLightSensor`](AppleEmbeddedI2CLightSensor.md) → [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleTSL2561` in [`com.apple.driver.AppleEmbeddedLightSensor`](../kexts/com.apple.driver.AppleEmbeddedLightSensor.md): `IOProviderClass` = `AppleARMIICDevice`, `IONameMatch` = `als,tsl2561`

## Strings in its kext that name it (12)

- `AppleTSL2561::handleStart -- No LUX extrapolation curve information\n`
- `ALS: [AppleTSL2561] setPropertiesGated: requested ReportInterval=0 turn OFF sensor\n`
- `AppleTSL2561::handleStart -- Too many curve segments.. \n`
- `ALS: [AppleTSL2561] setPropertiesGated: Requested: interval=%ld mics, Setting: interval=%ld mics\n`
- `AppleTSL2561::handleStart -- Insufficient intercepts.. \n`
- `site.AppleTSL2561`
- `AppleTSL2561::setSensorEnabled *** FAILED ***: _writeReg8 kTSL256xControl=%x result=%s\n`
- `AppleTSL2561`
- `AppleTSL2561::handleStart -- Insufficient ratioLimits.. \n`
- `AppleTSL2561::handleStart - Probing hardware failed (%s) \n`
- `AppleTSL2561::handleStart - ALS_INT is stuck low.. Disabling ALS. result = %x (%s), and isINTasserted= %x \n`
- `ALS: [AppleTSL2561] setPropertiesGated: enableTestMode=%ld\n`

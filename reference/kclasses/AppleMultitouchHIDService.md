# `AppleMultitouchHIDService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleMultitouchDriver`](../kexts/com.apple.driver.AppleMultitouchDriver.md)
- Object size: `0xd8` (216 bytes)
- Metaclass: `0xfffffe000b986670`; metaclass vtable `0xfffffe00081821e0`; class vtable `0xfffffe0008181c28`
- Registration (init): `0xfffffe00092dc9bc`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (5)

- `AppleMultitouchHIDService (0x0D,0x00)` in [`com.apple.driver.AppleMultitouchDriver`](../kexts/com.apple.driver.AppleMultitouchDriver.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1500`
- `AppleMultitouchHIDService (0x0D,0x04)` in [`com.apple.driver.AppleMultitouchDriver`](../kexts/com.apple.driver.AppleMultitouchDriver.md): `IOProviderClass` = `IOHIDInterface`
- `AppleMultitouchHIDService (0x0D,0x20)` in [`com.apple.driver.AppleMultitouchDriver`](../kexts/com.apple.driver.AppleMultitouchDriver.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1500`
- `MTUserDevice` in [`com.apple.driver.AppleMultitouchDriver`](../kexts/com.apple.driver.AppleMultitouchDriver.md): `IOProviderClass` = `IOHIDInterface`
- `Generic Touch - Apple USB` in [`com.apple.driver.AppleTopCaseHIDEventDriver`](../kexts/com.apple.driver.AppleTopCaseHIDEventDriver.md): `IOProviderClass` = `IOHIDInterface`

## Strings in its kext that name it (17)

- `AppleMultitouchHIDService::notifyClientsAction(%d)`
- `AppleMultitouchHIDService::simpleSetReport() for reportID 0x%02x, length %d`
- `AppleMultitouchHIDService::getMultitouchReportInfo() reportID 0x%02x`
- `AppleMultitouchHIDService::simpleGetReport() for reportID 0x%02x, length %d completed`
- `AppleMultitouchHIDService::getMultitouchReport() reportID 0x%02x, length %d`
- `AppleMultitouchHIDService`
- `[AppleMultitouchHIDService::handleInterruptReport reportID:%d (%d bytes)]`
- `AppleMultitouchHIDService::enableMultitouchEvents(%s)`
- `AppleMultitouchHIDService::simpleGetReport() for reportID 0x%02x, length %d`
- `site.AppleMultitouchHIDService`
- `AppleMultitouchHIDService::setMultitouchReport() reportID 0x%02x, length %d`
- `[AppleMultitouchHIDService] Start succeeded\n`
- `AppleMultitouchHIDService::updateNoiseAvoidanceGated failed to set noise avoidance state: 0x%08x`
- `AppleMultitouchHIDService::_systemPowerChangeHandler: Failed with error 0x%08x`
- `AppleMultitouchHIDService::updateNoiseAvoidanceGated ignoring unchanged noise avoidance state (existing state: %x)`
- `AppleMultitouchHIDService::noiseAvoidanceChangeNotification battery status changed`
- `AppleMultitouchHIDService::updateNoiseAvoidanceGated setting noise avoidance state: %x`

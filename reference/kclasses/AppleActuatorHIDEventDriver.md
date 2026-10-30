# `AppleActuatorHIDEventDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleActuatorDriver`](../kexts/com.apple.driver.AppleActuatorDriver.md)
- Object size: `0xd8` (216 bytes)
- Metaclass: `0xfffffe000b936c70`; metaclass vtable `0xfffffe0007feaf48`; class vtable `0xfffffe0007fea9b8`
- Registration (init): `0xfffffe000898a89c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (6)

- `Magic Trackpad BT iOS/tvOS Actuator Event Driver - TopCase - 613` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Trackpad BT iOS/tvOS Actuator Event Driver - TopCase - 804` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Trackpad USB iOS/tvOS Actuator Event Driver - TopCase - 613` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Trackpad USB iOS/tvOS Actuator Event Driver - TopCase - 804` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - ACT - TopCase - 1108` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - ACT - TopCase - 1109` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`

## Strings in its kext that name it (13)

- `AppleActuatorHIDEventDriver::getActuatorReport() reportID 0x%02x, length %d`
- `Error: AppleActuatorHIDEventDriver::simpleSetReport() returned 0x%08X for reportID 0x%02X`
- `AppleActuatorHIDEventDriver::willTerminate begin`
- `AppleActuatorHIDEventDriver::willTerminate end`
- `AppleActuatorHIDEventDriver::getActuatorReportInfo() reportID 0x%02x`
- `AppleActuatorHIDEventDriver::simpleSetReport() for reportID 0x%02x, length %d`
- `AppleActuatorHIDEventDriver - output reports disabled via boot-arg.\n`
- `AppleActuatorHIDEventDriver::enableActuatorEvents(%s)`
- `AppleActuatorHIDEventDriver`
- `AppleActuatorHIDEventDriver::simpleGetReport() for reportID 0x%02x, length %d`
- `AppleActuatorHIDEventDriver::setActuatorReport() reportID 0x%02x, length %d`
- `site.AppleActuatorHIDEventDriver`
- `AppleActuatorHIDEventDriver - couldn't kick off device builder!`

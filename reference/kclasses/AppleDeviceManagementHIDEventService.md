# `AppleDeviceManagementHIDEventService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleTopCaseHIDEventDriver`](../kexts/com.apple.driver.AppleTopCaseHIDEventDriver.md)
- Object size: `0x190` (400 bytes)
- Metaclass: `0xfffffe000b9d3510`; metaclass vtable `0xfffffe0008293b88`; class vtable `0xfffffe00082933e8`
- Registration (init): `0xfffffe0009a111ac`
- Superclasses: [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (30)

- `Magic Keyboard (BT) - AppleDeviceManagementHIDEventService` in [`com.apple.driver.AppleTopCaseHIDEventDriver`](../kexts/com.apple.driver.AppleTopCaseHIDEventDriver.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard (USB) - AppleDeviceManagementHIDEventService` in [`com.apple.driver.AppleTopCaseHIDEventDriver`](../kexts/com.apple.driver.AppleTopCaseHIDEventDriver.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard BT iOS/tvOS - DM - TopCase - 666` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard BT iOS/tvOS - DM - TopCase - 668` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard BT iOS/tvOS - DM - TopCase - 671` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard BT iOS/tvOS - DM - TopCase - 800` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard BT iOS/tvOS - DM - TopCase - 801` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard BT iOS/tvOS - DM - TopCase - 802` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard USB iOS/tvOS - DM - TopCase - 666` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard USB iOS/tvOS - DM - TopCase - 668` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard USB iOS/tvOS - DM - TopCase - 671` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard USB iOS/tvOS - DM - TopCase - 800` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard USB iOS/tvOS - DM - TopCase - 801` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard USB iOS/tvOS - DM - TopCase - 802` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Mouse BT iOS/tvOS - DM - TopCase - 617` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Mouse BT iOS/tvOS - DM - TopCase - 803` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Mouse USB iOS/tvOS - DM - TopCase - 617` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Mouse USB iOS/tvOS - DM - TopCase - 803` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Trackpad BT iOS/tvOS - DM - TopCase - 613` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Trackpad BT iOS/tvOS - DM - TopCase - 804` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Trackpad USB iOS/tvOS - DM - TopCase - 613` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Trackpad USB iOS/tvOS - DM - TopCase - 804` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - DM - TopCase - 1104` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - DM - TopCase - 1105` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - DM - TopCase - 1108` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - DM - TopCase - 1109` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - DM - TopCase - 1110` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - DM - TopCase - 1111` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - DM - TopCase - 622` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - DM - TopCase - 623` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`

## Strings in its kext that name it (3)

- `[HID] [%s] [Error] %s::%s Failed to cast target to AppleDeviceManagementHIDEventService\n`
- `site.AppleDeviceManagementHIDEventService`
- `AppleDeviceManagementHIDEventService`

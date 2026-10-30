# `AppleMultitouchMouseHIDEventDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleTopCaseHIDEventDriver`](../kexts/com.apple.driver.AppleTopCaseHIDEventDriver.md)
- Object size: `0x190` (400 bytes)
- Metaclass: `0xfffffe000b9d3588`; metaclass vtable `0xfffffe00082953e8`; class vtable `0xfffffe0008294c60`
- Registration (init): `0xfffffe0009a14708`
- Superclasses: [`AppleMultitouchInputHIDEventDriver`](AppleMultitouchInputHIDEventDriver.md) → [`AppleMultitouchHIDEventDriverV2`](AppleMultitouchHIDEventDriverV2.md) → [`IOHIDEventDriver`](IOHIDEventDriver.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (4)

- `Magic Mouse BT iOS/tvOS Event Driver - TopCase - 617` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Mouse BT iOS/tvOS Event Driver - TopCase - 803` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Mouse USB iOS/tvOS Event Driver - TopCase - 617` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Mouse USB iOS/tvOS Event Driver - TopCase - 803` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`

## Strings in its kext that name it (2)

- `AppleMultitouchMouseHIDEventDriver`
- `site.AppleMultitouchMouseHIDEventDriver`

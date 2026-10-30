# `AppleHIDKeyboardEventDriverV2`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHIDKeyboard`](../kexts/com.apple.driver.AppleHIDKeyboard.md)
- Object size: `0x150` (336 bytes)
- Metaclass: `0xfffffe000b94d368`; metaclass vtable `0xfffffe00080dec98`; class vtable `0xfffffe00080de520`
- Registration (init): `0xfffffe0008e800a0`
- Superclasses: [`AppleEmbeddedKeyboard`](AppleEmbeddedKeyboard.md) → [`IOHIDEventDriver`](IOHIDEventDriver.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (27)

- `Wired Keyboard 2015` in [`com.apple.driver.AppleHIDKeyboard`](../kexts/com.apple.driver.AppleHIDKeyboard.md): `IOProviderClass` = `IOHIDInterface`
- `Wired Keyboard 2016` in [`com.apple.driver.AppleHIDKeyboard`](../kexts/com.apple.driver.AppleHIDKeyboard.md): `IOProviderClass` = `IOHIDInterface`
- `Wired Keyboard 2017` in [`com.apple.driver.AppleHIDKeyboard`](../kexts/com.apple.driver.AppleHIDKeyboard.md): `IOProviderClass` = `IOHIDInterface`
- `Wired Keyboard 2018` in [`com.apple.driver.AppleHIDKeyboard`](../kexts/com.apple.driver.AppleHIDKeyboard.md): `IOProviderClass` = `IOHIDInterface`
- `Wired Keyboard 2018 B` in [`com.apple.driver.AppleHIDKeyboard`](../kexts/com.apple.driver.AppleHIDKeyboard.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard (BT) - AppleHIDKeyboardEventDriverV2` in [`com.apple.driver.AppleTopCaseHIDEventDriver`](../kexts/com.apple.driver.AppleTopCaseHIDEventDriver.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard (USB) - AppleHIDKeyboardEventDriverV2` in [`com.apple.driver.AppleTopCaseHIDEventDriver`](../kexts/com.apple.driver.AppleTopCaseHIDEventDriver.md): `IOProviderClass` = `IOHIDInterface`
- `Extended Magic Keyboard with Touch ID BT Event Driver - TopCase - 671` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Extended Magic Keyboard with Touch ID BT Event Driver - TopCase - 802` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Extended Magic Keyboard with Touch ID USB Event Driver - TopCase - 671` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Extended Magic Keyboard with Touch ID USB Event Driver - TopCase - 802` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard BT Event Driver - TopCase - 668` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard BT Event Driver - TopCase - 800` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard USB Event Driver - TopCase - 668` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard USB Event Driver - TopCase - 800` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard with Touch ID BT Event Driver - TopCase - 666` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard with Touch ID BT Event Driver - TopCase - 801` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard with Touch ID USB Event Driver - TopCase - 666` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `Magic Keyboard with Touch ID USB Event Driver - TopCase - 801` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - KB - TopCase - 1104` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - KB - TopCase - 1105` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - KB - TopCase - 1108` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - KB - TopCase - 1109` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - KB - TopCase - 1110` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - KB - TopCase - 1111` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - KB - TopCase - 622` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`
- `iPad Magic Keyboard - KB - TopCase - 623` in [`com.apple.driver.AppleTopCaseDriverV2`](../kexts/com.apple.driver.AppleTopCaseDriverV2.md): `IOProviderClass` = `IOHIDInterface`

## Strings in its kext that name it (2)

- `AppleHIDKeyboardEventDriverV2`
- `site.AppleHIDKeyboardEventDriverV2`

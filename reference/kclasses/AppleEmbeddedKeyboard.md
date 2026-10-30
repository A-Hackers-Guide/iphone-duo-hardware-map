# `AppleEmbeddedKeyboard`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md)
- Object size: `0x110` (272 bytes)
- Metaclass: `0xfffffe000b9f6ed8`; metaclass vtable `0xfffffe000839cc98`; class vtable `0xfffffe000839c5a0`
- Registration (init): `0xfffffe000a1d3ab0`
- Superclasses: [`IOHIDEventDriver`](IOHIDEventDriver.md) → [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleHIDKeyboardEventDriver`](AppleHIDKeyboardEventDriver.md) — `com.apple.driver.AppleHIDKeyboard`
- [`AppleHIDKeyboardEventDriverV2`](AppleHIDKeyboardEventDriverV2.md) — `com.apple.driver.AppleHIDKeyboard`

## IOKit personalities that instantiate it (9)

- `Wireless Keyboard 2009 ANSI Map` in [`com.apple.driver.AppleHIDKeyboard`](../kexts/com.apple.driver.AppleHIDKeyboard.md): `IOProviderClass` = `IOHIDInterface`
- `Wireless Keyboard 2009 B ANSI Map` in [`com.apple.driver.AppleHIDKeyboard`](../kexts/com.apple.driver.AppleHIDKeyboard.md): `IOProviderClass` = `IOHIDInterface`
- `Wireless Keyboard 2009 B ISO Map` in [`com.apple.driver.AppleHIDKeyboard`](../kexts/com.apple.driver.AppleHIDKeyboard.md): `IOProviderClass` = `IOHIDInterface`
- `Wireless Keyboard 2009 B JIS Map` in [`com.apple.driver.AppleHIDKeyboard`](../kexts/com.apple.driver.AppleHIDKeyboard.md): `IOProviderClass` = `IOHIDInterface`
- `Wireless Keyboard 2009 ISO Map` in [`com.apple.driver.AppleHIDKeyboard`](../kexts/com.apple.driver.AppleHIDKeyboard.md): `IOProviderClass` = `IOHIDInterface`
- `Wireless Keyboard 2009 JIS Map` in [`com.apple.driver.AppleHIDKeyboard`](../kexts/com.apple.driver.AppleHIDKeyboard.md): `IOProviderClass` = `IOHIDInterface`
- `iAP B62 ANSI Map` in [`com.apple.driver.AppleHIDKeyboardEmbedded`](../kexts/com.apple.driver.AppleHIDKeyboardEmbedded.md): `IOProviderClass` = `IOHIDInterface`
- `iAP B62 ISO Map` in [`com.apple.driver.AppleHIDKeyboardEmbedded`](../kexts/com.apple.driver.AppleHIDKeyboardEmbedded.md): `IOProviderClass` = `IOHIDInterface`
- `iAP B62 JIS Map` in [`com.apple.driver.AppleHIDKeyboardEmbedded`](../kexts/com.apple.driver.AppleHIDKeyboardEmbedded.md): `IOProviderClass` = `IOHIDInterface`

## Strings in its kext that name it (2)

- `site.AppleEmbeddedKeyboard`
- `AppleEmbeddedKeyboard`

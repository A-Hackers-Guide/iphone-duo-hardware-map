# `IOHIDEventDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md)
- Object size: `0x108` (264 bytes)
- Metaclass: `0xfffffe000b9f6c58`; metaclass vtable `0xfffffe0008397358`; class vtable `0xfffffe0008396c60`
- Registration (init): `0xfffffe000a1bc538`
- Superclasses: [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (7; 15 in total)

- [`AppleEmbeddedKeyboard`](AppleEmbeddedKeyboard.md) — `com.apple.iokit.IOHIDFamily`
- [`AppleHIDKeyboardDeviceManagement`](AppleHIDKeyboardDeviceManagement.md) — `com.apple.driver.AppleHIDKeyboard`
- [`AppleMultitouchHIDEventDriver`](AppleMultitouchHIDEventDriver.md) — `com.apple.driver.AppleMultitouchDriver`
- [`AppleMultitouchHIDEventDriverV2`](AppleMultitouchHIDEventDriverV2.md) — `com.apple.driver.AppleMultitouchDriver`
- [`AppleProxAbstractHIDEventDriver`](AppleProxAbstractHIDEventDriver.md) — `com.apple.driver.AppleProxDriver`
- [`AppleSPUHIDEventDriver`](AppleSPUHIDEventDriver.md) — `com.apple.driver.AppleSPU`
- [`AppleUserHIDEventService`](AppleUserHIDEventService.md) — `com.apple.iokit.IOHIDFamily`

## IOKit personalities that instantiate it (16)

- `HID Game Controller Pointing Driver` in [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md): `IOProviderClass` = `IOHIDInterface`
- `BLE Trackable Accessory` in [`com.apple.iokit.IOHIDEventDriver`](../kexts/com.apple.iokit.IOHIDEventDriver.md): `IOProviderClass` = `IOHIDInterface`, `IOPropertyMatch` = `{'IsSpatialBluetoothHID': True}`, `IOProbeScore` = `2000`
- `HID Buttons` in [`com.apple.iokit.IOHIDEventDriver`](../kexts/com.apple.iokit.IOHIDEventDriver.md): `IOProviderClass` = `IOHIDInterface`
- `HID Fast Path` in [`com.apple.iokit.IOHIDEventDriver`](../kexts/com.apple.iokit.IOHIDEventDriver.md): `IOProviderClass` = `IOHIDInterface`, `IOPropertyMatch` = `{'SupportsIOFastPath': True}`, `IOProbeScore` = `2000`
- `HID Keyboard Driver` in [`com.apple.iokit.IOHIDEventDriver`](../kexts/com.apple.iokit.IOHIDEventDriver.md): `IOProviderClass` = `IOHIDInterface`
- `HID Sensor` in [`com.apple.iokit.IOHIDEventDriver`](../kexts/com.apple.iokit.IOHIDEventDriver.md): `IOProviderClass` = `IOHIDInterface`
- `Peppy Touch Display` in [`com.apple.iokit.IOHIDEventDriver`](../kexts/com.apple.iokit.IOHIDEventDriver.md): `IOProviderClass` = `IOHIDInterface`
- `HID Built-In Orientation Driver` in [`com.apple.iokit.IOHIDEventDriverSafeBoot`](../kexts/com.apple.iokit.IOHIDEventDriverSafeBoot.md): `IOProviderClass` = `IOHIDInterface`, `IOPropertyMatch` = `{'Built-In': True}`, `IOProbeScore` = `2`
- `HID Pointing Shim Driver` in [`com.apple.iokit.IOHIDEventDriverSafeBoot`](../kexts/com.apple.iokit.IOHIDEventDriverSafeBoot.md): `IOProviderClass` = `IOHIDInterface`
- `HID Pointing/Consumer/System Control Driver` in [`com.apple.iokit.IOHIDEventDriverSafeBoot`](../kexts/com.apple.iokit.IOHIDEventDriverSafeBoot.md): `IOProviderClass` = `IOHIDInterface`
- `HID SensorEvent Driver` in [`com.apple.iokit.IOHIDEventDriverSafeBoot`](../kexts/com.apple.iokit.IOHIDEventDriverSafeBoot.md): `IOProviderClass` = `IOHIDInterface`
- `HID SensorEvent Driver - Apple Crane Driver` in [`com.apple.iokit.IOHIDEventDriverSafeBoot`](../kexts/com.apple.iokit.IOHIDEventDriverSafeBoot.md): `IOProviderClass` = `IOHIDInterface`, `IOPropertyMatch` = `{'Built-In': True}`, `IOProbeScore` = `2`
- `HID SensorEvent Driver - Heart Rate` in [`com.apple.iokit.IOHIDEventDriverSafeBoot`](../kexts/com.apple.iokit.IOHIDEventDriverSafeBoot.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `2`
- `HID SensorEvent Driver - Hinge Angle` in [`com.apple.iokit.IOHIDEventDriverSafeBoot`](../kexts/com.apple.iokit.IOHIDEventDriverSafeBoot.md): `IOProviderClass` = `IOHIDInterface`, `IOPropertyMatch` = `{'Built-In': True}`, `IOProbeScore` = `2`
- `HID VendorEvent Driver` in [`com.apple.iokit.IOHIDEventDriverSafeBoot`](../kexts/com.apple.iokit.IOHIDEventDriverSafeBoot.md): `IOProviderClass` = `IOHIDInterface`
- `VMWare Legacy Work-around` in [`com.apple.iokit.IOHIDEventDriverSafeBoot`](../kexts/com.apple.iokit.IOHIDEventDriverSafeBoot.md): `IOProviderClass` = `IOHIDInterface`

## Strings in its kext that name it (3)

- `IOHIDEventDriver-debug`
- `IOHIDEventDriver`
- `site.IOHIDEventDriver`

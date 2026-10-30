# `IOHIDEventService`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.iokit.IOHIDFamily`](../kexts/com.apple.iokit.IOHIDFamily.md)
- Object size: `0xc8` (200 bytes)
- Metaclass: `0xfffffe000b9f69f8`; metaclass vtable `0xfffffe00083966d0`; class vtable `0xfffffe0008395fe0`
- Registration (init): `0xfffffe000a1b7c1c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (10; 68 in total)

- [`AHSTemperatureReporter`](AHSTemperatureReporter.md) — `com.apple.driver.AppleHapticsSupportLEAP`
- [`AppleDeviceManagementHIDEventService`](AppleDeviceManagementHIDEventService.md) — `com.apple.driver.AppleTopCaseHIDEventDriver`
- [`AppleEmbeddedBluetooth`](AppleEmbeddedBluetooth.md) — `com.apple.driver.ApplePencilDriver`
- [`AppleEmbeddedHIDEventService`](AppleEmbeddedHIDEventService.md) — `com.apple.iokit.IOHIDFamily`
- [`AppleGCHIDUserEventDriver`](AppleGCHIDUserEventDriver.md) — `com.apple.driver.AppleGameControllerPersonality`
- [`AppleMultitouchHIDEventService`](AppleMultitouchHIDEventService.md) — `com.apple.driver.AppleMultitouchDriver`
- [`EXBrightKext`](EXBrightKext.md) — `com.apple.EXBrightKext`
- [`IOHIDComplexEventDriver`](IOHIDComplexEventDriver.md) — `com.apple.iokit.IOHIDFamily`
- [`IOHIDEventDriver`](IOHIDEventDriver.md) — `com.apple.iokit.IOHIDFamily`
- [`IOHIDEventDummyService`](IOHIDEventDummyService.md) — `com.apple.iokit.IOHIDFamily`

## Strings in its kext that name it (23)

- `OSAction_IOHIDEventService__SetLED`
- `site.IOHIDEventServiceQueue`
- `IOHIDEventServiceUserClient`
- `site.OSAction_IOHIDEventService__SetUserProperties`
- `site.OSAction_IOHIDEventService__CopyEvent`
- `OSAction_IOHIDEventService__CopyEvent`
- `site.IOHIDEventService`
- `IOHIDEventServiceFastPathUserClient`
- `site.OSAction_IOHIDEventService__SetLED`
- `site.IOHIDEventServiceFastPathUserClient`
- `IOHIDEventService`
- `OSAction_IOHIDEventService__SetUserProperties`
- `site.IOHIDEventServiceUserClient`
- `IOHIDEventServiceQueue`
- `IOHIDEventService.cpp`
- `IOHIDEventServiceFastPathUserClient::open:%x (task resume)\n`
- `IOHIDEventServiceQueue::enqueueEvent - Queue is full! %p\n`
- `IOHIDEventServiceFastPathUserClient suspended:%d\n`
- `IOHIDEventServiceFastPathUserClient::open missing properties\n`
- `IOHIDEventServiceFastPathUserClient::open not ready\n`
- `IOHIDEventServiceFastPathUserClient::open already opened\n`
- `IOHIDEventServiceFastPathUserClient::_copyEvent: %x\n`
- `IOHIDEventServiceFastPathUserClient::open _owner->openForClient failed\n`

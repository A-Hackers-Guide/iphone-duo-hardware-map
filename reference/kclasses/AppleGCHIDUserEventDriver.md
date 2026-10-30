# `AppleGCHIDUserEventDriver`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md)
- Object size: `0xd0` (208 bytes)
- Metaclass: `0xfffffe000b946638`; metaclass vtable `0xfffffe00080b7630`; class vtable `0xfffffe00080b6f40`
- Registration (init): `0xfffffe0008d0eda8`
- Superclasses: [`IOHIDEventService`](IOHIDEventService.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`SteamControllerUserEventDriver`](SteamControllerUserEventDriver.md) — `com.apple.driver.AppleGameControllerPersonality`

## IOKit personalities that instantiate it (21)

- `Access Controller IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `DualSense Controller IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `DualSense Edge Controller IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Generic Controller Device` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1301`
- `Luna Controller IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Nintendo JoyCon Grip IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Nintendo JoyCon L IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Nintendo JoyCon R IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Nintendo Switch N64 Controller IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Nintendo Switch Pro Controller IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Nintendo Switch SNES Controller IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Playstation Dualshock Controller IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `T1 DualShock 4 Controller IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Xbox 360 Controller IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Xbox Adaptive Controller` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Xbox Elite V2 Controller` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Xbox Elite V2 USB IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Xbox Series X Wired Controller IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Xbox Series X Wireless Controller` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Xbox Wired Controller IOService` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`
- `Xbox Wireless Controller` in [`com.apple.driver.AppleGameControllerPersonality`](../kexts/com.apple.driver.AppleGameControllerPersonality.md): `IOProviderClass` = `IOHIDInterface`, `IOProbeScore` = `1000`

## Strings in its kext that name it (4)

- `AppleGCHIDUserEventDriver`
- `site.AppleGCHIDUserEventDriver`
- `AppleGCHIDUserEventDriver::probe(<IOHIDDevice %#010llx>)`
- `AppleGCHIDUserEventDriver::handleStart(<IOHIDInterface %#010llx>)`

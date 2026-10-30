# `AppleTCControllerType10`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x1118` (4,376 bytes)
- Metaclass: `0xfffffe000b94ef78`; metaclass vtable `0xfffffe00080fde38`; class vtable `0xfffffe00080fd378`
- Registration (init): `0xfffffe0008f8b7b4`
- Superclasses: [`AppleTCController`](AppleTCController.md) → [`IOAccessoryManagerUSBC`](IOAccessoryManagerUSBC.md) → [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (2; 2 in total)

- [`AppleTCControllerType12`](AppleTCControllerType12.md) — `com.apple.driver.AppleHPM`
- [`AppleTCControllerType14`](AppleTCControllerType14.md) — `com.apple.driver.AppleHPM`

## IOKit personalities that instantiate it (1)

- `AppleTCControllerType10` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleHPMDevice`

## Strings in its kext that name it (19)

- `%s::%s(0x%x@0x%x): AppleTCControllerType10::forcePortEvaluation(@0x%x) - Defer failed, interrupts and messages may not have been sent\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::starttAMETimeoutTimer(@0x%x) - called\n\n`
- `AppleTCControllerType10::overrideHPMMode -- enforce=%d, keepRoleAndOrientation=%d, dataStatus=%u, status=%u\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10hal::forcePortEvaluation(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::stopUSBTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::forceUSB23On(@0x%x) - advertise unplug\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::startUSBTimer(@0x%x) - called\n\n`
- `AppleTCControllerType10`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::stoptAMETimeoutTimer(@0x%x) - called\n\n`
- `site.AppleTCControllerType10`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::start(@0x%x) - no command gate\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::tUSBTimeout(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::tAMETimeout(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::poweredStart(@0x%x) - start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::forceUSB23On(@0x%x) - force usb23 on, setting fWaitingForUSB to true\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::forcePortEvaluation(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::turnOnVbus(0x%x) - setting fWaitingForUSB to false\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::tUSBTimeout(@0x%x) - Waiting for USB Timedout After 10 seconds\n\n`

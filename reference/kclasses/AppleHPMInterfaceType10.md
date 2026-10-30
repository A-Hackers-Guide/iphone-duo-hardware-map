# `AppleHPMInterfaceType10`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x14a0` (5,280 bytes)
- Metaclass: `0xfffffe000b94ede8`; metaclass vtable `0xfffffe00080f8b90`; class vtable `0xfffffe00080f8038`
- Registration (init): `0xfffffe0008f8092c`
- Superclasses: [`AppleHPMInterface`](AppleHPMInterface.md) → [`AppleTCController`](AppleTCController.md) → [`IOAccessoryManagerUSBC`](IOAccessoryManagerUSBC.md) → [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (4; 4 in total)

- [`AppleHPMInterfaceType14`](AppleHPMInterfaceType14.md) — `com.apple.driver.AppleHPM`
- [`AppleHPMInterfaceType15`](AppleHPMInterfaceType15.md) — `com.apple.driver.AppleHPM`
- [`AppleHPMInterfaceType16`](AppleHPMInterfaceType16.md) — `com.apple.driver.AppleHPM`
- [`AppleHPMInterfaceType17`](AppleHPMInterfaceType17.md) — `com.apple.driver.AppleHPM`

## IOKit personalities that instantiate it (1)

- `AppleHPMInterfaceType10` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleHPMDeviceHAL`

## Strings in its kext that name it (18)

- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::forcePortEvaluation(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::stoptAMETimeoutTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::stopUSBTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::poweredStart(@0x%x) - start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::start(@0x%x) - no command gate\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::tAMETimeout(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::startUSBTimer(@0x%x) - called\n\n`
- `site.AppleHPMInterfaceType10`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::turnOnVbus(0x%x) - setting fWaitingForUSB to false\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::tUSBTimeout(@0x%x) - Waiting for USB Timedout After 10 seconds\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::configureUSBRemoteWakeup(@0x%x) - Called with args 0x%x\n\n`
- `AppleHPMInterfaceType10::overrideHPMMode -- enforce=%d, keepRoleAndOrientation=%d, dataStatus=%u, status=%u\n`
- `AppleHPMInterfaceType10`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::forceUSB23On(@0x%x) - force usb23 on, setting fWaitingForUSB to true\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::forceUSB23On(@0x%x) - advertise unplug\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::tUSBTimeout(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::starttAMETimeoutTimer(@0x%x) - called\n\n`

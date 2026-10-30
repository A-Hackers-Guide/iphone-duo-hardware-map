# `AppleTCControllerType1`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x1118` (4,376 bytes)
- Metaclass: `0xfffffe000b94f130`; metaclass vtable `0xfffffe00081043e0`; class vtable `0xfffffe0008103900`
- Registration (init): `0xfffffe0008fa7bf8`
- Superclasses: [`AppleTCController`](AppleTCController.md) → [`IOAccessoryManagerUSBC`](IOAccessoryManagerUSBC.md) → [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleTCControllerType1` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleHPMDevice`

## Strings in its kext that name it (40)

- `%s::%s(0x%x@0x%x): AppleTCControllerType10::forcePortEvaluation(@0x%x) - Defer failed, interrupts and messages may not have been sent\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::starttAMETimeoutTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType1::configureDP(@0x%x) - failed to get interface: AV=%p DP=%p\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType12::createUSB3PortObject(@0x%x) - creating usb3 port object tunnelAdapterType=%d\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType1::setPowerStateHPM(@0x%x) = Setting power state to 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType12::start - Overriding mux settings 0x%x\n\n`
- `AppleTCControllerType10::overrideHPMMode -- enforce=%d, keepRoleAndOrientation=%d, dataStatus=%u, status=%u\n`
- `AppleTCControllerType1`
- `%s::%s(0x%x@0x%x): AppleTCControllerType1::communicateDPIRQ(@0x%x) - Unused in this class\n\n`
- `AppleTCControllerType12`
- `%s::%s(0x%x@0x%x): AppleTCControllerType14::start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType1::setPowerStateHPM(@0x%x) - SSPS executed, status = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType14::hpmInterruptAction(@0x%x) - Interrupt Recieved\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType12::start - Overriding USB3 settings 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10hal::forcePortEvaluation(@0x%x) - Start\n\n`
- `site.AppleTCControllerType14`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::stopUSBTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::forceUSB23On(@0x%x) - advertise unplug\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType1::configureDP(@0x%x) - powering on DP\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::startUSBTimer(@0x%x) - called\n\n`
- `AppleTCControllerType10`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::stoptAMETimeoutTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType14::processInterruptEvents(@0x%x) - interrupts = 0x%x 0x%x 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType14::processInterruptEvents(@0x%x) - Start\n\n`
- `site.AppleTCControllerType1`
- `site.AppleTCControllerType10`
- `%s::%s(0x%x@0x%x): AppleTCControllerType1::configureDP(@0x%x) - powering off DP\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::start(@0x%x) - no command gate\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType1::communicateDPHPDChange(@0x%x) - Unused in this class\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::tUSBTimeout(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::tAMETimeout(@0x%x) - called\n\n`
- `site.AppleTCControllerType12`
- `%s::%s(0x%x@0x%x): AppleTCControllerType1::configureUSBRemoteWakeup(@0x%x) - Called with args 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::poweredStart(@0x%x) - start\n\n`
- `AppleTCControllerType14`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::forceUSB23On(@0x%x) - force usb23 on, setting fWaitingForUSB to true\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::forcePortEvaluation(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::turnOnVbus(0x%x) - setting fWaitingForUSB to false\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::tUSBTimeout(@0x%x) - Waiting for USB Timedout After 10 seconds\n\n`

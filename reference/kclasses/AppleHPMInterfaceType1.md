# `AppleHPMInterfaceType1`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x14a0` (5,280 bytes)
- Metaclass: `0xfffffe000b94f200`; metaclass vtable `0xfffffe0008107230`; class vtable `0xfffffe00081066b8`
- Registration (init): `0xfffffe0008fb0c18`
- Superclasses: [`AppleHPMInterface`](AppleHPMInterface.md) → [`AppleTCController`](AppleTCController.md) → [`IOAccessoryManagerUSBC`](IOAccessoryManagerUSBC.md) → [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleHPMInterfaceType3`](AppleHPMInterfaceType3.md) — `com.apple.driver.AppleHPM`

## IOKit personalities that instantiate it (1)

- `AppleHPMInterfaceType1` in [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md): `IOProviderClass` = `AppleHPMDeviceHAL`

## Strings in its kext that name it (60)

- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType17::start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType16::processInterruptEvents(@0x%x) - RREC %x RRaDC %x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType14::roleswapTimeoutCallback - swap waited, retrying\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType14::roleswapTimeoutCallback - swapping failed either rejected or cmd failure, status = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType11::start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType16::processInterruptEvents(@0x%x) - Ridge Ready\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::forcePortEvaluation(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::start\n\n`
- `site.AppleHPMInterfaceType11`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::stoptAMETimeoutTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType1::configureDP(@0x%x) - failed to get interface: AV=%p DP=%p\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::stopUSBTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType11::setInterruptMask(@0x%x) - start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType1::setPowerStateHPM(@0x%x) = Setting power state to 0x%x\n\n`
- `site.AppleHPMInterfaceType15`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::poweredStart(@0x%x) - start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType1::configureDP(@0x%x) - powering on DP\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::start(@0x%x) - no command gate\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType14::stopRoleswapTimeoutTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::tAMETimeout(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType16::configureUSB2PortObject(@0x%x) - Forcing USB2 UFP data role for optical cable\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::startUSBTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType11::start(@0x%x) - no command gate\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType1::communicateDPIRQ(@0x%x) - Unused in this class\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType16::processInterruptEvents(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType1::configureUSBRemoteWakeup(@0x%x) - Called with args 0x%x\n\n`
- `site.AppleHPMInterfaceType1`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType1::communicateDPHPDChange(@0x%x) - Unused in this class\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType15::start\n\n`
- `site.AppleHPMInterfaceType10`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType15::repeaterReset(@0x%x) - Called with target 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType17::start - Failed to get spmi provider\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType15::stopRoleswapTimeoutTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType16::start failed to get fHALType5\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType15::roleswapTimeoutCallback - swapping failed either rejected or cmd failure, status = 0x%x\n\n`
- `AppleHPMInterfaceType17`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType17::start - Failed to create interrupt source\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::turnOnVbus(0x%x) - setting fWaitingForUSB to false\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType16::processInterruptEvents(@0x%x) - No Data Status at UFP\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType17:setupMatchingForUFP can't find AppleHPMInterfaceType16\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::tUSBTimeout(@0x%x) - Waiting for USB Timedout After 10 seconds\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType14::start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType16::start fHALType5 %p\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType16::processInterruptEvents(@0x%x) - Ridge Ready Event\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType16::start - Failed to allocate DC2 IOIES\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType11::poweredStart(@0x%x) - start\n\n`
- `site.AppleHPMInterfaceType14`
- `AppleHPMInterfaceType15`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::configureUSBRemoteWakeup(@0x%x) - Called with args 0x%x\n\n`
- `AppleHPMInterfaceType10::overrideHPMMode -- enforce=%d, keepRoleAndOrientation=%d, dataStatus=%u, status=%u\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType14::startRoleswapTimeoutTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType16::setInterruptMask(@0x%x) - start\n\n`
- `AppleHPMInterfaceType14`
- `AppleHPMInterfaceType10`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::forceUSB23On(@0x%x) - force usb23 on, setting fWaitingForUSB to true\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::forceUSB23On(@0x%x) - advertise unplug\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType1::setPowerStateHPM(@0x%x) - SSPS executed, status = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType15::roleswapTimeoutCallback - swap waited, retrying\n\n`
- `AppleHPMInterfaceType11`
- `site.AppleHPMInterfaceType16`

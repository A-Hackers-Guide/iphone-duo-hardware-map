# `AppleTCController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x10f8` (4,344 bytes)
- Metaclass: `0xfffffe000b94f040`; metaclass vtable `0xfffffe0008100a10`; class vtable `0xfffffe00080fff50`
- Registration (init): `0xfffffe0008fa0e6c`
- Superclasses: [`IOAccessoryManagerUSBC`](IOAccessoryManagerUSBC.md) → [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (6; 16 in total)

- [`AppleHPMInterface`](AppleHPMInterface.md) — `com.apple.driver.AppleHPM`
- [`AppleTCControllerAssignableTransport`](AppleTCControllerAssignableTransport.md) — `com.apple.driver.AppleHPM`
- [`AppleTCControllerSingleTransport`](AppleTCControllerSingleTransport.md) — `com.apple.driver.AppleHPM`
- [`AppleTCControllerType1`](AppleTCControllerType1.md) — `com.apple.driver.AppleHPM`
- [`AppleTCControllerType10`](AppleTCControllerType10.md) — `com.apple.driver.AppleHPM`
- [`AppleTCControllerTypeSim`](AppleTCControllerTypeSim.md) — `com.apple.driver.AppleHPM`

## Strings in its kext that name it (60)

- `%s::%s(0x%x@0x%x): AppleTCController::initSingleHPM - Failed to get i2c provider\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::challengeCrypto(@0x%x) - HPMV1 locating function\n\n`
- `AppleTCController`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::Start(@0x%x) - no interrupt source found\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::setAccessoryID(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::start(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::genericStart - Failed to get dockPhandle\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::genericStart - Failed to get interrupt provider\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::createPCIePortObject(@0x%x) - pcie is not setup\n\n`
- `AppleTCControllerTypeSim`
- `%s::%s(0x%x@0x%x): AppleTCController::genericStart(@0x%x) - IONVRAM check failed\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::initSingleHPM - interrupt-type isn't 32-byte aligned no interrupts at all.\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::setPowerState(@0x%x) - Status != Success, setPowerStateHPM failed!\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::processInterruptEvents(@0x%x) - Not notifying drivers of state, fRestore = 0x%x and interruptCountAppLoaded = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::forcePortEvaluation(@0x%x) - Defer failed, interrupts and messages may not have been sent\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::stopAnalyticsTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::execute4Cc(@0x%x) - 4cc = %s\n\n`
- `AppleTCController::resolvePHandle - failed after service matching\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::start\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::enableOptions(0x%x) - kart already enabled\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::challengeCrypto(@0x%x) - Start hpmv1 = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::setupPCIClient(@0x%x) - Tunnel PCI client does not exist!\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::genericStart(@0x%x) - ***allow usb3 restores: %u***\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType10::starttAMETimeoutTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::genericStart(@0x%x) - disable USBPD SOPp nub publishing set 0x%X\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType1::configureDP(@0x%x) - failed to get interface: AV=%p DP=%p\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::processStatusRegisters(@0x%x) - advertise unplug\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::start(@0x%x) - Enabling Debug, Flags = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::callPlatformFunction(0x%x) - exit called no valid data\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType12::createUSB3PortObject(@0x%x) - creating usb3 port object tunnelAdapterType=%d\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::genericStart(@0x%x) - In Restore\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::setPinConfiguration(@0x%x) - Could not reconfigure pin configuration dictionary\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::configureDPPortObject(@0x%x) - Failed to activate tunneled transport, no tbthandle\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::initSingleHPM - failed to match on dock\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::challengeCrypto(@0x%x) - Aborting due to previous errors\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::exitPDMode(@0x%x) - DRST complete - status = 0x%08x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::start(@0x%x) - IONVRAM check failed\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::processInterruptEvents(@0x%x) - interrupts = 0x%x 0x%x 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::createUSB3PortObject(@0x%x) - creating usb3 port object tunnelAdapterType=%d\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::createDPPortObject(@0x%x) - dp is setup\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::genericStart(@0x%x) - CC transport failed!\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::createTunnelClient(@0x%x) - Client already exists for type 0x%x\n\n`
- `site.AppleTCControllerSingleTransport`
- `%s::%s(0x%x@0x%x): AppleTCController::challengeCrypto(@0x%x) - Warning: CRYm timed out after ~%u, aborting\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::configureDPPortObject(@0x%x) - Failed to activate DP transport!\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::processModeFlags(0x%x) - Kart mode skipping message due to forced disconnect\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::usbChangeNotification: kIOPortTransportState_Message_DriverStatusChange\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerType1::setPowerStateHPM(@0x%x) = Setting power state to 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::readRegWithLength(@0x%x) - Reading 0x%x with Length of 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::callPlatformFunction(0x%x) - prst called with 255, setting it to 0\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::initSingleHPM - Missing interrupt property, Check the EDT, AppleHPM will not be fully functional\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::setLDCMState(0x%x) - Could not assign power control, returning Error\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::genericStart(@0x%x) - Enabling Debug, Flags = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::genericStart - HPMV1\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::createUSB3PortObject(@0x%x) - USB3 is setup\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::setupDP1Client(@0x%x) - Tunnel DP1 client does not exist!\n\n`
- `%s::%s(0x%x@0x%x): AppleTCControllerSingleTransport::Start(@0x%x) - no interrupt source found to add\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::initSingleHPM - Failed to get workloop\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::setUSB2PortObjectInactive(@0x%x) - usb2handle NULL!\n\n`
- `%s::%s(0x%x@0x%x): AppleTCController::getSecondaryMuxConfig(@0x%x) - start\n\n`

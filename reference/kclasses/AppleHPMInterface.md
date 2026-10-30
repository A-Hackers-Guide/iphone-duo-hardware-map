# `AppleHPMInterface`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0x1480` (5,248 bytes)
- Metaclass: `0xfffffe000b94ed20`; metaclass vtable `0xfffffe00080f5490`; class vtable `0xfffffe00080f4938`
- Registration (init): `0xfffffe0008f7b614`
- Superclasses: [`AppleTCController`](AppleTCController.md) → [`IOAccessoryManagerUSBC`](IOAccessoryManagerUSBC.md) → [`IOAccessoryManager`](IOAccessoryManager.md) → [`IOPort`](IOPort.md) → [`IOPortFamily`](IOPortFamily.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (3; 8 in total)

- [`AppleHPMInterfaceType1`](AppleHPMInterfaceType1.md) — `com.apple.driver.AppleHPM`
- [`AppleHPMInterfaceType10`](AppleHPMInterfaceType10.md) — `com.apple.driver.AppleHPM`
- [`AppleHPMInterfaceType11`](AppleHPMInterfaceType11.md) — `com.apple.driver.AppleHPM`

## Strings in its kext that name it (60)

- `%s::%s(0x%x@0x%x): AppleHPMInterface::callPlatformFunction(0x%x) - exit called with %d\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::configureUSB3PortObject(@0x%x) - USB3 added and ready\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::ldcmInterruptAction(0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::commonStartPhase2 - Failed to create fDriverStatusInterrupt\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::createTunnelClientCallBacks(@0x%x) - Tunnel client does not exist!\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::enableOptions(0x%x) - kart already enabled\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::forcePortEvaluation(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setLDCMState(0x%x) - called with state = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType3::stopRoleswapTimeoutTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setCurrentModeFlags(@0x%x) - OTA upgrade check\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType3::roleswapTimeoutCallback - swap waited, retrying\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::challengeCrypto(@0x%x) - HPMV1 function located\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::hpmInterruptAction(@0x%x) - Interrupt Recieved\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setPinConfiguration(@0x%x) - No pin config set, no data connection\n\n`
- `site.AppleHPMInterface`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::rtPanicHandler(@0x%x) - Byte 0 of register 0x5d = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::challengeCrypto(@0x%x) - Warning: CRYm timed out after ~%u, aborting\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::createTunnelClientCallBacks(@0x%x) - Tunnel client call back created successfully\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setupMatchingForLDCM - Failed to allocate callback, LDCM wont' work properly\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType17::start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setCurrentModeFlags(@0x%x) - Removing port forcing and clearing flags, fisOTA = 0x%x, fRestore = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::start(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::configureDPPortObject(@0x%x) - Failed to activate DP transport!\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType16::processInterruptEvents(@0x%x) - RREC %x RRaDC %x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::configureUSB3PortObject(@0x%x) - Failed to activate USB transport!\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setCurrentModeFlags(@0x%x) - No plug detected, all flags cleared\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType14::roleswapTimeoutCallback - swap waited, retrying\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType14::roleswapTimeoutCallback - swapping failed either rejected or cmd failure, status = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::readReg(@0x%x) - Read completed after 0x%x retries\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::stopAnalyticsTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType3::startRoleswapTimeoutTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType11::start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::challengeCrypto(@0x%x) - HPMV1 function handle NOT found\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setPowerState(@0x%x) - Status != Success, setPowerStateHPM failed!\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::callPlatformFunction(0x%x) - prst called with 0x%x, which is unknown, not executing reset\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::processInterruptEvents(@0x%x) - Adjusting HPM power state to active unplugged\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::genericStart(@0x%x) - Enabling SSAM testing, Flags = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::initSingleHPM - Missing interrupt-type property, doing legacy interrupt handling, no SPMI sleep/wake support\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType16::processInterruptEvents(@0x%x) - Ridge Ready\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setUSB2PortObjectInactive(@0x%x) - usb2handle NULL!\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::configureUSB2PortObject(@0x%x) - WARNING: USB2 notifier was not created\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setLDCMPin(0x%x) - ACE Debug already set, skipping\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::configureTBTPortObject(@0x%x) - CIO already provisioned\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::createTunnelClient(@0x%x) - Client already exists for type 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::processModeFlags(0x%x) - Kart mode skipping message due to forced disconnect\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setLDCMMitigationsEnabled(0x%x) - called with mitigationsEnabled = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setLDCMPin(0x%x) - already Hi-Z, skipping\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::genericStart(@0x%x) - disable USBPD SOPp nub publishing set 0x%X\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::forcePortEvaluation(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::createTunnelHandles(@0x%x) - failed to create tunnel manager!\n\n`
- `AppleHPMInterfaceType3`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::processModeFlags(0x%x) - Kart mode looks ok, sending message\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setPowerStateHPM(@0x%x) = Setting power state to 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::createDPPortObject(@0x%x) - dp is setup\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::repeaterReset(@0x%x) - Called with target 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::initInterruptManager - Failed to get command gate\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::isCableKartCapable(0x%x) - active cable detected\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::getManagerType(@0x%x) - ERROR: _armHPMNub doesn't exist!\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType10::start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::tunnelClientChange(@0x%x) - dp2 client ping\n\n`

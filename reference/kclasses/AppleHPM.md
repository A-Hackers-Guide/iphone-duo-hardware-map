# `AppleHPM`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleHPM`](../kexts/com.apple.driver.AppleHPM.md)
- Object size: `0xf0` (240 bytes)
- Metaclass: `0xfffffe000b94f188`; metaclass vtable `0xfffffe0008105360`; class vtable `0xfffffe0008104c90`
- Registration (init): `0xfffffe0008fae308`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 5 in total)

- [`AppleHPMEmbedded`](AppleHPMEmbedded.md) — `com.apple.driver.AppleHPM`

## Strings in its kext that name it (60)

- `%s::%s(0x%x@0x%x): AppleHPMInterface::callPlatformFunction(0x%x) - exit called with %d\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::configureUSB3PortObject(@0x%x) - USB3 added and ready\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::ldcmInterruptAction(0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::commonStartPhase2 - Failed to create fDriverStatusInterrupt\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::createTunnelClientCallBacks(@0x%x) - Tunnel client does not exist!\n\n`
- `AppleHPMARM can't find AppleSMC\n`
- `AppleHPMDeviceHAL::setStatus - WARNING: Abnormal Status Length = 0x%x\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::enableOptions(0x%x) - kart already enabled\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::forcePortEvaluation(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setLDCMState(0x%x) - called with state = 0x%x\n\n`
- `AppleHPMLDCM::start - Periodic data gathering enable = 0x%x\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType3::stopRoleswapTimeoutTimer(@0x%x) - called\n\n`
- `AppleHPMSMCBridge<%p>::start - hpmlog boot-arg: 0x%X\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setCurrentModeFlags(@0x%x) - OTA upgrade check\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType3::roleswapTimeoutCallback - swap waited, retrying\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::challengeCrypto(@0x%x) - HPMV1 function located\n\n`
- `site.AppleHPMDeviceHAL`
- `AppleHPMSMCBridge<%p>::start - hpmI2CRetries boot-arg: %u ms\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::hpmInterruptAction(@0x%x) - Interrupt Recieved\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setPinConfiguration(@0x%x) - No pin config set, no data connection\n\n`
- `AppleHPMAIDType1::getHPMCommsBus - failed to get communication bus service, no messages will be sent`
- `AppleHPMARMSPMI::start - failed to register wake event int\n`
- `site.AppleHPMInterface`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::rtPanicHandler(@0x%x) - Byte 0 of register 0x5d = 0x%x\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::challengeCrypto(@0x%x) - Warning: CRYm timed out after ~%u, aborting\n\n`
- `AppleHPMCommandGate`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::createTunnelClientCallBacks(@0x%x) - Tunnel client call back created successfully\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setupMatchingForLDCM - Failed to allocate callback, LDCM wont' work properly\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType17::start\n\n`
- `site.AppleHPMARMI2C`
- `AppleHPMLDCM::start - couldn't allocate periodic buffer, failing start\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setCurrentModeFlags(@0x%x) - Removing port forcing and clearing flags, fisOTA = 0x%x, fRestore = 0x%x\n\n`
- `AppleHPMARMSPMI::start - interrupt-type and interrupts not equal length, things will not work. No SPMI slee/wake support\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::start(@0x%x) - Start\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::configureDPPortObject(@0x%x) - Failed to activate DP transport!\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType16::processInterruptEvents(@0x%x) - RREC %x RRaDC %x\n\n`
- `site.AppleHPMCommandGate`
- `AppleHPMAsyncEventSource`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::configureUSB3PortObject(@0x%x) - Failed to activate USB transport!\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setCurrentModeFlags(@0x%x) - No plug detected, all flags cleared\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType14::roleswapTimeoutCallback - swap waited, retrying\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType14::roleswapTimeoutCallback - swapping failed either rejected or cmd failure, status = 0x%x\n\n`
- `AppleHPMLDCM::isVoltageDetected - raw 0x%x\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::readReg(@0x%x) - Read completed after 0x%x retries\n\n`
- `AppleHPMDevice`
- `AppleHPMLDCM::setVbusPresent - called setting %x\n`
- `AppleHPM::atomic4cc -- UBaS/SAlr/NSup detected\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::stopAnalyticsTimer(@0x%x) - called\n\n`
- `AppleHPMBusController::setActiveHPMCount - Active HPM Counter Altered, new Active = 0x%x, expected = 0x%x\n`
- `site.AppleHPMDeviceHALType4`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType3::startRoleswapTimeoutTimer(@0x%x) - called\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterfaceType11::start\n\n`
- `AppleHPMDeviceHALType5::writeUSBConfigBuffer %02x %02x %02x %02x\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::challengeCrypto(@0x%x) - HPMV1 function handle NOT found\n\n`
- `AppleHPMSMCBridge<%p>::start - Unable to read hpmlog boot-arg\n`
- `site.AppleHPMBusDevice`
- `AppleHPM.kext/PlugIns/AppleHPMLib.plugin`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::setPowerState(@0x%x) - Status != Success, setPowerStateHPM failed!\n\n`
- `%s::%s(0x%x@0x%x): AppleHPMInterface::callPlatformFunction(0x%x) - prst called with 0x%x, which is unknown, not executing reset\n\n`
- `AppleHPMDeviceHAL::setDataStatus - WARNING: Abnormal DataStatus Length = 0x%x\n`

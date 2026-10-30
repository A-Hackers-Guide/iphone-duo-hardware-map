# `AppleSynopsysMIPIDSIController`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleSynopsysMIPIDSI`](../kexts/com.apple.driver.AppleSynopsysMIPIDSI.md)
- Object size: `0x65e0` (26,080 bytes)
- Metaclass: `0xfffffe000b9a58d8`; metaclass vtable `0xfffffe000823b770`; class vtable `0xfffffe000823b1b0`
- Registration (init): `0xfffffe0009792814`
- Superclasses: [`AppleARMMIPIDSIController`](AppleARMMIPIDSIController.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleSynopsysMIPIDSIController` in [`com.apple.driver.AppleSynopsysMIPIDSI`](../kexts/com.apple.driver.AppleSynopsysMIPIDSI.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `mipi-dsim-1,synopsys`

## Strings in its kext that name it (44)

- `AppleSynopsysMIPIDSIController::start Failed to get phy settings count\n`
- `AppleSynopsysMIPIDSIController::start: Sad SAC enabled, switch between MIPI freq highest and lowest\n`
- `\"AppleSynopsysMIPIDSIController::_sacGenerateFrequencyList: failed to generate any valid frequencies\" @%s:%d`
- `IOReturn AppleSynopsysMIPIDSIController::sendSWMPRShortCommandGated(UInt8, UInt8, UInt8)`
- `IOReturn AppleSynopsysMIPIDSIController::sendShortCommandGated(UInt8, UInt8, UInt8)`
- `\"AppleSynopsysMIPIDSIController:_leaveAPIFunction usage count < 0\" @%s:%d`
- `IOReturn AppleSynopsysMIPIDSIController::_enableDSIM(bool)`
- `IOReturn AppleSynopsysMIPIDSIController::enableInterfaceGated(bool)`
- `IOReturn AppleSynopsysMIPIDSIController::receiveLongCommandGated(UInt8, UInt8 *, IOByteCount *)`
- `\"AppleSynopsysMIPIDSIController::start: Failed to create the SAC thread\" @%s:%d`
- `IOReturn AppleSynopsysMIPIDSIController::sendLongCommandGated(UInt8, const UInt8 *, IOByteCount)`
- `IOReturn AppleSynopsysMIPIDSIController::enableVideoGated(bool)`
- `IOReturn AppleSynopsysMIPIDSIController::enableHighSpeedModeGated(bool)`
- `AppleSynopsysMIPIDSIController.cpp`
- `\"AppleSynopsysMIPIDSIController::start Not enough information to enable SAC \" @%s:%d`
- `void AppleSynopsysMIPIDSIController::_sacGetFrequencyList(UInt32 *, sac_pll_t **, const char *, const char *)`
- `IOReturn AppleSynopsysMIPIDSIController::_enableSWMPRGated(bool)`
- `IOReturn AppleSynopsysMIPIDSIController::_resetHSClockGated()`
- `\"AppleSynopsysMIPIDSIController::_waitPhyStatus timeout \" \"(status & 0x%08x) %s 0x%08x\\n\" @%s:%d`
- `\"AppleSynopsysMIPIDSIController::start Could not create lock\" @%s:%d`
- `virtual bool AppleSynopsysMIPIDSIController::start(IOService *)`
- `AppleSynopsysMIPIDSIController::start Failed to get phy settings\n`
- `void AppleSynopsysMIPIDSIController::_pollReg(UInt32, UInt32, UInt32, bool)`
- `void AppleSynopsysMIPIDSIController::_sacThread()`
- `IOReturn AppleSynopsysMIPIDSIController::_isDMMExitedGated()`
- `void AppleSynopsysMIPIDSIController::_initSWMPR()`
- `AppleSynopsysMIPIDSIController::start: Sad SAC enabled, switch between desense priority highest and lowest\n`
- `AppleSynopsysMIPIDSIController::enableInterface %d: _readReg32(kSynopsysDSIM_CORE_PHY_STATUS)  0x%x status_mask 0x%x\n`
- `IOReturn AppleSynopsysMIPIDSIController::_calculateRegisterValues(UInt32 *, UInt32 *, display_timing_t *, mipi_lpm_t *)`
- `\"AppleSynopsysMIPIDSIController::_sacGenerateFrequencyList: kSACMaxFrequencyCount exceeded\" @%s:%d`
- `IOReturn AppleSynopsysMIPIDSIController::_isCommitDoneGated()`
- `IOReturn AppleSynopsysMIPIDSIController::sendSWMPRLongCommandGated(UInt8, const UInt8 *, IOByteCount)`
- `IOReturn AppleSynopsysMIPIDSIController::receiveShortCommandGated(UInt8, UInt8 *)`
- `\"AppleSynopsysMIPIDSIController::start _sacGenerateFrequencyList failed: %08x\" @%s:%d`
- `AppleSynopsysMIPIDSIController::start: Sad SAC enabled, round robin MIPI desense priority freqeuncies\n`
- `\"AppleSynopsysMIPIDSIController::enableInterfaceGated : MIPI PLL Failed to lock: 0x%08x\" @%s:%d`
- `AppleSynopsysMIPIDSIController::start: this: %p, _dsimBaseAddress = %#lx physical = %#lx length %llu\n`
- `IOReturn AppleSynopsysMIPIDSIController::setLPMEnableGated(bool)`
- `site.AppleSynopsysMIPIDSIController`
- `\"AppleSynopsysMIPIDSIController::start AppleARMFunctionSlowAdaptiveClockingAggressor::withProvider() failed\" @%s:%d`
- `virtual IOReturn AppleSynopsysMIPIDSIController::getDisplayTiming(bool, display_timing_t *)`
- `AppleSynopsysMIPIDSIController`
- `\"AppleSynopsysMIPIDSIController::start AppleARMFunctionSlowAdaptiveClockingAggressor::withProvider() LPM failed\" @%s:%d`
- `\"AppleSynopsysMIPIDSIController::_sacGenerateFrequencyList: unsupported SAC Version (%d)\" @%s:%d`

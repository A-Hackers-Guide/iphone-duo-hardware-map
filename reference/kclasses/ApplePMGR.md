# `ApplePMGR`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.ApplePMGR`](../kexts/com.apple.driver.ApplePMGR.md)
- Object size: `0x738d8` (473,304 bytes)
- Metaclass: `0xfffffe000b987458`; metaclass vtable `0xfffffe000818f080`; class vtable `0xfffffe0008189e60`
- Registration (init): `0xfffffe000933d4c0`
- Superclasses: [`ApplePMGRBase`](ApplePMGRBase.md) → [`IOPMGR`](IOPMGR.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (1; 1 in total)

- [`AppleBringUpPMGR`](AppleBringUpPMGR.md) — `com.apple.driver.ApplePMGR`

## Strings in its kext that name it (60)

- `bool ApplePMGR::_getBit(UInt32, DeviceIDGroupMask *)`
- `void ApplePMGR::writeANEClkGenReg(UInt32, UInt32, UInt32, UInt32)`
- `\"ApplePMGR: %s:%u REQUIRE failed: %s\" @%s:%d`
- `void ApplePMGR::writePMGRClkGenSOCReg(UInt32, UInt32, UInt32)`
- `ApplePMGR:   %-16s| ID = %#04x | FLAGS = %#02x | PERF = %s + %#010x\n`
- `UInt64 ApplePMGR::_getCPUComplexCPMPowerGateCount(CPUComplex *)`
- `virtual bool ApplePMGRFunctionPerfCycleCount::initWithTargetDataAndSymbol(IOService *, const OSData *, const OSSymbol *)`
- `virtual bool ApplePMGR::roscDataUpdate(PerfDomainID, const RoscData *, bool, UInt32)`
- `ApplePMGRFunctionSetTouchClockSource`
- `void ApplePMGR::_publishTraceProperties()`
- `ApplePMGR: Powering down clusters associated with devices that are set to PowerOff\n`
- `UInt64 ApplePMGR::_getCPUComplexIdleExitCount(CPUComplex *)`
- `UInt32 ApplePMGR::getVirtToPhysComplexInDie(UInt32)`
- `ApplePMGR: Copying HW DPE node data\n`
- `void ApplePMGR::_waitForCioClusterCompleteGated(UInt64, UInt32, UInt32, bool)`
- `ApplePMGR:   %s + %#010x | Register Count = %u\n`
- `ApplePMGR: High Perf State Max Credits = %llu\n`
- `ApplePMGRFunctionGetServiceState`
- `\"ApplePMGR: %s:%u \" \"device %x (%s) wrong perfDomainID %x\\n\" @%s:%d`
- `site.ApplePMGRFunctionGetServiceState`
- `ApplePMGR: %s: autoPowerGating=%s\n`
- `void ApplePMGR::writePMGRAONMiniMiscReg(UInt32, UInt32, UInt32)`
- `site.ApplePMGRFunctionCLPCEnabled`
- `ApplePMGRFunctionEnableCPUCore`
- `ApplePMGRFunctionAssertReset`
- `site.ApplePMGRFunctionCPUIdle`
- `void ApplePMGR::writePMGRSOCGpce1Reg(UInt32, UInt32, UInt32)`
- `ApplePMGR: chipRevMinor = %x\n`
- `\"ApplePMGR: %s:%u \" \"_deviceIDToIndexMap[%x] == %x != kIndexReserved\" @%s:%d`
- `void ApplePMGR::updateDie1CPUVoltages()`
- `virtual IOReturn ApplePMGRFunctionEnableAutoClockGate::callFunction(void *, void *, void *)`
- `void ApplePMGR::_setPwrGateRetentionV2(DeviceID, bool, UInt32)`
- `ApplePMGRFunctionCPUIdle`
- `\"Attempting to register for scheduler callbacks via ApplePMGR\" @%s:%d`
- `virtual void ApplePMGR::setPLLOffMode(RegMap, UInt32, UInt32, UInt32)`
- `virtual void ApplePMGR::quiesceHW()`
- `ApplePMGR: Parameters:\n`
- `\"ApplePMGR: %s:%u \" \"acquireDeviceLocks took %lld us, startTime %lld, energyLockTime %lld, perfLocktime %lld, device %x\\n\" @%s:%d`
- `\"ApplePMGR: %s:%u \" \"device %x is perf counter only, not suitable for %s\" @%s:%d`
- `ApplePMGR: Interrupt received with intIndex = %u, cnt = %u\n`
- `ApplePMGR%sRoscData`
- `void ApplePMGR::writePMGRSOCGpce0Reg(UInt32, UInt32, UInt32)`
- `IOReturn ApplePMGR::_getClockReqMemoryPMC(unsigned int, void *)`
- `site.ApplePMGRNub`
- `virtual void ApplePMGR::enableFANE(bool)`
- `handle != ApplePMGR::kInvalidIndex`
- `site.ApplePMGRFunctionEnableCPUCore`
- `void ApplePMGR::_enableBridgeByteCounters(Bridge, bool, bool, UInt32)`
- `ApplePMGR: AP wake sources: %#x\n`
- `ApplePMGRv2.cpp`
- `site.ApplePMGRFunctionResetPSDService`
- `ApplePMGR: Restoring device perf counters\n`
- `ApplePMGRFunctionEnableTouchClock`
- `ApplePMGR: Perf State: %u:\n`
- `ApplePMGR: Restoring ACC %u event perf counters\n`
- `ApplePMGR: Register Groups:\n`
- `virtual void ApplePMGR::checkEnergy(EnergyNode *, UInt64)`
- `void ApplePMGR::_setPSAutoMinLevel(PSRegGroup, PSRegIndex, PSLevel, UInt32)`
- `com.apple.private.ApplePMGRUserClient.access`
- `virtual void ApplePMGR::panicHW()`

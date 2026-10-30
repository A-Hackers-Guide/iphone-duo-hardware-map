# `RTBuddy`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md)
- Object size: `0x66a0` (26,272 bytes)
- Metaclass: `0xfffffe000ba23c98`; metaclass vtable `0xfffffe0008494128`; class vtable `0xfffffe0008493a38`
- Registration (init): `0xfffffe000a92da00`
- Superclasses: [`IOSlaveProcessor`](IOSlaveProcessor.md) → [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## Direct subclasses (3; 3 in total)

- [`RTBuddy64`](RTBuddy64.md) — `com.apple.driver.RTBuddy`
- [`RTBuddyARG`](RTBuddyARG.md) — `com.apple.driver.RTBuddy`
- [`RTBuddyRouteOnly`](RTBuddyRouteOnly.md) — `com.apple.driver.RTBuddy`

## IOKit personalities that instantiate it (1)

- `RTBuddy` in [`com.apple.driver.RTBuddy`](../kexts/com.apple.driver.RTBuddy.md): `IOProviderClass` = `AppleA7IOPNub`, `IONameMatch` = `iop-nub,rtbuddy-v2`

## Device-tree nodes it binds (15) [DT]

- [`/arm-io/aop/iop-aop-nub`](../devicetree/root__arm-io__aop__iop-aop-nub.md) on `iop-nub,rtbuddy-v2`
- [`/arm-io/aop2/iop-aop2-nub`](../devicetree/root__arm-io__aop2__iop-aop2-nub.md) on `iop-nub,rtbuddy-v2`
- [`/arm-io/pmp/iop-pmp-nub`](../devicetree/root__arm-io__pmp__iop-pmp-nub.md) on `iop-nub,rtbuddy-v2`
- [`/arm-io/sio/iop-sio-nub`](../devicetree/root__arm-io__sio__iop-sio-nub.md) on `iop-nub,rtbuddy-v2`
- [`/arm-io/ans/iop-ans-nub`](../devicetree/root__arm-io__ans__iop-ans-nub.md) on `iop-nub,rtbuddy-v2`
- [`/arm-io/smc/iop-smc-nub`](../devicetree/root__arm-io__smc__iop-smc-nub.md) on `iop-nub,rtbuddy-v2`
- [`/arm-io/mtp/iop-mtp-nub`](../devicetree/root__arm-io__mtp__iop-mtp-nub.md) on `iop-nub,rtbuddy-v2`
- [`/arm-io/dcp/iop-dcp-nub`](../devicetree/root__arm-io__dcp__iop-dcp-nub.md) on `iop-nub,rtbuddy-v2`
- [`/arm-io/dcpsec/iop-dcpsec-nub`](../devicetree/root__arm-io__dcpsec__iop-dcpsec-nub.md) on `iop-nub,rtbuddy-v2`
- [`/arm-io/dcpext0/iop-dcpext0-nub`](../devicetree/root__arm-io__dcpext0__iop-dcpext0-nub.md) on `iop-nub,rtbuddy-v2`
- [`/arm-io/ispRtb/iop-isp-nub`](../devicetree/root__arm-io__ispRtb__iop-isp-nub.md) on `iop-nub,rtbuddy-v2`
- [`/arm-io/ane0/iop-ane0-nub`](../devicetree/root__arm-io__ane0__iop-ane0-nub.md) on `iop-nub,rtbuddy-v2`
- [`/arm-io/ane1/iop-ane1-nub`](../devicetree/root__arm-io__ane1__iop-ane1-nub.md) on `iop-nub,rtbuddy-v2`
- [`/arm-io/gfx-asc/iop-gfx-nub`](../devicetree/root__arm-io__gfx-asc__iop-gfx-nub.md) on `iop-nub,rtbuddy-v2`
- [`/arm-io/gfx1-asc/iop-gfx1-nub`](../devicetree/root__arm-io__gfx1-asc__iop-gfx1-nub.md) on `iop-nub,rtbuddy-v2`

## Strings in its kext that name it (60)

- `site.RTBuddyTimeDecoder`
- `IOMemoryMap *RTBuddyCoredumpMap::readwriteMapForIopVirtual(IOVirtualAddress, IOVirtualAddress *)`
- `\"RTBuddy(%s)::%s \" \"message %llx for unknown endpoint %d\" \"\\n%s\" @%s:%d`
- `RTBuddyCoredump`
- `RTBuddy(%s)::%s: 'crashlog-region' data invalid: %p:%p\n`
- `site.RTBuddySegmentSlice`
- `void RTBuddyTraceKitEndpoint::_setEndpointActiveGated(bool)`
- `RTBuddyHeapDecoder`
- `site.RTBuddyNvramDecoder`
- `site.RTBuddyUserClient`
- `IOReturn RTBuddyKdebugEndpoint::_kdebugSendFlushRequest()`
- `IOReturn RTBuddyTraceKitEndpoint::_configureGated(rtbuddy_trace_config_t, OSSharedPtr<RTBuddyTraceKitSession> &)`
- `RTBuddyUserClient`
- `RTBuddyCoredumpDecoder`
- `site.RTBuddyCoredumpMap`
- `IOReturn RTBuddyManagementEndpoint::_handlePowerAck(mbi_msg_t)`
- `site.RTBuddyBinaryLogEntryHandlerSysLog`
- `virtual void RTBuddyTraceKitEndpoint::kdebugCallback(kd_callback_type, void *)`
- `site.RTBuddyRouteAdaptor`
- `bool RTBuddyBuiltinEndpoint::initWithOptions(IOSlaveProcessor *, IOSlaveEndpoint::Action, void *, uint32_t, const char *, unsigned int)`
- `RTBuddy`
- `void RTBuddyEntropyEndpoint::_handleEntropyRequest(mbi_msg_t)`
- `RTBuddyService`
- `virtual IOReturn RTBuddy::loadFirmware(RTBuddyFirmware *)`
- `site.RTBuddyBuiltinEndpoint`
- `RTBuddy(%s): %s%s%s\n`
- `RTBuddyVisibleSlaveBuffer`
- `RTBuddySlaveMemoryDescriptor`
- `RTBuddy(%s): start(%p) - (%s@%s)\n`
- `site.RTBuddyCoredump`
- `IOReturn RTBuddyKdebugEndpoint::_kdebugSendEnabledState()`
- `RTBuddyDictionaryDecoder.cpp`
- `void RTBuddyKdebugEndpoint::_handleFlush(mbi_msg_t)`
- `RTBuddySymbolsDecoder`
- `\"RTBuddy(%s)::%s \" \"invalid reporter type (%d) for reporter %s (0x%llx)\" \"\\n%s\" @%s:%d`
- `RTBuddy(%s)::%s: Unimplemented kdebug command: %x\n`
- `site.RTBuddyTraceKitSession`
- `bool RTBuddy::_foundFirmwareService(void *, IOService *, IONotifier *)`
- `\"RTBuddy(%s)::%s \" \"Unable to restore SRAM contents\" \"\\n%s\" @%s:%d`
- `void RTBuddyKdebugEndpoint::_handleHereIsMyBuffer(mbi_msg_t)`
- `IOReturn RTBuddyTraceKitEndpoint::releaseChunkCPUTrace(rtbuddy_cputrace_chunk_t)_block_invoke`
- `site.RTBuddyCoprocDrivenCoredump`
- `_kdebugCoreID = kdebug_register_coproc(_iopRole->getCStringNoCopy(), _continuousTimestamps ? KDCP_CONTINUOUS_TIME : (kdebug_coproc_flags_t)0, OSMemberFunctionCast(kd_callback_fn, this, &RTBuddy::_kdebugCallback), this )`
- `void RTBuddyOSLogEndpoint::_handleNewCoalescerRequest(const mbi_msg_t)`
- `site.RTBuddy`
- `\"RTBuddy(%s)::%s \" \"failed to start (%x)\" \"\\n%s\" @%s:%d`
- `virtual IOReturn RTBuddy::_setPowerStatePerformChangeGated(const RTBuddyPowerState *, const bool *)`
- `IOReporter *RTBuddyIOReportingEndpoint::_addReporter(const io_reporting_reporter_t &, OSBoundedPtr<const uint8_t>)`
- `virtual IOSlaveEndpoint *RTBuddy::endpointForHandle(OSObject *, IOSlaveEndpoint::Action, UInt32, void *)`
- `%s:%d Assertion failed: %s : RTBuddyEndpointService doesn't work with built-in endpoints: %u\n`
- `RTBuddyCrashlogDecoder.cpp`
- `RTBuddyPatchBay.h`
- `IOReturn RTBuddyIOReportingEndpoint::_updateRemoteReportersGated()`
- `unsigned int RTBuddySyslogEndpoint::_maxEntrySize() const`
- `bool RTBuddyCoredump::initWithOptions(RTBuddy *, RTBuddyCoredumpArch)`
- `RTBuddyARG`
- `RTBuddyFirmwareService`
- `site.RTBuddyMailboxDecoder`
- `RTBuddyMessageQueue.cpp`
- `\"RTBuddy(%s)::%s \" \"Invalid Pstate passed: %d\" \"\\n%s\" @%s:%d`

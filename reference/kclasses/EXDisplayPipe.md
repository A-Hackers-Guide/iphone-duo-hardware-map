# `EXDisplayPipe`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.EXDisplayPipeH19P`](../kexts/com.apple.driver.EXDisplayPipeH19P.md)
- Object size: `0x958` (2,392 bytes)
- Metaclass: `0xfffffe000b9e0228`; metaclass vtable `0xfffffe00082de580`; class vtable `0xfffffe00082de028`
- Registration (init): `0xfffffe0009c5c14c`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `EXDisplayPipe` in [`com.apple.driver.EXDisplayPipeH19P`](../kexts/com.apple.driver.EXDisplayPipeH19P.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['exdisplaypipe,t8160', 'exdisplaypipe1,t8160']`

## Device-tree nodes it binds (2) [DT]

- [`/arm-io/exdisplaypipe`](../devicetree/root__arm-io__exdisplaypipe.md) on `exdisplaypipe,t8160`
- [`/arm-io/exdisplaypipe1`](../devicetree/root__arm-io__exdisplaypipe1.md) on `exdisplaypipe1,t8160`

## Strings in its kext that name it (60)

- `EXDisplayPipe::%s: m_frame_num_stale_timeout is %d\n`
- `EXDisplayPipe::%s Exits <-- \n`
- `EXDisplayPipe::%s SCA IOWorkLoop creation failed\n`
- `EXDisplayPipe: error: showIndicator(%u, ...) failed\n`
- `[EXDisplayPipe]: %s: m_display_index %d \n`
- `[EXDisplayPipe]: Hide Indicator %s\n`
- `EXDisplayPipe::%s exclaveStart failed\n`
- `[EXDisplayPipe]: %s: edk_service %s \n`
- `EXDisplayPipe::%s Telemetry IOWorkLoop creation failed\n`
- `EXDisplayPipe: error: args->structureOutputSize (0x%x) != sizeof(EXDisplayPipeHealthStats) (0x%lx)\n`
- `EXDisplayPipe: error: setPower(%u) failed\n`
- `[EXDisplayPipe]: %s: exclave_service_prop is NULL \n`
- `EXDisplayPipe: error: getFrameInfo(...) failed\n`
- `EXDisplayPipe::%s setup_exclave_async_notification failed\n`
- `EXDisplayPipe::%s failed!!! \n`
- `[EXDisplayPipe]: %s: disp_index %d \n`
- `EXDisplayPipe::%s get_display_index failed\n`
- `EXDisplayPipe::%s complete for ID %d \n`
- `EXDisplayPipe::%s: Couldn't map device memory.\n`
- `EXDisplayPipe::%s addEventSource failed for IOInterruptEventSource at index %d \n`
- `EXDisplayPipeUserClient: init failed\n`
- `EXDisplayPipe::setIndicators tightbeam call failed, has_value is false\n`
- `EXDisplayPipe::%s addEventSource failed with 0x%x\n`
- `[EXDisplayPipe]: setPowerInternal: power is already %s\n`
- `EXDisplayPipe::%s tightbeam call failed with 0x%x\n`
- `EXDisplayPipe::%s failed to get IODeviceTree:/options\n`
- `EXDisplayPipe::setLogMask tightbeam call failed with 0x%x\n`
- `EXDisplayPipe::%s telemetry IOTimerEventSource creation failed \n`
- `EXDisplayPipe::%s addEventSource failed for telemetry IOTimerEventSource \n`
- `EXDisplayPipe::%s: OSNumber allocation failed\n`
- `EXDisplayPipe::%s failed to allocate IOInterruptEventSource\n`
- `EXDisplayPipe: error: getScaSessionHealth(...) failed\n`
- `EXDisplayPipe::%s Exclave IOWorkLoop creation failed\n`
- `[EXDisplayPipe]: %s: edk_service_prop is NULL \n`
- `EXDisplayPipe::%s Unexpected message size!\n`
- `EXDisplayPipe::%s exclaveAsyncNotificationRegister failed with 0x%x\n`
- `[EXDisplayPipe] %s: stuck setting power to %u\n`
- `EXDisplayPipe::%s watchdog IOTimerEventSource creation failed \n`
- `EXDisplayPipeUserClient`
- `EXDisplayPipe::%s setup_sca_done_async_notification failed\n`
- `EXDisplayPipe: error: args->scalarInputCount (0x%x) != 1\n`
- `EXDisplayPipe: error: getStatus(...) failed\n`
- `EXDisplayPipe::%s exdisplaypipecompanioninterface__init failed with 0x%x\n`
- `EXDisplayPipe: error: structureOutputSize mismatch for GetFrameInfo\n`
- `EXDisplayPipe.cpp`
- `EXDisplayPipe::%s getNVRAMWriteInfo failed\n`
- `EXDisplayPipe::getSecureTEStatus unable to get status\n`
- `EXDisplayPipe::%s registerPrioritySleepWakeInterest failed\n`
- `EXDisplayPipe::%s Received shutdown notification (messageType=0x%x)\n`
- `EXDisplayPipe::hideIndicator tightbeam call failed, has_value is false\n`
- `EXDisplayPipe: error: submitTelemetry(...) failed\n`
- `EXDisplayPipeCompanionInterface_C.c`
- `\"[EXDisplayPipe] %s: failed to set power to %u in time\\n\" @%s:%d`
- `EXDisplayPipe::%s watchdog IOWorkLoop creation failed\n`
- `EXDisplayPipeDebug.cpp`
- `EXDisplayPipe::%s failed to allocate OSString\n`
- `EXDisplayPipe: error: getStats(...) failed\n`
- `EXDisplayPipe::%s NVRAM display-post set successfully\n`
- `EXDisplayPipe::showIndicator tightbeam call failed with 0x%x\n`
- `EXDisplayPipe::getStatus unable to get status\n`

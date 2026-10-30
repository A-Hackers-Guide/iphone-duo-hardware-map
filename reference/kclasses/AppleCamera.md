# `AppleCamera`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleCamera`](../kexts/com.apple.driver.AppleCamera.md)
- Object size: `0x84a28` (543,272 bytes)
- Metaclass: `0xfffffe000b93a540`; metaclass vtable `0xfffffe0008014260`; class vtable `0xfffffe0008013c48`
- Registration (init): `0xfffffe0008ab0f28`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (3)

- `RTBuddyBringup` in [`com.apple.driver.AppleCamera`](../kexts/com.apple.driver.AppleCamera.md): `IOProviderClass` = `RTBuddyService`, `IOPropertyMatch` = `{'role': 'ISP'}`
- `generic` in [`com.apple.driver.AppleCamera`](../kexts/com.apple.driver.AppleCamera.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `isp,isp-generic-1`
- `generic-ex` in [`com.apple.driver.AppleCamera`](../kexts/com.apple.driver.AppleCamera.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `isp,isp-generic-ex`, `IOProbeScore` = `10000`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/isp`](../devicetree/root__arm-io__isp.md) on `isp,isp-generic-ex`

## Strings in its kext that name it (60)

- `AppleCamera:%s - Failed to instantiate camera auth support\n`
- `AppleCamera:%s - I2C slave error, smsta=0x%08x\n`
- `AppleCamera:%s - Error: Overlapping end of copy offset memcpy\n`
- `AppleCamera:%s - Registering exclave isp upcall for strobe control with notification Id: %u\n`
- `AppleCamera:%s - Couldn't create ISPLoggerEventSource.\n`
- `AppleCamera:%s - messageClients(kISPTailspinAEReqLate, 0x%016llx)\n`
- `AppleCamera:%s - Enable ANE IPC service endpoint on platform: 0x%x\n`
- `AppleCamera:%s - wired client surface-id:0x%08X, w=%-4u, h=%-4u, fmt=%-3u, poolID=%-4u, dartMapBase=%#llX\n`
- `AppleCamera:%s - [Exclaves] ISP_InitializeExclave took %lld usec\n\n`
- `AppleCamera:%s - Could not change power state to %d: ret=0x%08X\n`
- `AppleCamera:%s - Could not create IOSurface for ISPCPU firmware buffer\n`
- `AppleCamera:%s - optical-dev-card-id is present in the IORegistry. val=???\n`
- `AppleCamera:%s - Not destroying session, at least one camera is active\n`
- `AppleCamera:%s - CISP_CMD_RPC_ENABLE failed!\n`
- `AppleCamera:%s - Error: The client's rawBuffer does not have the necessary privilege!\n\n`
- `AppleCamera:%s - Releasing ISP LTR override on power-up\n`
- `AppleCamera:%s - initializeEndpoint failed %d, 0x%08x\n`
- `AppleCamera:%s - Unable to start more than one channel at a time (channelMask=%8x)\n`
- `AppleCamera::client_log_buffer_t:%s - IOSurface ID %#x has insufficient size: %#zx bytes\n\n`
- `AppleCamera:%s - init IDL call failed\n`
- `AppleCamera:%s - Error: mcache request message exceeds message size limit!\n`
- `AppleCamera:%s - Invalid buffer return: 0x%llX\n`
- `AppleCamera:%s - mapFwCTRRRegion segment-ranges is not in the device tree\n`
- `AppleCamera:%s - [Exclaves] fExclaveInitializationStatus: FAIL\n`
- `AppleCamera:%s - EC NVM Read - mask: 0x%06X, ret: 0x%08X\n`
- `AppleCamera:%s - registerInterestedDriver: 0x%08lx (service=%s)\n`
- `AppleCamera:%s - Exclaves not supported on this platform\n`
- `AppleCamera`
- `AppleCamera:%s - ISP_Init failed: 0x%08X\n`
- `AppleCamera:%s - willChange: dev=%s state=%lu isSPU=%d isRTB=%d\n`
- `AppleCamera:%s - CISP_CMD_SUSPEND was NOT sent as res=0x%x\n`
- `AppleCamera:%s - starting\n`
- `AppleCamera:%s - Statistics: NonPersistentMemory:%llu, PersistentMemory:%llu, DeletionPendingMemory:%llu, NonPersistentMemoryMax:%llu, PersistentMemoryMax:%llu\n`
- `AppleCamera:%s - Unable to retrieve endpoint configuration from AOP\n`
- `AppleCamera::%s: Could not allocate memory for ioreg data\n`
- `AppleCamera:%s - AllocateHeapMemorySurface: 0x%x, heap size: 0x%x\n`
- `AppleCamera::%s: CISP_CMD_CH_SENSOR_BOOT failed, result = 0x%x\n`
- `AppleCamera:%s - clientContext or session is NULL\n`
- `AppleCamera:%s - Could not find a matching dictionary for the AOP RTBuddy Service\n`
- `AppleCamera:%s - ISP Logging Buffer Reallocation!. Current ISP firmware log message size (%d) does match driver's expectation (%d)\n`
- `site.AppleCameraVMAllocator`
- `AppleCamera:%s - Error: Overlapping start of copy offset memcpy\n`
- `AppleCamera:%s - ISPFW print buffer is invalid after address translation!\n`
- `AppleCamera:%s - Could not get a matching provider, exiting\n`
- `AppleCamera:%s - Statistics: Starts:%lld, Resumes:%lld, SuspendSuccesses:%lld, SuspendFails:%lld, ResumeFails:%lld, DeInits:%lld\n`
- `AppleCamera:%s - Could not get the matching provider, exiting\n`
- `AppleCamera:%s - MotionStateSet(true)\n`
- `AppleCamera:%s - Timed out waiting for the dartErrorHandler to complete\n`
- `com.apple.driver.AppleCamera.PearlCamBuffer`
- `AppleCamera:%s - couldn't prepare consolidated memory descriptor: 0x%x\n`
- `AppleCamera:%s - Failed to initialize ISP-ANE IPC\n`
- `AppleCamera:%s - kIOMessageSystemWillSleep fSystemSleepInProgress=%d. Setting fSystemSleepInProgress to false\n`
- `AppleCamera:%s - Could not map registers: PSExt0\n`
- `AppleCameraChannel:%s - sensor %d does not support hardware enable\n`
- `OSValueObject<AppleCameraFirmwareWorkProcessorRPCRequest>`
- `AppleCamera:%s - Timedout waiting for ISPCPU to write to IGP0RR register after CISP_CMD_POWER_DOWN.. Continue with power down\n`
- `AppleCamera::%s: Couldn't create a new memory descriptor for name\n`
- `AppleCamera:%s - ctrr-disabled is set\n`
- `AppleCamera:%s - GIC data exceeds maximum allowed size\n`
- `AppleCamera:%s - Channel %u metaBufferPoolId: %u\n`

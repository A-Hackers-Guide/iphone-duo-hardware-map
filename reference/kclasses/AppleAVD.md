# `AppleAVD`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleAVD`](../kexts/com.apple.driver.AppleAVD.md)
- Object size: `0x5060` (20,576 bytes)
- Metaclass: `0xfffffe000b9362b0`; metaclass vtable `0xfffffe0007fcf878`; class vtable `0xfffffe0007fcf318`
- Registration (init): `0xfffffe000877aafc`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `s5l8920x` in [`com.apple.driver.AppleAVD`](../kexts/com.apple.driver.AppleAVD.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['avd,s5l8920x', 'avd,t8020', 'avd,t8030', 'avd,t8101', 'avd,t8103']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/avd`](../devicetree/root__arm-io__avd.md) on `avd,t8103`

## Strings in its kext that name it (60)

- `AppleAVD: INFO: %s(): ## R/W DQ: %d %d; OQ: %d %d\n`
- `AppleAVD: ERROR: %s(): Failed to allocate AppleAVDPower object\n`
- `AppleAVD: INFO: %s(): M3 Retention Not Supported!\n\n`
- `AppleAVD: INFO: %s(): not supported HW Type %d\n`
- `AppleAVD: ERROR: %s(): kAllocMapTypeAllocatedUserMapKernel - IOMemoryDescriptor::withOptions API failed. %d \n\n`
- `AppleAVD: ERROR: %s(): CmdSetProperty (cid = %2d.%d) ACK = %d FAILED!!!!\n`
- `AppleAVD: ERROR: %s(): failed to allocate m_coreInfoList! status 0x%x\n`
- `AppleAVD: INFO: %s(): pWrap is NULL, assuming this is Ixora\n`
- `AppleAVD: ERROR: %s(): [Core %u] function-set_perf_state_floor is NULL!\n`
- `AppleAVD: ERROR: %s(): Failed to create rail gating timer source\n\n`
- `AppleAVD: INFO: %s(): avdConn. Aperture %d \n\n`
- `AppleAVD: ERROR: %s(): Failed to cast newService to CoreAnalyticsHub\n\n`
- `AppleAVD: INFO: %s(): AVD is not powered off in the retention state (power stage = %d), aborting!\n`
- `AppleAVD: INFO: %s(): AVDDart ERROR: m_Provider == NULL\n\n`
- `AppleAVD: WARNING: %s(): NULL pKernelMemInfo (index = %d)!\n\n`
- `AppleAVD: INFO: %s(): Shared buffer was never allocated!\n`
- `AppleAVD: ERROR: %s(): clientID %d not matching with resubmit client %d\n`
- `AppleAVD: INFO: %s(): Not supported AVD2 Revision %x\n`
- `AppleAVD: INFO: %s(): M3 Retention Supported!\n\n`
- `AppleAVD: INFO: %s(): [Core %u] Failed to boot\n`
- `AppleAVD: INFO: %s(): mapper/DART is inactive!\n`
- `AppleAVD: INFO: %s(): vp scheduling by Fw\n`
- `AppleAVD: ERROR: %s(): Likely an issue of mismatched KEXT vs plugin / test app\n`
- `AppleAVD: ERROR: %s(): addFrameToRefLists failed in->frameNumber = %d\n`
- `AppleAVD: INFO: %s(): %s returning kIOReturnSuccess always for 'drmi' %d\n`
- `AppleAVD: ERROR: %s(): unexpected start logic!! m_hwDeviceType = %d\n`
- `AppleAVD: ERROR: %s(): FW size is 0!. This is unexpected. Check if mBoot/IPCE had loaded AVD FW or not.\n`
- `AppleAVD: INFO: %s(): m_hwDeviceType = %d - Borage\n\n`
- `AppleAVD: INFO: %s(): Clean up input. Do not allow one-core platforms to choose which core to use\n`
- `AppleAVD: ERROR: %s(): invalid requested state!\n`
- `AppleAVD: ERROR: %s(): buffer has device memory cache mode!\n\n`
- `AppleAVD: INFO: %s(): sending encrypt property clientID %d for frame %d\n`
- `AppleAVD: INFO: %s(): [Hv0Cfg] %08x %08x %08x %08x\n`
- `AppleAVD: ERROR: %s(): Failed to allocate IOLock m_diagLock\n`
- `AppleAVD: INFO: %s(): only avd1 enabled (test mode); avdId = %d\n`
- `AppleAVD: ERROR: %s(): Failed to create AVD message box connection\n\n`
- `AppleAVD: ERROR: %s(): Failed to wait for MCpu boot - mcpu NULL!\n`
- `AppleAVD: INFO: %s(): t-out Handler: HW Timer event source found! Core%d!!\n`
- `AppleAVD: INFO: %s(): m_foxtrotRetryCount %u\n`
- `AppleAVD: INFO: %s(): clientID: %d - codecType: %d - isTestApp: %d - width: %d - height: %d - chromaFormat: %d - loadValue: %llu\n`
- `AppleAVD: INFO: %s(): m_maxFrameParamsInFlight changed from %d to %d\n`
- `AppleAVD: ERROR: %s(): failed to grab PQ! hwDeviceType: %d\n`
- `AppleAVD: INFO: %s(): Unsupported Codec Type %d for ApComm\n`
- `AppleAVD: ERROR: %s(): enter error code %d sub error %d\n`
- `AppleAVD: ERROR: %s(): Provided client did not match the entry in the user client list at index %u\n\n`
- `AppleAVD: INFO: %s(): AVD driver sees AVD0, but not AVD1 yet. Do not register service yet.\n`
- `AppleAVD: INFO: %s(): AVDDart ERROR: m_WorkLoop == NULL\n\n`
- `AppleAVD: ERROR: %s(): Failed for wait for DART mapper to become active (status 0x%x)\n\n`
- `AppleAVD: WARNING: %s(): NULL session struct for client %d\n\n`
- `AppleAVD: ERROR: %s(): bufIdx %d used yet\n`
- `AppleAVD: ERROR: %s(): should not have happen - invalid avdCore number %d(%d), nCid=%d, active=%d \n`
- `AppleAVD: ERROR: %s(): [FrameDone] cID %2d.%d, fNo: %8d, pCycle = %8d, cmpTOffset = %8d, %8d\n`
- `AppleAVD: ERROR: %s(): Failed to transition Driver state to kAvdDriverInactiveRG (result = %u)\n`
- `AppleAVD: INFO: %s(): AVDDart ERROR: failed to gen segments: 0x%08x\n\n`
- `AppleAVD: ERROR: %s(): setKDCryptRef failed\n\n`
- `AppleAVD: INFO: %s(): buffer still in-use, not ready to unmap, ref_count=%d, IOSID=%u\n\n`
- `AppleAVD: INFO: %s(): AVD ADS module valid bits not set yet! Waiting until valid. status=0x%x\n`
- `AppleAVD: ERROR: %s(): [Core %u] failed to grab WrapCtrl! hwDeviceType: %d\n\n`
- `AppleAVD: INFO: %s(): CAVDCMD_SET_PROPERTY (%d := %d)\n`
- `AppleAVD: INFO: %s(): setMemoryDescriptor success after flushing mapper cache\n`

# `AppleMSGKext`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleMSG`](../kexts/com.apple.driver.AppleMSG.md)
- Object size: `0x28288` (164,488 bytes)
- Metaclass: `0xfffffe000b97cc08`; metaclass vtable `0xfffffe000816b588`; class vtable `0xfffffe000816ae30`
- Registration (init): `0xfffffe0009224a28`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleMSG` in [`com.apple.driver.AppleMSG`](../kexts/com.apple.driver.AppleMSG.md): `IOProviderClass` = `AppleARMIODevice`, `IONameMatch` = `['msg-mapper']`

## Device-tree nodes it binds (1) [DT]

- [`/arm-io/msg`](../devicetree/root__arm-io__msg.md) on `msg-mapper`

## Strings in its kext that name it (60)

- `AppleMSGKext_Power::%s: _updateRegValues failed with retcode %x\n`
- `AppleMSGKext_RTVSync: AssertMacros: %s, %s file: %s, line: %d, value: %ld\n\n`
- `AppleMSGKextEPIC::%s: Overriding EDT sync configs for Camera 2-8 (DualSync=0)\n`
- `AppleMSGKext_EDT::%s: num_sync_interrupts = %d\n\n`
- `AppleMSGKext_ConfigCache::%s: dumping init config for sync id %i\n`
- `AppleMSGKextEPIC::%s: packetType:0x%x timestamp:%lld payloadSize:%zu\n`
- `AppleMSGKext_Power::%s: Detected transition still in progress on sleep, state %u (will be reset)\n`
- `AppleMSGKextEPIC::%s: Got report for ET #%u with count %llu, @time %llu.\n`
- `AppleMSGKextEPIC::%s: failed to end AFK Session during init!\n`
- `AppleMSGKext::%s: Boot-arg override syncgen %u frame duration: %llu\n`
- `AppleMSGKext_EDT::%s: Device Name in EDT is larger than allocation for our variable\n`
- `AppleMSGKextUserClient::%s: msg_log_info test\n`
- `AppleMSGKextEPIC::%s: Overriding EDT sync configs for Camera 2-8 (DualSync=1)\n`
- `AppleMSGKextEPIC::%s: Resuming GTB watchdog\n`
- `AppleMSGKext_EDT::%s: Found sync '%s' -> ID %u on device '%s'\n`
- `AppleMSGKext_EDT::%s: Found event trigger '%s' -> ID %u on device '%s'\n`
- `AppleMSGKext_UserMapping::%s: MSG memory mapping not available - _msgMemoryMap=%p, _msgProvider=%p\n`
- `AppleMSGKextEPIC::%s: Extending history for sync %u, count=%u, length=%u\n\n`
- `AppleMSGKextEPIC::%s: watchdog disabled by boot-arg.\n\n`
- `AppleMSGKextEPIC::%s: Response for bora errored with code: %x\n`
- `AppleMSGKextEPIC::%s: dumping current sync-gen history buffer for all active syncs\n`
- `AppleMSGKextEPIC::%s: Updated demand count=%llu and updated power state=%d\n`
- `AppleMSGKext_EDT::%s: No sync presets found\n\n`
- `AppleMSGKextEPIC::%s: syncGetStatus id %d retcode 0x%x active: %d\n`
- `AppleMSGKextEPIC::%s: err enqueueing cmd: %x\n`
- `AppleMSGKext_Transitions::%s: entry\n`
- `AppleMSGKext_Transitions::%s: Sync %d transitioning framerate index %u -> %u at GTB %llu (frame ID %u)\n`
- `AppleMSGKext_EDT::%s: configuring local sync #%d\n`
- `AppleMSGKext::%s: msg=0x%llx (%s)\n`
- `AppleMSGKextEPIC::%s: detected kernel POST testing enabled, watchdog disabled.\n\n`
- `AppleMSGKext_EDT::%s: Event trigger name '%s' not found in LUT\n`
- `AppleMSGKext_ConfigCache: AssertMacros: %s, %s file: %s, line: %d, value: %ld\n\n`
- `AppleMSGKext_TrackedTimer::%s: Set tracked time %hhu @ %llu: %llu; inc:%u+%hu/%hu\n`
- `AppleMSGKextEPIC::%s: msg_log_debug test\n`
- `AppleMSGKextEPIC: AssertMacros: %s, %s file: %s, line: %d, value: %ld\n\n`
- `AppleMSGKext_Notification::%s: Detected missed interrupt, using cached frame duration\n`
- `AppleMSGKext_Notification: AssertMacros: %s, %s file: %s, line: %d, value: %ld\n\n`
- `AppleMSGKextEPIC::%s: Read %u config presets in %u bytes from EDT\n\n`
- `AppleMSGKextEPIC::%s: intr enable vals=%u, sizeof=%lu\n`
- `AppleMSGKextEPIC::%s: msg_log_error test\n`
- `AppleMSGKext_Notification::%s: removed %u subscriptions for client\n`
- `AppleMSGKext_TrackedTimer: AssertMacros: %s, %s file: %s, line: %d, value: %ld\n\n`
- `AppleMSGKextUserClient::%s: msg_log_debug test\n`
- `AppleMSGKext_Interrupt::%s: AppleMSG Potentially Fatal (%u): FrameID changed from %llu to %llu between AP Interrupt Handler Executions.\n`
- `AppleMSGKext_EDT::%s: Found no interrupts for MSGKext\n\n`
- `AppleMSGKext_RTVSync::%s: last config, tracking: (%llu, %llu)\n`
- `AppleMSGKextEPIC::%s: Bora is powered off. Cannot release handles\n`
- `AppleMSGKext::%s: start\n`
- `AppleMSGKext::%s: probe()\n`
- `AppleMSGKext_Notification::%s: client DISCONNECTED id: %llu, checking for dangling subscriptions\n`
- `AppleMSGKextEPIC::%s: Enqueued ET #%u with count %llu, @time %llu.\n`
- `AppleMSGKextEPIC::%s: Config for sync %u is out of date\n\n`
- `AppleMSGKextEPICUserClient::%s: msg_log test\n`
- `AppleMSGKext_UserMapping::%s: Failed to create memory descriptor for MSG registers\n`
- `AppleMSGKextEPIC::%s: Found the EDT config hub!\n`
- `AppleMSGKextEPIC::%s: intr enable=%u\n`
- `AppleMSGKext_EDT::%s: Sync name LUT not available\n`
- `AppleMSGKext_Power::%s: _initSyncConfigs failed with retcode %x\n`
- `AppleMSGKextEPIC::%s: WARNING: sw sync id %u can't be mapped to hw sync id, skipping it's config tracing\n`
- `AppleMSGKextEPIC::%s: dumping current sync-gen history for sync %i\n`

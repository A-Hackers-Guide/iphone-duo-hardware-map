# `AppleMSGKextEPIC`

Kernel C++ class, from its OSMetaClass registration in `kernelcache.release.v6x-pandia`. **[KC]**

- Owner: [`com.apple.driver.AppleMSG`](../kexts/com.apple.driver.AppleMSG.md)
- Object size: `0x4430` (17,456 bytes)
- Metaclass: `0xfffffe000b97cd30`; metaclass vtable `0xfffffe000816d228`; class vtable `0xfffffe000816cc38`
- Registration (init): `0xfffffe0009235940`
- Superclasses: [`IOService`](IOService.md) → [`IORegistryEntry`](IORegistryEntry.md)

## IOKit personalities that instantiate it (1)

- `AppleMSGEPIC` in [`com.apple.driver.AppleMSG`](../kexts/com.apple.driver.AppleMSG.md): `IOProviderClass` = `AFKEndpointInterface`, `IONameMatch` = `msg-svc`

## Strings in its kext that name it (60)

- `AppleMSGKextEPIC::%s: Overriding EDT sync configs for Camera 2-8 (DualSync=0)\n`
- `AppleMSGKextEPIC::%s: packetType:0x%x timestamp:%lld payloadSize:%zu\n`
- `AppleMSGKextEPIC::%s: Got report for ET #%u with count %llu, @time %llu.\n`
- `AppleMSGKextEPIC::%s: failed to end AFK Session during init!\n`
- `AppleMSGKextEPIC::%s: Overriding EDT sync configs for Camera 2-8 (DualSync=1)\n`
- `AppleMSGKextEPIC::%s: Resuming GTB watchdog\n`
- `AppleMSGKextEPIC::%s: Extending history for sync %u, count=%u, length=%u\n\n`
- `AppleMSGKextEPIC::%s: watchdog disabled by boot-arg.\n\n`
- `AppleMSGKextEPIC::%s: Response for bora errored with code: %x\n`
- `AppleMSGKextEPIC::%s: dumping current sync-gen history buffer for all active syncs\n`
- `AppleMSGKextEPIC::%s: Updated demand count=%llu and updated power state=%d\n`
- `AppleMSGKextEPIC::%s: syncGetStatus id %d retcode 0x%x active: %d\n`
- `AppleMSGKextEPIC::%s: err enqueueing cmd: %x\n`
- `AppleMSGKextEPIC::%s: detected kernel POST testing enabled, watchdog disabled.\n\n`
- `AppleMSGKextEPIC::%s: msg_log_debug test\n`
- `AppleMSGKextEPIC: AssertMacros: %s, %s file: %s, line: %d, value: %ld\n\n`
- `AppleMSGKextEPIC::%s: Read %u config presets in %u bytes from EDT\n\n`
- `AppleMSGKextEPIC::%s: intr enable vals=%u, sizeof=%lu\n`
- `AppleMSGKextEPIC::%s: msg_log_error test\n`
- `AppleMSGKextEPIC::%s: Bora is powered off. Cannot release handles\n`
- `AppleMSGKextEPIC::%s: Enqueued ET #%u with count %llu, @time %llu.\n`
- `AppleMSGKextEPIC::%s: Config for sync %u is out of date\n\n`
- `AppleMSGKextEPICUserClient::%s: msg_log test\n`
- `AppleMSGKextEPIC::%s: Found the EDT config hub!\n`
- `AppleMSGKextEPIC::%s: intr enable=%u\n`
- `AppleMSGKextEPIC::%s: WARNING: sw sync id %u can't be mapped to hw sync id, skipping it's config tracing\n`
- `AppleMSGKextEPIC::%s: dumping current sync-gen history for sync %i\n`
- `AppleMSGKextEPICUserClient::%s: Output payload size %d didn't match the expected size %d\n`
- `AppleMSGKextEPIC::%s: probe()\n`
- `AppleMSGKextEPIC::%s: dumping new config for sync_id: %u\n`
- `AppleMSGKextEPICUserClient::%s: msg_log_always test\n`
- `AppleMSGKextEPIC::%s: Applied %d remote configurations\n\n`
- `AppleMSGKextEPIC::%s: wdt=0x%llx\n\n`
- `AppleMSGKextEPIC::%s: There are no handles to be released\n`
- `AppleMSGKextEPIC::%s: AppleMSG Potentially Fatal (%u): Inter-SOC GTB skew is too large (latency to Bora: %lli)\n`
- `AppleMSGKextEPIC::%s: Disabling GTB watchdog during sleep\n`
- `AppleMSGKextEPIC::%s: syncStop sync_id %u retcode %x\n`
- `AppleMSGKextEPIC::%s: Thread waiting on bora response was awakened\n`
- `AppleMSGKextEPIC::%s: AppleMSGKextEPIC's desired power state set to off in response to demand\n\n`
- `AppleMSGKextEPIC::%s: loadConfigsStartSynchronous retcode %x\n`
- `AppleMSGKextEPIC::%s: AppleMSG Potentially Fatal (%u): Failed to handle incoming AFK Report Packet!\n`
- `AppleMSGKextEPIC::%s: stop()\n`
- `AppleMSGKextEPIC::%s: entry\n`
- `AppleMSGKextEPIC::%s: msg_log_info test\n`
- `AppleMSGKextEPIC::%s: start\n`
- `AppleMSGKextEPIC::%s: response:time=%llu\n`
- `AppleMSGKextEPIC::%s: Bora-less wake feature enabled for MSG\n\n`
- `AppleMSGKextEPICUserClient::%s: msg_log_info test\n`
- `AppleMSGKextEPIC::%s: dumping init config for sync id %u\n`
- `AppleMSGKextEPIC::%s: WARNING: sw sync id %llu can't be mapped to hw sync id, skipping it's config tracing\n`
- `AppleMSGKextEPICUserClient::%s: msg_log_debug test\n`
- `AppleMSGKextEPIC::%s: entry for state: %lu\n`
- `AppleMSGKextEPICUserClient: AssertMacros: %s, %s file: %s, line: %d, value: %ld\n\n`
- `AppleMSGKextEPIC::%s: AppleMSG Potentially Fatal (%u): Inter-SOC GTB skew is too large (latency to Staten: %lli)\n`
- `AppleMSGKextEPIC::%s: Bora-less wake feature NOT enabled for MSG\n\n`
- `AppleMSGKextEPIC::%s: Response recieved, retcode:0x%x timestamp:%llu, payloadSize:%zu\n`
- `AppleMSGKextEPIC::%s: Unknown packet type!\n`
- `AppleMSGKextEPIC::%s: AppleMSGKextEPIC's desired power state set to on in response to demand\n\n`
- `AppleMSGKextEPIC::%s: Enqueueing ET got an error: 0x%x\n`
- `AppleMSGKextEPIC::%s: done\n`

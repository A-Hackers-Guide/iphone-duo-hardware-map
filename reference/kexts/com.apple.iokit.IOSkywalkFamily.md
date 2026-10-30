# `com.apple.iokit.IOSkywalkFamily`

- Name: IOSkywalkFamily
- Version: `1.0`
- UUID: `A2F22337-4D51-3312-A919-FFDF1826BA74`
- Source version: `598.0.0.0.0`
- Depends on: [`com.apple.driver.mDNSOffloadUserClient-Embedded`](com.apple.driver.mDNSOffloadUserClient-Embedded.md) 1.0.0d6, [`com.apple.iokit.IONetworkingFamily`](com.apple.iokit.IONetworkingFamily.md) 3.2, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 15.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 15.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 15.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 15.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 15.0.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 15.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (3) [KC]

### IOSkywalkKernelPipeBSDClient
- `CFBundleIdentifier`: `com.apple.iokit.IOSkywalkFamily`
- `IOClass`: `IOSkywalkKernelPipeBSDClient`
- `IOPersonalityPublisher`: `com.apple.iokit.IOSkywalkFamily`
- `IOProviderClass`: `IOSkywalkInterface`
- `IOResourceMatch`: `IOBSD`

### IOSkywalkLegacyEthernet
- `CFBundleIdentifier`: `com.apple.iokit.IOSkywalkFamily`
- `IOClass`: `IOSkywalkLegacyEthernet`
- `IOMatchCategory`: `IOSkywalkLegacyEthernet`
- `IOPersonalityPublisher`: `com.apple.iokit.IOSkywalkFamily`
- `IOProviderClass`: `IOSkywalkEthernetInterface`

### IOSkywalkNetworkBSDClient
- `CFBundleIdentifier`: `com.apple.iokit.IOSkywalkFamily`
- `IOClass`: `IOSkywalkNetworkBSDClient`
- `IOPersonalityPublisher`: `com.apple.iokit.IOSkywalkFamily`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOSkywalkNetworkInterface`
- `IOResourceMatch`: `IOBSD`


## C++ classes (47) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOSkywalkBSDClient` | 0xe8 | IOService → IORegistryEntry |
| `IOSkywalkCloneableNetworkPacket` | 0x90 | IOSkywalkNetworkPacket → IOSkywalkPacket → IOCommand |
| `IOSkywalkController` | 0x98 | IOService → IORegistryEntry |
| `IOSkywalkEthernetInterface` | 0x120 | IOSkywalkNetworkInterface → IOSkywalkInterface → IOService → IORegistryEntry |
| `IOSkywalkInterface` | 0xb0 | IOService → IORegistryEntry |
| `IOSkywalkKernelPipeBSDClient` | 0xf0 | IOSkywalkBSDClient → IOService → IORegistryEntry |
| `IOSkywalkLegacyEthernet` | 0x130 | IOEthernetController → IONetworkController → IOService → IORegistryEntry |
| `IOSkywalkLegacyEthernetInterface` | 0x160 | IOEthernetInterface → IONetworkInterface → IOService → IORegistryEntry |
| `IOSkywalkLogicalLink` | 0x30 |  |
| `IOSkywalkMemorySegment` | 0x78 |  |
| `IOSkywalkNetworkBSDClient` | 0x150 | IOSkywalkBSDClient → IOService → IORegistryEntry |
| `IOSkywalkNetworkController` | 0x98 | IOSkywalkController → IOService → IORegistryEntry |
| `IOSkywalkNetworkInterface` | 0xe0 | IOSkywalkInterface → IOService → IORegistryEntry |
| `IOSkywalkNetworkKDPPoller` | 0x10 |  |
| `IOSkywalkNetworkNotificationHelper` | 0x20 |  |
| `IOSkywalkNetworkPacket` | 0x78 | IOSkywalkPacket → IOCommand |
| `IOSkywalkPacket` | 0x70 | IOCommand |
| `IOSkywalkPacketBuffer` | 0x90 | IOCommand |
| `IOSkywalkPacketBufferPool` | 0xc0 |  |
| `IOSkywalkPacketPoller` | 0x130 | IOTimerEventSource → IOEventSource |
| `IOSkywalkPacketQueue` | 0xd8 | IOEventSource |
| `IOSkywalkQueueSet` | 0x80 |  |
| `IOSkywalkRxCompletionQueue` | 0x138 | IOSkywalkPacketQueue → IOEventSource |
| `IOSkywalkRxSubmissionQueue` | 0x150 | IOSkywalkPacketQueue → IOEventSource |
| `IOSkywalkStatisticsReporter` | 0xa0 | IOSimpleReporter → IOReporter |
| `IOSkywalkTxCompletionQueue` | 0x138 | IOSkywalkPacketQueue → IOEventSource |
| `IOSkywalkTxSubmissionQueue` | 0x168 | IOSkywalkPacketQueue → IOEventSource |
| `IOUserNetworkEthernet` | 0x1b0 | IOSkywalkEthernetInterface → IOSkywalkNetworkInterface → IOSkywalkInterface → IOService → IORegistryEntry |
| `IOUserNetworkLogicalLink` | 0x30 | IOSkywalkLogicalLink |
| `IOUserNetworkMemorySegment` | 0x90 | IOSkywalkMemorySegment |
| `IOUserNetworkPacket` | 0x90 | IOSkywalkCloneableNetworkPacket → IOSkywalkNetworkPacket → IOSkywalkPacket → IOCommand |
| `IOUserNetworkPacketBufferPool` | 0xd0 | IOSkywalkPacketBufferPool |
| `IOUserNetworkPacketQueue` | 0x108 | IOSkywalkPacketQueue → IOEventSource |
| `IOUserNetworkPacketQueueCompat` | 0x108 | IOSkywalkPacketQueue → IOEventSource |
| `IOUserNetworkQueueSet` | 0x80 | IOSkywalkQueueSet |
| `IOUserNetworkRxCompletionQueue` | 0x130 | IOUserNetworkPacketQueue → IOSkywalkPacketQueue → IOEventSource |
| `IOUserNetworkRxCompletionQueueCompat` | 0x130 | IOUserNetworkPacketQueueCompat → IOSkywalkPacketQueue → IOEventSource |
| `IOUserNetworkRxSubmissionQueue` | 0x140 | IOUserNetworkPacketQueue → IOSkywalkPacketQueue → IOEventSource |
| `IOUserNetworkRxSubmissionQueueCompat` | 0x138 | IOUserNetworkPacketQueueCompat → IOSkywalkPacketQueue → IOEventSource |
| `IOUserNetworkTxCompletionQueue` | 0x128 | IOUserNetworkPacketQueue → IOSkywalkPacketQueue → IOEventSource |
| `IOUserNetworkTxCompletionQueueCompat` | 0x120 | IOUserNetworkPacketQueueCompat → IOSkywalkPacketQueue → IOEventSource |
| `IOUserNetworkTxSubmissionQueue` | 0x178 | IOUserNetworkPacketQueue → IOSkywalkPacketQueue → IOEventSource |
| `IOUserNetworkTxSubmissionQueueCompat` | 0x178 | IOUserNetworkPacketQueueCompat → IOSkywalkPacketQueue → IOEventSource |
| `IOUserNetworkWLAN` | 0x208 | IOUserNetworkEthernet → IOSkywalkEthernetInterface → IOSkywalkNetworkInterface → IOSkywalkInterface → IOService → IORegistryEntry |
| `OSAction_IOUserNetworkEthernet__DataAvailable` | 0x20 | OSAction |
| `OSAction_IOUserNetworkEthernet__RxSQDataAvailable` | 0x20 | OSAction |
| `OSAction_IOUserNetworkEthernet__TxSQDataAvailable` | 0x20 | OSAction |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00005e10 off=0x00a565b0-0x00a5c3c0 addr=0xfffffe0007a5a5b0-0xfffffe0007a603c0 r--/r--   __TEXT            
	sz=0x00001d8e off=0x00a56cc8-0x00a58a56 addr=0xfffffe0007a5acc8-0xfffffe0007a5ca56               __TEXT.__cstring          (CstringLiterals)
	sz=0x00003960 off=0x00a58a60-0x00a5c3c0 addr=0xfffffe0007a5ca60-0xfffffe0007a603c0               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0004207c off=0x033856a0-0x033c771c addr=0xfffffe000a3896a0-0xfffffe000a3cb71c r-x/r-x   __TEXT_EXEC       
	sz=0x00040b1c off=0x033856a0-0x033c61bc addr=0xfffffe000a3896a0-0xfffffe000a3ca1bc          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00001560 off=0x033c61bc-0x033c771c addr=0xfffffe000a3ca1bc-0xfffffe000a3cb71c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000924 off=0x04a15e78-0x04a1679c addr=0xfffffe000ba19e78-0xfffffe000ba1a79c rw-/rw-   __DATA            
	sz=0x00000110 off=0x04a15e78-0x04a15f88 addr=0xfffffe000ba19e78-0xfffffe000ba19f88               __DATA.__data             
	sz=0x00000778 off=0x00000000-0x00000778 addr=0xfffffe000ba19f88-0xfffffe000ba1a700               __DATA.__common           (Zerofill)
	sz=0x0000009c off=0x00000000-0x0000009c addr=0xfffffe000ba1a700-0xfffffe000ba1a79c               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x0000c9a0 off=0x013df8a8-0x013ec248 addr=0xfffffe00083e38a8-0xfffffe00083f0248 rw-/rw-   __DATA_CONST      
	sz=0x00000158 off=0x013df8a8-0x013dfa00 addr=0xfffffe00083e38a8-0xfffffe00083e3a00         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000158 off=0x013dfa00-0x013dfb58 addr=0xfffffe00083e3a00-0xfffffe00083e3b58         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00009ac8 off=0x013dfb58-0x013e9620 addr=0xfffffe00083e3b58-0xfffffe00083ed620         __DATA_CONST.__const            
	sz=0x00001880 off=0x013e9620-0x013eaea0 addr=0xfffffe00083ed620-0xfffffe00083eeea0         __DATA_CONST.__kalloc_type      
	sz=0x00000780 off=0x013eaea0-0x013eb620 addr=0xfffffe00083eeea0-0xfffffe00083ef620         __DATA_CONST.__kalloc_var       
	sz=0x00000ab0 off=0x013eb620-0x013ec0d0 addr=0xfffffe00083ef620-0xfffffe00083f00d0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000168 off=0x013ec0d0-0x013ec238 addr=0xfffffe00083f00d0-0xfffffe00083f0238         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000010 off=0x013ec238-0x013ec248 addr=0xfffffe00083f0238-0xfffffe00083f0248         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 729 at 0x04af7158
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     A2F22337-4D51-3312-A919-FFDF1826BA74
008: LC_SOURCE_VERSION           598.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac4a70 size=0xb38
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `IOSkywalkFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IOSkywalkFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOSkywalkFamily`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2022 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Network-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOSkywalkFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894959184`
- `_PrelinkExecutableRelativePath`: `IOSkywalkFamily`
- `_PrelinkExecutableSize`: `348496`
- `_PrelinkExecutableSourceAddr`: `-2198894959184`
- `_PrelinkKmodInfo`: `-2198828114312`

## Strings (297) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `Request Dequeue Sync Path`
- `site.IOUserNetworkPacketBufferPool`
- `root`
- `iosk_bt_fix_enable`
- `Segment Prepare Max Retries`
- `Doorbell Async Path`
- `IOSkywalkNetworkNotificationHelper`
- `221212`
- `site.IOUserNetworkRxCompletionQueue`
- `IOUserNetworkRxSubmissionQueue`
- `\"%s: unknown queue type %d\" @%s:%d`
- `Non Doorbell Path`
- `site.PoolStatistics`
- `site.IOSkywalkCloneableNetworkPacket`
- `%s %02x `
- `121112111111111111222222221111111112222`
- `12111112122212121111111112222111211211121122`
- `IOUserServiceProperties`
- `Non Doorbell Path Early Return`
- `IOClassNameOverride`
- `IOReportLegendPublic`
- `121112111111111111222222221112111`
- ` Service class 0x%x`
- `121112222221111111111112`
- `IOSkywalkPacketQueue`
- `site.IOSkywalkEthernetInterface`
- `DataQueue Enqueue Errors`
- `IOInterfaceNamePrefix`
- `site.IOUserNetworkPacketQueue`
- `IOUserNetworkRxSubmissionQueueCompat`
- `Segment Ctor Count`
- `12221122121122121111`
- `en`
- `site.IOSkywalkNetworkController`
- `Doorbell Path`
- `IOBuiltin`
- `iosk_tx_sub_pkt_threshold`
- `Dequeue Throttled`
- `IOSkywalkStatisticsReporter`
- `IOSkywalkRxSubmissionQueue`
- `Buffer Size`
- `v24@?0^v8Q16`
- `121111121222121211111111222222`
- `IOSkywalkNetworkBSDClient.cpp`
- `Zero EQ By Driver`
- `IOSkywalkKernelPipeBSDClient`
- `site.IOSkywalkEthernetInterfaceVars`
- `21000000000000002000000000000000`
- `12111222222111111111111212`
- `IOUserNetworkMemorySegment`
- `IOUSBHostDevice`
- `AppleUSBDevice`
- `%s%u`
- `1212222`
- `site.IOSkywalkTxCompletionQueue`
- `site.IOUserNetworkMemorySegment`
- `IOSkywalkInterface`
- `%s.%s`
- `121112111111111111222222221112111122121`
- `site.IOSkywalkABFS`
- `IOSkywalkPacket`
- `IOSkywalkCloneableNetworkPacket`
- `site.IOSkywalkQueueSet *`
- `Partial Dequeue By Driver`
- `site.kern_nexus_netif_llink_qset_init`
- `iosk_debug`
- `IOInterfaceName`
- `IOSkywalkPacketBufferPool.cpp`
- `2121`
- `Request Dequeue Async Path`
- `1211111111222222`
- `site.IOUserNetworkTxSubmissionQueue`
- `12111112122212121111111122222`
- `121112111111111111222222221112111112`
- `Dequeue Throttled Max Time`
- `User TX Submission Queue`
- `IOBSD`
- `Segment Size`
- `site.IOSkywalkNetworkPacket`
- `1211`
- `site.OSAction_IOUserNetworkEthernet__DataAvailable`
- `%s\n`
- `\"default packetCompletion()\" @%s:%d`
- `Pkt Cnt`
- `22222212222222222222222222222222222222`
- `site.IOSkywalkNetworkSlidingLookupTable::Entry`
- `121111121222121211111111222221111111222222`
- `site.IOSkywalkPacket`
- `IOSkywalkMemorySegment`
- `site.IOUserNetworkTxCompletionQueueCompat`
- `site.Packet`
- `site.IOUserNetworkEthernet`
- `site.IOSkywalkLegacyEthernetInterface`
- `Queue State`
- `site.IOSkywalkLogicalLink`
- `%02X%02X%02X%02X%02X%02X`
- `IOSkywalkQueueSet`
- `site.IOSkywalkPacketQueue *`
- `IOPCIDevice`
- `site.IOSkywalkStatisticsReporter`
- `site.IOSkywalkPacketPoller`
- `1211121111111111112222222211121111112`
- `Service class 0x%x`
- `TX Submission Queue`
- `Doorbell Path Early Return`
- `12111112122212121111111221211111111111`
- `IOSkywalkBSDClient.cpp`
- `iosk_poll_interval`
- `\"IOSkywalkNetworkBSDClient: not on work loop\" @%s:%d`
- `Pool`
- `site.IOSkywalkNetworkKDPPoller`
- `IODeferBSDAttach`
- `Returned Packets`
- `Buffer Count`
- `IOSkywalkNetworkPacket`
- `121112111111111111222222221111111111112222222`
- `IOServiceDEXTEntitlements`
- `IOUserNetworkTxSubmissionQueue`
- `IOSkywalkRxCompletionQueue`
- `iosk_doorbell_limit`
- `site.IOUserNetworkPacketQueueCompat`
- `Packet Buffer Pool`
- `site.OSAction_IOUserNetworkEthernet__TxSQDataAvailable`
- `IOSkywalkBSDClient`
- `IOUserNetworkRxCompletionQueueCompat`
- `Pkt Cnt Max`
- `kdp_match_mac`
- `IOUserNetworkRxCompletionQueue`
- `site.IOSkywalkKernelPipeBSDClient`
- `v24@?0r^v8Q16`
- `TX Completion Queue`
- `OSAction_IOUserNetworkEthernet__RxSQDataAvailable`
- `IOSkywalkNexusDomainProvider`
- `IOUserNetworkPacketQueueCompat`
- `\"createSegmentBuffers failed\" @%s:%d`
- `Pool Flags`
- `1211111212221212111111121112`
- `DQ Action`
- `121112111111111111222222221111111122222`
- `IOSkywalkLegacyEthernet`
- `IOMACAddress`
- `Pool Allocation Retries`
- `Zero DQ By Driver`
- `1211121111111111112222222211121111111222`
- `IOUserNetworkTxSubmissionQueueCompat`
- `Partial Dequeue By AQM`
- `1`
- `Packet Completion Path`
- `IOSkywalkEthernetInterface`
- `IOUserNetworkLogicalLink`
- `site.IOUserNetworkTxCompletionQueue`
- `Capacity`
- `%s%sQueue ID %u`
- `12111211112111111111122222222222222222`
- `built-in`
- `iosk_abfs_enable`
- `Dequeue Errors`
- `\"%s: unknown packet type %d\" @%s:%d`
- `121112111111111111222222221111111112222222`
- `iosk_tx_sub_timeout`
- `121111121222121211111112111212221111`
- `site.OSAction_IOUserNetworkEthernet__RxSQDataAvailable`
- `Segment Prepare Error Code`
- `12111111112222`
- `IOSkywalkPacketBuffer`
- `RX Submission Queue`
- `IOUserNetworkQueueSet`
- `site.IOSkywalkInterface`
- `12111211111111111122222222111211111112221222212`
- `site.IOSkywalkPacketTable`
- `1211111212221212111`
- `Pool Allocation Errors`
- `site.IOSkywalkPacket *`
- `\"should not be called\" @%s:%d`
- `1211111212221212111111`
- `IOReportLegend`
- `site.IOSkywalkMemorySegment`
- `site.IOUserNetworkPacket`
- `Dequeue Count`
- `site.IOSkywalkPacketBufferPool`
- `iosk_abfs_hysteresis_time`
- `IOSkywalkNexusUUID`
- `WakeOnMagicPacket`
- `121111111122221121`
- `site.IOUserNetworkRxSubmissionQueue`
- `site.IOSkywalkController`
- `site.IOUserNetworkRxSubmissionQueueCompat`
- `IOSkywalkNetworkInterface`
- `IOUserNetworkEthernet`
- `Non Doorbell Path Pkt Cnt`
- `site.IOSkywalkLegacyEthernet`
- `User TX Completion Queue`
- `site.IOSkywalkRxSubmissionQueue`
- `EQ Action`
- `IOUserNetworkPacketQueue`
- `HiddenInterface`
- `IOLinkStatus`
- `IOSkywalkLegacyEthernetInterface`
- `BSD Name`
- `site.kern_packet_t`
- `121111111111111222`
- `Segment Prepare Errors`
- `12111112122212121111111211121222111111112122222222222222222222221`
- `QSet ID 0x%llx, `
- `Request DQ Sync Path`
- `IOSkywalkNetworkController`
- `site.IOUserNetworkLogicalLink`
- `site.IOSkywalkInterfaceVars`
- `Statistics`
- `site.IOUserNetworkRxCompletionQueueCompat`
- `Max Fragments`
- `Submission Packets`
- `IOSkywalkPacketPoller.cpp`
- `121111111211122221`
- `Pool Allocation Max Retries`
- `121112111111111111222222221`
- `Queue Full Count`
- `site.IOSkywalkNetworkNotificationHelper`
- `IOUserNetworkPacketBufferPool`
- `User RX Submission Queue`
- `IOSkywalkNetworkNexusDomainProvider`
- `User RX Completion Queue`
- `IOSkywalkPacketBufferPool`
- `\"default bufferCompletion()\" @%s:%d`
- `222222122222222222222222222222222`
- `IOSkywalkTxSubmissionQueue`
- `site.IOUserNetworkQueueSet`
- `IOSkywalkTxCompletionQueue`
- `IOInterfaceType`
- `IOSkywalkPacketQueue.cpp`
- `Dequeue Action`
- `site.IOSkywalkQueueSet`
- `IOSkywalkController`
- `Dequeued Packets`
- `Segment Count`
- `Request EQ Sync Path`
- `WARNING: using bogus hardcoded station address\n`
- `OSAction_IOUserNetworkEthernet__TxSQDataAvailable`
- `IOSkywalkEthernetVLANID`
- `Enabled`
- `Doorbell Path Pkt Cnt`
- `0x%04x:`
- `IOSkywalkLogicalLink`
- `IO80211Controller`
- `\"%s: segment prepare error 0x%x\" @%s:%d`
- `site.IOSkywalkPacketQueue`
- `v16@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8`
- `121`
- `site.IOSkywalkBSDClient`
- `site.IOSkywalkNetworkBSDClient`
- `121111111122221`
- `site.IOSkywalkNetworkInterface`
- `site._IOSkywalkPacketPollerParameters`
- `kdp_match_name`
- `iosk_abfs_min_limit`
- `Dequeue Depletions`
- `site.IOSkywalkPacketBuffer *`
- `1221`
- `Request DQ Async Path`
- `Segment Dtor Count`
- `site.IOSkywalkNetworkInterfaceVars`
- `site.IOSkywalkTxSubmissionQueue`
- `12111211111111111122222222111211111122`
- `site.IOSkywalkPacketBuffer`
- `I/F %s, `
- `1111112222211`
- `com.apple.developer.driverkit.family.networking`
- `IOUserNetworkPacketBufferPool_kext.cpp`
- `IOUserNetworkTxCompletionQueue`
- `B16@?0^{OSObject=^^?i}8`
- `site.RegistrationInfo`
- `121111111211122`
- `12`
- `IOUserNetworkPacket`
- `IOSkywalkNetworkBSDClient`
- `Packet Count`
- `site.QueueStatistics`
- `IOUserNetworkTxCompletionQueueCompat`
- `RX Completion Queue`
- `IOSkywalkPacketPoller`
- `\"poller disabled from callback\" @%s:%d`
- `USBPortType`
- `IOInterfaceUnit`
- `site.IOSkywalkRxCompletionQueue`
- `Request EQ Async Path`
- `site.IOSkywalkNetworkSlidingLookupTable`
- `site.IOUserNetworkPacketQueue *`
- `OSAction_IOUserNetworkEthernet__DataAvailable`
- `121112`
- `IOSkywalkNetworkKDPPoller`
- `121111121222121211111112111212221111111121222222222222`
- `IOPMResetPowerStateOnWake`
- `site.IOUserNetworkTxSubmissionQueueCompat`
- `IOUserNetworkWLAN`
- `site.IOUserNetworkWLAN`
- `site.kern_nexus_netif_llink_init`
- `Queue Flags`

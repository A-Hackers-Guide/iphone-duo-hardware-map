# `com.apple.driver.AppleFirmwareKit`

- Name: AppleFirmwareKit
- Version: `1`
- UUID: `5DA6467B-4FA9-3669-A528-5976CF12A484`
- Source version: `743.40.4.0.0`
- Depends on: [`com.apple.driver.AppleA7IOP`](com.apple.driver.AppleA7IOP.md) 1.0.0, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleFirmwareUpdateKext`](com.apple.driver.AppleFirmwareUpdateKext.md) 1.0.0, [`com.apple.driver.AppleSMC`](com.apple.driver.AppleSMC.md) 1.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0.0, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 14.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0.0b2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (11) [KC]

### AFKEchoTestEPIC
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareKit`
- `IOClass`: `AFKEchoTestEPIC`
- `IONameMatch`:
  - `ap_echo-test`
- `IOPersonalityPublisher`: `com.apple.driver.AppleFirmwareKit`
- `IOProviderClass`: `AFKEndpointInterface`
- `buffer-increment`: `9`
- `buffer-size`: `100`
- `interval`: `5000000`
- `perf-test-iterations`: `100`
- `send-command`: `True`

### AFKEndpointInterfaceRelay
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareKit`
- `IOClass`: `AFKEndpointInterfaceRelay`
- `IOPersonalityPublisher`: `com.apple.driver.AppleFirmwareKit`
- `IOPropertyMatch`:
  - `EPIRelaySupport`: `True`
- `IOProviderClass`: `AFKEndpointInterface`

### AFKIOServiceClient
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareKit`
- `IOClass`: `AFKIOServiceClient`
- `IONameMatch`: `afk-io-service-client`
- `IOPersonalityPublisher`: `com.apple.driver.AppleFirmwareKit`
- `IOProviderClass`: `AFKEndpointInterface`

### AFKLocalMemoryDescriptorManager
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareKit`
- `IOClass`: `AFKLocalMemoryDescriptorManager`
- `IOPersonalityPublisher`: `com.apple.driver.AppleFirmwareKit`
- `IOPropertyMatch`:
  - `md-allocator`: `md-al-remote`
- `IOProviderClass`: `AFKEndpointInterface`

### AFKRemoteSMCClient
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareKit`
- `IOClass`: `AFKRemoteSMCClient`
- `IONameMatch`: `afk-smc-client`
- `IOPersonalityPublisher`: `com.apple.driver.AppleFirmwareKit`
- `IOProviderClass`: `AFKEndpointInterface`

### AFKResource
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareKit`
- `IOClass`: `AFKResource`
- `IOMatchCategory`: `AFKResource`
- `IOPersonalityPublisher`: `com.apple.driver.AppleFirmwareKit`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOBSD`
- `IOUserClientClass`: `AFKResourceUserClient`

### AFKSharedMemoryMapServer
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareKit`
- `IOClass`: `AFKSharedMemoryMapServer`
- `IONameMatch`:
  - `afk-shmem-registry`
  - `afk-shmem-test-registry`
- `IOPersonalityPublisher`: `com.apple.driver.AppleFirmwareKit`
- `IOProviderClass`: `AFKEndpointInterface`

### AFKSharedMemoryResource
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareKit`
- `IOClass`: `AFKSharedMemoryResource`
- `IOMatchCategory`: `AFKSharedMemoryResource`
- `IOPersonalityPublisher`: `com.apple.driver.AppleFirmwareKit`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOBSD`

### AFKTBTestClient
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareKit`
- `IOClass`: `AFKTBTestClient`
- `IONameMatch`: `tb-test-server-ep`
- `IOPersonalityPublisher`: `com.apple.driver.AppleFirmwareKit`
- `IOProviderClass`: `AFKTightbeamEndpoint`

### AFKTBTestServer
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareKit`
- `IOClass`: `AFKTBTestServer`
- `IONameMatch`: `tb-test-client-ep`
- `IOPersonalityPublisher`: `com.apple.driver.AppleFirmwareKit`
- `IOProviderClass`: `AFKTightbeamEndpoint`

### AFKTightbeamEndpoint
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareKit`
- `IOClass`: `AFKTightbeamEndpoint`
- `IOPersonalityPublisher`: `com.apple.driver.AppleFirmwareKit`
- `IOPropertyMatch`:
  - `KEXTTBSupport`: `True`
- `IOProviderClass`: `AFKEndpointInterface`


## C++ classes (57) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AFKACIPCEndpoint` | 0x1b8 | AFKEPKextV2 → AFKEPKextBaseV2 → IOService → IORegistryEntry |
| `AFKACIPCMemoryDescriptorManager` | 0xc0 | AFKMemoryDescriptorManagerBase → AFKMemoryDescriptorManager → IOService → IORegistryEntry |
| `AFKAction` | 0x18 |  |
| `AFKAsyncRequestV2` | 0x28 |  |
| `AFKBufferMemoryDescriptor` | 0x20 | AFKMemoryDescriptor |
| `AFKEPCommandAction` | 0x70 | AFKEPPacketAction |
| `AFKEPInterfaceEventSourceV2` | 0x78 | IOEventSource |
| `AFKEPInterfaceKextV2` | 0x1e0 | AFKEndpointInterface_DescriptorBase → AFKEndpointInterface → IOService → IORegistryEntry |
| `AFKEPInterfaceServiceEvent` | 0x30 |  |
| `AFKEPInterfaceServiceKextV2` | 0xd8 | IOService → IORegistryEntry |
| `AFKEPKextBaseV2` | 0x198 | IOService → IORegistryEntry |
| `AFKEPKextV2` | 0x1b8 | AFKEPKextBaseV2 → IOService → IORegistryEntry |
| `AFKEPPacketAction` | 0x50 |  |
| `AFKEPReportAction` | 0x50 | AFKEPPacketAction |
| `AFKEPResponseAction` | 0x68 | AFKEPPacketAction |
| `AFKEndpointInterface` | 0xb0 | IOService → IORegistryEntry |
| `AFKEndpointInterfaceClient` | 0x38 |  |
| `AFKEndpointInterfaceClient_Descriptor` | 0x40 | AFKEndpointInterfaceClient |
| `AFKEndpointInterfaceRelay` | 0x128 | IOService → IORegistryEntry |
| `AFKEndpointInterfaceUserClient` | 0x180 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `AFKEndpointInterface_DescriptorBase` | 0xb8 | AFKEndpointInterface → IOService → IORegistryEntry |
| `AFKIOServiceClient` | 0xd0 | AFKIOServiceClientBase → IOService → IORegistryEntry |
| `AFKIOServiceClientBase` | 0xc0 | IOService → IORegistryEntry |
| `AFKKext2UserEP` | 0x1c0 | AFKEPKextBaseV2 → IOService → IORegistryEntry |
| `AFKLocalMemoryDescriptorManager` | 0xc8 | AFKMemoryDescriptorManagerBase → AFKMemoryDescriptorManager → IOService → IORegistryEntry |
| `AFKMemoryDescriptor` | 0x20 |  |
| `AFKMemoryDescriptorManager` | 0x88 | IOService → IORegistryEntry |
| `AFKMemoryDescriptorManagerBase` | 0xc0 | AFKMemoryDescriptorManager → IOService → IORegistryEntry |
| `AFKMemoryDescriptorManagerUserClient` | 0x108 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `AFKOOBMsgDescriptor` | 0xe8 | IOBufferMemoryDescriptor → IOGeneralMemoryDescriptor → IOMemoryDescriptor |
| `AFKRTBuddyHelper` | 0x38 |  |
| `AFKRemoteSMCClient` | 0xc8 | AFKIOServiceClientBase → IOService → IORegistryEntry |
| `AFKResource` | 0x90 | IOService → IORegistryEntry |
| `AFKResourceKext2UserEPUC` | 0x1a8 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `AFKResourceUserClient` | 0x118 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `AFKSharedDataQueue` | 0x38 | IOSharedDataQueue → IODataQueue |
| `AFKSharedMemoryMapServer` | 0xa8 | IOService → IORegistryEntry |
| `AFKSharedMemoryRegion` | 0xc8 | AFKSharedMemoryRegionBase → IOService → IORegistryEntry |
| `AFKSharedMemoryRegionBase` | 0x88 | IOService → IORegistryEntry |
| `AFKSharedMemoryResource` | 0x88 | IOService → IORegistryEntry |
| `AFKSharedMemoryUserClient` | 0xf0 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `AFKTBTestClient` | 0x98 | IOService → IORegistryEntry |
| `AFKTBTestServer` | 0x98 | IOService → IORegistryEntry |
| `AFKTestSharedMemoryRegion` | 0x90 | AFKSharedMemoryRegionBase → IOService → IORegistryEntry |
| `AFKTightbeamEndpoint` | 0xc0 | IOService → IORegistryEntry |
| `AFKUCTestEndpoint` | 0xe8 | IOService → IORegistryEntry |
| `AFKUCTestEndpointInterface` | 0xb8 | AFKEndpointInterface → IOService → IORegistryEntry |
| `AFKUserDataPipe` | 0x58 |  |
| `AFKWorkloop` | 0x28 |  |
| `AFKiBootSharedMemoryRegion` | 0x90 | AFKSharedMemoryRegionBase → IOService → IORegistryEntry |
| `OSAction_AFKUserDataPipe__HandleCommand` | 0x20 | OSAction |
| `OSAction_AFKUserDataPipe__HandleReport` | 0x20 | OSAction |
| `OSAction_AFKUserDataPipe__HandleResponse` | 0x20 | OSAction |
| `SMEvent` | 0x18 |  |
| `SMMachine` | 0x48 |  |
| `SMState` | 0x28 |  |
| `SMTransition` | 0x38 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000078e9 off=0x0046a1c0-0x00471aa9 addr=0xfffffe000746e1c0-0xfffffe0007475aa9 r--/r--   __TEXT            
	sz=0x000002a8 off=0x0046a8e0-0x0046ab88 addr=0xfffffe000746e8e0-0xfffffe000746eb88               __TEXT.__const            
	sz=0x00005814 off=0x0046ab88-0x0047039c addr=0xfffffe000746eb88-0xfffffe000747439c               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000170d off=0x0047039c-0x00471aa9 addr=0xfffffe000747439c-0xfffffe0007475aa9               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0004e21c off=0x01caded0-0x01cfc0ec addr=0xfffffe0008cb1ed0-0xfffffe0008d000ec r-x/r-x   __TEXT_EXEC       
	sz=0x0004d66c off=0x01caded0-0x01cfb53c addr=0xfffffe0008cb1ed0-0xfffffe0008cff53c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000bb0 off=0x01cfb53c-0x01cfc0ec addr=0xfffffe0008cff53c-0xfffffe0008d000ec          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000ef8 off=0x049411e8-0x049420e0 addr=0xfffffe000b9451e8-0xfffffe000b9460e0 rw-/rw-   __DATA            
	sz=0x000005d0 off=0x049411e8-0x049417b8 addr=0xfffffe000b9451e8-0xfffffe000b9457b8               __DATA.__data             
	sz=0x00000908 off=0x00000000-0x00000908 addr=0xfffffe000b9457b8-0xfffffe000b9460c0               __DATA.__common           (Zerofill)
	sz=0x00000020 off=0x00000000-0x00000020 addr=0xfffffe000b9460c0-0xfffffe000b9460e0               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000140f0 off=0x0109a630-0x010ae720 addr=0xfffffe000809e630-0xfffffe00080b2720 rw-/rw-   __DATA_CONST      
	sz=0x00000140 off=0x0109a630-0x0109a770 addr=0xfffffe000809e630-0xfffffe000809e770         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000140 off=0x0109a770-0x0109a8b0 addr=0xfffffe000809e770-0xfffffe000809e8b0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000119c8 off=0x0109a8b0-0x010ac278 addr=0xfffffe000809e8b0-0xfffffe00080b0278         __DATA_CONST.__const            
	sz=0x00001d80 off=0x010ac278-0x010adff8 addr=0xfffffe00080b0278-0xfffffe00080b1ff8         __DATA_CONST.__kalloc_type      
	sz=0x000005d8 off=0x010adff8-0x010ae5d0 addr=0xfffffe00080b1ff8-0xfffffe00080b25d0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000148 off=0x010ae5d0-0x010ae718 addr=0xfffffe00080b25d0-0xfffffe00080b2718         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x010ae718-0x010ae720 addr=0xfffffe00080b2718-0xfffffe00080b2720         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 415 at 0x04ad9ab0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     5DA6467B-4FA9-3669-A528-5976CF12A484
008: LC_SOURCE_VERSION           743.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9fa98 size=0xce0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleFirmwareKit`
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareKit`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleFirmwareKit`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2018 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleFirmwareKit.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901169728`
- `_PrelinkExecutableRelativePath`: `AppleFirmwareKit`
- `_PrelinkExecutableSize`: `436973`
- `_PrelinkExecutableSourceAddr`: `-2198901169728`
- `_PrelinkKmodInfo`: `-2198828985880`

## Strings (881) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AOP2NAPK`
- `EnsureDescriptorDelivery`
- `termination-events`
- `%c`
- `1211111`
- `\"properties\" @%s:%d`
- `\"me->_descriptor\" @%s:%d`
- `AFKResourceKext2UserEPUC`
- `\"((&_eventQ)->stqh_first == __null)\" @%s:%d`
- `type`
- `assertCnt`
- `\"md\" @%s:%d`
- `AOP2UTTX`
- `1211122`
- `\"0 == _sessionCount\" @%s:%d`
- `\"length <= _capacity\" @%s:%d`
- `\"AFKEPMessage::TypeBuffer == messages[0].type && sizeCheck\" @%s:%d`
- `AFKUCTestEndpoint`
- `\"_workloop->inGate()\" @%s:%d`
- `\"_assertCnt\" @%s:%d`
- `B16@?0^{OSObject=^^?i}8`
- `aop2.aop-test`
- `121111121222121211112`
- `AFKResource`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `site.AFKEndpointInterfaceUserClient`
- `SecP2SMDArrays`
- `B24@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{IONotifier=^^?i}16`
- `virtual bool AFKSharedMemoryUserClient::initWithTask(task_t, void *, UInt32, OSDictionary *)`
- `com.apple.afk.user.endpoint`
- `removedata`
- `enqueueResponse`
- `\"this->_clientWL\" @%s:%d`
- `site.AFKIOServiceClient`
- `handleReport`
- `publish-events`
- `on`
- `md-al-remote`
- `\"_asyncES\" @%s:%d`
- `SMEvent`
- `aop2.bt-data`
- `aop2.ulpn-tbfeth-rx`
- `\"serializer\" @%s:%d`
- `cmds`
- `\"object.get() != __null\" @%s:%d`
- `\"size\" @%s:%d`
- `12111112122212121111111111212111121111111122212111121111`
- `v16@?0r^{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}8`
- `\"entitlement\" @%s:%d`
- `terminate`
- `bora-dcps`
- `\"nullptr != properties\" @%s:%d`
- `RTBuddyOff`
- `pendingShutdown`
- `iop_ringbuffer.h`
- `\"TB_ASSERT: \" \"(server->getdata != ((void*)0)) && \\\"implementation for getData is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `i8@?0`
- `compatible`
- `IOUserClientDefaultLockingSetProperties`
- `enqueued-reports`
- `1121222221112`
- `\"(((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2c2) != rv\" @%s:%d`
- `AppleFirmwareKit_c.c`
- `\"me != nullptr\" @%s:%d`
- `site.AsyncEnqueueMessage`
- `TAOP2STX`
- `\"me->init() == true\" @%s:%d`
- `site.AFKKext2UserEP`
- `enqueueDescriptorGated`
- `queueSize`
- `121111121222121211111111112121111211111111222121111`
- `AOP2GPDB`
- `aop2.asen`
- `AOP2AOPT`
- `\"0 != messenger->remoteSize && 0 != remote_addr\" @%s:%d`
- `aop2.ulpn-tbfeth-tx`
- `aop2.wificsi`
- `KernelRegions`
- `\"context\" @%s:%d`
- `IdleTimeout`
- `assertion-count`
- `\"0 == result\" @%s:%d`
- `AFKEPInterfaceEventSourceV2.cpp`
- `DebugState`
- `AOP2BTDT`
- `\"command->response.result == 0\" @%s:%d`
- `12111112122212121111111112212`
- `AFKEPInterfaceServiceKextV2.cpp`
- `\"!overflow\" @%s:%d`
- `finalize`
- `site.AFKResource`
- `IOReportLegendPublic`
- `AFKIOServiceClient.cpp`
- `\"num\" @%s:%d`
- `1211111212221212111111111111111222211`
- `AOP2ALCT`
- `TX Queue Max Util (%)`
- `\"total_offset >= static_offset\" @%s:%d`
- `\"TB_ASSERT: \" \"(u8__v_decode(msg, &buffer) == TB_ERROR_SUCCESS) && \\\"failed to decode type: UInt8\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `AFKResourceKext2UserEPUC.cpp`
- `UCEPIF1Properties`
- `\"!isInactive()\" @%s:%d`
- `site.AFKEndpointInterfaceClient`
- `DescriptorCallback`
- `NoInterfaces`
- `service`
- `OSAction_AFKUserDataPipe__HandleResponse`
- `aop2.rtp-hr`
- `site.msg_list_entry`
- `AFKUCTestEndpoint.cpp`
- `\"_epicArr\" @%s:%d`
- `\"AFKEPAllocation::maxExtraBuffer >= extraSize\" @%s:%d`
- `AFKMemoryDescriptorManagerBase`
- `site.AFKEPCommandRemote`
- `handleStart`
- `12111112122212121`
- `AFKTBTestServer`
- `site.AFKUCTestEndpointInterface`
- `\"!pending\" @%s:%d`
- `site.IOMemoryMapNode`
- `\"this->_clientWL->inGate()\" @%s:%d`
- `\"prop\" @%s:%d`
- `intRetain`
- `virtual bool AFKSharedMemoryResource::start(IOService *)`
- `max-command-count`
- `publish`
- `AFKLocalMemoryDescriptorManager`
- `AFKMemoryDescriptorImpl.cpp`
- `\"propStr\" @%s:%d`
- `site.ResponseTask`
- `I16@?0^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}8`
- `AFKKext2UserEP.cpp`
- `\"counterIdx < this->_counters.size()\" @%s:%d`
- `role`
- `site.afk_rtbuddy_mem`
- `AOP2MTST`
- `AOP2CCLB`
- `aop2.ap2net_alpha_acipc`
- `\"configuration.get() != __null\" @%s:%d`
- `site.AFKTestSharedMemoryRegion`
- `shutdown`
- `\"_endpoint\" @%s:%d`
- `AOP22RTP`
- `aop2.gps-data.ent`
- `aop2.wificsi.mcache`
- `v12@?0B8`
- `\"((void*)0) != (void*)remote_addr\" @%s:%d`
- `\"TB_ASSERT: \" \"(vErr == TB_ERROR_SUCCESS) && \\\"tb_message_subrange failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `AOP2NARX`
- `createDescriptorInternal`
- `\"_uidGen > 0\" @%s:%d`
- `TokenGeneration`
- `site.SMEvent`
- `AFKEPInterfaceV2.cpp`
- `12111111112`
- `site.AsyncCommandContext`
- `virtual bool AFKTestSharedMemoryRegion::start(IOService *)`
- `AFKEPInterfaceKextV2.cpp`
- `AFKEPKextV2`
- `\"self->_endpointWL->inGate()\" @%s:%d`
- `12122212111122`
- `AFKAction`
- `\"(payload == __null && size == 0) || (payload != __null && size > 0)\" @%s:%d`
- `AFKKext2UserEP`
- `site.AFKACIPCMemoryDescriptorManager`
- `AFKWorkloop`
- `   `
- `\"this->getEndpointWorkloop()->inGate()\" @%s:%d`
- `site.afk_rtbuddy_tp`
- `\"_lockAsyncRequests\" @%s:%d`
- `IOPropertyExistsMatch`
- `\"_assertionCount\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->removedata != ((void*)0)) && \\\"implementation for removeData is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `21`
- `v56@?0{afktb_testkext_getdata__result_s=C(?=I{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})})}8`
- `\"token\" @%s:%d`
- `\"_provider\" @%s:%d`
- `site.DescEntry`
- `site.AFKEPCommandLocal`
- `start`
- `AFKACIPCMemoryDescriptorManager.cpp`
- `\"0 == ret || (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2d7) == ret\" @%s:%d`
- `site.AFKRemoteSMCClient`
- `\"_handleCommandAction == __null\" @%s:%d`
- `AFKiBootSharedMemoryRegion`
- `aop2.relay-ep`
- `AOP2UTRX`
- `com.apple.aop2.ap2net_alpha_shmem.ent`
- `\"size > 0\" @%s:%d`
- `getdata`
- `site.AFKEPInterfaceKextV2Allocation`
- `site.AFKBufferMemoryDescriptor`
- `121`
- `AFKEndpointInterface`
- `md-al-local`
- `\"bufferLen >= capacity * AFK_TAGGED_BUFFER_SIZE_SCALE\" @%s:%d`
- `\"_pipe\" @%s:%d`
- `Ready`
- `%08x: `
- `site.OSAction_AFKUserDataPipe__HandleReport`
- `AFKMCHistory.cpp`
- `aop2.gnss-userland-shm`
- `B8@?0`
- `AFKBufferMemoryDescriptor`
- `OSAction_AFKUserDataPipe__HandleCommand`
- `2nd EPI`
- `SecS2PMDArrays`
- `AOP2UFMX`
- `aop2.ap2net_ccpu_acipc`
- `SharedRegionName`
- `\"_interface\" @%s:%d`
- `v16@?0{afktb_testkext_removedata__result_s=C(?=I)}8`
- `site.AFKACIPCEndpoint`
- `\"command\" @%s:%d`
- `AFKSharedMemoryRegion`
- `interface-entitlements`
- `createDescriptorGated`
- `v60@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInt`
- `AOP2IMU1`
- `AFKEPKextV2.cpp`
- `\"_internalRetain\" @%s:%d`
- `AOP2ASN2`
- `AFKEndpointInterfaceRelay.cpp`
- `\"0 == status || (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2d7) == status\" @%s:%d`
- `entitlement`
- `AOP2GNUL`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `site.AFKResourceKext2UserEPUC`
- `site.afk_mem_uc`
- `AOP2UATX`
- `StaticRegions`
- `site.AFKEndpointInterfaceClient_Descriptor`
- `AFKEP%s`
- `site.AFKEPInterfaceEventSourceV2`
- `\"_handleResponseAction == __null\" @%s:%d`
- `EnsureCommandDelivery`
- `\"_interfaces\" @%s:%d`
- `\"!_internalRetain\" @%s:%d`
- `\"0 == err\" @%s:%d`
- `AFKEPInterfaceEventSourceV2`
- `\"TB_ASSERT: \" \"(server->setdataoneway != ((void*)0)) && \\\"implementation for setDataOneWay is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `121111121222121211`
- `aop.audio`
- `aop2.userland-shm`
- `\"_commandGate.get()\" @%s:%d`
- `md-allocator`
- `\"valid && size <= 4294967295U\" @%s:%d`
- `\"endRange <= _length\" @%s:%d`
- `site.AFKRTBuddyHelper`
- `\"me->payload\" @%s:%d`
- `handleDescriptor`
- `site.AFKSharedMemoryRegionBase`
- `buffer`
- `site.AFKWorkloop`
- `\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `11221212222222222222222222222222222222222222222222222222222222222222`
- `i48@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInt`
- `aop2.motiontest`
- `i24@?0^v8Q16`
- `AFKMemoryDescriptorManagerBase.cpp`
- `aop2.imu_1_100aop2`
- `1`
- `interface-reregister`
- `IOPMPowerOn`
- `AFKMemoryDescriptorManager`
- `OSAction_AFKUserDataPipe__HandleReport`
- `P2SPacketTypes`
- `\"command && commandLength && handler\" @%s:%d`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `site.afktb_testkext__server_s`
- `\"0 != _epicArr->getCount()\" @%s:%d`
- `off`
- `init`
- `\"nullptr != data\" @%s:%d`
- `aop2.ulpn.test.tx.default`
- `112`
- `\"_endpointWL->inGate()\" @%s:%d`
- `site.AFKEPKextV2`
- `\"TB_ASSERT: \" \"(server->setdatawithreturn != ((void*)0)) && \\\"implementation for setDataWithReturn is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `virtual bool AFKiBootSharedMemoryRegion::start(IOService *)`
- `AOPTRUST`
- `aop2.gnss-aop-tx`
- `\"ret\" @%s:%d`
- `virtual bool AFKEPInterfaceKextV2::handleOpen(IOService *, IOOptionBits, void *)`
- `StartupPowerTimeoutSec`
- `\"TB_FATAL: \" \"invalid tag in '[UInt8]' metadata: 0x%x\" @%s:%d`
- `size`
- `\"_clientWL\" @%s:%d`
- `AFKEPResponseAction`
- `EnsureReportDelivery`
- `\"queueDesc\" @%s:%d`
- `bora-dcpl`
- `queue-util`
- `AFKIOServiceClient`
- `name`
- `virtual IOReturn AFKSharedMemoryRegionBase::newUserClient(task_t, void *, UInt32, IOUserClient **)`
- `IOProviderClass`
- `1212221211112`
- `\"managerRole->isEqualTo(thisRole.get())\" @%s:%d`
- `TX Queue Size (bytes)`
- `DescCount`
- `site.SMState`
- `aop2.ulpn.apsd.tx.default`
- `\"_paddr != 0\" @%s:%d`
- `OSBoundedPtr.h`
- `1211111212221212111`
- `\"epic\" @%s:%d`
- `\"rtbuddy\" @%s:%d`
- `112222211112`
- `\"self->_clientWL->inGate()\" @%s:%d`
- `site.afktb_testkext_s`
- `mdMGRs`
- `1111111221211122211112221222112`
- `\"ok\" @%s:%d`
- `aop2.bluetooth-data.ent`
- `com.apple.afk.user`
- `site.AFKEPInterfaceServiceKextV2`
- `site.AFKLocalMemoryDescriptorManager`
- `PriS2PMDArrays`
- `aop2.net-uapsdtx`
- `v20@?0Q8C16`
- `\"_tcList[i]\" @%s:%d`
- `\"entry\" @%s:%d`
- `SpaceAvailableCnt`
- `enqueued-commands`
- `AFKMemoryDescriptor.cpp`
- `aop2.gps-debug`
- `aop2.uapsd-ufindmytx`
- `AFKSharedMemoryMapServer`
- `tail`
- `B32@?0^{SMState=^^?i*@?@?}8^{SMState=^^?i*@?@?}16^{SMEvent=^^?i*}24`
- `AOP2IMU2`
- `IOReturn AFKSharedMemoryUserClient::clientMemoryForTypeGated(UInt32 *, IOOptionBits *, IOMemoryDescriptor **)`
- `\"transport\" @%s:%d`
- `The offset of the pointer inside its valid memory range can't be represented using int32_t`
- `\"oobHdr.rspSize <= this->_oobHdr.rspSize\" @%s:%d`
- `IODeviceTree:/defaults`
- `IOReportLegend`
- `\"threadCall\" @%s:%d`
- `AFKEPKextBaseV2`
- `112222`
- `EPIRelayProps`
- `errs`
- `handleResponse`
- `\"this->_openSent\" @%s:%d`
- `\"this->_client == forClient\" @%s:%d`
- `AFKEndpointInterfaceRelay`
- `aop2.ulpn.test.rx.default`
- `AOP2DM10`
- `\"name\" @%s:%d`
- `com.apple.afk`
- `\"role\" @%s:%d`
- `AFKLocalMemoryDescriptorManager.cpp`
- `v56@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInt`
- `site.AFKiBootSharedMemoryRegion`
- `\"dict\" @%s:%d`
- `AFKTestSharedMemoryRegion.cpp`
- `\"AFKEPMessage::TypeBuffer == messages[0].type\" @%s:%d`
- `capacity`
- `\"notification > AFKEP::NotificationInvalid && notification < AFKEP::NotificationCount\" @%s:%d`
- `112122222`
- `ep-has-desc-mgr`
- `AFKEPInterfaceServiceKextV2`
- `bora-isp`
- `\"valid\" @%s:%d`
- `121112111111112`
- `AOP2GNRX`
- `121111121222121211111111111111211121211111111222`
- `121111121222121211111211112111112221111212111122111122221112`
- `AFKEPV2`
- `I12@?0I8`
- `111212223312`
- `openGated`
- `\"__null != packetBuffer || 0 == packetSize\" @%s:%d`
- `TAOP1CTX`
- `site.AFKSharedMemoryMapServer`
- `IOReturn AFKSharedMemoryUserClient::testMethodGated(void *, IOExternalMethodArguments *)`
- `KEXTTBEPCompanion`
- `default`
- `default-idle-time`
- `site.OSAction_AFKUserDataPipe__HandleCommand`
- `EPIRelayPriToSecDesc`
- `AOP2ASN1`
- `\"paddr\" @%s:%d`
- `KEXTTBInterface`
- `12111112122212121111111111111111111`
- `\"payloadSize == sizeof(AFKMDManagerCreateResponse)\" @%s:%d`
- `site.AFKEndpointInterface`
- `SessionStart`
- `virtual void AFKSharedMemoryMapServer::stop(IOService *)`
- `AFKEndpointInterfaceUserClient.cpp`
- `111`
- `interface-id`
- `enqueueResponse_block_invoke`
- `AFKEPKextBaseV2.cpp`
- `RTBuddySleep`
- `\"self->getEndpointWorkloop()->inGate()\" @%s:%d`
- `EnqueueOptions`
- `site.CommandContextNode`
- `epi-is-desc-mgr`
- `SMTransition`
- `\"NULL != mess\" @%s:%d`
- `afktp_rtbuddy.cpp`
- `AOP2ULSH`
- `AOP2UTFR`
- `aop2.ap2net_beta_acipc`
- `\"0 == _epWl->addEventSource(_epEvSrc.get())\" @%s:%d`
- `UCEPTCCount`
- `interface-name`
- `\"messenger->config.rxQueueLen && messenger->config.txQueueLen\" @%s:%d`
- `site.HandleCommandCall`
- `virtual void AFKSharedMemoryUserClient::stop(IOService *)`
- `AFKSharedDataQueue`
- `assertion-wait-count`
- `site.AFKUserDataPipe`
- `\"TB_FATAL: \" \"invalid error returned from %s\" @%s:%d`
- `getData`
- `\"0 == status || (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2d7) == status || (((signed)((((unsigned)(0x38))&0x3f)<<26))|(((0)&0xfff)<<14)|0x2e3) == status\" @%s:%d`
- `virtual bool AFKSharedMemoryRegion::start(IOService *)`
- `site.AFKEndpointInterface_DescriptorBase`
- `\"_clientCount < 4294967295U\" @%s:%d`
- `matching`
- `AFKMemoryDescriptor`
- `\"STAILQ_EMPTY(&this->_taskQ)\" @%s:%d`
- `\"0 == rv\" @%s:%d`
- `AOP2GPDT`
- `com.apple.aop2.ap2net_beta_shmem.ent`
- `site.AFKEPKextBaseV2`
- `RX Queue Size (bytes)`
- `\"capacity\" @%s:%d`
- `12122`
- `\"TB_FATAL: \" \"invalid result returned from getData\" @%s:%d`
- `\"op < Operation::Count\" @%s:%d`
- `aop2.net-aoptx`
- `\"nameSymbol\" @%s:%d`
- `\"0 == _assertionCount && 0 == _assertionWaitCount\" @%s:%d`
- `\"_secMemory\" @%s:%d`
- `1221122`
- `12212`
- `site.OSAction_AFKUserDataPipe__HandleResponse`
- `1112`
- `access`
- `\"_epEvSrc\" @%s:%d`
- `121111`
- `isBuffer`
- `I16@?0{afktb_testkext_removedata__result_s=C(?=I)}8`
- `AFKTBTestServer.cpp`
- `AFKEndpointInterface.cpp`
- `12111`
- `site.AFKMDListEntry`
- `\"nullptr == this->_out\" @%s:%d`
- `ReadOnly`
- `site.AFKEPPacketAction`
- `12111112122212121111121`
- `1211111212221212111112`
- `site.AFKAsyncRequestV2`
- `v8@?0`
- `\"!getRetainInternal()\" @%s:%d`
- `AFKRTBuddyHelper`
- `AOP2NUTX`
- `AOP2CCAC`
- `AFKSharedMemoryRegion.cpp`
- `IOUserClientDefaultLocking`
- ` `
- `AFKSharedMemoryResource`
- `\"nullptr != payload\" @%s:%d`
- `aop2.ulpn.apsd.rx.default`
- `AFKEPPacketAction`
- `AFKEndpointInterfaceUserClient`
- `\"!this->_published && !this->_openSent\" @%s:%d`
- `\"this->_endpointWL->inGate()\" @%s:%d`
- `EPIRelayAssertPower`
- `\"numBytes <= dst->getCapacity()\" @%s:%d`
- `\"configuration != NULL\" @%s:%d`
- `CommandCallback`
- `notifySpaceAvailable`
- `state`
- `aop2.net-aoprx`
- `com.apple.afk.shmem-user`
- `config`
- `1211`
- `12111112122212121111111111111111111111111111111111111`
- `AFKTBTestClient`
- `\"found\" @%s:%d`
- ` | `
- `AFKEP.cpp`
- `\"this->_queueLock\" @%s:%d`
- `AFKUserDataPipe`
- `AFKRTBuddyHelper.cpp`
- `\"0 == status\" @%s:%d`
- `AFKEndpointInterface_DescriptorBase`
- `?`
- `\"payload && size > 0\" @%s:%d`
- `\"region\" @%s:%d`
- `OOBThreshold`
- `121111121222121211112111112`
- `idleLowPower`
- `site.AFKMemoryDescriptor`
- `Descs`
- `aop2.ap2net_ccpu_loopback`
- `\"interface\" @%s:%d`
- `events`
- `bora-audl`
- `FreeReqs`
- `aop2.imu100aop2`
- `site.AFKSharedMemoryRegion`
- `afksharedmemory`
- `v40@?0i8Q12{span<unsigned char, 18446744073709551615UL>=*Q}20B36`
- `12112122222212132213211121222`
- `enqueued-responses`
- `handled-commands`
- `AFKEPInterfaceServiceEvent`
- `taop2.taop1-client-tx`
- `AFKSharedMemoryRegionBase`
- `AFKUCTestEndpointInterface`
- `v16@?0^{SMEvent=^^?i*}8`
- `SMMachine`
- `%02x `
- `AFKEPCommandContext.cpp`
- `afk_messenger_acipc.c`
- `aop2.asen-motion`
- `aop2.network.aop2apkernel`
- `121111121222121211111111`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `site.AFKTBTestServer`
- `aop2.gnss-shm`
- `virtual bool AFKSharedMemoryUserClient::start(IOService *)`
- `1111`
- `\"0 != status\" @%s:%d`
- `AOP2ALAC`
- `\"memory\" @%s:%d`
- `setdatawithreturn`
- `UCEPIF2Properties`
- `v16@?0^{IOTimerEventSource=^^?i^{IOEventSource}^{OSObject}^?B^{IOWorkLoop}^v^{ExpansionData}^vQ^{ExpansionData}}8`
- `AOP2CSIM`
- `\"!getEndpointWorkloop()->onThread()\" @%s:%d`
- `\"TB_FATAL: \" \"overflow detected when adding\" @%s:%d`
- `AOP2RELY`
- `site.AFKTightbeamEndpoint`
- `AFKEndpointInterfaceClient_Descriptor`
- `default-power-state`
- `\"!iObject->isEqualTo(jObject)\" @%s:%d`
- `AOP2BTAC`
- `AOP2GNTX`
- `visibility`
- `AFKTestSharedMemoryRegion`
- `ReportCallback`
- `site.AFKEPInterfaceServiceEvent`
- `v32@?0^{SMState=^^?i*@?@?}8^{SMState=^^?i*@?@?}16^{SMEvent=^^?i*}24`
- `\"getEndpointWorkloop()->inGate()\" @%s:%d`
- `1211111212221212111111112`
- `site.ReportTask`
- `\"_handleReportAction == __null\" @%s:%d`
- `EPIRelaySecToPriDesc`
- `\"buf != __null\" @%s:%d`
- `AFKACIPCMemoryDescriptorManager`
- `site.AFKOOBMsgDescriptor`
- `AFKIOServiceClientBase`
- `site.afk_messenger_int`
- `aop2.uapsd-ufindmyrx`
- `AOP2PRES`
- `aop2.gnss-aop-rx`
- `UseIOPMStateControl`
- `AFKEPCommandAction`
- `AFKAsyncRequestV2`
- `121111111`
- `\"__builtin_bswap32('IOP ') == magic\" @%s:%d`
- `\"_commandGate\" @%s:%d`
- `site.AFKSharedMemoryUserClient`
- `enqueueCommandSyncGated`
- `handled-reports`
- `\"0 != size\" @%s:%d`
- `\"!epConfig.size || epConfig.txQueueLen+epConfig.rxQueueLen == epConfig.size\" @%s:%d`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `taop2.taop2-server-tx`
- `IOKitDebug`
- `dataQueue`
- `head`
- `121111121222121211111112`
- `AFKRemoteSMCClient`
- `\"nullptr != task\" @%s:%d`
- `PriP2SMDArrays`
- `aop2.net-uapsdrx`
- `aop2.pressure120aop2`
- `SharedRegionSize`
- `\"_epi\" @%s:%d`
- `site.SMMachine`
- `site.PendingState`
- `aop2.icmemory`
- `AFKResourceUserClient`
- `RTBuddyOn`
- `AOP2UTFX`
- `aop2.audio`
- `aop2.ap2net_alpha_control`
- `AFKEPReportAction`
- `site.AFKUCTestEndpoint`
- `\"_mdMgr\" @%s:%d`
- `\"false\" @%s:%d`
- `handleCommand`
- `\"_ep\" @%s:%d`
- `AFKUCTestEndpointInterface.cpp`
- `com.apple.developer.driverkit.transport.afk`
- `terminateReportRecv`
- `v16@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8`
- `12112`
- `AFKEPV2.cpp`
- `rsps`
- `static OSSharedPtr<AFKSharedMemoryRegion> AFKSharedMemoryRegion::create(const OSSymbol *, size_t, uint8_t, OSString *, bool, IOPhysicalAddress)`
- `\"_impl->getUsable()\" @%s:%d`
- `\"!__os_warn_unused(__builtin_add_overflow((offset), (numBytes), (&endRange)))\" @%s:%d`
- `removeData`
- `AOP2ICMM`
- `Size`
- `AFKTightbeamEndpoint`
- `\"packetSize < 4294967295U\" @%s:%d`
- `\"packetSize >= sizeof(PublishReport)\" @%s:%d`
- `bora-dcpr`
- `AFKEPMessage.cpp`
- `site.AFKEndpointInterfaceRelay`
- `OutstandingCmd`
- `12111112122212121111111212`
- `\"nullptr == this->_client\" @%s:%d`
- `\"d->self->getEndpointWorkloop()->inGate()\" @%s:%d`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"failed to wrap packed buffer\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `v28@?0i8{span<unsigned char, 18446744073709551615UL>=*Q}12`
- `\"__null != extraBuffer || 0 == extraSize\" @%s:%d`
- `\"success\" @%s:%d`
- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
- `RTBuddyService`
- `\"_interface.get()\" @%s:%d`
- `IOServiceDEXTEntitlements`
- `121111121222121211111111111111`
- `site.AFKMemoryDescriptorImpl`
- `%s\n`
- `\"this->_pending.size() + messages[0].buffer.size() <= this->_pending.capacity()\" @%s:%d`
- `com.apple.aop2.ap2net_ccpu_shmem.ent`
- `site.AFKTBTestClient`
- `stop`
- `afk`
- `enqueueReport`
- `site.AFKEPInterfaceKextV2`
- `\"_asycRequestES\" @%s:%d`
- `Starting`
- `\"temp\" @%s:%d`
- `I16@?0@?<I@?{afktb_testkext_getdata__result_s=C(?=I{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})})}>8`
- `site.AFKEPReportAction`
- `SessionCount`
- `AFKEPInterfaceKextV2`
- `1212`
- `\"nullptr != command\" @%s:%d`
- `\"!this->_endpointWL->inGate()\" @%s:%d`
- `AOP2GNSS`
- `AFKSharedMemoryMapServer.cpp`
- `1211111212221212112211122`
- `site.AFKEPResponseAction`
- `isOpen`
- `\"!useIOPMStateControl()\" @%s:%d`
- `1211111212221212111111111121211112111111112221211111111`
- `site.AFKIOServiceClientBase`
- `\"%s\" @%s:%d`
- `\"getWorkLoop()->addEventSource(_commandGate.get()) == 0\" @%s:%d`
- `IOReturn AFKEPInterfaceKextV2::assertPowerState()`
- `\"payloadSize == sizeof(AFKMDManagerCreateCommand)\" @%s:%d`
- `length`
- `\"!__os_warn_unused(__builtin_add_overflow((offset), (numBytes), (&endRange))) && endRange <= _length\" @%s:%d`
- `\"messenger->config.allocator\" @%s:%d`
- `I8@?0`
- `\"dst\" @%s:%d`
- `site.AsyncContext`
- `\"!descriptor->_impl->getAssertPower()\" @%s:%d`
- `AFKACIPCEndpoint`
- `11`
- `site.StateTask`
- `afk_messenger_standard.c`
- `S2PPacketTypes`
- `AOP2UARX`
- `site.AFKResourceUserClient`
- `setdataoneway`
- `site.AFKMemoryDescriptorManagerBase`
- `122112`
- `\"this->_pendingStatesLock\" @%s:%d`
- `aop2.ulpn-tbfeth.ent`
- `aop2.dm100aop2`
- `\"result == 0\" @%s:%d`
- `RequiredEntitlement`
- `site.AFKSharedMemoryResource`
- `IOClass`
- `\"epWl\" @%s:%d`
- `I16@?0@?<I@?{afktb_testkext_removedata__result_s=C(?=I)}>8`
- `AOP2NURX`
- `AFKSharedMemoryUserClient`
- `site.AFKSharedDataQueue`
- `AFKOOBMsgDescriptor`
- `\"_endpointWL\" @%s:%d`
- `session-count`
- `CommandTimeoutMS`
- `1221`
- `regs`
- `AOP2CSID`
- `paddr`
- `site.AFKEPCommandAction`
- `IdleLowPower`
- `\"AFKEPInterfaceKextV2::%s: command response timeout (%u ms) on %s, \" \"commandID:%u, EP:%s\" @%s:%d`
- `\"client\" @%s:%d`
- `11122`
- `\"kIOReturnSuccess == status\" @%s:%d`
- `v12@?0I8`
- `virtual void AFKEPInterfaceKextV2::handleClose(IOService *, IOOptionBits)`
- `\"!overflow && newLength <= _capacity\" @%s:%d`
- `\"sizeCheck\" @%s:%d`
- `\"0 == ret\" @%s:%d`
- `\"d->notification != AFKEP::NotificationSendPossible\" @%s:%d`
- `\"options & (1 << 13)\" @%s:%d`
- `IOUserClientEntitlements`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `I24@?0r^{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}8@?<I@?I>16`
- `1212221211`
- `\"_mdMgrNotify\" @%s:%d`
- `1211111212221212111111121`
- `SMState`
- `site.CommandTask`
- `AAPL,phandle`
- `enqueueCommandGated`
- `enqueueTimestamp`
- `\"messages[0].buffer.size() >= sizeof(*header)\" @%s:%d`
- `handled-responses`
- `121111121222121211111111111112211`
- `\"(bool)epConfig.size == (bool)epConfig.buffer\" @%s:%d`
- `afk_messenger_common.c`
- `aop2.gps-data`
- `virtual bool AFKSharedMemoryMapServer::start(IOService *)`
- `\"_clientCount > 0\" @%s:%d`
- `AFKIOServiceClientBase.cpp`
- `\"messenger->state == handlers[i].startState\" @%s:%d`
- `\"ret == 0\" @%s:%d`
- `AFKTBTestClient.cpp`
- `site.AFKAction`
- `v64@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInt`
- `AFKMemoryDescriptorManagerUserClient`
- `\"nullptr != this->storage.data()\" @%s:%d`
- `AFKUserDataPipe_kext.cpp`
- `I56@?0{afktb_testkext_getdata__result_s=C(?=I{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})})}8`
- `11111`
- `i64@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{AFKEndpointInterface=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInt`
- `12111111`
- `\"descriptor->_impl->getUsable()\" @%s:%d`
- `cmdTimeoutTimerAction`
- `\"afk_mem_get_paddr(this->_rspPayload) == oobHdr.rspAddress\" @%s:%d`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`
- `bora-aop`
- `AFK%s`
- `site.AFKMemoryDescriptorManager`
- `site.AFKMemoryDescriptorManagerUserClient`
- `site.SMTransition`
- `AOP2NATX`
- `AFKTightbeamEndpoint.cpp`
- `bora-scdc`
- `control`
- `\"TB_FATAL: \" \"invalid result returned from removeData\" @%s:%d`
- `OutstandingMsg`
- `\"secondaryAddresses\" @%s:%d`
- `IOUserClientClass`
- `AFKEndpointInterfaceClient`
- `DataQueueSize`
- `\"uc\" @%s:%d`
- `RX Queue Max Util (%)`
- `\"endpointService\" @%s:%d`
- `AOP2UFMR`

**[__TEXT.__os_log]**

- `%s(%s:%#llx): AFKEPI base Open failed:0x%llx\n`
- `%s(%s:%#llx): AFKRemoteSMCClient writeKey_rpc(%x):%x\n`
- `[AFKEPInterfaceV2:%p]Unexpected Response (pktLen %zu pktType 0x%x commandID:%i)\n`
- `[AFKEPInterfaceV2] sendOpenReport:0x%x\n`
- `[AFKEPInterfaceV2] sendCloseReport:0x%x\n`
- `%s(%s:%#llx): Change name from %s to %s\n`
- `%s: %s\n`
- `[AFKEPInterfaceV2] sendPublishReport:0x%x\n`
- `%s\n`
- `createEndpoint:0x%x\n`
- `terminateEndpoint\n`
- `%s(%s:%#llx): %s failed: cap:0x%zx\n`
- `%s(%s:%#llx): Unable to find message contextUID %#llx associated with command \n`
- `%s(%s:%#llx): start:0\n`
- `%s(%s:%#llx): %s failed: 0x%x\n`
- `%s(%s:%#llx): multiple opens from client 0x%llx\n`
- `%s(%s:%#llx): init\n`
- `%s(%s:%#llx): provider is not an endpoint interface (%p)\n`
- `_descriptor_nop: type:%#x ts:%#llx descriptorSz:%zu options:%#x\n`
- `%s(%s:%#llx): if:0x%llx inCmd:%d inResp:%d outRepErr:%d outCmdErr:%d\n`
- `%s(%s:%#llx): registerPowerDriver:%x\n`
- `%s: init failed (%p)\n`
- `%s: tp:0x%x\n`
- `%s(%s:%#llx): addEventSource\n`
- `%s(%s:%#llx): createEndpoint:0xx%x\n`
- `sendAsyncResult64:0x%x\n`
- `[%s:%p] Unknown message '%x'\n`
- `failed\n`
- `%s(%s:%#llx): %s: result:0x%x status:0x%x timestamp:%lld outPayloadSize:%x\n\n`
- `%s(%s:%#llx): %s is missing\n`
- `%s(%s:%#llx): %s (type:%lu): 0x%x\n`
- `%s is not entitled\n`
- `[AFKEPInterfaceV2:%p]Enqueue unknown response (result 0x%x)\n`
- `%s: Transport not established (curr %x)\n`
- `%s(%s:%#llx): _workLoop\n`
- `%s(%s:%#llx): %s: 0x%x\n`
- `%s(%s:%#llx): %s: create descriptor failed 0x%x\n`
- `%s(%s:%#llx): AFKEPI openImpl failed:0x%llx\n`
- `%s(%s:%#llx): could not open secondary interface 0x%llx\n`
- `%s(%s:%#llx): afktb_testkext_setdatawithreturn(status):0x%x\n`
- `%s(%s:%#llx): could not open interface 0x%llx\n`
- `%s(%s:%#llx): %s: no mdmgrs\n`
- `%s: unexpected: msg=%016llx cmd: %x\n`
- `%s(%s:%#llx): handleCommandAction SetAbortedHandler 0x%x\n`
- `%s(%s:%#llx): %s: packetType:0x%x reportSize:%zu failed alloc\n`
- `%s(%s:%#llx): enqueueCommand:0x%x (type=%d)\n`
- `%s(%s:%#llx): performCommandSync:0x%x (type=%d)\n`
- `%s(%s:%#llx): %s: packetType:0x%x timestamp:%lld payloadSize:%zu ret:0x%x oob:%d\n\n`
- `%s(%s:%#llx): %s: result:0x%x\n\n`
- `%s(%s:%#llx): All EPICs handleCommand error 0x%x (pkt 0x%x)\n`
- `%s(%s:%#llx): could not open primary interface 0x%llx\n`
- `%s(%s:%#llx): failed to open endpoint interface (%p)\n`
- `%s(%s:%#llx): afktb_testkext_setdatawithreturn:0x%x\n`
- `%s(%s:%#llx): Dropping wait queue that was not delivered to AFKUser\n`
- `%s(%s:%#llx): %s: result:0x%x inPayloadSize:%x\n\n`
- `%s(%s:%#llx): addr:0x%llx len:0x%llx\n`
- `%s(%s:%#llx): AFKSharedMemoryRegion::create failed (%s)\n`
- `%s(%s:%#llx): failed to get RTBuddyService\n`
- `%s(%s:%#llx): no parent entry\n`
- `%s(%s:%#llx): descriptor:NULL (address:0x%llx, size:0x%llx)\n`
- `%s(%s:%#llx): failed to get shared memory configuration from IOP.\n`
- `%s(%s:%#llx): failed to get AppleA7IOPNub\n`
- `%s(%s:%#llx): enqueueAsyncRequest not supported\n\n`
- `%s(%s:%#llx): %s: 0x%llx isEpic:%u\n\n`
- `%s(%s:%#llx): %s: responseSize:0x%x context->getResponseBufferSize():%x\n`
- `%s(%s:%#llx): No phandle on provider id:%#llx\n`
- `%s(%s:%#llx): serializeDebugState: OSDictionary::withCapacity failed\n`
- `_report_nop: type:%#x ts:%#llx sz:%#zx options:%#x\n`
- `%s(%s:%#llx): %s: invalid AFKMDManagerReleaseReport\n`
- `%s(%s:%#llx): %s: payloadSize:%zu failed alloc\n`
- `%s(%s:%#llx): %s: packetType:0x%x timestamp:%lld ret:0x%x\n\n`
- `%s(%s:%#llx): afktb_testkext_removedata:0x%x\n`
- `%s: Message received for deinit'ed client\n`
- `%s(%s:%#llx): Failed to open %s(%s:%#llx)\n`
- `%s(%s:%#llx): createMemoryRegion(node:%#llx)\n`
- `%s(%s:%#llx): slaveNativeMemoryFromIOPPhys: 0x%x\n`
- `%s(%s:%#llx): %s:%d\n`
- `%s(%s:%#llx): Dropping oob msg that was not released by AFKUser\n`
- `%s(%s:%#llx): %s: _powerState:%x\n`
- `%s(%s:%#llx): AFKRemoteSMCClient readPKey_rpc(%x):%x\n`
- `_response_nop: ts:%#llx sz:%#zx\n`
- `%s(%s:%#llx): %s: result:0x%x timestamp:%lld payloadSize:%zu ret:0x%x oob:%d\n\n`
- `%s(%s:%#llx): %s: Interface doesn't support descriptor\n`
- `%s(%s:%#llx): %s: _assertionCount:%u status:%x\n`
- `%s(%s:%#llx): AFKRemoteSMCClient readKey_rpc(%x):%x\n`
- `%s: afk_messenger_int not started (cmd %x)\n`
- `%s(%s:%#llx): Context not found for command\n`
- `%s(%s:%#llx): AFKSharedMemoryRegion::attach failed (%s)\n`
- `%s(%s:%#llx): Unable to find message descriptor for address %#llx\n`
- `%s(%s:%#llx): AFKEPI assertPowerState failed:0x%x\n`
- `%s(%s:%#llx): service:%#llx not parent of node:%#llx\n`
- `%s(%s:%#llx): Unsupported packet type:0x%x\n`
- `createSharedMemoryRegion:0x%x\n`
- `%s(%s:%#llx): enqueueAction(%s:%p):0x%x\n`
- `%s(%s:%#llx): %s: mgruc not found:0x%llx\n`
- `%s(%s:%#llx): AFKSharedMemoryRegion::start failed (%s)\n`
- `%s(%s:%#llx): %s: timestamp:%lld payloadSize:%zu oob:%d\n\n`
- `%s(%s:%#llx): %s is not entitled\n`
- `%s(%s:%#llx): %s: didn't find MD for token:0x%llx\n`
- `[AFKEPInterfaceV2] sendTerminate:0x%x\n`
- `%s(%s:%#llx): _commandGate\n`
- `%s(%s:%#llx): failed to complete shared memory setup.\n`
- `%s(%s:%#llx): failed\n`
- `%s(%s:%#llx): Reregister\n`
- `%s(%s:%#llx): Terminate received for starting interface %u\n`
- `%s(%s:%#llx): open fail 0x%llx\n`
- `%s(%s:%#llx): Dropping context for command not completed by AFKUser\n`
- `%s(%s:%#llx): stop\n\n`
- `%s(%s:%#llx): setProperties_rpc: bad argument\n`
- `_command_nop: type:%#x sz:%#zx options:%#x\n`
- `%s(%s:%#llx): %s\n`
- `%s(%s:%#llx): regData:%u expected:%lu\n`
- `%s(%s:%#llx): afktb_testkext_setdataoneway:0x%x\n`

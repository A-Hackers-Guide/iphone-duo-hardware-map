# `com.apple.iokit.IONetworkingFamily`

- Name: I/O Kit Networking Family
- Version: `3.4`
- UUID: `15906F58-9240-39C2-BF84-20644DB6D0AE`
- Source version: `190.0.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 10.0.0d1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 10.0.0d1, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 10.0.0d1, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 10.0.0d1, [`com.apple.kpi.private`](com.apple.kpi.private.md) 10.0.0d1, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 10.0.0d1

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### IONetworkStack
- `CFBundleIdentifier`: `com.apple.iokit.IONetworkingFamily`
- `IOClass`: `IONetworkStack`
- `IOMatchCategory`: `IONetworkStack`
- `IOPersonalityPublisher`: `com.apple.iokit.IONetworkingFamily`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOBSD`

### Kernel Debugging Driver
- `CFBundleIdentifier`: `com.apple.iokit.IONetworkingFamily`
- `IOClass`: `IOKDP`
- `IOMatchCategory`: `IOKDP`
- `IOPersonalityPublisher`: `com.apple.iokit.IONetworkingFamily`
- `IOProviderClass`: `IOKernelDebugger`


## C++ classes (21) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOBasicOutputQueue` | 0x80 | IOOutputQueue |
| `IOECStateNotifier` | 0x20 |  |
| `IOECTimeSyncHandler` | 0x28 |  |
| `IOEthernetController` | 0x118 | IONetworkController → IOService → IORegistryEntry |
| `IOEthernetInterface` | 0x148 | IONetworkInterface → IOService → IORegistryEntry |
| `IOGatedOutputQueue` | 0x90 | IOBasicOutputQueue → IOOutputQueue |
| `IOKDP` | 0x88 | IOService → IORegistryEntry |
| `IOKernelDebugger` | 0xb8 | IOService → IORegistryEntry |
| `IOMbufBigMemoryCursor` | 0x48 | IOMbufMemoryCursor → IOMemoryCursor |
| `IOMbufLittleMemoryCursor` | 0x48 | IOMbufMemoryCursor → IOMemoryCursor |
| `IOMbufMemoryCursor` | 0x48 | IOMemoryCursor |
| `IOMbufNaturalMemoryCursor` | 0x48 | IOMbufMemoryCursor → IOMemoryCursor |
| `IONetworkController` | 0x110 | IOService → IORegistryEntry |
| `IONetworkData` | 0x50 |  |
| `IONetworkInterface` | 0x110 | IOService → IORegistryEntry |
| `IONetworkMedium` | 0x38 |  |
| `IONetworkStack` | 0xd0 | IOService → IORegistryEntry |
| `IONetworkStackUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |
| `IONetworkUserClient` | 0xf8 | IOUserClient → IOService → IORegistryEntry |
| `IOOutputQueue` | 0x20 |  |
| `IOPacketQueue` | 0x28 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001884 off=0x00a28300-0x00a29b84 addr=0xfffffe0007a2c300-0xfffffe0007a2db84 r--/r--   __TEXT            
	sz=0x00001113 off=0x00a28a18-0x00a29b2b addr=0xfffffe0007a2ca18-0xfffffe0007a2db2b               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000054 off=0x00a29b30-0x00a29b84 addr=0xfffffe0007a2db30-0xfffffe0007a2db84               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0001be68 off=0x032c33f0-0x032df258 addr=0xfffffe000a2c73f0-0xfffffe000a2e3258 r-x/r-x   __TEXT_EXEC       
	sz=0x0001b158 off=0x032c33f0-0x032de548 addr=0xfffffe000a2c73f0-0xfffffe000a2e2548          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000d10 off=0x032de548-0x032df258 addr=0xfffffe000a2e2548-0xfffffe000a2e3258          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000508 off=0x04a13650-0x04a13b58 addr=0xfffffe000ba17650-0xfffffe000ba17b58 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a13650-0x04a13718 addr=0xfffffe000ba17650-0xfffffe000ba17718               __DATA.__data             
	sz=0x000003b8 off=0x00000000-0x000003b8 addr=0xfffffe000ba17718-0xfffffe000ba17ad0               __DATA.__common           (Zerofill)
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000ba17ad0-0xfffffe000ba17b58               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00006760 off=0x013bf568-0x013c5cc8 addr=0xfffffe00083c3568-0xfffffe00083c9cc8 rw-/rw-   __DATA_CONST      
	sz=0x00000060 off=0x013bf568-0x013bf5c8 addr=0xfffffe00083c3568-0xfffffe00083c35c8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000060 off=0x013bf5c8-0x013bf628 addr=0xfffffe00083c35c8-0xfffffe00083c3628         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00005048 off=0x013bf628-0x013c4670 addr=0xfffffe00083c3628-0xfffffe00083c8670         __DATA_CONST.__const            
	sz=0x00000a80 off=0x013c4670-0x013c50f0 addr=0xfffffe00083c8670-0xfffffe00083c90f0         __DATA_CONST.__kalloc_type      
	sz=0x00000230 off=0x013c50f0-0x013c5320 addr=0xfffffe00083c90f0-0xfffffe00083c9320         __DATA_CONST.__kalloc_var       
	sz=0x0000021c off=0x013c5320-0x013c553c addr=0xfffffe00083c9320-0xfffffe00083c953c         __DATA_CONST.__assert           
	sz=0x00000688 off=0x013c5540-0x013c5bc8 addr=0xfffffe00083c9540-0xfffffe00083c9bc8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000100 off=0x013c5bc8-0x013c5cc8 addr=0xfffffe00083c9bc8-0xfffffe00083c9cc8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 450 at 0x04af4eb0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     15906F58-9240-39C2-BF84-20644DB6D0AE
008: LC_SOURCE_VERSION           190.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac3338 size=0x450
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IONetworkingFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IONetworkingFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `I/O Kit Networking Family`
- `CFBundleNumericVersion`: `54558720`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `3.4`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `3.4`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2000-2013 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0b1`
- `OSBundleRequired`: `Network-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IONetworkingFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895148288`
- `_PrelinkExecutableRelativePath`: `IONetworkingFamily`
- `_PrelinkExecutableSize`: `148308`
- `_PrelinkExecutableSourceAddr`: `-2198895148288`
- `_PrelinkKmodInfo`: `-2198828124592`

## Strings (212) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `IONetworkMedium`
- `site.IONetworkStack`
- `detach state`
- `IOLinkStatus`
- `Size`
- `IORegistryEntryID`
- `IOOutputQueue.cpp`
- `site.IOGatedOutputQueue`
- `( target == gIODebuggerDevice ) || ( target == 0 ) || ( gIODebuggerDevice == 0 )`
- `Speed`
- `IONetworkStackUserClient`
- `interface name prefix is null\n`
- `_stats`
- `12111112122212121111111112222111211211121`
- `IOFeatures`
- `site.IONetworkInterface`
- `22222222222222112122222111221122111221`
- `interface %s%u open failed\n`
- `IOOutputQueue`
- `ctr`
- `IOMediumDictionary`
- `%s: initIfnetParams failed\n`
- `site.IONetworkStackUserClient`
- `IOECStateNotifier`
- `dict && group`
- `location`
- `%s: registering debugger\n`
- `IONetworkController`
- `_debugLockCount >= 0`
- `IOInterfaceNamePrefix`
- `IOMediaHeaderLength`
- `21212121222222222222111111`
- `1211`
- `client`
- `%s: ifnet_set_offload error %d\n`
- `%s: SET_INPUT_MODEL bad params size %u != %u\n`
- `interface %s%u name assigment failed\n`
- `site.IOBasicOutputQueue`
- `IONetworkController::%s\n`
- `site.IOMbufNaturalMemoryCursor`
- `IOMbufBigMemoryCursor`
- `!doneCoalesce`
- `site.IONetworkController`
- `%s::%s Unknown client type\n`
- `IOOutputQueueStatsKey`
- `IOBSD`
- `%02X%02X%02X%02X%02X%02X`
- `site.IOECStateNotifier`
- `kdp_match_mac`
- `site.IOMbufBigMemoryCursor`
- `IOMbufLittleMemoryCursor`
- `IONetworkController::%s()\n`
- `cmdP && self`
- `IOEthernetInterface`
- `kdp_match_name`
- `site.IOMbufLittleMemoryCursor`
- `_clientSet->getCount() == 0`
- `IOInterfaceState`
- `remote_nmi`
- `Flags`
- `interface name %s%u is unavailable\n`
- `en`
- `sendPacket`
- `IOInterfaceFlags`
- `pkt`
- `121112221111112211`
- `site.IOPacketQueue`
- `IOPacketQueue: super::init() failed\n`
- `IOPacketFilters`
- `site.IOEthernetInterface`
- `Index`
- `IONetworkStackUserCommand`
- `IOPathMatch`
- `site.IONetworkUserClient`
- `1211122211111122`
- `data && (arg == kIOOutputQueueSignature)`
- `12112`
- `multiAddrs`
- `IOKernelDebugger`
- `site.IOMbufMemoryCursor`
- `IOMbufNaturalMemoryCursor`
- `IONetworkController.cpp`
- `Data`
- `%s: GET_INPUT_MODEL bad params size %u != %u\n`
- `IOActiveMedium`
- `IOSelectedMedium`
- `IOLinkData`
- `1212121111`
- `com.apple.networking.ionetworkstack.user-client`
- `IONetworkUserClient.cpp`
- `2121122111111121111211112221111`
- `IOEthernetController ERROR: Double complete of realtime AVB packet`
- `%s: Invalid alignment: start:%d, length:%d\n`
- `IONetworkInterface: unknown event type %x\n`
- `IONetworkUserClient`
- `IOGatedOutputQueue`
- `IOPacketQueue`
- `IOMACAddress`
- `gPTPPresent`
- `site.IOECTimeSyncHandler`
- `ok`
- `IOInterfaceType`
- `121222221`
- `enable`
- `IOModel`
- `%s%u`
- `%s: %s(0x%x, 0x%x) retry %u\n`
- `haltOutputThread`
- `12111112122212121111111111`
- `1211111212221212111111111111111`
- `site.IOEthernetAVBPacket`
- `WakeOnMagicPacket`
- `IOMbufMemoryCursor`
- `srcm`
- `IOMinPacketSize`
- `src && dst`
- `IONetworkInterface::init(%p, %s) failed\n`
- `IOBasicOutputQueue`
- `BSD Name`
- `%s: BSD attach failed, bad MAC address\n`
- `IOEthernetInterface.cpp`
- `IOEthernetStatsKey`
- `IONetworkInterface`
- `IODefaultMedium`
- `ionetwork_debug`
- `root`
- `site.IOEthernetAVBPacketPoolEntry`
- `nullRxHandler`
- `kdp`
- `disable`
- `unable to name interface in state 0x%x as %s%u\n`
- `12111112122212121111121`
- `temp`
- `IOLocation`
- `1222211`
- `m != NULL`
- `IOKernelDebugger::%s no debugger device\n`
- `site.IOECTSCallbackEntry`
- `IOKDP`
- `IOMbufMemoryCursor.cpp`
- `IOControllerEnabled`
- `receivePacket`
- `IOPrimaryInterface`
- `IOEthernetController`
- `site.IOEthernetController`
- `NumberOfRealtimeTransmitQueues`
- `IOActivePacketFilters`
- `site.IOKernelDebugger`
- `IOEthernetWakeOnLANFilterGroup`
- `site.IONetworkData`
- `IONetworkRootType`
- `IORevision`
- `IOMaxPacketSize`
- `NumberOfRealtimeReceiveQueues`
- `site.IOKDP`
- `built-in`
- `IOKernelDebugger.cpp`
- `IONetworkFilterGroup`
- `site.IOMbufQueue`
- `site.ExpansionData`
- `22121`
- `IOEthernetDisabledWakeOnLANFilterGroup`
- `IOMaxTransferUnit`
- `IOMediaAddressLength`
- `Type`
- `interface %s%u became inactive\n`
- `_owner`
- `m`
- `IORequiredPacketFilters`
- `12111112122212121`
- `remote NMI`
- `IOPlatformDeviceSignaledWakeup`
- `%s: ifnet_attach error %d\n`
- `%02X`
- `%s: SET_INPUT_MODEL unknown model 0x%x\n`
- `12111112122212121111111221211111111`
- `IOVendor`
- `IONetworkData`
- `IOBuiltin`
- `IOInterfaceUnit`
- `%s: ifnet_allocate_extended error %d\n`
- `IONetworkNoBSDAttach`
- `param0`
- `debug`
- `IOLinkSpeed`
- `IOInterfaceExtraFlags`
- `%08x`
- `site.IOOutputQueue`
- `11`
- `12111`
- `1211111212221212111111122121111111`
- `constraintsP`
- `1122`
- `IONetworkStack`
- `IONetworkStack::start(%p) %p failed\n`
- `1211111212221212111111111111`
- `AVBControllerState`
- `interface`
- `1211111212221212111111111222211121`
- `IONetworkStatsKey`
- `%s: BSD attach failed, no driver\n`
- `site.IONetworkMedium`
- `IONetworkStack::free() %p\n`
- `TimeSyncSupport`
- `IOLinkActiveCount`
- `1`
- `(mp != NULL) && (*mp != NULL)`
- `112`
- `IOECTimeSyncHandler`
- `IOMulticastAddressList`
- `IOPrimaryDebugPort`
- `Access Types`

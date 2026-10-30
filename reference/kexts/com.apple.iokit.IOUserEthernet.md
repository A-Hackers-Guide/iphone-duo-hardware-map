# `com.apple.iokit.IOUserEthernet`

- Name: IOUserEthernet
- Version: `1.0.1`
- UUID: `573636F2-B073-3153-8DF0-995964D9C2F1`
- Source version: `81.0.0.0.0`
- Depends on: [`com.apple.driver.AppleMobileFileIntegrity`](com.apple.driver.AppleMobileFileIntegrity.md) 1.0.2, [`com.apple.iokit.IONetworkingFamily`](com.apple.iokit.IONetworkingFamily.md) 1.6.1, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### IOUserEthernetResource
- `CFBundleIdentifier`: `com.apple.iokit.IOUserEthernet`
- `IOClass`: `IOUserEthernetResource`
- `IOMatchCategory`: `IOUserEthernetResource`
- `IOPersonalityPublisher`: `com.apple.iokit.IOUserEthernet`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `IOUserEthernetResourceUserClient`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOUserEthernetController` | 0x1a8 | IOEthernetController → IONetworkController → IOService → IORegistryEntry |
| `IOUserEthernetInterface` | 0x150 | IOEthernetInterface → IONetworkInterface → IOService → IORegistryEntry |
| `IOUserEthernetResource` | 0x98 | IOService → IORegistryEntry |
| `IOUserEthernetResourceUserClient` | 0xf0 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001301 off=0x00b67160-0x00b68461 addr=0xfffffe0007b6b160-0xfffffe0007b6c461 r--/r--   __TEXT            
	sz=0x00000018 off=0x00b677d8-0x00b677f0 addr=0xfffffe0007b6b7d8-0xfffffe0007b6b7f0               __TEXT.__const            
	sz=0x00000c71 off=0x00b677f0-0x00b68461 addr=0xfffffe0007b6b7f0-0xfffffe0007b6c461               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00005c08 off=0x03877240-0x0387ce48 addr=0xfffffe000a87b240-0xfffffe000a880e48 r-x/r-x   __TEXT_EXEC       
	sz=0x00005728 off=0x03877240-0x0387c968 addr=0xfffffe000a87b240-0xfffffe000a880968          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000004e0 off=0x0387c968-0x0387ce48 addr=0xfffffe000a880968-0xfffffe000a880e48          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000190 off=0x04a1cd28-0x04a1ceb8 addr=0xfffffe000ba20d28-0xfffffe000ba20eb8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a1cd28-0x04a1cdf0 addr=0xfffffe000ba20d28-0xfffffe000ba20df0               __DATA.__data             
	sz=0x000000b8 off=0x00000000-0x000000b8 addr=0xfffffe000ba20df0-0xfffffe000ba20ea8               __DATA.__common           (Zerofill)
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000ba20ea8-0xfffffe000ba20eb8               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000021e0 off=0x01473c88-0x01475e68 addr=0xfffffe0008477c88-0xfffffe0008479e68 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x01473c88-0x01473ca8 addr=0xfffffe0008477c88-0xfffffe0008477ca8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x01473ca8-0x01473cc8 addr=0xfffffe0008477ca8-0xfffffe0008477cc8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001d30 off=0x01473cc8-0x014759f8 addr=0xfffffe0008477cc8-0xfffffe00084799f8         __DATA_CONST.__const            
	sz=0x00000180 off=0x014759f8-0x01475b78 addr=0xfffffe00084799f8-0xfffffe0008479b78         __DATA_CONST.__kalloc_type      
	sz=0x00000270 off=0x01475b78-0x01475de8 addr=0xfffffe0008479b78-0xfffffe0008479de8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000080 off=0x01475de8-0x01475e68 addr=0xfffffe0008479de8-0xfffffe0008479e68         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 172 at 0x04afbc2c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     573636F2-B073-3153-8DF0-995964D9C2F1
008: LC_SOURCE_VERSION           81.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004acaa50 size=0xd8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOUserEthernet`
- `CFBundleIdentifier`: `com.apple.iokit.IOUserEthernet`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOUserEthernet`
- `CFBundleNumericVersion`: `16875520`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.1`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2008-2013 Apple Inc. All rights reserved.`
- `OSBundleLibraries_x86_64`:
  - `com.apple.iokit.IONetworkingFamily`: `2.0`
  - `com.apple.kpi.bsd`: `11.0.0`
  - `com.apple.kpi.iokit`: `11.0.0`
  - `com.apple.kpi.libkern`: `11.0.0`
  - `com.apple.kpi.mach`: `11.0.0`
  - `com.apple.kpi.private`: `11.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOUserEthernet.kext`
- `_PrelinkExecutableLoadAddr`: `-2198893842080`
- `_PrelinkExecutableRelativePath`: `IOUserEthernet`
- `_PrelinkExecutableSize`: `37497`
- `_PrelinkExecutableSourceAddr`: `-2198893842080`
- `_PrelinkKmodInfo`: `-2198828085976`

## Strings (124) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `iouether_debug`
- `MaxPacketSize`
- `MinPacketSize`
- `IOUE[%p]::%s\n`
- `attachToDataLinkLayer`
- `free`
- `IOUE_UC[%p]::%s()\n`
- `Cookie`
- `IOUE[%p]getRetainCount = %d\n`
- `createControllerGated`
- `IOUE_UC::%s failed : controller already exists\n`
- `IORegistryEntryID`
- `IOUE %s: packet too short, %zu < %lu\n`
- `IOUE %s: unsupported GSO type %d\n`
- `site.IOUserEthernetInterface`
- `EnableMultiPages`
- `Unit`
- `handleClientAttach`
- `IOUE %s() [%s %d 0x%llx] returning 0x%08x\n`
- `terminateController`
- `reportLinkUp`
- `nameBSDInterface`
- `111112`
- `v32@?0^{?=II^{ipc_port}^{ipc_port}Ii}8^(?={?=(?=^{ipc_port}^{ipc_port}^{ipc_port})b16b8b8I}{?=IIb8b8b8b8}{?=IIb8b8b8b8}{?=IIb24b8}{?=IIb16b8b8})16^v24`
- `IOUE[%p]::start ok, netif %p, cookie 0x%llx%s\n`
- `BSD Name`
- `IOUEI[%p]::%s %s%d\n`
- `121111121222121211111111111111`
- `IOUE_UC::%s attach failed\n`
- `handleClientDetach`
- `setIfpPowerSavingsMask`
- `IOUE_UC:: %s entitlement missing\n`
- `clientDied`
- `IOUE[%p]::%s(%d)\n`
- `IOUE %s: unrecognized GSO type %d\n`
- `IOUEI[%p]::%s(0x%08x)\n`
- `IOInterfaceUnit`
- `boolean_t en_set_route_cleanup(ifnet_t, boolean_t)`
- `clientClose`
- `ingest_virtio_header_tx`
- `%s provider cast failed\n`
- `MaxTransferUnit`
- `IOUserClientClass`
- ` self-named`
- `setEnableState`
- `<== IOUE[%p]::%s(%p) = 0x%08x\n`
- `IOUE_UC::%s start failed\n`
- `site.IOUserEthernetController`
- `12111112122212121111111221211111111112111111112222212`
- `%s: setting agressive route cleanup on: %s to ON\n`
- `%s: setting agressive route cleanup on: %s to OFF\n`
- `IOUE %s: GSO size is zero\n`
- `IOUE_UC[%p]::%s(%p)\n`
- `IOUE en_register error %d\n`
- `IOUserEthernetInterface`
- `IONetworkStackUserCommand`
- `IOUserEthernetResourceUserClient`
- `initWithTask`
- `IOUE_UC[%p]::%s\n`
- `%s: state event callback failed - msg_send returned: %d\n`
- `IOUserEthernetController`
- `setLinkState`
- `start`
- `EnableCrossover`
- `==> IOUE[%p]::%s(%p)\n`
- `IOUE[%p]::free\n`
- `stop`
- `IOUE_UC::%s failed : could not create descriptor\n`
- `IOUE[%p]::stop(%p)\n`
- `invalidateStateEventCallback`
- `handleBSDDetach`
- `en_register`
- `IOUE %s: mbuf_set_csum_requested %d\n`
- `com.apple.networking.ethernet.user-access`
- `IOUE_UC::%s failed\n`
- `SelfNamed`
- `setRunningState`
- `handleBSDAttach`
- `%s - ctl_register failed: %d\n`
- `populate_virtio_header_tx`
- `com.apple.userspace_ethernet`
- `virtio_mbuf_ingest_header`
- `IOUE %s: gso_hdr_len %d > %ld\n`
- `site.IOUserEthernetResourceUserClient`
- `EnableVirtIOHeader`
- `registerService`
- `success`
- `P2PInstance`
- `<== IOUE[%p]::%s(%p)\n`
- `1211111212221212112`
- `IOUE[%p]::%s()\n`
- `IONetworkStack`
- `site.struct en_client`
- `failure`
- `EnableTSO`
- `IOUE: namePrefix length %u is invalid, must be 2..11\n`
- `IOUE %s: GSO_UDP not supported\n`
- `IOUE %s: gso_hdr_len %d <= %d\n`
- `IOUE_UC::%s failed : controller is NULL\n`
- `IOUE[%p]::outputStart dequeue error 0x%x\n`
- `IOUserEthernetResource`
- `IOUserEthernetInterfaceMergeProperties`
- `121111121222121211111111122221112112111212`
- `IOUE_UC[%p]::%s(%p, %p, 0x%08x) %s\n`
- `IOUE attach client %p, cookie 0x%llx, netif %p\n`
- `Failed to set subtype %d\n`
- `SubType`
- `IOUE[%p]::start failed\n`
- `IOUE[%p]::outputStart: en_packet_list_to_client failed\n`
- `IOUE %s: GSO requested without seg_size\n`
- `IOUE %s: mbuf_set_tso_info() %d\n`
- `site.IOUserEthernetResource`
- `EnableChecksumOffload`
- `IOUE %s: TSO requested without CSUM\n`
- `getNamePrefix`
- `HardwareAddress`
- `Failed to self name using unit %d, 0x%x\n`
- `NONE`
- `NamePrefix`
- `IOUE mbuf_prepend failed %d\n`
- `IOUE %s: offset %d >= %ld\n`
- `detachFromDataLinkLayer`
- `IOUEI[%p]::%s() %s\n`
- `IOUE[%p]::start(%p)\n`

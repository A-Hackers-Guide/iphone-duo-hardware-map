# `com.apple.driver.ExclaveSEPManagerProxy`

- Name: ExclaveSEPManagerProxy
- Version: `1`
- UUID: `E113A8BA-2497-39A5-9283-9735ACBCBD07`
- Source version: `928.40.6.0.0`
- Depends on: [`com.apple.driver.AppleSEPManager`](com.apple.driver.AppleSEPManager.md) 1.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/esm`](../devicetree/root__arm-io__esm.md) | `ExclaveSEPManagerProxy` | `iop,exclave-sep-manager` |

## IOKit personalities (1) [KC]

### ExclaveSEPManagerProxy
- `CFBundleIdentifier`: `com.apple.driver.ExclaveSEPManagerProxy`
- `IOClass`: `ExclaveSEPManagerProxy`
- `IOExclaveProxy`: `True`
- `IONameMatch`: `iop,exclave-sep-manager`
- `IOPersonalityPublisher`: `com.apple.driver.ExclaveSEPManagerProxy`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOService`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `ExclaveSEPManagerProxy` | 0xd0 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000fa7 off=0x00923960-0x00924907 addr=0xfffffe0007927960-0xfffffe0007928907 r--/r--   __TEXT            
	sz=0x000000e0 off=0x00923fd8-0x009240b8 addr=0xfffffe0007927fd8-0xfffffe00079280b8               __TEXT.__const            
	sz=0x0000084f off=0x009240b8-0x00924907 addr=0xfffffe00079280b8-0xfffffe0007928907               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00001ff8 off=0x02c5ca70-0x02c5ea68 addr=0xfffffe0009c60a70-0xfffffe0009c62a68 r-x/r-x   __TEXT_EXEC       
	sz=0x00001d48 off=0x02c5ca70-0x02c5e7b8 addr=0xfffffe0009c60a70-0xfffffe0009c627b8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000002b0 off=0x02c5e7b8-0x02c5ea68 addr=0xfffffe0009c627b8-0xfffffe0009c62a68          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000118 off=0x049dc3b0-0x049dc4c8 addr=0xfffffe000b9e03b0-0xfffffe000b9e04c8 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049dc3b0-0x049dc474 addr=0xfffffe000b9e03b0-0xfffffe000b9e0474               __DATA.__data             
	sz=0x00000040 off=0x00000000-0x00000040 addr=0xfffffe000b9e0478-0xfffffe000b9e04b8               __DATA.__common           (Zerofill)
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000b9e04b8-0xfffffe000b9e04c8               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00000870 off=0x012dc088-0x012dc8f8 addr=0xfffffe00082e0088-0xfffffe00082e08f8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x012dc088-0x012dc090 addr=0xfffffe00082e0088-0xfffffe00082e0090         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x012dc090-0x012dc098 addr=0xfffffe00082e0090-0xfffffe00082e0098         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000006a0 off=0x012dc098-0x012dc738 addr=0xfffffe00082e0098-0xfffffe00082e0738         __DATA_CONST.__const            
	sz=0x00000040 off=0x012dc738-0x012dc778 addr=0xfffffe00082e0738-0xfffffe00082e0778         __DATA_CONST.__kalloc_type      
	sz=0x00000158 off=0x012dc778-0x012dc8d0 addr=0xfffffe00082e0778-0xfffffe00082e08d0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000028 off=0x012dc8d0-0x012dc8f8 addr=0xfffffe00082e08d0-0xfffffe00082e08f8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 91 at 0x04aef008
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     E113A8BA-2497-39A5-9283-9735ACBCBD07
008: LC_SOURCE_VERSION           928.40.6.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab9d38 size=0x58
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `ExclaveSEPManagerProxy`
- `CFBundleGetInfoString`: `Copyright © 2023 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.ExclaveSEPManagerProxy`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `ExclaveSEPManagerProxy`
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
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/ExclaveSEPManagerProxy.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896215712`
- `_PrelinkExecutableRelativePath`: `ExclaveSEPManagerProxy`
- `_PrelinkExecutableSize`: `14631`
- `_PrelinkExecutableSourceAddr`: `-2198896215712`
- `_PrelinkKmodInfo`: `-2198828350544`

## Strings (43) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `v12@?0B8`
- `TB_ERROR_SUCCESS == exclavesepmanager_exclavesepmanagerproxyinterface_outboxnotemptyinterrupt(&client, ^ (uint32_t ret) { message_count = ret; })`
- `message_count != __UINT32_MAX__`
- `ExclaveSEPManagerProxy`
- `exclaveStart(provider, &exclaveState)`
- `sepBootedOnce`
- `dict != nullptr`
- `tb_endpoint != nullptr`
- `-run-sep-exclaves-test`
- `ExclaveSEPTestClient: running sep_exclaves_test\n`
- `TB_ERROR_SUCCESS == exclaveseptestclient_exclaveseptestclientproxyinterface__init(&test_client, test_tb_endpoint)`
- `FAILED`
- `TB_ERROR_SUCCESS == exclavesepmanager_exclavesepmanagerproxyinterface_completepowertransition(&client, ps)`
- `ExclaveSEPManager_C.c`
- `ExclaveSEPManagerProxy.cpp`
- `setActive`
- `TB_ERROR_SUCCESS == exclaveseptestclient_exclaveseptestclientproxyinterface_sep_exclaves_test( &test_client, ^(bool result) { test_result = result; })`
- `ExclaveSEPTestClient sep_exclaves_test result: %s\n`
- `\"TB_FATAL: \" \"invalid value: unexpected case value, %llx\" @%s:%d`
- `\"failed REQUIRE condition (condition: \\\"%s\\\"), (%s line %d)\" @%s:%d`
- `IOService::start(provider)`
- `TB_ERROR_SUCCESS == exclavesepmanager_exclavesepmanagerproxyinterface__init(&client, tb_endpoint)`
- `workLoop->inGate()`
- `Powering down ExclaveSEPManager now`
- `i8@?0`
- `result == kIOReturnSuccess`
- `PASSED`
- `/Library/Caches/com.apple.xbs/4DCEF7EB-8EF5-4AEA-A320-964676D951EC/TemporaryDirectory.LWoUbI/Sources/AppleSEPManager/ExclaveSEPManager/Sources/ExclaveSEPManagerProxy/ExclaveSEPManagerProxy.cpp`
- `-no-sep-exclaves`
- `AppleSEPManager`
- `IOHibernateState`
- `TB_ERROR_SUCCESS == exclavesepmanager_exclavesepmanagerproxyinterface_initiatepowertransition(&client, ps,^ (uint32_t tb_ret) { initiate_pt_ret = tb_ret; })`
- `outstanding_messages >= message_count`
- `(static_cast<PowerState>(powerStateOrdinal) == PowerState::kOn) || (static_cast<PowerState>(powerStateOrdinal) == PowerState::kOff)`
- `mapper != nullptr`
- `TB_ERROR_SUCCESS == exclavesepmanager_exclavesepmanagerproxyinterface_unmapoolbuffers(&client)`
- `TB_ERROR_SUCCESS == exclavesepmanager_exclavesepmanagerproxyinterface_mapoolbuffers(&client)`
- `v12@?0I8`
- `site.ExclaveSEPManagerProxy`
- `whatDevice == this`
- `12111112122212121111112211`
- `exclaveMapper != nullptr`
- `test_tb_endpoint != nullptr`

# `com.apple.driver.AFKHIDTBDevice`

- Name: AFKHIDTBDevice
- Version: `1`
- UUID: `3D45CF4F-CB74-34E0-9B95-CD1737C65A4C`
- Source version: `224.40.2.0.0`
- Depends on: [`com.apple.driver.AppleFirmwareKit`](com.apple.driver.AppleFirmwareKit.md) 1.0.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.5, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 14.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 14.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 14.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0.0b2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AFKHIDTBDevice
- `CFBundleIdentifier`: `com.apple.driver.AFKHIDTBDevice`
- `IOClass`: `AFKHIDTBDevice`
- `IOMatchCategory`: `AFKHIDTBDevice`
- `IOPersonalityPublisher`: `com.apple.driver.AFKHIDTBDevice`
- `IOProbeScore`: `1000`
- `IOPropertyMatch`:
  - `KEXTTBInterface`: `AFKHIDDevice`
- `IOProviderClass`: `AFKTightbeamEndpoint`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AFKHIDTBDevice` | 0x128 | IOHIDDevice → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000022d6 off=0x00117e60-0x0011a136 addr=0xfffffe000711be60-0xfffffe000711e136 r--/r--   __TEXT            
	sz=0x000000e0 off=0x001184d8-0x001185b8 addr=0xfffffe000711c4d8-0xfffffe000711c5b8               __TEXT.__const            
	sz=0x0000177e off=0x001185b8-0x00119d36 addr=0xfffffe000711c5b8-0xfffffe000711dd36               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000400 off=0x00119d36-0x0011a136 addr=0xfffffe000711dd36-0xfffffe000711e136               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0000c7d8 off=0x0151a140-0x01526918 addr=0xfffffe000851e140-0xfffffe000852a918 r-x/r-x   __TEXT_EXEC       
	sz=0x0000c2e8 off=0x0151a140-0x01526428 addr=0xfffffe000851e140-0xfffffe000852a428          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000004f0 off=0x01526428-0x01526918 addr=0xfffffe000852a428-0xfffffe000852a918          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x04924278-0x04924378 addr=0xfffffe000b928278-0xfffffe000b928378 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04924278-0x04924340 addr=0xfffffe000b928278-0xfffffe000b928340               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b928340-0xfffffe000b928378               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000e80 off=0x00f68648-0x00f694c8 addr=0xfffffe0007f6c648-0xfffffe0007f6d4c8 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x00f68648-0x00f68650 addr=0xfffffe0007f6c648-0xfffffe0007f6c650         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x00f68650-0x00f68658 addr=0xfffffe0007f6c650-0xfffffe0007f6c658         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000009c8 off=0x00f68658-0x00f69020 addr=0xfffffe0007f6c658-0xfffffe0007f6d020         __DATA_CONST.__const            
	sz=0x000001c0 off=0x00f69020-0x00f691e0 addr=0xfffffe0007f6d020-0xfffffe0007f6d1e0         __DATA_CONST.__kalloc_type      
	sz=0x00000278 off=0x00f691e0-0x00f69458 addr=0xfffffe0007f6d1e0-0xfffffe0007f6d458         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000070 off=0x00f69458-0x00f694c8 addr=0xfffffe0007f6d458-0xfffffe0007f6d4c8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 172 at 0x04acf504
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     3D45CF4F-CB74-34E0-9B95-CD1737C65A4C
008: LC_SOURCE_VERSION           224.40.2.0.0
009: LC_FUNCTION_STARTS          offset=0x004a94dd0 size=0x198
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AFKHIDTBDevice`
- `CFBundleIdentifier`: `com.apple.driver.AFKHIDTBDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AFKHIDTBDevice`
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
- `NSHumanReadableCopyright`: `Copyright © 2026 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleRequired`: `Auxiliary`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AFKHIDTBDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198904652192`
- `_PrelinkExecutableRelativePath`: `AFKHIDTBDevice`
- `_PrelinkExecutableSize`: `64046`
- `_PrelinkExecutableSourceAddr`: `-2198904652192`
- `_PrelinkKmodInfo`: `-2198829104520`

## Strings (123) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `failed to wrap packed buffer`
- `\"TB_ASSERT: \" \"(afkhidtbdevice_reporttype__decode(msg, &reportType) == TB_ERROR_SUCCESS) && \\\"failed to decode type: AFKHIDTBDevice.ReportType\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"invalid error returned from %s\" @%s:%d`
- `this->_matchingThread`
- `site.afkhidtbdevice_deviceclient__service_s`
- `v24@?0Q8r^{afkhidtbdevice_report_s={u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}16`
- `AFKHIDTBDevice_c.c`
- `tb_message_subrange failed`
- `unexpected tb_error_t returned`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->sendreport != ((void*)0)) && \\\"implementation for sendReport is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `site.afkhidtbdevice_deviceclient__server_s`
- `SetReportFailCount`
- `\"TB_ASSERT: \" \"(afkhidtbdevice_devicedescription__sizeof(value, &__sz) == TB_ERROR_SUCCESS) && \\\"marshal_sizeof\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `1211111212221212112111222121121111111`
- `/Library/Caches/com.apple.xbs/2E36C77F-9AB7-49A3-AAD4-083D32455892/TemporaryDirectory.cxrco6/Sources/AppleHIDRT/AFKHIDTBDevice/AFKHIDTBDevice/kext/AFKHIDTBDevice.cpp`
- `\"TB_FATAL: \" \"invalid result returned from setReport\" @%s:%d`
- `RegisterService`
- `DebugState`
- `reportMap`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"failed to wrap packed buffer\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `failed to decode type: AFKHIDTBDevice.ReportType`
- `I56@?0{afkhidtbdevice_device_getreport__result_s=C(?=I{afkhidtbdevice_report_s={u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}})}8`
- `\"TB_ASSERT: \" \"(server->setreport != ((void*)0)) && \\\"implementation for setReport is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `getReport`
- `status`
- `AFKTightbeamEndpoint`
- `report->prepare() == kIOReturnSuccess`
- `failed to encode type: AFKHIDTBDevice.Report`
- `completion block must be called before returning`
- `I16@?0{afkhidtbdevice_device_setreport__result_s=C(?=I)}8`
- `\"TB_FATAL: \" \"invalid result returned from getReportDescriptor\" @%s:%d`
- `\"TB_FATAL: \" \"invalid result returned from getDeviceDescription\" @%s:%d`
- `SerialNumber`
- `\"TB_ASSERT: \" \"(afkhidtbdevice_report__sizeof(value, &__sz) == TB_ERROR_SUCCESS) && \\\"marshal_sizeof\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `implementation for getReportDescriptor is not present`
- `implementation for sendReport is not present`
- `\"TB_FATAL: \" \"overflow detected when adding\" @%s:%d`
- `setReport`
- `getReportDescriptor`
- `\"TB_ASSERT: \" \"(vErr == TB_ERROR_SUCCESS) && \\\"tb_message_subrange failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `implementation for getReport is not present`
- `\"TB_ASSERT: \" \"(server->getreport != ((void*)0)) && \\\"implementation for getReport is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `I120@?0{afkhidtbdevice_device_getdevicedescription__result_s=C(?=I{afkhidtbdevice_devicedescription_s={u32__opt_s=BI}{u64__opt_s=BQ}{u64__opt_s=BQ}{u64__opt_s=BQ}{u8_v__opt_s=B{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}})}8`
- `this->_epIN`
- `ProductID`
- `report->getLength()`
- `v56@?0{afkhidtbdevice_device_getreport__result_s=C(?=I{afkhidtbdevice_report_s={u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}})}8`
- `marshal_sizeof`
- `failed to encode type: AFKHIDTBDevice.ReportType`
- `implementation for setReport is not present`
- `\"TB_FATAL: \" \"invalid value: unexpected case value, %llx\" @%s:%d`
- `_commandGate && _workLoop->addEventSource(_commandGate.get()) == kIOReturnSuccess`
- `report`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS || err == TB_ERROR_USER_FAILURE) && \\\"unexpected tb_error_t returned\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `failed to decode type: AFKHIDTBDevice.Report`
- `getDeviceDescription`
- `site.afkhidtbdevice_device_s`
- `_notif`
- `!isInactive()`
- `v56@?0{afkhidtbdevice_device_getreportdescriptor__result_s=C(?=I{afkhidtbdevice_descriptor_s={u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}})}8`
- `\"TB_ASSERT: \" \"(server->getreportdescriptor != ((void*)0)) && \\\"implementation for getReportDescriptor is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `implementation for getDeviceDescription is not present`
- `site.AFKHIDTBDevice`
- `HIDDefaultBehavior`
- `KEXTTBEPCompanion`
- `debugSerializer`
- `v120@?0{afkhidtbdevice_device_getdevicedescription__result_s=C(?=I{afkhidtbdevice_devicedescription_s={u32__opt_s=BI}{u64__opt_s=BQ}{u64__opt_s=BQ}{u64__opt_s=BQ}{u8_v__opt_s=B{u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}}})}8`
- `blockDescriptorData`
- `GetReportFailCount`
- `\"TB_ASSERT: \" \"(afkhidtbdevice_descriptor__sizeof(value, &__sz) == TB_ERROR_SUCCESS) && \\\"marshal_sizeof\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `!this->_server && !this->_service`
- `Virtual`
- `ReportDescriptor`
- `dict`
- `isInactive() == false`
- `v16@?0{afkhidtbdevice_device_setreport__result_s=C(?=I)}8`
- `\"TB_ASSERT: \" \"(cmp.encoded) && \\\"completion block must be called before returning\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(afkhidtbdevice_report__decode(msg, &report) == TB_ERROR_SUCCESS) && \\\"failed to decode type: AFKHIDTBDevice.Report\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `1`
- `_workLoop`
- `AFKHIDTBDevice`
- `companionDictTyped`
- `this->_epOUT`
- `ReportInterval`
- `I16@?0^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}8`
- `\"TB_ASSERT: \" \"(afkhidtbdevice_reporttype__raw_encode(&msg, reportType) == TB_ERROR_SUCCESS) && \\\"failed to encode type: AFKHIDTBDevice.ReportType\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(afkhidtbdevice_report__raw_encode(&msg, report) == TB_ERROR_SUCCESS) && \\\"failed to encode type: AFKHIDTBDevice.Report\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->getdevicedescription != ((void*)0)) && \\\"implementation for getDeviceDescription is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `AssertMacros: %s, %s file: %s, line: %d, value: %lld\n`
- `LocationID`
- `\"TB_FATAL: \" \"invalid tag in '[UInt8]' metadata: 0x%x\" @%s:%d`
- `\"TB_FATAL: \" \"overflow detected when multiplying\" @%s:%d`
- `I56@?0{afkhidtbdevice_device_getreportdescriptor__result_s=C(?=I{afkhidtbdevice_descriptor_s={u8_v_s=C(?={?=*Q@?}{?=*QQ}{?=^{tb_message_s}QQQ})}})}8`
- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
- `I8@?0`
- `\"TB_FATAL: \" \"invalid result returned from getReport\" @%s:%d`
- `i8@?0`
- `tbStatus == TB_ERROR_SUCCESS`

**[__TEXT.__os_log]**

- `%s:0x%llx Failed to add matching notification\n`
- `%s:0x%llx No _epOUT available\n`
- `%s:0x%llx workLoop\n\n`
- `%s:0x%llx getreportdescriptor callback: failed to get success result\n`
- `%s:0x%llx Failed to allocate temp buffer for descriptor\n`
- `%s:0x%llx No descriptor data after callback\n`
- `%s:0x%llx provider is not AFKTightbeamEndpoint (type: %s, registryID: 0x%llx)\n`
- `%s:0x%llx handleMatchingNotification\n`
- `%s:0x%llx completeServiceMatchingGated\n`
- `%s:0x%llx super::handleStart failed\n`
- `%s:0x%llx Failed to create OSData from descriptor\n`
- `%s:0x%llx u8__v_copyout failed: 0x%x\n`
- `%s:0x%llx Start\n`
- `%s:0x%llx super::start failed\n`
- `%s:0x%llx KEXTTBEPCompanion is not a dictionary\n`
- `%s:0x%llx completeServiceMatchingGated faield\n`
- `%s:0x%llx service stoppped\n`
- `%s:0x%llx newReportDescriptor failed\n`
- `%s:0x%llx No workloop available\n`
- `%s:0x%llx Already initialized\n`
- `%s:0x%llx Tightbeam client and server initialized successfully\n`
- `%s:0x%llx _commandGate\n`
- `%s:0x%llx afkhidtbdevice_device_getreportdescriptor failed: 0x%x\n`
- `%s:0x%llx Failed to allocate thread call\n`

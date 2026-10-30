# `com.apple.driver.SecureRTBuddyProxy`

- Name: SecureRTBuddyProxy
- Version: `1.0.0`
- UUID: `F5A56548-ED23-3818-B90B-46923543E11E`
- Source version: `778.40.12.0.0`
- Depends on: [`com.apple.driver.RTBuddy`](com.apple.driver.RTBuddy.md) 1.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (7) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/aop-exclave-mailbox`](../devicetree/root__arm-io__aop-exclave-mailbox.md) | `SecureRTBuddyProxy` | `iop,secure-rtbuddy-proxy` |
| [`/arm-io/aop-exclave-ioreporting`](../devicetree/root__arm-io__aop-exclave-ioreporting.md) | `SecureRTBuddyIOReporting` | `iop,secure-rtbuddy-ioreporting` |
| [`/arm-io/aop2-exclave-mailbox`](../devicetree/root__arm-io__aop2-exclave-mailbox.md) | `SecureRTBuddyProxy` | `iop,secure-rtbuddy-proxy` |
| [`/arm-io/dcp-exclave-mailbox`](../devicetree/root__arm-io__dcp-exclave-mailbox.md) | `SecureRTBuddyProxy` | `iop,secure-rtbuddy-proxy` |
| [`/arm-io/dcp-exclave-ioreporting`](../devicetree/root__arm-io__dcp-exclave-ioreporting.md) | `SecureRTBuddyIOReporting` | `iop,secure-rtbuddy-ioreporting` |
| [`/arm-io/dcpsec-exclave-mailbox`](../devicetree/root__arm-io__dcpsec-exclave-mailbox.md) | `SecureRTBuddyProxy` | `iop,secure-rtbuddy-proxy` |
| [`/arm-io/dcpsec-exclave-ioreporting`](../devicetree/root__arm-io__dcpsec-exclave-ioreporting.md) | `SecureRTBuddyIOReporting` | `iop,secure-rtbuddy-ioreporting` |

## IOKit personalities (2) [KC]

### SecureRTBuddyIOReporting
- `CFBundleIdentifier`: `com.apple.driver.SecureRTBuddyProxy`
- `IOClass`: `SecureRTBuddyIOReporting`
- `IOExclaveProxy`: `True`
- `IONameMatch`: `iop,secure-rtbuddy-ioreporting`
- `IOPersonalityPublisher`: `com.apple.driver.SecureRTBuddyProxy`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOService`

### SecureRTBuddyProxy
- `CFBundleIdentifier`: `com.apple.driver.SecureRTBuddyProxy`
- `IOClass`: `SecureRTBuddyProxy`
- `IOExclaveProxy`: `True`
- `IONameMatch`: `iop,secure-rtbuddy-proxy`
- `IOPersonalityPublisher`: `com.apple.driver.SecureRTBuddyProxy`
- `IOProbeScore`: `10000`
- `IOProviderClass`: `IOService`


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `SecureRTBuddyIOReporting` | 0x140 | IOService → IORegistryEntry |
| `SecureRTBuddyPowerStateCallback` | 0x20 |  |
| `SecureRTBuddyProxy` | 0x100 | RTBuddyRouteProvider → IOService → IORegistryEntry |
| `SecureRTBuddyProxyEndpoint` | 0x80 | IOEventSource |
| `SecureRTBuddyProxyRouteAdaptor` | 0x18 | RTBuddyRoute |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001910 off=0x00da2b30-0x00da4440 addr=0xfffffe0007da6b30-0xfffffe0007da8440 r--/r--   __TEXT            
	sz=0x0000128b off=0x00da31a8-0x00da4433 addr=0xfffffe0007da71a8-0xfffffe0007da8433               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000008 off=0x00da4438-0x00da4440 addr=0xfffffe0007da8438-0xfffffe0007da8440               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0000a0b8 off=0x0398d0e0-0x03997198 addr=0xfffffe000a9910e0-0xfffffe000a99b198 r-x/r-x   __TEXT_EXEC       
	sz=0x00009b18 off=0x0398d0e0-0x03996bf8 addr=0xfffffe000a9910e0-0xfffffe000a99abf8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000005a0 off=0x03996bf8-0x03997198 addr=0xfffffe000a99abf8-0xfffffe000a99b198          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001a0 off=0x04a35820-0x04a359c0 addr=0xfffffe000ba39820-0xfffffe000ba399c0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a35820-0x04a358e8 addr=0xfffffe000ba39820-0xfffffe000ba398e8               __DATA.__data             
	sz=0x000000d8 off=0x00000000-0x000000d8 addr=0xfffffe000ba398e8-0xfffffe000ba399c0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001678 off=0x0149e0d0-0x0149f748 addr=0xfffffe00084a20d0-0xfffffe00084a3748 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x0149e0d0-0x0149e0f8 addr=0xfffffe00084a20d0-0xfffffe00084a20f8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000028 off=0x0149e0f8-0x0149e120 addr=0xfffffe00084a20f8-0xfffffe00084a2120         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001030 off=0x0149e120-0x0149f150 addr=0xfffffe00084a2120-0xfffffe00084a3150         __DATA_CONST.__const            
	sz=0x00000140 off=0x0149f150-0x0149f290 addr=0xfffffe00084a3150-0xfffffe00084a3290         __DATA_CONST.__kalloc_type      
	sz=0x00000168 off=0x0149f290-0x0149f3f8 addr=0xfffffe00084a3290-0xfffffe00084a33f8         __DATA_CONST.__assert           
	sz=0x000002d0 off=0x0149f3f8-0x0149f6c8 addr=0xfffffe00084a33f8-0xfffffe00084a36c8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000080 off=0x0149f6c8-0x0149f748 addr=0xfffffe00084a36c8-0xfffffe00084a3748         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 196 at 0x04afe134
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     F5A56548-ED23-3818-B90B-46923543E11E
008: LC_SOURCE_VERSION           778.40.12.0.0
009: LC_FUNCTION_STARTS          offset=0x004acc8f0 size=0x188
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `SecureRTBuddyProxy`
- `CFBundleGetInfoString`: `Copyright © 2023 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.SecureRTBuddyProxy`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `SecureRTBuddyProxy`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/SecureRTBuddyProxy.kext`
- `_PrelinkExecutableLoadAddr`: `-2198891500752`
- `_PrelinkExecutableRelativePath`: `SecureRTBuddyProxy`
- `_PrelinkExecutableSize`: `53728`
- `_PrelinkExecutableSourceAddr`: `-2198891500752`
- `_PrelinkKmodInfo`: `-2198827984864`

## Strings (89) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.SecureRTBuddyProxyEndpoint`
- `claim-wake-endpoint-flags`
- `SecureRTBuddyProxy.cpp`
- `tberr == TB_ERROR_SUCCESS`
- `workLoop->inGate()`
- `%s: Failed to retrieve RTKit exception statistics: %08x\n`
- `IRQ disabled time`
- `The offset of the pointer inside its valid memory range can't be represented using int32_t`
- `exclave-endpoint`
- `%s: tb_endpoint_create_with_value failed\n`
- `Power`
- `\"TB_ASSERT: \" \"(server->outboxnotemptyinterrupt != ((void*)0)) && \\\"implementation for outboxNotEmptyInterrupt is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `role`
- `SecureRTBuddyIOReporting`
- `SecureRTBuddyIOReporting.cpp`
- `Power state`
- `RTBuddy_tightbeam.c`
- `\"TB_ASSERT: \" \"(server->changepowerstateexit != ((void*)0)) && \\\"implementation for changePowerStateExit is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `1211121111111222`
- `%s.MBIEndpoint.%u`
- `SecureRTBuddyPowerStateCallback`
- `12111112122212121111111111112122`
- `SecureRTBuddyProxyRouteAdaptor`
- `\"TB_ASSERT: \" \"(rtbuddyservice_powerstate__decode(msg, &prev) == TB_ERROR_SUCCESS) && \\\"failed to decode type: RTBuddyService.PowerState\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->recordpowerstate != ((void*)0)) && \\\"implementation for recordPowerState is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->fetchexceptions != ((void*)0)) && \\\"implementation for fetchExceptions is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `_pmAssertionCount == 0`
- `endpointNumber < 64`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `site.SecureRTBuddyProxyRouteAdaptor`
- `Free heap`
- `Used stack`
- `Used Stack`
- `\"TB_ASSERT: \" \"(server->fetchthread != ((void*)0)) && \\\"implementation for fetchThread is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->fetchbase != ((void*)0)) && \\\"implementation for fetchBase is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"%s\" @%s:%d`
- `%s: super::start failed\n`
- `\"Missing exclave-endpoint property\" @%s:%d`
- `rtbuddyNotifier != NULL`
- `\"TB_ASSERT: \" \"(err == TB_ERROR_SUCCESS) && \\\"tb_service_connection_message_configure_reply failed\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_FATAL: \" \"unrecognized selector: %llu\" @%s:%d`
- `\"TB_FATAL: \" \"invalid value: unexpected case value, %llx\" @%s:%d`
- `SecureRTBuddyProxyEndpoint.cpp`
- `site.SecureRTBuddyPowerStateCallback`
- `SecureRTBuddyProxy(%s)`
- `OSBoundedPtr.h`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `%s: Failed to retrieve RTKit base statistics: %08x\n`
- `Total heap`
- `1211`
- `claim-wake`
- `\"%s: assertion failed: %s\" @%s:%d`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `%s: rtkit_stats_init failed with error %08x\n`
- `\"TB_ASSERT: \" \"(server->performpowerstatechange != ((void*)0)) && \\\"implementation for performPowerStateChange is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `site.SecureRTBuddyProxy`
- `NULL != tb_endpoint`
- `121`
- `Thread time`
- `%02X`
- `\"TB_ASSERT: \" \"(rtbuddyservice_powerstate__decode(msg, &state) == TB_ERROR_SUCCESS) && \\\"failed to decode type: RTBuddyService.PowerState\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->notifypowerstatechange != ((void*)0)) && \\\"implementation for notifyPowerStateChange is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}24@?0^{tb_connection_s=(?=[97c]^v)}8^{tb_message_s=ICQQQQ[4Q]Q^{tb_transport_message_buffer_s}}16`
- `stats_tightbeam.c`
- `%s: start\n`
- `setActive`
- `SecureRTBuddyIOReporting(%s)`
- `status == kIOReturnSuccess`
- `Total stack`
- `\"TB_ASSERT: \" \"(server->fetch != ((void*)0)) && \\\"implementation for fetch is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `SecureRTBuddyProxy`
- `1211111212221212121111111122221111111111`
- `Wake Count`
- `Peak heap alloc`
- `Total Stack`
- `IOReportLegend`
- `bank < 4`
- `\"TB_ASSERT: \" \"(rtbuddyservice_powerstate__decode(msg, &next) == TB_ERROR_SUCCESS) && \\\"failed to decode type: RTBuddyService.PowerState\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `Sleep count`
- `_pmAssertionID != kIOPMUndefinedDriverAssertionID`
- `TB_ERROR_SUCCESS == tberr`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `site.SecureRTBuddyIOReporting`
- `IOReportLegendPublic`
- `\"TB_ASSERT: \" \"(server->activatemapper != ((void*)0)) && \\\"implementation for activateMapper is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `SecureRTBuddyProxyEndpoint`
- `\"TB_ASSERT: \" \"(server->changepowerstateentry != ((void*)0)) && \\\"implementation for changePowerStateEntry is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->checkforwork != ((void*)0)) && \\\"implementation for checkForWork is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`
- `\"TB_ASSERT: \" \"(server->start != ((void*)0)) && \\\"implementation for Start is not present\\\"\" \", \" \"\\b\\b\" \" (%s:%d)\" @%s:%d`

# `com.apple.driver.AppleIISController`

- Name: AppleIISController
- Version: `600.3`
- UUID: `727E302C-B745-3BFB-AE7E-7D11F1488076`
- Source version: `600.3.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (6) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleARMFunctionIISActive` | 0x60 | AppleARMFunction |
| `AppleARMFunctionIISRoute` | 0x38 | AppleARMFunction |
| `AppleARMIISCommand` | 0xe8 | IODMACommand → IOCommand |
| `AppleARMIISController` | 0x2b8 | IOService → IORegistryEntry |
| `AppleARMIISDevice` | 0xc0 | IOService → IORegistryEntry |
| `AppleARMIISSwitch` | 0xa8 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001506 off=0x0051ba90-0x0051cf96 addr=0xfffffe000751fa90-0xfffffe0007520f96 r--/r--   __TEXT            
	sz=0x000009b8 off=0x0051c1a8-0x0051cb60 addr=0xfffffe00075201a8-0xfffffe0007520b60               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000436 off=0x0051cb60-0x0051cf96 addr=0xfffffe0007520b60-0xfffffe0007520f96               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x000081a0 off=0x02001e30-0x02009fd0 addr=0xfffffe0009005e30-0xfffffe000900dfd0 r-x/r-x   __TEXT_EXEC       
	sz=0x00007eb0 off=0x02001e30-0x02009ce0 addr=0xfffffe0009005e30-0xfffffe000900dce0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000002f0 off=0x02009ce0-0x02009fd0 addr=0xfffffe000900dce0-0xfffffe000900dfd0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000298 off=0x0494d100-0x0494d398 addr=0xfffffe000b951100-0xfffffe000b951398 rw-/rw-   __DATA            
	sz=0x00000188 off=0x0494d100-0x0494d288 addr=0xfffffe000b951100-0xfffffe000b951288               __DATA.__data             
	sz=0x00000100 off=0x00000000-0x00000100 addr=0xfffffe000b951288-0xfffffe000b951388               __DATA.__common           (Zerofill)
	sz=0x00000010 off=0x00000000-0x00000010 addr=0xfffffe000b951388-0xfffffe000b951398               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001d50 off=0x0110faf0-0x01111840 addr=0xfffffe0008113af0-0xfffffe0008115840 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x0110faf0-0x0110fb00 addr=0xfffffe0008113af0-0xfffffe0008113b00         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x0110fb00-0x0110fb10 addr=0xfffffe0008113b00-0xfffffe0008113b10         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001868 off=0x0110fb10-0x01111378 addr=0xfffffe0008113b10-0xfffffe0008115378         __DATA_CONST.__const            
	sz=0x00000180 off=0x01111378-0x011114f8 addr=0xfffffe0008115378-0xfffffe00081154f8         __DATA_CONST.__kalloc_type      
	sz=0x00000140 off=0x011114f8-0x01111638 addr=0xfffffe00081154f8-0xfffffe0008115638         __DATA_CONST.__kalloc_var       
	sz=0x00000178 off=0x01111638-0x011117b0 addr=0xfffffe0008115638-0xfffffe00081157b0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000088 off=0x011117b0-0x01111838 addr=0xfffffe00081157b0-0xfffffe0008115838         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x01111838-0x01111840 addr=0xfffffe0008115838-0xfffffe0008115840         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 111 at 0x04adcf84
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     727E302C-B745-3BFB-AE7E-7D11F1488076
008: LC_SOURCE_VERSION           600.3.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa5278 size=0x100
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleIISController`
- `CFBundleGetInfoString`: `Copyright © 2020 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleIISController`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleIISController`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `600.3`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `600.3`
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
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleIISController.kext`
- `_PrelinkExecutableLoadAddr`: `-2198900442480`
- `_PrelinkExecutableRelativePath`: `AppleIISController`
- `_PrelinkExecutableSize`: `46734`
- `_PrelinkExecutableSourceAddr`: `-2198900442480`
- `_PrelinkKmodInfo`: `-2198828936960`

## Strings (108) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s:%s::%s:%d: this %p, iisCommand %p, iisCommandsPending %#x\n`
- `AppleARMIISCommand`
- `(`
- `iis`
- `%s:%s::%s:%d: this %p, iisCommand %p, iisCommandsPending %#x, target %p\n`
- `site.AppleARMIISDevice`
- `initWithRegistryEntry`
- `initWithController`
- `default-routes`
- `null`
- `setMCLKFrequency`
- `AppleARMFunctionIISRoute`
- `1211111`
- `site.ObjectInfo`
- `<`
- `%s:%s::%s:%d: start failed\n`
- `%s:%s::%s:%d: provider %p, class is \"%s\", from %p, class is \"%s\"\n`
- `ActiveRoutes`
- `IOPlatformWakeAction`
- `121111121222121212122211111111112122222222222222222222222222222222222222222222222222222`
- `%s:%s::%s:%d: this %p, device %p (%s), direction %#x, iisCommand %p\n`
- `121111121222121212122222`
- `12111222111222121122222211111`
- `site.ConnectionInfo`
- `-`
- `%s:%s::%s:%d: this %p, configPtr %p, iisController %p, %d/%#x, %d/%#x\n`
- `setIISConfig`
- `site.AppleARMFunctionIISActive`
- `AppleARMIISSwitch`
- `>`
- ` `
- `site.AppleARMIISController`
- `result == 0 `
- `%s:%s::%s:%d: NULL buffer\n`
- `212`
- `%s: routing failed: clock conflict (%s vs %s) for %s\n`
- `(null)`
- `completeIISNoCommand`
- `getIISConfig`
- `%s:%s::%s:%d: this %p, configPtr %p, iisController %p, rv %s\n`
- `%s:%s::%s:%d: %#llx\n`
- `SynthesizedRoutes`
- `AppleARMIISController`
- `%s:%s::%s:%d: device %p (\"%s\") not %p (\"%s\"), Busy\n`
- `%s:%s::%s:%d: this %p, iisCommand=%p != dequeuedIISCommand=%p\n`
- `%s:%s::%s:%d: cast failed, provider class is \"%s\"\n`
- `site.AppleARMFunctionIISRoute`
- `AppleARMFunctionIISActive`
- `completeIISCommand`
- `%s:%s::%s:%d: this %p, configPtr %p, %d/%#x, %d/%#x\n`
- `validIISConfig`
- `transferData`
- `%s:%s::%s:%d: NULL cmd\n`
- `site.AppleARMIISSwitch`
- `121111121222121212111`
- `%s:%s::%s:%d: iisMaxCommands==0\n`
- `true`
- `%s:%s::%s:%d: setMemoryDescriptor failed %#x\n`
- `121111211112`
- `super::configureReport() returned error`
- `IOReporter::updateAllReports returned error`
- `super::updateReport() returned error`
- `AppleARMIISSwitch.cpp`
- `%s:%s::%s:%d: workLoop failed\n`
- `/Library/Caches/com.apple.xbs/9878BC02-3747-40AF-B7F4-9A47EE373EE9/TemporaryDirectory.G9gaGG/Sources/AppleIISController/AppleARMIIS.cpp`
- `site.AppleARMIISCommand`
- `%s::%s:%d: controller %p, rv %s\n`
- `M`
- `(M)`
- `%s: routing failed: could not connect %s: %s\n`
- `%s:%s::%s:%d: commandGate failed\n`
- `AssertMacros: %s, %s file: %s, line: %d, value: %lld\n`
- `enqueueIISCommandGated`
- `%s:%s::%s:%d: this %p, iisCommandsPending %#x\n`
- `init`
- `IOReporter::configureAllReports returned error`
- `AppleARMIISDevice`
- `%s: clock conflict at %s\n`
- `isVirtual`
- `%s:%s::%s:%d: this %p, result %#x, direction %#x, iisConfig.iisTransferDirection %#x, iisTransferDirection %#x\n`
- `false`
- `reg`
- `start`
- `%s:%s::%s:%d: withWorkLoop failed\n`
- `\"%s: error establishing default routes: %s\" @%s:%d`
- `)`

**[__TEXT.__os_log]**

- `%s:%s::%s:%d: commandGate failed\n`
- `%s:%s::%s:%d: device %p (\"%s\") not %p (\"%s\"), Busy\n`
- `%s:%s::%s:%d: this %p, configPtr %p, iisController %p, %d/%#x, %d/%#x\n`
- `%s:%s::%s:%d: this %p, configPtr %p, iisController %p, rv %s\n`
- `%s:%s::%s:%d: NULL buffer\n`
- `%s:%s::%s:%d: NULL cmd\n`
- `%s:%s::%s:%d: cast failed, provider class is \"%s\"\n`
- `%s:%s::%s:%d: start failed\n`
- `%s:%s::%s:%d: this %p, result %#x, direction %#x, iisConfig.iisTransferDirection %#x, iisTransferDirection %#x\n`
- `%s:%s::%s:%d: this %p, iisCommand %p, iisCommandsPending %#x\n`
- `%s:%s::%s:%d: this %p, iisCommandsPending %#x\n`
- `%s:%s::%s:%d: %#llx\n`
- `%s:%s::%s:%d: workLoop failed\n`
- `%s:%s::%s:%d: withWorkLoop failed\n`
- `%s:%s::%s:%d: this %p, device %p (%s), direction %#x, iisCommand %p\n`
- `%s:%s::%s:%d: this %p, iisCommand %p, iisCommandsPending %#x, target %p\n`
- `%s:%s::%s:%d: this %p, configPtr %p, %d/%#x, %d/%#x\n`
- `%s:%s::%s:%d: setMemoryDescriptor failed %#x\n`
- `%s:%s::%s:%d: provider %p, class is \"%s\", from %p, class is \"%s\"\n`
- `%s:%s::%s:%d: iisMaxCommands==0\n`
- `%s:%s::%s:%d: this %p, iisCommand=%p != dequeuedIISCommand=%p\n`
- `%s:%s::%s:%d: %s\n`

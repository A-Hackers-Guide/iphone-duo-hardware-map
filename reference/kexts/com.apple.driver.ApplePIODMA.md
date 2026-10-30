# `com.apple.driver.ApplePIODMA`

- Name: ApplePIODMA
- Version: `1`
- UUID: `4014C4BC-493D-3CBB-A3A8-230629A17D96`
- Source version: `764.40.4.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 15.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 15.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 15.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 15.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `ApplePIODMA` | 0xf8 | IOService → IORegistryEntry |
| `ApplePIODMARequest` | 0xa8 | IOCommand |
| `ApplePIODMARequestPool` | 0x70 | IOCommandPool |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001022 off=0x00688e40-0x00689e62 addr=0xfffffe000768ce40-0xfffffe000768de62 r--/r--   __TEXT            
	sz=0x000009fa off=0x00689468-0x00689e62 addr=0xfffffe000768d468-0xfffffe000768de62               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000041c4 off=0x022f70e0-0x022fb2a4 addr=0xfffffe00092fb0e0-0xfffffe00092ff2a4 r-x/r-x   __TEXT_EXEC       
	sz=0x00003f94 off=0x022f70e0-0x022fb074 addr=0xfffffe00092fb0e0-0xfffffe00092ff074          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000230 off=0x022fb074-0x022fb2a4 addr=0xfffffe00092ff074-0xfffffe00092ff2a4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x04983198-0x049832e8 addr=0xfffffe000b987198-0xfffffe000b9872e8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04983198-0x04983260 addr=0xfffffe000b987198-0xfffffe000b987260               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b987260-0xfffffe000b9872e8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000d28 off=0x011847c0-0x011854e8 addr=0xfffffe00081887c0-0xfffffe00081894e8 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x011847c0-0x011847d8 addr=0xfffffe00081887c0-0xfffffe00081887d8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x011847d8-0x011847f0 addr=0xfffffe00081887d8-0xfffffe00081887f0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000970 off=0x011847f0-0x01185160 addr=0xfffffe00081887f0-0xfffffe0008189160         __DATA_CONST.__const            
	sz=0x000000c0 off=0x01185160-0x01185220 addr=0xfffffe0008189160-0xfffffe0008189220         __DATA_CONST.__kalloc_type      
	sz=0x00000140 off=0x01185220-0x01185360 addr=0xfffffe0008189220-0xfffffe0008189360         __DATA_CONST.__kalloc_var       
	sz=0x00000118 off=0x01185360-0x01185478 addr=0xfffffe0008189360-0xfffffe0008189478         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000070 off=0x01185478-0x011854e8 addr=0xfffffe0008189478-0xfffffe00081894e8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 84 at 0x04ae112c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     4014C4BC-493D-3CBB-A3A8-230629A17D96
008: LC_SOURCE_VERSION           764.40.4.0.0
009: LC_FUNCTION_STARTS          offset=0x004aab9a0 size=0x80
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `ApplePIODMA`
- `CFBundleIdentifier`: `com.apple.driver.ApplePIODMA`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `ApplePIODMA`
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
- `NSHumanReadableCopyright`: `Copyright © 2020 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/ApplePIODMA.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898946496`
- `_PrelinkExecutableRelativePath`: `ApplePIODMA`
- `_PrelinkExecutableSize`: `24670`
- `_PrelinkExecutableSourceAddr`: `-2198898946496`
- `_PrelinkKmodInfo`: `-2198828715624`

## Strings (57) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%06lu.%06u %s:@%s %s::%s: couldn't create workLoop\n`
- `%s@%s-debug`
- `%06lu.%06u %s %s::%s: failed super::init\n`
- `piodma-num-address-bits`
- `%06lu.%06u %s:@%s %s::%s: couldn't create request pool\n`
- `%06lu.%06u %s:@%s %s::%s: enqueuing command Tag 0x%x at index %u\n`
- `%06lu.%06u %s %s::%s: couldn't set memory descriptor for command source buffer, result = 0x%x\n`
- `site.uint64_t`
- `ApplePIODMARequest`
- `site.ApplePIODMARequest *`
- `%06lu.%06u %s:@%s %s::%s: couldn't create completionqueue\n`
- `%06lu.%06u Unknown: %s::%s: couldn't generate physical address for buffer, result = 0x%x\n`
- `%06lu.%06u Unknown: %s::%s: generic packet word0 = 0x%x, word1 = 0x%x, word2 = 0x%x, word3 = 0x%x, buffer = 0x%llx, target = 0x%llx\n`
- `%06lu.%06u %s:@%s %s::%s: failed start\n`
- `piodma-byte-alignment`
- `%s-debug`
- `%06lu.%06u Unknown: %s::%s: couldn't set memory descriptor for command destination buffer, result = 0x%x\n`
- `1211111212221212121211111111221`
- `piodma-max-segment-size`
- `%06lu.%06u %s:@%s %s::%s: couldn't create interrupt event source\n`
- `%06lu.%06u %s %s::%s: generic packet word0 = 0x%x, word1 = 0x%x, word2 = 0x%x, word3 = 0x%x, buffer = 0x%llx, target = 0x%llx\n`
- `%06lu.%06u %s:@%s %s::%s: \n`
- `disableGated`
- `site.ApplePIODMARequestPool`
- `121111111111111122222`
- `%06lu.%06u Unknown: %s::%s: failed super::init\n`
- `piodma-id`
- `%06lu.%06u %s:@%s %s::%s: couldn't add event source to workLoop\n`
- `%06lu.%06u %s:@%s %s::%s: request tag 0x%x thread did not wake normally, result = 0x%x\n`
- `start`
- `%06lu.%06u %s %s::%s: couldn't set memory descriptor for command destination buffer, result = 0x%x\n`
- `%06lu.%06u Unknown: %s::%s: couldn't generate physical address for target, result = 0x%x\n`
- `%06lu.%06u Unknown: %s::%s: couldn't set memory descriptor for command source buffer, result = 0x%x\n`
- `%06lu.%06u %s:@%s %s::%s: Couldn't get device memory\n`
- `piodma-max-transfer-size`
- `piodma-base-address`
- `ApplePIODMARequestPool`
- `12112112112222`
- `%06lu.%06u Unknown: %s::%s: couldn't allocate DMA commands\n`
- `%06lu.%06u %s:@%s %s::%s: couldn't copy mapper\n`
- `piodma-fifo-size`
- `executeRequestGated`
- `%06lu.%06u %s %s::%s: couldn't allocate DMA commands\n`
- `%06lu.%06u Unknown: %s::%s: rejecting scalar request of size %llu\n`
- `site.ApplePIODMA`
- `%x`
- `%06lu.%06u %s:@%s %s::%s: couldn't create commandGate\n`
- `%06lu.%06u %s:@%s %s::%s: couldn't map memory\n`
- `1`
- `initWithMapper`
- `enableGated`
- `%06lu.%06u %s %s::%s: couldn't generate physical address for buffer, result = 0x%x\n`
- `prepareGenericPacket`
- `%06lu.%06u %s %s::%s: couldn't generate physical address for target, result = 0x%x\n`
- `ApplePIODMA`
- `site.ApplePIODMARequest`
- `%06lu.%06u %s %s::%s: rejecting scalar request of size %llu\n`

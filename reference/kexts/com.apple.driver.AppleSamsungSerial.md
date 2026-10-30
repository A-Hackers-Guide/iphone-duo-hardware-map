# `com.apple.driver.AppleSamsungSerial`

- Name: AppleSamsungSerial
- Version: `1.0.0d1`
- UUID: `AF7D9BD8-6DAC-3EBB-A3F4-DBD961D5C857`
- Source version: `154.40.1.0.1`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleOnboardSerial`](com.apple.driver.AppleOnboardSerial.md) 1.0, [`com.apple.iokit.IOSerialFamily`](com.apple.iokit.IOSerialFamily.md) 1.0.4, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/uart0`](../devicetree/root__arm-io__uart0.md) | `AppleSamsungSerial` | `uart-1,samsung` |

## IOKit personalities (1) [KC]

### AppleSamsungSerial
- `CFBundleIdentifier`: `com.apple.driver.AppleSamsungSerial`
- `IOClass`: `AppleSamsungSerial`
- `IONameMatch`:
  - `uart-1,samsung`
- `IOPersonalityPublisher`: `com.apple.driver.AppleSamsungSerial`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleSamsungSerial` | 0x128 | AppleMMIOSerial → AppleOnboardSerialBusInterface → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000007a2 off=0x00781320-0x00781ac2 addr=0xfffffe0007785320-0xfffffe0007785ac2 r--/r--   __TEXT            
	sz=0x000001ca off=0x007818f8-0x00781ac2 addr=0xfffffe00077858f8-0xfffffe0007785ac2               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00001ee0 off=0x02725b30-0x02727a10 addr=0xfffffe0009729b30-0xfffffe000972ba10 r-x/r-x   __TEXT_EXEC       
	sz=0x00001d40 off=0x02725b30-0x02727870 addr=0xfffffe0009729b30-0xfffffe000972b870          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001a0 off=0x02727870-0x02727a10 addr=0xfffffe000972b870-0xfffffe000972ba10          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x0499a248-0x0499a348 addr=0xfffffe000b99e248-0xfffffe000b99e348 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0499a248-0x0499a310 addr=0xfffffe000b99e248-0xfffffe000b99e310               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b99e310-0xfffffe000b99e348               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000810 off=0x01226790-0x01226fa0 addr=0xfffffe000822a790-0xfffffe000822afa0 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x01226790-0x01226798 addr=0xfffffe000822a790-0xfffffe000822a798         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x01226798-0x012267a0 addr=0xfffffe000822a798-0xfffffe000822a7a0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000006c8 off=0x012267a0-0x01226e68 addr=0xfffffe000822a7a0-0xfffffe000822ae68         __DATA_CONST.__const            
	sz=0x00000040 off=0x01226e68-0x01226ea8 addr=0xfffffe000822ae68-0xfffffe000822aea8         __DATA_CONST.__kalloc_type      
	sz=0x000000d0 off=0x01226ea8-0x01226f78 addr=0xfffffe000822aea8-0xfffffe000822af78         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000028 off=0x01226f78-0x01226fa0 addr=0xfffffe000822af78-0xfffffe000822afa0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 57 at 0x04ae6bf4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     AF7D9BD8-6DAC-3EBB-A3F4-DBD961D5C857
008: LC_SOURCE_VERSION           154.40.1.0.1
009: LC_FUNCTION_STARTS          offset=0x004ab2d08 size=0x48
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleSamsungSerial`
- `CFBundleIdentifier`: `com.apple.driver.AppleSamsungSerial`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleSamsungSerial`
- `CFBundleNumericVersion`: `16785409`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1.0.0d1`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleSamsungSerial.kext`
- `_PrelinkExecutableLoadAddr`: `-2198897929440`
- `_PrelinkExecutableRelativePath`: `AppleSamsungSerial`
- `_PrelinkExecutableSize`: `12178`
- `_PrelinkExecutableSourceAddr`: `-2198897929440`
- `_PrelinkKmodInfo`: `-2198828621240`

## Strings (20) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.AppleSamsungSerial`
- `no-flow-control`
- `function-rx`
- `uart-version`
- `%s: %s override dma_multiple=%d\n`
- `1211111212221212111112111111112222222`
- `function-tx`
- `line-enable-alt-function`
- `no-multiple-dma`
- `nclk`
- `service-gates`
- `%s_dma_enable`
- `dma-disable`
- `%s_dma_multiple`
- `AppleSamsungSerial`
- `function-cts`
- `function-rts`
- `dma-types`
- `%s: could not find IODMAEventSource for %s\n`
- `%s: Cannot program rate %d.%d buad within acceptable tolerance; programming closest possible rate (%d baud)\n`

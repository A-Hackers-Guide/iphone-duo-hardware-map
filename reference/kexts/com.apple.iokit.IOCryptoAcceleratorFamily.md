# `com.apple.iokit.IOCryptoAcceleratorFamily`

- Name: IOCryptoAcceleratorFamily
- Version: `1.0.1`
- UUID: `09095AC1-904F-3536-ABD9-74F081887EB7`
- Source version: `137.40.2.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOAESAccelerator` | 0x120 | IOCryptoAccelerator → IOService → IORegistryEntry |
| `IOAESAcceleratorCommand` | 0x90 | IOCommand |
| `IOAESAcceleratorUserClient` | 0xe8 | IOUserClient → IOService → IORegistryEntry |
| `IOCryptoAccelerator` | 0x88 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000bbf off=0x009c4020-0x009c4bdf addr=0xfffffe00079c8020-0xfffffe00079c8bdf r--/r--   __TEXT            
	sz=0x00000068 off=0x009c4648-0x009c46b0 addr=0xfffffe00079c8648-0xfffffe00079c86b0               __TEXT.__const            
	sz=0x0000052f off=0x009c46b0-0x009c4bdf addr=0xfffffe00079c86b0-0xfffffe00079c8bdf               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x0000398c off=0x030837e0-0x0308716c addr=0xfffffe000a0877e0-0xfffffe000a08b16c r-x/r-x   __TEXT_EXEC       
	sz=0x0000366c off=0x030837e0-0x03086e4c addr=0xfffffe000a0877e0-0xfffffe000a08ae4c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000320 off=0x03086e4c-0x0308716c addr=0xfffffe000a08ae4c-0xfffffe000a08b16c          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000200 off=0x049ef2e0-0x049ef4e0 addr=0xfffffe000b9f32e0-0xfffffe000b9f34e0 rw-/rw-   __DATA            
	sz=0x00000140 off=0x049ef2e0-0x049ef420 addr=0xfffffe000b9f32e0-0xfffffe000b9f3420               __DATA.__data             
	sz=0x000000c0 off=0x00000000-0x000000c0 addr=0xfffffe000b9f3420-0xfffffe000b9f34e0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001700 off=0x01355e98-0x01357598 addr=0xfffffe0008359e98-0xfffffe000835b598 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x01355e98-0x01355ea8 addr=0xfffffe0008359e98-0xfffffe0008359ea8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x01355ea8-0x01355eb8 addr=0xfffffe0008359ea8-0xfffffe0008359eb8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001408 off=0x01355eb8-0x013572c0 addr=0xfffffe0008359eb8-0xfffffe000835b2c0         __DATA_CONST.__const            
	sz=0x00000100 off=0x013572c0-0x013573c0 addr=0xfffffe000835b2c0-0xfffffe000835b3c0         __DATA_CONST.__kalloc_type      
	sz=0x00000190 off=0x013573c0-0x01357550 addr=0xfffffe000835b3c0-0xfffffe000835b550         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x01357550-0x01357598 addr=0xfffffe000835b550-0xfffffe000835b598         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 109 at 0x04af0f1c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     09095AC1-904F-3536-ABD9-74F081887EB7
008: LC_SOURCE_VERSION           137.40.2.0.0
009: LC_FUNCTION_STARTS          offset=0x004abe270 size=0x80
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOCryptoAcceleratorFamily`
- `CFBundleGetInfoString`: `Crypto Accelerator Family`
- `CFBundleIdentifier`: `com.apple.iokit.IOCryptoAcceleratorFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOCryptoAcceleratorFamily`
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
- `OSBundleCompatibleVersion`: `1.0b1`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOCryptoAcceleratorFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895558624`
- `_PrelinkExecutableRelativePath`: `IOCryptoAcceleratorFamily`
- `_PrelinkExecutableSize`: `24139`
- `_PrelinkExecutableSourceAddr`: `-2198895558624`
- `_PrelinkKmodInfo`: `-2198828272928`

## Strings (42) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `AES-CBC`
- `IOBSD`
- `SecureRootCallBack`
- `IOAESAccelerator::performAES -- unable to prepare cipherText error - %08x (%s)\n`
- `subclass is required to implement performAESQuantum`
- `IOAESAccelerator.cpp`
- `DecryptUsingAESHw 1`
- `IOAES TEST::%s: regular path test - %lld usec/transaction\n`
- `IOAESAcceleratorCommand`
- `121111212122222211`
- `%s_%d`
- `\"Creating Special Keys Twice\" @%s:%d`
- `CrashReporter-ID`
- `DecryptUsingAESHw 2`
- `unique-chip-id`
- `IOAESAcceleratorUserClient`
- `\"Tried to call commandSleep without holding command gate\" @%s:%d`
- `site.IOAESAcceleratorUserClient`
- `IOAES TEST::%s: can't allocate text buffers\n`
- `/chosen`
- `\"subclass is required to implement getAlgorithmName\" @%s:%d`
- `IOCryptoAccelerator.cpp`
- `kern.hv_vmm_present`
- `site.IOAESAccelerator`
- `SecureRoot`
- `IOAESAccelerator::performAES -- unable to prepare plainText error - %08x (%s)\n`
- `12111112122212121111111111111`
- `_internalTest`
- `site.IOCryptoAccelerator`
- `121111121222121212212221121222111121`
- `IOAES TEST::%s: test failed - 0x%x\n`
- `IOAES TEST::%s: regular path test - doing %d iterations at %d bytes\n`
- `IOCryptoAccelerator`
- `12111112122212121`
- `IOAESAccelerator`
- `aes`
- `IOAES TEST::%s: fastpath test - %lld usec/transaction\n`
- `site.IOAESAcceleratorCommand`
- `com.apple.private.IOAESAccelerator.fdr-key-handle`
- `[PASTIS_STACK_PAINTING: %s] USED = %u, REMAINING = %u\n`
- `aesdev`
- `IOAES TEST::%s: fastpath test - doing %d iterations at %d bytes\n`

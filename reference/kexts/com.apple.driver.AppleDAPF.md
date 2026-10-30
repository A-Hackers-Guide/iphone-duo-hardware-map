# `com.apple.driver.AppleDAPF`

- Name: AppleDAPF
- Version: `1`
- UUID: `CD401146-C3E7-3461-AC48-673B7C3C6A78`
- Source version: `12.0.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.4.1, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.4.1, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.4.1, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.4.1, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleDAPF
- `CFBundleIdentifier`: `com.apple.driver.AppleDAPF`
- `IOClass`: `AppleDAPF`
- `IONameMatch`: `dapf,t8020`
- `IOPersonalityPublisher`: `com.apple.driver.AppleDAPF`
- `IOProviderClass`: `AppleARMIODevice`


## C++ classes (1) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleDAPF` | 0x1d8 | IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000096f off=0x00411ce0-0x0041264f addr=0xfffffe0007415ce0-0xfffffe000741664f r--/r--   __TEXT            
	sz=0x00000008 off=0x00412308-0x00412310 addr=0xfffffe0007416308-0xfffffe0007416310               __TEXT.__const            
	sz=0x0000033f off=0x00412310-0x0041264f addr=0xfffffe0007416310-0xfffffe000741664f               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00000e34 off=0x01b5a310-0x01b5b144 addr=0xfffffe0008b5e310-0xfffffe0008b5f144 r-x/r-x   __TEXT_EXEC       
	sz=0x00000d74 off=0x01b5a310-0x01b5b084 addr=0xfffffe0008b5e310-0xfffffe0008b5f084          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000c0 off=0x01b5b084-0x01b5b144 addr=0xfffffe0008b5f084-0xfffffe0008b5f144          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000100 off=0x0493c308-0x0493c408 addr=0xfffffe000b940308-0xfffffe000b940408 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0493c308-0x0493c3d0 addr=0xfffffe000b940308-0xfffffe000b9403d0               __DATA.__data             
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9403d0-0xfffffe000b940408               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000006c0 off=0x010469a8-0x01047068 addr=0xfffffe000804a9a8-0xfffffe000804b068 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x010469a8-0x010469b0 addr=0xfffffe000804a9a8-0xfffffe000804a9b0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x010469b0-0x010469b8 addr=0xfffffe000804a9b0-0xfffffe000804a9b8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000005f0 off=0x010469b8-0x01046fa8 addr=0xfffffe000804a9b8-0xfffffe000804afa8         __DATA_CONST.__const            
	sz=0x00000040 off=0x01046fa8-0x01046fe8 addr=0xfffffe000804afa8-0xfffffe000804afe8         __DATA_CONST.__kalloc_type      
	sz=0x00000060 off=0x01046fe8-0x01047048 addr=0xfffffe000804afe8-0xfffffe000804b048         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000020 off=0x01047048-0x01047068 addr=0xfffffe000804b048-0xfffffe000804b068         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 28 at 0x04ad67bc
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     CD401146-C3E7-3461-AC48-673B7C3C6A78
008: LC_SOURCE_VERSION           12.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9cfa0 size=0x30
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleDAPF`
- `CFBundleIdentifier`: `com.apple.driver.AppleDAPF`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleDAPF`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSignature`: `????`
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
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleDAPF.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901531424`
- `_PrelinkExecutableRelativePath`: `AppleDAPF`
- `_PrelinkExecutableSize`: `8035`
- `_PrelinkExecutableSourceAddr`: `-2198901531424`
- `_PrelinkKmodInfo`: `-2198829006072`

## Strings (23) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `\"DAPF : %s : was previously locked but not enabled\" @%s:%d`
- `\"DAPF: %s : %sreg mismatch - offset 0x(%x). read 0x%llx, but expected 0x%llx\" @%s:%d`
- `start `
- `len `
- `12111112122212121111112222222222222222222222222222222222222`
- `unknown`
- `always-on`
- `range start `
- `\"DAPF: %s : %sfilter reg mismatch - slice(%d) offset 0x(%x). read 0x%llx, but expected 0x%llx\" @%s:%d`
- `AppleDAPF.cpp`
- `role`
- `filter`
- `(%s) %s:%u: filter slice %d length is not %#llx-byte aligned: %#llx`
- `AppleDAPF`
- `site.AppleDAPF`
- `dapf-all`
- `/Library/Caches/com.apple.xbs/DAB96E05-6272-485E-B9D3-B66C5BE3B14E/TemporaryDirectory.2Jwzr6/Sources/AppleDAPF/AppleDAPF.cpp`
- `(%s) %s:%u: filter slice %d start/end is invalid: (%#llx, %#llx)`
- `range len `
- `\"(%s) %s::%s: \" \"Superclass failed to start\" @%s:%d`
- `start`
- `(%s) %s:%u: REQUIRE failed`
- `(%s) %s:%u: filter slice %d start is not %#llx-byte aligned: %#llx`

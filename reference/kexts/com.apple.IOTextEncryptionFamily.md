# `com.apple.IOTextEncryptionFamily`

- Name: IOTextEncryptionFamily
- Version: `1.0.0`
- UUID: `7FB838AC-58BF-3D92-A694-4A03F4626432`
- Source version: `28.0.0.0.0`
- Depends on: [`com.apple.driver.FairPlayIOKit`](com.apple.driver.FairPlayIOKit.md) 3.8, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 9.3.1

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleFairplayTextCrypter
- `CFBundleIdentifier`: `com.apple.IOTextEncryptionFamily`
- `IOClass`: `AppleFairplayTextCrypter`
- `IOMatchCategory`: `AppleFairplayTextCrypter`
- `IOPersonalityPublisher`: `com.apple.IOTextEncryptionFamily`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOBSD`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleFairplayTextCrypter` | 0xa0 | IOTextCrypter → IOService → IORegistryEntry |
| `AppleFairplayTextCrypterSession` | 0x38 | TextCrypterSession |
| `IOTextCrypter` | 0x88 | IOService → IORegistryEntry |
| `TextCrypterSession` | 0x20 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000887 off=0x00a67200-0x00a67a87 addr=0xfffffe0007a6b200-0xfffffe0007a6ba87 r--/r--   __TEXT            
	sz=0x000002af off=0x00a677d8-0x00a67a87 addr=0xfffffe0007a6b7d8-0xfffffe0007a6ba87               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x000019b4 off=0x0341dc50-0x0341f604 addr=0xfffffe000a421c50-0xfffffe000a423604 r-x/r-x   __TEXT_EXEC       
	sz=0x00001854 off=0x0341dc50-0x0341f4a4 addr=0xfffffe000a421c50-0xfffffe000a4234a4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000160 off=0x0341f4a4-0x0341f604 addr=0xfffffe000a4234a4-0xfffffe000a423604          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000180 off=0x04a175d8-0x04a17758 addr=0xfffffe000ba1b5d8-0xfffffe000ba1b758 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a175d8-0x04a176a0 addr=0xfffffe000ba1b5d8-0xfffffe000ba1b6a0               __DATA.__data             
	sz=0x000000b8 off=0x00000000-0x000000b8 addr=0xfffffe000ba1b6a0-0xfffffe000ba1b758               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001050 off=0x013fc108-0x013fd158 addr=0xfffffe0008400108-0xfffffe0008401158 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x013fc108-0x013fc110 addr=0xfffffe0008400108-0xfffffe0008400110         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x013fc110-0x013fc118 addr=0xfffffe0008400110-0xfffffe0008400118         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000e68 off=0x013fc118-0x013fcf80 addr=0xfffffe0008400118-0xfffffe0008400f80         __DATA_CONST.__const            
	sz=0x00000100 off=0x013fcf80-0x013fd080 addr=0xfffffe0008400f80-0xfffffe0008401080         __DATA_CONST.__kalloc_type      
	sz=0x000000b0 off=0x013fd080-0x013fd130 addr=0xfffffe0008401080-0xfffffe0008401130         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000028 off=0x013fd130-0x013fd158 addr=0xfffffe0008401130-0xfffffe0008401158         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 49 at 0x04af8900
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     7FB838AC-58BF-3D92-A694-4A03F4626432
008: LC_SOURCE_VERSION           28.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac6150 size=0x68
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOTextEncryptionFamily`
- `CFBundleIdentifier`: `com.apple.IOTextEncryptionFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOTextEncryptionFamily`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `????`
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
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOTextEncryptionFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198894890496`
- `_PrelinkExecutableRelativePath`: `IOTextEncryptionFamily`
- `_PrelinkExecutableSize`: `13323`
- `_PrelinkExecutableSourceAddr`: `-2198894890496`
- `_PrelinkKmodInfo`: `-2198828108328`

## Strings (22) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `1211`
- `AppleFairplayTextCrypter`
- `site.AppleFairplayTextCrypter`
- `com_apple_driver_FairPlayIOKit`
- `\"%s: Unknown origin indicator %d\\n\" @%s:%d`
- `site.IOTextCrypter`
- `site.TextCrypterSession`
- `12111112122212121111`
- `com.apple.unfree`
- `\"AppleFairplayTextCrypter::sessionDidEnd(): no session!\" @%s:%d`
- `newCryptSession`
- `Production hardware. Debug must be disabled for decrypter to work.\n`
- `\"IOTextCrypter::endCryptSession: no session!\" @%s:%d`
- `TextCrypterSession`
- `AppleFairplayTextCrypterSession`
- `site.AppleFairplayTextCrypterSession`
- `AppleFairplayTextCrypterSession::fairplayOpen() failed, error %ld\n`
- `12111112122212121`
- `1211122`
- `IOTextCrypter`
- `\"IOTextCrypter::decryptPage: no session!\" @%s:%d`
- `IOTextEncryptionFamily.cpp`

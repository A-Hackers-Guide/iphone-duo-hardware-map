# `com.apple.driver.IOAudioCodecs`

- Name: IOAudioCodecs
- Version: `1.0.0`
- UUID: `4EFE50D2-74B5-3027-9DF3-F6AB1325E008`
- Source version: `210.2.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.FairPlayIOKit`](com.apple.driver.FairPlayIOKit.md) 3.3.0d1, [`com.apple.kec.Libm`](com.apple.kec.Libm.md) 1.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### IOAudioCodecs
- `CFBundleIdentifier`: `com.apple.driver.IOAudioCodecs`
- `IOClass`: `IOAudioCodecs`
- `IOMatchCategory`: `IOAudioCodecs`
- `IOPersonalityPublisher`: `com.apple.driver.IOAudioCodecs`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `IOAudioCodecsUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOAudioCodecs` | 0xa8 | IOService → IORegistryEntry |
| `IOAudioCodecsUserClient` | 0x100 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00002f48 off=0x009bda60-0x009c09a8 addr=0xfffffe00079c1a60-0xfffffe00079c49a8 r--/r--   __TEXT            
	sz=0x000004f6 off=0x009be128-0x009be61e addr=0xfffffe00079c2128-0xfffffe00079c261e               __TEXT.__cstring          (CstringLiterals)
	sz=0x00002388 off=0x009be620-0x009c09a8 addr=0xfffffe00079c2620-0xfffffe00079c49a8               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x0000cfdc off=0x03064d10-0x03071cec addr=0xfffffe000a068d10-0xfffffe000a075cec r-x/r-x   __TEXT_EXEC       
	sz=0x0000cd8c off=0x03064d10-0x03071a9c addr=0xfffffe000a068d10-0xfffffe000a075a9c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000250 off=0x03071a9c-0x03071cec addr=0xfffffe000a075a9c-0xfffffe000a075cec          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x049eec48-0x049eed70 addr=0xfffffe000b9f2c48-0xfffffe000b9f2d70 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049eec48-0x049eed10 addr=0xfffffe000b9f2c48-0xfffffe000b9f2d10               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9f2d10-0xfffffe000b9f2d70               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00002ee8 off=0x0134de00-0x01350ce8 addr=0xfffffe0008351e00-0xfffffe0008354ce8 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x0134de00-0x0134de10 addr=0xfffffe0008351e00-0xfffffe0008351e10         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x0134de10-0x0134de20 addr=0xfffffe0008351e10-0xfffffe0008351e20         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000021e8 off=0x0134de20-0x01350008 addr=0xfffffe0008351e20-0xfffffe0008354008         __DATA_CONST.__const            
	sz=0x000006c0 off=0x01350008-0x013506c8 addr=0xfffffe0008354008-0xfffffe00083546c8         __DATA_CONST.__kalloc_type      
	sz=0x000004b0 off=0x013506c8-0x01350b78 addr=0xfffffe00083546c8-0xfffffe0008354b78         __DATA_CONST.__kalloc_var       
	sz=0x00000128 off=0x01350b78-0x01350ca0 addr=0xfffffe0008354b78-0xfffffe0008354ca0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000040 off=0x01350ca0-0x01350ce0 addr=0xfffffe0008354ca0-0xfffffe0008354ce0         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x01350ce0-0x01350ce8 addr=0xfffffe0008354ce0-0xfffffe0008354ce8         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 82 at 0x04af0af0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     4EFE50D2-74B5-3027-9DF3-F6AB1325E008
008: LC_SOURCE_VERSION           210.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004abdd70 size=0x200
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `IOAudioCodecs`
- `CFBundleGetInfoString`: `1.0.0, Copyright Apple Computer, Inc. 2011`
- `CFBundleIdentifier`: `com.apple.driver.IOAudioCodecs`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOAudioCodecs`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
- `CFBundleSignature`: `aapl`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOAudioCodecs.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895584672`
- `_PrelinkExecutableRelativePath`: `IOAudioCodecs`
- `_PrelinkExecutableSize`: `77620`
- `_PrelinkExecutableSourceAddr`: `-2198895584672`
- `_PrelinkKmodInfo`: `-2198828274616`

## Strings (31) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `122222222222121121111111111111122222`
- `GetSyncFrameSize`
- `1212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220221220222012122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220221220`
- `122222222222`
- `1121112`
- `IOAudioCodecs`
- `21`
- `site.T`
- `site.IOAudioCodecsUserClient`
- `ERROR: terminate() failed.\n\n`
- `A5AC3PassThrough::%s insufficient input packet\n`
- `\"AudioCodecWrapper::Initialize error, all of these should be null: m_InputData %p m_OutputData %p m_ShadowInputData %p\\n\" @%s:%d`
- `121111121222121211111`
- `A5AudioCodec: can't allocate memory`
- `A5EC3PassThrough::%s unknowd bsid value %d\n`
- `A5AC3PassThrough::%s missing sync word\n`
- `\"abort()\" @%s:%d`
- `abort.c`
- `site.IOAudioCodecs`
- `12111112122212121111111111111121`
- `magic cookie`
- `1212122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222220221220`
- `A5EC3PassThrough::%s missing sync word\n`
- `A5AC3PassThrough::%s input packet too large for output packet\n`
- `com_apple_driver_FairPlayIOKit`
- `ERROR: Failed to decrypt a packet with a crypto key(%p)\n`
- `AudioCodecWrapper.cpp`
- `setProperties`
- `ProcessSinglePacket`
- `IOAudioCodecsUserClient`
- `%s[%p]::%s: property not dictionary\n\n`

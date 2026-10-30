# `com.apple.driver.AppleFirmwareUpdateKext`

- Name: AppleFirmwareUpdateKext
- Version: `1`
- UUID: `1010FA20-9BCE-3B10-9D1C-E8098261DE77`
- Source version: `1587.40.33.0.0`
- Depends on: [`com.apple.kec.corecrypto`](com.apple.kec.corecrypto.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0, [`com.apple.security.AppleImage4`](com.apple.security.AppleImage4.md) 3.0.0, [`com.apple.security.Image4`](com.apple.security.Image4.md) 1.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleFirmwareUpdateKext` | 0x148 | IOService → IORegistryEntry |
| `AppleFirmwareUpdateUserClient` | 0xe8 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1400)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000e5d off=0x00471ab0-0x0047290d addr=0xfffffe0007475ab0-0xfffffe000747690d r--/r--   __TEXT            
	sz=0x00000885 off=0x00472088-0x0047290d addr=0xfffffe0007476088-0xfffffe000747690d               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00002708 off=0x01cfc0f0-0x01cfe7f8 addr=0xfffffe0008d000f0-0xfffffe0008d027f8 r-x/r-x   __TEXT_EXEC       
	sz=0x000024c8 off=0x01cfc0f0-0x01cfe5b8 addr=0xfffffe0008d000f0-0xfffffe0008d025b8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000240 off=0x01cfe5b8-0x01cfe7f8 addr=0xfffffe0008d025b8-0xfffffe0008d027f8          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x049420e0-0x04942208 addr=0xfffffe000b9460e0-0xfffffe000b946208 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049420e0-0x049421a8 addr=0xfffffe000b9460e0-0xfffffe000b9461a8               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9461a8-0xfffffe000b946208               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000e68 off=0x010ae720-0x010af588 addr=0xfffffe00080b2720-0xfffffe00080b3588 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x010ae720-0x010ae730 addr=0xfffffe00080b2720-0xfffffe00080b2730         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x010ae730-0x010ae740 addr=0xfffffe00080b2730-0xfffffe00080b2740         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000c70 off=0x010ae740-0x010af3b0 addr=0xfffffe00080b2740-0xfffffe00080b33b0         __DATA_CONST.__const            
	sz=0x00000080 off=0x010af3b0-0x010af430 addr=0xfffffe00080b33b0-0xfffffe00080b3430         __DATA_CONST.__kalloc_type      
	sz=0x00000120 off=0x010af430-0x010af550 addr=0xfffffe00080b3430-0xfffffe00080b3550         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000038 off=0x010af550-0x010af588 addr=0xfffffe00080b3550-0xfffffe00080b3588         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 79 at 0x04ada12c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     1010FA20-9BCE-3B10-9D1C-E8098261DE77
008: LC_SOURCE_VERSION           1587.40.33.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa0778 size=0x68
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleFirmwareUpdateKext`
- `CFBundleIdentifier`: `com.apple.driver.AppleFirmwareUpdateKext`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleFirmwareUpdateKext`
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
- `LSApplicationCategoryType`: ``
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2016 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleFirmwareUpdateKext.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901138768`
- `_PrelinkExecutableRelativePath`: `AppleFirmwareUpdateKext`
- `_PrelinkExecutableSize`: `17653`
- `_PrelinkExecutableSourceAddr`: `-2198901138768`
- `_PrelinkKmodInfo`: `-2198828982048`

## Strings (58) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `validateFirmware`
- `%s[%p]::%s() Only non signed FDR data supported\n`
- `loadFDRDataComplete`
- `%s[%p]::%s() commandSleep interrupted, validateImage4Completed = %s\n`
- `%s::%s(): Calling external handler for manifest tag 0x%08x\n`
- `12111112122212121111111111111`
- `%s[%p]::%s() Invalid _firmwareDescriptor\n`
- `%s[%p]::%s() commandSleep awakened, validateImage4Completed = %s\n`
- `12111112122212121111111111111111122222222`
- `loadFirmware`
- `%s[%p]::%s() Boot-arg present, skipping firmware validation\n`
- `validateImage4`
- `%s[%p]::%s() No FDR callback registered\n`
- `Image Tag`
- `IOUserClientClass`
- `com.apple.afu.userclientaccess`
- `%s[%p]::%s() Return value from inputMD->prepare(): %d\n`
- `%s[%p]::%s() Invalid map\n`
- `AppleFirmwareUpdateKext`
- `%s::%s() Time Taken For IMG4 Validation: %llu ms\n`
- `%s[%p]::%s() No loadFDRDataComplete callback registered\n`
- `AppleFirmwareUpdateUserClient`
- `UserSpaceRequestTimeMs`
- `KernelClientRequestTimeMs`
- `%s[%p]::%s() kFWValidationFailed: %u\n`
- `site.AppleFirmwareUpdateKext`
- `%s[%p]::%s() Invalid _firmwareBuffer\n`
- `ValidationTimeMs`
- `%s[%p]::%s() bufferLength must be > classLength (%u > %u)\n`
- `%s[%p]::%s() Invalid _firmwareMap\n`
- `validateFirmwareGated`
- `true`
- `FDR Classes`
- `%s[%p]::%s() Cannot create fdrClassBuffer\n`
- `%s::%s(): Unhandled manifest tag 0x%08x\n`
- `loadFDRData`
- `%s[%p]::%s() No FDR data received\n`
- `%s Task  not privileged \n`
- `%s::%s() Total Time Taken For Kernel Client's to complete: %llu ms\n`
- `false`
- `virtual IOReturn AppleFirmwareUpdateUserClient::externalMethod(uint32_t, IOExternalMethodArguments *, IOExternalMethodDispatch *, OSObject *, void *)`
- `%s[%p]::%s() Cannot create fdrClass\n`
- `skipFWValidation`
- `%s[%p]::%s() commandSleep waitResult = %d, validateImage4Completed = %s\n`
- `%s[%p]::%s() Exiting with status = 0x%x \n`
- `%s::%s() Performing img4 validation outside of workloop\n`
- `%s[%p]::%s() status = 0x%x, Disabling event source\n`
- `%s[%p]::%s() Entering \n`
- `%s[%p]::%s() commandSleep timed out, validateImage4Completed = %s\n`
- `validationComplete`
- `performCustomValidation`
- `skip-image-loading`
- `site.AppleFirmwareUpdateUserClient`
- `%s[%p]::%s() Cannot create fdrData\n`
- `Need FUD Download`
- `%s[%p]::%s() No FDR class received\n`
- `%s[%p]::%s() %s is working asynchronously\n`
- `%s::%s() Total Time Taken For User Space Request to complete: %llu ms\n`

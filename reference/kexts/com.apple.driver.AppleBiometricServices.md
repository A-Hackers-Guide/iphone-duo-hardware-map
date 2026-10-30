# `com.apple.driver.AppleBiometricServices`

- Name: AppleBiometricServices
- Version: `1`
- UUID: `133BB9CF-1929-3F28-B5D5-E0DB701D73AE`
- Source version: `10321.40.10.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleMesaSEPDriver`](com.apple.driver.AppleMesaSEPDriver.md) 1.0.0, [`com.apple.iokit.IOBiometricFamily`](com.apple.iokit.IOBiometricFamily.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleBiometricServices
- `CFBundleIdentifier`: `com.apple.driver.AppleBiometricServices`
- `IOClass`: `AppleBiometricServices`
- `IOMatchCategory`: `com_apple_driver_AppleBiometricServices`
- `IOPersonalityPublisher`: `com.apple.driver.AppleBiometricServices`
- `IOProviderClass`: `AppleMesaSEPDriver`
- `IOUserClientClass`: `AppleBiometricServicesUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleBiometricServices` | 0x90 | IOService → IORegistryEntry |
| `AppleBiometricServicesUserClient` | 0xe8 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000fa8 off=0x003b8100-0x003b90a8 addr=0xfffffe00073bc100-0xfffffe00073bd0a8 r--/r--   __TEXT            
	sz=0x0000041f off=0x003b8728-0x003b8b47 addr=0xfffffe00073bc728-0xfffffe00073bcb47               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000561 off=0x003b8b47-0x003b90a8 addr=0xfffffe00073bcb47-0xfffffe00073bd0a8               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00000f60 off=0x01a10500-0x01a11460 addr=0xfffffe0008a14500-0xfffffe0008a15460 r-x/r-x   __TEXT_EXEC       
	sz=0x00000e60 off=0x01a10500-0x01a11360 addr=0xfffffe0008a14500-0xfffffe0008a15360          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000100 off=0x01a11360-0x01a11460 addr=0xfffffe0008a15360-0xfffffe0008a15460          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000148 off=0x04934018-0x04934160 addr=0xfffffe000b938018-0xfffffe000b938160 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x04934018-0x049340dc addr=0xfffffe000b938018-0xfffffe000b9380dc               __DATA.__data             
	sz=0x00000080 off=0x00000000-0x00000080 addr=0xfffffe000b9380e0-0xfffffe000b938160               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000dc0 off=0x00ffa710-0x00ffb4d0 addr=0xfffffe0007ffe710-0xfffffe0007fff4d0 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x00ffa710-0x00ffa720 addr=0xfffffe0007ffe710-0xfffffe0007ffe720         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x00ffa720-0x00ffa730 addr=0xfffffe0007ffe720-0xfffffe0007ffe730         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000c70 off=0x00ffa730-0x00ffb3a0 addr=0xfffffe0007ffe730-0xfffffe0007fff3a0         __DATA_CONST.__const            
	sz=0x00000080 off=0x00ffb3a0-0x00ffb420 addr=0xfffffe0007fff3a0-0xfffffe0007fff420         __DATA_CONST.__kalloc_type      
	sz=0x00000080 off=0x00ffb420-0x00ffb4a0 addr=0xfffffe0007fff420-0xfffffe0007fff4a0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000030 off=0x00ffb4a0-0x00ffb4d0 addr=0xfffffe0007fff4a0-0xfffffe0007fff4d0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 38 at 0x04ad415c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     133BB9CF-1929-3F28-B5D5-E0DB701D73AE
008: LC_SOURCE_VERSION           10321.40.10.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9af50 size=0x30
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleBiometricServices`
- `CFBundleIdentifier`: `com.apple.driver.AppleBiometricServices`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleBiometricServices`
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
- `NSHumanReadableCopyright`: `Copyright © 2012 Apple. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleBiometricServices.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901899008`
- `_PrelinkExecutableRelativePath`: `AppleBiometricServices`
- `_PrelinkExecutableSize`: `11792`
- `_PrelinkExecutableSourceAddr`: `-2198901899008`
- `_PrelinkKmodInfo`: `-2198829039592`

## Strings (41) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `ERROR: AppleBiometricServices::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n`
- `performCommand`
- `err == 0 `
- `site.AppleBiometricServices`
- `_provider`
- `message`
- `site.AppleBiometricServicesUserClient`
- `12111112122212121111111111111`
- `AppleBiometricServices-UserClient`
- `extPerform`
- `ERROR: AppleBiometricServicesUserClient::%s: AssertMacros: %s (value = 0x%lx), %s file: %s, line: %d\n\n\n`
- `AppleBiometricServices`
- `121111121222121211`
- `com.apple.BiometricKit`
- `result`
- `stop`
- `AppleBiometricServicesUserClient`
- `initWithTask`
- `ERROR: AppleBiometricServicesUserClient::%s: terminate() failed.\n\n`
- `start`
- `/Library/Caches/com.apple.xbs/689DFD13-7801-4997-BC10-72E9357F1AF3/TemporaryDirectory.WXiexE/Sources/Mesa/AppleBiometricServices/AppleBiometricServices/AppleBiometricServices.cpp`
- `type == (UInt32)(((signed)((((unsigned)(0x38))&0x3f)<<26))|(((-2)&0xfff)<<14)|0)`
- `clientClose`
- `externalMethod`
- `/Library/Caches/com.apple.xbs/689DFD13-7801-4997-BC10-72E9357F1AF3/TemporaryDirectory.WXiexE/Sources/Mesa/AppleBiometricServices/AppleBiometricServices/AppleBiometricServicesUserClient.cpp`

**[__TEXT.__os_log]**

- `AppleBiometricServicesUserClient::%s <- selector:%u, arguments:%p, dispatch:%p, target:%p, reference:%p\n`
- `AppleBiometricServices::%s <- provider:%p\n`
- `AppleBiometricServices::%s <- provider:%p --> void\n`
- `AppleBiometricServicesUserClient::%s <- owningTask:%p, securityToken:%p, type:%u, properties:%p\n`
- `AppleBiometricServicesUserClient::%s -> kIOReturnSuccess\n`
- `AppleBiometricServices::%s <- inData:%p, outData:%p, outSize:%p --> _provider->performCommand\n`
- `AppleBiometricServicesUserClient::%s -> success:%d\n`
- `AppleBiometricServicesUserClient::%s <- \n`
- `AppleBiometricServicesUserClient::%s <- provider:%p\n`
- `AppleBiometricServicesUserClient::%s <- inObj:%p, inRef:%p, inArg:%p\n`
- `AppleBiometricServicesUserClient::%s -> err:0x%x\n`
- `Couldn't create OS Log for 'com.apple.BiometricKit.AppleBiometricServices'!\n`
- `AppleBiometricServices::%s -> result:%d\n`
- `Couldn't create OS Log for 'com.apple.BiometricKit.AppleBiometricServices-UserClient'!\n`
- `AppleBiometricServicesUserClient::%s <- provider:%p --> super::stop\n`
- `AppleBiometricServicesUserClient::%s: in md = %p out md = %p  out md size %d\n\n`

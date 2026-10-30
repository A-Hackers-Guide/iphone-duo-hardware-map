# `com.apple.driver.FairPlayIOKit`

- Name: FairPlayIOKit
- Version: `72.19.0`
- UUID: `7C63C4E7-6602-33C2-A30A-6EC4BA5034BA`
- Source version: `72.19.0.0.0`
- Depends on: [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0, [`com.apple.kpi.dsep`](com.apple.kpi.dsep.md) 16.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 9.3.1

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### FairPlayIOKit
- `CFBundleIdentifier`: `com.apple.driver.FairPlayIOKit`
- `IOClass`: `com_apple_driver_FairPlayIOKit`
- `IOKitDebug`: `0`
- `IOMatchCategory`: `FairPlayIOKit`
- `IOPersonalityPublisher`: `com.apple.driver.FairPlayIOKit`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOKit`
- `IOUserClientClass`: `com_apple_driver_FairPlayIOKitUserClient`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `FPMemoryDescriptor` | 0x30 |  |
| `com_apple_driver_FairPlayIOKit` | 0x88 | IOService → IORegistryEntry |
| `com_apple_driver_FairPlayIOKitUserClient` | 0xf8 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000440b0 off=0x0092ac30-0x0096ece0 addr=0xfffffe000792ec30-0xfffffe0007972ce0 r--/r--   __TEXT            
	sz=0x00001d84 off=0x0092b2f8-0x0092d07c addr=0xfffffe000792f2f8-0xfffffe000793107c               __TEXT.__cstring          (CstringLiterals)
	sz=0x00041c60 off=0x0092d080-0x0096ece0 addr=0xfffffe0007931080-0xfffffe0007972ce0               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00235ea4 off=0x02c75e20-0x02eabcc4 addr=0xfffffe0009c79e20-0xfffffe0009eafcc4 r-x/r-x   __TEXT_EXEC       
	sz=0x002359c4 off=0x02c75e20-0x02eab7e4 addr=0xfffffe0009c79e20-0xfffffe0009eaf7e4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000004e0 off=0x02eab7e4-0x02eabcc4 addr=0xfffffe0009eaf7e4-0xfffffe0009eafcc4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00004000 off=0x049dc710-0x049e0710 addr=0xfffffe000b9e0710-0xfffffe000b9ef480 rw-/rw-   __DATA            
	sz=0x000011c0 off=0x049dc710-0x049dd8d0 addr=0xfffffe000b9e0710-0xfffffe000b9e18d0               __DATA.__data             
	sz=0x0000db78 off=0x00000000-0x0000db78 addr=0xfffffe000b9e18d0-0xfffffe000b9ef448               __DATA.__common           (Zerofill)
	sz=0x00000038 off=0x00000000-0x00000038 addr=0xfffffe000b9ef448-0xfffffe000b9ef480               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000178b0 off=0x012de520-0x012f5dd0 addr=0xfffffe00082e2520-0xfffffe00082f9dd0 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x012de520-0x012de538 addr=0xfffffe00082e2520-0xfffffe00082e2538         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x012de538-0x012de550 addr=0xfffffe00082e2538-0xfffffe00082e2550         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00015718 off=0x012de550-0x012f3c68 addr=0xfffffe00082e2550-0xfffffe00082f7c68         __DATA_CONST.__const            
	sz=0x00001e80 off=0x012f3c68-0x012f5ae8 addr=0xfffffe00082f7c68-0xfffffe00082f9ae8         __DATA_CONST.__kalloc_type      
	sz=0x00000270 off=0x012f5ae8-0x012f5d58 addr=0xfffffe00082f9ae8-0xfffffe00082f9d58         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000068 off=0x012f5d58-0x012f5dc0 addr=0xfffffe00082f9d58-0xfffffe00082f9dc0         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000010 off=0x012f5dc0-0x012f5dd0 addr=0xfffffe00082f9dc0-0xfffffe00082f9dd0         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 169 at 0x04aef33c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     7C63C4E7-6602-33C2-A30A-6EC4BA5034BA
008: LC_SOURCE_VERSION           72.19.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aba0d8 size=0x300
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleDisplayName`: `FairPlayIOKit`
- `CFBundleExecutable`: `FairPlayIOKit`
- `CFBundleIdentifier`: `com.apple.driver.FairPlayIOKit`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `FairPlayIOKit`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `72.19.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `72.19.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2008-2019 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `3.3.0d1`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/FairPlayIOKit.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896186320`
- `_PrelinkExecutableRelativePath`: `FairPlayIOKit`
- `_PrelinkExecutableSize`: `2753908`
- `_PrelinkExecutableSourceAddr`: `-2198896186320`
- `_PrelinkKmodInfo`: `-2198828349680`

## Strings (90) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.FPMemoryDescriptor`
- `site.com_apple_driver_FairPlayIOKitUserClient`
- `1211111212221212111111111111112`
- `com.apple.private.ProvInfoIOKitUserClient.access`
- `[com_apple_driver_FairPlayIOKitUserClient::ucEncryptSUInfo] Error: bad input structure length\n`
- `[com_apple_driver_FairPlayIOKit::encryptWithWrappedKey] Error: invalid input parameters\n`
- `Assertion failure: %s == %d [File: %s:%u]`
- `[com_apple_driver_FairPlayIOKit::generateSeed] IOService::serviceMatching returned NULL\n`
- `[com_apple_driver_FairPlayIOKit::generateInFieldSeed] 2nd IOAESAccelerator::performAES randomV returned %d\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOAESAccelerator::performAES scrambler returned 0x%x\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOAESAccelerator::performAES (UID) returned %d\n`
- `com.apple.private.FairPlayIOKitUserClient.access`
- `[com_apple_driver_FairPlayIOKit::generateSeed] Error: null pointer detected\n`
- `[com_apple_driver_FairPlayIOKit::generateSeed] IOAESAccelerator::performAES UID returned 0x%x\n`
- `AppleSTDP2700`
- `[com_apple_driver_FairPlayIOKit::encryptSUInfo] Error: invalid input parameters\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucGenerateSeed] Error: null pointer parameter\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucEncryptSUInfo] Error: null pointer for input parameter\n`
- `IODeviceTree:/product`
- `[com_apple_driver_FairPlayIOKit::GetProductID] Error: The ProductID length doesn't match!!!\n`
- `[com_apple_driver_FairPlayIOKit::isJ42dDevice] Error: GetProductID() returns %x\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] Bad VSegInfoLength for In-Field Seed detected\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] Failed to get product ID\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOBufferMemoryDescriptor::prepare returned %d\n`
- `/Library/Caches/com.apple.xbs/CE3AD0E4-13B6-4A91-AB52-4FC2760744E8/TemporaryDirectory.wpg3zC/Sources/FairPlayIOKit/FairPlayIOKit/src/LSKD/FairPlayIOKit_LSKD.cpp`
- `[FairPlayIOKitUserClient::initWithTask] Error: caller does not have a valid entitlement\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucExchangeWithHoover] ProvInfoIOKit::exchangeWithHoover returned %d\n`
- `product-id`
- `[com_apple_driver_FairPlayIOKit::generateInFieldSeed] IOBufferMemoryDescriptor::inTaskWithOptions returned NULL\n`
- `[com_apple_driver_FairPlayIOKit::encryptWithWrappedKey] IOService::serviceMatching returned NULL\n`
- `Failed to create a vfs context\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucEncryptSUInfo] ProvInfoIOKit::encryptedSUInfo returned %d\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucEncryptWithWrappedKey] bad input structure length\n`
- `[FairPlayIOKitUserClient::ucSendFPMessage got error back from FPIOKit->SendFPMessage %d \n`
- `IOAESAccelerator`
- `[com_apple_driver_FairPlayIOKit::encryptWithWrappedKey] IOBufferMemoryDescriptor::inTaskWithOptions returned NULL\n`
- `/Library/Caches/com.apple.xbs/CE3AD0E4-13B6-4A91-AB52-4FC2760744E8/TemporaryDirectory.wpg3zC/Sources/FairPlayIOKit/FairPlayIOKit/src/common/FairPlayUtilities.cpp`
- `[com_apple_driver_FairPlayIOKitUserClient::ucEncryptWithWrappedKey] ProvInfoIOKit::ucEncryptWithWrappedKey returned %d\n`
- `[com_apple_driver_FairPlayIOKit::exchangeWithHoover] IOService::serviceMatching returned NULL (probably means no Hoover on the device)\n`
- `Warning: arc4random not implemented\n`
- `[com_apple_driver_FairPlayIOKit::exchangeWithHoover] Hoover response is larger than response buffer (%u vs %u)\n`
- `FPMemoryDescriptor`
- `[com_apple_driver_FairPlayIOKit::generateSeed] IOBufferMemoryDescriptor::prepare returned %d\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] unsupported seed segment offset\n`
- `[com_apple_driver_FairPlayIOKit::encryptSUInfo] IOAESAccelerator::performAES returned %d\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucGenerateSeed] Error: ProvInfoIOKit::generateSeed returned %d\n`
- `[com_apple_driver_FairPlayIOKit::generateSeed] Returned error: %x\n`
- `[com_apple_driver_FairPlayIOKit::exchangeWithHoover] Error: null pointer detected\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOAESAccelerator::performAES GID returned 0x%x\n`
- `[com_apple_driver_FairPlayIOKit::encryptSUInfo] IOBufferMemoryDescriptor::prepare returned %d\n`
- `/Library/Caches/com.apple.xbs/CE3AD0E4-13B6-4A91-AB52-4FC2760744E8/TemporaryDirectory.wpg3zC/Sources/FairPlayIOKit/FairPlayIOKit/src/crypto/FairPlayCryptoUtilities.cpp`
- `121112`
- `com_apple_driver_FairPlayIOKitUserClient`
- `[com_apple_driver_FairPlayIOKit::generateSeed] IOBufferMemoryDescriptor::inTaskWithOptions returned NULL\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucGenerateInFieldSeed] Error: null pointer parameter\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucGetEncryptedSeedSegment] Error: bad input structure lengths\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucGetEncryptedSeedSegment] ProvInfoIOKit::getEncryptedSeedSegment returned %d\n`
- `[com_apple_driver_FairPlayIOKit::generateInFieldSeed] IOService::serviceMatching returned NULL\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] null pointer parameter detected\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucGetEncryptedSeedSegment] Error: null pointer for input structure\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOAESAccelerator::performAES in-field returned 0x%x\n`
- `com.apple.managed_drm_id`
- `com.apple.private.FairPlayIOKitUserClient.Virtual.access`
- `[com_apple_driver_FairPlayIOKitUserClient::ucEncryptWithWrappedKey] bad pointer for input or output structure\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOBufferMemoryDescriptor::inTaskWithOptions returned NULL\n`
- `[com_apple_driver_FairPlayIOKit::encryptSUInfo] IOService::serviceMatching returned NULL\n`
- `[com_apple_driver_FairPlayIOKit::encryptSUInfo] IOBufferMemoryDescriptor::inTaskWithOptions returned NULL\n`
- `com_apple_driver_FairPlayIOKit`
- `site.com_apple_driver_FairPlayIOKit`
- `12111112122212121`
- `[FairPlayIOKitUserClient::initWithTask] Error: entitlement not found\n`
- `[com_apple_driver_FairPlayIOKit::generateSeed] IOAESAccelerator::performAES GID returned 0x%x\n`
- `[com_apple_driver_FairPlayIOKit::exchangeWithHoover] IOAVService::createAUPPacket returned NULL\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOService::serviceMatching returned NULL\n`
- `[com_apple_driver_FairPlayIOKit::encryptWithWrappedKey] IOAESAccelerator::performAES returned %d\n`
- `[com_apple_driver_FairPlayIOKitUserClient::ucGenerateInFieldSeed] Error: ProvInfoIOKit::generateInFieldSeed returned %d\n`
- `[com_apple_driver_FairPlayIOKit::GetDeviceProperty] Error: The string length is not correct!\n`
- `[com_apple_driver_FairPlayIOKit::generateSeed] Error: invalid seed version (%u)\n`
- `[com_apple_driver_FairPlayIOKit::generateInFieldSeed] Error: invalid seed version (%u)\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] PIKDecryptWithFixedSharedKey returned %d\n`
- `[com_apple_driver_FairPlayIOKit::encryptWithWrappedKey] IOBufferMemoryDescriptor::prepare returned %d\n`
- `IONVRAM-FORCESYNCNOW-PROPERTY`
- `status`
- `[com_apple_driver_FairPlayIOKit::GetDeviceProperty] Error: The data length is not correct!\n`
- `[com_apple_driver_FairPlayIOKit::GetDeviceProperty] Error: The property type is unknown!\n`
- `[com_apple_driver_FairPlayIOKit::generateInFieldSeed] Error: null pointer detected\n`
- `[com_apple_driver_FairPlayIOKit::generateInFieldSeed] 1st IOAESAccelerator::performAES Seed returned 0x%x\n`
- `[com_apple_driver_FairPlayIOKit::generateInFieldSeed] IOBufferMemoryDescriptor::prepare returned %d\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] Error: invalid seed version (%u)\n`
- `[com_apple_driver_FairPlayIOKit::getEncryptedSeedSegment] IOAESAccelerator::performAES (scrambled) returned %d\n`

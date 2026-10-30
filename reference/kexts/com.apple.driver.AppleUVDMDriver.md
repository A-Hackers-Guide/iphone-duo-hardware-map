# `com.apple.driver.AppleUVDMDriver`

- Name: AppleUVDMDriver
- Version: `1.0.0`
- UUID: `FB19EEE9-3FCB-3ECC-8E9F-1D82E746407F`
- Source version: `29.0.0.0.0`
- Depends on: [`com.apple.driver.AppleHPM`](com.apple.driver.AppleHPM.md) 3.4.4, [`com.apple.driver.AppleUVDM`](com.apple.driver.AppleUVDM.md) 1.0.0, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0.0, [`com.apple.iokit.IOPortFamily`](com.apple.iokit.IOPortFamily.md) 1.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleUVDMDriver
- `CFBundleIdentifier`: `com.apple.driver.AppleUVDMDriver`
- `IOClass`: `IOPortTransportProtocolAppleUVDM`
- `IOPersonalityPublisher`: `com.apple.driver.AppleUVDMDriver`
- `IOProviderClass`: `IOPortTransportComponentCC`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleUVDMAceInterface` | 0x20 | AppleUVDMPDControllerInterface |
| `AppleUVDMEndpoint` | 0xc0 | AppleUVDMEndpointInterface → IOService → IORegistryEntry |
| `AppleUVDMPDControllerInterface` | 0x20 |  |
| `IOPortTransportProtocolAppleUVDM` | 0x130 | IOPortTransportProtocol → IOPortFamily → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000019f0 off=0x008e1060-0x008e2a50 addr=0xfffffe00078e5060-0xfffffe00078e6a50 r--/r--   __TEXT            
	sz=0x000013a6 off=0x008e1688-0x008e2a2e addr=0xfffffe00078e5688-0xfffffe00078e6a2e               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000020 off=0x008e2a30-0x008e2a50 addr=0xfffffe00078e6a30-0xfffffe00078e6a50               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00006e48 off=0x02b65010-0x02b6be58 addr=0xfffffe0009b69010-0xfffffe0009b6fe58 r-x/r-x   __TEXT_EXEC       
	sz=0x00006b58 off=0x02b65010-0x02b6bb68 addr=0xfffffe0009b69010-0xfffffe0009b6fb68          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000002f0 off=0x02b6bb68-0x02b6be58 addr=0xfffffe0009b6fb68-0xfffffe0009b6fe58          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000238 off=0x049d1e88-0x049d20c0 addr=0xfffffe000b9d5e88-0xfffffe000b9d60c0 rw-/rw-   __DATA            
	sz=0x00000188 off=0x049d1e88-0x049d2010 addr=0xfffffe000b9d5e88-0xfffffe000b9d6010               __DATA.__data             
	sz=0x000000b0 off=0x00000000-0x000000b0 addr=0xfffffe000b9d6010-0xfffffe000b9d60c0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000013b8 off=0x012b3e80-0x012b5238 addr=0xfffffe00082b7e80-0xfffffe00082b9238 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x012b3e80-0x012b3ea0 addr=0xfffffe00082b7e80-0xfffffe00082b7ea0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x012b3ea0-0x012b3ec0 addr=0xfffffe00082b7ea0-0xfffffe00082b7ec0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001098 off=0x012b3ec0-0x012b4f58 addr=0xfffffe00082b7ec0-0xfffffe00082b8f58         __DATA_CONST.__const            
	sz=0x00000100 off=0x012b4f58-0x012b5058 addr=0xfffffe00082b8f58-0xfffffe00082b9058         __DATA_CONST.__kalloc_type      
	sz=0x00000178 off=0x012b5058-0x012b51d0 addr=0xfffffe00082b9058-0xfffffe00082b91d0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000068 off=0x012b51d0-0x012b5238 addr=0xfffffe00082b91d0-0xfffffe00082b9238         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 107 at 0x04aece34
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     FB19EEE9-3FCB-3ECC-8E9F-1D82E746407F
008: LC_SOURCE_VERSION           29.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab7db0 size=0xb8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleUVDMDriver`
- `CFBundleGetInfoString`: `Copyright © 2022-2023 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleUVDMDriver`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleUVDMDriver`
- `CFBundleNumericVersion`: `16809984`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0.0`
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
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleLibraries_x86_64`: `{}`
- `OSBundleRequired`: `Local-Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleUVDMDriver.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896488352`
- `_PrelinkExecutableRelativePath`: `AppleUVDMDriver`
- `_PrelinkExecutableSize`: `40488`
- `_PrelinkExecutableSourceAddr`: `-2198896488352`
- `_PrelinkKmodInfo`: `-2198828392824`

## Strings (155) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `initWithSelf`
- `%s::%s - failCode 0x%X\n`
- `getAppleVDOs`
- `site.AppleUVDMAceInterface`
- `%s::%s - Can't alloc dataBuf memory\n`
- `%s::%s - Failed to fetch the number of VDOs\n`
- `%s::%s - [%s] \n%s: %s\n\n`
- `Vendor`
- `%s::%s - [%s] Can't open\n`
- `Protocol Type`
- `%s::%s - extData: 0x%X\n\n`
- `Serial Number`
- `%s::%s - [%s] ERROR: loopIter=0x%X >= MAX_ACCESS_TIMES=0x%X OR bytesRead=0x%X >= MAX_APPLEVDO_LEN=0x%X\n\n`
- `EP Unused`
- `writeStream`
- `%s::%s - Try to read 4 bytes at a time instead...\n`
- `%s::%s - [%s] Cannot grab workloop\n\n`
- `%s::%s - [%s] Power registration failed! with status = 0x%x\n\n`
- `%s::%s - [%s] Plugin dict alloc failed\n`
- `%s::%s - [%s] writeLen %u, offset 0x%X\n`
- `%s::%s - localEP: %u, remoteEP: %u, outBufLen: %u\n`
- `%s::%s - [%s] Retry%d: status=0x%X, failCode=0x%X\n\n`
- `%s::%s - [%s] Failed to start\n`
- `IOCFPlugInTypes`
- `SOPPrimePrime`
- `%s::%s - localEP: %u, remoteEP: %u, inBufLen: %u\n`
- `%s::%s - [%s] Found AppleVDO of type %s and of length %u at offset 0x%X\n`
- `SOP`
- `%s::%s - outExtData: 0x%X\n\n`
- `%s::%s - [%s] ERROR: returnLen [0x%X] != length2read [0x%X]\n\n`
- `Charger Telemetry Update`
- `Reserved`
- `%s::%s - [%s] writeLen %u, protoLen %u\n`
- `setAvailableEPs`
- `%s::%s - Init failed\n`
- `lockBus`
- `Failed to init EP%u\n`
- `open`
- `Charger FW Update Protocol`
- `site.IOPortTransportProtocolAppleUVDM`
- `Number of Data EPs`
- `%s::%s - [%s] Type 0x%X\n\n`
- `%s::%s - [%s] Provider not an IOPortTransportComponentCC\n`
- `%s::%s - Failed: failCode 0x%X\n`
- `%s::%s - [%s] Failed to get available endpoints, status=0x%X, failCode=0x%X\n\n`
- `%s::%s - [%s] Setting power state to 0x%lx\n\n`
- `site.AppleUVDMPDControllerInterface`
- `%s::%s - SMC-HPM lock not acquired after writing to their lock key\n\n`
- `121111121222121211112111`
- `setProperties`
- `SOPPrime`
- `isUVDMModeActive`
- `%s::%s - Unsupported target\n`
- `Product ID`
- `User String`
- `Model`
- `%s::%s - [%s] readLen %u, offset 0x%X\n`
- `%s::%s - [%s] No more retry, status=0x%X, failCode=0x%X\n\n`
- `Diagnostic Tester`
- `readStream`
- `%s::%s - Failed: extData: 0x%x, outExtData: 0x%x\n`
- `Number of VDOs`
- `EP Length`
- `%s::%s - [%s] Failed to get PD controller interface\n`
- `Unknown`
- `Charger Authentication`
- `1211`
- `%s::%s - status = 0x%X\n\n`
- `Product`
- `%s::%s - [%s] DFP, sleep for %ums\n\n`
- `init`
- `%s::%s - localEP: %u, remoteEP: %u\n`
- `uvdmdebug`
- `%s::%s - [%s] sleep for %ums after UVMD state machine reset...\n`
- `poweredStart`
- `%s::%s - [%s] finishStart() failed\n\n`
- `%s::%s - [%s] Start time: %lus,%uus, finish time: %lus,%uus, status=0x%X\n\n`
- `%s::%s - SOPx lock not acquired, retrying\n\n`
- `site.AppleUVDMEndpoint`
- `%s::%s - [%s] Can't get protocol ID, failCode 0x%X\n`
- `Discovery`
- `%s::%s - [%s] Can't find ARM provider\n`
- `%s::%s - [%s] Cannot make cmd gate\n\n`
- `Hardware Version`
- `AppleUVDMAceInterface`
- `%s::%s - [%s] Failed to init\n`
- `%s::%s - [%s] Failed to alloc metadata\n`
- `10903A4F-5790-45D3-B1FA-AB3E7585C863`
- `%s::%s - [%s] Failed start\n`
- `%s::%s - [%s] uvdmlog boot-arg: 0x%X, uvdmdebug boot-arg: 0x%X\n`
- `%s::%s - [%s] Failed to get VDO%d info, status=0x%X, failCode=0x%X\n\n`
- `readAccessForStart`
- `AppleUVDMUserClient`
- `%s::%s - localEP: %u, remoteEP: %u, inBufLen: %u, offset 0x%X\n`
- `%s::%s - CFUm failed; failCode 0x%X\n`
- `%s::%s - [%s] WARNING: potentially bad number of AppleVDOs returned, numVDOs=0x%X; Setting the max to read to %u\n\n`
- `%s::%s - No AppleUVDM version\n\n`
- `%s::%s - Found AppleVDO of type %s and of length %u at offset %u\n`
- `AppleUVDM`
- `Vendor ID`
- `%s::%s - [%s] ERROR: bytesLeft2Read [0x%X] < returnLen (already read here) [0x%X]; more bytes read than left to be read\n\n`
- `%s::%s - [%s] AUVDM mode not active\n`
- `%s::%s - [%s] ProtocolVDO is 0!\n\n`
- `%s::%s - [%s] Provider not IOPortTransportProtocolAppleUVDM\n`
- `%s::%s - returnLen %u\n`
- `uvdmlog`
- `%s::%s - Lock alloc failed\n`
- `%s::%s - [%s] retry %u; status=0x%X, valid=%u\n\n`
- `Protocol ID`
- `%s::%s - atomic4cc failed or couldn't lock\n`
- `terminate`
- `%s::%s - [%s] Failed to fetch the number of VDOs, status=0x%X, failCode=0x%X\n\n`
- `%s::%s - [%s] Available EPs (hexstring): %u\n\n`
- `%s::%s - [%s] ERROR: reading more than the outBufLen [0x%X], bytesRead [0x%X], returnLen [0x%X]\n\n`
- `Error`
- `%s::%s - [%s] VDO count: %u\n\n`
- `%s::%s - [%s] Rejected, failCode=0x%X\n\n`
- `%s::%s - [%s] User client property setting failed\n`
- `%s::%s - [%s] readLen %u, protoLen %u\n`
- `%s::%s - Cannot lock\n`
- `%s::%s - VDO count: %u\n\n`
- `start`
- `IECS Protocol`
- `%s::%s - [%s] failCode 0x%X\n`
- `%s::%s - [%s] Failed to get VDO%d content, status=0x%X, failCode=0x%X\n\n`
- `Manufacturer`
- `12111112122212121111112111111111112112`
- `%s::%s - [%s] Can't alloc dataBuf memory\n`
- `writeAccess`
- `AppleUVDMEndpoint`
- `SOPType`
- `%s::%s - Failed to get VDO %u\n`
- `resetAccess`
- `%s::%s - Aborting\n`
- `%s::%s - \n%s: %s\n\n`
- `probe`
- `IOPortTransportProtocolAppleUVDM`
- `getAvailableEPs`
- `message`
- `%s::%s - [%s] Performing a reset\n`
- `setPowerState`
- `readAccess`
- `%s::%s - Failed to alloc memory for register read\n\n`
- `AppleUVDMPDControllerInterface`
- `%s::%s - Message length exceeds maximum supported by this PD controller (%u > %u). See getTransportParameters.\n`
- `setUVDMMode`
- `Firmware Version`
- `setupPowerManagement`
- `%s::%s - [%s] Can't find plugin\n`
- `%s::%s - localEP: %u, remoteEP: %u, outBufLen: %u, offset 0x%X\n`
- `%s::%s - [%s] terminating\n\n`
- `%s::%s - [%s] Failed to lock for the entire sequence\n\n`
- `IOUserClientClass`
- `AppleUVDM.kext/PlugIns/AppleUVDMLib.plugin`
- `%s::%s - [%s] Termination detected\n\n`

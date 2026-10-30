# `com.apple.driver.AppleIDV`

- Name: AppleIDV
- Version: `9.108`
- UUID: `1FD817EE-AABA-3F6B-A54A-E986AF8B45FD`
- Source version: `9.108.0.0.0`
- Depends on: [`com.apple.driver.AppleSEPManager`](com.apple.driver.AppleSEPManager.md) 1.0.0, [`com.apple.driver.IOSlaveProcessor`](com.apple.driver.IOSlaveProcessor.md) 1.0.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 9.3.1

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleIDV
- `CFBundleIdentifier`: `com.apple.driver.AppleIDV`
- `IOClass`: `AppleIDV`
- `IOKitDebug`: `0`
- `IOMatchCategory`: `AppleIDV`
- `IOPersonalityPublisher`: `com.apple.driver.AppleIDV`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `SEP`
- `IOUserClientClass`: `AppleIDVUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleIDV` | 0x40d8 | IOService → IORegistryEntry |
| `AppleIDVUserClient` | 0xf0 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001ab2 off=0x00519fd0-0x0051ba82 addr=0xfffffe000751dfd0-0xfffffe000751fa82 r--/r--   __TEXT            
	sz=0x000000f8 off=0x0051a5f8-0x0051a6f0 addr=0xfffffe000751e5f8-0xfffffe000751e6f0               __TEXT.__const            
	sz=0x00001392 off=0x0051a6f0-0x0051ba82 addr=0xfffffe000751e6f0-0xfffffe000751fa82               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00006ff8 off=0x01ffae30-0x02001e28 addr=0xfffffe0008ffee30-0xfffffe0009005e28 r-x/r-x   __TEXT_EXEC       
	sz=0x00006e08 off=0x01ffae30-0x02001c38 addr=0xfffffe0008ffee30-0xfffffe0009005c38          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001f0 off=0x02001c38-0x02001e28 addr=0xfffffe0009005c38-0xfffffe0009005e28          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000128 off=0x0494cfd8-0x0494d100 addr=0xfffffe000b950fd8-0xfffffe000b951100 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x0494cfd8-0x0494d09c addr=0xfffffe000b950fd8-0xfffffe000b95109c               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b9510a0-0xfffffe000b951100               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00001020 off=0x0110ead0-0x0110faf0 addr=0xfffffe0008112ad0-0xfffffe0008113af0 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x0110ead0-0x0110eae0 addr=0xfffffe0008112ad0-0xfffffe0008112ae0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x0110eae0-0x0110eaf0 addr=0xfffffe0008112ae0-0xfffffe0008112af0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000e38 off=0x0110eaf0-0x0110f928 addr=0xfffffe0008112af0-0xfffffe0008113928         __DATA_CONST.__const            
	sz=0x00000080 off=0x0110f928-0x0110f9a8 addr=0xfffffe0008113928-0xfffffe00081139a8         __DATA_CONST.__kalloc_type      
	sz=0x000000f8 off=0x0110f9a8-0x0110faa0 addr=0xfffffe00081139a8-0xfffffe0008113aa0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000050 off=0x0110faa0-0x0110faf0 addr=0xfffffe0008113aa0-0xfffffe0008113af0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 72 at 0x04adce64
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     1FD817EE-AABA-3F6B-A54A-E986AF8B45FD
008: LC_SOURCE_VERSION           9.108.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa5170 size=0x108
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `AppleIDV`
- `CFBundleIdentifier`: `com.apple.driver.AppleIDV`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleIDV`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `9.108`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `9.108`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2019 Apple Inc. All rights reserved.`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleIDV.kext`
- `_PrelinkExecutableLoadAddr`: `-2198900449328`
- `_PrelinkExecutableRelativePath`: `AppleIDV`
- `_PrelinkExecutableSize`: `39922`
- `_PrelinkExecutableSourceAddr`: `-2198900449328`
- `_PrelinkKmodInfo`: `-2198828937256`

## Strings (118) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `powerOffActionGated`
- `aIDV_EstablishPrearmTrustWithKey`
- `sGetTrustKeyOnPhone`
- `revokeCredential`
- `%s::%s no sepEndpoint`
- `wakeupActionGated`
- `sGenerateTrustKeyOnPhone`
- `%s::%s / %d\n`
- `start`
- `setPowerStateGated`
- `%s::%s returning\n`
- `getWorkLoop`
- `recoverPersistedACLBlobGated`
- `validatePrearmTrustWithKey`
- `%s::%s init\n`
- `unlockItem`
- `lockItem`
- `setPowerState`
- `sendSEPCommand`
- `sep-endpoint,sidv`
- `%s::%s: SEP returned error, request = %d, info = %d, length = %d\n`
- `sendSEPMessage`
- `%s::%s *outSize=%d / OUT_MAX_SIZE=%d\n`
- `generatePhoneToken`
- `generatePhoneTokenGated`
- `authorizePresentment`
- `%s::%s bytes written = %d\n`
- `site.AppleIDVUserClient`
- `AppleSEPManager`
- `aIDV_RevokeCredential`
- `121111121222121211111111111112`
- `sRevokeCredential`
- `generateNonceOnWatch`
- `AppleIDV: %-30s: error: require failed at %s line %d\n`
- `persistACLBlobGated`
- `aIDV_GenerateNonceOnWatch`
- `sPrearmCredential`
- `getStatusAndVersion`
- `generateNonceOnWatchGated`
- `%s::%s re-enabling sepEndpoint \n`
- `%s::%s returning, _sepEndpoint set = %u\n`
- `revokeCredentialGated`
- `site.AppleIDV`
- `generateTrustKeyOnPhoneGated`
- `%s::%s started\n`
- `%s::%s start failed\n`
- `%s::%s ignoring unsupported message from SEP, request = %d, info = %d, length = %d\n`
- `[AppleIDVUserClient::start] Attached new client connection, provider at %p\n`
- `init`
- `writeToSEPBuffer`
- `aIDV_GenerateTrustKeyOnPhone`
- `%s::%s *outSize=%d / OUT_PAGE_SIZE=%d\n`
- `sGetStatusAndVersion`
- `%s::%s insize is %d, max %d`
- `OFF`
- `wakeupAction`
- `readFromSEPBuffer`
- `aIDV_RecoverPersistedACLBlob`
- `aIDV_AuthorizePresentment`
- `%s::%s returning 0x%x\n`
- `getSEPEndpoint`
- `aIDV_ValidatePrearmTrustWithKey`
- `authorizePresentmentGated`
- `sPersistACLBlob`
- `sUpdateTrustKeyOnPhone`
- `sValidatePrearmTrustWithKey`
- `%s::%s returning, err = 0x%x\n`
- `establishPrearmTrustWithKeyGated`
- `validatePrearmTrustWithKeyGated`
- `%s::%s holdingGate: %d\n`
- `handleSEPMessage`
- `aIDV_UpdateTrustKeyOnPhone`
- `genericAppleIDVCommand`
- `powerOffAction`
- `[AppleIDVUserClient::initWithTask] entering\n`
- `%s::%s outsize is smaller than max`
- `sendCommand`
- `%s::%s / %d - current state: %s, new state: %s\n`
- `%s::%s called\n`
- `unlockSEP`
- `%s::%s *outSize=%d / PREARM_TRUSTKEY_MAX_LENGTH=%d\n`
- `externalMethod`
- `AppleIDVUserClient::%s out_md = %p  out_md_size = %u\n`
- `recoverPersistedACLBlob`
- `com.apple.private.appleidv.allow`
- `AppleIDV`
- `stop`
- `9.108`
- `aIDV_PersistACLBlob`
- `aIDV_GetTrustKeyOnPhone`
- `aIDV_PrearmCredential`
- `AppleIDVUserClient`
- `sEstablishPrearmTrustWithKey`
- `%s::%s re-enabling SEP endpoint \n`
- `aIDV_GeneratePhoneToken`
- `transmitSIDVCommandBuffer`
- `getTrustKeyOnPhoneGated`
- `updateTrustKeyOnPhoneGated`
- `clientClose`
- `%s::%s deferring power off for %u s`
- `%s::%s called with pointer %p and timeout %d\n`
- `persistACLBlob`
- `121111121222121211111122222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222222`
- `lockSEP`
- `%s::%s writtenToSEP=%zu, dataLength=%zu\n`
- `sRecoverPersistedACLBlob`
- `%s::%s returning, result = %d\n`
- `%s::%s disable SEPEndpoint\n`
- `%s::%s outputBufferLength=%d, _sepContext.responseDataLength=%d\n`
- `aIDV_GetStatusAndVersion`
- `prearmCredentialGated`
- `sGenerateNonceOnWatch`
- `AppleIDVUserClient::%s in_md = %p out_md = %p  out_md_size = %u\n`
- `ON`
- `getStatusAndVersionGated`
- `sAuthorizePresentment`
- `sGeneratePhoneToken`
- `prearmCredential`

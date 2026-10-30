# `com.apple.driver.AppleAuthCP`

- Name: AppleAuthCP
- Version: `1.0.0`
- UUID: `A4DEF7B2-950A-343E-A088-6A892BEFEB66`
- Source version: `186.40.3.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.driver.AppleSMC`](com.apple.driver.AppleSMC.md) 1, [`com.apple.iokit.IOAccessoryManager`](com.apple.iokit.IOAccessoryManager.md) 1.0.0, [`com.apple.iokit.IOPortFamily`](com.apple.iokit.IOPortFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 13.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 13.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (6) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/i2c3/mogul-display`](../devicetree/root__arm-io__i2c3__mogul-display.md) | `MogulAuthI2CRelayInterface` | `mogul,a1222` |
| [`/arm-io/i2c3/mogul-display`](../devicetree/root__arm-io__i2c3__mogul-display.md) | `MogulAuthSMCRelayInterface` | `mogul,a1222` |
| [`/arm-io/i2c3/mogul-display2`](../devicetree/root__arm-io__i2c3__mogul-display2.md) | `MogulAuthI2CRelayInterface` | `mogul,a1222` |
| [`/arm-io/i2c3/mogul-display2`](../devicetree/root__arm-io__i2c3__mogul-display2.md) | `MogulAuthSMCRelayInterface` | `mogul,a1222` |
| [`/arm-io/i2c4/mogul-mlb`](../devicetree/root__arm-io__i2c4__mogul-mlb.md) | `MogulAuthI2CRelayInterface` | `mogul,a1222` |
| [`/arm-io/i2c4/mogul-mlb`](../devicetree/root__arm-io__i2c4__mogul-mlb.md) | `MogulAuthSMCRelayInterface` | `mogul,a1222` |

## IOKit personalities (13) [KC]

### AppleAuthCPAID
- `CFBundleIdentifier`: `com.apple.driver.AppleAuthCP`
- `IOAccessoryDigitalID`: `<data 28 chars>`
- `IOAccessoryPowerMode`: `2`
- `IOClass`: `AppleAuthCPAID`
- `IOMatchCategory`: `AU`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAuthCP`
- `IOProviderClass`: `IOAccessoryDock9Pin`
- `IOUserClientClass`: `AppleAuthCPUserClient`

### AppleAuthCPAIDIOPort
- `CFBundleIdentifier`: `com.apple.driver.AppleAuthCP`
- `IOClass`: `AppleAuthCPAID`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAuthCP`
- `IOPropertyMatch`:
  - `ComponentType`: `mogul,a1222`
- `IOProviderClass`: `IOPortTransportAIDBus`
- `IOUserClientClass`: `AppleAuthCPUserClient`

### AppleAuthCPAIDInternal
- `CFBundleIdentifier`: `com.apple.driver.AppleAuthCP`
- `IOAccessoryIDBusTransportInternalAuth`: `True`
- `IOClass`: `AppleAuthCPAID`
- `IOMatchCategory`: `AU`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAuthCP`
- `IOProviderClass`: `IOAccessoryIDBusTransport`
- `IOUserClientClass`: `AppleAuthCPUserClient`

### AppleAuthCPAIDOrion
- `CFBundleIdentifier`: `com.apple.driver.AppleAuthCP`
- `IOAccessoryDigitalID`: `<data 28 chars>`
- `IOAccessoryPowerMode`: `2`
- `IOClass`: `AppleAuthCPAID`
- `IOMatchCategory`: `AU`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAuthCP`
- `IOProviderClass`: `IOAccessoryManagerOrion`
- `IOUserClientClass`: `AppleAuthCPUserClient`

### AppleAuthCPDock
- `CFBundleIdentifier`: `com.apple.driver.AppleAuthCP`
- `IOClass`: `AppleAuthCPDock`
- `IOMatchCategory`: `AUDock`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAuthCP`
- `IOPropertyMatch`:
  - `IOAccessoryManagerPortAuthentication`: `True`
- `IOProviderClass`: `IOAccessoryManager`
- `IOUserClientClass`: `AppleAuthCPUserClient`

### AppleAuthCPHSAID
- `CFBundleIdentifier`: `com.apple.driver.AppleAuthCP`
- `IOClass`: `AppleAuthCPHSAID`
- `IOMatchCategory`: `AU`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAuthCP`
- `IOPropertyMatch`:
  -
    - `IOAccessoryAccessoryModelNumber`: `A2261`
    - `SupportsLegacyAuth`: `True`
  -
    - `IOAccessoryAccessoryModelNumber`: `A1998`
    - `SupportsLegacyAuth`: `True`
  -
    - `IOAccessoryAccessoryModelNumber`: `A2480`
    - `SupportsLegacyAuth`: `True`
  -
    - `IOAccessoryAccessoryModelNumber`: `A2975`
    - `SupportsLegacyAuth`: `True`
  -
    - `IOAccessoryAccessoryModelNumber`: `A2974`
    - `SupportsLegacyAuth`: `True`
- `IOProviderClass`: `IOAccessoryManagerHSAID`
- `IOUserClientClass`: `AppleAuthCPUserClient`

### AppleAuthCPI2C
- `CFBundleIdentifier`: `com.apple.driver.AppleAuthCP`
- `IOClass`: `AppleAuthCPI2C`
- `IONameMatch`:
  - `authcp,2c`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAuthCP`
- `IOProviderClass`: `AppleARMIICDevice`
- `IOUserClientClass`: `AppleAuthCPUserClient`

### AppleAuthCPMGAID 
- `CFBundleIdentifier`: `com.apple.driver.AppleAuthCP`
- `IOAccessoryDigitalID`: `<data 28 chars>`
- `IOAccessoryPowerMode`: `2`
- `IOClass`: `AppleAuthCPMGAID`
- `IOMatchCategory`: `AU`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAuthCP`
- `IOProviderClass`: `IOAccessoryDock9Pin`
- `IOUserClientClass`: `AppleAuthCPUserClient`

### AppleAuthCPRelay
- `CFBundleIdentifier`: `com.apple.driver.AppleAuthCP`
- `IOClass`: `AppleAuthCPRelay`
- `IOMatchCategory`: `AppleAuthCP`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAuthCP`
- `IOProviderClass`: `AppleAuthCPRelayInterface`
- `IOUserClientClass`: `AppleAuthCPUserClient`

### Area51AuthSMCRelayInterface
- `CFBundleIdentifier`: `com.apple.driver.AppleAuthCP`
- `IOClass`: `Area51AuthSMCRelayInterface`
- `IONameMatch`:
  - `area51`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAuthCP`
- `IOProviderClass`: `AppleSMCInterface`

### MogulAuthI2CRelayInterface
- `CFBundleIdentifier`: `com.apple.driver.AppleAuthCP`
- `IOClass`: `MogulAuthI2CRelayInterface`
- `IONameMatch`:
  - `mogul,a1222`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAuthCP`
- `IOProviderClass`: `AppleARMIICDevice`

### MogulAuthSMCRelayInterface
- `CFBundleIdentifier`: `com.apple.driver.AppleAuthCP`
- `IOClass`: `MogulAuthSMCRelayInterface`
- `IONameMatch`:
  - `mogul,a1222`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAuthCP`
- `IOProviderClass`: `AppleSMCInterface`

### RoswellAuthI2CRelayInterface
- `CFBundleIdentifier`: `com.apple.driver.AppleAuthCP`
- `IOClass`: `RoswellAuthI2CRelayInterface`
- `IONameMatch`:
  - `roswell`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAuthCP`
- `IOProviderClass`: `AppleARMIICDevice`


## C++ classes (14) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleAuthCP` | 0x98 | IOService → IORegistryEntry |
| `AppleAuthCPAID` | 0xc8 | AppleAuthCP → IOService → IORegistryEntry |
| `AppleAuthCPDock` | 0xa0 | AppleAuthCP → IOService → IORegistryEntry |
| `AppleAuthCPHSAID` | 0xd8 | AppleAuthCP → IOService → IORegistryEntry |
| `AppleAuthCPI2C` | 0xb0 | AppleAuthCP → IOService → IORegistryEntry |
| `AppleAuthCPMGAID` | 0xc8 | AppleAuthCPAID → AppleAuthCP → IOService → IORegistryEntry |
| `AppleAuthCPRelay` | 0xc8 | AppleAuthCP → IOService → IORegistryEntry |
| `AppleAuthCPRelayInterface` | 0x90 | IOService → IORegistryEntry |
| `AppleAuthCPUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |
| `Area51AuthSMCRelayInterface` | 0xc0 | AppleAuthCPRelayInterface → IOService → IORegistryEntry |
| `IDBusTransportPrivate` | 0xb0 | IOService → IORegistryEntry |
| `MogulAuthI2CRelayInterface` | 0xc0 | AppleAuthCPRelayInterface → IOService → IORegistryEntry |
| `MogulAuthSMCRelayInterface` | 0xc0 | AppleAuthCPRelayInterface → IOService → IORegistryEntry |
| `RoswellAuthI2CRelayInterface` | 0xb8 | AppleAuthCPRelayInterface → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1720)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00004b30 off=0x00390b10-0x00395640 addr=0xfffffe0007394b10-0xfffffe0007399640 r--/r--   __TEXT            
	sz=0x0000007c off=0x00391228-0x003912a4 addr=0xfffffe0007395228-0xfffffe00073952a4               __TEXT.__const            
	sz=0x00002cc2 off=0x003912a4-0x00393f66 addr=0xfffffe00073952a4-0xfffffe0007397f66               __TEXT.__cstring          (CstringLiterals)
	sz=0x000016da off=0x00393f66-0x00395640 addr=0xfffffe0007397f66-0xfffffe0007399640               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0001a9b4 off=0x0198bf10-0x019a68c4 addr=0xfffffe000898ff10-0xfffffe00089aa8c4 r-x/r-x   __TEXT_EXEC       
	sz=0x0001a524 off=0x0198bf10-0x019a6434 addr=0xfffffe000898ff10-0xfffffe00089aa434          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000490 off=0x019a6434-0x019a68c4 addr=0xfffffe00089aa434-0xfffffe00089aa8c4          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000003ca off=0x049330c0-0x0493348a addr=0xfffffe000b9370c0-0xfffffe000b93748a rw-/rw-   __DATA            
	sz=0x00000188 off=0x049330c0-0x04933248 addr=0xfffffe000b9370c0-0xfffffe000b937248               __DATA.__data             
	sz=0x00000240 off=0x00000000-0x00000240 addr=0xfffffe000b937248-0xfffffe000b937488               __DATA.__common           (Zerofill)
	sz=0x00000002 off=0x00000000-0x00000002 addr=0xfffffe000b937488-0xfffffe000b93748a               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00006ab0 off=0x00fe8870-0x00fef320 addr=0xfffffe0007fec870-0xfffffe0007ff3320 rw-/rw-   __DATA_CONST      
	sz=0x00000050 off=0x00fe8870-0x00fe88c0 addr=0xfffffe0007fec870-0xfffffe0007fec8c0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000050 off=0x00fe88c0-0x00fe8910 addr=0xfffffe0007fec8c0-0xfffffe0007fec910         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00005f60 off=0x00fe8910-0x00fee870 addr=0xfffffe0007fec910-0xfffffe0007ff2870         __DATA_CONST.__const            
	sz=0x00000780 off=0x00fee870-0x00feeff0 addr=0xfffffe0007ff2870-0xfffffe0007ff2ff0         __DATA_CONST.__kalloc_type      
	sz=0x00000248 off=0x00feeff0-0x00fef238 addr=0xfffffe0007ff2ff0-0xfffffe0007ff3238         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000d0 off=0x00fef238-0x00fef308 addr=0xfffffe0007ff3238-0xfffffe0007ff3308         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000018 off=0x00fef308-0x00fef320 addr=0xfffffe0007ff3308-0xfffffe0007ff3320         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 172 at 0x04ad37fc
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     A4DEF7B2-950A-343E-A088-6A892BEFEB66
008: LC_SOURCE_VERSION           186.40.3.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9a2a0 size=0x358
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleAuthCP`
- `CFBundleIdentifier`: `com.apple.driver.AppleAuthCP`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleAuthCP`
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
- `NSHumanReadableCopyright`: `Copyright © 2019 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
  - `2`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleAuthCP.kext`
- `_PrelinkExecutableLoadAddr`: `-2198902060272`
- `_PrelinkExecutableRelativePath`: `AppleAuthCP`
- `_PrelinkExecutableSize`: `156510`
- `_PrelinkExecutableSourceAddr`: `-2198902060272`
- `_PrelinkKmodInfo`: `-2198829043520`

## Strings (463) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s: error in StartAuth transfer, 0x%x\n`
- `site.AppleAuthCPRelay`
- `%s:%s no data received for command kAuthCommandIDGetInfo\n`
- `%s:%s Received challenge different than what we have stored. Removing stored info and requesting new signature\n`
- `auth-error`
- `AppleAuthCPHSAID::%s Received Start Authentication Response.\n`
- `handleGetLastErrorResponse`
- `%s::%s: !parentManager\n`
- `createFormattedResponse`
- `%s: Version(M=%d,m=%d) DevId=%02x%02x FW=%d`
- `isTrusted`
- `Fail`
- `Area51AuthSMCRelayInterface`
- `%s: unexpected startOfMessage: %d`
- `%s: error in CheckAuth transfer: auth challenge not received\n`
- `Signature`
- `ComponentIndex`
- `setActualPairedCertSN`
- `AppleAuthCPHSAID::%s Starting!\n`
- `AppleAuthCPAID: error 0x%x\n`
- `authError`
- `%s:%s _getDeviceIDSN() failed (status = 0x%x)\n`
- `%s:%s failed to generate challenge for command kAuthCommandIDGetSignature\n`
- `extGetTransportEntryId`
- `121111121222121212111112`
- `%s::%s: obj == NULL key = %s\n`
- `%s: error in CheckAuth transfer, 0x%x\n`
- `%s:%s No signature found for the associated challenge. Removing stored info and requesting new signature \n`
- `%s::%s: %s: () auth_debug %x\n`
- `pretend_auth`
- `%s:%s set auth status = %d\n`
- `IOAccessoryAccessoryModelNumber`
- `site.AppleAuthCPHSAID`
- `%s::%s: %s: rsp:len=%d [%02x %02x]\n`
- `_getCert`
- `%s:%s %s\n`
- `write to`
- `start_block_invoke`
- `AppleAuthCPHSAID::%s result %s\n`
- `authcp-ace`
- `%s:%s\n`
- `_fetchPropertyGated`
- `AuthCPPID`
- `%s:%s failed to send command kAuthCommandIDGetCertSN\n`
- `%s:%s %d\n`
- `site.AppleAuthCPRelayInterface`
- `requestLastAuthenticationError`
- `%s::%s: %s: override AuthCPAuthMajorVersion of %d -> %d\n\n`
- `%s:%s: applyToTransport failed: 0x%x\n`
- `%s: %s reading device info: retries=%d \n`
- `AppleAuthCPHSAID::%s Disabled with boot-arg!\n`
- `AppleAuthCPHSAID::%s Fetching auth signature!\n`
- `AppleAuthCPHSAID::%s Received Auth Info Version:%d.%d, DeviceID:%02x%02x FW=%d\n`
- `IDBusTransportPrivate`
- `1211111212221212111112`
- `1212`
- `AppleAuthCPAID::_aidTransportLockAction: open failed: ret:%x\n`
- `AIDAuthParams`
- `%s::%s: %s: %s: ignore endExclusiveMode, _startedExclusiveMode %d \n\n`
- `%s:%s failed to send command kAuthCommandIDGetSignature\n`
- `setTrustStatus`
- `%s: error in GetLastError transfer: 0x%x\n`
- `%s: error reading String: %s, call _endExclusiveModeIfRequired!! \n`
- `setAuthFullPass`
- `%s:%s !transportService\n`
- `PrimaryAuthPassed`
- `1211111212221212122112`
- `AppleAuthCPHSAID::%s Authentication result: %s\n`
- `AppleAuthCPAID::_aidTransportLockAction: GetAuthInfo: ret:%x\n`
- `AuthMajorVersion`
- `ReadCommand: %x %x %x %x %x %x %x %x %x %x %x %x\n`
- `%s::%s: error reading IDSN: %s\n`
- `%s:%s invalid data received for command kAuthCommandIDGetCertSN\n`
- `%s:%s !pairedAuthChipPrimary\n`
- `site.AppleAuthCPDock`
- `site.MogulAuthI2CRelayInterface`
- `site.MogulAuthSMCRelayInterface`
- `%s::%s: %s: () authcp_fix_mode %d\n`
- `_getCertSN`
- `%s:%s failed to send command kAuthCommandIDSetTrustStatus\n`
- `setTrustStatusForUI`
- `AppleAuthCPHSAID::%s Fetching auth certificate!\n`
- `1211111212221212122`
- `%s:%s set trust status = %d\n`
- `%s:%s matchingDictionaryForTransport failed\n`
- `%s:%s Found pack index on parent. Adding to componentIndex\n`
- `%s:%s !_transportType\n`
- `i8@?0`
- `AppleAuthCPAID::%s: super::start failed\n`
- `site.AppleAuthCPUserClient`
- `extGenerateSignatureWithIndexAndToken`
- `generateSignatureWithIndexAndToken`
- `setAuthError`
- `%s:%s !certSN\n`
- `com.apple.driver.AppleAuthCP.i2c.user-access`
- `message`
- `AppleAuthCPHSAID::%s terminating due to message!\n`
- `site.AppleAuthCPMGAID`
- `%s:%s _getCertSN() failed (status = 0x%x)\n`
- `%s:%s failed to send command kAuthCommandIDGetCert\n`
- `setExpectedPairedCertSN`
- `121111121222121212211111121`
- `requestAuthenticationInfo`
- `AppleAuthCPUserClient`
- `site.ReadMemoryCommand`
- `%s: error reading Signature: %s, call _endExclusiveModeIfRequired!! \n`
- `pairedAuthChipSecondary`
- `component-index`
- `%s:%s copyCertificate() failed (status = 0x%x)\n`
- `%s:%s failed to send command kAuthCommandIDGetInfo\n`
- `clearCertificate`
- `AppleAuthCPHSAID::%s Starting auth with version: %d, challenge len: %llu.\n`
- `requestAuthenticationCertificate`
- `AppleAuthCPHSAID::%s Getting error!\n`
- `DeviceVersion`
- `BatteryCode`
- `%s::%s: %s: dir=%d add=%02x len=%d\n`
- `AppleAuthCPHSAID::%s Could not send command: %s\n!`
- `site.Area51AuthSMCRelayInterface`
- `auth,mlb`
- `%s: too many retries\n`
- `B24@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{IONotifier=^^?i}16`
- `_updatePortTransportAuthStatus`
- `_transferData`
- `AppleAuthCPUserClient::extSetAuthError\n`
- `MogulAuthSMCRelayInterface`
- `clearAuthState`
- `%s:%s _getAuthInfo() failed\n`
- `%s::%s: %s: ()\n`
- `%s::%s: initWithTransportAID failed\n`
- `%s::%s: %s: () auth_max_cert %d\n`
- `%s::%s: %s: Version(M=%d,m=%d) DevId=%02x%02x%02x%02x FW=%d retries=%d\n`
- `AppleAuthCPHSAID::%s success!\n`
- `%s:%s no dictionary received for CMD=0x%x\n`
- `%s:%s set trust status for UI = %d\n`
- `%s:%s !entryId\n`
- `certificate`
- `handleGetAuthenticationCertificateResponse`
- `site.AIDTransferRequest`
- `AppleAuthCPAID::_threadFunc\n`
- `%s:%s CMD=0x%x _receivedStatus ERROR ( status = 0x%x )\n`
- `AppleAuthCPHSAID::%s Couldn't create string for serial number!\n`
- `FirmwareVersion`
- `%s::%s: %s: cmd:[%02x]\n`
- `%s: error in GetLastError transfer: bad message id=0x%x\n`
- `extSetExpectedPairedCertSN`
- `auth-passed`
- `handleGetAuthentationSignatureResponse`
- `auth,display`
- `setAuthStatus`
- `FdrValidationStatus`
- `211`
- `read from`
- `%s: error in CheckAuth transfer: auth response not ready\n`
- `%s:%s contains nonce from device\n`
- `%s::%s: !parentManagerAID\n`
- `AM002`
- `iic-bus-num`
- `%s:%s _getIDSN() failed\n`
- `%s:%s no dictionary received for command kAuthCommandIDGetInfo\n`
- `_getDeviceInfo`
- `AppleAuthCPHSAID::%s Fetching auth info!\n`
- `AppleAuthCPHSAID::%s Starting auth with challenge length %llu\n`
- `%s:%s !matchingDict\n`
- `_readString`
- `%s:%s processing deferred CMD=0x%x \n`
- `site.AppleAuthCPI2C`
- `AppleAuthCPHSAID::%s Stopping!\n`
- `IOAccessoryIDBusTransportTaskComplete`
- `PackIndex`
- `%s:%s failed to generate trustStatus for command kAuthCommandIDSetTrustStatus\n`
- `site.IDSNCommand`
- `AppleAuthCPHSAID::%s Could not open HSAID transport!\n`
- `InternalComponent`
- `%s: error reading certificate serial number: %s\n`
- `%s:%s invalid data received for command kAuthCommandIDGetCert\n`
- `AppleAuthCP`
- `AppleAuthCPRelayInterface`
- `AppleAuthCPHSAID::%s Received Certificate Response! Length %d\n`
- `_getDeviceManufacturerData`
- `applyToTransport`
- `createFormattedChallenge`
- `1211111212221212122121222`
- `%s::%s: initWithIDBusTransport failed\n`
- `AppleAuthCPRelay`
- `%s::%s: %s: () override_auth4 %d\n`
- `AM001`
- `%s: error reading certificate length: %s\n`
- `IsInductiveTransport`
- `%s:%s _getDeviceInfo() failed (status = 0x%x)\n`
- `%s: bad certificate length %u\n`
- `%s::%s: %s: AuthMajor(%d), len: challenge=%d sig=%d\n`
- `site.AuthQueryCmd`
- `_smcIICRegisterWrite`
- `pairedAuthChipPrimary`
- `AppleAuthCPAID::_getIDSN: _vendorId:%x, _productId:%x\n`
- `%s: error reading authentication info: %s, call _endExclusiveModeIfRequired!! \n`
- `%s:%s _commandGate == NULL\n`
- `%s:%s no data received for command kAuthCommandIDGetCertSN\n`
- `setExpectedPairedCertSN_block_invoke`
- `X533b`
- `_smcIICRegisterRead`
- `%s::%s: error reading authentication info: %s\n`
- `authErrorDescription`
- `start`
- `%s::%s: !_idBus\n`
- `%s::%s: !allowAuthCPOverAce\n`
- `AccessoryCertificate`
- `%s: transferData timeout\n`
- `%s:%s challengeLength is too large\n`
- `extSetActualPairedCertSN`
- `1211111212221212122112122`
- `%s:%s _getCert() failed (status = 0x%x)\n`
- `extCreateFormattedResponse`
- `MogulAuthI2CRelayInterface`
- `AppleAuthCPHSAID::%s Provider isn't a HSAID manager!\n`
- `X533c`
- `device-version`
- `idsn`
- `site.IDBusTransportPrivate`
- `IDSN`
- `%s:%s authInit() failed (status = 0x%x)\n`
- `%s:%s:%d: CMD=0x%x  (status = THREAD_INTERRUPTED) \n`
- `_getDeviceIDSN`
- `%s:%s found transport service\n`
- `site.RoswellAuthI2CRelayInterface`
- `probe`
- `Unknown`
- `AppleAuthCPHSAID`
- `AppleAuthCPHSAID::%s Copy certificate result %s`
- `copyCertificate`
- `AppleAuthCPHSAID::%s Transport not active.\n`
- `AppleAuthCPHSAID::%s Got %d bytes, expected %lu!\n`
- `handleStartAuthenticationResponse`
- `AppleAuthCPHSAID::%s Failed to allocate buffer!\n`
- `%s:%s failed to send command kAuthCommandIDSetAuthStatus\n`
- `%s:%s setProperty failed\n`
- `extGetChallengeSignatureLengths`
- `(no provider)`
- `%s::%s: could not open ID bus\n`
- `Challenge`
- `generateSignatureLocked`
- `%s:%s invalid data received for CMD=0x%x\n`
- `1211111212221212111111111111`
- `AppleAuthCPHSAID::%s Failed to get HSAID transport!\n`
- `challenge`
- `%s::%s: error reading certificate serial number: %s\n`
- `AccessoryCertificateSerialNumber`
- `%s:%s no data received for command kAuthCommandIDGetSignature\n`
- `override_auth4`
- `AppleAuthCP::start: pretend_auth %d\n`
- `getAuthVersionMajor`
- `ExpectedPairedCertSN`
- `AppleAuthCPI2C`
- `%s::%s: failed\n`
- `stop`
- `auth_cmd_timeout`
- `%s:%s no data received for command kAuthCommandIDGetCert\n`
- `generateSignature`
- `setCertificate`
- `AppleAuthCPHSAID::%s Failed super::start!\n`
- `requestAuthenticationSignature`
- `AppleAuthCPAID`
- `_endExclusiveModeIfRequired`
- `%s:%s !batteryCode\n`
- `Invalid`
- `%s:%s !certificate\n`
- `copyCertificateLocked`
- `extCreateFormattedChallenge`
- `AppleAuthCPHSAID::%s Received Get Authentication Info Response!\n`
- `copyProperty`
- `%s: cert length >= _maxCertLength\n`
- `%s::%s: %s: cmd:len=%d [%02x %02x %02x %02x %02x pay:%02x]\n`
- `auth_debug`
- `flags`
- `AuthMinorVersion`
- `%s::%s: %s: resp:[%02x, %02x] ret=%x\n`
- `%s::%s: %s: cmd:len=%d [%02x %02x %02x %02x %02x]\n`
- `%s:%s:%d: CMD=0x%x  (status = THREAD_TIMED_OUT) \n`
- `%s:%s failed to send command kAuthCommandIDSetBatteryCode\n`
- `isTrustedForUI`
- `ActualPairedCertSN`
- `%s: error reading IDSN: %s, call _endExclusiveModeIfRequired!! \n`
- `DeviceID`
- `%s::%s: %s: len: %d <%s>\n`
- `DeviceNonce`
- `%s:%s !port\n`
- `AppleAuthCPHSAID::%s Failed to create command gate!\n`
- `requestAuthenticationStart`
- `handleGetAuthenticationInfoResponse`
- `%s: error in CheckAuth transfer: bad message id=0x%x\n`
- `authcp_fix_mode`
- `matchingDictionaryForTransport`
- `SecondaryAuthPassed`
- `%s: bad info: Version(M=%d,m=%d) DevId=%02x%02x%02x%02x FW=%d retries=%d\n`
- `extSetCertificate`
- `121111121222121212`
- `IOAccessoryManagerHSAID`
- `site.AppleAuthCPAID`
- `%s: error reading certificate data: %s\n`
- `%s::%s: %s: AuthMajor(%d), len: challenge=%d sig=%d max-xfer %d\n`
- `%s:%s CMD=0x%x authSendData() failed (ret = 0x%x)\n`
- `_processDeferredCommandGated`
- `%s:%s !authStatus\n`
- `site.AppleAuthCP`
- `%s: error reading serial number: %s\n`
- `extI2CWrite`
- `AppleAuthCPHSAID::%s Fetching certificate serial number!\n`
- `AppleAuthCPHSAID::%s Received Get Last Error Response!\n`
- `handleGetAuthenticationCertificateSerialNumberResponse`
- `%s: _read failed`
- `%s::%s: !_commandGate\n`
- `%s::%s: !kIOServiceRegisteredState\n`
- `_threadFunc_block_invoke`
- `setBatteryCode`
- `AM003`
- `com.apple.driver.AppleAuthCP.user-access`
- `AppleAuthCPHSAID::%s Inactive when starting!\n`
- `AppleAuthCPHSAID::%s Could not send command: %s!\n`
- `%s:%s:%d: CMD=0x%x isInactive() == TRUE \n`
- `AuthFullPass`
- `%s::%s: %s: Version(M=%d,m=%d) DevId=%02x%02x%02x%02x FW=%d\n`
- `AppleAuthCPHSAID::%s Failed to read serial number!\n`
- `%s: _write failed`
- `ic-auth-type`
- `_readData`
- `expectDualAuth`
- `signature`
- `%s: unexpected messageID: %x`
- `%s:%s !dict\n`
- `12111112122212121221`
- `requestAuthenticationCertificateSerialNumber`
- `AppleAuthCPHSAID::%s Received Signature Response. Length: %d\n`
- `AppleAuthCPHSAID::%s Received Certificate Serial Number Response. Length: %d\n`
- `%s: error reading authentication info: %s\n`
- `auth_max_cert`
- `%s: Error hit max retries\n`
- `RoswellAuthI2CRelayInterface`
- `ComponentFunction`
- `AppleAuthCPMGAID::%s: super::start failed\n`
- `iboot-auth`
- `setAuthErrorDescription`
- `12111112122212121211111`
- `AppleAuthCPHSAID::%s terminating due to bus requesting close!\n`
- `getTransportEntryId`
- `%s::%s: %s: NAK\n`
- `%s: unexpected messageLength: %d`
- `AuthCPVID`
- `IOAccessoryManagerNeedsAuthCPMGWorkaround`
- `%s::%s: %s: resp:[%02x %02x %02x]\n`
- `%s:%s super::start failed\n`
- `%s:%s _provider == NULL\n`
- `Pass`
- `%s:%s !pairedAuthChipSecondary\n`
- `extI2CRead`
- `AppleAuthCPMGAID`
- `AppleAuthCPRelay::start: provider has no IDSN\n`
- `AuthPassed`
- `_sendCommandGated`
- `AppleAuthCPDock`
- `hsaid-auth`
- `ReadCommand response: %x %x %x %x %x %x %x %x %x %x %x %x\n`
- `%s: 16 byte pkt send err 0x%x\n`

**[__TEXT.__os_log]**

- `%s: Failed to access provider`
- `%s: SMC read failure! (ret: %x)`
- `Writing %u bytes to register 0x%02X...`
- `MogulAuthI2CRelayInterface::_read:%d: address:0x%x, failed:0x%x\n`
- `MogulAuthI2CRelayInterface::_readWithAidPassthroughCommand: error code\n`
- `MogulAuthI2CRelayInterface::_readWithAidPassthroughCommand: _read failed\n`
- `MogulAuthSMCRelayInterface::transferData:dir=%d add=%02x len=%llu`
- `%s: unexpected structureOutputSize:%u`
- `%s: SMC write failure! (ret: %x)`
- `%s: Challenge length not valid \n`
- `_getCertSN: error: %s`
- `MogulAuthI2CRelayInterface::_write:%d: address:0x%x, data:0x%x, dataLength:%d\n`
- `%s: Address provided is null!`
- `Area51AuthSMCRelayInterface::transferData:dir=%d add=NULL len=%llu`
- `%s:%s: SMC Error in SMBS: 0x%02X`
- `%s: unexpected outputSize:%llu`
- `%s: unexpected inCmdLen:%llu`
- `%s: I2C read of %u bytes successful!`
- `Mogul Error Code: 0x%02X`
- `Area51AuthSMCRelayInterface::_read:%d: data:0x%x, dataLength:%llu, failed:0x%x\n`
- `%s:%s: A null buffer was provided!`
- `%s: unexpected structureOutputSize=%d`
- `%s: Certificate length not valid \n`
- `%s: Signature Generation did not succeed \n`
- `_getCert: Got certData! certLen %d`
- `MogulAuthI2CRelayInterface::_readWithAidPassthroughCommand: _write failed\n`
- `%s: A null buffer was provided!`
- `I2C write successful!`
- `%s: size:%d`
- `%s: I2C write failure! (ret: %x)`
- `MogulAuthSMCRelayInterface::transferData:dir=%d add=NULL len=%llu`
- `%s: Data length %llu > Maximum %d`
- `%s: unexpected challengeLength:%llu`
- `MogulAuthI2CRelayInterface::_read:%d: data:0x%x, dataLength:%llu, failed:0x%x\n`
- `%s: SMC Error in SMBC: 0x%02X`
- `MogulAuthSMCRelayInterface::_readWithAidPassthroughCommand: error code\n`
- `%s:%s: SMC Error in key write %u: 0x%02X`
- `%s:%s: SMC Error in SMBG: 0x%02X`
- `%s:%s: SMC Error in SMBD: 0x%02X`
- `%s: !structureOutput`
- `%s: unexpected outRspLen:%llu`
- `%s: getTransportEntryId failed 0x%x`
- `%s: Error received for %s address 0x%x for len %llu: 0x%x`
- `Unexpected certificate length! Skipping read of cert serial...`
- `MogulAuthI2CRelayInterface::_readWithAidPassthroughCommand: zone:%d, address:0x%x, length:%d\n`
- `%s: SMC Error in SMBD: 0x%02X`
- `%s:%s: Data + Address length %llu > Maximum %d`
- `_getCert: certLen %d`
- `MogulAuthSMCRelayInterface::_write:%d: address:0x%x, data:0x%x, dataLength:%d\n`
- `MogulAuthSMCRelayInterface::transferData: Success!`
- `%s: Bus Error in SMC write: 0x%02X 0x%02X`
- `Area51AuthSMCRelayInterface::_read:%d: address:0x%x, failed:0x%x\n`
- `Area51AuthSMCRelayInterface::transferData: Transfer failed after %d retries!`
- `%s:%s: Data length is %llu but a null buffer was provided!`
- `%s:%s: Bus Error in SMC write: 0x%02X 0x%02X`
- `%s: !structureInput`
- `Area51AuthSMCRelayInterface::_write:%d: address:0x%x, data:0x%x, dataLength:%d\n`
- `%s: !structureInputSize`
- `%s: !structureOutputSize`
- `%s: Data length is %llu but a null buffer was provided!`
- `%s: SMC Error in SMBU: 0x%02X`
- `%s:%s: Data length %llu > Maximum %d`
- `%s: SMC read of %u bytes successful!`
- `%s: getChallengeSignatureLengths failed 0x%x`
- `%s: Signature length not valid \n`
- `%s: I2C read failure! (ret: %x)`
- `MogulAuthSMCRelayInterface::_read:%d: data:0x%x, dataLength:%llu, failed:0x%x\n`
- `MogulAuthSMCRelayInterface::_readWithAidPassthroughCommand: error:0x%x`
- `Area51AuthSMCRelayInterface::transferData:dir=%d add=%02x len=%llu`
- `%s:%s: SMBS success`
- `%s`
- `%s: unexpected scalarOutputCount:%u`
- `_getSignature: error: %s`
- `%s: _iicBusNumber:%d\n`
- `MogulAuthSMCRelayInterface::transferData: Transfer failed after %d retries!`
- `%s:%s: SMC Error in SMBC: 0x%02X`
- `%s: unexpected structureInputSize=%d`
- `%s: unexpected scalarInputCount:%u`
- `%s: unexpected structureInputSize:%u`
- `%s: unexpected lengths: %llu > %llu`
- `_getCertSN: certLen %d, max %d`
- `_getCert: error: %s`
- `MogulAuthI2CRelayInterface::_read: bus error during certificate read\n`
- `%s: Transfer attempt failed! Retries left: %d`
- `%s: length:%d, size:%d`
- `%s: options:%llu`
- `%s: Certificate length not valid`
- `MogulAuthSMCRelayInterface::_read:%d: address:0x%x, failed:0x%x\n`
- `%s: SMC Error in SMBS: 0x%02X`
- `MogulAuthSMCRelayInterface::_readWithAidPassthroughCommand: zone:%d, address:0x%x, length:%d\n`
- `MogulAuthSMCRelayInterface::_readWithAidPassthroughCommand: _write failed\n`
- `Area51AuthSMCRelayInterface::transferData: Success!`
- `%s: provider is not AppleAuthCPRelayInterface`
- `I2C write failure! (ret: %x)`
- `_checkErrorCode failed: 0x%x`
- `MogulAuthI2CRelayInterface::_readWithAidPassthroughCommand: error:0x%x`
- `%s: Data + Address length %llu > Maximum %d`
- `%s: SMC Error in SMBG: 0x%02X`
- `MogulAuthSMCRelayInterface::_readWithAidPassthroughCommand: _read failed\n`
- `Reading %u bytes from register 0x%02X...`

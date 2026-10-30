# `com.apple.driver.IOPAudioClientManagerDevice`

- Name: IOPAudioClientManagerDevice
- Version: `400.36`
- UUID: `24911B80-4C58-341B-8E9C-00B3FE3102DA`
- Source version: `400.36.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.IOPAudioDriverFamily`](com.apple.iokit.IOPAudioDriverFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/iop-audio-controller/siri-listening-device`](../devicetree/root__arm-io__iop-audio-controller__siri-listening-device.md) | `IOPAudioClientManagerDevice` | `iop-audio,client-manager-device` |

## IOKit personalities (1) [KC]

### ClientManagerDevice
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioClientManagerDevice`
- `IOClass`: `IOPAudioClientManagerDevice`
- `IONameMatch`:
  - `iop-audio,client-manager-device`
- `IOPersonalityPublisher`: `com.apple.driver.IOPAudioClientManagerDevice`
- `IOProviderClass`: `IOPAudioNode`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOPAudioClientManagerDevice` | 0x2d0 | IOPAudioDevice → IOService → IORegistryEntry |
| `IOPAudioClientManagerDeviceUserClient` | 0xf0 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001de2 off=0x00a2a770-0x00a2c552 addr=0xfffffe0007a2e770-0xfffffe0007a30552 r--/r--   __TEXT            
	sz=0x00000008 off=0x00a2ae38-0x00a2ae40 addr=0xfffffe0007a2ee38-0xfffffe0007a2ee40               __TEXT.__const            
	sz=0x00000d8c off=0x00a2ae40-0x00a2bbcc addr=0xfffffe0007a2ee40-0xfffffe0007a2fbcc               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000986 off=0x00a2bbcc-0x00a2c552 addr=0xfffffe0007a2fbcc-0xfffffe0007a30552               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00004360 off=0x032dffa0-0x032e4300 addr=0xfffffe000a2e3fa0-0xfffffe000a2e8300 r-x/r-x   __TEXT_EXEC       
	sz=0x00004250 off=0x032dffa0-0x032e41f0 addr=0xfffffe000a2e3fa0-0xfffffe000a2e81f0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000110 off=0x032e41f0-0x032e4300 addr=0xfffffe000a2e81f0-0xfffffe000a2e8300          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000130 off=0x04a13c58-0x04a13d88 addr=0xfffffe000ba17c58-0xfffffe000ba17d88 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a13c58-0x04a13d20 addr=0xfffffe000ba17c58-0xfffffe000ba17d20               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000ba17d20-0xfffffe000ba17d80               __DATA.__common           (Zerofill)
	sz=0x00000008 off=0x00000000-0x00000008 addr=0xfffffe000ba17d80-0xfffffe000ba17d88               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001070 off=0x013c63e0-0x013c7450 addr=0xfffffe00083ca3e0-0xfffffe00083cb450 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x013c63e0-0x013c63f0 addr=0xfffffe00083ca3e0-0xfffffe00083ca3f0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x013c63f0-0x013c6400 addr=0xfffffe00083ca3f0-0xfffffe00083ca400         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000f00 off=0x013c6400-0x013c7300 addr=0xfffffe00083ca400-0xfffffe00083cb300         __DATA_CONST.__const            
	sz=0x00000080 off=0x013c7300-0x013c7380 addr=0xfffffe00083cb300-0xfffffe00083cb380         __DATA_CONST.__kalloc_type      
	sz=0x00000088 off=0x013c7380-0x013c7408 addr=0xfffffe00083cb380-0xfffffe00083cb408         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000048 off=0x013c7408-0x013c7450 addr=0xfffffe00083cb408-0xfffffe00083cb450         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 43 at 0x04af5628
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     24911B80-4C58-341B-8E9C-00B3FE3102DA
008: LC_SOURCE_VERSION           400.36.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac37c0 size=0xc8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleExecutable`: `IOPAudioClientManagerDevice`
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioClientManagerDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOPAudioClientManagerDevice`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `400.36`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `400.36`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2023 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOPAudioClientManagerDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895138960`
- `_PrelinkExecutableRelativePath`: `IOPAudioClientManagerDevice`
- `_PrelinkExecutableSize`: `29410`
- `_PrelinkExecutableSourceAddr`: `-2198895138960`
- `_PrelinkKmodInfo`: `-2198828123048`

## Strings (73) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `!((inClient) == nullptr)`
- `supports-multiple-user-clients`
- `ret = userClient->mDevice->enableClientManager(false, direction, userClient->mClientID) == 0 `
- `com.apple.private.aop-audio.user-access`
- `ret = super::_handleStart(inProvider) == 0 `
- `inType < IOPAudio::ClientManagerDevice::kMaximumSupportedClients`
- `inArguments->structureInputSize == sizeof(PowerRequest)`
- `!(inClientIDMask == 0)`
- `mOpenedClients[clientID] == nullptr`
- `ret = userClient->mDevice->getNodeProperty(propertyDescriptor) == 0 `
- `IOUserClientClass`
- `IOUserClient::initWithTask(inOwningTask, inSecurityToken, inType, inProperties)`
- `mDevice->open(this, 0, &mClientID)`
- `!((inArguments->scalarOutput) == nullptr)`
- `!((inArguments->structureOutput) == nullptr)`
- `IOPAudio::ClientManagerDevice::UserClient`
- `ret = notifyRet == 0 `
- `power-down-prior-to-sleep`
- `entitlement == kOSBooleanTrue`
- `ret = userClient->mDevice->getCurrentClientManagerPowerState(state) == 0 `
- `!((kClientID < 0))`
- `function-cm_power_change_notify`
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/ClientManagerDevice/ClientManagerDeviceHelpers.hpp`
- `121111121222121211112222111111111111111111111111111111111111111111111111111111111111111121`
- `ret = super::_handleDeviceReady(inProvider) == 0 `
- `!((inArguments) == nullptr)`
- `ret = _configure(inProvider) == 0 `
- `!(static_cast<bool>(mOpenedClientMasks))`
- `ret = _enableClientManagerForMask(inEnable, inDirection, kClientIDMask) == 0 `
- `!(isSuspended())`
- `IOPAudioClientManagerDeviceUserClient`
- `site.IOPAudioClientManagerDeviceUserClient`
- `!((mDevice) == nullptr)`
- `mOpenedClients[kClientID] == inClient`
- `power-up-on-start`
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/ClientManagerDevice/UserClient/ClientManagerDeviceUserClient.cpp`
- `super::start(inProvider)`
- `ret = userClient->mDevice->enableClientManager(true, direction, userClient->mClientID) == 0 `
- `inArguments->scalarOutputCount == 1`
- `clientID < IOPAudio::ClientManagerDevice::kMaximumSupportedClients`
- `!(__builtin_popcountll(updatedClientIDMask) > 1)`
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/ClientManagerDevice/ClientManagerDevice.cpp`
- `ret = getNodeInterface()->getNodeProperty(ioPropertyDescriptor) == 0 `
- `setProperty(\"IOUserClientClass\", kIOUserClientClassName)`
- `IOUserClientDefaultLockingSetProperties`
- `!((inArguments->scalarInput) == nullptr)`
- `power-up-on-set-power-state-on`
- `power-down-on-uc-close`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `!((userClient) == nullptr)`
- `ret = _retrieveConfig(inProvider, mClientManagerDeviceConfig) == 0 `
- `ret = getNodeInterface()->setNodeProperty(inPropertyDescriptor) == 0 `
- `ret = _enableClientManagerForMask(false, kIODirectionNone, kClientIDMask) == 0 `
- `!((dataPtr) == nullptr)`
- `121111121222121211111111111112`
- `ret = userClient->mDevice->setNodeProperty(propertyDescriptor) == 0 `
- `ret = super::_retrieveDeviceConfig(inProvider, ioConfig) == 0 `
- `IOUserClientEntitlements`
- `!(static_cast<bool>(mOpenedClientMasks & clientIDMask))`
- `IOPAudioClientManagerDevice`
- `site.IOPAudioClientManagerDevice`
- `target-power-on-state`
- `publish-user-client`
- `!((userClient->mDevice) == nullptr)`
- `ret = userClient->mDevice->setClientManagerPowerRequest(*powerRequest) == 0 `
- `_handleSetPowerState`
- `i8@?0`
- `ret = _enableClientManagerPowerRequest(inEnable, inDirection) == 0 `
- `IOUserClientDefaultLocking`
- `!((inArguments->structureInput) == nullptr)`

**[__TEXT.__os_log]**

- `%s: %s, %s file: %s, line: %d\n`
- `%s::%s(%lu) disabling client managers [PreviousEnabledMask=%#llx mCurrentlyEnabledMask=%#llx ret=%#x]`
- `%s::%s(%lu) re-enabling client managers [PreviousEnabledMask=%#llx mCurrentlyEnabledMask=%#llx ret=%#x]`

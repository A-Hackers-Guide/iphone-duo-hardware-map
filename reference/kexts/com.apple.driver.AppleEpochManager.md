# `com.apple.driver.AppleEpochManager`

- Name: AppleEpochManager
- Version: `1`
- UUID: `28AF847F-8F3F-3615-B270-7A884B7E5AC8`
- Source version: `17.0.0.0.0`
- Depends on: [`com.apple.driver.AppleSEPManager`](com.apple.driver.AppleSEPManager.md) 1.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (1) [KC]

### AppleEpochManager
- `CFBundleIdentifier`: `com.apple.driver.AppleEpochManager`
- `IOClass`: `AppleEpochManager`
- `IOMatchCategory`: `AppleEpochManager`
- `IOPersonalityPublisher`: `com.apple.driver.AppleEpochManager`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `SEP`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleEpochManager` | 0xb8 | IOService → IORegistryEntry |
| `AppleEpochManagerUserClient` | 0xe0 | IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000fb8 off=0x004628c0-0x00463878 addr=0xfffffe00074668c0-0xfffffe0007467878 r--/r--   __TEXT            
	sz=0x00000953 off=0x00462ee8-0x0046383b addr=0xfffffe0007466ee8-0xfffffe000746783b               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000038 off=0x00463840-0x00463878 addr=0xfffffe0007467840-0xfffffe0007467878               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00001d20 off=0x01c9f6d0-0x01ca13f0 addr=0xfffffe0008ca36d0-0xfffffe0008ca53f0 r-x/r-x   __TEXT_EXEC       
	sz=0x00001b20 off=0x01c9f6d0-0x01ca11f0 addr=0xfffffe0008ca36d0-0xfffffe0008ca51f0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000200 off=0x01ca11f0-0x01ca13f0 addr=0xfffffe0008ca51f0-0xfffffe0008ca53f0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000130 off=0x04940c70-0x04940da0 addr=0xfffffe000b944c70-0xfffffe000b944da0 rw-/rw-   __DATA            
	sz=0x000000d0 off=0x04940c70-0x04940d40 addr=0xfffffe000b944c70-0xfffffe000b944d40               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000b944d40-0xfffffe000b944da0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00000e98 off=0x01096428-0x010972c0 addr=0xfffffe000809a428-0xfffffe000809b2c0 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x01096428-0x01096438 addr=0xfffffe000809a428-0xfffffe000809a438         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x01096438-0x01096448 addr=0xfffffe000809a438-0xfffffe000809a448         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000cb8 off=0x01096448-0x01097100 addr=0xfffffe000809a448-0xfffffe000809b100         __DATA_CONST.__const            
	sz=0x00000080 off=0x01097100-0x01097180 addr=0xfffffe000809b100-0xfffffe000809b180         __DATA_CONST.__kalloc_type      
	sz=0x00000100 off=0x01097180-0x01097280 addr=0xfffffe000809b180-0xfffffe000809b280         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000040 off=0x01097280-0x010972c0 addr=0xfffffe000809b280-0xfffffe000809b2c0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 72 at 0x04ad9704
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     28AF847F-8F3F-3615-B270-7A884B7E5AC8
008: LC_SOURCE_VERSION           17.0.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9f910 size=0x60
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleEpochManager`
- `CFBundleIdentifier`: `com.apple.driver.AppleEpochManager`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleEpochManager`
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
- `NSHumanReadableCopyright`: `Copyright © 2022-2023 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEpochManager.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901200704`
- `_PrelinkExecutableRelativePath`: `AppleEpochManager`
- `_PrelinkExecutableSize`: `15520`
- `_PrelinkExecutableSourceAddr`: `-2198901200704`
- `_PrelinkKmodInfo`: `-2198828987280`

## Strings (65) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `nullptr != epoch_array`
- `%s%s:\n%s    super did not start\n`
- `void AppleEpochManager::processEpochProposalsGated()`
- `%s%s:\n%s    Epoch proposals committed\n`
- `bool AppleEpochManager::setBuddyDone(bool)`
- `nullptr != name`
- `%s%s:\n%s    starting\n`
- `_aem != NULL`
- `site.AppleEpochManager`
- `INIT: `
- `clientClassName`
- `nullptr != buddy_done_data`
- `len > 0 && (size_t)len < sizeof(bootarg_name)`
- `dc_epoch_roll`
- `!(_passed_berb && _passed_refk)`
- `IONVRAM`
- `owningTask != NULL`
- `/arm-io/sep/iop-sep-nub/Sandcat`
- `asked to but NOT `
- `AppleEpochManagerUserClient.cpp`
- `seeker-passed-refk`
- `/Library/Caches/com.apple.xbs/0896B3D0-4755-4106-AE97-16B9AF5EF03F/TemporaryDirectory.H9Znna/Sources/AppleEpochManager/AppleEpochManager.cpp`
- `%s%s:\n%s    Option \"%s\" set to %u by boot-arg \"%s\"\n`
- `AppleEpochManager.cpp`
- `static IOReturn AppleEpochManagerUserClient::DispatchUserClientBuddyComplete(AppleEpochManagerUserClient *, void *, IOExternalMethodArguments *)`
- `seeker-found-refk`
- `getWorkLoop()->inGate()`
- `IOReturn AppleEpochManager::signalBuddyDoneGated()`
- `AppleEpochManagerUserClient`
- `target->_aem`
- `AppleEpochManager`
- `%s%s:\n%s    %scommitting epoch slot %d:%d\n`
- `virtual bool AppleEpochManager::start(IOService *)`
- `ERROR: `
- `kIOReturnSuccess == _workloop->addEventSource(_command_gate)`
- `%s%s:\n%s    Buddy done not set.\n`
- `seeker-manifest-eply`
- `40A0DDD2-77F8-4392-B4A3-1E7304206516:BuddyDone`
- `virtual bool AppleEpochManagerUserClient::initWithTask(task_t, void *, UInt32)`
- `nullptr != sandcat_node`
- `bool AppleEpochManager::_updateEpochCommits(SEPEpoch::Epoch *, SEPEpoch::EpochIndex, uint8_t)`
- `factory_key_disable`
- `IODTNVRAM`
- `site.AppleEpochManagerUserClient`
- `/Library/Caches/com.apple.xbs/0896B3D0-4755-4106-AE97-16B9AF5EF03F/TemporaryDirectory.H9Znna/Sources/AppleEpochManager/AppleEpochManagerUserClient.cpp`
- `com.apple.private.appleepochmanager.allow`
- `%s%s:\n%s    Option \"%s\" enabled by presence in EDT\n`
- `%s%s:\n%s    Cannot find Sandcat DT node (%s)\n`
- `%s%s:\n%s    Failed to write buddy done nvram.\n`
- `12111112122212121221111`
- `seeker-found-berb`
- `%s%s:\n%s    thread_call_allocate failed\n`
- `%s%s:\n%s    Option \"%s\" disabled by absence in EDT\n`
- `seeker-passed-berb`
- `nullptr != sync_now`
- `virtual bool AppleEpochManagerUserClient::start(IOService *)`
- `size == sizeof(_eply)`
- `IONVRAM-FORCESYNCNOW-PROPERTY`
- `1211111212221212111111111111`
- `\"%s:%s:%u: REQUIRE failed: %s\" @%s:%d`
- `target`
- `bool AppleEpochManager::_getSandcatOption(DTEntry, const char *)`
- `sandcat_%s`
- `size == sizeof(uint32_t)`
- `seeker-restore`

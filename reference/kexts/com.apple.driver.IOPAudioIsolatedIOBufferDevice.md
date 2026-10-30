# `com.apple.driver.IOPAudioIsolatedIOBufferDevice`

- Name: IOPAudioIsolatedIOBufferDevice
- Version: `400.36`
- UUID: `BCA9A9A1-C62E-3466-8A03-C6BAD85B7C1A`
- Source version: `400.36.0.0.0`
- Depends on: [`com.apple.driver.ExclavesAudioKext`](com.apple.driver.ExclavesAudioKext.md) 1.0, [`com.apple.iokit.IOPAudioDriverFamily`](com.apple.iokit.IOPAudioDriverFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0

## Device-tree nodes it binds (1) [DT][KC]

| Node | IOClass | matched on |
|---|---|---|
| [`/arm-io/iop-audio-controller/lp-mic-io-buffer-device`](../devicetree/root__arm-io__iop-audio-controller__lp-mic-io-buffer-device.md) | `IOPAudioIsolatedIOBufferDevice` | `iop-audio,isolated-io-buffer-device` |

## IOKit personalities (1) [KC]

### IsolatedIOBufferDevice
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioIsolatedIOBufferDevice`
- `IOClass`: `IOPAudioIsolatedIOBufferDevice`
- `IOExclaveProxy`: `True`
- `IONameMatch`:
  - `iop-audio,isolated-io-buffer-device`
- `IOPersonalityPublisher`: `com.apple.driver.IOPAudioIsolatedIOBufferDevice`
- `IOProviderClass`: `IOPAudioNode`
- `IOUserClientClass`: `IOPAudioIsolatedIOBufferDeviceUserClient`


## C++ classes (2) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOPAudioIsolatedIOBufferDevice` | 0xb8 | IOPAudioDevice → IOService → IORegistryEntry |
| `IOPAudioIsolatedIOBufferDeviceUserClient` | 0xe8 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001248 off=0x00a34a50-0x00a35c98 addr=0xfffffe0007a38a50-0xfffffe0007a39c98 r--/r--   __TEXT            
	sz=0x000006da off=0x00a35118-0x00a357f2 addr=0xfffffe0007a39118-0xfffffe0007a397f2               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000049a off=0x00a357f2-0x00a35c8c addr=0xfffffe0007a397f2-0xfffffe0007a39c8c               __TEXT.__os_log           
	sz=0x00000008 off=0x00a35c90-0x00a35c98 addr=0xfffffe0007a39c90-0xfffffe0007a39c98               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00002b50 off=0x032fb380-0x032fded0 addr=0xfffffe000a2ff380-0xfffffe000a301ed0 r-x/r-x   __TEXT_EXEC       
	sz=0x00002a50 off=0x032fb380-0x032fddd0 addr=0xfffffe000a2ff380-0xfffffe000a301dd0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000100 off=0x032fddd0-0x032fded0 addr=0xfffffe000a301dd0-0xfffffe000a301ed0          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000130 off=0x04a14410-0x04a14540 addr=0xfffffe000ba18410-0xfffffe000ba18540 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04a14410-0x04a144d8 addr=0xfffffe000ba18410-0xfffffe000ba184d8               __DATA.__data             
	sz=0x00000060 off=0x00000000-0x00000060 addr=0xfffffe000ba184d8-0xfffffe000ba18538               __DATA.__common           (Zerofill)
	sz=0x00000008 off=0x00000000-0x00000008 addr=0xfffffe000ba18538-0xfffffe000ba18540               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00001018 off=0x013cb690-0x013cc6a8 addr=0xfffffe00083cf690-0xfffffe00083d06a8 rw-/rw-   __DATA_CONST      
	sz=0x00000010 off=0x013cb690-0x013cb6a0 addr=0xfffffe00083cf690-0xfffffe00083cf6a0         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000010 off=0x013cb6a0-0x013cb6b0 addr=0xfffffe00083cf6a0-0xfffffe00083cf6b0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00000eb8 off=0x013cb6b0-0x013cc568 addr=0xfffffe00083cf6b0-0xfffffe00083d0568         __DATA_CONST.__const            
	sz=0x00000080 off=0x013cc568-0x013cc5e8 addr=0xfffffe00083d0568-0xfffffe00083d05e8         __DATA_CONST.__kalloc_type      
	sz=0x00000080 off=0x013cc5e8-0x013cc668 addr=0xfffffe00083d05e8-0xfffffe00083d0668         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000040 off=0x013cc668-0x013cc6a8 addr=0xfffffe00083d0668-0xfffffe00083d06a8         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 40 at 0x04af5ae0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     BCA9A9A1-C62E-3466-8A03-C6BAD85B7C1A
008: LC_SOURCE_VERSION           400.36.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ac3c20 size=0x98
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleExecutable`: `IOPAudioIsolatedIOBufferDevice`
- `CFBundleIdentifier`: `com.apple.driver.IOPAudioIsolatedIOBufferDevice`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOPAudioIsolatedIOBufferDevice`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOPAudioIsolatedIOBufferDevice.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895097264`
- `_PrelinkExecutableRelativePath`: `IOPAudioIsolatedIOBufferDevice`
- `_PrelinkExecutableSize`: `20192`
- `_PrelinkExecutableSourceAddr`: `-2198895097264`
- `_PrelinkKmodInfo`: `-2198828121072`

## Strings (37) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `site.IOPAudioIsolatedIOBufferDeviceUserClient`
- `super::start(inProvider)`
- `IOUserClientDefaultLocking`
- `!(isSuspended())`
- `IOPAudioIsolatedIOBufferDevice`
- `IOPAudioIsolatedIOBufferDeviceUserClient`
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/IsolatedIOBufferDevice/UserClient/IsolatedIOBufferDeviceUserClient.cpp`
- `IOUserClient::initWithTask(inOwningTask, inSecurityToken, inType, inProperties)`
- `IOUserClientDefaultLockingSetProperties`
- `ret = userClient->mDevice->setupClientIO(clientID, bufferFrameSize) == 0 `
- `ret = super::_handleDeviceReady(inProvider) == 0 `
- `i8@?0`
- `12111112122212121111111111111`
- `IOUserClientEntitlements`
- `ret = userClient->mDevice->setStreamDescription(*streamDescription, bufferFrameSize) == 0 `
- `IsolatedIOBufferDeviceUserClient`
- `!((mDriverInterface) == nullptr)`
- `!((mDevice) == nullptr)`
- `ret = userClient->mDevice->teardownIO() == 0 `
- `ret = userClient->mDevice->teardownClientIO(clientID) == 0 `
- `mDevice->open(this)`
- `!((userClient->mDevice) == nullptr)`
- `ret = userClient->mDevice->setupIO() == 0 `
- `ret = mDriverInterface->mapDMABuffer() == 0 `
- `ret = mDevice->readInput(clientID, sampleTime, frames) == 0 `
- `com.apple.private.aop-audio.user-access`
- `ret = super::_handleStart(inProvider) == 0 `
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `!((userClient) == nullptr)`
- `ret = userClient->mDevice->getStreamDescription(*streamDescription) == 0 `
- `entitlement == kOSBooleanTrue`
- `/Library/Caches/com.apple.xbs/20732553-D3E1-4B38-B5F5-87A23D935C9E/TemporaryDirectory.oCjbCa/Sources/IOPAudioDrivers/src/kext/IsolatedIOBufferDevice/Device/IsolatedIOBufferDevice.cpp`
- `ret = _configure(inProvider) == 0 `
- `!((mEndpoint) == nullptr)`
- `site.IOPAudioIsolatedIOBufferDevice`
- `12111112122212121111211`

**[__TEXT.__os_log]**

- `%s: %s, %s file: %s, line: %d\n`

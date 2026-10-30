# `com.apple.driver.AppleAOPHaptics`

- Name: AppleAOPHaptics
- Version: `1010.2`
- UUID: `74D43C10-1697-3F62-B2CD-DDE70EA5A2B1`
- Source version: `1010.2.0.0.0`
- Depends on: [`com.apple.driver.AppleAOPAudio`](com.apple.driver.AppleAOPAudio.md) 1.1, [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0, [`com.apple.driver.AppleEmbeddedAudio`](com.apple.driver.AppleEmbeddedAudio.md) 1.1.0, [`com.apple.driver.AppleIISController`](com.apple.driver.AppleIISController.md) 1.0, [`com.apple.iokit.AppleARMIISAudio`](com.apple.iokit.AppleARMIISAudio.md) 1.0, [`com.apple.iokit.IOAudio2Family`](com.apple.iokit.IOAudio2Family.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (2) [KC]

### AppleAOPHapticsAudio
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPHaptics`
- `IOClass`: `AppleAOPHaptics`
- `IOMatchCategory`: `AppleAOPHaptics`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPHaptics`
- `IOPropertyMatch`:
  - `compatible`: `aop-audio-haptic`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`

### AppleAOPHapticsDebug
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPHaptics`
- `IOClass`: `AppleAOPInput`
- `IOPersonalityPublisher`: `com.apple.driver.AppleAOPHaptics`
- `IOPropertyMatch`:
  - `compatible`: `aop-audio-hpdbg`
- `IOProviderClass`: `AppleAOPAudioDeviceNode`
- `IOResourceMatch`: `IOKit`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleAOPEmbeddedAudio` | 0x1f0 | AppleEmbeddedAudio → IOService → IORegistryEntry |
| `AppleAOPHaptics` | 0x230 | AppleAOPEmbeddedAudio → AppleEmbeddedAudio → IOService → IORegistryEntry |
| `AppleAOPInput` | 0x208 | AppleAOPEmbeddedAudio → AppleEmbeddedAudio → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001221 off=0x00436ea0-0x004380c1 addr=0xfffffe000743aea0-0xfffffe000743c0c1 r--/r--   __TEXT            
	sz=0x0000068b off=0x00437518-0x00437ba3 addr=0xfffffe000743b518-0xfffffe000743bba3               __TEXT.__cstring          (CstringLiterals)
	sz=0x000001e8 off=0x00437ba8-0x00437d90 addr=0xfffffe000743bba8-0xfffffe000743bd90               __TEXT.__const            
	sz=0x00000331 off=0x00437d90-0x004380c1 addr=0xfffffe000743bd90-0xfffffe000743c0c1               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00002de8 off=0x01bff3a0-0x01c02188 addr=0xfffffe0008c033a0-0xfffffe0008c06188 r-x/r-x   __TEXT_EXEC       
	sz=0x00002c18 off=0x01bff3a0-0x01c01fb8 addr=0xfffffe0008c033a0-0xfffffe0008c05fb8          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001d0 off=0x01c01fb8-0x01c02188 addr=0xfffffe0008c05fb8-0xfffffe0008c06188          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x0493e198-0x0493e2e8 addr=0xfffffe000b942198-0xfffffe000b9422e8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x0493e198-0x0493e260 addr=0xfffffe000b942198-0xfffffe000b942260               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b942260-0xfffffe000b9422e8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000024f0 off=0x01074038-0x01076528 addr=0xfffffe0008078038-0xfffffe000807a528 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x01074038-0x01074050 addr=0xfffffe0008078038-0xfffffe0008078050         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x01074050-0x01074068 addr=0xfffffe0008078050-0xfffffe0008078068         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00002268 off=0x01074068-0x010762d0 addr=0xfffffe0008078068-0xfffffe000807a2d0         __DATA_CONST.__const            
	sz=0x00000140 off=0x010762d0-0x01076410 addr=0xfffffe000807a2d0-0xfffffe000807a410         __DATA_CONST.__kalloc_type      
	sz=0x000000e8 off=0x01076410-0x010764f8 addr=0xfffffe000807a410-0xfffffe000807a4f8         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000030 off=0x010764f8-0x01076528 addr=0xfffffe000807a4f8-0xfffffe000807a528         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 64 at 0x04ad7dc4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     74D43C10-1697-3F62-B2CD-DDE70EA5A2B1
008: LC_SOURCE_VERSION           1010.2.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9e808 size=0xb8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleAOPHaptics`
- `CFBundleIdentifier`: `com.apple.driver.AppleAOPHaptics`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleAOPHaptics`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1010.2`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1010.2`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleEmbeddedAudio.kext/PlugIns/AppleAOPHaptics.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901379424`
- `_PrelinkExecutableRelativePath`: `AppleAOPHaptics`
- `_PrelinkExecutableSize`: `26185`
- `_PrelinkExecutableSourceAddr`: `-2198901379424`
- `_PrelinkKmodInfo`: `-2198828998248`

## Strings (60) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `%s::%s(state=%d) failed [errorCode: 0x%x]\n`
- `AppleAOPEmbeddedAudio::%s unable to create matching dictionary\n`
- `compatible`
- `%s::%s() using default audio enable warm up time %d ms\n`
- `_notifyHapticsSessionStartStop`
- `AppleAOPInput`
- `preflightMultiControl`
- `%s::%s(inSelectors=%p) failed [result: 0x%x]\n`
- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/AppleAOPEmbeddedAudio.cpp`
- `AppleAOPEmbeddedAudio::%s unable to retrieve matching interface\n`
- `_setupAudioEnableWarmupDelay`
- `/Library/Caches/com.apple.xbs/7374CF14-96FD-494A-A9F3-D02707F144CC/TemporaryDirectory.6UQLML/Sources/AppleEmbeddedAudio/AppleAOPInput.cpp`
- `setDevicePowerState`
- `_obtainAOPNub`
- `%s::%s() using default parking timeout value of %d ms\n`
- `start`
- `stop`
- `%s::Unable to notify Haptics Session %s %d\n`
- `site.AppleAOPInput`
- `%s::%s handleStartFailed\n`
- `Unable to locate __powerThermalBudgetChangeFunction handler.\n`
- `IODeviceTree:/product/audio`
- `site.AppleEmbeddedAudioRangeInfo`
- `12111112122212121121212111211111111121111111211121112111111112`
- `%s::%s Failed with error::%x\n`
- `AppleAOPAudioDeviceProvider`
- `site.AppleAOPHaptics`
- `_setupParkingTimeout`
- `SetMultiControl`
- `_obtainDefaultInputSelectors`
- `handleStart`
- `Error obtaining AOP register nub\n`
- `AppleAOPEmbeddedAudio`
- `site.AppleAOPEmbeddedAudio`
- `AppleAOPHaptics`
- `1211111212221212112121211121111111112111111121112111211111111211221112`
- `Unable to locate _powerPeakBudgetChangeFunction handler.\n`
- `12111112122212121121212111211111111121111111211121112111111112111`
- `%s::%s(..) unable to create OSNumber. [selectorIndex=%u]\n`
- `AppleAOPEmbeddedAudio::%s unable to create OSDictionary\n`
- `AppleAOPEmbeddedAudio::%s unable to create OSSymbol\n`
- `DeviceAttached`

**[__TEXT.__os_log]**

- `Unable to locate _powerPeakBudgetChangeFunction handler.`
- `%s::%s() using default audio enable warm up time %d ms`
- `AppleAOPEmbeddedAudio::%s unable to create matching dictionary`
- `AppleAOPEmbeddedAudio::%s unable to create OSDictionary`
- `%s::Unable to notify Haptics Session %s %d`
- `%s::%s(..) unable to create OSNumber. [selectorIndex=%u]`
- `+ %s::%s\n`
- `- %s::%s\n`
- `%s::%s() using default parking timeout value of %d ms`
- `%s::%s(inSelectors=%p) failed [result: 0x%x]`
- `+- %s::%s (%p)\n`
- `Unable to locate __powerThermalBudgetChangeFunction handler.`
- `%s::%s handleStartFailed`
- `%s::%s Failed with error::%x`
- `Error obtaining AOP register nub`
- `%s::%s(state=%d) failed [errorCode: 0x%x]`
- `AppleAOPEmbeddedAudio::%s unable to create OSSymbol`
- `AppleAOPEmbeddedAudio::%s unable to retrieve matching interface`

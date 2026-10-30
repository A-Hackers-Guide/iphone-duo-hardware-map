# `com.apple.driver.AppleH10PearlCameraInterface`

- Name: AppleH10PearlCamInterface
- Version: `22.304.0`
- UUID: `FB5656C4-0C2F-3F00-9E17-1379E82CAAAF`
- Source version: `22.304.0.0.0`
- Depends on: [`com.apple.driver.AppleARMPlatform`](com.apple.driver.AppleARMPlatform.md) 1.0.0, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0.0, [`com.apple.iokit.IOSurface`](com.apple.iokit.IOSurface.md) 52.6.0, [`com.apple.kec.corecrypto`](com.apple.kec.corecrypto.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 8.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (18) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleH10PearlCamInterface` | 0x88 | IOService → IORegistryEntry |
| `BoxFilter` | 0x10 |  |
| `PearlCamAbortMessage` | 0x20 | PearlCamMessage |
| `PearlCamDoBioCaptureMessage` | 0x28 | PearlCamMessage |
| `PearlCamDoRetryMessage` | 0x20 | PearlCamMessage |
| `PearlCamDoSecretPatternMessage` | 0x28 | PearlCamMessage |
| `PearlCamFaceDetectStatusMessage` | 0x28 | PearlCamMessage |
| `PearlCamFrameReceiverFramesMessage` | 0xa8 | PearlCamMessage |
| `PearlCamMessage` | 0x18 |  |
| `PearlCamNotificationMessage` | 0x28 | PearlCamMessage |
| `PearlCamPowerOffMessage` | 0x18 | PearlCamMessage |
| `PearlCamPowerOnMessage` | 0x28 | PearlCamMessage |
| `PearlCamReportErrorMessage` | 0x20 | PearlCamMessage |
| `PearlCamSendBuffersMessage` | 0x28 | PearlCamMessage |
| `PearlCamStartMessage` | 0x30 | PearlCamMessage |
| `PearlCamStopMessage` | 0x18 | PearlCamMessage |
| `PearlCamTimerTimeoutMessage` | 0x20 | PearlCamMessage |
| `PearlCamUtilities` | 0x10 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00000dd3 off=0x0047f550-0x00480323 addr=0xfffffe0007483550-0xfffffe0007484323 r--/r--   __TEXT            
	sz=0x0000067b off=0x0047fb78-0x004801f3 addr=0xfffffe0007483b78-0xfffffe00074841f3               __TEXT.__cstring          (CstringLiterals)
	sz=0x00000130 off=0x004801f3-0x00480323 addr=0xfffffe00074841f3-0xfffffe0007484323               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00007be8 off=0x01d17760-0x01d1f348 addr=0xfffffe0008d1b760-0xfffffe0008d23348 r-x/r-x   __TEXT_EXEC       
	sz=0x00007b28 off=0x01d17760-0x01d1f288 addr=0xfffffe0008d1b760-0xfffffe0008d23288          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000000c0 off=0x01d1f288-0x01d1f348 addr=0xfffffe0008d23288-0xfffffe0008d23348          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000003a8 off=0x04942850-0x04942bf8 addr=0xfffffe000b946850-0xfffffe000b946bf8 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04942850-0x04942918 addr=0xfffffe000b946850-0xfffffe000b946918               __DATA.__data             
	sz=0x000002e0 off=0x00000000-0x000002e0 addr=0xfffffe000b946918-0xfffffe000b946bf8               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x00002060 off=0x010b62a0-0x010b8300 addr=0xfffffe00080ba2a0-0xfffffe00080bc300 rw-/rw-   __DATA_CONST      
	sz=0x00000008 off=0x010b62a0-0x010b62a8 addr=0xfffffe00080ba2a0-0xfffffe00080ba2a8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000008 off=0x010b62a8-0x010b62b0 addr=0xfffffe00080ba2a8-0xfffffe00080ba2b0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001b50 off=0x010b62b0-0x010b7e00 addr=0xfffffe00080ba2b0-0xfffffe00080bbe00         __DATA_CONST.__const            
	sz=0x00000480 off=0x010b7e00-0x010b8280 addr=0xfffffe00080bbe00-0xfffffe00080bc280         __DATA_CONST.__kalloc_type      
	sz=0x00000060 off=0x010b8280-0x010b82e0 addr=0xfffffe00080bc280-0xfffffe00080bc2e0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000020 off=0x010b82e0-0x010b8300 addr=0xfffffe00080bc2e0-0xfffffe00080bc300         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 28 at 0x04ada86c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     FB5656C4-0C2F-3F00-9E17-1379E82CAAAF
008: LC_SOURCE_VERSION           22.304.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aa0b20 size=0x1c8
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleH10PearlCameraInterface`
- `CFBundleIdentifier`: `com.apple.driver.AppleH10PearlCameraInterface`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleH10PearlCamInterface`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `22.304.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `22.304.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2016-2017 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `1.0.0`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleH10PearlCameraInterface.kext`
- `_PrelinkExecutableLoadAddr`: `-2198901082800`
- `_PrelinkExecutableRelativePath`: `AppleH10PearlCameraInterface`
- `_PrelinkExecutableSize`: `44483`
- `_PrelinkExecutableSourceAddr`: `-2198901082800`
- `_PrelinkKmodInfo`: `-2198828980144`

## Strings (94) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `BoxFilter::%s - invalid input! inData:%p outData:%p filterSize:%u\n`
- `PearlCamUtilities::%s - invalid input! inData:%p mean:%p std:%p bc:%p bf:%p\n`
- `PearlCamUtilities::%s - invalid input!\n`
- `PearlCamUtilities::%s - invalid input! inPackedBuf:%p roi:%p outUnpackedBuf:%p\n`

**[__TEXT.__cstring]**

- `12211`
- `PearlCamStopMessage`
- `site.PearlCamStopMessage`
- `Notification`
- `PowerUpFailure`
- `StreamStartupFailure`
- `SecretCaptureTimeout`
- `unpackRaw10`
- `site.PearlCamDoRetryMessage`
- `122222222222222222222`
- `PearlCamAbortMessage`
- `BoxFilter`
- `12111112122212121`
- `Busy`
- `nth_smallest_element`
- `site.PearlCamDoBioCaptureMessage`
- `PowerOn`
- `PearlCamMessage`
- `site.PearlCamStartMessage`
- `site.PearlCamAbortMessage`
- `ESDFailure`
- `122`
- `site.PearlCamSendBuffersMessage`
- `site.PearlCamDoSecretPatternMessage`
- `PearlCamFrameReceiverFramesMessage`
- `ReportError`
- `DoFasterAutoFlow`
- `InvalidMessageType`
- `PearlCamDoSecretPatternMessage`
- `Unknown`
- `IllegalRetryMode`
- `PearlCamDoBioCaptureMessage`
- `12212`
- `PearlCamReportErrorMessage`
- `site.PearlCamPowerOnMessage`
- `site.PearlCamFaceDetectStatusMessage`
- `site.PearlCamFrameReceiverFramesMessage`
- `DoBioCapture`
- `DoRetry`
- `site.PearlCamMessage`
- `PearlCamPowerOffMessage`
- `PearlCamUtilities`
- `Stop`
- `DoFastAutoFlow`
- `GeneralError`
- `PPMError`
- `PPMNoPower`
- `FDRNotValidated`
- `HardwareCheckFailed`
- `SPMIError`
- `site.PearlCamReportErrorMessage`
- `PearlCamTimerTimeoutMessage`
- `PearlCamNotificationMessage`
- `AppleH10PearlCamInterface`
- `DoSecretPattern`
- `FrameReceiverFrames`
- `SequenceError`
- `FrameReceivedTimeout`
- `PearlCamPowerOnMessage`
- `122121`
- `site.BoxFilter`
- `Start`
- `Abort`
- `ChannelReleased`
- `BF1DCoreU8`
- `filterData`
- `site.PearlCamPowerOffMessage`
- `site.PearlCamUtilities`
- `FaceDetectStatus`
- `TimerTimeout`
- `BioCaptureTimeout`
- `bimodalityCoef`
- `PearlCamSendBuffersMessage`
- `PearlCamDoRetryMessage`
- `1222`
- `site.PearlCamNotificationMessage`
- `12`
- `site.AppleH10PearlCamInterface`
- `SendBuffers`
- `FaceDetectTimeout`
- `DoAutoFlow`
- `StreamingFailure`
- `FirmwareFailure`
- `12221`
- `PearlCamStartMessage`
- `PearlCamFaceDetectStatusMessage`
- `site.PearlCamTimerTimeoutMessage`
- `PowerOff`
- `DoAutoEnroll`
- `DoAutoAttention`

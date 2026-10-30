# `com.apple.iokit.IOGameControllerFamily`

- Name: IOGameControllerFamily
- Version: `14.1.2`
- UUID: `BFF99FD6-13F5-3EFD-B643-890A225C96AA`
- Source version: `14.1.2.0.0`
- Depends on: [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 2.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 22.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 22.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 12.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 22.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 11.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (4) [KC]

### Dynamic IOHIDDevice Probe
- `CFBundleIdentifier`: `com.apple.iokit.IOGameControllerFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsage`: `5`
    - `DeviceUsagePage`: `1`
- `IOClass`: `IOGCDynamicDeviceProbe`
- `IOMatchCategory`: `GameController`
- `IOPersonalityPublisher`: `com.apple.iokit.IOGameControllerFamily`
- `IOProbeScore`: `100`
- `IOProviderClass`: `IOHIDDevice`
- `IOUserClientClass`: `IOGCDynamicDeviceProbeUserClient`

### PSVR2 Sense Left Controller Personality
- `CFBundleIdentifier`: `com.apple.iokit.IOGameControllerFamily`
- `GameControllerCategory`: `psvr2`
- `IOClass`: `PSVR2SenseDevice`
- `IOPersonalityPublisher`: `com.apple.iokit.IOGameControllerFamily`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryUsage`: `5`
- `PrimaryUsagePage`: `1`
- `ProductID`: `3653`
- `VendorID`: `1356`

### PSVR2 Sense Right Controller Personality
- `CFBundleIdentifier`: `com.apple.iokit.IOGameControllerFamily`
- `GameControllerCategory`: `psvr2`
- `IOClass`: `PSVR2SenseDevice`
- `IOPersonalityPublisher`: `com.apple.iokit.IOGameControllerFamily`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryUsage`: `5`
- `PrimaryUsagePage`: `1`
- `ProductID`: `3654`
- `VendorID`: `1356`

### PSVR2SenseDevice User Client
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.iokit.IOGameControllerFamily`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `PSVR2SenseDevice`
- `IOProviderMergeProperties`:
  - `GameControllerSupport`: `True`
  - `HIDServiceSupport`: `True`
  - `IOCFPlugInTypes`:
    - `217D5BAD-AB5E-4323-9C00-2AE488D5DA87`: `IOGameControllerFamily.kext/PlugIns/PSVR2.plugin`
    - `F25FF3C2-330F-4B52-8207-A0D6F23DF0CD`: `IOGameControllerFamily.kext/PlugIns/PSVR2.plugin`


## C++ classes (16) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `IOGCCircularControlQueue` | 0x48 | IODataQueue |
| `IOGCCircularDataQueue` | 0x60 | IODataQueue |
| `IOGCCircularDataQueueCursor` | 0x28 |  |
| `IOGCCommandQueue` | 0x68 | IOEventSource |
| `IOGCDynamicDeviceProbe` | 0xa0 | IOService → IORegistryEntry |
| `IOGCDynamicDeviceProbeUserClient` | 0xe8 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `IOGCPortNotifier` | 0x40 | IODataQueue |
| `IOGCResource` | 0x90 | IOService → IORegistryEntry |
| `IOHIDGCDevice` | 0xc0 | IOService → IORegistryEntry |
| `PSVR2SenseDevice` | 0x198 | IOHIDGCDevice → IOService → IORegistryEntry |
| `PSVR2SenseDeviceFastPathUserClient` | 0xf0 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `PSVR2SenseDeviceFastPathUserClientHapticsQueue` | 0xa8 | PSVR2SenseDeviceFastPathUserClientQueue → IOService → IORegistryEntry |
| `PSVR2SenseDeviceFastPathUserClientInputQueue` | 0xa8 | PSVR2SenseDeviceFastPathUserClientQueue → IOService → IORegistryEntry |
| `PSVR2SenseDeviceFastPathUserClientQueue` | 0xa0 | IOService → IORegistryEntry |
| `PSVR2SenseDeviceFastPathUserClientTrackingQueue` | 0xa8 | PSVR2SenseDeviceFastPathUserClientQueue → IOService → IORegistryEntry |
| `PSVR2SenseDeviceHIDEventServerUserClient` | 0xe8 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x000037b4 off=0x009e6230-0x009e99e4 addr=0xfffffe00079ea230-0xfffffe00079ed9e4 r--/r--   __TEXT            
	sz=0x00000480 off=0x009e6900-0x009e6d80 addr=0xfffffe00079ea900-0xfffffe00079ead80               __TEXT.__const            
	sz=0x0000104c off=0x009e6d80-0x009e7dcc addr=0xfffffe00079ead80-0xfffffe00079ebdcc               __TEXT.__cstring          (CstringLiterals)
	sz=0x00001c18 off=0x009e7dcc-0x009e99e4 addr=0xfffffe00079ebdcc-0xfffffe00079ed9e4               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x0001af7c off=0x03137030-0x03151fac addr=0xfffffe000a13b030-0xfffffe000a155fac r-x/r-x   __TEXT_EXEC       
	sz=0x0001aa3c off=0x03137030-0x03151a6c addr=0xfffffe000a13b030-0xfffffe000a155a6c          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000540 off=0x03151a6c-0x03151fac addr=0xfffffe000a155a6c-0xfffffe000a155fac          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000370 off=0x049f0ad8-0x049f0e48 addr=0xfffffe000b9f4ad8-0xfffffe000b9f4e48 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049f0ad8-0x049f0ba0 addr=0xfffffe000b9f4ad8-0xfffffe000b9f4ba0               __DATA.__data             
	sz=0x00000290 off=0x00000000-0x00000290 addr=0xfffffe000b9f4ba0-0xfffffe000b9f4e30               __DATA.__common           (Zerofill)
	sz=0x00000018 off=0x00000000-0x00000018 addr=0xfffffe000b9f4e30-0xfffffe000b9f4e48               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x000066f0 off=0x013772f0-0x0137d9e0 addr=0xfffffe000837b2f0-0xfffffe00083819e0 rw-/rw-   __DATA_CONST      
	sz=0x00000060 off=0x013772f0-0x01377350 addr=0xfffffe000837b2f0-0xfffffe000837b350         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000060 off=0x01377350-0x013773b0 addr=0xfffffe000837b350-0xfffffe000837b3b0         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00005a70 off=0x013773b0-0x0137ce20 addr=0xfffffe000837b3b0-0xfffffe0008380e20         __DATA_CONST.__const            
	sz=0x00000840 off=0x0137ce20-0x0137d660 addr=0xfffffe0008380e20-0xfffffe0008381660         __DATA_CONST.__kalloc_type      
	sz=0x000002a0 off=0x0137d660-0x0137d900 addr=0xfffffe0008381660-0xfffffe0008381900         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000e0 off=0x0137d900-0x0137d9e0 addr=0xfffffe0008381900-0xfffffe00083819e0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 196 at 0x04af20f4
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     BFF99FD6-13F5-3EFD-B643-890A225C96AA
008: LC_SOURCE_VERSION           14.1.2.0.0
009: LC_FUNCTION_STARTS          offset=0x004abfc08 size=0x380
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `IOGameControllerFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IOGameControllerFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOGameControllerFamily`
- `CFBundleNumericVersion`: `336756736`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1.0`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `14.1.2`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2026 Apple Inc. All rights reserved.`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOGameControllerFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895418832`
- `_PrelinkExecutableRelativePath`: `IOGameControllerFamily`
- `_PrelinkExecutableSize`: `151952`
- `_PrelinkExecutableSourceAddr`: `-2198895418832`
- `_PrelinkKmodInfo`: `-2198828266792`

## Strings (299) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `USB`
- `_11`
- `_21`
- `_23`
- `_28`
- `_29`
- `PrimaryUsage`
- `site.PSVR2SenseDeviceFastPathUserClientInputQueue`
- `v12@?0i8`
- `B8@?0`
- `_1`
- `_10`
- `_24`
- `_43`
- `Input.NormalizedThumbstickAxisSnapRadius`
- `site.PSVR2SenseDeviceFastPathUserClientTrackingQueue`
- `PSVR2HeldInHand`
- `%#0.2x`
- `site.PSVR2SenseDeviceHIDEventServerUserClient`
- `Product`
- `LED`
- `LED~Override`
- `12122`
- `site.PSVR2SenseDeviceFastPathUserClientQueue`
- `121111121222121211111111111112`
- `_15`
- `PhysicalDeviceUniqueID`
- `Input.NormalizedThumbstickDeadzoneRadius`
- `121112222112`
- `site.IOGCCircularDataQueueCursor`
- `v24@?0^v8Q16`
- `QueueChannel`
- `QueueID`
- `Sense Right`
- `121111121222121211111122`
- `22111111`
- `ReportInterval`
- `_3`
- `_7`
- `_30`
- `v20@?0^v8i16`
- `GameControllerSupport`
- `IOGCCircularDataQueue`
- `IOGCCircularDataQueueCursor`
- `com.apple.arkitd-objecttracking`
- `com.apple.gamecontroller`
- `121111121222121211111122111112221112111211111211212`
- `Bluetooth`
- `HIDVirtualDevice`
- `_19`
- `Input.NormalizedThumbstickMaxzoneRadius`
- `IOGCDynamicDeviceProbe`
- `_4`
- `_34`
- `_39`
- `v40@?0i8r^v12Q20{CRCResult=BII}28`
- `PSVR2SenseDeviceFastPathUserClientQueue`
- `12111112122212121112`
- `i24@?0^v8Q16`
- `i24@?0Q8@?<i@?^vQ>16`
- `IOUserClientDefaultLocking`
- `ProductID`
- `MV`
- `_20`
- `PSVR2SenseDeviceHIDEventServerUserClient`
- `LocationID`
- `UniformTypeIdentifiers`
- `12112222212111`
- `_5`
- `_PSVR2MotionCalibrationInfo`
- `PrimaryUsagePage`
- `Transport.TimeSynchronization~Override`
- `PSVR2SenseDeviceFastPathUserClientHapticsQueue`
- `site.struct SetReportContinuation`
- `com.apple.iohideventsystem.server`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `UC`
- `_40`
- `Input.NormalizedTriggerDeadzone`
- `PSVR2SenseDeviceFastPathUserClientTrackingQueue`
- `DynamicDevice`
- `site.IOHIDGCDevice`
- `site.PSVR2SenseDeviceFastPathUserClient`
- `PSVR2SenseDevice`
- `_26`
- `_42`
- `Transport.TimeSynchronization~Latest`
- `QueueCapacity`
- `GCSyntheticDevice`
- `site.IOGCDynamicDeviceProbeUserClient`
- `QueueGuard`
- `SS`
- `_35`
- `12111112122212121111111111111`
- `Transport.ReportInterval~Override`
- `IOGCCommandQueue`
- `com.apple.private.game-controller.dynamic-device-manager`
- `i92@?0^{IOGCCircularControlQueueMemory=QIIAQ[2{?=AQAQAQ}][0{IOGCCircularControlQueueEntry=QAQ[2{?=QQQ}][0C]}]}8Q16Q24I32Q36^AQ44Q52^AQ60Q68^AQ76@?<i@?Q@?<i@?^vQ>>84`
- `Debug`
- `BT`
- `_27`
- `_41`
- `Unknown`
- `Transport.TimeSynchronization`
- `Privileged`
- `_PSVR2FirmwareInfo`
- `com.sony.playstation.vr2-sense.left`
- `HI`
- `_2`
- `_9`
- `site.PSVR2SenseDevice`
- `com.sony.playstation.vr2-sense.right`
- `DeviceUsagePage`
- `site.IOGCResource`
- `com.apple.arkitd`
- `QueueMemorySize`
- `SerialNumber`
- `site.IOGCCircularControlQueue`
- `GameControllerEligible`
- `com.apple.gamecontroller.driver`
- ` (skipped CRC)`
- `Manufacturer`
- `DeviceUsagePairs`
- `HasDeviceSequenceIdentifiers`
- `VendorIDSource`
- `site.struct GetReportContinuation`
- `GameControllerSupportedHIDDevice`
- `11112`
- `Transport`
- `_17`
- `Power.Disconnect.OnBattery.AtLevel`
- `IOGCCircularControlQueue`
- `PSVR2`
- `v8@?0`
- `_31`
- `VersionNumber`
- `site.IOGCCircularDataQueue`
- `12111112122212121111`
- `IOUserClass`
- `com.apple.`
- `dynamic`
- `i8@?0`
- `_8`
- `v32@?0i8r^{?=[11c][8c]SSII[12C]SC[1C]b1b7[11C]}12{CRCResult=BII}20`
- `Power.Disconnect.OnBattery.AtLowVoltage`
- `1211121112111`
- `PSVR2Connection`
- `v12@?0B8`
- `_22`
- `_36`
- `DeviceUsage`
- `121112222`
- `2111111`
- `IOUserClientEntitlements`
- `QueueEntrySize`
- `com.sony.playstation.vr2-sense`
- `InputReportElements`
- `i16@?0@?<v@?i^{?=[11c][8c]SSII[12C]SC[1C]b1b7[11C]}{CRCResult=BII}>8`
- `_13`
- `B36@?0Q8B16^v20Q28`
- `mfi`
- `Sense Left`
- `v32@?0i8r^{?=b7b1(?=[58C][29C]{?=sssssssssssssssssssssssssssss}{?=sssssssssssss})}12{CRCResult=BII}20`
- `%#0.8x`
- `_14`
- `CFBundleIdentifier`
- `Rapport`
- `site.struct _Continuation`
- `PSVR2SenseDeviceFastPathUserClient`
- `IOUserClientDefaultLockingSetProperties`
- `UV`
- `i16@?0@?<v@?i^{?=b7b1(?=[58C][29C]{?=sssssssssssssssssssssssssssss}{?=sssssssssssss})}{CRCResult=BII}>8`
- `_6`
- `_33`
- `IOHIDGCDevice`
- `12112112`
- `PSVR2DeviceType`
- `VendorID`
- `site.MotionCorrectionDataFetchContext`
- `_25`
- ` (bad CRC)`
- `GameControllerCategory`
- `Transport.ReportInterval`
- `Transport.ReportInterval~Latest`
- `application-identifier`
- `_16`
- `121111121222121211111`
- `IOGCPortNotifier`
- `site.FirmwareInfoDataFetchContext`
- `_38`
- `CountryCode`
- `site.PSVR2SenseDeviceFastPathUserClientHapticsQueue`
- `site.IOGCDynamicDeviceProbe`
- `_12`
- `_18`
- `_32`
- `_37`
- `Power.Disconnect.OnBattery.NotHeldAfterTime`
- `PSVR2SenseDeviceFastPathUserClientInputQueue`
- `site.IOGCCommandQueue`
- `121111121222121211`
- `12222222222222212111`
- `%#0.4x`
- `Built-In`
- `ReportInterval~Latest`
- `site.IOGCPortNotifier`
- `IOGCDynamicDeviceProbeUserClient`
- `IOGCResource`
- `TimeSyncEnabled`
- `ReportInterval~Override`

**[__TEXT.__os_log]**

- `[%#010llx] Could not determine connection type!`
- `[%#010llx] #INPUT Queue Reset failed: %x`
- `[%#010llx] #DENY openHapticsControl(<IOService %#010llx>).  Currently open by other client %#010llx.`
- `[%#010llx] Fetch motion correction data (g: %llu a:%u p:%u) failed: invalid checksum.`
- `[%#010llx] #INPUT Queue Enqueue failed.`
- `[%#010llx] Refresh accessory firmware info completed with status (Attempt 2/2): %#x`
- `[%#010llx] Request Firmware Info failed: %#x`
- `[%#010llx] Apply 'Input' configuration {\n\tInput.NormalizedTriggerDeadzone = ERROR, expected number value!\n}`
- `[%#010llx] Get feature report %#0.2x error: Response is empty. Expected at least %zu bytes.`
- `[%#010llx] #DENY openTrackingControl(<IOService %#010llx>).  Currently open by other client %#010llx.`
- `IOGCCircularDataQueue::initWithEntries failed: size [%zd] too large.`
- `[%#010llx] PSVR2SenseDevice::didTerminate(<IOHIDInterface %#010llx>)`
- `[%#010llx] PSVR2SenseDevice::handleProviderClosed(%llu)`
- `[%#010llx] Get feature report %#0.2x error: Response [%#0.2x] has length %{bytes}zu.  Expected at least %zu bytes.`
- `[%#010llx] Fetch motion correction data (g: %llu a:%u p:%u) failed: %#x`
- `Could not unserialize input arguments!`
- `[%#010llx] PSVR2SenseDeviceFastPathUserClient::start(<PSVR2SenseDevice %#010llx>) for pid %i, %s`
- `[%#010llx] PSVR2SenseDevice::handleStart(<IOHIDInterface %#010llx>)`
- `[%#010llx] PSVR2SenseDevice::handleProviderOpened(%llu)`
- `[%#010llx] ERROR: Refresh accessory motion correction data failed (Attempt 2/2): %#x`
- `[%#010llx] Get feature report %#0.2x: [%#0.2x] | %#0.8x%{public}s (%zu bytes)`
- `[%#010llx] Set feature report %#0.2x failed: %#x`
- `[%#010llx] openHapticsControl(<PSVR2SenseDevice %#010llx>) denied: %x.`
- `[%#010llx] PSVR2SenseDeviceFastPathUserClientHapticsQueue::stop(<IOService %#010llx>)`
- `[%#010llx] Missing motion correction data page %u.`
- `[%#010llx] Received unknown input report: reportID = %#lx`
- `[%#010llx] Set output report %#0.2x failed: %#x`
- `[%#010llx] Get feature report %#0.2x failed: %#x`
- `[%#010llx] Get feature report %#0.2x error: Response has length %{bytes}zu, which is abnormally large.`
- `[%#010llx] Failed to open provider.`
- `[%#010llx] Create control queue (%llx): Not permitted`
- `[%#010llx] [!] Refresh accessory info failed: %#x. The service will not be registered.  Disconnect and reconnect the accessory.`
- `[%#010llx] #POWER Battery low voltage meets BATTERY disconnect criteria.`
- `[%#010llx] Set feature report %#0.2x | %{private}.*P | %{public}.*P%{public}s`
- `[%#010llx] Request Motion Correction Data failed: %#x`
- `[%#010llx] Get feature report %#0.2x #NOTE: Response [%#0.2x] (%zu bytes) has invalid checksum '%#0.8x'; expected '%#0.8x'.`
- `[%#010llx] PSVR2SenseDevice::openHapticsControl(<IOService %#010llx>)`
- `[%#010llx] PSVR2SenseDeviceFastPathUserClientInputQueue::stop(<IOService %#010llx>)`
- `[%#010llx] PSVR2SenseDeviceFastPathUserClientHapticsQueue::start(<IOService %#010llx>)`
- `[%#010llx] Refresh accessory motion correction data completed with status (Attempt 1/2): %#x`
- `[%#010llx] Missing one or more motion correction data pages after %u.`
- `[%#010llx] Fetch accessory firmware info (g: %llu a:%u) failed: %#x`
- `IOGCCircularDataQueue::initWithEntries failed: could not allocate memory (size=%zu).`
- `[%#010llx] PSVR2SenseDeviceFastPathUserClientTrackingQueue::stop(<IOService %#010llx>)`
- `[%#010llx] Registering service with IOKit...`
- `[%#010llx] WARNING: Refresh accessory motion correction data failed (Attempt 1/2): %#x`
- `[%#010llx] Refresh accessory firmware info completed with status (Attempt 1/2): %#x`
- `[%#010llx] Payload for input report [%#x] has length [%{bytes}zu], which is less than the minimum expected length [%{bytes}zu]. Ignoring.`
- `[%#010llx] Input report %#0.2x payload [%#0.2x] (%zu bytes) has invalid checksum '%#0.8x'; expected '%#0.8x'.`
- `[%#010llx] IOGCDynamicDeviceProbe::start(<IOService %#010llx>)`
- `[%#010llx] Missing motion correction data pages.`
- `[%#010llx] Get feature report %#0.2x: [%#0.2x] | (%zu bytes)`
- `[%#010llx] Apply 'Input' configuration {\n\tInput.NormalizedThumbstickDeadzoneRadius = ERROR, expected number value!\n}`
- `[%#010llx] Apply 'Input' configuration {\n\tInput.NormalizedThumbstickAxisSnapRadius = %f\n}`
- `[%#010llx] Apply 'Power' configuration {\n\tPower.Disconnect.OnBattery.NotHeldAfterTime = %u\n}`
- `[%#010llx] openTrackingControl(<PSVR2SenseDevice %#010llx>) denied: %x.`
- `::initWithEntries failed: could not allocate memory.`
- `[%#010llx] Refresh accessory motion correction data completed with status (Attempt 2/2): %#x`
- `[%#010llx] WARNING: Refresh accessory firmware info failed (Attempt 1/2): %#x`
- `[%#010llx] #POWER Notifying clients that 'should disconnect' state changed %#x -> %#x`
- `[%#010llx] Get feature report %#0.2x error: Response [%#0.2x] is too short. Expected at least %zu bytes.`
- `[%#010llx] Fetch motion correction data (g: %llu a:%u p:%u) failed: %#x (will retry)`
- `[%#010llx] IOGCDynamicDeviceProbeUserClient::start(<IOService %#010llx>) for pid %i, %s`
- `[%#010llx] Could not determine device type!`
- `[%#010llx] Get feature report %#0.2x error: Could not map response.`
- `[%#010llx] PSVR2SenseDevice::openTrackingControl(<IOService %#010llx>)`
- `[%#010llx] Apply 'Input' configuration {\n\tInput.NormalizedTriggerDeadzone = %f\n}`
- `[%#010llx] PSVR2SenseDeviceFastPathUserClientInputQueue::start(<IOService %#010llx>)`
- `[%#010llx] PSVR2SenseDeviceFastPathUserClientTrackingQueue::start(<IOService %#010llx>)`
- `[%#010llx] Started PSVR2 %s {\n    isVirtual = %d\n    isProxied = %d\n    transport = %d\n    connection = %d\n    reportInterval = %uus\n}`
- `[%#010llx] Missing some motion correction data pages.`
- `[%#010llx] #POWER 'Controller not held' time meets BATTERY disconnect criteria {\n\t now = %llums\n\t last held in hand update = %llums\n\t should disconnect after = %ums\n}`
- `[%#010llx] Apply 'Power' configuration {\n\tPower.Disconnect.OnBattery.AtLevel = %hhu\n}`
- `IOGCCircularDataQueue::initWithEntries failed: %{mach.errno}d.`
- `[%#010llx] PSVR2SenseDevice::handleStop(<IOHIDInterface %#010llx>)`
- `[%#010llx] ERROR: Refresh accessory firmware info failed (Attempt 2/2): %#x`
- `[%#010llx] Input report %#0.2x payload has length (%zu bytes), which is less than the minimum expected length (%zu bytes). Ignoring.`
- `[%#010llx] Set feature report %#0.2x | %{private}.*P`
- `[%#010llx] PSVR2SenseDevice::closeHapticsControl(<IOService %#010llx>)`
- `[%#010llx] Fetch accessory firmware info  (g: %llu a:%u) failed: invalid checksum`
- `[%#010llx] PSVR2SenseDeviceHIDEventServerUserClient::start(<PSVR2SenseDevice %#010llx>) for pid %i, %s`
- `[%#010llx] Apply 'Input' configuration {\n\tInput.NormalizedThumbstickDeadzoneRadius = %f\n}`
- `[%#010llx] Motion correction data page out of order.`
- `[%#010llx] #POWER Battery level %d meets BATTERY disconnect criteria.`
- `[%#010llx] PSVR2SenseDevice::closeTrackingControl(<IOService %#010llx>)`
- `[%#010llx] Fetch accessory firmware info (g: %llu a:%u) failed: %#x (will retry)`
- `[%#010llx] Apply 'Input' configuration {\n\tInput.NormalizedThumbstickAxisSnapRadius = ERROR, expected number value!\n}`
- `[%#010llx] Apply 'Power' configuration {\n\tPower.Disconnect.OnBattery.AtLowVoltage = %d\n}`
- `IOGCDynamicDeviceProbe::probe(<IOHIDDevice %#010llx>)`

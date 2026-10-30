# `com.apple.iokit.IOHIDFamily`

- Name: IOHIDFamily
- Version: `2.0.0`
- UUID: `23A0066B-F610-342C-8315-1CD23FF821D0`
- Source version: `2360.40.13.0.1`
- Depends on: [`com.apple.driver.AppleMobileFileIntegrity`](com.apple.driver.AppleMobileFileIntegrity.md) 1.0.2, [`com.apple.iokit.CoreAnalyticsFamily`](com.apple.iokit.CoreAnalyticsFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 8.0.0b2, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 8.0.0b2, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 8.0.0b2, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 8.0.0b2, [`com.apple.kpi.private`](com.apple.kpi.private.md) 22.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0.0b2

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (9) [KC]

### HID Game Controller Pointing Driver
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `5`
    - `DeviceUsagePage`: `1`
  -
    - `DeviceUsage`: `4`
    - `DeviceUsagePage`: `1`
- `HIDDefaultBehavior`: ``
- `IOClass`: `IOHIDEventDriver`
- `IOMatchDefer`: `True`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDFamily`
- `IOProviderClass`: `IOHIDInterface`

### IOFastPath Support Merger
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `118`
    - `DeviceUsagePage`: `65280`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDFamily`
- `IOProviderClass`: `IOHIDDevice`
- `IOProviderMergeProperties`:
  - `SupportsIOFastPath`: `True`

### IOHIDBTCETimeSyncService
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDBTCETimeSyncService`
- `IOMatchCategory`: `IOHIDTimeSyncService`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDFamily`
- `IOPropertyMatch`:
  - `HIDTimeSyncProtocol`: `3`
- `IOProviderClass`: `IOHIDDevice`

### IOHIDEventServiceUserClient
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDFamily`
- `IOProviderClass`: `IOHIDEventService`
- `IOProviderMergeProperties`:
  - `HIDServiceSupport`: `True`
  - `IOCFPlugInTypes`:
    - `7DDEECA8-A7B4-11DA-8A0E-0014519758EF`: `IOHIDFamily.kext/PlugIns/IOHIDLib.plugin`
    - `FA12FA38-6F1A-11D4-BA0C-0005028F18D5`: `IOHIDFamily.kext/PlugIns/IOHIDLib.plugin`
  - `IOUserClientClass`: `IOHIDEventServiceUserClient`

### IOHIDLibUserClient
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDFamily`
- `IOProviderClass`: `IOHIDDevice`
- `IOProviderMergeProperties`:
  - `IOCFPlugInTypes`:
    - `40A57A4E-26A0-11D8-9295-000A958A2C78`: `IOHIDFamily.kext/PlugIns/IOHIDLib.plugin`
    - `7DDEECA8-A7B4-11DA-8A0E-0014519758EF`: `IOHIDFamily.kext/PlugIns/IOHIDLib.plugin`
    - `FA12FA38-6F1A-11D4-BA0C-0005028F18D5`: `IOHIDFamily.kext/PlugIns/IOHIDLib.plugin`
  - `IOUserClientClass`: `IOHIDLibUserClient`

### IOHIDResource
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDResource`
- `IOMatchCategory`: `IOHIDResource`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDFamily`
- `IOProviderClass`: `IOResources`
- `IOResourceMatch`: `IOBSD`
- `IOUserClientClass`: `IOHIDResourceDeviceUserClient`

### R1 Merge
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDFamily`
- `IOPropertyMatch`:
  - `PrimaryUsage`: `27`
  - `PrimaryUsagePage`: `65280`
- `IOProviderClass`: `IOHIDDevice`
- `IOProviderMergeProperties`:
  - `ProtectedAccess`: `True`

### ShuttleExpress
- `ButtonMaps`:
  -
    - `ButtonNumber`: `5`
    - `EventType`: `17`
    - `Mask`: `1`
  -
    - `ButtonNumber`: `6`
    - `EventType`: `3`
    - `Usage`: `548`
    - `UsagePage`: `12`
  -
    - `ButtonNumber`: `7`
    - `EventType`: `3`
    - `Usage`: `207`
    - `UsagePage`: `12`
  -
    - `ButtonNumber`: `8`
    - `EventType`: `3`
    - `Usage`: `547`
    - `UsagePage`: `12`
  -
    - `ButtonNumber`: `9`
    - `EventType`: `3`
    - `Usage`: `33`
    - `UsagePage`: `11`
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDEventOverrideDriver`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDFamily`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `32`
- `VendorID`: `2867`

### StarkPorscheWheel
- `ButtonMaps`:
  -
    - `ButtonNumber`: `1`
    - `EventType`: `3`
    - `Usage`: `207`
    - `UsagePage`: `12`
  -
    - `ButtonNumber`: `3`
    - `EventType`: `3`
    - `Usage`: `182`
    - `UsagePage`: `12`
  -
    - `ButtonNumber`: `4`
    - `EventType`: `3`
    - `Usage`: `181`
    - `UsagePage`: `12`
  -
    - `ButtonNumber`: `8`
    - `EventType`: `3`
    - `Usage`: `32`
    - `UsagePage`: `11`
  -
    - `ButtonNumber`: `12`
    - `EventType`: `3`
    - `Usage`: `38`
    - `UsagePage`: `11`
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDEventOverrideDriver`
- `IOPersonalityPublisher`: `com.apple.iokit.IOHIDFamily`
- `IOProviderClass`: `IOHIDInterface`
- `ProductID`: `407`
- `VendorID`: `3767`


## C++ classes (62) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleEmbeddedHIDEventService` | 0xc8 | IOHIDEventService → IOService → IORegistryEntry |
| `AppleEmbeddedKeyboard` | 0x110 | IOHIDEventDriver → IOHIDEventService → IOService → IORegistryEntry |
| `AppleUserHIDDevice` | 0xd8 | IOHIDDevice → IOService → IORegistryEntry |
| `AppleUserHIDEventService` | 0x110 | IOHIDEventDriver → IOHIDEventService → IOService → IORegistryEntry |
| `DigitizerTransducer` | 0x28 | EventElementCollection |
| `EventElementCollection` | 0x20 |  |
| `IOFastPathDescriptor` | 0x20 |  |
| `IOFastPathField` | 0x28 |  |
| `IOFastPathHIDAccelService` | 0xb8 | IOFastPathHIDService → IOFastPathService → IOService → IORegistryEntry |
| `IOFastPathHIDButtonService` | 0xb0 | IOFastPathHIDService → IOFastPathService → IOService → IORegistryEntry |
| `IOFastPathHIDGyroService` | 0xb8 | IOFastPathHIDService → IOFastPathService → IOService → IORegistryEntry |
| `IOFastPathHIDLEDService` | 0x120 | IOFastPathHIDService → IOFastPathService → IOService → IORegistryEntry |
| `IOFastPathHIDService` | 0xb0 | IOFastPathService → IOService → IORegistryEntry |
| `IOFastPathService` | 0xa0 | IOService → IORegistryEntry |
| `IOFastPathUserClient` | 0xe8 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `IOHIDAccelElementProcessor` | 0x70 | IOHIDElementProcessor |
| `IOHIDAsyncReportQueue` | 0x60 | IOEventSource |
| `IOHIDBTCETimeSyncService` | 0xc8 | IOHIDTimeSyncService → IOService → IORegistryEntry |
| `IOHIDButtonElementProcessor` | 0x60 | IOHIDElementProcessor |
| `IOHIDClientData` | 0x28 |  |
| `IOHIDComplexEventDriver` | 0x130 | IOHIDEventService → IOService → IORegistryEntry |
| `IOHIDDevice` | 0xd0 | IOService → IORegistryEntry |
| `IOHIDDeviceElementContainer` | 0x20 | IOHIDElementContainer |
| `IOHIDElement` | 0x20 | OSCollection |
| `IOHIDElementContainer` | 0x18 |  |
| `IOHIDElementPrivate` | 0xe8 | IOHIDElement → OSCollection |
| `IOHIDElementProcessor` | 0x40 |  |
| `IOHIDEvent` | 0x50 |  |
| `IOHIDEventDriver` | 0x108 | IOHIDEventService → IOService → IORegistryEntry |
| `IOHIDEventDummyService` | 0xd0 | IOHIDEventService → IOService → IORegistryEntry |
| `IOHIDEventQueue` | 0x98 | IOSharedDataQueue → IODataQueue |
| `IOHIDEventService` | 0xc8 | IOService → IORegistryEntry |
| `IOHIDEventServiceFastPathUserClient` | 0x138 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `IOHIDEventServiceQueue` | 0x50 | IOSharedDataQueue → IODataQueue |
| `IOHIDEventServiceUserClient` | 0x128 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `IOHIDEventSource` | 0x48 | IOEventSource |
| `IOHIDForceSensorElementProcessor` | 0x48 | IOHIDElementProcessor |
| `IOHIDGyroElementProcessor` | 0x70 | IOHIDElementProcessor |
| `IOHIDInterface` | 0x108 | IOService → IORegistryEntry |
| `IOHIDLEDConstellationElementProcessor` | 0x78 | IOHIDElementProcessor |
| `IOHIDLibUserClient` | 0x1a0 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `IOHIDOOBReportDescriptor` | 0x100 | IOBufferMemoryDescriptor → IOGeneralMemoryDescriptor → IOMemoryDescriptor |
| `IOHIDProviderPropertyMerger` | 0x90 | IOProviderPropertyMerger → IOService → IORegistryEntry |
| `IOHIDProximityElementProcessor` | 0x50 | IOHIDElementProcessor |
| `IOHIDReportElementQueue` | 0xa8 | IOHIDEventQueue → IOSharedDataQueue → IODataQueue |
| `IOHIDResource` | 0x90 | IOService → IORegistryEntry |
| `IOHIDResourceDeviceUserClient` | 0x170 | IOUserClient2022 → IOUserClient → IOService → IORegistryEntry |
| `IOHIDResourceQueue` | 0x40 | IOSharedDataQueue → IODataQueue |
| `IOHIDRootElementProcessor` | 0x48 | IOHIDElementProcessor |
| `IOHIDTestTimeSyncService` | 0x98 | IOHIDTimeSyncService → IOService → IORegistryEntry |
| `IOHIDThumbstickElementProcessor` | 0x58 | IOHIDElementProcessor |
| `IOHIDTimeSyncClientData` | 0x20 |  |
| `IOHIDTimeSyncService` | 0x98 | IOService → IORegistryEntry |
| `IOHIDUserDevice` | 0xe0 | IOHIDDevice → IOService → IORegistryEntry |
| `OSAction_IOHIDDevice__CompleteReport` | 0x20 | OSAction |
| `OSAction_IOHIDEventService__CopyEvent` | 0x20 | OSAction |
| `OSAction_IOHIDEventService__SetLED` | 0x20 | OSAction |
| `OSAction_IOHIDEventService__SetUserProperties` | 0x20 | OSAction |
| `OSValueObject<AsyncCommitParam>` | 0x18 |  |
| `OSValueObject<AsyncReportParam>` | 0x18 |  |
| `OSValueObject<__ReportResult>` | 0x18 |  |
| `TransducerState` | 0x28 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1800)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00008eac off=0x009f6910-0x009ff7bc addr=0xfffffe00079fa910-0xfffffe0007a037bc r--/r--   __TEXT            
	sz=0x000033c6 off=0x009f7078-0x009fa43e addr=0xfffffe00079fb078-0xfffffe00079fe43e               __TEXT.__cstring          (CstringLiterals)
	sz=0x00001090 off=0x009fa440-0x009fb4d0 addr=0xfffffe00079fe440-0xfffffe00079ff4d0               __TEXT.__const            
	sz=0x000042ec off=0x009fb4d0-0x009ff7bc addr=0xfffffe00079ff4d0-0xfffffe0007a037bc               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00079aa0 off=0x0317c3d0-0x031f5e70 addr=0xfffffe000a1803d0-0xfffffe000a1f9e70 r-x/r-x   __TEXT_EXEC       
	sz=0x00078fe0 off=0x0317c3d0-0x031f53b0 addr=0xfffffe000a1803d0-0xfffffe000a1f93b0          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000ac0 off=0x031f53b0-0x031f5e70 addr=0xfffffe000a1f93b0-0xfffffe000a1f9e70          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00001768 off=0x049f1918-0x049f3080 addr=0xfffffe000b9f5918-0xfffffe000b9f7080 rw-/rw-   __DATA            
	sz=0x00000bcc off=0x049f1918-0x049f24e4 addr=0xfffffe000b9f5918-0xfffffe000b9f64e4               __DATA.__data             
	sz=0x00000ae0 off=0x00000000-0x00000ae0 addr=0xfffffe000b9f64e8-0xfffffe000b9f6fc8               __DATA.__common           (Zerofill)
	sz=0x000000b8 off=0x00000000-0x000000b8 addr=0xfffffe000b9f6fc8-0xfffffe000b9f7080               __DATA.__bss              (Zerofill)
003: LC_SEGMENT_64 sz=0x00012728 off=0x01389820-0x0139bf48 addr=0xfffffe000838d820-0xfffffe000839ff48 rw-/rw-   __DATA_CONST      
	sz=0x00000128 off=0x01389820-0x01389948 addr=0xfffffe000838d820-0xfffffe000838d948         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000110 off=0x01389948-0x01389a58 addr=0xfffffe000838d948-0xfffffe000838da58         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x0000f8a0 off=0x01389a58-0x013992f8 addr=0xfffffe000838da58-0xfffffe000839d2f8         __DATA_CONST.__const            
	sz=0x00001ac0 off=0x013992f8-0x0139adb8 addr=0xfffffe000839d2f8-0xfffffe000839edb8         __DATA_CONST.__kalloc_type      
	sz=0x00000ac8 off=0x0139adb8-0x0139b880 addr=0xfffffe000839edb8-0xfffffe000839f880         __DATA_CONST.__assert           
	sz=0x00000560 off=0x0139b880-0x0139bde0 addr=0xfffffe000839f880-0xfffffe000839fde0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000160 off=0x0139bde0-0x0139bf40 addr=0xfffffe000839fde0-0xfffffe000839ff40         __DATA_CONST.__got              (NonLazySymbolPointers)
	sz=0x00000008 off=0x0139bf40-0x0139bf48 addr=0xfffffe000839ff40-0xfffffe000839ff48         __DATA_CONST.__auth_ptr         
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 388 at 0x04af2d5c
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     23A0066B-F610-342C-8315-1CD23FF821D0
008: LC_SOURCE_VERSION           2360.40.13.0.1
009: LC_FUNCTION_STARTS          offset=0x004ac0540 size=0xea0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleExecutable`: `IOHIDFamily`
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `IOHIDFamily`
- `CFBundleNumericVersion`: `33587200`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `2.0.0`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `2.0.0`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `"Copyright © 2000-2018 Apple Inc. All rights reserved. [IOHIDFamily-2360.40.13.0.1]"`
- `OSBundleCompatibleVersion`: `1.0.0b1`
- `OSBundleRequired`: `Root`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/IOHIDFamily.kext`
- `_PrelinkExecutableLoadAddr`: `-2198895351536`
- `_PrelinkExecutableRelativePath`: `IOHIDFamily`
- `_PrelinkExecutableSize`: `616412`
- `_PrelinkExecutableSourceAddr`: `-2198895351536`
- `_PrelinkKmodInfo`: `-2198828263144`

## Strings (943) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `Temperature`
- `HIDDefaultBehavior`
- `entitlements`
- `NMI`
- `AxisCapabilities`
- `site.IOHIDResourceQueue`
- `GetReportTimeoutCount`
- `com.apple.hid.manager.user-access-interface-rematch`
- `OSBoundedPtr.h`
- `UnitExponent`
- `collectionDispatch`
- `site.IOHIDEvent`
- `NotificationForce`
- `OSValueObject<__ReportResult>`
- `Gesture`
- `SupportsGyroEvents`
- `121222111122`
- `IsWrapping`
- `EventType`
- `ChildVendorMessage`
- `MaxFeatureReportSize`
- `_descriptor`
- `IOHIDClientData`
- `Legacy`
- `Orientation`
- `InputReportTime`
- `errcount`
- `%u`
- `site.IOHIDForceSensorElementProcessor`
- `VariableSize`
- `InputReportCount`
- `MaxReportBufferCount`
- `MultipleInterfaceEnabled`
- `IORegistryEntryID`
- `DeviceOpenedByEventSystem`
- `SampleInterval`
- `HasPreferredState`
- `HIDDebug`
- `12111112122212121111111211`
- `copycount`
- `DigitizerCollectionDispatch`
- `PrimaryVendorEvents`
- `UsagePage`
- `VendorIDSource`
- `IOHIDBTCETimeSyncService.cpp`
- `12122211111111`
- `key`
- `_notifier`
- `HIDSupportsScrollAcceleration`
- `GetReportTime`
- `numEntries`
- `site.AsyncCommitContext`
- `matching`
- `HIDKeyboardSupportedModifiers`
- `com.apple.developer.driverkit.family.hid.device`
- `anchorDict`
- `site.IOFastPathHIDLEDService`
- `IOServiceDEXTEntitlements`
- `DeviceModeElement`
- `site.IOHIDEventDummyService`
- `site.AsyncReportEntry`
- `IOName`
- `isApprovedCarPlayDeviceHIDRMDeviceState`
- `site.IOHIDTimeSyncClientData`
- `1211111212221212112112221`
- `ClientOpened`
- `container`
- `_clients`
- `-s`
- `Max`
- `HIDKeyboardSupportsEscKey`
- `site.AppleEmbeddedKeyboard`
- `IOHIDTimeSyncClientData`
- `1211`
- `site.IOHIDTestTimeSyncService`
- `Flags`
- `HIDScrollAccelerationType`
- `CountryCode`
- `site.IOHIDRootElementProcessor`
- `HID: Triggering NMI (Ctrl + Shift + Option + Right Command + Esc)`
- `1211111212221212111111111111111111112221222222`
- `GameControllerFormFitting`
- `SetReportTimeoutCount`
- `ClientOptions`
- `requests`
- `HIDProcessorPropertyKey`
- `IOHIDPointingEventDevice`
- `Height`
- `ret == kIOReturnSuccess`
- `HIDDKStart`
- `status`
- `false`
- `_queue`
- `IsSpatialBluetoothHID`
- `Unknown`
- `hidq_no_full_msg`
- `AppleEmbeddedHIDEventService`
- `ReportRate`
- `11111222222222`
- `CEMachTime`
- `HIDResetPointer`
- `site.TransducerState`
- `site.IOHIDUserDevice`
- `B16@?0^{OSObject=^^?i}8`
- `LEDConstellationElements`
- `CFBundleIdentifier`
- `Virtual`
- `OSAction_IOHIDEventService__SetLED`
- `SerialNumber`
- `LocationID`
- `IOHIDElementProcessor`
- `IOFastPathHIDGyroService`
- `IOHIDUserDeviceDebugState`
- `OutstandingAsyncCount`
- `GameControllerPointer`
- `GetReportFailCount`
- `OSValueObject<AsyncReportParam>`
- `site.struct _notifyMsg`
- `CECount`
- `121`
- `Denied`
- `Bluetooth`
- `event`
- `IOHIDElementContainer`
- `com.apple.hid.inductive.allowlist.reject`
- `site.IOFastPathService`
- `val`
- `com.apple.hid.system.user-access-service`
- `HIDVirtualDevice`
- `AppleUserHIDDevice`
- `IOHIDLibUserClient`
- `1122`
- `site.OSAction_IOHIDDevice__CompleteReport`
- `i8@?0`
- `DigitizerCharacterGestureState`
- `SetReportCnt`
- `ClientSuspended`
- `site.IOHIDDevice`
- `11221111111112111112112`
- `%s:0x%llx open by %s:0x%llx (0x%x)\n`
- `debugSerializer`
- `IOFastPathService`
- `duration <= period`
- `v8@?0`
- `CEOffset`
- `collection`
- `site.IOHIDGyroElementProcessor`
- `2121112`
- `Yes`
- `HIDRelaySupport`
- `*`
- `_sample`
- `QueueSize`
- `The offset of the pointer inside its valid memory range can't be represented using int32_t`
- `CollectionType`
- `ReportCount`
- `site.IOFastPathHIDAccelService`
- `true`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `IOHIDElementProcessor.cpp`
- `ElementCookie`
- `Anchors`
- `121222111`
- `CreatedBuffers`
- `RelayServiceInterfaceActive`
- `IOHIDComplexEventDriver.cpp`
- `site.DigitizerTransducer`
- `12111112122212121121112221`
- `1211122222222222222`
- `tsTimestamp`
- `ReportSize`
- `HIDKeyboardKeysDefined`
- `NotificationCount`
- `buttons`
- `OSValueObject.h`
- `BLETimesyncInfo`
- `site.IOHIDTimeSyncService`
- `1211111212221212112`
- `%4.4x%4.4x%4.4x`
- `StandardType`
- `IOFastPathHIDAccelService`
- `me`
- `MaxFIFOEvents`
- `SupportsGlobeKey`
- `KeyboardEnabledEvent`
- `IOUserClientDefaultLockingSetProperties`
- `121222111111111`
- `_serviceMatchThread`
- `HingeAngle`
- `site.IOHIDEventServiceQueue`
- `1211111212221212111111121111112211`
- `Biometric`
- `IOHIDEventType`
- `ReportAvailableCalls`
- `11111111222222212122222222222222222222222222122`
- `accel`
- `1211111212221212112111222111`
- `ReportLatency`
- `1211111212221212111111111111111111112121112221221221`
- `CEInterval`
- `IOHIDEventServiceUserClient`
- `Elements`
- `ok`
- `12211111111111111112222222222`
- `Unicode`
- `121111121222121211211122211`
- `FastPathMotionEventEntitlement`
- `SupportsLEDConstellation`
- `hidq_size`
- `FastPathHasEntitlement`
- `IOHIDOOBReportDescriptor`
- `ButtonReleaseThreshold`
- `Usage`
- `HIDKeyboardSupportsDoNotDisturbKey`
- `BlessedUsagePairs`
- `PrimaryUsagePage`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `data`
- `IOFastPathFieldType`
- `n`
- `IOPropertyMatch`
- `SupportsIOFastPath`
- `site.IOFastPathHIDButtonService`
- `suspendcount`
- `IOReportLegend`
- `HIDTimeSyncProperties`
- `IOFastPathFieldOffset`
- `childEvents`
- `Attempted to get %s on an element with %d children`
- `site.AppleEmbeddedHIDEventService`
- `UsagePercentHist`
- `ReportAvailableRuns`
- `HID: Power Button NMI`
- `AppleEmbeddedKeyboard`
- `EventQueue`
- `LastDroppedEventTime`
- `Privileged`
- `SupportedKeyboardUsagePairs`
- `Gyro`
- `DeviceUsagePage`
- `opened`
- `IOHIDLibUserClient.cpp`
- `site.AppleUserHIDEventService::AppleUserHIDEventService_IVars`
- `IOHIDEventQueue`
- `IOHIDTestTimeSyncService`
- `TestFactor`
- `tsEvent`
- `LastEventTime`
- `121112111`
- `GetReportCompletedCount`
- `Digitizer`
- `RequestTimeout`
- `B24@?0r^{OSSymbol=^^?ib14b18*{smrq_slink={?=^{smrq_slink}}}}8^{OSObject=^^?i}16`
- `HIDDeviceAccessEntitlement`
- `IOResources`
- `IOFastPathDescriptor`
- `site.AsyncCommitCall`
- `PhysicalMin`
- `GameControllerType`
- `IOUserClientDefaultLocking`
- `fWL->inGate()`
- `site.ExpansionData`
- `BLETimesyncConnectionInterval`
- `site.IOHIDAccelElementProcessor`
- `EnqueueTimestamp`
- `ExtendedData`
- `PhysicalDeviceUniqueID`
- `1`
- `SupportedVendorUsagePairs`
- `site.IOHIDButtonElementProcessor`
- `IOFastPathUserClient`
- `subArray`
- `DeviceTypeHint`
- `IOHIDResource`
- `RelativePointer`
- `IOHIDEventDummyService`
- `_fields`
- `HIDProcessorID`
- `1211112122`
- `121111121222121211111111222111111122`
- `EnqueueEventCount`
- `site.IOHIDEventSource`
- `ReportBufferEntrySize`
- `IOHIDDevice`
- `BluetoothLowEnergy`
- `11221112`
- `_children`
- `ScaledMax`
- `EnqueueFailCount`
- `GameControllerCapabilities`
- `IOHIDReportElementQueue`
- `com.apple.hid.system.fast-path-motion-event-privileged`
- `%d`
- `_workloop`
- `prev`
- `site.AnchorEvent`
- `Size`
- `GetReportCnt`
- `12111112122212121111`
- `HIDCompatibilityInterface`
- `IOFastPathHIDLEDService`
- `11122211`
- `Cookie`
- `12122211211`
- `HID: Triggering NMI`
- `BlessedUsage`
- `IOHIDProviderPropertyMerger`
- `2112`
- `Inductive In-Band`
- `12222`
- `SniffControl`
- `interface`
- `ReportPoolSize`
- `site.IOHIDLEDConstellationElementProcessor`
- `1211111212221212111111121`
- `DroppedEventCount`
- `com.apple.hid.manager.user-access-protected`
- `super::init()`
- `12111112122212121111112`
- `AppleVendorSupported`
- `SupportsButtonEvents`
- `SupportsForceEvents`
- `site.IOFastPathHIDService`
- `IOHIDUserDevice`
- `IOHIDUserDeviceSuspend`
- `12111112`
- `site.OSAction_IOHIDEventService__SetUserProperties`
- `OSValueObject<AsyncCommitParam>`
- `root`
- `IsNonLinear`
- `IOHIDInterface.cpp`
- `12112`
- `SetReportCompletedCount`
- `GestureCharacterStateElement`
- `Manufacturer`
- `IOFastPathUserClient.cpp`
- `121111121222121211111111112222221`
- `Headset`
- `IOHIDProximityElementProcessor`
- `HIDPointerButtonCount`
- `unknown:`
- `com.apple.hid.manager.user-access-custom-queue-size`
- `CoreAnalyticsHub`
- `com.apple.`
- `site.IOHIDElementContainer`
- `site.OSAction_IOHIDEventService__CopyEvent`
- `ProductID`
- `DeviceUsagePairs`
- `site.IOHIDEventQueue`
- `com.apple.developer.driverkit.builtin`
- `IOProviderMergeProperties`
- `IOFastPathService.cpp`
- `child`
- `IsArray`
- `BatchInterval`
- `SensorPropertySupported`
- `site.IOHIDThumbstickElementProcessor`
- `PrimaryVendorUsages`
- `output`
- `RegisterService`
- `first`
- `IOProviderClass`
- `v16@?0i8i12`
- `site.IOHIDResource`
- `OSAction_IOHIDEventService__CopyEvent`
- `com.apple.hid.system.user-access-fast-path`
- `bInterfaceProtocol`
- `IOFastPathHIDService.cpp`
- `LED`
- `openedByClient`
- `121112111111`
- `DeviceUsage`
- `Authenticated`
- `ProductIDMask`
- `HIDEventServiceProperties`
- `IOFastPathFieldKey`
- `ProductIDArray`
- `IOHIDInterface`
- `ReleasedBuffers`
- `site.IOHIDEventService`
- `tail`
- `SetReportDroppedCount`
- `com.apple.developer.driverkit.family.hid.eventservice`
- `IOHIDEventServiceFastPathUserClient`
- `Report %d`
- `BootProtocol`
- `21111121`
- `default`
- `DisplayIntegrated`
- `NoFullMsg`
- `GetReportDroppedCount`
- `OSAction_IOHIDDevice__CompleteReport`
- `site.OSAction_IOHIDEventService__SetLED`
- `KeyboardEnabled`
- `PrimaryVendorMessage`
- `site.IOHIDAsyncReportQueue`
- `site.AsyncReportCall`
- `com.apple.hid.manager.user-access-device`
- `com.apple.iohid`
- `VersionNumber`
- `DuplicateIndex`
- `SetReportErrCnt`
- `IOUserClientCrossEndianCompatible`
- `IOHIDThumbstickElementProcessor`
- `HIDResetKeyboard`
- `site.IOHIDResourceDeviceUserClientAsyncParamBlock`
- `MaxOutputReportSize`
- `site.IOHIDEventServiceFastPathUserClient`
- `11111112`
- `children`
- `third party dext`
- `HIDProcessorPropertyAccess`
- `Width`
- `1211122222`
- `121112222222222222211`
- `DigitizerSurfaceSwitch`
- `VendorID`
- `IOUserClientMessageAppSuspended`
- `site.IOHIDOOBReportDescriptor`
- `Children`
- `IOHIDAccelElementProcessor`
- `12111112122212121111111111111`
- `site.IOHIDReportElementQueue`
- `DeviceOrientation`
- `site.AppleUserHIDDevice`
- `InputReportElements`
- `site.IOHIDComplexEventDriver`
- `Name`
- `IOFastPathHIDService`
- `site.IOHIDResourceDeviceUserClient`
- `12112121212212132213211121212111`
- `IOUserClientClass`
- `HasNullState`
- `IOHIDEventDriver-debug`
- `AbsoluteAxisBoundsRemovalPercentage`
- `CEHorizon`
- `!_timeSync`
- `IOHIDEventDriver`
- `222111211211111221111112222221112122222222222221111111111111111112111211`
- `site.IOFastPathHIDGyroService`
- `site.T`
- `BLETimesyncMachAbsoluteTime`
- `IOHIDElement`
- `ScaledMin`
- `LastEventType`
- `com.apple.developer.hid.virtual.device`
- `Compass`
- `Product`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `12111112122212121111111211111111122222`
- `VendorSpecific`
- `HIDSupportsPointerAcceleration`
- `_timer`
- `HIDDeviceParameters`
- `IOHIDDevice Input Report Errors`
- `%s:0x%llx close by %s:0x%llx (0x%x)\n`
- `Active`
- `121111121222121211111112111111221`
- `Keyboard`
- `Accel`
- `RequiresTCCAuthorization`
- `SupportsAccelEvents`
- `ReportID`
- `site.IOHIDInterface`
- `HandleReportCount`
- `0x%04x%04x`
- `site.AppleUserHIDEventService`
- `touchCancelElement`
- `HIDPointerResolution`
- `111111111111111111111111111111222`
- `site.IOHIDElementPrivateCalibrationData`
- `1211111212221212111111`
- `KeyboardUsageMap`
- `IOHIDAsyncReportQueue`
- `1212221111`
- `IOHIDLEDConstellationElementProcessor`
- `ElementProcessors`
- `KeyboardEnabledByEvent`
- `SupportsInk`
- `121111121222121211111111111111111212122`
- `\"%s\" @%s:%d`
- `IOHIDGyroElementProcessor`
- `site.IOHIDProximityElementProcessor`
- `_device`
- `MultiBit`
- `_gate`
- `ModelNumber`
- `!isParentOf(child)`
- `_processors`
- `com.apple.developer.driverkit.transport.hid`
- `oversized`
- `DebugState`
- `com.apple.hid.manager.user-access-privileged`
- `site.IOHIDClientData`
- `HeartRate`
- `head`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `Transport`
- `GameControllerSupportedHIDDevice`
- `interfaces`
- `HIDKeyboardLayoutValue`
- `IOHIDEventService`
- `site.IOHIDElementProcessor`
- `ReportInterval`
- `com.apple.iohideventsystem.server`
- `1121222111`
- `ButtonPressThreshold`
- `HID: Triggering NMI (Ctrl + Shift + Option + Left Command + Esc)`
- `EventQueueMap`
- `site.IOFastPathField`
- `alt_handler_id`
- `button-nmi_mask`
- `IOHIDResourceDeviceUserClient`
- `111111112`
- `EnqueueErrorCount`
- `PhysicalMax`
- `Scroll`
- `IOUserClientEntitlements`
- `AnchorErrorCount`
- `IOHIDComplexEventDriver`
- `UniformTypeIdentifiers`
- `12111`
- `TCCService`
- `IOFastPathHIDButtonService`
- `MultiAxisPointer`
- `GetReportCount`
- `1221`
- `IsRelative`
- `TransducerState`
- `element`
- `OSAction_IOHIDEventService__SetUserProperties`
- `SensorProperties`
- `MaxInputReportSize`
- `IOHIDDevice.cpp`
- `IOReportLegendPublic`
- `HIDScrollResolution`
- `IOHIDKeyboardEventDevice`
- `USB`
- `IOHIDButtonElementProcessor`
- `IOClass`
- `site.IOFastPathUserClient`
- `site.IOHIDElementPrivate`
- `Type`
- `SupportsHIDInputTopology`
- `IOHIDDeviceElementContainer`
- `IOUserClientDefaultLockingSingleThreadExternalMethod`
- `Stackshot triggered using keycombo`
- `LastReportTime`
- `IOHIDEvent`
- `1211111212221212111111111111121222221`
- `11211111111111`
- `IOHIDTimeSyncService.cpp`
- `IOFastPathFieldSize`
- `_properties`
- `EventElementCollection`
- `site.IOHIDProviderPropertyMerger`
- `121111121222121211`
- `TimeSyncEnabled`
- `IOHIDTimeSyncService`
- `Built-In`
- `GetReportErrCnt`
- `Approving`
- `B24@?0^{IOService=^^?i^{ExpansionData}^{OSDictionary}^{OSDictionary}^{ExpansionData}^{IOService}i^{IOService}[2I]QQ^{IOServicePM}B^vi^{IOInterruptSource}}8^{IONotifier=^^?i}16`
- `str`
- `ReportDescriptor`
- `SetReportFailCount`
- `SetReportTime`
- `SharedMemorySize`
- `IOFastPathField`
- `IOHIDRootElementProcessor`
- `SupportsMultiAxisPointerEvents`
- `site.IOHIDElement`
- `HIDProcessorPropertyValue`
- `entrySize`
- `site.AppleUserHIDDevice::AppleUserHIDDevice_IVars`
- `Allowed`
- `site.IOHIDBTCETimeSyncService`
- `1212`
- `IOKitDebug`
- `DigitizerTransducer`
- `2121212121212122`
- `Unit`
- `HID: Stackshot triggered using keycombo`
- `BlessedUsagePage`
- `site.IOHIDEventServiceUserClient`
- `hidq_force_usage_pair`
- `MaxEnqueueReportSize`
- `IOHIDBTCETimeSyncService`
- `IOHIDDeviceShim`
- `MaxClientTimeoutUS`
- `IOHIDResourceQueue`
- `hid_dtrace_debug`
- `com.apple.hid.manager.user-access-keyboard`
- `12122211`
- `Min`
- `gyro`
- `IOHIDEventSource`
- `SupportedHIDEventMask`
- `SetReportCount`
- `PrimaryUsage`
- `1111111112111`
- `Input Report IDs`
- `HIDRMDeviceState`
- `subevent`
- `site.HIDPreparsedData`
- `AppleUserHIDEventService`
- `BLETimesyncConnectionEventOffset`
- `ValueLocation`
- `leds`
- `IOCFPlugInTypes`
- `Placement`
- `getWorkLoop()->inGate()`
- `IOUserClass`
- `site.IOHIDDeviceElementContainer`
- `site.IOHIDLibUserClient`
- `111111111111`
- `BLETimesyncConnectionEventCount`
- `SupportsProximityEvents`
- `processor`
- `Transducers`
- `site.IOFastPathDescriptor`
- `IOHIDEventServiceQueue`
- `%02x`
- `dict`
- `IOHIDForceSensorElementProcessor`
- `site.EventElementCollection`
- `ReportQueue`
- `ParentCollection`
- `HIDPointerAccelerationType`
- `IOHIDDeviceForceInterfaceRematch`
- `offset <= (elementValues->getLength() - sizeof(IOHIDElementValueHeader))`
- `site.IOHIDEventDriver`
- `SurfaceDimensions`
- `ProtectedAccess`
- `ClientSeized`
- `No`
- `hid-inductive-bypass`
- `interfaceElementArrays`
- `IOHIDElementPrivate`
- `IOHIDEventService.cpp`
- `HID: Triggering NMI (Left Command + Right Command + Delete)`

**[__TEXT.__os_log]**

- `%s:0x%llx doTimeSyncForLocalTimeGated:0x%x\n\n`
- `%s:0x%llx start failed\n\n`
- `%s:0x%llx message: 0x%x from: 0x%llx\n\n`
- `%s:0x%llx Client not permitted\n\n`
- `%s:0x%llx setReport failed: 0x%x\n\n`
- `%s:0x%llx thread_call_allocate_with_options failed\n\n`
- `%s:0x%llx MachTime unexpected type\n\n`
- `%s:0x%llx attach failed\n\n`
- `[%s] unexpected collection type for child:%d\n\n`
- `IOHIDEventServiceFastPathUserClient::open:%x (task resume)\n`
- `%s:0x%llx new user client\n\n`
- `%s:0x%llx Cookie data buffer is smaller than expected. %u expected %u\n\n`
- `[ElementContainer] createElementHierarchy createValueElements (input) failed\n\n`
- `Created OOB report data: %#llx(%d)\n`
- `%s:0x%llx IOSimpleReporter::with failed\n\n`
- `%s:0x%llx failed to create user client: 0x%x\n\n`
- `[ElementContainer] Unable to print descriptor. Descriptor length is invalid.\n\n`
- `%s:0x%llx disposeQueue failed: 0x%x\n\n`
- `%s:0x%llx failed to handle report\n\n`
- `%s:0x%llx kIOHIDTimeSyncPropertiesKey is not a dictionary\n\n`
- `%s:0x%llx initWithTask failed\n\n`
- `[%s] unexpected report size:%d for switch element (button %u)\n\n`
- `No element for cookie %d\n`
- `%s:0x%llx setValid: from %s to %s\n\n`
- `%s:0x%llx Failed to validate all the cookies and data. Expected count changed, validated %zu of %u cookies\n\n`
- `%s:0x%llx Suspicious time-sync anchor: {%u,%u},%llu (prev:{%u,%u},%llu)\n\n`
- `failed : could not create descriptor\n`
- `%s:0x%llx super::start:0x%x\n\n\n`
- `%s:0x%llx Error parsing the blessed usage pair array!\n\n`
- `%s:0x%llx HID EventService not ready (state:0x%x)\n\n`
- `%s:0x%llx IOBufferMemoryDescriptor\n\n`
- `%s:0x%llx Ignore porperty for key %s\n\n`
- `%s:0x%llx suspended:%d\n\n`
- `%s:0x%llx XML serialization failed\n\n`
- `[ElementContainer] createElementHierarchy createValueElements (feature) failed\n\n`
- `%s:0x%llx Un-authenticated game controller device attached\n\n`
- `%s:0x%llx keyboard: %d digitizer: %d gameController: %d multiAxis: %d proximity: %d relative: %d scroll: %d led: %d unicode: %d %dcompass: %d orientation %d %d vendor (child): %d vendor (primary): %d biometric: %d gyro: %d temperature: %d accel: %d heartrate:%d hingeangle: %d\n\n`
- `%s:0x%llx start (state:0x%x)\n\n`
- `%s:0x%llx Async report completion dropped, weird size: %u\n\n`
- `%s:0x%llx destroying interfaces\n\n`
- `[%s] missing fast blink off time element\n\n`
- `%s:0x%llx BMD create\n\n`
- `%s:0x%llx OSUnserializeXML:NULL\n\n`
- `%s:0x%llx properties is not OSDictionary\n\n`
- `%s:0x%llx Waking due to space available in queue\n\n`
- `%s:0x%llx _reporterList creation failed\n\n`
- `%s:0x%llx IOHIDManager: It appears that an application is attempting to locate an invalid device.  A workaround is in currently in place, but will be removed after version 10.2\n\n`
- `[%s] missing Fast Blink Mode element\n\n`
- `%s:0x%llx TimeSync event:%d (precision:%d)\n\n`
- `%s:0x%llx synced %llu remote, %llu local timestamps during session\n\n`
- `[ElementContainer] createElementHierarchy createCollectionElements failed\n\n`
- `%s:0x%llx resourceNotificationGated client not privileged\n\n`
- `%s:0x%llx close (set reports:%d(err:%d), get reports:%d(err:%d))\n\n`
- `[%s] collection has no child elements\n\n`
- `%s:0x%llx Significant amount of temporary report buffers created.\n\n`
- `IOHIDInterface GetElementValues totalSize: %d length: %d\n`
- `0x%llx: IOHIDUserDevice getReport enqueue failed.\n\n`
- `%s:0x%llx handleStart\n\n`
- `%s:0x%llx getElements failed: 0x%x\n\n`
- `%s:0x%llx Horizon unexpected type\n\n`
- `[ElementContainer] Failed to create element hierarchy: 0x%x\n\n`
- `Failed to allocate set for requests that timed out\n`
- `[%s] mode, timestamp elements do not have the same report id (%d/%d)\n\n`
- `[ElementContainer] createElementHierarchy HIDGetCapabilities failed: 0x%x\n\n`
- `%s:0x%llx Error parsing blessed usage pairs!\n\n`
- `result=0x%08x\n`
- `%s:0x%llx postElementValues failed: 0x%x\n\n`
- `%s:0x%llx IOHIDDevice::createReporters failed\n\n`
- `[%s] missing report interval element\n\n`
- `[%s] unexpected logical max:%d for switch element (button %u)\n\n`
- `%s:0x%llx isValidProcessorPropertyRequest: missing key kIOHIDProcessorID\n\n`
- `[ElementContainer] createElementHierarchy createElementValuesMemory failed\n\n`
- `%s:0x%llx time-sync service opened (%llu earlier attempts to time-sync failed)\n\n`
- `%s:0x%llx handleStart: unexpected provider type %s\n\n`
- `%s:0x%llx HIDRM: Built-in device detected, state = Allowed\n\n`
- `%s:0x%llx Failed to create event\n\n`
- `%s:0x%llx IOCircularDataQueueEnqueue:0x%x\n\n`
- `%s:0x%llx AppleUserHIDEventService::Start:0x%x\n\n\n`
- `%s:0x%llx Async commit result dropped: 0x%x\n\n`
- `%s:0x%llx EventCount unexpected type\n\n`
- `[%s] unexpected collection type for mode:%d\n\n`
- `[%s] missing intensity element\n\n`
- `[%s] missing device timestamp element\n\n`
- `%s:0x%llx %llu attempts to time-sync before active\n\n`
- `failed : device is NULL\n`
- `%s:0x%llx createQueue failed: 0x%x\n\n`
- `%s:0x%llx %s is not entitled\n\n`
- `%s:0x%llx asyncActions\n\n\n`
- `%s:0x%llx Blocked reports sleep completed(%#x)\n\n`
- `%s:0x%llx HIDRMDeviceState: %s\n\n`
- `[%s] cannot set release threshold (%f) higher than press (%f)\n\n`
- `[ElementContainer] createElementHierarchy createButtonElements (feature) failed\n\n`
- `%s:0x%llx ignoring anchor with offset %u >= connection interval %u\n\n`
- `%s:0x%llx received out-of-range token: %d\n\n`
- `%s:0x%llx failed to allocate user client\n\n`
- `[%s] unexpected collection type:%d\n\n`
- `IOHIDEventServiceQueue::enqueueEvent - Queue is full! %p\n`
- `%s:0x%llx ProcessReport:0x%x %d %d\n\n`
- `%s:0x%llx start\n\n`
- `%s:0x%llx Could not find element for cookie during validation: %d\n\n`
- `%s:0x%llx Client not opened\n\n`
- `%s:0x%llx start for %s:0x%llx\n\n`
- `event length:%d expected:%ld\n`
- `failed\n`
- `[%s] got no complete (x,y,z,ts) tuples\n\n`
- `%s:0x%llx inactive\n\n`
- `%s:0x%llx Unable to prepare report for setReport.\n\n`
- `0x%llx: IOHIDUserDevice setReport enqueue failed.\n\n`
- `IOHIDEventServiceFastPathUserClient suspended:%d\n`
- `%s:0x%llx getReport failed: 0x%x\n\n`
- `%s:0x%llx failed to stop event delivery\n\n`
- `[%s] x,y inputs do not have the same report id (%d/%d)\n\n`
- `[%s] missing mode selector elements\n\n`
- `%s:0x%llx Message : Seize Device\n\n`
- `%s:0x%llx IOTimerEventSource::timerEventSource failed\n\n`
- `%s:0x%llx handleStart failed\n\n`
- `[%s] subcollection has no child elements\n\n`
- `Failed to load %s, non-Apple HID dexts are not allowed on this system\n`
- `[ElementContainer] createElementHierarchy createReportHandlerElements failed\n\n`
- `%s:0x%llx workLoop\n\n\n`
- `%s:0x%llx handleStop sleeping %d\n\n`
- `[%s] unexpected logical min:%d for button %u\n\n`
- `Could not create large report mapping.\n`
- `%s:0x%llx open\n\n`
- `%s:0x%llx Waking blocked reports due to close\n\n`
- `%s:0x%llx No space for element values. Need: %d Available: %d\n\n`
- `[%s] unexpected logical min:%d for switch element (button %u)\n\n`
- `%s:0x%llx handleStart: failed to create any input processors\n\n`
- `%s:0x%llx No element found for cookie %d\n\n`
- `[%s] unexpected page for child:%d\n\n`
- `%s:0x%llx isValidProcessorPropertyRequest: request has %d keys (expected 3)\n\n`
- `IOHIDEventServiceFastPathUserClient::open missing properties\n`
- `%s:0x%llx Dropping report that was not released by IOKit client\n\n`
- `%s:0x%llx Got time-sync anchor: {%u,%u},%llu\n\n`
- `[%s] missing fast blink on time element\n\n`
- `%s:0x%llx failed to parse elements.\n\n`
- `%s:0x%llx Message : Close Device\n\n`
- `%s:0x%llx failed to get a work loop\n\n`
- `0x%llx: IOHIDUserDevice setReport thread timed out.\n\n`
- `%s:0x%llx Failed to enqueue oversized report.\n\n`
- `%s:0x%llx Interval must be nonzero\n\n`
- `[%s] missing force element\n\n`
- `%s:0x%llx handleStart: failed to get elements from IOHIDInterface\n\n`
- `%s:0x%llx [%s] Entitlements %x privilegedClient : %s\n\n`
- `%s:0x%llx Client does not have entitlement: %s\n\n`
- `%s:0x%llx open: 0x%llx %d\n\n`
- `[%s] missing input element for button %u\n\n`
- `Not enough space in buffer to write report %d < %d\n`
- `IOHIDEventServiceFastPathUserClient::open not ready\n`
- `%s:0x%llx Overflow verifying cookie data buffer %u %u\n\n`
- `%s:0x%llx HandleReport reportLength:%d capacity:%d\n\n\n`
- `%s:0x%llx IOCircularDataQueueCreateWithEntries:0x%x\n\n`
- `setValue failed (%lu):%x\n`
- `%s:0x%llx Insufficient permissions to access device for PID: %d, missing entitlement: %s\n\n`
- `%s:0x%llx %s is requesting a queue size %d (%d, %d) but is not entitled.\n\n`
- `%s:0x%llx Could not find element for cookie: %d\n\n`
- `[%s] unexpected logical max:%d for button %u\n\n`
- `%s:0x%llx Set %s value %d\n\n`
- `%s:0x%llx Cookie data buffer is smaller than expected after revalidation. %u expected %u\n\n`
- `[%s] unexpected physical max:%d for button %u\n\n`
- `Overflow when calculating endBit\n`
- `getDataValue failed (%lu):%x\n`
- `%s:0x%llx failed to open %s:0x%llx\n\n`
- `%s:0x%llx IOCircularDataQueueCopyLatest:0x%x\n\n`
- `%s:0x%llx failed to parse element with usage page 0x%x, id 0x%x\n\n`
- `%s:0x%llx Element value overflow\n\n`
- `[%s] unexpected physical min:%d for button %u\n\n`
- `[%s] unexpected report size:%d for button %u\n\n`
- `%s:0x%llx updateElementValues failed: 0x%x\n\n`
- `%s:0x%llx Device never closed by %s: 0x%llx\n\n`
- `%s:0x%llx %llu attempts to dequeue before first enqueue\n\n`
- `IOCFPlugInTypes property already exists, not overwriting`
- `%s:0x%llx inactive, cannot create user client\n\n`
- `%s:0x%llx serialize\n\n`
- `%s:0x%llx removeElementFromQueue failed: 0x%x\n\n`
- `[%s] missing Off Mode element\n\n`
- `[ElementContainer] Element value capacity %ld\n\n`
- `%s:0x%llx asyncActionsLock\n\n\n`
- `%s:0x%llx Async report result dropped: 0x%x\n\n`
- `[%s] x(%d),y(%d) count mismatch\n\n`
- `[%s] missing x-axis element\n\n`
- `[%s] touch,prox inputs do not have the same report id (%d/%d)\n\n`
- `%s:0x%llx isValidProcessorPropertyRequest: unknown processor:%u\n\n`
- `[ElementContainer] createElementHierarchy createValueElements (output) failed\n\n`
- `Failed to map report, could not copy results of get report.\n`
- `IOHIDEventServiceFastPathUserClient::open already opened\n`
- `%s:0x%llx Wait for space available in queue\n\n`
- `%s:0x%llx message: 0x%x from: 0x%llx %d\n\n`
- `[%s] unexpected element type:%d\n\n`
- `[ElementContainer] createElementHierarchy createButtonElements (output) failed\n\n`
- `%s:0x%llx Large amount of outstanding buffers: %u %u\n\n`
- `%s:0x%llx close: 0x%llx\n\n`
- `%s:0x%llx kIOBLETimesyncInfo is not a dictionary\n\n`
- `_copyEvent: No output data\n`
- `%s:0x%llx generated out-of-range index: %d\n\n`
- `%s:0x%llx Unable to create large report map in user task. Dropping large report.\n\n`
- `%s:0x%llx close by %s:0x%llx\n\n`
- `updateElementValues failed (%lu):%x\n`
- `%s Does not have fast path entitlement\n`
- `%s\n`
- `[%s] missing y-axis element\n\n`
- `[ElementContainer] createElementHierarchy createButtonElements (input) failed\n\n`
- `[ElementContainer] Report ID: %ld input:%ld output:%ld feature:%ld\n\n`
- `%s:0x%llx Horizon (%u) must be at least one interval (%u)\n\n`
- `[%s] unexpected element type for child:%d\n\n`
- `%s:0x%llx createDigitizerTransducerEventForReport generates null event: dispatched input report not present in digitizer collection\n\n`
- `%s:0x%llx failed to open provider\n\n`
- `%s:0x%llx updateElementValues failed:0x%x\n\n`
- `%s:0x%llx open by %s:0x%llx\n\n`
- `[%s] cannot set press threshold (%f) lower than release (%f)\n\n`
- `Overflow calculating readsize\n`
- `%s:0x%llx HIDRM: External device detected, state = Unknown\n\n`
- `%s:0x%llx Invalid digitizer  transducer elements\n\n`
- `%s:0x%llx syncActions\n\n\n`
- `%s:0x%llx invalid object type\n\n`
- `%s:0x%llx HID Device not ready (state:0x%x)\n\n`
- `%s:0x%llx failed to start event delivery: 0x%x\n\n`
- `setDataValue failed (%lu):%x\n`
- `Unable to allocate calibration data\n`
- `HID: Posted stackshot event 0x%08x\n`
- `%s:0x%llx %s is not entitled for IOHIDLibUserClient keyboard access\n\n`
- `%s:0x%llx start failed.\n\n`
- `0x%llx: IOHIDUserDevice getReport thread timed out.\n\n`
- `%s:0x%llx Client is seized\n\n`
- `%s:0x%llx message: 0x%x\n\n`
- `[%s] x(%d),z(%d) count mismatch\n\n`
- `[ElementContainer] Descriptor: %s\n\n`
- `IOHIDEventServiceFastPathUserClient::_copyEvent: %x\n`
- `%s:0x%llx startQueue\n\n`
- `%s:0x%llx has multiple interface support\n\n`
- `0x%llx: parse report descriptor failed: 0x%x\n`
- `%s:0x%llx Service never closed by %s: 0x%llx\n\n`
- `%s:0x%llx Invalid digitizer transducer count\n\n`
- `%s:0x%llx setLEDOutputReport:0x%x\n\n`
- `Invalid report length expected : %d got : %d\n`
- `%s:0x%llx called with an irrationally large output size: %u\n\n`
- `%s:0x%llx EventOffset unexpected type\n\n`
- `[%s] got no complete (x,y,z,ts) input tuples\n\n`
- `%s:0x%llx handleStart: set ElementProcessors property failed\n\n`
- `%s:0x%llx Insufficient permissions to access device for PID: %d\n\n`
- `%s:0x%llx setStateForQueues: 0x%x\n\n`
- `%s:0x%llx Unable to find report descriptor\n\n`
- `[%s] mode, blink on time elements do not have the same report id (%d/%d)\n\n`
- `%s:0x%llx isValidProcessorPropertyRequest: missing key kIOHIDProcessorPropertyKey\n\n`
- `Could not save large report mapping.\n`
- `%s:0x%llx Failed to create attach/start nub.\n\n\n`
- `%s:0x%llx Creating temporary buffer for report data\n\n`
- `%s:0x%llx Ignoring synthetic event for keychord\n\n`
- `%s:0x%llx: failed to open %s:0x%llx\n`
- `%s:0x%llx handleStop src: %d srfc: %d srtc: %d srt: %llu grc: %d grfc: %d grtc: %d grt: %llu irc: %d irt: %llu\n\n`
- `%s:0x%llx %02x/%02x blocked due to lack of privileges\n\n`
- `IOHIDSystem posted stackshot event 0x%08x\n`
- `%s:0x%llx handleStart: super::handleStart failed\n\n`
- `%s:0x%llx handleStart: failed to open provider\n\n`
- `%s:0x%llx IOHIDDevice::Start:0x%x\n\n\n`
- `%s:0x%llx Overflow calculating cookieSize\n\n`
- `[%s] missing touch element\n\n`
- `%s:0x%llx isValidProcessorPropertyRequest: request is not dictionary\n\n`
- `%s:0x%llx open client not privileged\n\n`
- `%s:0x%llx failed to parse report descriptor\n\n`
- `[%s] mode, intensity elements do not have the same report id (%d/%d)\n\n`
- `%s:0x%llx TransducerState overload\n\n`
- `Failed to allocate pending set copy\n`
- `%s:0x%llx OSSerialize\n\n`
- `%s:0x%llx Unable to create large report descriptor. Dropping large report.\n\n`
- `%s:0x%llx creating interfaces\n\n`
- `[%s] bad report id:%d\n\n`
- `%s:0x%llx No report pool\n\n`
- `%s:0x%llx Report too large %d %d\n\n`
- `HID: taking action for debug key mask %x\n`
- `%s:0x%llx Error parsing a blessed usage pair dict!\n\n`
- `%s:0x%llx Missing entitlement to access protected service\n\n`
- `%s:0x%llx Client not Permitted\n\n`
- `%s:0x%llx Waking close thread\n\n`
- `%s:0x%llx Inductive descriptor contains usage: %x and usage page: %x pair outside of allow list\n\n`
- `%s:0x%llx Overflow iterating cookie data buffer %u %u\n\n`
- `%s:0x%llx postElementValues:%#x\n\n`
- `%s:0x%llx isValidProcessorPropertyRequest: missing key kIOHIDProcessorPropertyValue\n\n`
- `[ElementContainer] Unable to print descriptor. Memory allocation failed.\n\n`
- `%s:0x%llx Attempt to do kernel start for device multiple times\n\n`
- `%s:0x%llx stop\n\n`
- `%s:0x%llx createMappingInTask failed\n\n`
- `%s:0x%llx createDescriptor failed\n\n`
- `[%s] x(%d),ts(%d) count mismatch\n\n`
- `%s:0x%llx IOHIDTimeSyncService::open failed\n\n`
- `%s:0x%llx _commandGate\n\n`
- `%s:0x%llx Action aborted %d %d\n\n`
- `IOHIDEventServiceFastPathUserClient::open _owner->openForClient failed\n`
- `%s:0x%llx Woke blocked report thread due to suspended client\n\n`
- `[ElementContainer] Failed to open report descriptor: 0x%x\n\n`
- `%s:0x%llx Unable to prepare temp report for setReport.\n\n`
- `%s:0x%llx CreateAction_CompleteReport:%x\n\n`
- `%s:0x%llx addElementToQueue failed: 0x%x\n\n`
- `%s:0x%llx stopQueue\n\n`
- `%s:0x%llx Interval unexpected type\n\n`
- `[%s] mode, blink off time elements do not have the same report id (%d/%d)\n\n`
- `[ElementContainer] Report count: %ld\n\n`
- `IOHIDReportElementQueue: invalid queue size, too large: %u\n`
- `%s:0x%llx Overflow in queueSize.\n\n`
- `%s:0x%llx Multiple opens from client 0x%llx\n\n`
- `%s:0x%llx super::start failed\n\n`
- `[%s] missing On Mode element\n\n`

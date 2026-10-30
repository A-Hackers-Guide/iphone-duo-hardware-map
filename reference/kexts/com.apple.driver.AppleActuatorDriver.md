# `com.apple.driver.AppleActuatorDriver`

- Name: AppleActuatorDriver
- Version: `1010.4`
- UUID: `B1D516E4-CFC5-3550-8B28-A417BF71B1B9`
- Source version: `10110.4.0.0.0`
- Depends on: [`com.apple.driver.AppleInputDeviceSupport`](com.apple.driver.AppleInputDeviceSupport.md) 1.0, [`com.apple.driver.AppleMultitouchDriver`](com.apple.driver.AppleMultitouchDriver.md) 423, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.iokit.IOReportFamily`](com.apple.iokit.IOReportFamily.md) 1.0, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.0.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 12.0.0, [`com.apple.kpi.unsupported`](com.apple.kpi.unsupported.md) 8.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (0) [KC]


## C++ classes (5) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleActuatorDevice` | 0xd8 | IOService → IORegistryEntry |
| `AppleActuatorDeviceUserClient` | 0x150 | IOUserClient → IOService → IORegistryEntry |
| `AppleActuatorHIDEventDriver` | 0xd8 | IOService → IORegistryEntry |
| `HIDMTQueueEventSource` | 0x68 | IOEventSource |
| `HIDMTQueueEventSourceWorkItem` | 0x40 |  |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1640)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001e1f off=0x0038d670-0x0038f48f addr=0xfffffe0007391670-0xfffffe000739348f r--/r--   __TEXT            
	sz=0x00000068 off=0x0038dd40-0x0038dda8 addr=0xfffffe0007391d40-0xfffffe0007391da8               __TEXT.__const            
	sz=0x000011ca off=0x0038dda8-0x0038ef72 addr=0xfffffe0007391da8-0xfffffe0007392f72               __TEXT.__cstring          (CstringLiterals)
	sz=0x0000051d off=0x0038ef72-0x0038f48f addr=0xfffffe0007392f72-0xfffffe000739348f               __TEXT.__os_log           
001: LC_SEGMENT_64 sz=0x00009a10 off=0x0197d580-0x01986f90 addr=0xfffffe0008981580-0xfffffe000898af90 r-x/r-x   __TEXT_EXEC       
	sz=0x000095a0 off=0x0197d580-0x01986b20 addr=0xfffffe0008981580-0xfffffe000898ab20          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x00000470 off=0x01986b20-0x01986f90 addr=0xfffffe000898ab20-0xfffffe000898af90          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x000001b8 off=0x04932ae0-0x04932c98 addr=0xfffffe000b936ae0-0xfffffe000b936c98 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x04932ae0-0x04932ba8 addr=0xfffffe000b936ae0-0xfffffe000b936ba8               __DATA.__data             
	sz=0x000000f0 off=0x00000000-0x000000f0 addr=0xfffffe000b936ba8-0xfffffe000b936c98               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000020c0 off=0x00fe56f0-0x00fe77b0 addr=0xfffffe0007fe96f0-0xfffffe0007feb7b0 rw-/rw-   __DATA_CONST      
	sz=0x00000028 off=0x00fe56f0-0x00fe5718 addr=0xfffffe0007fe96f0-0xfffffe0007fe9718         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000028 off=0x00fe5718-0x00fe5740 addr=0xfffffe0007fe9718-0xfffffe0007fe9740         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00001880 off=0x00fe5740-0x00fe6fc0 addr=0xfffffe0007fe9740-0xfffffe0007feafc0         __DATA_CONST.__const            
	sz=0x00000380 off=0x00fe6fc0-0x00fe7340 addr=0xfffffe0007feafc0-0xfffffe0007feb340         __DATA_CONST.__kalloc_type      
	sz=0x00000190 off=0x00fe7340-0x00fe74d0 addr=0xfffffe0007feb340-0xfffffe0007feb4d0         __DATA_CONST.__kalloc_var       
	sz=0x00000238 off=0x00fe74d0-0x00fe7708 addr=0xfffffe0007feb4d0-0xfffffe0007feb708         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x000000a8 off=0x00fe7708-0x00fe77b0 addr=0xfffffe0007feb708-0xfffffe0007feb7b0         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 163 at 0x04ad3454
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     B1D516E4-CFC5-3550-8B28-A417BF71B1B9
008: LC_SOURCE_VERSION           10110.4.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004a9a090 size=0x138
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleActuatorDriver`
- `CFBundleGetInfoString`: `Copyright © 2021 Apple Inc. All rights reserved.`
- `CFBundleIdentifier`: `com.apple.driver.AppleActuatorDriver`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleActuatorDriver`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1010.4`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1010.4`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2021 Apple Inc. All rights reserved.`
- `OSBundleCompatibleVersion`: `193.8`
- `OSBundleRequired`: `Console`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleActuatorDriver.kext`
- `_PrelinkExecutableLoadAddr`: `-2198902073744`
- `_PrelinkExecutableRelativePath`: `AppleActuatorDriver`
- `_PrelinkExecutableSize`: `55975`
- `_PrelinkExecutableSourceAddr`: `-2198902073744`
- `_PrelinkKmodInfo`: `-2198829045024`

## Strings (160) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `12`
- `%s::%s IOPMrootDomain sleep notification. Enable FW click control for registry entry ID 0x%08llX\n`
- `%s::%s Called with invalid arugments\n`
- `MT`
- `clientMemoryForType`
- `AppleActuatorHIDEventDriver::getActuatorReport() reportID 0x%02x, length %d`
- `systemPowerChangeHandler`
- `%s::%s Scheduling set host click control on separate thread\n`
- `enqueueLog`
- `simpleGetReport`
- `%s exit\n`
- `HIDMTQueueEventSource`
- `start`
- `InterfaceAvailableOnPowerTreeWake`
- `SPI`
- `%s::%s  Unsupported request %d\n\n`
- `message`
- `AppleActuatorDevice::_scheduleSetHostClickControl() Failed to enqueue host click work item!\n`
- `site.AppleActuatorDeviceUserClient`
- `121111121222121211111111111112222222221112`
- `setHostClickControlRequested`
- `Error: AppleActuatorHIDEventDriver::simpleSetReport() returned 0x%08X for reportID 0x%02X`
- `com.apple.hid.multitouch.user-access`
- `registerUserClient`
- `powerStateWillChangeTo`
- `AppleActuatorHIDEventDriver::willTerminate begin`
- `%s::%s could not get the memory descriptor for the data queue\n\n`
- `setWaveform`
- `AppleActuatorDeviceUserClient`
- `HIDMTQueueEventSourceWorkItem`
- `site.OSObject*`
- `AppleActuatorDevice::init() Failed to create _queueEventSource!\n`
- `AppleActuatorHIDEventDriver::willTerminate end`
- `setPowerState`
- `issueDriverRequest`
- `buildActDevice`
- `LocationID`
- `site.AADUserClientState`
- `site.AADHandlersStruct`
- `Bluetooth`
- `false`
- `AppleActuatorHIDEventDriver::getActuatorReportInfo() reportID 0x%02x`
- `Error: getReport() returned 0x%08X for reportID 0x%02X\n`
- `%s::%s Could not allocate _userClientsState->clients\n`
- `IOUserClientClass`
- `createLogQueue`
- `tpad_output_reports`
- `failed to enable Actuator events\n`
- `resetDevice`
- `111111111111`
- `[0x%llx][%llx][%s::%s]: id:0x%llx %s(%d)`
- `USB`
- `%s::%s Set host click control was already enqueued\n`
- `%s::%s registerUserClient returned error 0x%x\n`
- `%s::%s  Resetting device\n\n`
- `AppleActuatorHIDEventDriver::simpleSetReport() for reportID 0x%02x, length %d`
- `%s enter\n`
- `1`
- `[0x%llx][%llx][%s::%s]: Error: In AppleActuatorDevice::_deviceGetReportWithLookUp, mtReportID %d is invalid.`
- `%s::%s getActuatorReport returned error 0x%x\n`
- `_deviceSetReportWithLookUp`
- `[0x%llx][%llx][%s::%s]: Resetting device`
- `getActuatorReportInfoGated`
- `SupportReportInfo`
- `%s::%s mtReportID 0x%x is invalid\n`
- `%s::%s ERROR: mtReportID 0x%02x has status 0x%02x. Report not valid\n\n`
- `%s::%s setNotifyHandler error 0x%08X\n`
- `%s: %s type 0x%lx\n`
- `site.HIDMTQueueEventSource`
- `UseProviderWorkLoop`
- `%s::%s Unknown power state ordinal: %lu\n`
- `scheduleSetHostClickControl`
- `AppleActuatorHIDEventDriver - output reports disabled via boot-arg.\n`
- `Transport`
- `11211`
- `DummyID`
- `%s::%s invalid type in registerNotificationPort\n\n`
- `121111121222121211121121112`
- `handleInterruptReport`
- `%s::%s _getFeatureReportInfo returned result 0x%x\n`
- `unregisterUserClient`
- `AppleActuatorDevice::_scheduleSetHostClickControl() Failed to create host click work item!\n`
- `%s::%s unknown memory type in clientMemoryForType() 0x%x\n\n`
- `%s::%s Device ready notification for registry entry ID 0x%08llX\n`
- `i8@?0`
- `AppleActuatorHIDEventDriver::enableActuatorEvents(%s)`
- `removeHostClickControlClient`
- `handleInterfaceNotification`
- `%s::%s ordinal %lu\n`
- `%s::%s Entered\n`
- `%s::%s Calling into reserved method, this is unexpected\n`
- `reservedMethod`
- `site.ExpansionData`
- `%s::%s Priority wake notification for registry entry ID 0x%08llX\n`
- `_scheduleSetHostClickControl`
- `AppleActuatorDevice::_setHostClickControl() Failed to set host click control. Error = 0x%08x\n`
- `initWithTask`
- `true`
- `simpleSetReport`
- `registerNotificationPort`
- `AppleActuatorHIDEventDriver`
- `[0x%llx][%llx][%s::%s]: `
- `%s::%s resetDevice returned error 0x%x\n`
- `changeHostClickControl`
- `addHostClickControlClient`
- `site.CallParam`
- `AppleActuatorHIDEventDriver::simpleGetReport() for reportID 0x%02x, length %d`
- `_deviceGetReportWithLookUp`
- `%s::%s Enable host click control for registry entry ID 0x%08llX\n`
- `[0x%llx][%llx][%s::%s]: Unsupported request %d`
- `site.HIDMTQueueEventSourceWorkItem`
- `%s::%s Could not cast our provider into appropriate device class\n`
- `_getFeatureReportInfo`
- `MaxOutputReportSize`
- `DefaultActuatorProperties`
- `12111111`
- `121111121222121211111111212`
- `setReport`
- `_cacheDeviceProperties`
- `%s::%s could not create a driver logging queue\n\n`
- `%s: %s service is terminated\n`
- `1211121111221`
- `%s::%s Transport interface 0x%08llX\n`
- `%s: %s\n`
- `Multitouch Actuator ID`
- `%s::%s NULL notification received\n`
- `AppleActuatorHIDEventDriver::setActuatorReport() reportID 0x%02x, length %d`
- `BuildActDeviceEntry`
- `getReport`
- `IsFake`
- `InterfaceAvailableOnDeviceReadyNotification`
- `AppleActuatorDevice`
- `site.AppleActuatorDevice`
- `Dummy`
- `FIFO`
- `bInterfaceID`
- `ActuatorPreferences`
- `%s::%s registerPowerDriver error 0x%08X\n`
- `stop`
- `setPreferences`
- `site.AppleActuatorHIDEventDriver`
- `AppleActuatorHIDEventDriver - couldn't kick off device builder!`

**[__TEXT.__os_log]**

- `[HID] [%s] [Error] %s::%s [0x%llx] Couldn't attach Actuator handler\n`
- `[HID] [%s] [Error] %s::%s %s is not entitled\n`
- `[HID] [%s] %s::%s entered\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] returned 0x%08X for reportID 0x%02X\n\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Couldn't start Actuator handler\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] returned 0x%08X for reportID 0x%02X\n`
- `[HID] [%s] %s::%s [0x%llx] Successfully started\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] ERROR - Invalid length : Report struct [ID:0x%02x] length [%u] is larger than max buffer size [%zu]\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] ERROR - UNDERRUN: mtReportID 0x%02x has reportLength of %d, attempting to write %d bytes\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] ERROR - OVERRUN: mtReportID 0x%02x has reportLength of %d, attempting to write %d bytes\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] _hidInterface->open failed\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not initialize properties dictionary\n`
- `[HID] [%s] %s::%s [0x%llx] Entered\n`
- `[HID] [%s] [Error] %s::%s failed\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] _getFeatureReportInfo returned error 0x%x\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Ignoring interrupt report id = 0x%08x\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] returned 0x%08X\n`
- `[HID] [%s] [Error] %s::%s [0x%llx] Could not create new MT handler\n`

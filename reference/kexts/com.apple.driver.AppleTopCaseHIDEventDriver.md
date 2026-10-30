# `com.apple.driver.AppleTopCaseHIDEventDriver`

- Name: AppleTopCaseHIDEventDriver
- Version: `1000.22`
- UUID: `A024857C-0C3A-325E-9476-A5D6AD2A7371`
- Source version: `10100.22.0.0.0`
- Depends on: [`com.apple.driver.AppleHIDKeyboard`](com.apple.driver.AppleHIDKeyboard.md) 170.10, [`com.apple.driver.AppleInputDeviceSupport`](com.apple.driver.AppleInputDeviceSupport.md) 1000.1, [`com.apple.driver.AppleMultitouchDriver`](com.apple.driver.AppleMultitouchDriver.md) 237.1, [`com.apple.driver.AppleMultitouchSPI`](com.apple.driver.AppleMultitouchSPI.md) 1.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.4, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 9.6.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.6.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.6.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.6.0, [`com.apple.kpi.private`](com.apple.kpi.private.md) 9.6.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (5) [KC]

### Generic Touch - Apple USB
- `BuildAMDWithMTInit`: `True`
- `CFBundleIdentifier`: `com.apple.driver.AppleTopCaseHIDEventDriver`
- `DefaultMultitouchProperties`: `{}`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `2`
    - `DeviceUsagePage`: `1`
- `IOClass`: `AppleMultitouchHIDService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleTopCaseHIDEventDriver`
- `IOProviderClass`: `IOHIDInterface`
- `ProductIDArray`:
  - `5696`
  - `34305`
  - `621`
  - `788`
  - `789`
- `Transport`: `USB`
- `VendorID`: `1452`

### Magic Keyboard (BT) - AppleDeviceManagementHIDEventService
- `BluetoothDevice`: `True`
- `Built-In`: `False`
- `CFBundleIdentifier`: `com.apple.driver.AppleTopCaseHIDEventDriver`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `11`
    - `DeviceUsagePage`: `65280`
- `HIDServiceSupport`: `True`
- `HasBattery`: `True`
- `IOClass`: `AppleDeviceManagementHIDEventService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleTopCaseHIDEventDriver`
- `IOProviderClass`: `IOHIDInterface`
- `ProductIDArray`:
  - `615`
  - `620`
- `VendorID`: `76`

### Magic Keyboard (BT) - AppleHIDKeyboardEventDriverV2
- `CFBundleIdentifier`: `com.apple.driver.AppleHIDKeyboard`
- `CapsLockDelay`: `75`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `6`
    - `DeviceUsagePage`: `1`
- `DualTransport`: `True`
- `FnKeyboardUsageMap`: `0x00070050,0x0007004a,0x00070052,0x0007004b,0x0007002a,0x0007004c,0x0007004f,0x0007004d,0x00070051,0x0007004e,0x00070028,0x00070058`
- `FnModifierUsage`: `3`
- `FnModifierUsagePage`: `255`
- `IOClass`: `AppleHIDKeyboardEventDriverV2`
- `IOPersonalityPublisher`: `com.apple.driver.AppleTopCaseHIDEventDriver`
- `IOProviderClass`: `IOHIDInterface`
- `NumLockKeyboardUsageMap`: `0x00070029,0x00070029,0x0007002a,0x0007002a,0x0007002b,0x0007002b,0x0007003a,0x0007003a,0x0007003b,0x0007003b,0x0007003c,0x0007003c,0x0007003d,0x0007003d,0x0007003e,0x0007003e,0x0007003f,0x0007003f,0x00070040,0x00070040,0x00070041,0x00070041,0x00070042,0x00070042,0x00070043,0x00070043,0x00070044,0x00070044,0x00070045,0x00070045,0x0007004a,0x0007004a,0x0007004b,0x0007004b,0x0007004c,0x0007004c,0x0007004d,0x0007004d,0x0007004e,0x0007004e,0x0007004f,0x0007004f,0x00070050,0x00070050,0x00070051,0x00070051,0x00070052,0x00070052,0x0007000d,0x00070059,0x0007000e,0x0007005a,0x0007000f,0x0007005b,0x00070018,0x0007005c,0x0007000c,0x0007005d,0x00070012,0x0007005e,0x00070024,0x0007005f,0x00070025,0x00070060,0x00070026,0x00070061,0x00070010,0x00070062,0x00070037,0x00070063,0x00070082,0x00070082,0x000700e0,0x000700e0,0x000700e1,0x000700e1,0x000700e2,0x000700e2,0x000700e3,0x000700e3,0x000700e4,0x000700e4,0x000700e5,0x000700e5,0x000700e6,0x000700e6,0x000700e7,0x000700e7`
- `ProductIDArray`:
  - `615`
  - `620`
- `VendorID`: `76`

### Magic Keyboard (USB) - AppleDeviceManagementHIDEventService
- `BluetoothDevice`: `True`
- `Built-In`: `False`
- `CFBundleIdentifier`: `com.apple.driver.AppleTopCaseHIDEventDriver`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `11`
    - `DeviceUsagePage`: `65280`
- `HIDServiceSupport`: `True`
- `HasBattery`: `True`
- `IOClass`: `AppleDeviceManagementHIDEventService`
- `IOPersonalityPublisher`: `com.apple.driver.AppleTopCaseHIDEventDriver`
- `IOProviderClass`: `IOHIDInterface`
- `ProductIDArray`:
  - `615`
  - `620`
- `VendorID`: `1452`

### Magic Keyboard (USB) - AppleHIDKeyboardEventDriverV2
- `CFBundleIdentifier`: `com.apple.driver.AppleHIDKeyboard`
- `CapsLockDelay`: `75`
- `DeviceUsagePairs`:
  -
    - `DeviceUsage`: `6`
    - `DeviceUsagePage`: `1`
- `DualTransport`: `True`
- `FnKeyboardUsageMap`: `0x00070050,0x0007004a,0x00070052,0x0007004b,0x0007002a,0x0007004c,0x0007004f,0x0007004d,0x00070051,0x0007004e,0x00070028,0x00070058`
- `FnModifierUsage`: `3`
- `FnModifierUsagePage`: `255`
- `IOClass`: `AppleHIDKeyboardEventDriverV2`
- `IOPersonalityPublisher`: `com.apple.driver.AppleTopCaseHIDEventDriver`
- `IOProviderClass`: `IOHIDInterface`
- `NumLockKeyboardUsageMap`: `0x00070029,0x00070029,0x0007002a,0x0007002a,0x0007002b,0x0007002b,0x0007003a,0x0007003a,0x0007003b,0x0007003b,0x0007003c,0x0007003c,0x0007003d,0x0007003d,0x0007003e,0x0007003e,0x0007003f,0x0007003f,0x00070040,0x00070040,0x00070041,0x00070041,0x00070042,0x00070042,0x00070043,0x00070043,0x00070044,0x00070044,0x00070045,0x00070045,0x0007004a,0x0007004a,0x0007004b,0x0007004b,0x0007004c,0x0007004c,0x0007004d,0x0007004d,0x0007004e,0x0007004e,0x0007004f,0x0007004f,0x00070050,0x00070050,0x00070051,0x00070051,0x00070052,0x00070052,0x0007000d,0x00070059,0x0007000e,0x0007005a,0x0007000f,0x0007005b,0x00070018,0x0007005c,0x0007000c,0x0007005d,0x00070012,0x0007005e,0x00070024,0x0007005f,0x00070025,0x00070060,0x00070026,0x00070061,0x00070010,0x00070062,0x00070037,0x00070063,0x00070082,0x00070082,0x000700e0,0x000700e0,0x000700e1,0x000700e1,0x000700e2,0x000700e2,0x000700e3,0x000700e3,0x000700e4,0x000700e4,0x000700e5,0x000700e5,0x000700e6,0x000700e6,0x000700e7,0x000700e7`
- `ProductIDArray`:
  - `615`
  - `620`
- `VendorID`: `1452`


## C++ classes (4) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleDeviceManagementHIDEventService` | 0x190 | IOHIDEventService → IOService → IORegistryEntry |
| `AppleMultitouchInputHIDEventDriver` | 0x190 | AppleMultitouchHIDEventDriverV2 → IOHIDEventDriver → IOHIDEventService → IOService → IORegistryEntry |
| `AppleMultitouchMouseHIDEventDriver` | 0x190 | AppleMultitouchInputHIDEventDriver → AppleMultitouchHIDEventDriverV2 → IOHIDEventDriver → IOHIDEventService → IOService → IORegistryEntry |
| `AppleMultitouchTrackpadHIDEventDriver` | 0x190 | AppleMultitouchInputHIDEventDriver → AppleMultitouchHIDEventDriverV2 → IOHIDEventDriver → IOHIDEventService → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1560)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x0000227f off=0x008967f0-0x00898a6f addr=0xfffffe000789a7f0-0xfffffe000789ca6f r--/r--   __TEXT            
	sz=0x00000a24 off=0x00896e68-0x0089788c addr=0xfffffe000789ae68-0xfffffe000789b88c               __TEXT.__cstring          (CstringLiterals)
	sz=0x00001168 off=0x0089788c-0x008989f4 addr=0xfffffe000789b88c-0xfffffe000789c9f4               __TEXT.__os_log           
	sz=0x0000007b off=0x008989f4-0x00898a6f addr=0xfffffe000789c9f4-0xfffffe000789ca6f               __TEXT.__const            
001: LC_SEGMENT_64 sz=0x00008484 off=0x02a08ac0-0x02a10f44 addr=0xfffffe0009a0cac0-0xfffffe0009a14f44 r-x/r-x   __TEXT_EXEC       
	sz=0x000081e4 off=0x02a08ac0-0x02a10ca4 addr=0xfffffe0009a0cac0-0xfffffe0009a14ca4          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000002a0 off=0x02a10ca4-0x02a10f44 addr=0xfffffe0009a14ca4-0xfffffe0009a14f44          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000178 off=0x049cf438-0x049cf5b0 addr=0xfffffe000b9d3438-0xfffffe000b9d35b0 rw-/rw-   __DATA            
	sz=0x000000c8 off=0x049cf438-0x049cf500 addr=0xfffffe000b9d3438-0xfffffe000b9d3500               __DATA.__data             
	sz=0x000000b0 off=0x00000000-0x000000b0 addr=0xfffffe000b9d3500-0xfffffe000b9d35b0               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000023a8 off=0x0128f388-0x01291730 addr=0xfffffe0008293388-0xfffffe0008295730 rw-/rw-   __DATA_CONST      
	sz=0x00000020 off=0x0128f388-0x0128f3a8 addr=0xfffffe0008293388-0xfffffe00082933a8         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000020 off=0x0128f3a8-0x0128f3c8 addr=0xfffffe00082933a8-0xfffffe00082933c8         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x00002098 off=0x0128f3c8-0x01291460 addr=0xfffffe00082933c8-0xfffffe0008295460         __DATA_CONST.__const            
	sz=0x00000100 off=0x01291460-0x01291560 addr=0xfffffe0008295460-0xfffffe0008295560         __DATA_CONST.__kalloc_type      
	sz=0x00000150 off=0x01291560-0x012916b0 addr=0xfffffe0008295560-0xfffffe00082956b0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000080 off=0x012916b0-0x01291730 addr=0xfffffe00082956b0-0xfffffe0008295730         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 100 at 0x04aea9f0
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     A024857C-0C3A-325E-9476-A5D6AD2A7371
008: LC_SOURCE_VERSION           10100.22.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004ab6568 size=0xe0
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `English`
- `CFBundleExecutable`: `AppleTopCaseHIDEventDriver`
- `CFBundleIdentifier`: `com.apple.driver.AppleTopCaseHIDEventDriver`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `AppleTopCaseHIDEventDriver`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `1000.22`
- `CFBundleSignature`: `????`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `1000.22`
- `DTCompiler`: `com.apple.compilers.llvm.clang.1_0`
- `DTPlatformBuild`: `24B91012`
- `DTPlatformName`: `iphoneos`
- `DTPlatformVersion`: `27.2`
- `DTSDKBuild`: `24B91012`
- `DTSDKName`: `iphoneos27.2.internal`
- `DTXcode`: `2700`
- `DTXcodeBuild`: `27A225b`
- `MinimumOSVersion`: `27.2`
- `NSHumanReadableCopyright`: `Copyright © 2013 Apple Inc. All rights reserved.`
- `OSBundleRequired`: `Console`
- `OSBundleUUID`: `<data 32 chars>`
- `UIDeviceFamily`:
  - `1`
- `_InfoPlistDigest`: `<data 52 chars>`
- `_PrelinkBundlePath`: `/System/Library/Extensions/AppleTopCase.kext/PlugIns/AppleTopCaseHIDEventDriver.kext`
- `_PrelinkExecutableLoadAddr`: `-2198896793616`
- `_PrelinkExecutableRelativePath`: `AppleTopCaseHIDEventDriver`
- `_PrelinkExecutableSize`: `52259`
- `_PrelinkExecutableSourceAddr`: `-2198896793616`
- `_PrelinkKmodInfo`: `-2198828403656`

## Strings (158) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__os_log]**

- `[HID] [%s] %s::%s Resume from sleep thread call is already pending\n`
- `[HID] [%s] %s::%s [0x%llX] Successfully started\n`
- `[HID] [%s] %s::%s Ignoring interrupt report id = 0x%08x, length = %llu\n`
- `[HID] [%s] [Error] %s::%s Report ID 0x%02X payload has invalid size %llu\n`
- `[HID] [%s] [Error] %s::%s getReport result size (%d) does not match BTInfo struct size (%lu)\n`
- `[HID] [%s] %s::%s Getting device color, legacy devices may not support this.\n`
- `[HID] [%s] [Error] %s::%s Failed to allocate _inputReportBuffer\n`
- `[HID] [%s] [Error] %s::%s setNotifyHandler error 0x%08X\n`
- `[HID] [%s] [Error] %s::%s getReport result size (%u) does not match expected size (%lu)\n`
- `[HID] [%s] [Error] %s::%s Received Critical Error: 0x%08x\n`
- `[HID] [%s] [Error] %s::%s Could not get wake reason (reportID = 0x%02x, Return Value = 0x%08x)\n`
- `[HID] [%s] [Error] %s::%s Could not get system power state (reportID = 0x%02x, Return Value = 0x%08x)\n`
- `[HID] [%s] %s::%s Serial number fetched from super: %s\n`
- `[HID] [%s] [Error] %s::%s Failed to prepare _inputReportBuffer\n`
- `[HID] [%s] [Error] %s::%s Failed to allocate _mtPreferences\n`
- `[HID] [%s] [Error] %s::%s NULL notification received\n`
- `[HID] [%s] [Error] %s::%s _resumeFromSleepThread is NULL\n`
- `[HID] [%s] [Error] %s::%s Could not set USB sleep on suspend (reportID = 0x%02x, Return Value = 0x%08x\n`
- `[HID] [%s] [Error] %s::%s Failed to allocate _unleashThread\n`
- `[HID] [%s] %s::%s Priority wake notification for registry ID 0x%08llX\n`
- `[HID] [%s] [Error] %s::%s Failed to get device leash state. Error = 0x%08x\n`
- `[HID] [%s] [Error] %s::%s Failed to set device leash state. Error = 0x%08x\n`
- `[HID] [%s] [Error] %s::%s Input report length (%u bytes) > capacity. Dropping report.\n`
- `[HID] [%s] [Error] %s::%s Could not get battery status (reportID = 0x%02x, Return Value = 0x%08x)\n`
- `[HID] [%s] %s::%s Wake reason: %s\n`
- `[HID] [%s] %s::%s Device Color ID = [%u]\n`
- `[HID] [%s] %s::%s Device power state right before going to AP sleep: 0x%x\n`
- `[HID] [%s] [Error] %s::%s Failed to allocate _mtPrefsLock\n`
- `[HID] [%s] [Error] %s::%s super::handleStart failed\n`
- `[HID] [%s] %s::%s Device ready notification for registry ID 0x%08llX\n`
- `[HID] [%s] [Error] %s::%s Property %s not found\n`
- `[HID] [%s] [Error] %s::%s simpleGetReport for reportID 0x%02x returned 0x%08X\n`
- `[HID] [%s] %s::%s Serial number fetched from parents: %s\n`
- `[HID] [%s] [Error] %s::%s super::init() failed\n`
- `[HID] [%s] [Error] %s::%s Failed to prepare reallocated inputReportBuffer of size %llu\n`
- `[HID] [%s] [Error] %s::%s Received 0x%02X report of incorrect size!\n`
- `[HID] [%s] %s::%s [0x%llX] Entered\n`
- `[HID] [%s] [Error] %s::%s simpleGetReport for reportID 0x%02x returned 0x%08x\n`
- `[HID] [%s] [Error] %s::%s Could not get critical error (reportID = 0x%02x, Return Value = 0x%08x)\n`
- `[HID] [%s] [Error] %s::%s registerPrioritySleepWakeInterest failed\n`
- `[HID] [%s] [Error] %s::%s Failed to set device leash state. Result = 0x%08x\n`
- `[HID] [%s] [Error] %s::%s Input report length (%llu bytes) > capacity. Dropping report.\n`
- `[HID] [%s] %s::%s Serial number fetched from feature report: %s\n`
- `[HID] [%s] %s::%s schedule unleash for registry ID 0x%08llX\n`
- `[HID] [%s] %s::%s Schedule unleash thread call is already pending\n`
- `[HID] [%s] [Error] %s::%s Could not clear button state because AMD is not available!\n`
- `[HID] [%s] [Error] %s::%s failed to get work loop\n`
- `[HID] [%s] [Error] %s::%s reportVersion mismatch: bluetoothInfo->reportVersion = %u, BT_INFO_STRUCT_VERSION = %u\n`
- `[HID] [%s] [Error] %s::%s Could not process wake reason\n`
- `[HID] [%s] [Error] %s::%s Error setting wake reason (reportID = 0x%02x, Return Value = 0x%08x)\n`
- `[HID] [%s] [Error] %s::%s Failed to cast target to AppleDeviceManagementHIDEventService\n`
- `[HID] [%s] [Error] %s::%s Failed to re-allocate inputReportBuffer of size %llu\n`
- `[HID] [%s] %s::%s Transport interface 0x%08llX\n`
- `[HID] [%s] [Error] %s::%s _unleashThread is NULL\n`

**[__TEXT.__cstring]**

- `LastCriticalError`
- `SerialNumber`
- `AudioFW Version`
- `TestFW Version`
- `site.AppleMultitouchTrackpadHIDEventDriver`
- `HSTouchHIDService`
- `scheduleResumeFromSleep`
- `site.AppleDeviceManagementHIDEventService`
- `Bluetooth`
- `%02x-%02x-%02x-%02x-%02x-%02x`
- `getCriticalError`
- `processCriticalError`
- `RadioFW Version`
- `VibeWaveformFW Version`
- `ATC`
- `handleStart`
- `HasBattery`
- `processBatteryState`
- `BD_ADDR`
- `getSTFirmwareVersion`
- `setWakeReason`
- `KeyCalFW Version`
- `handleInterruptReport`
- `getBatteryState`
- `setUSBSleepOnSuspend`
- `AccelCalFW Version`
- `ChargerFW Version`
- `12111112122212121111111211111122111111211121111112`
- `LogPowerStateBeforeSleep`
- `HardwareID`
- `getWakeReason`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `bounded_array_ref: n + m is larger than the size of any bounded_array_ref`
- `handleInterfaceNotification`
- `BatteryStatusFlags`
- `AppleDeviceManagementHIDEventService`
- `AppleUSBVHCIPort`
- `ColorID`
- `BootLoaderFW Version`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `HIDPointerResolution`
- `getBluetoothInfo`
- `processWakeReason`
- `getDeviceColor`
- `getSerialNumber`
- `UnknownFW Version`
- `TrustedAccessoryFW Version`
- `systemPowerChangeHandler`
- `unleashDeviceGated`
- `BatteryPercent`
- `BTFW Version`
- `STFW Version`
- `getHardwareId`
- `WakeReason`
- `OSBoundedPtr.h`
- `false`
- `HostTransportSwitchNotificationType`
- `AppleMultitouchMouseHIDEventDriver`
- `%s (0x%02X)`
- `LowBatteryNotificationPercentage`
- `PoweredOffNotificationType`
- `stop`
- `AccelAlgsFW Version`
- `bounded_array_ref: invalid slice provided, the indices are of bounds for the bounded_array_ref`
- `AppleMultitouchInputHIDEventDriver`
- `MaxInputReportSize`
- `USB`
- `AudioCalFW Version`
- `MTCalFW Version`
- `ForceCalFW Version`
- `site.AppleMultitouchInputHIDEventDriver`
- `site.AppleMultitouchMouseHIDEventDriver`
- `ColorIDMapping`
- `\"%s\" @%s:%d`
- `UnleashUnsupported`
- `true`
- `BatteryLowPowerDisconnectionNotificationType`
- `DeviceAddress`
- `To`
- `resumeFromSleepThreadEnter`
- `init`
- `AppleMultitouchTrackpadHIDEventDriver`
- `BatteryLowNotificationType`
- `12111112122212121111111211111111122111121211111221`
- `start`
- `getDevicePowerState`
- `clearButtonStateForUnleash`
- `CurrentBatteryPercentNotificationType`
- `BluetoothDevice`
- `bounded_array_ref: Can't construct from a size greater than UINT32_MAX`
- `MTFW Version`
- `RadioDiagsFW Version`
- `InterfaceAvailableOnDeviceReadyNotification`
- `enableMultitouchEventsGated`
- `scheduleUnleash`
- `ConnectionNotificationType`
- `Built-In`
- `DisconnectionNotificationType`
- `From`
- `ActCalFW Version`
- `PowerFW Version`
- `UserPreferences`
- `AppleMultitouchInputHIDEventDriver::enableMultitouchEvents(%s)`

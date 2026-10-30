# `com.apple.driver.ApplePencilDriver`

- Name: ApplePencilDriver
- Version: `45.10`
- UUID: `ACF7686A-93C8-3709-8CC5-369C1CE72853`
- Source version: `45.10.0.0.0`
- Depends on: [`com.apple.driver.AppleInputDeviceSupport`](com.apple.driver.AppleInputDeviceSupport.md) 1.0, [`com.apple.iokit.IOHIDFamily`](com.apple.iokit.IOHIDFamily.md) 1.7, [`com.apple.kpi.bsd`](com.apple.kpi.bsd.md) 11.0, [`com.apple.kpi.iokit`](com.apple.kpi.iokit.md) 9.0.0, [`com.apple.kpi.libkern`](com.apple.kpi.libkern.md) 9.0.0, [`com.apple.kpi.mach`](com.apple.kpi.mach.md) 9.0.0

## Device-tree nodes it binds (0) [DT][KC]

None by name match. It matches on a provider class, a property, or is a library.

## IOKit personalities (15) [KC]

### Apple Pencil DM IOService (wired)
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `HIDServiceSupport`: `False`
- `IOClass`: `IOHIDEventDummyService`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryUsage`: `11`
- `PrimaryUsagePage`: `65280`
- `ProductIDArray`:
  - `786`
  - `1057`
- `VendorID`: `1452`

### Apple Pencil DM IOService (wireless)
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `HIDServiceSupport`: `False`
- `IOClass`: `IOHIDEventDummyService`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryUsage`: `11`
- `PrimaryUsagePage`: `65280`
- `ProductIDArray`:
  - `546`
  - `332`
  - `482`
  - `1106`
- `VendorID`: `76`

### Apple Pencil DM Property Merger (Pencil 1 wired)
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProbeScore`: `1000`
- `IOPropertyMatch`:
  - `PrimaryUsage`: `11`
  - `PrimaryUsagePage`: `65280`
  - `ProductID`: `786`
  - `VendorID`: `1452`
- `IOProviderClass`: `IOHIDDevice`
- `IOProviderMergeProperties`:
  - `HIDServiceSupport`: `True`

### Apple Pencil DM Property Merger (Pencil 1 wireless)
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProbeScore`: `1000`
- `IOPropertyMatch`:
  - `PrimaryUsage`: `11`
  - `PrimaryUsagePage`: `65280`
  - `ProductID`: `546`
  - `VendorID`: `76`
- `IOProviderClass`: `IOHIDDevice`
- `IOProviderMergeProperties`:
  - `HIDServiceSupport`: `True`

### Apple Pencil DM Property Merger (Pencil 2 wireless)
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProbeScore`: `1000`
- `IOPropertyMatch`:
  - `PrimaryUsage`: `11`
  - `PrimaryUsagePage`: `65280`
  - `ProductID`: `332`
  - `VendorID`: `76`
- `IOProviderClass`: `IOHIDDevice`
- `IOProviderMergeProperties`:
  - `HIDServiceSupport`: `True`

### Apple Pencil DM Property Merger (Pencil 2.5 wired)
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProbeScore`: `1000`
- `IOPropertyMatch`:
  - `PrimaryUsage`: `11`
  - `PrimaryUsagePage`: `65280`
  - `ProductID`: `1057`
  - `VendorID`: `1452`
- `IOProviderClass`: `IOHIDDevice`
- `IOProviderMergeProperties`:
  - `HIDServiceSupport`: `True`

### Apple Pencil DM Property Merger (Pencil 2.5 wireless)
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProbeScore`: `1000`
- `IOPropertyMatch`:
  - `PrimaryUsage`: `11`
  - `PrimaryUsagePage`: `65280`
  - `ProductID`: `482`
  - `VendorID`: `76`
- `IOProviderClass`: `IOHIDDevice`
- `IOProviderMergeProperties`:
  - `HIDServiceSupport`: `True`

### Apple Pencil DM Property Merger (Pencil 3 wireless)
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProbeScore`: `1000`
- `IOPropertyMatch`:
  - `PrimaryUsage`: `11`
  - `PrimaryUsagePage`: `65280`
  - `ProductID`: `1106`
  - `VendorID`: `76`
- `IOProviderClass`: `IOHIDDevice`
- `IOProviderMergeProperties`:
  - `HIDServiceSupport`: `True`

### Apple Pencil Haptics Property Merger
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProbeScore`: `1000`
- `IOPropertyMatch`:
  - `PrimaryUsage`: `4101`
  - `PrimaryUsagePage`: `65376`
  - `ProductID`: `1106`
  - `VendorID`: `76`
- `IOProviderClass`: `IOHIDDevice`
- `IOProviderMergeProperties`:
  - `HIDServiceSupport`: `True`

### Apple Pencil Haptics Property Merger (old usage)
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProbeScore`: `1000`
- `IOPropertyMatch`:
  - `PrimaryUsage`: `1`
  - `PrimaryUsagePage`: `65326`
  - `ProductID`: `1106`
  - `VendorID`: `76`
- `IOProviderClass`: `IOHIDDevice`
- `IOProviderMergeProperties`:
  - `HIDServiceSupport`: `True`

### Apple Pencil Motion IOService
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `HIDServiceSupport`: `False`
- `IOClass`: `IOHIDEventDummyService`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProbeScore`: `1000`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryUsage`: `51`
- `PrimaryUsagePage`: `65280`
- `ProductIDArray`:
  - `1106`
- `VendorID`: `76`

### Apple Pencil Motion Property Merger (Pencil 3)
- `CFBundleIdentifier`: `com.apple.iokit.IOHIDFamily`
- `IOClass`: `IOHIDProviderPropertyMerger`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProbeScore`: `1000`
- `IOPropertyMatch`:
  - `PrimaryUsage`: `51`
  - `PrimaryUsagePage`: `65280`
  - `ProductID`: `1106`
  - `VendorID`: `76`
- `IOProviderClass`: `IOHIDDevice`
- `IOProviderMergeProperties`:
  - `HIDServiceSupport`: `True`

### AppleEmbeddedBluetoothForce
- `CFBundleIdentifier`: `com.apple.driver.ApplePencilDriver`
- `IOClass`: `AppleEmbeddedBluetoothForce`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryUsage`: `17`
- `PrimaryUsagePage`: `65280`
- `ProductIDArray`:
  - `546`
  - `332`
  - `482`
  - `1106`
- `VendorID`: `76`

### AppleEmbeddedBluetoothHaptics
- `CFBundleIdentifier`: `com.apple.driver.ApplePencilDriver`
- `IOClass`: `AppleEmbeddedBluetoothHaptics`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryUsage`: `4101`
- `PrimaryUsagePage`: `65376`
- `ProductIDArray`:
  - `1106`
- `VendorID`: `76`

### AppleEmbeddedBluetoothHaptics (old usage)
- `CFBundleIdentifier`: `com.apple.driver.ApplePencilDriver`
- `IOClass`: `AppleEmbeddedBluetoothHaptics`
- `IOPersonalityPublisher`: `com.apple.driver.ApplePencilDriver`
- `IOProviderClass`: `IOHIDInterface`
- `PrimaryUsage`: `1`
- `PrimaryUsagePage`: `65326`
- `ProductIDArray`:
  - `1106`
- `VendorID`: `76`


## C++ classes (3) [KC]

Object size and full superclass chain, from the OSMetaClass registrations (`ipsw kernel cpp`).

| Class | Size | Superclasses |
|---|---|---|
| `AppleEmbeddedBluetooth` | 0xf8 | IOHIDEventService → IOService → IORegistryEntry |
| `AppleEmbeddedBluetoothForce` | 0x100 | AppleEmbeddedBluetooth → IOHIDEventService → IOService → IORegistryEntry |
| `AppleEmbeddedBluetoothHaptics` | 0xf8 | AppleEmbeddedBluetooth → IOHIDEventService → IOService → IORegistryEntry |

## Mach-O layout [KC]

```
Magic         = 64-bit MachO
Type          = KEXT_BUNDLE
CPU           = AARCH64, 0xc caps: KER00
Commands      = 10 (Size: 1480)
Flags         = NoUndefs, DyldLink, TwoLevel, DylibInCache
000: LC_SEGMENT_64 sz=0x00001383 off=0x006b3b20-0x006b4ea3 addr=0xfffffe00076b7b20-0xfffffe00076b8ea3 r--/r--   __TEXT            
	sz=0x00000050 off=0x006b4148-0x006b4198 addr=0xfffffe00076b8148-0xfffffe00076b8198               __TEXT.__const            
	sz=0x00000d0b off=0x006b4198-0x006b4ea3 addr=0xfffffe00076b8198-0xfffffe00076b8ea3               __TEXT.__cstring          (CstringLiterals)
001: LC_SEGMENT_64 sz=0x00004354 off=0x023bebb0-0x023c2f04 addr=0xfffffe00093c2bb0-0xfffffe00093c6f04 r-x/r-x   __TEXT_EXEC       
	sz=0x000041b4 off=0x023bebb0-0x023c2d64 addr=0xfffffe00093c2bb0-0xfffffe00093c6d64          __TEXT_EXEC.__text            PureInstructions|SomeInstructions 
	sz=0x000001a0 off=0x023c2d64-0x023c2f04 addr=0xfffffe00093c6d64-0xfffffe00093c6f04          __TEXT_EXEC.__auth_stubs      PureInstructions|SomeInstructions (SymbolStubs)
002: LC_SEGMENT_64 sz=0x00000150 off=0x049849d8-0x04984b28 addr=0xfffffe000b9889d8-0xfffffe000b988b28 rw-/rw-   __DATA            
	sz=0x000000c4 off=0x049849d8-0x04984a9c addr=0xfffffe000b9889d8-0xfffffe000b988a9c               __DATA.__data             
	sz=0x00000088 off=0x00000000-0x00000088 addr=0xfffffe000b988aa0-0xfffffe000b988b28               __DATA.__common           (Zerofill)
003: LC_SEGMENT_64 sz=0x000018f0 off=0x0119e230-0x0119fb20 addr=0xfffffe00081a2230-0xfffffe00081a3b20 rw-/rw-   __DATA_CONST      
	sz=0x00000018 off=0x0119e230-0x0119e248 addr=0xfffffe00081a2230-0xfffffe00081a2248         __DATA_CONST.__mod_init_func    (ModInitFuncPointers)
	sz=0x00000018 off=0x0119e248-0x0119e260 addr=0xfffffe00081a2248-0xfffffe00081a2260         __DATA_CONST.__mod_term_func    (ModTermFuncPointers)
	sz=0x000016d0 off=0x0119e260-0x0119f930 addr=0xfffffe00081a2260-0xfffffe00081a3930         __DATA_CONST.__const            
	sz=0x000000c0 off=0x0119f930-0x0119f9f0 addr=0xfffffe00081a3930-0xfffffe00081a39f0         __DATA_CONST.__kalloc_type      
	sz=0x000000d0 off=0x0119f9f0-0x0119fac0 addr=0xfffffe00081a39f0-0xfffffe00081a3ac0         __DATA_CONST.__auth_got         (NonLazySymbolPointers)
	sz=0x00000060 off=0x0119fac0-0x0119fb20 addr=0xfffffe00081a3ac0-0xfffffe00081a3b20         __DATA_CONST.__got              (NonLazySymbolPointers)
004: LC_SEGMENT_64 sz=0x00074e21 off=0x04a8c000-0x04b00e21 addr=0xfffffe000ba90000-0xfffffe000bb04e21 r--/r--   __LINKEDIT        
005: LC_SYMTAB                   Symbol offset=0x04A8C000, Num Syms: 0, String offset=0x04B00E20-0x04B00E21
006: LC_DYSYMTAB                 
	             Local Syms: 0 at 0
	          External Syms: 0 at 0
	         Undefined Syms: 0 at 0
	                    TOC: No
	                 Modtab: No
	External symtab Entries: None
	Indirect symtab Entries: 64 at 0x04ae2630
	 External Reloc Entries: None
	    Local Reloc Entries: None
007: LC_UUID                     ACF7686A-93C8-3709-8CC5-369C1CE72853
008: LC_SOURCE_VERSION           45.10.0.0.0
009: LC_FUNCTION_STARTS          offset=0x004aad020 size=0x88
```

## Info.plist keys [KC]

- `BuildMachineOSBuild`: `23A344017`
- `CFBundleDevelopmentRegion`: `en`
- `CFBundleExecutable`: `ApplePencilDriver`
- `CFBundleIdentifier`: `com.apple.driver.ApplePencilDriver`
- `CFBundleInfoDictionaryVersion`: `6.0`
- `CFBundleName`: `ApplePencilDriver`
- `CFBundleNumericVersion`: `0`
- `CFBundlePackageType`: `KEXT`
- `CFBundleShortVersionString`: `45.10`
- `CFBundleSupportedPlatforms`:
  - `iPhoneOS`
- `CFBundleVersion`: `45.10`
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
- `_PrelinkBundlePath`: `/System/Library/Extensions/ApplePencilDriver.kext`
- `_PrelinkExecutableLoadAddr`: `-2198898771168`
- `_PrelinkExecutableRelativePath`: `ApplePencilDriver`
- `_PrelinkExecutableSize`: `28951`
- `_PrelinkExecutableSourceAddr`: `-2198898771168`
- `_PrelinkKmodInfo`: `-2198828709416`

## Strings (84) [KC]

C strings and os_log formats from the kext, in section order. They name registers, states, errors and the protocol the kext speaks to its hardware.

**[__TEXT.__cstring]**

- `12111112122212121111111211121111`
- `%s::%s: [Error] Couldn't acquire command gate lock`
- `%s::%s: [Error] Failed to get report to 0x%02X length %u, type %u with error code 0x%02X\n`
- `FireflyDescriptor`
- `%s::%s: Sending stim config`
- `recordReportData`
- `bounded_ptr<T>::operator+=(n): Adding the specified number of bytes to the offset representing the current position would overflow.`
- `AppleEmbeddedBluetoothHaptics`
- `%s::%s: [Error] Interface open failed\n`
- `getReportGated`
- `newUserClientGated`
- `%s::%s: [Error] super start failed\n`
- `%s::%s: Sending scan plan V1`
- `bounded_ptr<T>::operator*: Dereferencing this pointer would access memory outside of the bounds set originally`
- `%s::%s: System haptics are disabled globally. Dropping request\n`
- `AppleEmbeddedBluetooth`
- `%s::%s: [Error] Failed to read bytes\n`
- `%s::%s: Received pencil FSM state message`
- `sendFireflyMessage`
- `%s::%s: [Error] Data length exceeds %d maximum\n`
- `kBTFirmwareRevisionKey`
- `FireflyMessage`
- `%s::%s: Sending sync mode`
- `HapticsMessage`
- `HapticsDisabled`
- `site.AppleEmbeddedBluetoothForce`
- `%s::%s: [Error] Failed to create command gate\n`
- `%s::%s: [Error] Inactive device\n`
- `sendStimSettingV2`
- `%s::%s: [Error] Failed to resend descriptor because no data is found for key <%s>`
- `bounded_ptr<T>::discard_bounds: Discarding the bounds on this pointer would lose the fact that it is outside of the bounds set originally`
- `site.AppleEmbeddedBluetoothHaptics`
- `%s::%s: [Error] Unknown haptics message contents\n`
- `%s::%s: [Error] Failed to set report with length %u, type %u to 0x%02X with error code 0x%02X\n`
- `%s::%s: [Error] Couldn't allocate data to store firefly descriptor`
- `%s::%s: Sending stim mode`
- `ScanPlanReportData_0000_0000`
- `\"%s\" @%s:%d`
- `%s::%s: [Error] Could not retrieve event system properties\n`
- `%s::%s: [Error] Firefly message type (%u) unknown`
- `ResendDescriptor`
- `i8@?0`
- `StimConfigReportData`
- `%s::%s: Sending stim setting V1`
- `ScanPlanReportData`
- `%s::%s: Sending scan plan V2 (endpoint 0x%X, scan plan ID 0x%X)`
- `%s::%s: [Error] Failed to create logger\n`
- `%s::%s: Sending host ready`
- `This bounded_ptr is pointing to memory outside of what can be represented by a native pointer.`
- `AppleEmbeddedBluetoothForce`
- `%s::%s: [Error] No HID interface\n`
- `%s::%s: [Error] Coulnd't get firefly descriptor report: %08X`
- `%s::%s: [Error] Cannot allocate reportData (%u bytes) for %s`
- `%s::%s: [Error] Failed to add command gate to event source\n`
- `setReportGated`
- `%s::%s: [Error] Couldn't allocate thread_call to retrieve firefly descriptor`
- `%s::%s: Sending host state`
- `resendDescriptor`
- `OSBoundedPtr.h`
- `HapticsConfig`
- `start`
- `retrieveFireflyDescriptor_block_invoke`
- `%s::%s: Sending type state`
- `ScanPlanReportData_%04X_%04X`
- `%s::%s: reportID: 0x%X (%d bytes)\n`
- `handleInterruptReport`
- `%s::%s: [Error] No data in this report\n`
- `%s::%s: Ignoring firefly descriptor received as an input report`
- `site.AppleEmbeddedBluetooth`
- `1211111212221212111111121112111`
- `interruptReport`
- `setProperties`
- `%s::%s: [Error] Interface cast failed\n`
- `%s::%s: [Error] No control buffer\n`
- `StimSettingReportData`
- `HIDEventServiceProperties`
- `%s::%s: [Error] Buffer or report is empty\n`
- `%s::%s: [Error] HID device cast failed\n`
- `kBTHardwareRevisionKey`
- `%s::%s: Sending stim setting V2 (endpoint 0x%X, scan plan ID 0x%X)`
- `isHapticsDisabled`
- `%s::%s: [Error] Coulnd't store firefly descriptor in registry`
- `sendScanPlanV2`
- `The range of valid memory is too large to be represented by this type, or [begin, end) is not a well-formed range`

# `/System/Library/PrivateFrameworks/HIDDisplay.framework/HIDDisplay`

iOS 27.2 dyld shared cache image. Version `2360.40.13.0.1`. **[DSC]**

## Linked libraries (6)

- `/System/Library/PrivateFrameworks/HID.framework/HID`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 6 classes, 0 protocols, 63 methods, 8 properties

### Class pages

Every class and protocol, with its methods: [`HIDDisplayDeviceManagementInterface`](../objc/HIDDisplayDeviceManagementInterface_HIDDisplay.md), [`HIDDisplayIOReportingInterface`](../objc/HIDDisplayIOReportingInterface_HIDDisplay.md), [`HIDDisplayInterface`](../objc/HIDDisplayInterface_HIDDisplay.md), [`HIDDisplayPresetData`](../objc/HIDDisplayPresetData_HIDDisplay.md), [`HIDDisplayPresetInterface`](../objc/HIDDisplayPresetInterface_HIDDisplay.md), [`HIDDisplayUserAdjustmentInterface`](../objc/HIDDisplayUserAdjustmentInterface_HIDDisplay.md)

### Classes

`HIDDisplayDeviceManagementInterface`, `HIDDisplayIOReportingInterface`, `HIDDisplayInterface`, `HIDDisplayPresetData`, `HIDDisplayPresetInterface`, `HIDDisplayUserAdjustmentInterface`

### Properties

```
@property (T@"NSString",R,V_containerID) containerID;
@property (TQ,R,V_registryID) registryID;
@property (T@"NSArray",R) capabilities;
@property (TB,R) valid;
@property (TB,R) writable;
@property (T@"NSData",R) uniqueID;
@property (T@"NSArray",R,V_presets) presets;
@property (TB,R) valid;
```

## Strings (101)

```
Success
v16@?0@\"HIDElement\"8
Invalid Unique ID Data
Invalid User Adjsutment Information
kUSBContainerID
Invalid Block One Data
Failure
DeviceUsage
Invalid Argument
v8@?0
PresetWritable
PresetName
-[HIDDisplayInterface initWithMatching:]
IOService
Preset is not valid.
 com.apple.iohid 
UserAdjustmentInformation
PresetValid
PresetDataBlockOne
PresetDataBlockTwo
[regID:0x%llx][containerID:%@][instance:%p]
Undefined
HIDDisplay
PresetDataBlockOneLength
PresetDataBlockTwoLength
Invalid object
i
UsagePage
Invalid Block Two Data
UserAdjustmentDescription
PresetDescription
Invalid index
DeviceUsagePairs
DeviceUsagePage
Preset index out of range.
Invalid argument
PresetUniqueID
v32@?0@8@16^B24
Failed to create HIDDisplayDeviceManagementInterface for %@
%@ getActivePresetIndex no associated element
Invalid Unique ID Data %@ Cancel Device Transaction
Invalid / Empty user adjustment description %@
%@ Dealloc
Failed to setup HIDDisplayDeviceManagementInterface for %@
Skip Device Transaction due to previous issues
Invalid HIDDisplayInterfaceRef
%@ set preset for index %ld data %{public}@
%@ Failed to update elements
Invalid preset index %ld 
%s
%@ Container ID Match for %@ returned %s
%@ getCurrentPresetIndex no associated element
Invalid / Empty Name Data %@
%@ setActivePresetIndex on invalid  preset index : %ld
%@ setActivePresetIndex no associated element
%@ get preset for index %ld returned data %{public}@
%@ set preset for index %ld key : %@ value : %@
%@ getFactoryDefaultPresetIndex no associated element
Invalid Data Block Two Data %@
%@ Preset data uniqueID no associated element
%@ valid no associated element
%@ set adjustment %@
%@ HIDDisplayCopyPreset error %@ for  preset index %ld 
%@ Init
%@ Display Device Element UP: 0x%lx , U: 0x%lx 
Invalid Block One Data %@ Cancel Device Transaction
Failed to setup HIDDisplayUserAdjustmentInterface for %@
%@ HIDDisplayGetFactoryDefaultPresetIndex error %@ 
%@ HIDDisplaySetActivePresetIndex error %@ for  preset index %ld 
%@ setCurrentPresetIndex no associated element
%@ Failed set preset index %ld
Invalid UUID Data %@
Invalid Description %@ , Converting it to 2 byte null value
%@ no matching element to set 
%@ invalidate user adjustement
Invalid HIDDisplayPresetInterfaceRef
%@ HIDDisplaySetPreset error %@ for  preset index %ld 
%@ factoryResetElement no associated element factoryReset : %@ securityToken : %@
Failed to create HIDDisplayUserAdjustmentInterface for %d
%@ Invalid preset index %ld 
%@ getSecurityToken no associated element
%@ Preset data writable no associated element
%@ Failed to update elements for preset index %ld
%@ failed to extract valid element value with error %@
%@ Failed Get HID Elements values with error %@
Failed to create HIDDisplayDeviceManagementInterface for %d
%@ setActivePresetIndex on preset index : %ld
Invalid Data Block One Data %@
Invalid Name %@ , Converting it to 2 byte null value
Failed to create HIDDisplayUserAdjustmentInterface for %@
%@ HIDDisplayGetActivePresetIndex error %@ 
Failed to setup HIDDisplayDeviceManagementInterface for %d
%@ get user adjustment returned data %{public}@
%@ Failed Set HID Elements values with error %@
%@ factoryReset type %d
Invalid / Empty Description Data %@
Failed to get valid hid device for %@
%@ Preset data valid no associated element
Failed to setup HIDDisplayUserAdjustmentInterface for %d
Invalid User Adjsutment Information %@ Cancel Device Transaction
Invalid user adjustment information %@
```

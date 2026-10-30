# `CTQuickSwitchCircleDeviceInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 1 instance variables, 8 properties, 14 instance methods, 2 class methods

## Instance variables

```
{QuickSwitchCircleDeviceInfo="deviceId"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"serialNumber"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}"lastSeenTime"Q"presence"B"deviceIsSelf"B"mode"C"lastTransitionTime"Q"pushToken"{basic_string<char, std::char_traits<char>, std::allocator<char>>=""{?="__rep_"(__rep="__s"{__short="__data_"[23c]"__size_"b7"__is_long_"b1}"__l"{__long="__data_"*"__size_"Q"__cap_"b63"__is_long_"b1})}}} _internalInfo;
```

## Properties

```
@property (T@"NSString",R) deviceId;
@property (T@"NSString",R) serialNumber;
@property (TB,R) presence;
@property (TQ,R) lastSeenTime;
@property (TB,R) deviceIsSelf;
@property (Tq,R) mode;
@property (TQ,R) lastTransitionTime;
@property (T@"NSString",R) pushToken;
```

## Class methods

```
+[CTQuickSwitchCircleDeviceInfo supportsSecureCoding];
+[CTQuickSwitchCircleDeviceInfo deviceCircleInfoWithInternalInfo:];
```

## Instance methods

```
-[CTQuickSwitchCircleDeviceInfo pushToken];
-[CTQuickSwitchCircleDeviceInfo deviceId];
-[CTQuickSwitchCircleDeviceInfo serialNumber];
-[CTQuickSwitchCircleDeviceInfo encodeWithCoder:];
-[CTQuickSwitchCircleDeviceInfo mode];
-[CTQuickSwitchCircleDeviceInfo description];
-[CTQuickSwitchCircleDeviceInfo initWithInternalInfo:];
-[CTQuickSwitchCircleDeviceInfo initWithCoder:];
-[CTQuickSwitchCircleDeviceInfo copyWithZone:];
-[CTQuickSwitchCircleDeviceInfo deviceIsSelf];
-[CTQuickSwitchCircleDeviceInfo internalInfo];
-[CTQuickSwitchCircleDeviceInfo lastSeenTime];
-[CTQuickSwitchCircleDeviceInfo lastTransitionTime];
-[CTQuickSwitchCircleDeviceInfo presence];
```

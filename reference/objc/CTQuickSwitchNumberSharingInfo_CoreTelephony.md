# `CTQuickSwitchNumberSharingInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 19 instance variables, 19 properties, 42 instance methods, 1 class methods

## Instance variables

```
B _isPrimary;
B _isQuickSwitchStatePassiveDataSuppressed;
B _isEnabled;
@"NSString" _pairedDeviceType;
@"NSString" _pairedDeviceName;
@"NSString" _pairedDeviceSerialNumber;
@"NSString" _pairedDeviceOSVersion;
Q _pairedDeviceRole;
@"NSString" _pairedICCID;
@"NSString" _mode;
@"NSString" _serialNumber;
@"NSDate" _firstEnrolledDate;
@"CTQuickSwitchNumberSharingSession" _lastSession;
Q _role;
Q _lifecycleState;
@"NSString" _iccid;
@"NSString" _phoneNumber;
@"NSString" _formattedPhoneNumber;
@"NSString" _carrierName;
```

## Properties

```
@property (T@"NSString",&,N,V_pairedDeviceType) pairedDeviceType;
@property (T@"NSString",&,N,V_pairedDeviceName) pairedDeviceName;
@property (T@"NSString",&,N,V_pairedDeviceSerialNumber) pairedDeviceSerialNumber;
@property (T@"NSString",&,N,V_pairedDeviceOSVersion) pairedDeviceOSVersion;
@property (TQ,N,V_pairedDeviceRole) pairedDeviceRole;
@property (T@"NSString",&,N,V_pairedICCID) pairedICCID;
@property (T@"NSString",&,N,V_mode) mode;
@property (T@"NSString",&,N,V_serialNumber) serialNumber;
@property (T@"NSString",&,N,V_iccid) iccid;
@property (T@"NSString",&,N,V_phoneNumber) phoneNumber;
@property (T@"NSString",&,N,V_formattedPhoneNumber) formattedPhoneNumber;
@property (T@"NSString",&,N,V_carrierName) carrierName;
@property (TQ,N,V_role) role;
@property (TQ,N,V_lifecycleState) lifecycleState;
@property (TB,N,V_isEnabled) isEnabled;
@property (T@"NSDate",&,N,V_firstEnrolledDate) firstEnrolledDate;
@property (T@"CTQuickSwitchNumberSharingSession",&,N,V_lastSession) lastSession;
@property (TB,N,V_isPrimary) isPrimary;
@property (TB,N,V_isQuickSwitchStatePassiveDataSuppressed) isQuickSwitchStatePassiveDataSuppressed;
```

## Class methods

```
+[CTQuickSwitchNumberSharingInfo supportsSecureCoding];
```

## Instance methods

```
-[CTQuickSwitchNumberSharingInfo phoneNumber];
-[CTQuickSwitchNumberSharingInfo setPairedDeviceName:];
-[CTQuickSwitchNumberSharingInfo lifecycleState];
-[CTQuickSwitchNumberSharingInfo setSerialNumber:];
-[CTQuickSwitchNumberSharingInfo carrierName];
-[CTQuickSwitchNumberSharingInfo setPairedDeviceType:];
-[CTQuickSwitchNumberSharingInfo setCarrierName:];
-[CTQuickSwitchNumberSharingInfo lastSession];
-[CTQuickSwitchNumberSharingInfo pairedDeviceSerialNumber];
-[CTQuickSwitchNumberSharingInfo setLastSession:];
-[CTQuickSwitchNumberSharingInfo isPrimary];
-[CTQuickSwitchNumberSharingInfo pairedICCID];
-[CTQuickSwitchNumberSharingInfo setIsEnabled:];
-[CTQuickSwitchNumberSharingInfo pairedDeviceOSVersion];
-[CTQuickSwitchNumberSharingInfo formattedPhoneNumber];
-[CTQuickSwitchNumberSharingInfo setPhoneNumber:];
-[CTQuickSwitchNumberSharingInfo pairedDeviceName];
-[CTQuickSwitchNumberSharingInfo pairedDeviceRole];
-[CTQuickSwitchNumberSharingInfo iccid];
-[CTQuickSwitchNumberSharingInfo setFormattedPhoneNumber:];
-[CTQuickSwitchNumberSharingInfo serialNumber];
-[CTQuickSwitchNumberSharingInfo isQuickSwitchStatePassiveDataSuppressed];
-[CTQuickSwitchNumberSharingInfo setMode:];
-[CTQuickSwitchNumberSharingInfo setIsQuickSwitchStatePassiveDataSuppressed:];
-[CTQuickSwitchNumberSharingInfo isEnabled];
-[CTQuickSwitchNumberSharingInfo setPairedDeviceOSVersion:];
-[CTQuickSwitchNumberSharingInfo setFirstEnrolledDate:];
-[CTQuickSwitchNumberSharingInfo encodeWithCoder:];
-[CTQuickSwitchNumberSharingInfo mode];
-[CTQuickSwitchNumberSharingInfo role];
-[CTQuickSwitchNumberSharingInfo setRole:];
-[CTQuickSwitchNumberSharingInfo setLifecycleState:];
-[CTQuickSwitchNumberSharingInfo description];
-[CTQuickSwitchNumberSharingInfo initWithCoder:];
-[CTQuickSwitchNumberSharingInfo setPairedDeviceRole:];
-[CTQuickSwitchNumberSharingInfo setPairedDeviceSerialNumber:];
-[CTQuickSwitchNumberSharingInfo setPairedICCID:];
-[CTQuickSwitchNumberSharingInfo setIsPrimary:];
-[CTQuickSwitchNumberSharingInfo copyWithZone:];
-[CTQuickSwitchNumberSharingInfo setIccid:];
-[CTQuickSwitchNumberSharingInfo pairedDeviceType];
-[CTQuickSwitchNumberSharingInfo firstEnrolledDate];
```

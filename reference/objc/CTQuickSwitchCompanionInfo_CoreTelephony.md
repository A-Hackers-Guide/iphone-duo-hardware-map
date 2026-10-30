# `CTQuickSwitchCompanionInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 7 instance variables, 7 properties, 22 instance methods, 2 class methods

## Instance variables

```
@"NSString" _iccid;
Q _role;
@"NSString" _displayName;
@"NSString" _model;
@"NSString" _serialNumber;
@"NSString" _osVersion;
@"NSString" _eid;
```

## Properties

```
@property (T@"NSString",&,V_iccid) iccid;
@property (TQ,V_role) role;
@property (T@"NSString",&,V_displayName) displayName;
@property (T@"NSString",&,V_model) model;
@property (T@"NSString",&,V_serialNumber) serialNumber;
@property (T@"NSString",&,V_osVersion) osVersion;
@property (T@"NSString",&,V_eid) eid;
```

## Class methods

```
+[CTQuickSwitchCompanionInfo supportsSecureCoding];
+[CTQuickSwitchCompanionInfo companionInfoFromDictionary:];
```

## Instance methods

```
-[CTQuickSwitchCompanionInfo toDictionary];
-[CTQuickSwitchCompanionInfo model];
-[CTQuickSwitchCompanionInfo setSerialNumber:];
-[CTQuickSwitchCompanionInfo setModel:];
-[CTQuickSwitchCompanionInfo osVersion];
-[CTQuickSwitchCompanionInfo setOsVersion:];
-[CTQuickSwitchCompanionInfo displayName];
-[CTQuickSwitchCompanionInfo setDisplayName:];
-[CTQuickSwitchCompanionInfo iccid];
-[CTQuickSwitchCompanionInfo serialNumber];
-[CTQuickSwitchCompanionInfo encodeWithCoder:];
-[CTQuickSwitchCompanionInfo role];
-[CTQuickSwitchCompanionInfo hash];
-[CTQuickSwitchCompanionInfo setRole:];
-[CTQuickSwitchCompanionInfo description];
-[CTQuickSwitchCompanionInfo initWithCoder:];
-[CTQuickSwitchCompanionInfo copyWithZone:];
-[CTQuickSwitchCompanionInfo setIccid:];
-[CTQuickSwitchCompanionInfo isEqual:];
-[CTQuickSwitchCompanionInfo setEid:];
-[CTQuickSwitchCompanionInfo eid];
-[CTQuickSwitchCompanionInfo initWithIccid:role:displayName:model:serialNumber:osVersion:eid:];
```

# `CTQuickSwitchAccountInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 10 instance variables, 18 properties, 36 instance methods, 2 class methods

## Instance variables

```
B _isEligibleAsPrimary;
B _isEnabled;
B _supportsNoChargeForOnboarding;
Q _supportType;
Q _qsRole;
Q _qsLifecycleState;
@"CTAppleAccountDsids" _appleAccountDsids;
@"NSArray" _companionInfos;
@"CTDeviceIdentifier" _deviceID;
@"CTPlanIdentifier" _planID;
```

## Properties

```
@property (T@"CTDeviceIdentifier",&,V_deviceID) deviceID;
@property (T@"CTPlanIdentifier",&,V_planID) planID;
@property (TB,V_isEligibleAsPrimary) isEligibleAsPrimary;
@property (TB,V_isEnabled) isEnabled;
@property (TQ,V_supportType) supportType;
@property (TQ,V_qsRole) qsRole;
@property (TQ,V_qsLifecycleState) qsLifecycleState;
@property (T@"CTAppleAccountDsids",&,V_appleAccountDsids) appleAccountDsids;
@property (T@"NSArray",&,V_companionInfos) companionInfos;
@property (TB,V_supportsNoChargeForOnboarding) supportsNoChargeForOnboarding;
@property (T@"NSString",R) deviceName;
@property (T@"NSString",R) iccid;
@property (T@"NSString",R) modelName;
@property (T@"NSString",R) phoneNumber;
@property (T@"NSString",R) serialNumber;
@property (TB,R) isQuickSwitchSupported;
@property (TB,R) requiresSoftwareUpdate;
@property (TB,R) isEnrolled;
```

## Class methods

```
+[CTQuickSwitchAccountInfo supportsSecureCoding];
+[CTQuickSwitchAccountInfo accountInfoFromDictionary:];
```

## Instance methods

```
-[CTQuickSwitchAccountInfo toDictionary];
-[CTQuickSwitchAccountInfo phoneNumber];
-[CTQuickSwitchAccountInfo deviceID];
-[CTQuickSwitchAccountInfo setIsEnabled:];
-[CTQuickSwitchAccountInfo iccid];
-[CTQuickSwitchAccountInfo serialNumber];
-[CTQuickSwitchAccountInfo isEnabled];
-[CTQuickSwitchAccountInfo setDeviceID:];
-[CTQuickSwitchAccountInfo encodeWithCoder:];
-[CTQuickSwitchAccountInfo hash];
-[CTQuickSwitchAccountInfo description];
-[CTQuickSwitchAccountInfo initWithCoder:];
-[CTQuickSwitchAccountInfo copyWithZone:];
-[CTQuickSwitchAccountInfo isEqual:];
-[CTQuickSwitchAccountInfo deviceName];
-[CTQuickSwitchAccountInfo modelName];
-[CTQuickSwitchAccountInfo isEnrolled];
-[CTQuickSwitchAccountInfo setSupportType:];
-[CTQuickSwitchAccountInfo appleAccountDsids];
-[CTQuickSwitchAccountInfo companionInfos];
-[CTQuickSwitchAccountInfo initWithIccid:phoneNumber:deviceName:modelName:serialNumber:isEligibleAsPrimary:isEnabled:supportType:qsRole:qsLifecycleState:appleAccountDsids:];
-[CTQuickSwitchAccountInfo isEligibleAsPrimary];
-[CTQuickSwitchAccountInfo isQuickSwitchSupported];
-[CTQuickSwitchAccountInfo planID];
-[CTQuickSwitchAccountInfo qsLifecycleState];
-[CTQuickSwitchAccountInfo qsRole];
-[CTQuickSwitchAccountInfo requiresSoftwareUpdate];
-[CTQuickSwitchAccountInfo setAppleAccountDsids:];
-[CTQuickSwitchAccountInfo setCompanionInfos:];
-[CTQuickSwitchAccountInfo setIsEligibleAsPrimary:];
-[CTQuickSwitchAccountInfo setPlanID:];
-[CTQuickSwitchAccountInfo setQsLifecycleState:];
-[CTQuickSwitchAccountInfo setQsRole:];
-[CTQuickSwitchAccountInfo setSupportsNoChargeForOnboarding:];
-[CTQuickSwitchAccountInfo supportType];
-[CTQuickSwitchAccountInfo supportsNoChargeForOnboarding];
```

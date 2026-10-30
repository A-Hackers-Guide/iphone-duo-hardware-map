# `BKIdentity`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 31 instance methods, 1 class methods

## Instance variables

```
B _placeholderIdentity;
B _hasPeriocularEnrollment;
B _hasPeriocularEnrollmentWithGlasses;
B _canAddPeriocularEnrollment;
I _userID;
@"NSUUID" _uuid;
q _type;
@"NSString" _name;
@"NSDate" _creationTime;
@"BKDevice" _device;
@"BKAccessory" _accessory;
@"BKAccessoryGroup" _accessoryGroup;
q _secondaryPeriocularEnrollments;
```

## Properties

```
@property (T@"NSUUID",&,N,V_uuid) uuid;
@property (TI,N,V_userID) userID;
@property (Tq,N,V_type) type;
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSDate",&,N,V_creationTime) creationTime;
@property (T@"BKDevice",&,N,V_device) device;
@property (T@"BKAccessory",&,N,V_accessory) accessory;
@property (T@"BKAccessoryGroup",&,N,V_accessoryGroup) accessoryGroup;
@property (TB,N,V_placeholderIdentity) placeholderIdentity;
@property (TB,N,V_hasPeriocularEnrollment) hasPeriocularEnrollment;
@property (TB,N,V_hasPeriocularEnrollmentWithGlasses) hasPeriocularEnrollmentWithGlasses;
@property (TB,N,V_canAddPeriocularEnrollment) canAddPeriocularEnrollment;
@property (Tq,N,V_secondaryPeriocularEnrollments) secondaryPeriocularEnrollments;
```

## Class methods

```
+[BKIdentity identity];
```

## Instance methods

```
-[BKIdentity creationTime];
-[BKIdentity userID];
-[BKIdentity setUserID:];
-[BKIdentity setDevice:];
-[BKIdentity uuid];
-[BKIdentity device];
-[BKIdentity setUuid:];
-[BKIdentity setType:];
-[BKIdentity type];
-[BKIdentity hash];
-[BKIdentity setName:];
-[BKIdentity isEqualToIdentity:];
-[BKIdentity isEqual:];
-[BKIdentity name];
-[BKIdentity setCreationTime:];
-[BKIdentity accessory];
-[BKIdentity setAccessory:];
-[BKIdentity serverIdentity];
-[BKIdentity hasPeriocularEnrollment];
-[BKIdentity accessoryGroup];
-[BKIdentity canAddPeriocularEnrollment];
-[BKIdentity hasPeriocularEnrollmentWithGlasses];
-[BKIdentity initWithServerIdentity:device:];
-[BKIdentity placeholderIdentity];
-[BKIdentity secondaryPeriocularEnrollments];
-[BKIdentity setAccessoryGroup:];
-[BKIdentity setCanAddPeriocularEnrollment:];
-[BKIdentity setHasPeriocularEnrollment:];
-[BKIdentity setHasPeriocularEnrollmentWithGlasses:];
-[BKIdentity setPlaceholderIdentity:];
-[BKIdentity setSecondaryPeriocularEnrollments:];
```

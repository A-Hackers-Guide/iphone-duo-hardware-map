# `BiometricKitIdentity`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 12 instance variables, 12 properties, 32 instance methods, 2 class methods

## Instance variables

```
I _userID;
i _type;
i _attribute;
i _entity;
I _flags;
@"NSUUID" _uuid;
@"NSString" _name;
@"NSDate" _creationTime;
q _matchCount;
q _matchCountContinuous;
q _updateCount;
@"BiometricKitAccessory" _accessory;
```

## Properties

```
@property (T@"NSUUID",&,N,V_uuid) uuid;
@property (TI,N,V_userID) userID;
@property (Ti,N,V_type) type;
@property (Ti,N,V_attribute) attribute;
@property (Ti,N,V_entity) entity;
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSDate",&,N,V_creationTime) creationTime;
@property (Tq,N,V_matchCount) matchCount;
@property (Tq,N,V_matchCountContinuous) matchCountContinuous;
@property (Tq,N,V_updateCount) updateCount;
@property (TI,N,V_flags) flags;
@property (T@"BiometricKitAccessory",&,N,V_accessory) accessory;
```

## Class methods

```
+[BiometricKitIdentity supportsSecureCoding];
+[BiometricKitIdentity biometricKitIdentity];
```

## Instance methods

```
-[BiometricKitIdentity creationTime];
-[BiometricKitIdentity userID];
-[BiometricKitIdentity setUserID:];
-[BiometricKitIdentity setEntity:];
-[BiometricKitIdentity setFlags:];
-[BiometricKitIdentity uuid];
-[BiometricKitIdentity flags];
-[BiometricKitIdentity init];
-[BiometricKitIdentity setUuid:];
-[BiometricKitIdentity updateCount];
-[BiometricKitIdentity setType:];
-[BiometricKitIdentity entity];
-[BiometricKitIdentity type];
-[BiometricKitIdentity encodeWithCoder:];
-[BiometricKitIdentity hash];
-[BiometricKitIdentity description];
-[BiometricKitIdentity setName:];
-[BiometricKitIdentity initWithCoder:];
-[BiometricKitIdentity attribute];
-[BiometricKitIdentity copyWithZone:];
-[BiometricKitIdentity isEqualToIdentity:];
-[BiometricKitIdentity isEqual:];
-[BiometricKitIdentity name];
-[BiometricKitIdentity setCreationTime:];
-[BiometricKitIdentity accessory];
-[BiometricKitIdentity setAccessory:];
-[BiometricKitIdentity setAttribute:];
-[BiometricKitIdentity setUpdateCount:];
-[BiometricKitIdentity matchCount];
-[BiometricKitIdentity matchCountContinuous];
-[BiometricKitIdentity setMatchCount:];
-[BiometricKitIdentity setMatchCountContinuous:];
```

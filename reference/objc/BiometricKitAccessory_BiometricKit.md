# `BiometricKitAccessory`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
I _type;
I _flags;
@"NSUUID" _uuid;
@"NSString" _name;
@"BiometricKitAccessoryGroup" _group;
```

## Properties

```
@property (TI,N,V_type) type;
@property (T@"NSUUID",&,N,V_uuid) uuid;
@property (T@"NSString",C,N,V_name) name;
@property (T@"BiometricKitAccessoryGroup",&,N,V_group) group;
@property (TI,N,V_flags) flags;
```

## Class methods

```
+[BiometricKitAccessory supportsSecureCoding];
```

## Instance methods

```
-[BiometricKitAccessory setGroup:];
-[BiometricKitAccessory setFlags:];
-[BiometricKitAccessory uuid];
-[BiometricKitAccessory flags];
-[BiometricKitAccessory setUuid:];
-[BiometricKitAccessory group];
-[BiometricKitAccessory setType:];
-[BiometricKitAccessory type];
-[BiometricKitAccessory encodeWithCoder:];
-[BiometricKitAccessory hash];
-[BiometricKitAccessory description];
-[BiometricKitAccessory setName:];
-[BiometricKitAccessory initWithCoder:];
-[BiometricKitAccessory copyWithZone:];
-[BiometricKitAccessory isEqual:];
-[BiometricKitAccessory name];
-[BiometricKitAccessory isEqualToAccessory:];
```

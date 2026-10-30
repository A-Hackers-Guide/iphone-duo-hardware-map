# `BiometricKitAccessoryGroup`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
I _type;
@"NSUUID" _uuid;
@"NSString" _name;
```

## Properties

```
@property (TI,N,V_type) type;
@property (T@"NSUUID",&,N,V_uuid) uuid;
@property (T@"NSString",C,N,V_name) name;
```

## Class methods

```
+[BiometricKitAccessoryGroup supportsSecureCoding];
```

## Instance methods

```
-[BiometricKitAccessoryGroup uuid];
-[BiometricKitAccessoryGroup setUuid:];
-[BiometricKitAccessoryGroup setType:];
-[BiometricKitAccessoryGroup type];
-[BiometricKitAccessoryGroup encodeWithCoder:];
-[BiometricKitAccessoryGroup hash];
-[BiometricKitAccessoryGroup description];
-[BiometricKitAccessoryGroup setName:];
-[BiometricKitAccessoryGroup initWithCoder:];
-[BiometricKitAccessoryGroup copyWithZone:];
-[BiometricKitAccessoryGroup isEqual:];
-[BiometricKitAccessoryGroup name];
-[BiometricKitAccessoryGroup isEqualToAccessoryGroup:];
```

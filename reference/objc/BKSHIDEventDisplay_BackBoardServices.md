# `BKSHIDEventDisplay`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `BSProtobufSerializable`, `NSCopying`
- 2 instance variables, 4 properties, 12 instance methods, 5 class methods

## Instance variables

```
B _builtin;
@"NSString" _hardwareIdentifier;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventDisplay supportsSecureCoding];
+[BKSHIDEventDisplay protobufSchema];
+[BKSHIDEventDisplay displayWithHardwareIdentifier:];
+[BKSHIDEventDisplay nullDisplay];
+[BKSHIDEventDisplay builtinDisplay];
```

## Instance methods

```
-[BKSHIDEventDisplay initForProtobufDecoding];
-[BKSHIDEventDisplay init];
-[BKSHIDEventDisplay _hardwareIdentifier];
-[BKSHIDEventDisplay _isBuiltinDisplay];
-[BKSHIDEventDisplay encodeWithCoder:];
-[BKSHIDEventDisplay hash];
-[BKSHIDEventDisplay description];
-[BKSHIDEventDisplay _isNullDisplay];
-[BKSHIDEventDisplay initWithCoder:];
-[BKSHIDEventDisplay _initWithHardwareIdentifier:];
-[BKSHIDEventDisplay copyWithZone:];
-[BKSHIDEventDisplay isEqual:];
```

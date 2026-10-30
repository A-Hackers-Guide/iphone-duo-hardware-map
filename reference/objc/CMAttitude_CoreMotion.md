# `CMAttitude`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 1 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
@ _internal;
```

## Properties

```
@property (Td,R,N) roll;
@property (Td,R,N) pitch;
@property (Td,R,N) yaw;
@property (T{?=ddddddddd},R,N) rotationMatrix;
@property (T{?=dddd},R,N) quaternion;
```

## Class methods

```
+[CMAttitude supportsSecureCoding];
```

## Instance methods

```
-[CMAttitude pitch];
-[CMAttitude yaw];
-[CMAttitude dealloc];
-[CMAttitude encodeWithCoder:];
-[CMAttitude description];
-[CMAttitude initWithCoder:];
-[CMAttitude copyWithZone:];
-[CMAttitude isEqual:];
-[CMAttitude quaternion];
-[CMAttitude roll];
-[CMAttitude initWithQuaternion:];
-[CMAttitude multiplyByInverseOfAttitude:];
-[CMAttitude rotationMatrix];
-[CMAttitude setQuaternion:];
```

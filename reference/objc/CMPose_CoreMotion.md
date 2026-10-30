# `CMPose`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CMLogItem`
- 1 instance variables, 6 properties, 14 instance methods, 1 class methods

## Instance variables

```
@ _internal;
```

## Properties

```
@property (T@"CMAttitude",R,N) attitude;
@property (T{?=ddd},R,N) translation;
@property (Td,R,N) consumedAuxTimestamp;
@property (Td,R,N) receivedAuxTimestamp;
@property (Td,R,N) machAbsTimestamp;
@property (Td,R,N) presentationTimestamp;
```

## Class methods

```
+[CMPose supportsSecureCoding];
```

## Instance methods

```
-[CMPose dealloc];
-[CMPose encodeWithCoder:];
-[CMPose description];
-[CMPose initWithCoder:];
-[CMPose copyWithZone:];
-[CMPose isEqual:];
-[CMPose translation];
-[CMPose attitude];
-[CMPose consumedAuxTimestamp];
-[CMPose initWithPose:timestamp:];
-[CMPose isEqualToPose:];
-[CMPose machAbsTimestamp];
-[CMPose presentationTimestamp];
-[CMPose receivedAuxTimestamp];
```

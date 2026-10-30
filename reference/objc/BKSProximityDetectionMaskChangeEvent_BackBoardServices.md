# `BKSProximityDetectionMaskChangeEvent`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `NSSecureCoding`, `BSDescriptionStreamable`
- 3 instance variables, 7 properties, 12 instance methods, 3 class methods

## Instance variables

```
I _detectionMask;
i _mode;
Q _timestamp;
```

## Properties

```
@property (TI,R,N) detectionMask;
@property (Ti,R,N) mode;
@property (TQ,R,N) timestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSProximityDetectionMaskChangeEvent build:];
+[BKSProximityDetectionMaskChangeEvent supportsSecureCoding];
+[BKSProximityDetectionMaskChangeEvent new];
```

## Instance methods

```
-[BKSProximityDetectionMaskChangeEvent mutableCopyWithZone:];
-[BKSProximityDetectionMaskChangeEvent init];
-[BKSProximityDetectionMaskChangeEvent appendDescriptionToFormatter:];
-[BKSProximityDetectionMaskChangeEvent timestamp];
-[BKSProximityDetectionMaskChangeEvent encodeWithCoder:];
-[BKSProximityDetectionMaskChangeEvent mode];
-[BKSProximityDetectionMaskChangeEvent hash];
-[BKSProximityDetectionMaskChangeEvent description];
-[BKSProximityDetectionMaskChangeEvent initWithCoder:];
-[BKSProximityDetectionMaskChangeEvent copyWithZone:];
-[BKSProximityDetectionMaskChangeEvent isEqual:];
-[BKSProximityDetectionMaskChangeEvent detectionMask];
```

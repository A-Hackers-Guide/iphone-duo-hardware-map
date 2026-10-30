# `CMAPosition`

- Image: [`/System/Library/PrivateFrameworks/CoreMotionAlgorithms.framework/CoreMotionAlgorithms`](../userland/System__Library__PrivateFrameworks__CoreMotionAlgorithms.framework__CoreMotionAlgorithms.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 22 instance methods, 0 class methods

## Instance variables

```
q convergenceStatus;
q revokeReason;
q verticalState;
d _timestamp;
d _distance;
@"NSNumber" _horizontalDistanceNumber;
d _horizontalAngle;
@"NSNumber" _horizontalAngleNumber;
d _horizontalAngleAccuracy;
@"NSNumber" _horizontalAngleAccuracyNumber;
@"NSNumber" _horizontalAngleUncertaintyNumber;
```

## Properties

```
@property (Td,N,V_timestamp) timestamp;
@property (Td,N,V_distance) distance;
@property (T@"NSNumber",N,V_horizontalDistanceNumber) horizontalDistanceNumber;
@property (Td,N,V_horizontalAngle) horizontalAngle;
@property (T@"NSNumber",N,V_horizontalAngleNumber) horizontalAngleNumber;
@property (Td,N,V_horizontalAngleAccuracy) horizontalAngleAccuracy;
@property (T@"NSNumber",N,V_horizontalAngleAccuracyNumber) horizontalAngleAccuracyNumber;
@property (T@"NSNumber",N,V_horizontalAngleUncertaintyNumber) horizontalAngleUncertaintyNumber;
@property (Tq,N,VconvergenceStatus) convergenceStatus;
@property (Tq,N,VrevokeReason) revokeReason;
@property (Tq,N,VverticalState) verticalState;
```

## Instance methods

```
-[CMAPosition distance];
-[CMAPosition setTimestamp:];
-[CMAPosition setDistance:];
-[CMAPosition timestamp];
-[CMAPosition horizontalAngle];
-[CMAPosition setHorizontalAngle:];
-[CMAPosition horizontalAngleAccuracy];
-[CMAPosition setHorizontalAngleAccuracy:];
-[CMAPosition convergenceStatus];
-[CMAPosition horizontalAngleAccuracyNumber];
-[CMAPosition horizontalAngleNumber];
-[CMAPosition horizontalAngleUncertaintyNumber];
-[CMAPosition horizontalDistanceNumber];
-[CMAPosition revokeReason];
-[CMAPosition setConvergenceStatus:];
-[CMAPosition setHorizontalAngleAccuracyNumber:];
-[CMAPosition setHorizontalAngleNumber:];
-[CMAPosition setHorizontalAngleUncertaintyNumber:];
-[CMAPosition setHorizontalDistanceNumber:];
-[CMAPosition setRevokeReason:];
-[CMAPosition setVerticalState:];
-[CMAPosition verticalState];
```

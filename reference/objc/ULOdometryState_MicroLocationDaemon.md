# `ULOdometryState`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 10 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"NSNumber" _deltaPositionX;
@"NSNumber" _deltaPositionY;
@"NSNumber" _deltaPositionZ;
@"NSNumber" _alignmentAngleRad;
@"NSNumber" _alignmentAngleErrorEstimateRad;
@"NSNumber" _quaternionX;
@"NSNumber" _quaternionY;
@"NSNumber" _quaternionZ;
@"NSNumber" _quaternionW;
d _timestamp;
```

## Properties

```
@property (T@"NSNumber",&,N,V_deltaPositionX) deltaPositionX;
@property (T@"NSNumber",&,N,V_deltaPositionY) deltaPositionY;
@property (T@"NSNumber",&,N,V_deltaPositionZ) deltaPositionZ;
@property (T@"NSNumber",&,N,V_alignmentAngleRad) alignmentAngleRad;
@property (T@"NSNumber",&,N,V_alignmentAngleErrorEstimateRad) alignmentAngleErrorEstimateRad;
@property (T@"NSNumber",&,N,V_quaternionX) quaternionX;
@property (T@"NSNumber",&,N,V_quaternionY) quaternionY;
@property (T@"NSNumber",&,N,V_quaternionZ) quaternionZ;
@property (T@"NSNumber",&,N,V_quaternionW) quaternionW;
@property (Td,N,V_timestamp) timestamp;
```

## Instance methods

```
-[ULOdometryState setQuaternionY:];
-[ULOdometryState quaternionW];
-[ULOdometryState setDeltaPositionY:];
-[ULOdometryState setQuaternionX:];
-[ULOdometryState setQuaternionW:];
-[ULOdometryState setDeltaPositionZ:];
-[ULOdometryState quaternionZ];
-[ULOdometryState setQuaternionZ:];
-[ULOdometryState deltaPositionY];
-[ULOdometryState quaternionY];
-[ULOdometryState deltaPositionX];
-[ULOdometryState deltaPositionZ];
-[ULOdometryState setDeltaPositionX:];
-[ULOdometryState alignmentAngleRad];
-[ULOdometryState setTimestamp:];
-[ULOdometryState setAlignmentAngleErrorEstimateRad:];
-[ULOdometryState timestamp];
-[ULOdometryState quaternionX];
-[ULOdometryState initWithDeltaPositionX:deltaPositionY:deltaPositionZ:alignmentAngleRad:alignmentAngleErrorEstimateRad:quaternionX:quaternionY:quaternionZ:quaternionW:timestamp:];
-[ULOdometryState alignmentAngleErrorEstimateRad];
-[ULOdometryState setAlignmentAngleRad:];
```

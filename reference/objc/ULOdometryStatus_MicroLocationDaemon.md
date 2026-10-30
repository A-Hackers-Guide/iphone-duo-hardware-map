# `ULOdometryStatus`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 13 properties, 27 instance methods, 0 class methods

## Instance variables

```
I _sensorID;
@"NSNumber" _deltaPositionX;
@"NSNumber" _deltaPositionY;
@"NSNumber" _deltaPositionZ;
@"NSNumber" _alignmentAngleRad;
@"NSNumber" _alignmentAngleErrorEstimateRad;
@"NSNumber" _quaternionX;
@"NSNumber" _quaternionY;
@"NSNumber" _quaternionZ;
@"NSNumber" _quaternionW;
@"NSDate" _statusDate;
q _odometrySourceType;
@"NSString" _deviceIdentifier;
```

## Properties

```
@property (T@"NSString",&,N,V_deviceIdentifier) deviceIdentifier;
@property (T@"NSNumber",&,N,V_deltaPositionX) deltaPositionX;
@property (T@"NSNumber",&,N,V_deltaPositionY) deltaPositionY;
@property (T@"NSNumber",&,N,V_deltaPositionZ) deltaPositionZ;
@property (T@"NSNumber",&,N,V_alignmentAngleRad) alignmentAngleRad;
@property (T@"NSNumber",&,N,V_alignmentAngleErrorEstimateRad) alignmentAngleErrorEstimateRad;
@property (T@"NSNumber",&,N,V_quaternionX) quaternionX;
@property (T@"NSNumber",&,N,V_quaternionY) quaternionY;
@property (T@"NSNumber",&,N,V_quaternionZ) quaternionZ;
@property (T@"NSNumber",&,N,V_quaternionW) quaternionW;
@property (TI,N,V_sensorID) sensorID;
@property (T@"NSDate",&,N,V_statusDate) statusDate;
@property (Tq,N,V_odometrySourceType) odometrySourceType;
```

## Instance methods

```
-[ULOdometryStatus setQuaternionY:];
-[ULOdometryStatus quaternionW];
-[ULOdometryStatus setDeltaPositionY:];
-[ULOdometryStatus setQuaternionX:];
-[ULOdometryStatus setQuaternionW:];
-[ULOdometryStatus setDeltaPositionZ:];
-[ULOdometryStatus quaternionZ];
-[ULOdometryStatus setQuaternionZ:];
-[ULOdometryStatus deltaPositionY];
-[ULOdometryStatus quaternionY];
-[ULOdometryStatus deltaPositionX];
-[ULOdometryStatus deltaPositionZ];
-[ULOdometryStatus setDeltaPositionX:];
-[ULOdometryStatus alignmentAngleRad];
-[ULOdometryStatus setDeviceIdentifier:];
-[ULOdometryStatus setAlignmentAngleErrorEstimateRad:];
-[ULOdometryStatus setOdometrySourceType:];
-[ULOdometryStatus deviceIdentifier];
-[ULOdometryStatus setStatusDate:];
-[ULOdometryStatus statusDate];
-[ULOdometryStatus quaternionX];
-[ULOdometryStatus sensorID];
-[ULOdometryStatus alignmentAngleErrorEstimateRad];
-[ULOdometryStatus setSensorID:];
-[ULOdometryStatus initWithOdometrySourceType:deltaPositionX:deltaPositionY:deltaPositionZ:alignmentAngleRad:alignmentAngleErrorEstimateRad:quaternionX:quaternionY:quaternionZ:quaternionW:date:];
-[ULOdometryStatus odometrySourceType];
-[ULOdometryStatus setAlignmentAngleRad:];
```

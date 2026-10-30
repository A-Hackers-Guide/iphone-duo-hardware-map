# `ULPDRFenceBridge`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _isFenceActive;
B _isSessionStarted;
f _radiusSquare;
f _positionX;
f _positionY;
@"ULOdometryMonitor" _odometryMonitor;
@"NSString" _fenceName;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSNumber" _radius;
q _sourceType;
@? _onMotionMeasurements;
@? _onErrorIndication;
```

## Properties

```
@property (T@"ULOdometryMonitor",&,N,V_odometryMonitor) odometryMonitor;
@property (T@"NSString",&,N,V_fenceName) fenceName;
@property (TB,N,V_isFenceActive) isFenceActive;
@property (TB,N,V_isSessionStarted) isSessionStarted;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSNumber",&,N,V_radius) radius;
@property (Tq,N,V_sourceType) sourceType;
@property (Tf,N,V_radiusSquare) radiusSquare;
@property (Tf,N,V_positionX) positionX;
@property (Tf,N,V_positionY) positionY;
@property (T@?,C,N,V_onMotionMeasurements) onMotionMeasurements;
@property (T@?,C,N,V_onErrorIndication) onErrorIndication;
```

## Instance methods

```
-[ULPDRFenceBridge sourceType];
-[ULPDRFenceBridge setOdometryMonitor:];
-[ULPDRFenceBridge fenceName];
-[ULPDRFenceBridge queue];
-[ULPDRFenceBridge endSession];
-[ULPDRFenceBridge setRadius:];
-[ULPDRFenceBridge setSourceType:];
-[ULPDRFenceBridge setPositionX:];
-[ULPDRFenceBridge radius];
-[ULPDRFenceBridge positionX];
-[ULPDRFenceBridge startSession];
-[ULPDRFenceBridge positionY];
-[ULPDRFenceBridge setPositionY:];
-[ULPDRFenceBridge setQueue:];
-[ULPDRFenceBridge odometryMonitor];
-[ULPDRFenceBridge isSessionStarted];
-[ULPDRFenceBridge clearFence];
-[ULPDRFenceBridge isFenceActive];
-[ULPDRFenceBridge setIsFenceActive:];
-[ULPDRFenceBridge setIsSessionStarted:];
-[ULPDRFenceBridge setFenceRadius:];
-[ULPDRFenceBridge handleOdometryStatus:withError:];
-[ULPDRFenceBridge handleFenceCrossWithError:];
-[ULPDRFenceBridge initWithFenceIdentifier:odometryMonitor:sourceType:queue:radiusInMeters:callback:errorCallback:];
-[ULPDRFenceBridge onErrorIndication];
-[ULPDRFenceBridge onMotionMeasurements];
-[ULPDRFenceBridge radiusSquare];
-[ULPDRFenceBridge setFence];
-[ULPDRFenceBridge setFenceName:];
-[ULPDRFenceBridge setOnErrorIndication:];
-[ULPDRFenceBridge setOnMotionMeasurements:];
-[ULPDRFenceBridge setRadiusSquare:];
-[ULPDRFenceBridge startMonitoringOdometry];
```

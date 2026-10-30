# `ULCMFenceBridge`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _isFenceActive;
B _isSessionStarted;
@"CMPedestrianFenceManager" _fenceManager;
@"NSString" _fenceIdentifier;
@"NSString" _fenceName;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSNumber" _radius;
@? _onMotionMeasurements;
@? _onErrorIndication;
```

## Properties

```
@property (T@"CMPedestrianFenceManager",&,N,V_fenceManager) fenceManager;
@property (T@"NSString",&,N,V_fenceIdentifier) fenceIdentifier;
@property (T@"NSString",&,N,V_fenceName) fenceName;
@property (TB,N,V_isFenceActive) isFenceActive;
@property (TB,N,V_isSessionStarted) isSessionStarted;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"NSNumber",&,N,V_radius) radius;
@property (T@?,C,N,V_onMotionMeasurements) onMotionMeasurements;
@property (T@?,C,N,V_onErrorIndication) onErrorIndication;
```

## Class methods

```
+[ULCMFenceBridge _isAvailable];
```

## Instance methods

```
-[ULCMFenceBridge fenceName];
-[ULCMFenceBridge queue];
-[ULCMFenceBridge endSession];
-[ULCMFenceBridge setRadius:];
-[ULCMFenceBridge radius];
-[ULCMFenceBridge fenceManager];
-[ULCMFenceBridge startSession];
-[ULCMFenceBridge setFenceManager:];
-[ULCMFenceBridge setQueue:];
-[ULCMFenceBridge isSessionStarted];
-[ULCMFenceBridge fenceIdentifier];
-[ULCMFenceBridge clearFence];
-[ULCMFenceBridge isFenceActive];
-[ULCMFenceBridge setFenceIdentifier:];
-[ULCMFenceBridge setIsFenceActive:];
-[ULCMFenceBridge setIsSessionStarted:];
-[ULCMFenceBridge setFenceRadius:];
-[ULCMFenceBridge _handleFenceCross:error:];
-[ULCMFenceBridge initWithFenceIdentifier:queue:radiusInMeters:callback:errorCallback:];
-[ULCMFenceBridge onErrorIndication];
-[ULCMFenceBridge onMotionMeasurements];
-[ULCMFenceBridge setFence];
-[ULCMFenceBridge setFenceName:];
-[ULCMFenceBridge setOnErrorIndication:];
-[ULCMFenceBridge setOnMotionMeasurements:];
```

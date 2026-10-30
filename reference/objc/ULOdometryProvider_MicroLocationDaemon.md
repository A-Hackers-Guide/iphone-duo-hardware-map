# `ULOdometryProvider`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 15 properties, 44 instance methods, 4 class methods

## Instance variables

```
@"<ULOdometrySource>" _odometrySource;
q _odometrySourceType;
@"NSObject<OS_dispatch_queue>" _queue;
@"<ULOdometryProviderDelegate>" _delegate;
@"NSUUID" _trajectoryUUID;
@"NSNumber" _deltaPositionX;
@"NSNumber" _deltaPositionY;
@"NSNumber" _deltaPositionZ;
@"NSNumber" _quaternionX;
@"NSNumber" _quaternionY;
@"NSNumber" _quaternionZ;
@"NSNumber" _quaternionW;
@"NSDate" _previousStatusUpdateDate;
@"NSMutableArray" _alignmentAngleBuffer;
@"NSNumber" _accumulatedAlignmentAngleRad;
@"NSNumber" _accumulatedAlignmentAngleErrorEstimateRad;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"<ULOdometryProviderDelegate>",&,N,V_delegate) delegate;
@property (T@"NSUUID",&,N,V_trajectoryUUID) trajectoryUUID;
@property (T@"NSNumber",&,N,V_deltaPositionX) deltaPositionX;
@property (T@"NSNumber",&,N,V_deltaPositionY) deltaPositionY;
@property (T@"NSNumber",&,N,V_deltaPositionZ) deltaPositionZ;
@property (T@"NSNumber",&,N,V_quaternionX) quaternionX;
@property (T@"NSNumber",&,N,V_quaternionY) quaternionY;
@property (T@"NSNumber",&,N,V_quaternionZ) quaternionZ;
@property (T@"NSNumber",&,N,V_quaternionW) quaternionW;
@property (T@"NSDate",&,N,V_previousStatusUpdateDate) previousStatusUpdateDate;
@property (Tq,N,V_odometrySourceType) odometrySourceType;
@property (T@"NSMutableArray",&,N,V_alignmentAngleBuffer) alignmentAngleBuffer;
@property (T@"NSNumber",&,N,V_accumulatedAlignmentAngleRad) accumulatedAlignmentAngleRad;
@property (T@"NSNumber",&,N,V_accumulatedAlignmentAngleErrorEstimateRad) accumulatedAlignmentAngleErrorEstimateRad;
```

## Class methods

```
+[ULOdometryProvider findFenceCrossingOdometryEntryWithOdometryEntries:fenceRadius:shouldReturnNilIfNoCrossing:];
+[ULOdometryProvider isCMOdometryAvailable];
+[ULOdometryProvider isNPDROdometryAvailable];
+[ULOdometryProvider runtimeOdometrySourceType];
```

## Instance methods

```
-[ULOdometryProvider setQuaternionY:];
-[ULOdometryProvider quaternionW];
-[ULOdometryProvider setDeltaPositionY:];
-[ULOdometryProvider setQuaternionX:];
-[ULOdometryProvider setQuaternionW:];
-[ULOdometryProvider setDeltaPositionZ:];
-[ULOdometryProvider quaternionZ];
-[ULOdometryProvider setQuaternionZ:];
-[ULOdometryProvider deltaPositionY];
-[ULOdometryProvider quaternionY];
-[ULOdometryProvider deltaPositionX];
-[ULOdometryProvider deltaPositionZ];
-[ULOdometryProvider setDeltaPositionX:];
-[ULOdometryProvider didReceiveOdometryProviderStateIsAvailable:];
-[ULOdometryProvider _resetTrajectory];
-[ULOdometryProvider _addAlignmentAngleToBuffer:errorEstimate:timestamp:];
-[ULOdometryProvider setOdometrySourceType:];
-[ULOdometryProvider setPreviousStatusUpdateDate:];
-[ULOdometryProvider _updatePosition:];
-[ULOdometryProvider requestNPDRUpdate];
-[ULOdometryProvider queue];
-[ULOdometryProvider _resetPosition];
-[ULOdometryProvider stopBackgroundUpdates];
-[ULOdometryProvider accumulatedAlignmentAngleErrorEstimateRad];
-[ULOdometryProvider setDelegate:];
-[ULOdometryProvider setAlignmentAngleBuffer:];
-[ULOdometryProvider _checkIfExitedBubble];
-[ULOdometryProvider setAccumulatedAlignmentAngleRad:];
-[ULOdometryProvider _getTimestampFromState:];
-[ULOdometryProvider quaternionX];
-[ULOdometryProvider delegate];
-[ULOdometryProvider trajectoryUUID];
-[ULOdometryProvider accumulatedAlignmentAngleRad];
-[ULOdometryProvider initWithQueue:odometrySourceType:delegate:];
-[ULOdometryProvider startBackgroundUpdates];
-[ULOdometryProvider alignmentAngleBuffer];
-[ULOdometryProvider setAccumulatedAlignmentAngleErrorEstimateRad:];
-[ULOdometryProvider previousStatusUpdateDate];
-[ULOdometryProvider _updateAlignmentAngle];
-[ULOdometryProvider didReceiveOdometryUpdate:withError:];
-[ULOdometryProvider odometrySourceType];
-[ULOdometryProvider injectOdometryState:];
-[ULOdometryProvider setQueue:];
-[ULOdometryProvider setTrajectoryUUID:];
```

# `ULOdometryBridge`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ULOdometrySource`
- 4 instance variables, 9 properties, 14 instance methods, 6 class methods

## Instance variables

```
B _backgroudUpdatesRunning;
@"NSObject<OS_dispatch_queue>" _queue;
@"<ULOdometryDelegate>" _delegate;
@"CMOdometryManager" _odometryManager;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"<ULOdometryDelegate>",W,N,V_delegate) delegate;
@property (T@"CMOdometryManager",&,N,V_odometryManager) odometryManager;
@property (TB,N,V_backgroudUpdatesRunning) backgroudUpdatesRunning;
@property (Tq,R,N) odometrySourceType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULOdometryBridge referenceFrame];
+[ULOdometryBridge isBackgroundAvailable];
+[ULOdometryBridge isNeuralPDRAvailable];
+[ULOdometryBridge enableNeuralPDR];
+[ULOdometryBridge getNorthAlignmentAngleRadFrom:];
+[ULOdometryBridge northAlignmentErrorFrom:];
```

## Instance methods

```
-[ULOdometryBridge requestNPDRUpdate];
-[ULOdometryBridge queue];
-[ULOdometryBridge stopBackgroundUpdates];
-[ULOdometryBridge setDelegate:];
-[ULOdometryBridge delegate];
-[ULOdometryBridge startBackgroundUpdates];
-[ULOdometryBridge odometrySourceType];
-[ULOdometryBridge setQueue:];
-[ULOdometryBridge odometryManager];
-[ULOdometryBridge initWithDelegateQueue:delegate:];
-[ULOdometryBridge backgroudUpdatesRunning];
-[ULOdometryBridge handleOdometryMeasurement:error:];
-[ULOdometryBridge setBackgroudUpdatesRunning:];
-[ULOdometryBridge setOdometryManager:];
```

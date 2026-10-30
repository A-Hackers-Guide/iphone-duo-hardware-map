# `ULAttitudeBridge`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ULAttitudeSource`
- 6 instance variables, 10 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _updatesRunning;
@"NSObject<OS_dispatch_queue>" _queue;
@"<ULAttitudeDelegate>" _delegate;
@"CMMotionManager" _motionManager;
@"NSOperationQueue" _operationQueue;
d _updateInterval;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (T@"<ULAttitudeDelegate>",W,N,V_delegate) delegate;
@property (T@"CMMotionManager",&,N,V_motionManager) motionManager;
@property (T@"NSOperationQueue",&,N,V_operationQueue) operationQueue;
@property (TB,N,V_updatesRunning) updatesRunning;
@property (Td,N,V_updateInterval) updateInterval;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[ULAttitudeBridge isAvailable];
```

## Instance methods

```
-[ULAttitudeBridge queue];
-[ULAttitudeBridge stopUpdates];
-[ULAttitudeBridge setDelegate:];
-[ULAttitudeBridge setUpdateInterval:];
-[ULAttitudeBridge delegate];
-[ULAttitudeBridge operationQueue];
-[ULAttitudeBridge setOperationQueue:];
-[ULAttitudeBridge setQueue:];
-[ULAttitudeBridge updateInterval];
-[ULAttitudeBridge motionManager];
-[ULAttitudeBridge setMotionManager:];
-[ULAttitudeBridge startUpdates];
-[ULAttitudeBridge initWithQueue:delegate:updateInterval:bufferDurationSeconds:];
-[ULAttitudeBridge setUpdatesRunning:];
-[ULAttitudeBridge updatesRunning];
```

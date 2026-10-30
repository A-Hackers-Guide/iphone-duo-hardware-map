# `BLSHWaiterForBacklight`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightHostObserving`, `BSInvalidatable`
- 3 instance variables, 4 properties, 9 instance methods, 6 class methods

## Instance variables

```
@? _completion;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_invalidated;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHWaiterForBacklight waitForBacklightDisplayMode:];
+[BLSHWaiterForBacklight waitForBacklightDisplayModePassingTest:];
+[BLSHWaiterForBacklight waitForBacklightState:];
+[BLSHWaiterForBacklight waitForBacklightStatePassingTest:];
+[BLSHWaiterForBacklight waitForBlanked];
+[BLSHWaiterForBacklight waitForUnblanked];
```

## Instance methods

```
-[BLSHWaiterForBacklight init];
-[BLSHWaiterForBacklight dealloc];
-[BLSHWaiterForBacklight isInvalidated];
-[BLSHWaiterForBacklight invalidate];
-[BLSHWaiterForBacklight _main_callCompletion];
-[BLSHWaiterForBacklight _main_waitWithCompletion:];
-[BLSHWaiterForBacklight callCompletion];
-[BLSHWaiterForBacklight isAlreadyAtDesiredState];
-[BLSHWaiterForBacklight waitWithCompletion:];
```

# `BLSHSystemWakeWaiter`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SWSystemSleepObserver`, `BSInvalidatable`
- 9 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSString" _identifier;
@"<BLSHOSInterfaceProviding>" _osInterfaceProvider;
@? _lock_completion;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
Q _lock_waitStartTimestamp;
Q _lock_didWakeTimestamp;
B _lock_waiting;
B _lock_didCallCompletion;
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
+[BLSHSystemWakeWaiter waiterWithIdentifier:osInterfaceProvider:];
```

## Instance methods

```
-[BLSHSystemWakeWaiter systemSleepMonitorDidWakeFromSleep:];
-[BLSHSystemWakeWaiter dealloc];
-[BLSHSystemWakeWaiter invalidate];
-[BLSHSystemWakeWaiter _lock_invalidate];
-[BLSHSystemWakeWaiter initWithIdentifier:osInterfaceProvider:];
-[BLSHSystemWakeWaiter runWhenAwakeWithCompletion:];
```

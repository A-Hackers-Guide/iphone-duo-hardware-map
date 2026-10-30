# `BLSHSystemWaker`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 12 instance variables, 4 properties, 8 instance methods, 2 class methods

## Instance variables

```
@"NSString" _identifier;
@"<BLSHOSInterfaceProviding>" _osInterfaceProvider;
@"<BLSHSystemActivityAsserting>" _lock_systemActivity;
@"<BSTimerScheduleQuerying><BSCancellable><BSInvalidatable>" _lock_wakeWatchdogTimer;
@? _lock_completion;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
Q _lock_waitStartTimestamp;
Q _lock_didWakeTimestamp;
Q _stateHandler;
B _lock_waking;
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
+[BLSHSystemWaker sharedSystemActivityFactory];
+[BLSHSystemWaker wakerWithIdentifier:osInterfaceProvider:];
```

## Instance methods

```
-[BLSHSystemWaker dealloc];
-[BLSHSystemWaker invalidate];
-[BLSHSystemWaker description];
-[BLSHSystemWaker wakeWithCompletion:];
-[BLSHSystemWaker callCompletionForReason:];
-[BLSHSystemWaker initWithIdentifier:osInterfaceProvider:];
-[BLSHSystemWaker startWatchdogTimer];
-[BLSHSystemWaker watchdogTimerFired:];
```

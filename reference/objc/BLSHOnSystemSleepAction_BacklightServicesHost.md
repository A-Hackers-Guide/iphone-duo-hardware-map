# `BLSHOnSystemSleepAction`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SWSystemSleepObserver`, `BSInvalidatable`, `BSCancellable`
- 7 instance variables, 6 properties, 14 instance methods, 2 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BLSHOSInterfaceProviding>" _osInterfaceProvider;
@"<BLSHOnSystemSleepActionDelegate>" _delegate;
@? _lock_proceedWithSleepBlock;
d _lock_sleepRequestedTime;
q _lock_state;
@"NSString" _identifier;
```

## Properties

```
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (Tq,R,N) state;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHOnSystemSleepAction actionWithIdentifier:delegate:];
+[BLSHOnSystemSleepAction actionWithIdentifier:delegate:osInterfaceProvider:];
```

## Instance methods

```
-[BLSHOnSystemSleepAction systemSleepMonitor:prepareForSleepWithCompletion:];
-[BLSHOnSystemSleepAction uninstall];
-[BLSHOnSystemSleepAction identifier];
-[BLSHOnSystemSleepAction systemSleepMonitorWillWakeFromSleep:];
-[BLSHOnSystemSleepAction invalidate];
-[BLSHOnSystemSleepAction description];
-[BLSHOnSystemSleepAction cancel];
-[BLSHOnSystemSleepAction systemSleepMonitorSleepRequestAborted:];
-[BLSHOnSystemSleepAction state];
-[BLSHOnSystemSleepAction install];
-[BLSHOnSystemSleepAction systemSleepMonitor:sleepRequestedWithResult:];
-[BLSHOnSystemSleepAction actionCompleted];
-[BLSHOnSystemSleepAction initWithIdentifier:delegate:osInterfaceProvider:];
-[BLSHOnSystemSleepAction systemWillWakeForReason:];
```

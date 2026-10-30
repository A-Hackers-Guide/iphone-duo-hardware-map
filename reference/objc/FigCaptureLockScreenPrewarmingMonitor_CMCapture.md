# `FigCaptureLockScreenPrewarmingMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FigCaptureDisplayLayoutObserver`
- 15 instance variables, 4 properties, 2 instance methods, 3 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _notifyQueue;
i _biometricEnrollmentChangedToken;
B _haveEnrolledBiometricIdentities;
i _activeBiometricOperationChangedToken;
i _activeBiometricOperationType;
q _lastBiometricMatchCompleteTime;
@"NSDictionary" _mobileKeyBagOptions;
i _deviceLockStateChangedToken;
i _deviceLockState;
q _lastDeviceUnlockTime;
B _onLockScreen;
B _addingLayoutObserver;
B _observingLayoutChanges;
B _isPrewarming;
@"NSObject<OS_dispatch_source>" _delayedPrewarmTimer;
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
+[FigCaptureLockScreenPrewarmingMonitor initialize];
+[FigCaptureLockScreenPrewarmingMonitor stop];
+[FigCaptureLockScreenPrewarmingMonitor start];
```

## Instance methods

```
-[FigCaptureLockScreenPrewarmingMonitor layoutMonitor:didUpdateLayout:];
-[FigCaptureLockScreenPrewarmingMonitor dealloc];
```

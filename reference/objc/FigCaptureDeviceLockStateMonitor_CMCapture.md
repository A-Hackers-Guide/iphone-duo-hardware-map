# `FigCaptureDeviceLockStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 5 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _monitorQueue;
@"NSObject<OS_dispatch_queue>" _notificationQueue;
@"NSMutableArray" _deviceLockStateObservers;
i _deviceLockStateChangedToken;
@"NSDictionary" _mobileKeyBagOptions;
B _deviceIsLocked;
B _invalid;
```

## Class methods

```
+[FigCaptureDeviceLockStateMonitor initialize];
+[FigCaptureDeviceLockStateMonitor sharedDeviceLockStateMonitor];
```

## Instance methods

```
-[FigCaptureDeviceLockStateMonitor init];
-[FigCaptureDeviceLockStateMonitor dealloc];
-[FigCaptureDeviceLockStateMonitor addDeviceLockStateObserver:];
-[FigCaptureDeviceLockStateMonitor deviceIsLocked];
-[FigCaptureDeviceLockStateMonitor removeDeviceLockStateObserver:];
```

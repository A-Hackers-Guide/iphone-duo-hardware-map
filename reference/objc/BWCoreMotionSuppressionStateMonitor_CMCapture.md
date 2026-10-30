# `BWCoreMotionSuppressionStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"CMSuppressionManager" _suppressionManager;
i _suppressionState;
i _facedownState;
@"NSOperationQueue" _eventQueue;
@? _handler;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _monitoringStateLock;
B _isMonitoring;
```

## Class methods

```
+[BWCoreMotionSuppressionStateMonitor initialize];
```

## Instance methods

```
-[BWCoreMotionSuppressionStateMonitor stop];
-[BWCoreMotionSuppressionStateMonitor dealloc];
-[BWCoreMotionSuppressionStateMonitor start];
-[BWCoreMotionSuppressionStateMonitor initWithSuppressionStateChangeHandler:];
```

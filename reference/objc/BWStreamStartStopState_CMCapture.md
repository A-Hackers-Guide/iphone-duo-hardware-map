# `BWStreamStartStopState`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
i _state;
@"BWFigVideoCaptureStream" _stream;
@"NSObject<OS_dispatch_group>" _hasStartedGroup;
B _hasEnteredStartedGroup;
@"NSObject<OS_dispatch_group>" _dependentsHaveStoppedGroup;
@"BWStreamStartStopState" _blockingMasterState;
@"NSArray" _blockingSlaveStates;
f _timeoutInSeconds;
B _waitForMasterAEToSettle;
```

## Instance methods

```
-[BWStreamStartStopState dealloc];
-[BWStreamStartStopState description];
```

# `SBLockScreenStateCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _pendingRequests;
B _isProcessingRequest;
```

## Instance methods

```
-[SBLockScreenStateCoordinator _enqueueCoordinationRequest:];
-[SBLockScreenStateCoordinator _executeCoordinationRequest:];
-[SBLockScreenStateCoordinator _finalizeCoordinationRequestWithTargetLockScreenManager:];
-[SBLockScreenStateCoordinator _processRequestIfNeeded];
-[SBLockScreenStateCoordinator coordinateStateForActiveLockScreenManager:previousActiveManager:];
```

# `SBCaptureButtonSuppressionManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBCaptureButtonSuppressionEvent`, `SBDisplayContentModeTransitionObserver`
- 8 instance variables, 9 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"CMSuppressionManager" _suppressionManager;
@"NSHashTable" _observers;
q _suppressionState;
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
q _currentSurfaceType;
B _inCameraCapturePose;
Q _cameraCapturePoseType;
d _secondsAfterFaceDownAtUnsuppressionTime;
```

## Properties

```
@property (Tq,N,V_suppressionState) suppressionState;
@property (Td,N,V_secondsAfterFaceDownAtUnsuppressionTime) secondsAfterFaceDownAtUnsuppressionTime;
@property (TB,N,GisInCameraCapturePose,V_inCameraCapturePose) inCameraCapturePose;
@property (TQ,N,V_cameraCapturePoseType) cameraCapturePoseType;
@property (T@"SBCaptureButtonLowLatencyPose",R,N) lowLatencyPose;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCaptureButtonSuppressionManager initWithDisplayContentModeCoordinator:];
-[SBCaptureButtonSuppressionManager displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBCaptureButtonSuppressionManager dealloc];
-[SBCaptureButtonSuppressionManager displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBCaptureButtonSuppressionManager suppressionState];
-[SBCaptureButtonSuppressionManager _notifyObserversOfSuppressionState];
-[SBCaptureButtonSuppressionManager _reconfigureForSurfaceType:];
-[SBCaptureButtonSuppressionManager _subscribeToViewObstructedUpdatesForSurfaceType:];
-[SBCaptureButtonSuppressionManager _unsubscribeFromViewObstructedUpdates];
-[SBCaptureButtonSuppressionManager cameraCapturePoseType];
-[SBCaptureButtonSuppressionManager isInCameraCapturePose];
-[SBCaptureButtonSuppressionManager lowLatencyPose];
-[SBCaptureButtonSuppressionManager secondsAfterFaceDownAtUnsuppressionTime];
-[SBCaptureButtonSuppressionManager setCameraCapturePoseType:];
-[SBCaptureButtonSuppressionManager setInCameraCapturePose:];
-[SBCaptureButtonSuppressionManager setSecondsAfterFaceDownAtUnsuppressionTime:];
-[SBCaptureButtonSuppressionManager setSuppressionState:];
```

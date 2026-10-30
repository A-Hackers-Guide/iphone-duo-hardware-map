# `SBSensorAccessMinimumOnTimeProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFDevicePoseProviderObserver`, `SBSecureIndicatorMinimumOnTimeProvider`
- 12 instance variables, 7 properties, 35 instance methods, 2 class methods

## Instance variables

```
@"SBFDevicePoseProvider" _devicePoseProvider;
{?="orientation"q"coverOrientation"q"innerOrientation"q"hinge"{?="isAvailable"B"position"d"state"q"fullyClosedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"closedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"partiallyOpenRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"openFlatRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"activateFoldAvoidanceRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"transitionToOpenRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"transitionToClosedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"isTransitioning"B"transitionProgress"d"progressToSwap"d"progressFromSwap"d"continuousFoldPosition"d"velocity"d"acceleration"d}"uiHingeStatus"{?="isAvailable"B"status"q"magicPose"q"hingeAngle"d"nextStatus"q"progress"d"timestamp"d}"cmAngle"{?="minAngleDegrees"f"maxAngleDegrees"f"angleDegrees"f"velocityDegreesPerSeconds"f"isAvailable"B"timestamp"d}"cmMagicPose"{?="deviceOrientation"q"deviceOrientationForCover"q"deviceOrientationForInner"q"tabletopPose"q"hingeState"q"progressValid"B"fromHingeState"q"toHingeState"q"progressValue"d"isAvailable"B"timestamp"d}"flipState"{?="isAvailable"B"showYoinkingAffordance"B}"settings"{?="showDebugHUD"B"showDisplaySupport3Required"B"usesStrictCoreMotion"B"invertHingeAngles"B"continuousFoldEnabled"B"closedToPartiallyOpenBoundary"d"partiallyOpenToOpenFlatBoundary"d"openTransitionBeginBoundary"d"closeTransitionBeginBoundary"d"transitionAutoCompleteDuration"d"velocitySmoothingFactor"d"enterFoldAvoidancePredictionWindow"d"sustainFoldAvoidancePredictionWindow"d}"internal"{?="isInitialized"B"forceStrictCoreMotion"B"invertHingeAngles"B"isOnVM"B"isDisplaySupport3Set"B"hingeRegionsAreDefault"B"needsTransitionAutocompletion"B"transitionAutocompletionProgress"d"autocompleteStartTime"d"timestampOfLastTransitionProgressChange"d"transitionProgressWhenAutocompletionBegan"d"transitionSwapProgressWhenAutocompletionBegan"d"hingePositionWhenAutocompletionBegan"d}"displayTool"{?="state"q"duration"d"deviceOrientation"q"profileOverride"q"waitForCompletion"B"targetMode"q"targetHingePosition"d"lockedForTestingUntil"d}} _latestDevicePose;
q _requiredSurface;
@"NSHashTable" _secureDisplayObservers;
B _secureIndicatorRequired;
B _deviceStateQueryInFlight;
B _deviceStateQueryPending;
B _resolutionPendingDuringThrottle;
@"BSContinuousMachTimer" _throttleTimer;
@"BSContinuousMachTimer" _deviceStatePollTimer;
@? _deviceStateQuery;
@"NSObject<OS_dispatch_queue>" _deviceStateQueue;
```

## Properties

```
@property (T@?,C,N,V_deviceStateQuery) deviceStateQuery;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_deviceStateQueue) deviceStateQueue;
@property (Tq,R,N,V_requiredSurface) requiredSurface;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSensorAccessMinimumOnTimeProvider _remainingTimeToSatisfyMinimumOnTimeForIndicators:error:];
+[SBSensorAccessMinimumOnTimeProvider sharedSensorAccessIndicator];
```

## Instance methods

```
-[SBSensorAccessMinimumOnTimeProvider dealloc];
-[SBSensorAccessMinimumOnTimeProvider poseProvider:didUpdateFromPose:toPose:];
-[SBSensorAccessMinimumOnTimeProvider initWithDevicePoseProvider:];
-[SBSensorAccessMinimumOnTimeProvider _hasPendingDeviceStatePollTimer];
-[SBSensorAccessMinimumOnTimeProvider _querySurfaceFromDeviceStateSPI];
-[SBSensorAccessMinimumOnTimeProvider requiredSurface];
-[SBSensorAccessMinimumOnTimeProvider _continuousDeviceStatePollEnabled];
-[SBSensorAccessMinimumOnTimeProvider _devicePoseIsFullyClosed];
-[SBSensorAccessMinimumOnTimeProvider _deviceStatePollEnabled];
-[SBSensorAccessMinimumOnTimeProvider _deviceStatePollInterval];
-[SBSensorAccessMinimumOnTimeProvider _evaluateDeviceStatePoll];
-[SBSensorAccessMinimumOnTimeProvider _handleDeviceStatePollFired];
-[SBSensorAccessMinimumOnTimeProvider _handleDeviceStateQueryDidCompleteWithSurface:];
-[SBSensorAccessMinimumOnTimeProvider _handleThrottleWindowElapsed];
-[SBSensorAccessMinimumOnTimeProvider _hasActiveThrottleWindow];
-[SBSensorAccessMinimumOnTimeProvider _isThrottleWorthyPoseChangeFromPose:toPose:];
-[SBSensorAccessMinimumOnTimeProvider _meaningfulPoseChangesFromPose:toPose:];
-[SBSensorAccessMinimumOnTimeProvider _notePoseChangeThrottled];
-[SBSensorAccessMinimumOnTimeProvider _openThrottleWindow];
-[SBSensorAccessMinimumOnTimeProvider _poseGateSatisfiedForDeviceStatePoll];
-[SBSensorAccessMinimumOnTimeProvider _poseThrottleInterval];
-[SBSensorAccessMinimumOnTimeProvider _refreshRequiredSurfaceFromDeviceState];
-[SBSensorAccessMinimumOnTimeProvider _resolveRequiredSurfaceForCurrentState];
-[SBSensorAccessMinimumOnTimeProvider _setRequiredSurface:forceObserverNotification:];
-[SBSensorAccessMinimumOnTimeProvider _shouldPollDeviceState];
-[SBSensorAccessMinimumOnTimeProvider _startDeviceStatePollTimer];
-[SBSensorAccessMinimumOnTimeProvider addSecureDisplayObserver:];
-[SBSensorAccessMinimumOnTimeProvider deviceStateQuery];
-[SBSensorAccessMinimumOnTimeProvider deviceStateQueue];
-[SBSensorAccessMinimumOnTimeProvider remainingTimeToSatisfyMinimumOnTimeForIndicators:error:];
-[SBSensorAccessMinimumOnTimeProvider remainingTimeToSteadyForLayer:display:];
-[SBSensorAccessMinimumOnTimeProvider removeSecureDisplayObserver:];
-[SBSensorAccessMinimumOnTimeProvider setDeviceStateQuery:];
-[SBSensorAccessMinimumOnTimeProvider setDeviceStateQueue:];
-[SBSensorAccessMinimumOnTimeProvider setSecureIndicatorRequired:];
```

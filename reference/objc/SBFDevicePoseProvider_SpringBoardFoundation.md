# `SBFDevicePoseProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSAccelerometerDelegate`, `PTSettingsKeyPathObserver`, `BSInvalidatable`
- 19 instance variables, 7 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"BKSAccelerometer" _accelerometer;
@"CMAngleManager" _cmAngleManager;
@"CMMagicPoseManager" _cmMagicPoseManager;
{?="devicePose"{?="orientation"q"coverOrientation"q"innerOrientation"q"hinge"{?="isAvailable"B"position"d"state"q"fullyClosedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"closedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"partiallyOpenRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"openFlatRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"activateFoldAvoidanceRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"transitionToOpenRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"transitionToClosedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"isTransitioning"B"transitionProgress"d"progressToSwap"d"progressFromSwap"d"continuousFoldPosition"d"velocity"d"acceleration"d}"uiHingeStatus"{?="isAvailable"B"status"q"magicPose"q"hingeAngle"d"nextStatus"q"progress"d"timestamp"d}"cmAngle"{?="minAngleDegrees"f"maxAngleDegrees"f"angleDegrees"f"velocityDegreesPerSeconds"f"isAvailable"B"timestamp"d}"cmMagicPose"{?="deviceOrientation"q"deviceOrientationForCover"q"deviceOrientationForInner"q"tabletopPose"q"hingeState"q"progressValid"B"fromHingeState"q"toHingeState"q"progressValue"d"isAvailable"B"timestamp"d}"flipState"{?="isAvailable"B"showYoinkingAffordance"B}"settings"{?="showDebugHUD"B"showDisplaySupport3Required"B"usesStrictCoreMotion"B"invertHingeAngles"B"continuousFoldEnabled"B"closedToPartiallyOpenBoundary"d"partiallyOpenToOpenFlatBoundary"d"openTransitionBeginBoundary"d"closeTransitionBeginBoundary"d"transitionAutoCompleteDuration"d"velocitySmoothingFactor"d"enterFoldAvoidancePredictionWindow"d"sustainFoldAvoidancePredictionWindow"d}"internal"{?="isInitialized"B"forceStrictCoreMotion"B"invertHingeAngles"B"isOnVM"B"isDisplaySupport3Set"B"hingeRegionsAreDefault"B"needsTransitionAutocompletion"B"transitionAutocompletionProgress"d"autocompleteStartTime"d"timestampOfLastTransitionProgressChange"d"transitionProgressWhenAutocompletionBegan"d"transitionSwapProgressWhenAutocompletionBegan"d"hingePositionWhenAutocompletionBegan"d}"displayTool"{?="state"q"duration"d"deviceOrientation"q"profileOverride"q"waitForCompletion"B"targetMode"q"targetHingePosition"d"lockedForTestingUntil"d}}"mechanicalAngleDegrees"d"autocompletionMinDelay"d"autocompletionMaxDelay"d"likelyToOpenVelocityDegreesPerSecond"d"swapDegreesForContinuousLiveStyle"d"swapDegreesForContinuousSnapshotStyleWhenOpening"d"swapDegreesForContinuousSnapshotStyleWhenClosing"d"swapDegreesForFadeInFadeOutStyle"d"transitionStyle"q"autocompletionDelay"d"continuousFoldEffectProgress"d"continuousFoldEffectSettlingTarget"d"continuousFoldEffectIsSettling"B} _lock_devicePoseBox;
{?="devicePose"{?="orientation"q"coverOrientation"q"innerOrientation"q"hinge"{?="isAvailable"B"position"d"state"q"fullyClosedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"closedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"partiallyOpenRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"openFlatRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"activateFoldAvoidanceRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"transitionToOpenRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"transitionToClosedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"isTransitioning"B"transitionProgress"d"progressToSwap"d"progressFromSwap"d"continuousFoldPosition"d"velocity"d"acceleration"d}"uiHingeStatus"{?="isAvailable"B"status"q"magicPose"q"hingeAngle"d"nextStatus"q"progress"d"timestamp"d}"cmAngle"{?="minAngleDegrees"f"maxAngleDegrees"f"angleDegrees"f"velocityDegreesPerSeconds"f"isAvailable"B"timestamp"d}"cmMagicPose"{?="deviceOrientation"q"deviceOrientationForCover"q"deviceOrientationForInner"q"tabletopPose"q"hingeState"q"progressValid"B"fromHingeState"q"toHingeState"q"progressValue"d"isAvailable"B"timestamp"d}"flipState"{?="isAvailable"B"showYoinkingAffordance"B}"settings"{?="showDebugHUD"B"showDisplaySupport3Required"B"usesStrictCoreMotion"B"invertHingeAngles"B"continuousFoldEnabled"B"closedToPartiallyOpenBoundary"d"partiallyOpenToOpenFlatBoundary"d"openTransitionBeginBoundary"d"closeTransitionBeginBoundary"d"transitionAutoCompleteDuration"d"velocitySmoothingFactor"d"enterFoldAvoidancePredictionWindow"d"sustainFoldAvoidancePredictionWindow"d}"internal"{?="isInitialized"B"forceStrictCoreMotion"B"invertHingeAngles"B"isOnVM"B"isDisplaySupport3Set"B"hingeRegionsAreDefault"B"needsTransitionAutocompletion"B"transitionAutocompletionProgress"d"autocompleteStartTime"d"timestampOfLastTransitionProgressChange"d"transitionProgressWhenAutocompletionBegan"d"transitionSwapProgressWhenAutocompletionBegan"d"hingePositionWhenAutocompletionBegan"d}"displayTool"{?="state"q"duration"d"deviceOrientation"q"profileOverride"q"waitForCompletion"B"targetMode"q"targetHingePosition"d"lockedForTestingUntil"d}}"mechanicalAngleDegrees"d"autocompletionMinDelay"d"autocompletionMaxDelay"d"likelyToOpenVelocityDegreesPerSecond"d"swapDegreesForContinuousLiveStyle"d"swapDegreesForContinuousSnapshotStyleWhenOpening"d"swapDegreesForContinuousSnapshotStyleWhenClosing"d"swapDegreesForFadeInFadeOutStyle"d"transitionStyle"q"autocompletionDelay"d"continuousFoldEffectProgress"d"continuousFoldEffectSettlingTarget"d"continuousFoldEffectIsSettling"B} _lock_currentDevicePoseBox;
B _lock_observersNeedUpdate;
B _lock_hasHingeAngleHUDViews;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSOperationQueue" _cmUpdateQueue;
@"NSHashTable" _observers;
@"NSHashTable" _hingeAngleHUDViews;
@"UIUpdateLink" _heartbeat;
@"UIWindowScene" _heartbeatSource;
d _lastNotificationTimestamp;
@"SBFDevicePosePTSettings" _settings;
B _isInvalidated;
@"SBFInstrumentationEmitter" _instrumentationEmitter;
@"<BSInvalidatable>" _stateCaptureHandle;
@"<SBFDevicePoseLikelyTransitionDelegate>" _likelyTransitionDelegate;
```

## Properties

```
@property (TB,R,N,GisContinuousFoldEnabled) continuousFoldEnabled;
@property (T@"SBFInstrumentationEmitter",R,N) instrumentationEmitter;
@property (T@"<SBFDevicePoseLikelyTransitionDelegate>",W,N,V_likelyTransitionDelegate) likelyTransitionDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFDevicePoseProvider removeObserver:];
-[SBFDevicePoseProvider init];
-[SBFDevicePoseProvider dealloc];
-[SBFDevicePoseProvider accelerometer:didChangeDeviceOrientation:];
-[SBFDevicePoseProvider addObserver:];
-[SBFDevicePoseProvider invalidate];
-[SBFDevicePoseProvider description];
-[SBFDevicePoseProvider accelerometer:didAccelerateWithTimeStamp:x:y:z:eventType:];
-[SBFDevicePoseProvider setTransitionStyle:];
-[SBFDevicePoseProvider settings:changedValueForKeyPath:];
-[SBFDevicePoseProvider initWithInstrumentationEmitter:];
-[SBFDevicePoseProvider _beginTransitionAutocompletion];
-[SBFDevicePoseProvider _cmUpdateQueue];
-[SBFDevicePoseProvider _handleAngle:];
-[SBFDevicePoseProvider _publishedMechanicalAngleDegreesForAngle:];
-[SBFDevicePoseProvider _updateDevicePoseBoxForReason:usingBlock:];
-[SBFDevicePoseProvider _updateInitialPoseUsingBlock:];
-[SBFDevicePoseProvider continuousFoldEffectProgress];
-[SBFDevicePoseProvider currentBox];
-[SBFDevicePoseProvider currentPose];
-[SBFDevicePoseProvider instrumentationEmitter];
-[SBFDevicePoseProvider isContinuousFoldEnabled];
-[SBFDevicePoseProvider likelyTransitionDelegate];
-[SBFDevicePoseProvider makeHingeAngleHUDView];
-[SBFDevicePoseProvider setDisplayToolProfileOverride:];
-[SBFDevicePoseProvider setLikelyTransitionDelegate:];
-[SBFDevicePoseProvider setUpdateLinkSource:backlightActive:];
-[SBFDevicePoseProvider updateDevicePoseForReason:usingBlock:];
```

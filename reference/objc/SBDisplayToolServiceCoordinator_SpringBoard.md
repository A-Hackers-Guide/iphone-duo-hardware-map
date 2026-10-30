# `SBDisplayToolServiceCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayContentModeTransitionObserver`
- 18 instance variables, 4 properties, 56 instance methods, 0 class methods

## Instance variables

```
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@"SBFDevicePoseProvider" _devicePoseProvider;
@"SBDisplayYoinkingCoordinator" _displayYoinkingCoordinator;
@"SBWindowSceneManager" _windowSceneManager;
@"<BSInvalidatable>" _yoinkActivationAssertion;
{?="state"q"duration"d"deviceOrientation"q"profileOverride"q"waitForCompletion"B"targetMode"q"targetHingePosition"d"lockedForTestingUntil"d} _currentSettings;
q _currentDirection;
@? _currentSwapCompletion;
@? _replaySetupCompletion;
@? _replaySweepSettled;
B _replaySweepTransitionEnded;
B _replayIsRunning;
B _instantSwapIsRunning;
B _instantSwapTransitionBegan;
@"NSObject<OS_dispatch_source>" _testLockExpiryTimer;
@"NSObject<OS_dispatch_source>" _yoinkingFlipOverrideExpiryTimer;
@"<BSInvalidatable>" _testLockMarkPersistenceAssertion;
@"<BSInvalidatable>" _requestedMarkPersistenceAssertion;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDisplayToolServiceCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBDisplayToolServiceCoordinator dealloc];
-[SBDisplayToolServiceCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBDisplayToolServiceCoordinator _transitionToIdle];
-[SBDisplayToolServiceCoordinator _afterSettingUp];
-[SBDisplayToolServiceCoordinator _releaseTestLockMarkPersistence];
-[SBDisplayToolServiceCoordinator _bundleIdentifiersInLayoutState];
-[SBDisplayToolServiceCoordinator _afterSweepSettles:];
-[SBDisplayToolServiceCoordinator _applicationForSystemSpace:];
-[SBDisplayToolServiceCoordinator _awaitArrivalIn:windowScene:deadline:reached:completion:];
-[SBDisplayToolServiceCoordinator _cancelTestLockExpiryTimer];
-[SBDisplayToolServiceCoordinator _cancelYoinkingFlipOverrideExpiryTimer];
-[SBDisplayToolServiceCoordinator _dismissLockScreenOnWindowScene:completion:];
-[SBDisplayToolServiceCoordinator _driveToStartPoseForLoop:settings:completion:];
-[SBDisplayToolServiceCoordinator _driveToSystemSpace:windowScene:completion:];
-[SBDisplayToolServiceCoordinator _finishReplaySetup];
-[SBDisplayToolServiceCoordinator _interLoopGapForSettings:];
-[SBDisplayToolServiceCoordinator _isDeviceInBaseOfSystemSpace:windowScene:];
-[SBDisplayToolServiceCoordinator _isOverlayPresentedForSystemSpace:windowScene:];
-[SBDisplayToolServiceCoordinator _layoutStateHoldsApplicationOfSystemSpace:];
-[SBDisplayToolServiceCoordinator _noteSweepTransitionEnded];
-[SBDisplayToolServiceCoordinator _playRun:settings:completion:];
-[SBDisplayToolServiceCoordinator _playSamples:completion:];
-[SBDisplayToolServiceCoordinator _presentOverlayForSystemSpace:windowScene:deadline:completion:];
-[SBDisplayToolServiceCoordinator _publishedStateDescriptionForWindowScene:];
-[SBDisplayToolServiceCoordinator _pushCurrentSettingsThroughPose:];
-[SBDisplayToolServiceCoordinator _reasonSystemSpaceCannotBeRequested:windowScene:];
-[SBDisplayToolServiceCoordinator _replayLoop:fromSamples:settings:remaining:completion:];
-[SBDisplayToolServiceCoordinator _replayLoopsFromSamples:settings:remaining:completion:];
-[SBDisplayToolServiceCoordinator _replaySweep:loopIdentifier:band:completion:];
-[SBDisplayToolServiceCoordinator _requestBaseOfSystemSpace:windowScene:];
-[SBDisplayToolServiceCoordinator _rescheduleTestLockExpiryAt:];
-[SBDisplayToolServiceCoordinator _rescheduleYoinkingFlipOverrideExpiryAt:];
-[SBDisplayToolServiceCoordinator _resetToHomeScreenOnWindowScene:completion:];
-[SBDisplayToolServiceCoordinator _resetToIdleWithReason:];
-[SBDisplayToolServiceCoordinator _resolveSwapDirection];
-[SBDisplayToolServiceCoordinator _runAngleTimerFromAngle:toAngle:duration:timingFunction:completion:];
-[SBDisplayToolServiceCoordinator _runForSettings:path:error:];
-[SBDisplayToolServiceCoordinator _setDisplayPrewarmDuration:reason:];
-[SBDisplayToolServiceCoordinator _sweepStartAngle];
-[SBDisplayToolServiceCoordinator _systemSpaceError:description:];
-[SBDisplayToolServiceCoordinator _transitionToAbsoluteSweeping];
-[SBDisplayToolServiceCoordinator _transitionToCompleted];
-[SBDisplayToolServiceCoordinator _transitionToPreparing:];
-[SBDisplayToolServiceCoordinator _transitionToSettingUp];
-[SBDisplayToolServiceCoordinator _transitionToSwapping];
-[SBDisplayToolServiceCoordinator _transitionToWaitingForDisplayTransition];
-[SBDisplayToolServiceCoordinator awaitSystemSpace:completion:];
-[SBDisplayToolServiceCoordinator disableYoinkingFlipOverride];
-[SBDisplayToolServiceCoordinator enableYoinkingFlipOverrideForDuration:];
-[SBDisplayToolServiceCoordinator initWithDisplayContentModeCoordinator:devicePoseProvider:windowSceneManager:displayYoinkingCoordinator:];
-[SBDisplayToolServiceCoordinator lockForTesting];
-[SBDisplayToolServiceCoordinator performDisplaySwapWithSettings:completion:];
-[SBDisplayToolServiceCoordinator performHingeReplayWithSettings:samplesPath:completion:];
-[SBDisplayToolServiceCoordinator setDynamicMarkPersistenceEnabled:];
-[SBDisplayToolServiceCoordinator unlockForTesting];
```

# `SBSceneRegionsUpdater`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `PTSettingsKeyObserver`, `SDUDisplayRegionBlankingObserver`, `SBDeviceApplicationSceneStatusBarStateObserver`, `SBFDevicePoseProviderObserver`, `SBFStatusBarManagerObserver`, `SBLayoutStateTransitionObserver`, `BSInvalidatable`
- 15 instance variables, 9 properties, 42 instance methods, 0 class methods

## Instance variables

```
B _innerCameraRegionBlanked;
B _statusBarHidden;
B _invalidated;
q _statusBarAxis;
@"SBWindowScene" _windowScene;
@"FBScene" _scene;
@"SBSystemAnimationSettings" _systemAnimationSettings;
{?="orientation"q"coverOrientation"q"innerOrientation"q"hinge"{?="isAvailable"B"position"d"state"q"fullyClosedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"closedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"partiallyOpenRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"openFlatRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"activateFoldAvoidanceRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"transitionToOpenRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"transitionToClosedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"isTransitioning"B"transitionProgress"d"progressToSwap"d"progressFromSwap"d"continuousFoldPosition"d"velocity"d"acceleration"d}"uiHingeStatus"{?="isAvailable"B"status"q"magicPose"q"hingeAngle"d"nextStatus"q"progress"d"timestamp"d}"cmAngle"{?="minAngleDegrees"f"maxAngleDegrees"f"angleDegrees"f"velocityDegreesPerSeconds"f"isAvailable"B"timestamp"d}"cmMagicPose"{?="deviceOrientation"q"deviceOrientationForCover"q"deviceOrientationForInner"q"tabletopPose"q"hingeState"q"progressValid"B"fromHingeState"q"toHingeState"q"progressValue"d"isAvailable"B"timestamp"d}"flipState"{?="isAvailable"B"showYoinkingAffordance"B}"settings"{?="showDebugHUD"B"showDisplaySupport3Required"B"usesStrictCoreMotion"B"invertHingeAngles"B"continuousFoldEnabled"B"closedToPartiallyOpenBoundary"d"partiallyOpenToOpenFlatBoundary"d"openTransitionBeginBoundary"d"closeTransitionBeginBoundary"d"transitionAutoCompleteDuration"d"velocitySmoothingFactor"d"enterFoldAvoidancePredictionWindow"d"sustainFoldAvoidancePredictionWindow"d}"internal"{?="isInitialized"B"forceStrictCoreMotion"B"invertHingeAngles"B"isOnVM"B"isDisplaySupport3Set"B"hingeRegionsAreDefault"B"needsTransitionAutocompletion"B"transitionAutocompletionProgress"d"autocompleteStartTime"d"timestampOfLastTransitionProgressChange"d"transitionProgressWhenAutocompletionBegan"d"transitionSwapProgressWhenAutocompletionBegan"d"hingePositionWhenAutocompletionBegan"d}"displayTool"{?="state"q"duration"d"deviceOrientation"q"profileOverride"q"waitForCompletion"B"targetMode"q"targetHingePosition"d"lockedForTestingUntil"d}} _lastReportedPose;
@"SBFDevicePoseProvider" _devicePoseProvider;
B _isObservingDevicePose;
@"NSArray" _lastSentSceneRegions;
B _isForeground;
B _allowsSceneRegionUpdatesInBackground;
@"SBSceneRegionsSettings" _sceneRegionsSettings;
@"SBDeviceApplicationSceneStatusBarStateProvider" _observedStatusBarStateProvider;
```

## Properties

```
@property (T@"SBSceneRegionsSettings",&,N,V_sceneRegionsSettings) sceneRegionsSettings;
@property (T@"SBDeviceApplicationSceneStatusBarStateProvider",&,N,V_observedStatusBarStateProvider) observedStatusBarStateProvider;
@property (T@"SBWindowScene",W,N) windowScene;
@property (TB,R,N) isValid;
@property (TB,N,V_allowsSceneRegionUpdatesInBackground) allowsSceneRegionUpdatesInBackground;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSceneRegionsUpdater statusBarManager:didUpdateAvoidanceFrameForStatusBar:withAnimationSettings:];
-[SBSceneRegionsUpdater statusBarManager:didUpdateOcclusionFrameForStatusBar:];
-[SBSceneRegionsUpdater sceneWithIdentifier:didChangeStatusBarAlphaTo:];
-[SBSceneRegionsUpdater setWindowScene:];
-[SBSceneRegionsUpdater sceneDidInvalidate:withContext:];
-[SBSceneRegionsUpdater _scene];
-[SBSceneRegionsUpdater scene:didUpdateSettings:];
-[SBSceneRegionsUpdater dealloc];
-[SBSceneRegionsUpdater settings:changedValueForKey:];
-[SBSceneRegionsUpdater poseProvider:didUpdateFromPose:toPose:];
-[SBSceneRegionsUpdater invalidate];
-[SBSceneRegionsUpdater layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBSceneRegionsUpdater isValid];
-[SBSceneRegionsUpdater windowScene];
-[SBSceneRegionsUpdater sceneWithIdentifier:didChangeStatusBarHiddenTo:withAnimation:];
-[SBSceneRegionsUpdater _isClassic];
-[SBSceneRegionsUpdater blankingStateDidChange:forDisplayRegion:onWindowScene:forBundleIDs:];
-[SBSceneRegionsUpdater blankingStateWillChange:forDisplayRegion:onWindowScene:forBundleIDs:];
-[SBSceneRegionsUpdater _computeSceneRegionsForPose:settings:animationSettings:];
-[SBSceneRegionsUpdater _localFrameForRegionFrame:settings:outLocalFrame:];
-[SBSceneRegionsUpdater _reevaluateStatusBar];
-[SBSceneRegionsUpdater _relevantSceneHandle];
-[SBSceneRegionsUpdater _sceneFrameForSettings:];
-[SBSceneRegionsUpdater _sceneFrameToReferenceSpaceTransformForSettings:];
-[SBSceneRegionsUpdater _shouldAddFullScreenAppOnlySceneRegions];
-[SBSceneRegionsUpdater _statusBarOcclusionFrame];
-[SBSceneRegionsUpdater _updateHingeStatusWithPose:settings:];
-[SBSceneRegionsUpdater _updateObservingDevicePose];
-[SBSceneRegionsUpdater _updateObservingDevicePoseWithSettings:];
-[SBSceneRegionsUpdater allowsSceneRegionUpdatesInBackground];
-[SBSceneRegionsUpdater initWithHostScene:devicePoseProvider:];
-[SBSceneRegionsUpdater initWithWindowScene:devicePoseProvider:];
-[SBSceneRegionsUpdater observedStatusBarStateProvider];
-[SBSceneRegionsUpdater sceneRegionsSettings];
-[SBSceneRegionsUpdater sceneWithIdentifier:didChangeStatusBarAxisTo:withAnimationParameters:];
-[SBSceneRegionsUpdater setAllowsSceneRegionUpdatesInBackground:];
-[SBSceneRegionsUpdater setObservedStatusBarStateProvider:];
-[SBSceneRegionsUpdater setSceneRegionsSettings:];
-[SBSceneRegionsUpdater updateSceneRegionsAnimated:];
-[SBSceneRegionsUpdater updateSceneRegionsAnimated:pose:];
-[SBSceneRegionsUpdater updateSceneRegionsAnimated:pose:settings:];
-[SBSceneRegionsUpdater updateSceneRegionsAnimated:settings:];
```

# `_SBFInFlightPoseUpdate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _started;
B _completed;
B _wasInteresting;
S _updateType;
Q _poseId;
Q _startMCT;
@"NSNumber" _enqueuedMCT;
{?="orientation"q"coverOrientation"q"innerOrientation"q"hinge"{?="isAvailable"B"position"d"state"q"fullyClosedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"closedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"partiallyOpenRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"openFlatRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"activateFoldAvoidanceRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"transitionToOpenRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"transitionToClosedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"isTransitioning"B"transitionProgress"d"progressToSwap"d"progressFromSwap"d"continuousFoldPosition"d"velocity"d"acceleration"d}"uiHingeStatus"{?="isAvailable"B"status"q"magicPose"q"hingeAngle"d"nextStatus"q"progress"d"timestamp"d}"cmAngle"{?="minAngleDegrees"f"maxAngleDegrees"f"angleDegrees"f"velocityDegreesPerSeconds"f"isAvailable"B"timestamp"d}"cmMagicPose"{?="deviceOrientation"q"deviceOrientationForCover"q"deviceOrientationForInner"q"tabletopPose"q"hingeState"q"progressValid"B"fromHingeState"q"toHingeState"q"progressValue"d"isAvailable"B"timestamp"d}"flipState"{?="isAvailable"B"showYoinkingAffordance"B}"settings"{?="showDebugHUD"B"showDisplaySupport3Required"B"usesStrictCoreMotion"B"invertHingeAngles"B"continuousFoldEnabled"B"closedToPartiallyOpenBoundary"d"partiallyOpenToOpenFlatBoundary"d"openTransitionBeginBoundary"d"closeTransitionBeginBoundary"d"transitionAutoCompleteDuration"d"velocitySmoothingFactor"d"enterFoldAvoidancePredictionWindow"d"sustainFoldAvoidancePredictionWindow"d}"internal"{?="isInitialized"B"forceStrictCoreMotion"B"invertHingeAngles"B"isOnVM"B"isDisplaySupport3Set"B"hingeRegionsAreDefault"B"needsTransitionAutocompletion"B"transitionAutocompletionProgress"d"autocompleteStartTime"d"timestampOfLastTransitionProgressChange"d"transitionProgressWhenAutocompletionBegan"d"transitionSwapProgressWhenAutocompletionBegan"d"hingePositionWhenAutocompletionBegan"d}"displayTool"{?="state"q"duration"d"deviceOrientation"q"profileOverride"q"waitForCompletion"B"targetMode"q"targetHingePosition"d"lockedForTestingUntil"d}} _previous;
{?="orientation"q"coverOrientation"q"innerOrientation"q"hinge"{?="isAvailable"B"position"d"state"q"fullyClosedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"closedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"partiallyOpenRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"openFlatRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"activateFoldAvoidanceRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"transitionToOpenRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"transitionToClosedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"isTransitioning"B"transitionProgress"d"progressToSwap"d"progressFromSwap"d"continuousFoldPosition"d"velocity"d"acceleration"d}"uiHingeStatus"{?="isAvailable"B"status"q"magicPose"q"hingeAngle"d"nextStatus"q"progress"d"timestamp"d}"cmAngle"{?="minAngleDegrees"f"maxAngleDegrees"f"angleDegrees"f"velocityDegreesPerSeconds"f"isAvailable"B"timestamp"d}"cmMagicPose"{?="deviceOrientation"q"deviceOrientationForCover"q"deviceOrientationForInner"q"tabletopPose"q"hingeState"q"progressValid"B"fromHingeState"q"toHingeState"q"progressValue"d"isAvailable"B"timestamp"d}"flipState"{?="isAvailable"B"showYoinkingAffordance"B}"settings"{?="showDebugHUD"B"showDisplaySupport3Required"B"usesStrictCoreMotion"B"invertHingeAngles"B"continuousFoldEnabled"B"closedToPartiallyOpenBoundary"d"partiallyOpenToOpenFlatBoundary"d"openTransitionBeginBoundary"d"closeTransitionBeginBoundary"d"transitionAutoCompleteDuration"d"velocitySmoothingFactor"d"enterFoldAvoidancePredictionWindow"d"sustainFoldAvoidancePredictionWindow"d}"internal"{?="isInitialized"B"forceStrictCoreMotion"B"invertHingeAngles"B"isOnVM"B"isDisplaySupport3Set"B"hingeRegionsAreDefault"B"needsTransitionAutocompletion"B"transitionAutocompletionProgress"d"autocompleteStartTime"d"timestampOfLastTransitionProgressChange"d"transitionProgressWhenAutocompletionBegan"d"transitionSwapProgressWhenAutocompletionBegan"d"hingePositionWhenAutocompletionBegan"d}"displayTool"{?="state"q"duration"d"deviceOrientation"q"profileOverride"q"waitForCompletion"B"targetMode"q"targetHingePosition"d"lockedForTestingUntil"d}} _updated;
```

## Properties

```
@property (TQ,R,N,V_poseId) poseId;
@property (TQ,R,N,V_startMCT) startMCT;
@property (T{?=qqq{?=Bdq{?=ddBB}{?=ddBB}{?=ddBB}{?=ddBB}{?=ddBB}{?=ddBB}{?=ddBB}Bdddddd}{?=Bqqdqdd}{?=ffffBd}{?=qqqqqBqqdBd}{?=BB}{?=BBBBBdddddddd}{?=BBBBBBBdddddd}{?=qdqqBqdd}},R,N,V_previous) previous;
@property (T{?=qqq{?=Bdq{?=ddBB}{?=ddBB}{?=ddBB}{?=ddBB}{?=ddBB}{?=ddBB}{?=ddBB}Bdddddd}{?=Bqqdqdd}{?=ffffBd}{?=qqqqqBqqdBd}{?=BB}{?=BBBBBdddddddd}{?=BBBBBBBdddddd}{?=qdqqBqdd}},R,N,V_updated) updated;
@property (TB,R,N,V_wasInteresting) wasInteresting;
@property (TS,N,V_updateType) updateType;
@property (T@"NSNumber",R,N,V_enqueuedMCT) enqueuedMCT;
```

## Instance methods

```
-[_SBFInFlightPoseUpdate setUpdateType:];
-[_SBFInFlightPoseUpdate previous];
-[_SBFInFlightPoseUpdate updated];
-[_SBFInFlightPoseUpdate updateType];
-[_SBFInFlightPoseUpdate enqueuedMCT];
-[_SBFInFlightPoseUpdate initWithEnqueuedMCT:previousPose:updatedPose:];
-[_SBFInFlightPoseUpdate markAsInteresting];
-[_SBFInFlightPoseUpdate markCompleted:];
-[_SBFInFlightPoseUpdate markStarted];
-[_SBFInFlightPoseUpdate poseId];
-[_SBFInFlightPoseUpdate startMCT];
-[_SBFInFlightPoseUpdate wasInteresting];
```

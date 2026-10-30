# `SBFResolvedDisplayContentMode`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`
- 6 instance variables, 7 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _targetModesByIdentifier;
@"NSDictionary" _resolvedModesByIdentifier;
@"NSDictionary" _swapsContentModeByIdentifier;
@"SBFDisplayContentModeResolutionPolicy" _prevailingPolicy;
@"NSArray" _displayProxies;
{?="orientation"q"coverOrientation"q"innerOrientation"q"hinge"{?="isAvailable"B"position"d"state"q"fullyClosedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"closedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"partiallyOpenRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"openFlatRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"activateFoldAvoidanceRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"transitionToOpenRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"transitionToClosedRegion"{?="start"d"end"d"isActive"B"canBecomeActive"B}"isTransitioning"B"transitionProgress"d"progressToSwap"d"progressFromSwap"d"continuousFoldPosition"d"velocity"d"acceleration"d}"uiHingeStatus"{?="isAvailable"B"status"q"magicPose"q"hingeAngle"d"nextStatus"q"progress"d"timestamp"d}"cmAngle"{?="minAngleDegrees"f"maxAngleDegrees"f"angleDegrees"f"velocityDegreesPerSeconds"f"isAvailable"B"timestamp"d}"cmMagicPose"{?="deviceOrientation"q"deviceOrientationForCover"q"deviceOrientationForInner"q"tabletopPose"q"hingeState"q"progressValid"B"fromHingeState"q"toHingeState"q"progressValue"d"isAvailable"B"timestamp"d}"flipState"{?="isAvailable"B"showYoinkingAffordance"B}"settings"{?="showDebugHUD"B"showDisplaySupport3Required"B"usesStrictCoreMotion"B"invertHingeAngles"B"continuousFoldEnabled"B"closedToPartiallyOpenBoundary"d"partiallyOpenToOpenFlatBoundary"d"openTransitionBeginBoundary"d"closeTransitionBeginBoundary"d"transitionAutoCompleteDuration"d"velocitySmoothingFactor"d"enterFoldAvoidancePredictionWindow"d"sustainFoldAvoidancePredictionWindow"d}"internal"{?="isInitialized"B"forceStrictCoreMotion"B"invertHingeAngles"B"isOnVM"B"isDisplaySupport3Set"B"hingeRegionsAreDefault"B"needsTransitionAutocompletion"B"transitionAutocompletionProgress"d"autocompleteStartTime"d"timestampOfLastTransitionProgressChange"d"transitionProgressWhenAutocompletionBegan"d"transitionSwapProgressWhenAutocompletionBegan"d"hingePositionWhenAutocompletionBegan"d}"displayTool"{?="state"q"duration"d"deviceOrientation"q"profileOverride"q"waitForCompletion"B"targetMode"q"targetHingePosition"d"lockedForTestingUntil"d}} _devicePose;
```

## Properties

```
@property (T@"SBFDisplayContentModeResolutionPolicy",R,N,V_prevailingPolicy) prevailingPolicy;
@property (T@"NSArray",R,C,N,V_displayProxies) displayProxies;
@property (T{?=qqq{?=Bdq{?=ddBB}{?=ddBB}{?=ddBB}{?=ddBB}{?=ddBB}{?=ddBB}{?=ddBB}Bdddddd}{?=Bqqdqdd}{?=ffffBd}{?=qqqqqBqqdBd}{?=BB}{?=BBBBBdddddddd}{?=BBBBBBBdddddd}{?=qdqqBqdd}},R,N,V_devicePose) devicePose;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFResolvedDisplayContentMode debugDescription];
-[SBFResolvedDisplayContentMode hash];
-[SBFResolvedDisplayContentMode description];
-[SBFResolvedDisplayContentMode appendDescriptionToStream:];
-[SBFResolvedDisplayContentMode isEqual:];
-[SBFResolvedDisplayContentMode devicePose];
-[SBFResolvedDisplayContentMode displayProxies];
-[SBFResolvedDisplayContentMode initWithPrevailingPolicy:devicePose:displayProxies:];
-[SBFResolvedDisplayContentMode isInteractiveForDisplayProxy:devicePose:];
-[SBFResolvedDisplayContentMode logDeltaFromResolution:];
-[SBFResolvedDisplayContentMode prevailingPolicy];
-[SBFResolvedDisplayContentMode resolvedModeForDisplayProxy:];
-[SBFResolvedDisplayContentMode swapsContentModeForDisplayProxy:];
-[SBFResolvedDisplayContentMode targetModeForDisplayProxy:];
```

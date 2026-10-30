# `BLSBacklightFBSSceneEnvironment`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSBacklightSceneEnvironment_Private`
- 6 instance variables, 23 properties, 33 instance methods, 1 class methods

## Instance variables

```
@"<BLSBacklightSceneEnvironmentDelegate>" _delegate;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _animatingVisualState;
@"BLSAlwaysOnSession" _alwaysOnSession;
@"<BLSBacklightSceneEnvironmentUpdating>" _updater;
@"FBSScene" _fbsScene;
```

## Properties

```
@property (T@"FBSScene",W,G_FBSScene,S_setFBSScene:,V_fbsScene) fbsScene;
@property (TB) optsOutOfProcessAssertions;
@property (T@"NSDate",R) presentationDate;
@property (TQ,R) lowPowerRenderingPresentationTime;
@property (T@"BLSAlwaysOnSession",&,V_alwaysOnSession) alwaysOnSession;
@property (TB,GisAnimatingVisualState,V_animatingVisualState) animatingVisualState;
@property (T@"<BLSBacklightSceneEnvironmentUpdating>",&,V_updater) updater;
@property (T@"<BLSBacklightSceneEnvironmentDelegate>",&) delegate;
@property (T@"NSString",R,C) identifier;
@property (TB,R,GisDelegateActive) delegateActive;
@property (T@"BLSBacklightSceneVisualState",R) visualState;
@property (T@"BLSAlwaysOnFrameSpecifier",R) frameSpecifier;
@property (TB,R,GisLiveUpdating) liveUpdating;
@property (TB,R,GhasUnrestrictedFramerateUpdates) unrestrictedFramerateUpdates;
@property (TB) supportsAlwaysOn;
@property (TB) alwaysOnContentIs1hz;
@property (TB) needsFlipbookStateUpdates;
@property (TB) supportsLowPowerRendering;
@property (TB) needsLowPowerRenderingStateUpdates;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSBacklightFBSSceneEnvironment createEnvironmentForFBSScene:];
```

## Instance methods

```
-[BLSBacklightFBSSceneEnvironment updater];
-[BLSBacklightFBSSceneEnvironment visualState];
-[BLSBacklightFBSSceneEnvironment identifier];
-[BLSBacklightFBSSceneEnvironment invalidateAllTimelinesForReason:];
-[BLSBacklightFBSSceneEnvironment setUpdater:];
-[BLSBacklightFBSSceneEnvironment hasUnrestrictedFramerateUpdates];
-[BLSBacklightFBSSceneEnvironment setDelegate:];
-[BLSBacklightFBSSceneEnvironment delegate];
-[BLSBacklightFBSSceneEnvironment description];
-[BLSBacklightFBSSceneEnvironment presentationDate];
-[BLSBacklightFBSSceneEnvironment isLiveUpdating];
-[BLSBacklightFBSSceneEnvironment lowPowerRenderingPresentationTime];
-[BLSBacklightFBSSceneEnvironment _FBSScene];
-[BLSBacklightFBSSceneEnvironment _setFBSScene:];
-[BLSBacklightFBSSceneEnvironment frameSpecifier];
-[BLSBacklightFBSSceneEnvironment initWithFBSScene:];
-[BLSBacklightFBSSceneEnvironment setSupportsAlwaysOn:];
-[BLSBacklightFBSSceneEnvironment supportsLowPowerRendering];
-[BLSBacklightFBSSceneEnvironment setOptsOutOfProcessAssertions:];
-[BLSBacklightFBSSceneEnvironment alwaysOnSession];
-[BLSBacklightFBSSceneEnvironment alwaysOnContentIs1hz];
-[BLSBacklightFBSSceneEnvironment isDelegateActive];
-[BLSBacklightFBSSceneEnvironment needsFlipbookStateUpdates];
-[BLSBacklightFBSSceneEnvironment needsLowPowerRenderingStateUpdates];
-[BLSBacklightFBSSceneEnvironment setAlwaysOnContentIs1hz:];
-[BLSBacklightFBSSceneEnvironment setAlwaysOnSession:];
-[BLSBacklightFBSSceneEnvironment supportsAlwaysOn];
-[BLSBacklightFBSSceneEnvironment isAnimatingVisualState];
-[BLSBacklightFBSSceneEnvironment optsOutOfProcessAssertions];
-[BLSBacklightFBSSceneEnvironment setAnimatingVisualState:];
-[BLSBacklightFBSSceneEnvironment setNeedsFlipbookStateUpdates:];
-[BLSBacklightFBSSceneEnvironment setNeedsLowPowerRenderingStateUpdates:];
-[BLSBacklightFBSSceneEnvironment setSupportsLowPowerRendering:];
```

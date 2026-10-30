# `BLSBacklightSceneEnvironment` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 14 properties, 21 instance methods, 0 class methods

## Properties

```
@property (T@"<BLSBacklightSceneEnvironmentDelegate>",&) delegate;
@property (T@"NSString",R,C) identifier;
@property (TB,R,GisDelegateActive) delegateActive;
@property (T@"BLSBacklightSceneVisualState",R) visualState;
@property (T@"BLSAlwaysOnFrameSpecifier",R) frameSpecifier;
@property (TB,R,GisAnimatingVisualState) animatingVisualState;
@property (T@"BLSAlwaysOnSession",R) alwaysOnSession;
@property (TB,R,GisLiveUpdating) liveUpdating;
@property (TB,R,GhasUnrestrictedFramerateUpdates) unrestrictedFramerateUpdates;
@property (TB) supportsAlwaysOn;
@property (TB) alwaysOnContentIs1hz;
@property (TB) needsFlipbookStateUpdates;
@property (TB) supportsLowPowerRendering;
@property (TB) needsLowPowerRenderingStateUpdates;
```

## Instance methods

```
-[BLSBacklightSceneEnvironment visualState];
-[BLSBacklightSceneEnvironment identifier];
-[BLSBacklightSceneEnvironment invalidateAllTimelinesForReason:];
-[BLSBacklightSceneEnvironment hasUnrestrictedFramerateUpdates];
-[BLSBacklightSceneEnvironment setDelegate:];
-[BLSBacklightSceneEnvironment delegate];
-[BLSBacklightSceneEnvironment isLiveUpdating];
-[BLSBacklightSceneEnvironment frameSpecifier];
-[BLSBacklightSceneEnvironment setSupportsAlwaysOn:];
-[BLSBacklightSceneEnvironment supportsLowPowerRendering];
-[BLSBacklightSceneEnvironment alwaysOnSession];
-[BLSBacklightSceneEnvironment alwaysOnContentIs1hz];
-[BLSBacklightSceneEnvironment isDelegateActive];
-[BLSBacklightSceneEnvironment needsFlipbookStateUpdates];
-[BLSBacklightSceneEnvironment needsLowPowerRenderingStateUpdates];
-[BLSBacklightSceneEnvironment setAlwaysOnContentIs1hz:];
-[BLSBacklightSceneEnvironment supportsAlwaysOn];
-[BLSBacklightSceneEnvironment isAnimatingVisualState];
-[BLSBacklightSceneEnvironment setNeedsFlipbookStateUpdates:];
-[BLSBacklightSceneEnvironment setNeedsLowPowerRenderingStateUpdates:];
-[BLSBacklightSceneEnvironment setSupportsLowPowerRendering:];
```

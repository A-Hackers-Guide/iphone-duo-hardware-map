# `BLSHBacklightSceneHostEnvironment` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 22 properties, 42 instance methods, 0 class methods

## Properties

```
@property (T@"NSString",R,C) identifier;
@property (T@"RBSProcessIdentity",R) budgetProcessIdentity;
@property (TB,R) clientHasDelegate;
@property (TB,R,GisClientActive) clientActive;
@property (T@"BLSBacklightSceneVisualState",R) visualState;
@property (T@"NSDate",R) presentationDate;
@property (TB,R) clientSupportsAlwaysOn;
@property (TB,R) clientAlwaysOnContentIs1hz;
@property (TB,?,R,GisLocal) local;
@property (TB,?,R) supportsLowPowerRendering;
@property (TB,GisAlwaysOnEnabledForEnvironment) alwaysOnEnabledForEnvironment;
@property (TB,GisLiveUpdating) liveUpdating;
@property (TB,GhasUnrestrictedFramerateUpdates) unrestrictedFramerateUpdates;
@property (TB,?,R,Gis1HzFlipbook) oneHzFlipbook;
@property (TB,?,Gis1HzFlipbookForAssertion,Sset1HzFlipbookForAssertion:) oneHzFlipbookForAssertion;
@property (TB,?) cacheFlipbookOnDisplayWake;
@property (TB,?,GisHighLuminanceAlwaysOn) highLuminanceAlwaysOn;
@property (TB,?,GisLowPowerRenderingRequested) lowPowerRenderingRequested;
@property (TQ,?,R) lowPowerRenderingPresentationTime;
@property (TB,?,R) clientNeedsFlipbookStateUpdates;
@property (TB,?,R) clientSupportsLowPowerRendering;
@property (TB,?,R) clientNeedsLowPowerRenderingStateUpdates;
```

## Instance methods

```
-[BLSHBacklightSceneHostEnvironment clientDidRequestInvalidationForReason:];
-[BLSHBacklightSceneHostEnvironment isClientActive];
-[BLSHBacklightSceneHostEnvironment setUnrestrictedFramerateUpdates:];
-[BLSHBacklightSceneHostEnvironment visualState];
-[BLSHBacklightSceneHostEnvironment identifier];
-[BLSHBacklightSceneHostEnvironment removeObserver:];
-[BLSHBacklightSceneHostEnvironment requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:];
-[BLSHBacklightSceneHostEnvironment isAlwaysOnEnabledForEnvironment];
-[BLSHBacklightSceneHostEnvironment clearPresentationDate];
-[BLSHBacklightSceneHostEnvironment hasUnrestrictedFramerateUpdates];
-[BLSHBacklightSceneHostEnvironment clientAlwaysOnContentIs1hz];
-[BLSHBacklightSceneHostEnvironment invalidateContentForReason:];
-[BLSHBacklightSceneHostEnvironment addObserver:];
-[BLSHBacklightSceneHostEnvironment requestedFidelityForInactiveContentWithCompletion:];
-[BLSHBacklightSceneHostEnvironment willBeginRenderSession:];
-[BLSHBacklightSceneHostEnvironment clientHasDelegate];
-[BLSHBacklightSceneHostEnvironment deactivateClient];
-[BLSHBacklightSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:];
-[BLSHBacklightSceneHostEnvironment budgetProcessIdentity];
-[BLSHBacklightSceneHostEnvironment setAlwaysOnEnabledForEnvironment:];
-[BLSHBacklightSceneHostEnvironment presentationDate];
-[BLSHBacklightSceneHostEnvironment clientSupportsAlwaysOn];
-[BLSHBacklightSceneHostEnvironment isLiveUpdating];
-[BLSHBacklightSceneHostEnvironment setLiveUpdating:];
-[BLSHBacklightSceneHostEnvironment willEndRenderSession:];
-[BLSHBacklightSceneHostEnvironment updateToPresentationDate:visualState:sceneContentsUpdated:];
-[BLSHBacklightSceneHostEnvironment setCacheFlipbookOnDisplayWake:];
-[BLSHBacklightSceneHostEnvironment setHighLuminanceAlwaysOn:];
-[BLSHBacklightSceneHostEnvironment set1HzFlipbookForAssertion:];
-[BLSHBacklightSceneHostEnvironment isLowPowerRenderingRequested];
-[BLSHBacklightSceneHostEnvironment is1HzFlipbook];
-[BLSHBacklightSceneHostEnvironment clientNeedsFlipbookStateUpdates];
-[BLSHBacklightSceneHostEnvironment isHighLuminanceAlwaysOn];
-[BLSHBacklightSceneHostEnvironment isLocal];
-[BLSHBacklightSceneHostEnvironment clientNeedsLowPowerRenderingStateUpdates];
-[BLSHBacklightSceneHostEnvironment setLowPowerRenderingRequested:];
-[BLSHBacklightSceneHostEnvironment cacheFlipbookOnDisplayWake];
-[BLSHBacklightSceneHostEnvironment lowPowerRenderingPresentationTime];
-[BLSHBacklightSceneHostEnvironment is1HzFlipbookForAssertion];
-[BLSHBacklightSceneHostEnvironment clientSupportsLowPowerRendering];
-[BLSHBacklightSceneHostEnvironment supportsLowPowerRendering];
-[BLSHBacklightSceneHostEnvironment updateToDateSpecifier:sceneContentsUpdated:lowPowerRenderingDisabled:];
```

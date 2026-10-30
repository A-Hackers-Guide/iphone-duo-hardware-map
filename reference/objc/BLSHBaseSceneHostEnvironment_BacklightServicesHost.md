# `BLSHBaseSceneHostEnvironment`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightSceneHostEnvironment_Private`, `BLSHBacklightSceneHostEnvironment`
- 12 instance variables, 27 properties, 48 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSHashTable" _lock_observers;
B _lock_unrestrictedFramerateUpdates;
B _lock_1HzFlipbook;
B _lock_cacheFlipbookOnDisplayWake;
B _lock_highLuminanceAlwaysOn;
B _lock_lowPowerRenderingRequested;
B _lock_liveUpdating;
B _lock_alwaysOnEnabledForEnvironment;
@"BLSBacklightSceneVisualState" _lock_visualState;
@"NSDate" _lock_presentationDate;
@"NSString" _identifier;
```

## Properties

```
@property (TB,R) wantsStateUpdateToActiveAfterRemovalFromPresentation;
@property (T@"NSString",R,C,V_identifier) identifier;
@property (T@"RBSProcessIdentity",R) budgetProcessIdentity;
@property (TB,R) clientHasDelegate;
@property (TB,R,GisClientActive) clientActive;
@property (T@"BLSBacklightSceneVisualState",R,V_lock_visualState) visualState;
@property (T@"NSDate",R,V_lock_presentationDate) presentationDate;
@property (TB,R) clientSupportsAlwaysOn;
@property (TB,R) clientAlwaysOnContentIs1hz;
@property (TB,?,R,GisLocal) local;
@property (TB,?,R) supportsLowPowerRendering;
@property (TB,GisAlwaysOnEnabledForEnvironment,V_lock_alwaysOnEnabledForEnvironment) alwaysOnEnabledForEnvironment;
@property (TB,GisLiveUpdating,V_lock_liveUpdating) liveUpdating;
@property (TB,GhasUnrestrictedFramerateUpdates,V_lock_unrestrictedFramerateUpdates) unrestrictedFramerateUpdates;
@property (TB,?,R,Gis1HzFlipbook) oneHzFlipbook;
@property (TB,?,Gis1HzFlipbookForAssertion,Sset1HzFlipbookForAssertion:,V_lock_1HzFlipbook) oneHzFlipbookForAssertion;
@property (TB,?,V_lock_cacheFlipbookOnDisplayWake) cacheFlipbookOnDisplayWake;
@property (TB,?,GisHighLuminanceAlwaysOn,V_lock_highLuminanceAlwaysOn) highLuminanceAlwaysOn;
@property (TB,?,GisLowPowerRenderingRequested,V_lock_lowPowerRenderingRequested) lowPowerRenderingRequested;
@property (TQ,?,R) lowPowerRenderingPresentationTime;
@property (TB,?,R) clientNeedsFlipbookStateUpdates;
@property (TB,?,R) clientSupportsLowPowerRendering;
@property (TB,?,R) clientNeedsLowPowerRenderingStateUpdates;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHBaseSceneHostEnvironment updateToPresentationDate:visualState:sceneContentsUpdated:];
-[BLSHBaseSceneHostEnvironment setCacheFlipbookOnDisplayWake:];
-[BLSHBaseSceneHostEnvironment clientDidRequestInvalidationForReason:];
-[BLSHBaseSceneHostEnvironment isClientActive];
-[BLSHBaseSceneHostEnvironment setUnrestrictedFramerateUpdates:];
-[BLSHBaseSceneHostEnvironment visualState];
-[BLSHBaseSceneHostEnvironment setHighLuminanceAlwaysOn:];
-[BLSHBaseSceneHostEnvironment set1HzFlipbookForAssertion:];
-[BLSHBaseSceneHostEnvironment isLowPowerRenderingRequested];
-[BLSHBaseSceneHostEnvironment identifier];
-[BLSHBaseSceneHostEnvironment removeObserver:];
-[BLSHBaseSceneHostEnvironment is1HzFlipbook];
-[BLSHBaseSceneHostEnvironment clientNeedsFlipbookStateUpdates];
-[BLSHBaseSceneHostEnvironment requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:];
-[BLSHBaseSceneHostEnvironment isAlwaysOnEnabledForEnvironment];
-[BLSHBaseSceneHostEnvironment isHighLuminanceAlwaysOn];
-[BLSHBaseSceneHostEnvironment clearPresentationDate];
-[BLSHBaseSceneHostEnvironment hasUnrestrictedFramerateUpdates];
-[BLSHBaseSceneHostEnvironment clientAlwaysOnContentIs1hz];
-[BLSHBaseSceneHostEnvironment invalidateContentForReason:];
-[BLSHBaseSceneHostEnvironment isLocal];
-[BLSHBaseSceneHostEnvironment clientNeedsLowPowerRenderingStateUpdates];
-[BLSHBaseSceneHostEnvironment addObserver:];
-[BLSHBaseSceneHostEnvironment requestedFidelityForInactiveContentWithCompletion:];
-[BLSHBaseSceneHostEnvironment willBeginRenderSession:];
-[BLSHBaseSceneHostEnvironment clientHasDelegate];
-[BLSHBaseSceneHostEnvironment deactivateClient];
-[BLSHBaseSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:];
-[BLSHBaseSceneHostEnvironment budgetProcessIdentity];
-[BLSHBaseSceneHostEnvironment description];
-[BLSHBaseSceneHostEnvironment setAlwaysOnEnabledForEnvironment:];
-[BLSHBaseSceneHostEnvironment presentationDate];
-[BLSHBaseSceneHostEnvironment wantsStateUpdateToActiveAfterRemovalFromPresentation];
-[BLSHBaseSceneHostEnvironment setLowPowerRenderingRequested:];
-[BLSHBaseSceneHostEnvironment clientSupportsAlwaysOn];
-[BLSHBaseSceneHostEnvironment cacheFlipbookOnDisplayWake];
-[BLSHBaseSceneHostEnvironment isLiveUpdating];
-[BLSHBaseSceneHostEnvironment updateToVisualState:presentationDate:];
-[BLSHBaseSceneHostEnvironment setLiveUpdating:];
-[BLSHBaseSceneHostEnvironment initWithIdentifier:];
-[BLSHBaseSceneHostEnvironment is1HzFlipbookForAssertion];
-[BLSHBaseSceneHostEnvironment willEndRenderSession:];
-[BLSHBaseSceneHostEnvironment clientSupportsLowPowerRendering];
-[BLSHBaseSceneHostEnvironment withLock:];
-[BLSHBaseSceneHostEnvironment notifyObserversWithBlock:];
-[BLSHBaseSceneHostEnvironment setVisualState:presentationDate:];
-[BLSHBaseSceneHostEnvironment setDateSpecifier:];
-[BLSHBaseSceneHostEnvironment setPresentationDate:];
```

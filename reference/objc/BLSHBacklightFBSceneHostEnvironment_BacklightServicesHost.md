# `BLSHBacklightFBSceneHostEnvironment`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `BLSHBacklightSceneHostEnvironment_Private`
- 26 instance variables, 27 properties, 49 instance methods, 1 class methods

## Instance variables

```
@"FBScene" _fbScene;
@"BLSHBacklightSceneClientSettingsDiffInspector" _lock_diffInspector;
@"NSString" _nilSceneIdentifier;
@"BLSHAggregatedProcessAssertion" _lock_secondsFidelityAssertion;
@"BLSHAggregatedProcessAssertion" _lock_renderSessionAssertion;
@"RBSProcessIdentity" _budgetProcessIdentity;
@"NSHashTable" _lock_observers;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BLSBacklightSceneVisualState" _lock_visualState;
@"NSDate" _lock_presentationDate;
Q _creationMachTime;
Q _lock_renderSeed;
I _lock_requestDateSpecifierFailureCount;
B _lock_clientHasDelegate;
B _lock_clientActive;
B _lock_alwaysOnEnabledForEnvironment;
B _lock_clientSupportsAlwaysOn;
B _lock_clientAlwaysOnContentIs1hz;
B _lock_liveUpdating;
B _lock_unrestrictedFramerateUpdates;
B _lock_shouldInvalidateWhenActivated;
B _lock_1HzFlipbookForAssertion;
B _lock_cacheFlipbookOnDisplayWake;
B _lock_highLuminanceAlwaysOn;
B _lock_lowPowerRenderingRequested;
Q _lock_lowPowerRenderingPresentationTime;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R) wantsStateUpdateToActiveAfterRemovalFromPresentation;
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

## Class methods

```
+[BLSHBacklightFBSceneHostEnvironment setAmendSceneSettingsDelegate:];
```

## Instance methods

```
-[BLSHBacklightFBSceneHostEnvironment updateToPresentationDate:visualState:sceneContentsUpdated:];
-[BLSHBacklightFBSceneHostEnvironment setCacheFlipbookOnDisplayWake:];
-[BLSHBacklightFBSceneHostEnvironment clientDidRequestInvalidationForReason:];
-[BLSHBacklightFBSceneHostEnvironment isClientActive];
-[BLSHBacklightFBSceneHostEnvironment setUnrestrictedFramerateUpdates:];
-[BLSHBacklightFBSceneHostEnvironment visualState];
-[BLSHBacklightFBSceneHostEnvironment setHighLuminanceAlwaysOn:];
-[BLSHBacklightFBSceneHostEnvironment set1HzFlipbookForAssertion:];
-[BLSHBacklightFBSceneHostEnvironment isLowPowerRenderingRequested];
-[BLSHBacklightFBSceneHostEnvironment identifier];
-[BLSHBacklightFBSceneHostEnvironment removeObserver:];
-[BLSHBacklightFBSceneHostEnvironment sceneDidActivate:];
-[BLSHBacklightFBSceneHostEnvironment is1HzFlipbook];
-[BLSHBacklightFBSceneHostEnvironment dealloc];
-[BLSHBacklightFBSceneHostEnvironment clientNeedsFlipbookStateUpdates];
-[BLSHBacklightFBSceneHostEnvironment requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:];
-[BLSHBacklightFBSceneHostEnvironment isAlwaysOnEnabledForEnvironment];
-[BLSHBacklightFBSceneHostEnvironment isHighLuminanceAlwaysOn];
-[BLSHBacklightFBSceneHostEnvironment clearPresentationDate];
-[BLSHBacklightFBSceneHostEnvironment initWithFBScene:];
-[BLSHBacklightFBSceneHostEnvironment hasUnrestrictedFramerateUpdates];
-[BLSHBacklightFBSceneHostEnvironment sceneDidInvalidate:];
-[BLSHBacklightFBSceneHostEnvironment clientAlwaysOnContentIs1hz];
-[BLSHBacklightFBSceneHostEnvironment scene:didUpdateClientSettingsWithDiff:oldClientSettings:transitionContext:];
-[BLSHBacklightFBSceneHostEnvironment invalidateContentForReason:];
-[BLSHBacklightFBSceneHostEnvironment isLocal];
-[BLSHBacklightFBSceneHostEnvironment clientNeedsLowPowerRenderingStateUpdates];
-[BLSHBacklightFBSceneHostEnvironment addObserver:];
-[BLSHBacklightFBSceneHostEnvironment requestedFidelityForInactiveContentWithCompletion:];
-[BLSHBacklightFBSceneHostEnvironment willBeginRenderSession:];
-[BLSHBacklightFBSceneHostEnvironment clientHasDelegate];
-[BLSHBacklightFBSceneHostEnvironment deactivateClient];
-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:];
-[BLSHBacklightFBSceneHostEnvironment budgetProcessIdentity];
-[BLSHBacklightFBSceneHostEnvironment amendSceneSettings:];
-[BLSHBacklightFBSceneHostEnvironment description];
-[BLSHBacklightFBSceneHostEnvironment setAlwaysOnEnabledForEnvironment:];
-[BLSHBacklightFBSceneHostEnvironment presentationDate];
-[BLSHBacklightFBSceneHostEnvironment wantsStateUpdateToActiveAfterRemovalFromPresentation];
-[BLSHBacklightFBSceneHostEnvironment setLowPowerRenderingRequested:];
-[BLSHBacklightFBSceneHostEnvironment clientSupportsAlwaysOn];
-[BLSHBacklightFBSceneHostEnvironment cacheFlipbookOnDisplayWake];
-[BLSHBacklightFBSceneHostEnvironment isLiveUpdating];
-[BLSHBacklightFBSceneHostEnvironment updateToVisualState:presentationDate:];
-[BLSHBacklightFBSceneHostEnvironment setLiveUpdating:];
-[BLSHBacklightFBSceneHostEnvironment lowPowerRenderingPresentationTime];
-[BLSHBacklightFBSceneHostEnvironment is1HzFlipbookForAssertion];
-[BLSHBacklightFBSceneHostEnvironment willEndRenderSession:];
-[BLSHBacklightFBSceneHostEnvironment clientSupportsLowPowerRendering];
```

# `BLSHLocalHostSceneEnvironment`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BLSHBaseSceneHostEnvironment`
- 5 instance variables, 0 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"<BLSBacklightSceneEnvironment_Private>" _clientEnvironment;
@"BLSBacklightSceneVisualState" _lock_visualState;
@"NSDate" _lock_presentationDate;
@"NSDate" _lock_visualStateMismatchStartTime;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Instance methods

```
-[BLSHLocalHostSceneEnvironment updateToPresentationDate:visualState:sceneContentsUpdated:];
-[BLSHLocalHostSceneEnvironment isClientActive];
-[BLSHLocalHostSceneEnvironment setUnrestrictedFramerateUpdates:];
-[BLSHLocalHostSceneEnvironment visualState];
-[BLSHLocalHostSceneEnvironment clientNeedsFlipbookStateUpdates];
-[BLSHLocalHostSceneEnvironment requestDateSpecifiersForDateInterval:previousPresentationDate:shouldReset:completion:];
-[BLSHLocalHostSceneEnvironment clearPresentationDate];
-[BLSHLocalHostSceneEnvironment hasUnrestrictedFramerateUpdates];
-[BLSHLocalHostSceneEnvironment clientAlwaysOnContentIs1hz];
-[BLSHLocalHostSceneEnvironment clientNeedsLowPowerRenderingStateUpdates];
-[BLSHLocalHostSceneEnvironment requestedFidelityForInactiveContentWithCompletion:];
-[BLSHLocalHostSceneEnvironment clientHasDelegate];
-[BLSHLocalHostSceneEnvironment updateToVisualState:presentationDateSpecifier:animated:triggerEvent:touchTargetable:sceneContentsUpdated:performBacklightRamp:animationComplete:];
-[BLSHLocalHostSceneEnvironment presentationDate];
-[BLSHLocalHostSceneEnvironment clientSupportsAlwaysOn];
-[BLSHLocalHostSceneEnvironment isLiveUpdating];
-[BLSHLocalHostSceneEnvironment setLiveUpdating:];
-[BLSHLocalHostSceneEnvironment clientSupportsLowPowerRendering];
-[BLSHLocalHostSceneEnvironment _lock_updateVisualState:];
-[BLSHLocalHostSceneEnvironment hasVisualStateMistmach];
-[BLSHLocalHostSceneEnvironment initWithBacklightSceneEnvironment:];
```

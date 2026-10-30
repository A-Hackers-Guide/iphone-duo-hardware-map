# `BLSHEnvironmentTransitionState`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BLSHEnvironmentTransitionStateDelegate>" _delegate;
@"NSString" _delegateLoggingName;
@"<BLSHDisplayFlipbookStateProvider>" _displayFlipbookStateProvider;
@"BLSHEnvironmentTransitionStateTarget" _lock_requestingFidelityTarget;
@"BLSHEnvironmentTransitionStateTarget" _lock_inProgressUpdateTarget;
@"BLSHEnvironmentTransitionStateTarget" _lock_animationCompletedForOldTarget;
@"BLSHEnvironmentTransitionStateTarget" _lock_animationCompletedWithNewTarget;
Q _lock_nextSequenceID;
B _lock_animating;
@"<BLSHBacklightSceneHostEnvironment>" _environment;
```

## Properties

```
@property (T@"<BLSHBacklightSceneHostEnvironment>",R,N,V_environment) environment;
@property (TB,R,N,GisUpdatingInitialState) updatingInitialState;
@property (TB,R,N,GisUpdatingVisualState) updatingVisualState;
@property (TB,R,N,GisAnimating) animating;
```

## Class methods

```
+[BLSHEnvironmentTransitionState createStateForEnvironment:delegate:displayFlipbookStateProvider:];
```

## Instance methods

```
-[BLSHEnvironmentTransitionState isUpdatedToBacklightState:lowPowerRendering:];
-[BLSHEnvironmentTransitionState bls_loggingString];
-[BLSHEnvironmentTransitionState bls_shortLoggingString];
-[BLSHEnvironmentTransitionState debugDescription];
-[BLSHEnvironmentTransitionState dealloc];
-[BLSHEnvironmentTransitionState updateToBacklightState:forEvent:touchTargetable:presentationDate:sceneUpdate:lowPowerRenderingPresentationTime:performBacklightRamp:];
-[BLSHEnvironmentTransitionState updateToDateSpecifier:];
-[BLSHEnvironmentTransitionState performBacklightRampIfPendingForReason:];
-[BLSHEnvironmentTransitionState description];
-[BLSHEnvironmentTransitionState updateToExplicitVisualState:dateSpecifier:];
-[BLSHEnvironmentTransitionState isUpdatingVisualState];
-[BLSHEnvironmentTransitionState updateToFlipbookVisualState:backlightState:presentationDate:sceneUpdate:lowPowerRenderingPresentationTime:];
-[BLSHEnvironmentTransitionState isAnimating];
-[BLSHEnvironmentTransitionState isUpdatingInitialState];
-[BLSHEnvironmentTransitionState environment];
```

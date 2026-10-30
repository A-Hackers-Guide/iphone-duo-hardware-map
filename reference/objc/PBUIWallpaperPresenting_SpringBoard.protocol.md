# `PBUIWallpaperPresenting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 13 properties, 71 instance methods, 0 class methods

## Properties

```
@property (T@"<PBUIWallpaperPresentingDelegate>",W,N) wallpaperPresentingDelegate;
@property (T{?=qqd},R,N) currentHomescreenStyleTransitionState;
@property (Tq,N) activeVariant;
@property (Td,R,N) minimumHomescreenWallpaperScale;
@property (Td,R,N) homescreenWallpaperScale;
@property (Td,R,N) minimumLockscreenWallpaperScale;
@property (Td,R,N) lockscreenWallpaperScale;
@property (T@"PBUIHomeVariantStyleState",?,R,N) currentHomeVariantStyleState;
@property (TQ,?,R,N) significantEventsCounter;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},?,R,N) preferredSalientContentRectangle;
@property (TB,?,R,N) adaptiveTimeHonorsPreferredSalientContentRectangle;
@property (Td,?,N) deviceMotionUpdateInterval;
@property (Td,?,R,N) preferredDeviceMotionUpdateInterval;
```

## Instance methods

```
-[PBUIWallpaperPresenting activeVariant];
-[PBUIWallpaperPresenting requireWallpaperWithReason:];
-[PBUIWallpaperPresenting setActiveVariant:];
-[PBUIWallpaperPresenting setWallpaperStyleTransitionState:forPriority:forVariant:withAnimationFactory:];
-[PBUIWallpaperPresenting homescreenWallpaperScale];
-[PBUIWallpaperPresenting cancelInProcessAnimations];
-[PBUIWallpaperPresenting requireWallpaperRasterizationWithReason:];
-[PBUIWallpaperPresenting setWallpaperStyle:forPriority:forVariant:withAnimationFactory:];
-[PBUIWallpaperPresenting minimumHomescreenWallpaperScale];
-[PBUIWallpaperPresenting setActiveVariant:withOutAnimationFactory:inAnimationFactory:completion:];
-[PBUIWallpaperPresenting lockscreenWallpaperScale];
-[PBUIWallpaperPresenting setWallpaperPresentingDelegate:];
-[PBUIWallpaperPresenting suspendWallpaperAnimationForReason:];
-[PBUIWallpaperPresenting removeWallpaperStyleForPriority:forVariant:withAnimationFactory:];
-[PBUIWallpaperPresenting removeObserver:forVariant:];
-[PBUIWallpaperPresenting currentHomescreenStyleTransitionState];
-[PBUIWallpaperPresenting addObserver:forVariant:];
-[PBUIWallpaperPresenting setLockscreenWallpaperScale:withAnimationFactory:];
-[PBUIWallpaperPresenting setHomescreenWallpaperScale:withAnimationFactory:];
-[PBUIWallpaperPresenting minimumLockscreenWallpaperScale];
-[PBUIWallpaperPresenting wallpaperPresentingDelegate];
-[PBUIWallpaperPresenting invalidatePortalSources];
-[PBUIWallpaperPresenting posterHasRequestedHingeStateEvents];
-[PBUIWallpaperPresenting posterHidesDimmingLayer];
-[PBUIWallpaperPresenting updateCurrentPosterWithUpdates:error:];
-[PBUIWallpaperPresenting updateActiveVariantTransitionProgress:];
-[PBUIWallpaperPresenting scenesForBacklightSession];
-[PBUIWallpaperPresenting takeInSwitcherAssertionWithReason:];
-[PBUIWallpaperPresenting posterWantsDefaultParallax];
-[PBUIWallpaperPresenting posterDeviceMotionMode];
-[PBUIWallpaperPresenting posterHandlesWakeAnimation];
-[PBUIWallpaperPresenting endActiveVariantTransition];
-[PBUIWallpaperPresenting triggerSceneUpdate];
-[PBUIWallpaperPresenting currentHomeVariantStyleState];
-[PBUIWallpaperPresenting preferredSalientContentRectangle];
-[PBUIWallpaperPresenting freezeWallpaperFloatingLayerInContainerView:forReason:];
-[PBUIWallpaperPresenting beginActiveVariantTransition];
-[PBUIWallpaperPresenting setDeviceMotionUpdateInterval:];
-[PBUIWallpaperPresenting setAssociatedPosterConfiguration:withAnimationSettings:];
-[PBUIWallpaperPresenting setWallpaperObscured:];
-[PBUIWallpaperPresenting adaptiveTimeHonorsPreferredSalientContentRectangle];
-[PBUIWallpaperPresenting significantEventsCounterForPosterWithIdentifier:];
-[PBUIWallpaperPresenting preferredDeviceMotionUpdateInterval];
-[PBUIWallpaperPresenting userTapEventsRequested];
-[PBUIWallpaperPresenting deviceMotionUpdateInterval];
-[PBUIWallpaperPresenting significantEventsCounter];
-[PBUIWallpaperPresenting updateSalientContentRectangle:];
-[PBUIWallpaperPresenting fetchWallpaperProminentColor:];
-[PBUIWallpaperPresenting stopSendingHingeProgressEvents];
-[PBUIWallpaperPresenting triggerPosterTapEvent:];
-[PBUIWallpaperPresenting noteHomeVariantStyleStateMayHaveUpdated];
-[PBUIWallpaperPresenting acquireDuckHomeScreenWallpaperDimAssertionWithReason:];
-[PBUIWallpaperPresenting startSendingHingeProgressEvents];
-[PBUIWallpaperPresenting noteWillAnimateToInterfaceOrientation:duration:];
-[PBUIWallpaperPresenting setConfiguration:withAnimationSettings:];
-[PBUIWallpaperPresenting scenesForInactiveEnvironmentSession];
-[PBUIWallpaperPresenting updateWallpaperAnimationWithRotation:];
-[PBUIWallpaperPresenting homeScreenPosterMirrorsLock];
-[PBUIWallpaperPresenting hostDidEndDeviceMotionEventGeneration];
-[PBUIWallpaperPresenting createWallpaperFloatingViewForReason:ignoreReplica:];
-[PBUIWallpaperPresenting noteFencedUpdatesShouldBeSuppressed:];
-[PBUIWallpaperPresenting updateWallpaperAnimationWithIconFlyInTension:friction:];
-[PBUIWallpaperPresenting posterHasRequestedDeviceMotionEvents];
-[PBUIWallpaperPresenting updateWallpaperAnimationWithProgress:];
-[PBUIWallpaperPresenting updateWallpaperAnimationWithPitch:roll:yaw:];
-[PBUIWallpaperPresenting updateWallpaperAnimationWithWakeSourceIsSwipeToUnlock:];
-[PBUIWallpaperPresenting noteDidRotateFromInterfaceOrientation:];
-[PBUIWallpaperPresenting hostWillStartDeviceMotionEventGeneration];
-[PBUIWallpaperPresenting triggerPosterSignificantEvent];
-[PBUIWallpaperPresenting setWallpaperFloatingLayerContainerView:forReason:withAnimationFactory:];
-[PBUIWallpaperPresenting noteWillAnimateToInterfaceOrientation:];
```

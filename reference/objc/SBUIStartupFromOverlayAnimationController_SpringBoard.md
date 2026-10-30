# `SBUIStartupFromOverlayAnimationController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBUIMainScreenAnimationController`
- Protocols: `SBSceneViewPresentationConfiguring`
- 7 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _overlays;
@"BSAnimationSettings" _animationSettings;
B _waitsForAppActivation;
@"BSUIOrientationTransformWrapperView" _orientationWrapperView;
@"SBSceneView" _sceneView;
d _commitWaitStartTime;
B _overlaysDismissed;
```

## Properties

```
@property (T@"BSAnimationSettings",&,N,V_animationSettings) animationSettings;
@property (TB,N,V_waitsForAppActivation) waitsForAppActivation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBUIStartupFromOverlayAnimationController setAnimationSettings:];
-[SBUIStartupFromOverlayAnimationController _windowScene];
-[SBUIStartupFromOverlayAnimationController animationSettings];
-[SBUIStartupFromOverlayAnimationController initWithTransitionContextProvider:];
-[SBUIStartupFromOverlayAnimationController _prepareAnimation];
-[SBUIStartupFromOverlayAnimationController _cleanupAnimation];
-[SBUIStartupFromOverlayAnimationController _startAnimation];
-[SBUIStartupFromOverlayAnimationController sceneViewPresentationPriority:];
-[SBUIStartupFromOverlayAnimationController sceneViewPresentationIdentifier:];
-[SBUIStartupFromOverlayAnimationController _dismissOverlaysForReason:];
-[SBUIStartupFromOverlayAnimationController _primarySceneHandle];
-[SBUIStartupFromOverlayAnimationController _shouldDismissBanner];
-[SBUIStartupFromOverlayAnimationController _waitsForActivatingSceneContentAvailableIfNecessary];
-[SBUIStartupFromOverlayAnimationController initWithTransitionContextProvider:overlays:];
-[SBUIStartupFromOverlayAnimationController setWaitsForAppActivation:];
-[SBUIStartupFromOverlayAnimationController waitsForAppActivation];
```

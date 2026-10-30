# `SBUIStartupFromBlackAnimationController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBUIMainScreenAnimationController`
- Protocols: `SBSceneViewPresentationConfiguring`
- 6 instance variables, 6 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"BSAnimationSettings" _animationSettings;
B _waitsForAppActivation;
@"UIView" _internalContainerView;
@"UIView" _blackView;
@"BSUIOrientationTransformWrapperView" _orientationWrapperView;
@"SBDeviceApplicationSceneView" _sceneView;
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
-[SBUIStartupFromBlackAnimationController setAnimationSettings:];
-[SBUIStartupFromBlackAnimationController animationSettings];
-[SBUIStartupFromBlackAnimationController initWithTransitionContextProvider:];
-[SBUIStartupFromBlackAnimationController _prepareAnimation];
-[SBUIStartupFromBlackAnimationController _cleanupAnimation];
-[SBUIStartupFromBlackAnimationController _setHidden:];
-[SBUIStartupFromBlackAnimationController _startAnimation];
-[SBUIStartupFromBlackAnimationController sceneViewPresentationPriority:];
-[SBUIStartupFromBlackAnimationController sceneViewPresentationIdentifier:];
-[SBUIStartupFromBlackAnimationController _getTransitionWindow];
-[SBUIStartupFromBlackAnimationController _shouldDismissBanner];
-[SBUIStartupFromBlackAnimationController _showBlackView];
-[SBUIStartupFromBlackAnimationController _waitsForActivatingSceneContentAvailableIfNecessary];
-[SBUIStartupFromBlackAnimationController setWaitsForAppActivation:];
-[SBUIStartupFromBlackAnimationController waitsForAppActivation];
```

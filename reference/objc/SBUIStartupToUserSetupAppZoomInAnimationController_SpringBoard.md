# `SBUIStartupToUserSetupAppZoomInAnimationController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBUIMainScreenAnimationController`
- Protocols: `SBSceneViewPresentationConfiguring`
- 3 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"BSUIOrientationTransformWrapperView" _orientationWrapperView;
@"SBSceneView" _sceneView;
@"NSArray" _persistentSnapshotOverlays;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBUIStartupToUserSetupAppZoomInAnimationController animationSettings];
-[SBUIStartupToUserSetupAppZoomInAnimationController initWithTransitionContextProvider:];
-[SBUIStartupToUserSetupAppZoomInAnimationController _prepareAnimation];
-[SBUIStartupToUserSetupAppZoomInAnimationController _cleanupAnimation];
-[SBUIStartupToUserSetupAppZoomInAnimationController _setHidden:];
-[SBUIStartupToUserSetupAppZoomInAnimationController _startAnimation];
-[SBUIStartupToUserSetupAppZoomInAnimationController sceneViewPresentationPriority:];
-[SBUIStartupToUserSetupAppZoomInAnimationController sceneViewPresentationIdentifier:];
-[SBUIStartupToUserSetupAppZoomInAnimationController _getTransitionWindow];
-[SBUIStartupToUserSetupAppZoomInAnimationController _shouldDismissBanner];
-[SBUIStartupToUserSetupAppZoomInAnimationController _waitsForActivatingSceneContentAvailableIfNecessary];
-[SBUIStartupToUserSetupAppZoomInAnimationController initWithTransitionContextProvider:overlays:];
```

# `SBCenterAppIconZoomAnimator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBCenterIconZoomAnimator`
- 8 instance variables, 5 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"UIView" _appView;
@"UIView" _appZoomView;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _destinationFrame;
C _testCompletionCount;
d _distantScale;
@"SBReversibleLayerPropertyAnimator" _appZoomAnimator;
@"NSMutableArray" _animationCompletions;
@"UIWindow" _window;
```

## Properties

```
@property (T@"SBReversibleLayerPropertyAnimator",&,N,V_appZoomAnimator) appZoomAnimator;
@property (T@"NSMutableArray",&,N,V_animationCompletions) animationCompletions;
@property (T@"UIWindow",&,N,V_window) window;
@property (T@"SBHCenterAppZoomSettings",&,D,N) settings;
@property (Td,V_distantScale) distantScale;
```

## Instance methods

```
-[SBCenterAppIconZoomAnimator _prepareAnimation];
-[SBCenterAppIconZoomAnimator window];
-[SBCenterAppIconZoomAnimator _cleanupAnimation];
-[SBCenterAppIconZoomAnimator _numberOfSignificantAnimations];
-[SBCenterAppIconZoomAnimator _performAnimationToFraction:withCentralAnimationSettings:delay:alreadyAnimating:sharedCompletion:];
-[SBCenterAppIconZoomAnimator _setAnimationFraction:];
-[SBCenterAppIconZoomAnimator setWindow:];
-[SBCenterAppIconZoomAnimator _delayedForRotation];
-[SBCenterAppIconZoomAnimator _iconZoomDelay];
-[SBCenterAppIconZoomAnimator animationCompletions];
-[SBCenterAppIconZoomAnimator cameraPosition];
-[SBCenterAppIconZoomAnimator setAnimationCompletions:];
-[SBCenterAppIconZoomAnimator appZoomAnimator];
-[SBCenterAppIconZoomAnimator _appZPositionForZoomFraction:];
-[SBCenterAppIconZoomAnimator _appZoomDelay];
-[SBCenterAppIconZoomAnimator _fadeAppForZoomFraction:];
-[SBCenterAppIconZoomAnimator _translateAppForZoomFraction:];
-[SBCenterAppIconZoomAnimator _zoomAppForZoomFraction:];
-[SBCenterAppIconZoomAnimator distantScale];
-[SBCenterAppIconZoomAnimator initWithFolderController:appView:window:];
-[SBCenterAppIconZoomAnimator setAppZoomAnimator:];
-[SBCenterAppIconZoomAnimator setDistantScale:];
```

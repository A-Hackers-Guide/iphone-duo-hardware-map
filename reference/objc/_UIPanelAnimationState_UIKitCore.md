# `_UIPanelAnimationState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 9 properties, 18 instance methods, 3 class methods

## Instance variables

```
B _isFinishingAnimation;
B _shouldAssignOffscreenWidthsToStateRequest;
B _animatorShouldCoordinate;
@"UISlidingBarStateRequest" _fromRequest;
@"UISlidingBarStateRequest" _toRequest;
d _progress;
q _affectedSides;
@"_UIPanelCoordinatingAnimator" _animator;
```

## Properties

```
@property (T@"UISlidingBarStateRequest",C,N,V_fromRequest) fromRequest;
@property (T@"UISlidingBarStateRequest",C,N,V_toRequest) toRequest;
@property (Td,N,V_progress) progress;
@property (TB,N,SsetFinishingAnimation:,V_isFinishingAnimation) isFinishingAnimation;
@property (Tq,N,V_affectedSides) affectedSides;
@property (TB,N,V_shouldAssignOffscreenWidthsToStateRequest) shouldAssignOffscreenWidthsToStateRequest;
@property (T@"UISlidingBarStateRequest",R,N) stateRequest;
@property (T@"_UIPanelCoordinatingAnimator",&,N,V_animator) animator;
@property (TB,N,V_animatorShouldCoordinate) animatorShouldCoordinate;
```

## Class methods

```
+[_UIPanelAnimationState defaultDuration];
+[_UIPanelAnimationState timingCurveProvider];
+[_UIPanelAnimationState timingCurveProviderWithVelocity:];
```

## Instance methods

```
-[_UIPanelAnimationState setProgress:];
-[_UIPanelAnimationState setAnimator:];
-[_UIPanelAnimationState animator];
-[_UIPanelAnimationState progress];
-[_UIPanelAnimationState description];
-[_UIPanelAnimationState setFromRequest:];
-[_UIPanelAnimationState affectedSides];
-[_UIPanelAnimationState animatorShouldCoordinate];
-[_UIPanelAnimationState fromRequest];
-[_UIPanelAnimationState isFinishingAnimation];
-[_UIPanelAnimationState setAffectedSides:];
-[_UIPanelAnimationState setAnimatorShouldCoordinate:];
-[_UIPanelAnimationState setFinishingAnimation:];
-[_UIPanelAnimationState setShouldAssignOffscreenWidthsToStateRequest:];
-[_UIPanelAnimationState setToRequest:];
-[_UIPanelAnimationState shouldAssignOffscreenWidthsToStateRequest];
-[_UIPanelAnimationState stateRequest];
-[_UIPanelAnimationState toRequest];
```

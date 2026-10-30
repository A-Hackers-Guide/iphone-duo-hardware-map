# `_UIHomeAffordanceGateGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `UITapRecognizerDelegate`, `_UIHomeAffordanceObserver`
- 5 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _homeAffordanceFrame;
@"UITapRecognizer" _tapRecognizer;
@"BSAbsoluteMachTimer" _timeoutTimer;
@"<_UIInvalidatable>" _homeAffordanceObserver;
B _didReceiveTouch;
```

## Properties

```
@property (T@"UIView",R,N) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIHomeAffordanceGateGestureRecognizer _isAllowedToReceiveGESEvents];
-[_UIHomeAffordanceGateGestureRecognizer _notifier:homeAffordanceFrameDidChange:];
-[_UIHomeAffordanceGateGestureRecognizer touchesEnded:withEvent:];
-[_UIHomeAffordanceGateGestureRecognizer _notifier:homeAffordanceDoubleTapGestureDidSucceed:];
-[_UIHomeAffordanceGateGestureRecognizer canBePreventedByGestureRecognizer:];
-[_UIHomeAffordanceGateGestureRecognizer setState:];
-[_UIHomeAffordanceGateGestureRecognizer touchesCancelled:withEvent:];
-[_UIHomeAffordanceGateGestureRecognizer init];
-[_UIHomeAffordanceGateGestureRecognizer _windowDidMoveToNilScene:];
-[_UIHomeAffordanceGateGestureRecognizer reset];
-[_UIHomeAffordanceGateGestureRecognizer setView:];
-[_UIHomeAffordanceGateGestureRecognizer touchesBegan:withEvent:];
-[_UIHomeAffordanceGateGestureRecognizer touchesMoved:withEvent:];
-[_UIHomeAffordanceGateGestureRecognizer shouldBeRequiredToFailByGestureRecognizer:];
-[_UIHomeAffordanceGateGestureRecognizer tapIsPossibleForTapRecognizer:];
-[_UIHomeAffordanceGateGestureRecognizer _touchSloppinessFactor];
-[_UIHomeAffordanceGateGestureRecognizer _windowDidMoveToScene:];
-[_UIHomeAffordanceGateGestureRecognizer tapRecognizerFailedToRecognizeTap:];
-[_UIHomeAffordanceGateGestureRecognizer name];
-[_UIHomeAffordanceGateGestureRecognizer tapRecognizerRecognizedTap:];
```

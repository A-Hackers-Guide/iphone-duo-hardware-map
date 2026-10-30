# `_UIFlexInteractionPanGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 2 instance variables, 2 properties, 12 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _initialTouchLocation;
q _currentTouchType;
```

## Properties

```
@property (TB,R,N) isCurrentlyActive;
@property (Tq,R,N,V_currentTouchType) currentTouchType;
```

## Instance methods

```
-[_UIFlexInteractionPanGestureRecognizer canPreventGestureRecognizer:];
-[_UIFlexInteractionPanGestureRecognizer translationInView:];
-[_UIFlexInteractionPanGestureRecognizer touchesEnded:withEvent:];
-[_UIFlexInteractionPanGestureRecognizer _acceptsBeingFailureRequirementForGestureRecognizer:];
-[_UIFlexInteractionPanGestureRecognizer canBePreventedByGestureRecognizer:];
-[_UIFlexInteractionPanGestureRecognizer _acceptsBeingFailureDependentOnGestureRecognizer:];
-[_UIFlexInteractionPanGestureRecognizer _canCancelGestureRecognizer:];
-[_UIFlexInteractionPanGestureRecognizer touchesCancelled:withEvent:];
-[_UIFlexInteractionPanGestureRecognizer isCurrentlyActive];
-[_UIFlexInteractionPanGestureRecognizer touchesBegan:withEvent:];
-[_UIFlexInteractionPanGestureRecognizer initWithTarget:action:];
-[_UIFlexInteractionPanGestureRecognizer currentTouchType];
```

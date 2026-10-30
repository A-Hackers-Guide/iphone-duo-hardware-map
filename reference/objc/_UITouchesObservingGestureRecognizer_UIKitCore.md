# `_UITouchesObservingGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 1 instance variables, 1 properties, 16 instance methods, 2 class methods

## Instance variables

```
@"NSSet" _touches;
```

## Properties

```
@property (T@"NSSet",C,N,V_touches) touches;
```

## Class methods

```
+[_UITouchesObservingGestureRecognizer _supportsDefaultTouchTypes];
+[_UITouchesObservingGestureRecognizer _supportsDefaultPressTypes];
```

## Instance methods

```
-[_UITouchesObservingGestureRecognizer canPreventGestureRecognizer:];
-[_UITouchesObservingGestureRecognizer touchesEnded:withEvent:];
-[_UITouchesObservingGestureRecognizer _acceptsBeingFailureRequirementForGestureRecognizer:];
-[_UITouchesObservingGestureRecognizer canBePreventedByGestureRecognizer:];
-[_UITouchesObservingGestureRecognizer _acceptsBeingFailureDependentOnGestureRecognizer:];
-[_UITouchesObservingGestureRecognizer _canCancelGestureRecognizer:];
-[_UITouchesObservingGestureRecognizer touchesCancelled:withEvent:];
-[_UITouchesObservingGestureRecognizer touches];
-[_UITouchesObservingGestureRecognizer reset];
-[_UITouchesObservingGestureRecognizer touchesBegan:withEvent:];
-[_UITouchesObservingGestureRecognizer touchesMoved:withEvent:];
-[_UITouchesObservingGestureRecognizer initWithTarget:action:];
-[_UITouchesObservingGestureRecognizer _allTouchesAreEndedOrCancelled:];
-[_UITouchesObservingGestureRecognizer _updateTouchesFromEvent:];
-[_UITouchesObservingGestureRecognizer _wantsPartialTouchSequences];
-[_UITouchesObservingGestureRecognizer setTouches:];
```

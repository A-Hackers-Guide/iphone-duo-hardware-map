# `_UIContextMenuActionScrubbingHandoffGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 2 instance variables, 1 properties, 14 instance methods, 1 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _initialLocation;
d _hysteresis;
```

## Properties

```
@property (Td,N,V_hysteresis) hysteresis;
```

## Class methods

```
+[_UIContextMenuActionScrubbingHandoffGestureRecognizer _supportsTouchContinuation];
```

## Instance methods

```
-[_UIContextMenuActionScrubbingHandoffGestureRecognizer setHysteresis:];
-[_UIContextMenuActionScrubbingHandoffGestureRecognizer canPreventGestureRecognizer:];
-[_UIContextMenuActionScrubbingHandoffGestureRecognizer touchesEnded:withEvent:];
-[_UIContextMenuActionScrubbingHandoffGestureRecognizer hysteresis];
-[_UIContextMenuActionScrubbingHandoffGestureRecognizer _acceptsBeingFailureRequirementForGestureRecognizer:];
-[_UIContextMenuActionScrubbingHandoffGestureRecognizer canBePreventedByGestureRecognizer:];
-[_UIContextMenuActionScrubbingHandoffGestureRecognizer _acceptsBeingFailureDependentOnGestureRecognizer:];
-[_UIContextMenuActionScrubbingHandoffGestureRecognizer touchesCancelled:withEvent:];
-[_UIContextMenuActionScrubbingHandoffGestureRecognizer _gestureIsStillValid];
-[_UIContextMenuActionScrubbingHandoffGestureRecognizer touchesBegan:withEvent:];
-[_UIContextMenuActionScrubbingHandoffGestureRecognizer touchesMoved:withEvent:];
-[_UIContextMenuActionScrubbingHandoffGestureRecognizer initWithTarget:action:];
-[_UIContextMenuActionScrubbingHandoffGestureRecognizer _beginGestureIfPossible];
-[_UIContextMenuActionScrubbingHandoffGestureRecognizer _satisfiedHysteresis];
```

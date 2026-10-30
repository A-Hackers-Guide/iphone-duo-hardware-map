# `_UISwipeDismissalGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 2 instance variables, 2 properties, 10 instance methods, 2 class methods

## Instance variables

```
d _allowableMovement;
{CGPoint="x"d"y"d} _originalTouchPoint;
```

## Properties

```
@property (T{CGPoint=dd},N,V_originalTouchPoint) originalTouchPoint;
@property (Td,N,V_allowableMovement) allowableMovement;
```

## Class methods

```
+[_UISwipeDismissalGestureRecognizer _supportsDefaultTouchTypes];
+[_UISwipeDismissalGestureRecognizer _supportsDefaultPressTypes];
```

## Instance methods

```
-[_UISwipeDismissalGestureRecognizer allowableMovement];
-[_UISwipeDismissalGestureRecognizer touchesEnded:withEvent:];
-[_UISwipeDismissalGestureRecognizer touchesCancelled:withEvent:];
-[_UISwipeDismissalGestureRecognizer setAllowableMovement:];
-[_UISwipeDismissalGestureRecognizer reset];
-[_UISwipeDismissalGestureRecognizer touchesBegan:withEvent:];
-[_UISwipeDismissalGestureRecognizer touchesMoved:withEvent:];
-[_UISwipeDismissalGestureRecognizer initWithTarget:action:];
-[_UISwipeDismissalGestureRecognizer originalTouchPoint];
-[_UISwipeDismissalGestureRecognizer setOriginalTouchPoint:];
```

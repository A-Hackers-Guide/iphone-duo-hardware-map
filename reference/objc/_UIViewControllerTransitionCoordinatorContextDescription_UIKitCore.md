# `_UIViewControllerTransitionCoordinatorContextDescription`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 10 instance variables, 10 properties, 22 instance methods, 2 class methods

## Instance variables

```
B _animated;
B _interactive;
B _cancelled;
d _transitionDuration;
d _percentComplete;
d _completionVelocity;
q _completionCurve;
q _toOrientation;
q _fromOrientation;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _targetTransform;
```

## Properties

```
@property (TB,N,GisAnimated,V_animated) animated;
@property (TB,N,GisInteractive,V_interactive) interactive;
@property (TB,N,GisCancelled,V_cancelled) cancelled;
@property (Td,N,V_transitionDuration) transitionDuration;
@property (Td,N,V_percentComplete) percentComplete;
@property (Td,N,V_completionVelocity) completionVelocity;
@property (Tq,N,V_completionCurve) completionCurve;
@property (T{CGAffineTransform=dddddd},N,V_targetTransform) targetTransform;
@property (Tq,N,V_toOrientation) toOrientation;
@property (Tq,N,V_fromOrientation) fromOrientation;
```

## Class methods

```
+[_UIViewControllerTransitionCoordinatorContextDescription supportsSecureCoding];
+[_UIViewControllerTransitionCoordinatorContextDescription descriptionForTransitionCoordinatorContext:];
```

## Instance methods

```
-[_UIViewControllerTransitionCoordinatorContextDescription completionVelocity];
-[_UIViewControllerTransitionCoordinatorContextDescription setTargetTransform:];
-[_UIViewControllerTransitionCoordinatorContextDescription percentComplete];
-[_UIViewControllerTransitionCoordinatorContextDescription setCancelled:];
-[_UIViewControllerTransitionCoordinatorContextDescription isAnimated];
-[_UIViewControllerTransitionCoordinatorContextDescription isInteractive];
-[_UIViewControllerTransitionCoordinatorContextDescription isCancelled];
-[_UIViewControllerTransitionCoordinatorContextDescription transitionDuration];
-[_UIViewControllerTransitionCoordinatorContextDescription setAnimated:];
-[_UIViewControllerTransitionCoordinatorContextDescription setTransitionDuration:];
-[_UIViewControllerTransitionCoordinatorContextDescription targetTransform];
-[_UIViewControllerTransitionCoordinatorContextDescription completionCurve];
-[_UIViewControllerTransitionCoordinatorContextDescription encodeWithCoder:];
-[_UIViewControllerTransitionCoordinatorContextDescription initWithCoder:];
-[_UIViewControllerTransitionCoordinatorContextDescription setInteractive:];
-[_UIViewControllerTransitionCoordinatorContextDescription fromOrientation];
-[_UIViewControllerTransitionCoordinatorContextDescription setCompletionCurve:];
-[_UIViewControllerTransitionCoordinatorContextDescription setCompletionVelocity:];
-[_UIViewControllerTransitionCoordinatorContextDescription setFromOrientation:];
-[_UIViewControllerTransitionCoordinatorContextDescription setPercentComplete:];
-[_UIViewControllerTransitionCoordinatorContextDescription setToOrientation:];
-[_UIViewControllerTransitionCoordinatorContextDescription toOrientation];
```

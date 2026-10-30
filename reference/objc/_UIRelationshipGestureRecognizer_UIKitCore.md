# `_UIRelationshipGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 2 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _succeedsOnTouchesEnded;
B _failsOnTouchesCancelled;
```

## Properties

```
@property (TB,N,V_succeedsOnTouchesEnded) succeedsOnTouchesEnded;
@property (TB,N,V_failsOnTouchesCancelled) failsOnTouchesCancelled;
```

## Instance methods

```
-[_UIRelationshipGestureRecognizer touchesEnded:withEvent:];
-[_UIRelationshipGestureRecognizer touchesCancelled:withEvent:];
-[_UIRelationshipGestureRecognizer failsOnTouchesCancelled];
-[_UIRelationshipGestureRecognizer _fail];
-[_UIRelationshipGestureRecognizer _isGestureType:];
-[_UIRelationshipGestureRecognizer initWithTarget:action:];
-[_UIRelationshipGestureRecognizer _succeed];
-[_UIRelationshipGestureRecognizer setSucceedsOnTouchesEnded:];
-[_UIRelationshipGestureRecognizer setFailsOnTouchesCancelled:];
-[_UIRelationshipGestureRecognizer succeedsOnTouchesEnded];
```

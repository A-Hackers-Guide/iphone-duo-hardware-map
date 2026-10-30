# `PKPencilObserverGestureRecognizer`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 4 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"UITouch" _drawingTouch;
B _delegateRespondsToDidBegin;
B _delegateRespondsToDidMove;
B _delegateRespondsToDidEnd;
```

## Instance methods

```
-[PKPencilObserverGestureRecognizer canPreventGestureRecognizer:];
-[PKPencilObserverGestureRecognizer touchesEnded:withEvent:];
-[PKPencilObserverGestureRecognizer canBePreventedByGestureRecognizer:];
-[PKPencilObserverGestureRecognizer touchesCancelled:withEvent:];
-[PKPencilObserverGestureRecognizer reset];
-[PKPencilObserverGestureRecognizer touchesBegan:withEvent:];
-[PKPencilObserverGestureRecognizer touchesMoved:withEvent:];
-[PKPencilObserverGestureRecognizer locationInView:];
-[PKPencilObserverGestureRecognizer shouldBeRequiredToFailByGestureRecognizer:];
-[PKPencilObserverGestureRecognizer setDelegate:];
-[PKPencilObserverGestureRecognizer shouldRequireFailureOfGestureRecognizer:];
```

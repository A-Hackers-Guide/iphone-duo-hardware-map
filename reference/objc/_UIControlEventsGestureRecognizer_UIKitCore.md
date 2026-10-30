# `_UIControlEventsGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 3 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
{?="touchInside"b1"touchDragged"b1"deliveredCancel"b1} _flags;
@"UITouch" _activeTouch;
@"<_UIControlEventsGestureRecognizerDelegate>" _controlEventsDelegate;
```

## Properties

```
@property (T@"UITouch",R,N,V_activeTouch) activeTouch;
@property (T@"<_UIControlEventsGestureRecognizerDelegate>",W,N,V_controlEventsDelegate) controlEventsDelegate;
```

## Instance methods

```
-[_UIControlEventsGestureRecognizer touchesEnded:withEvent:];
-[_UIControlEventsGestureRecognizer touchesCancelled:withEvent:];
-[_UIControlEventsGestureRecognizer activeTouch];
-[_UIControlEventsGestureRecognizer sendControlEvent:withEvent:];
-[_UIControlEventsGestureRecognizer reset];
-[_UIControlEventsGestureRecognizer touchesBegan:withEvent:];
-[_UIControlEventsGestureRecognizer touchesMoved:withEvent:];
-[_UIControlEventsGestureRecognizer gestureRecognizerFailed];
-[_UIControlEventsGestureRecognizer setControlEventsDelegate:];
-[_UIControlEventsGestureRecognizer controlEventsDelegate];
```

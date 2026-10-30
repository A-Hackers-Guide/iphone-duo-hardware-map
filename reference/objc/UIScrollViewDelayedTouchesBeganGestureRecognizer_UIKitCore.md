# `UIScrollViewDelayedTouchesBeganGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 3 instance variables, 0 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"UIDelayedAction" _touchDelay;
{CGPoint="x"d"y"d} _startSceneReferenceLocation;
@"UIView<UIScrollViewDelayedTouchesBeganGestureRecognizerClient>" _client;
```

## Class methods

```
+[UIScrollViewDelayedTouchesBeganGestureRecognizer _supportsDefaultTouchTypes];
+[UIScrollViewDelayedTouchesBeganGestureRecognizer _supportsDefaultPressTypes];
```

## Instance methods

```
-[UIScrollViewDelayedTouchesBeganGestureRecognizer touchesEnded:withEvent:];
-[UIScrollViewDelayedTouchesBeganGestureRecognizer _resetGestureRecognizer];
-[UIScrollViewDelayedTouchesBeganGestureRecognizer clearTimer];
-[UIScrollViewDelayedTouchesBeganGestureRecognizer touchesCancelled:withEvent:];
-[UIScrollViewDelayedTouchesBeganGestureRecognizer sendTouchesShouldBeginForTouches:withEvent:];
-[UIScrollViewDelayedTouchesBeganGestureRecognizer dealloc];
-[UIScrollViewDelayedTouchesBeganGestureRecognizer sendTouchesShouldBeginForDelayedTouches:];
-[UIScrollViewDelayedTouchesBeganGestureRecognizer touchesBegan:withEvent:];
-[UIScrollViewDelayedTouchesBeganGestureRecognizer touchesMoved:withEvent:];
-[UIScrollViewDelayedTouchesBeganGestureRecognizer _clientView];
-[UIScrollViewDelayedTouchesBeganGestureRecognizer _shouldMakeTimerForDelayedContentTouches:];
-[UIScrollViewDelayedTouchesBeganGestureRecognizer _updateGestureTraits];
-[UIScrollViewDelayedTouchesBeganGestureRecognizer sendDelayedTouches];
```

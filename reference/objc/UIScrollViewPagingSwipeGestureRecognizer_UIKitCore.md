# `UIScrollViewPagingSwipeGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 6 instance variables, 1 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"UIScrollView" _scrollView;
@"UIDelayedAction" _swipeFailureDelay;
{CGPoint="x"d"y"d} _startLocation;
{CGPoint="x"d"y"d} _lastLocation;
d _lastTime;
i _directionalFailureCount;
```

## Properties

```
@property (T@"UIScrollView",W,N,V_scrollView) scrollView;
```

## Class methods

```
+[UIScrollViewPagingSwipeGestureRecognizer _supportsDefaultTouchTypes];
+[UIScrollViewPagingSwipeGestureRecognizer _supportsDefaultPressTypes];
```

## Instance methods

```
-[UIScrollViewPagingSwipeGestureRecognizer touchesEnded:withEvent:];
-[UIScrollViewPagingSwipeGestureRecognizer _resetGestureRecognizer];
-[UIScrollViewPagingSwipeGestureRecognizer clearTimer];
-[UIScrollViewPagingSwipeGestureRecognizer touchesCancelled:withEvent:];
-[UIScrollViewPagingSwipeGestureRecognizer enoughTimeElapsed:];
-[UIScrollViewPagingSwipeGestureRecognizer scrollView];
-[UIScrollViewPagingSwipeGestureRecognizer dealloc];
-[UIScrollViewPagingSwipeGestureRecognizer setScrollView:];
-[UIScrollViewPagingSwipeGestureRecognizer touchesBegan:withEvent:];
-[UIScrollViewPagingSwipeGestureRecognizer touchesMoved:withEvent:];
-[UIScrollViewPagingSwipeGestureRecognizer _processNewLocation:];
```

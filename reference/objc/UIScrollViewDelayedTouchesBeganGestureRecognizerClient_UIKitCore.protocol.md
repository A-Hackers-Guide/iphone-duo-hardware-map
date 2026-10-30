# `UIScrollViewDelayedTouchesBeganGestureRecognizerClient` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 5 properties, 6 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) delaysContentTouches;
@property (Td,R,N,G_touchDelayForScrollDetection) touchDelayForScrollDetection;
@property (Td,R,N,G_scrollHysteresis) scrollHysteresis;
@property (TB,R,N,G_canScrollX) canScrollX;
@property (TB,R,N,G_canScrollY) canScrollY;
```

## Instance methods

```
-[UIScrollViewDelayedTouchesBeganGestureRecognizerClient _canScrollX];
-[UIScrollViewDelayedTouchesBeganGestureRecognizerClient _canScrollY];
-[UIScrollViewDelayedTouchesBeganGestureRecognizerClient _scrollHysteresis];
-[UIScrollViewDelayedTouchesBeganGestureRecognizerClient _touchDelayForScrollDetection];
-[UIScrollViewDelayedTouchesBeganGestureRecognizerClient delaysContentTouches];
-[UIScrollViewDelayedTouchesBeganGestureRecognizerClient touchesShouldBegin:withEvent:inContentView:];
```

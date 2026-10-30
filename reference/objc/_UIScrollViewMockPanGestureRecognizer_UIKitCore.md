# `_UIScrollViewMockPanGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _translation;
{CGPoint="x"d"y"d} _velocity;
q _state;
@"UIScrollViewPanGestureRecognizer" _gestureRecognizer;
```

## Properties

```
@property (T@"UIScrollViewPanGestureRecognizer",&,N,V_gestureRecognizer) gestureRecognizer;
@property (Tq,N) state;
```

## Instance methods

```
-[_UIScrollViewMockPanGestureRecognizer translationInView:];
-[_UIScrollViewMockPanGestureRecognizer velocityInView:];
-[_UIScrollViewMockPanGestureRecognizer setState:];
-[_UIScrollViewMockPanGestureRecognizer gestureRecognizer];
-[_UIScrollViewMockPanGestureRecognizer forwardingTargetForSelector:];
-[_UIScrollViewMockPanGestureRecognizer locationInView:];
-[_UIScrollViewMockPanGestureRecognizer setGestureRecognizer:];
-[_UIScrollViewMockPanGestureRecognizer state];
-[_UIScrollViewMockPanGestureRecognizer setTranslation:inView:];
-[_UIScrollViewMockPanGestureRecognizer simulateTranslation:velocity:];
```

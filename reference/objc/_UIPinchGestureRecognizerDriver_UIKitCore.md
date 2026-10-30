# `_UIPinchGestureRecognizerDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIGestureRecognizerDriver`
- 13 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
d _initialTouchDistance;
d _initialScale;
d _lastEventTime;
d _velocity;
d _previousVelocity;
d _lastNonZeroTimestampDelta;
d _scaleThreshold;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _transform;
d _hysteresis;
@"_UIGestureRecognizerTransformAnalyzer" _transformAnalyzer;
{?="endsOnSingleTouch"b1"receivedTwoTouches"b1} _flags;
{CGPoint="x"d"y"d} _anchorPoint;
{CGPoint="x"d"y"d} _initialAnchorPoint;
```

## Instance methods

```
-[_UIPinchGestureRecognizerDriver touchesEnded:withEvent:];
-[_UIPinchGestureRecognizerDriver touchesCancelled:withEvent:];
-[_UIPinchGestureRecognizerDriver init];
-[_UIPinchGestureRecognizerDriver reset];
-[_UIPinchGestureRecognizerDriver transformChangedWithEvent:];
-[_UIPinchGestureRecognizerDriver touchesBegan:withEvent:];
-[_UIPinchGestureRecognizerDriver touchesMoved:withEvent:];
-[_UIPinchGestureRecognizerDriver shouldReceiveComponent:withEvent:];
```

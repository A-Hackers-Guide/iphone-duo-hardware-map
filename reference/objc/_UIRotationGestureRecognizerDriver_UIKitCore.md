# `_UIRotationGestureRecognizerDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIGestureRecognizerDriver`
- 15 instance variables, 0 properties, 8 instance methods, 0 class methods

## Instance variables

```
d _initialTouchDistance;
d _initialTouchAngle;
d _currentTouchAngle;
q _currentRotationCount;
d _lastTouchTime;
d _velocity;
d _previousVelocity;
@"_UIGestureRecognizerTransformAnalyzer" _transformAnalyzer;
@"NSArray" _touches;
f _preRecognitionWeight;
f _postRecognitionWeight;
{?="receivedTwoTouches"b1} _flags;
B _hysteresisEnabled;
{CGPoint="x"d"y"d} _anchorPoint;
{CGPoint="x"d"y"d} _initialAnchorPoint;
```

## Instance methods

```
-[_UIRotationGestureRecognizerDriver touchesEnded:withEvent:];
-[_UIRotationGestureRecognizerDriver touchesCancelled:withEvent:];
-[_UIRotationGestureRecognizerDriver init];
-[_UIRotationGestureRecognizerDriver reset];
-[_UIRotationGestureRecognizerDriver transformChangedWithEvent:];
-[_UIRotationGestureRecognizerDriver touchesBegan:withEvent:];
-[_UIRotationGestureRecognizerDriver touchesMoved:withEvent:];
-[_UIRotationGestureRecognizerDriver shouldReceiveComponent:withEvent:];
```

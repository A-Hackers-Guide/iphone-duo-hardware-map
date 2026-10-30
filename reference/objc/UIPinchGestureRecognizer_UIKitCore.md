# `UIPinchGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 2 instance variables, 6 properties, 21 instance methods, 3 class methods

## Instance variables

```
@"_UIPinchGestureRecognizerDriver" _driver;
{?="shouldConsiderTransformEventTouchCompatibility"b1"evaluatedWantsTransformEventTouchCompatibility"b1"wantsTransformEventTouchCompatibilityIfNeeded"b1"needsTransformEventTouchCompatibility"b1} _flags;
```

## Properties

```
@property (Td,N) scaleThreshold;
@property (T{CGPoint=dd},R,N) anchorPoint;
@property (Td,N,G_hysteresis,S_setHysteresis:) hysteresis;
@property (T{CGAffineTransform=dddddd},N) transform;
@property (Td,N) scale;
@property (Td,R,N) velocity;
```

## Class methods

```
+[UIPinchGestureRecognizer supportsSecureCoding];
+[UIPinchGestureRecognizer _supportsDefaultTouchTypes];
+[UIPinchGestureRecognizer _supportsDefaultPressTypes];
```

## Instance methods

```
-[UIPinchGestureRecognizer _hysteresis];
-[UIPinchGestureRecognizer _resetGestureRecognizer];
-[UIPinchGestureRecognizer anchorPoint];
-[UIPinchGestureRecognizer _driver];
-[UIPinchGestureRecognizer _isGestureType:];
-[UIPinchGestureRecognizer numberOfTouches];
-[UIPinchGestureRecognizer setScale:];
-[UIPinchGestureRecognizer setTransform:];
-[UIPinchGestureRecognizer velocity];
-[UIPinchGestureRecognizer transform];
-[UIPinchGestureRecognizer initWithTarget:action:];
-[UIPinchGestureRecognizer locationInView:];
-[UIPinchGestureRecognizer scale];
-[UIPinchGestureRecognizer _shouldReceiveEvent:];
-[UIPinchGestureRecognizer locationOfTouch:inView:];
-[UIPinchGestureRecognizer _setHysteresis:];
-[UIPinchGestureRecognizer _endsOnSingleTouch];
-[UIPinchGestureRecognizer _evaluateTransformEventTouchCompatibility];
-[UIPinchGestureRecognizer _setEndsOnSingleTouch:];
-[UIPinchGestureRecognizer scaleThreshold];
-[UIPinchGestureRecognizer setScaleThreshold:];
```

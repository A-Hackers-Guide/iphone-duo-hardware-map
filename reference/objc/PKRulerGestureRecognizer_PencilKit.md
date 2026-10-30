# `PKRulerGestureRecognizer`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PKFreeTransformGestureRecognizer`
- 4 instance variables, 2 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSTimer" _startTimer;
B _initialSnap;
d _startDelay;
d _startSnapThreshold;
```

## Properties

```
@property (Td,N,V_startDelay) startDelay;
@property (Td,N,V_startSnapThreshold) startSnapThreshold;
```

## Instance methods

```
-[PKRulerGestureRecognizer touchesEnded:withEvent:];
-[PKRulerGestureRecognizer start];
-[PKRulerGestureRecognizer reset];
-[PKRulerGestureRecognizer touchesBegan:withEvent:];
-[PKRulerGestureRecognizer touchesMoved:withEvent:];
-[PKRulerGestureRecognizer initWithTarget:action:];
-[PKRulerGestureRecognizer stopTimer];
-[PKRulerGestureRecognizer startDelay];
-[PKRulerGestureRecognizer setStartDelay:];
-[PKRulerGestureRecognizer freeTransform];
-[PKRulerGestureRecognizer resetAndAccumulateTransform];
-[PKRulerGestureRecognizer rulerTransform];
-[PKRulerGestureRecognizer setStartSnapThreshold:];
-[PKRulerGestureRecognizer startSnapThreshold];
-[PKRulerGestureRecognizer unscaledFreeTransform];
```

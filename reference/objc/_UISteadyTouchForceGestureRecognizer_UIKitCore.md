# `_UISteadyTouchForceGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 7 instance variables, 1 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"CADisplayLink" _continuousEvaluationDisplayLink;
@"_UIVelocityIntegrator" _velocityIntegrator;
d _currentTouchForce;
@"NSDate" _steadyTimestamp;
B _useOverridingMinimumDuration;
d _overrideMinimumSteadyTouchForceDuration;
d _minimumSteadyTouchForceDuration;
```

## Properties

```
@property (Td,N,V_minimumSteadyTouchForceDuration) minimumSteadyTouchForceDuration;
```

## Instance methods

```
-[_UISteadyTouchForceGestureRecognizer touchesEnded:withEvent:];
-[_UISteadyTouchForceGestureRecognizer touchesCancelled:withEvent:];
-[_UISteadyTouchForceGestureRecognizer reset];
-[_UISteadyTouchForceGestureRecognizer setView:];
-[_UISteadyTouchForceGestureRecognizer touchesBegan:withEvent:];
-[_UISteadyTouchForceGestureRecognizer touchesMoved:withEvent:];
-[_UISteadyTouchForceGestureRecognizer initWithTarget:action:];
-[_UISteadyTouchForceGestureRecognizer cancel];
-[_UISteadyTouchForceGestureRecognizer _updateForContinuousEvaluation:];
-[_UISteadyTouchForceGestureRecognizer minimumSteadyTouchForceDuration];
-[_UISteadyTouchForceGestureRecognizer _adjustSteadyForceDurationIfNeeded:event:];
-[_UISteadyTouchForceGestureRecognizer _beginForContinuousEvaluationForTouches:];
-[_UISteadyTouchForceGestureRecognizer _endContinuousEvaluation];
-[_UISteadyTouchForceGestureRecognizer _evaluateTouches:];
-[_UISteadyTouchForceGestureRecognizer _evaluateWithTouchForce:];
-[_UISteadyTouchForceGestureRecognizer recognize];
-[_UISteadyTouchForceGestureRecognizer setMinimumSteadyTouchForceDuration:];
```

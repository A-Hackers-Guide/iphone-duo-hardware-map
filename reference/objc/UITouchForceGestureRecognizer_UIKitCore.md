# `UITouchForceGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 18 instance variables, 11 properties, 40 instance methods, 0 class methods

## Instance variables

```
@"CADisplayLink" _continuousEvaluationDisplayLink;
@"NSMutableSet" _currentTouches;
Q _eventTouchCount;
d _currentTouchForce;
{CGPoint="x"d"y"d} _initialCentroidOfTouches;
{CGPoint="x"d"y"d} _currentCentroidOfTouches;
@"_UIVelocityIntegrator" _velocityIntegrator;
B _automaticallyIncreaseTouchForce;
d _touchesBeganTimestamp;
B _steady;
d _touchForce;
d _minimumRequiredTouchForce;
d _velocity;
d _allowableMovement;
Q _maximumNumberOfTouches;
d _automaticTouchForce;
d _automaticTouchForceDuration;
@? _configurationBlock;
```

## Properties

```
@property (Td,N,V_touchForce) touchForce;
@property (Td,N,V_velocity) velocity;
@property (TB,N,GisSteady,V_steady) steady;
@property (Td,N,V_minimumRequiredTouchForce) minimumRequiredTouchForce;
@property (Td,N,V_allowableMovement) allowableMovement;
@property (TB,R,N) hasExceededAllowableMovement;
@property (TQ,N,V_maximumNumberOfTouches) maximumNumberOfTouches;
@property (Td,N,V_automaticTouchForce) automaticTouchForce;
@property (Td,N,V_automaticTouchForceDuration) automaticTouchForceDuration;
@property (Td,R,N) touchDuration;
@property (T@?,C,N,V_configurationBlock) configurationBlock;
```

## Instance methods

```
-[UITouchForceGestureRecognizer allowableMovement];
-[UITouchForceGestureRecognizer canPreventGestureRecognizer:];
-[UITouchForceGestureRecognizer touchesEnded:withEvent:];
-[UITouchForceGestureRecognizer touchesCancelled:withEvent:];
-[UITouchForceGestureRecognizer touchDuration];
-[UITouchForceGestureRecognizer setAllowableMovement:];
-[UITouchForceGestureRecognizer hasExceededAllowableMovement];
-[UITouchForceGestureRecognizer reset];
-[UITouchForceGestureRecognizer setView:];
-[UITouchForceGestureRecognizer velocity];
-[UITouchForceGestureRecognizer touchesBegan:withEvent:];
-[UITouchForceGestureRecognizer touchForce];
-[UITouchForceGestureRecognizer touchesMoved:withEvent:];
-[UITouchForceGestureRecognizer initWithTarget:action:];
-[UITouchForceGestureRecognizer setMaximumNumberOfTouches:];
-[UITouchForceGestureRecognizer setConfigurationBlock:];
-[UITouchForceGestureRecognizer configurationBlock];
-[UITouchForceGestureRecognizer maximumNumberOfTouches];
-[UITouchForceGestureRecognizer setVelocity:];
-[UITouchForceGestureRecognizer _shouldReceiveTouch:forEvent:recognizerView:];
-[UITouchForceGestureRecognizer _updateForContinuousEvaluation:];
-[UITouchForceGestureRecognizer setAutomaticTouchForceDuration:];
-[UITouchForceGestureRecognizer _beginForContinuousEvaluationForTouches:];
-[UITouchForceGestureRecognizer _endContinuousEvaluation];
-[UITouchForceGestureRecognizer _endIfNeeded:];
-[UITouchForceGestureRecognizer _evaluateAutomaticTouchForceForTimeInterval:actualTouchForce:];
-[UITouchForceGestureRecognizer _evaluateTouches:withEvent:];
-[UITouchForceGestureRecognizer _evaluateWithTouchForce:centroidAtLocation:];
-[UITouchForceGestureRecognizer _hasExceededAllowableMovement];
-[UITouchForceGestureRecognizer _hasExceededMaximumNumberOfTouches];
-[UITouchForceGestureRecognizer _updateTouchForce:];
-[UITouchForceGestureRecognizer _validateHysteresis];
-[UITouchForceGestureRecognizer automaticTouchForce];
-[UITouchForceGestureRecognizer automaticTouchForceDuration];
-[UITouchForceGestureRecognizer isSteady];
-[UITouchForceGestureRecognizer minimumRequiredTouchForce];
-[UITouchForceGestureRecognizer setAutomaticTouchForce:];
-[UITouchForceGestureRecognizer setMinimumRequiredTouchForce:];
-[UITouchForceGestureRecognizer setSteady:];
-[UITouchForceGestureRecognizer setTouchForce:];
```

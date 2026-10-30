# `_UIGestureStudyMetricsGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- Protocols: `_UIGestureStudyParticipating`
- 5 instance variables, 12 properties, 25 instance methods, 0 class methods

## Instance variables

```
q _observedTouchCount;
d _startTimestamp;
d _allowableMovement;
@"UITouch" _primaryTouch;
{CGPoint="x"d"y"d} _originalPosition;
```

## Properties

```
@property (Td,N,V_startTimestamp) startTimestamp;
@property (T{CGPoint=dd},N,V_originalPosition) originalPosition;
@property (Td,N,V_allowableMovement) allowableMovement;
@property (T@"UITouch",&,N,V_primaryTouch) primaryTouch;
@property (Tq,R,N,V_observedTouchCount) observedTouchCount;
@property (T@"NSString",R,N) eventName;
@property (Td,R,N) duration;
@property (Td,R,N) movement;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIGestureStudyMetricsGestureRecognizer allowableMovement];
-[_UIGestureStudyMetricsGestureRecognizer canPreventGestureRecognizer:];
-[_UIGestureStudyMetricsGestureRecognizer touchesEnded:withEvent:];
-[_UIGestureStudyMetricsGestureRecognizer _acceptsBeingFailureRequirementForGestureRecognizer:];
-[_UIGestureStudyMetricsGestureRecognizer canBePreventedByGestureRecognizer:];
-[_UIGestureStudyMetricsGestureRecognizer _acceptsBeingFailureDependentOnGestureRecognizer:];
-[_UIGestureStudyMetricsGestureRecognizer _canCancelGestureRecognizer:];
-[_UIGestureStudyMetricsGestureRecognizer locationInCoordinateSpace:];
-[_UIGestureStudyMetricsGestureRecognizer touchesCancelled:withEvent:];
-[_UIGestureStudyMetricsGestureRecognizer setAllowableMovement:];
-[_UIGestureStudyMetricsGestureRecognizer setStartTimestamp:];
-[_UIGestureStudyMetricsGestureRecognizer reset];
-[_UIGestureStudyMetricsGestureRecognizer touchesBegan:withEvent:];
-[_UIGestureStudyMetricsGestureRecognizer touchesMoved:withEvent:];
-[_UIGestureStudyMetricsGestureRecognizer initWithTarget:action:];
-[_UIGestureStudyMetricsGestureRecognizer duration];
-[_UIGestureStudyMetricsGestureRecognizer locationInView:];
-[_UIGestureStudyMetricsGestureRecognizer startTimestamp];
-[_UIGestureStudyMetricsGestureRecognizer eventName];
-[_UIGestureStudyMetricsGestureRecognizer movement];
-[_UIGestureStudyMetricsGestureRecognizer observedTouchCount];
-[_UIGestureStudyMetricsGestureRecognizer originalPosition];
-[_UIGestureStudyMetricsGestureRecognizer primaryTouch];
-[_UIGestureStudyMetricsGestureRecognizer setOriginalPosition:];
-[_UIGestureStudyMetricsGestureRecognizer setPrimaryTouch:];
```

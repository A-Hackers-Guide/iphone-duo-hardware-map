# `_UITouchForceObservable`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObservationSource`
- Protocols: `NSObserver`
- 7 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
q _observerCount;
@"_UITouchesObservingGestureRecognizer" _gestureRecognizer;
@"NSObservation" _touchesObservation;
@"CADisplayLink" _continuousEvaluationDisplayLink;
@"NSSet" _currentTouches;
d _lastObservationTime;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITouchForceObservable init];
-[_UITouchForceObservable initWithView:];
-[_UITouchForceObservable dealloc];
-[_UITouchForceObservable addObserver:];
-[_UITouchForceObservable receiveObservedValue:];
-[_UITouchForceObservable removeObservation:];
-[_UITouchForceObservable _unclampedTouchForceForTouches:];
-[_UITouchForceObservable _updateForContinuousEvaluation:];
-[_UITouchForceObservable _cancelContinuousEvaluation];
-[_UITouchForceObservable _didEndHavingAnyObservers];
-[_UITouchForceObservable _maximumPossibleForceForTouches:];
-[_UITouchForceObservable _shouldFilterDueToSystemGesturesForTouches:];
-[_UITouchForceObservable _timestampForTouches:];
-[_UITouchForceObservable _touchForceMessageForTouches:];
-[_UITouchForceObservable _willBeginHavingAnyObservers];
```

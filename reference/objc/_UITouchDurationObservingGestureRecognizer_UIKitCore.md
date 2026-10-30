# `_UITouchDurationObservingGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 9 instance variables, 10 properties, 30 instance methods, 0 class methods

## Instance variables

```
B _hasExceededAllowableMovement;
@"CADisplayLink" _displayLink;
@"_UIWeakGestureTarget" _weakTarget;
d _minimumDurationRequired;
d _allowableMovement;
d _touchForce;
d _touchStartTimestamp;
@"UIDelayedAction" _delayedAction;
{CGPoint="x"d"y"d} _originalCentroid;
```

## Properties

```
@property (T@"CADisplayLink",R,N,V_displayLink) displayLink;
@property (Td,N,V_touchStartTimestamp) touchStartTimestamp;
@property (T{CGPoint=dd},N,V_originalCentroid) originalCentroid;
@property (T@"UIDelayedAction",R,N,V_delayedAction) delayedAction;
@property (T@"_UIWeakGestureTarget",R,N,V_weakTarget) _weakTarget;
@property (Td,N,V_minimumDurationRequired) minimumDurationRequired;
@property (Td,N,V_allowableMovement) allowableMovement;
@property (TB,R,N,V_hasExceededAllowableMovement) hasExceededAllowableMovement;
@property (Td,R,N) touchDuration;
@property (Td,R,N,V_touchForce) touchForce;
```

## Instance methods

```
-[_UITouchDurationObservingGestureRecognizer allowableMovement];
-[_UITouchDurationObservingGestureRecognizer canPreventGestureRecognizer:];
-[_UITouchDurationObservingGestureRecognizer displayLink];
-[_UITouchDurationObservingGestureRecognizer touchesEnded:withEvent:];
-[_UITouchDurationObservingGestureRecognizer touchesCancelled:withEvent:];
-[_UITouchDurationObservingGestureRecognizer touchDuration];
-[_UITouchDurationObservingGestureRecognizer setAllowableMovement:];
-[_UITouchDurationObservingGestureRecognizer hasExceededAllowableMovement];
-[_UITouchDurationObservingGestureRecognizer _handleStateChange:];
-[_UITouchDurationObservingGestureRecognizer _exceededNumberOfTouchesForEvent:];
-[_UITouchDurationObservingGestureRecognizer _isGestureType:];
-[_UITouchDurationObservingGestureRecognizer dealloc];
-[_UITouchDurationObservingGestureRecognizer reset];
-[_UITouchDurationObservingGestureRecognizer setOriginalCentroid:];
-[_UITouchDurationObservingGestureRecognizer setView:];
-[_UITouchDurationObservingGestureRecognizer touchesBegan:withEvent:];
-[_UITouchDurationObservingGestureRecognizer touchForce];
-[_UITouchDurationObservingGestureRecognizer touchesMoved:withEvent:];
-[_UITouchDurationObservingGestureRecognizer initWithTarget:action:];
-[_UITouchDurationObservingGestureRecognizer _cancelOrFail];
-[_UITouchDurationObservingGestureRecognizer _allTouchesMatchingRequirementsForEvent:];
-[_UITouchDurationObservingGestureRecognizer _performDelayedBegin];
-[_UITouchDurationObservingGestureRecognizer _weakTarget];
-[_UITouchDurationObservingGestureRecognizer originalCentroid];
-[_UITouchDurationObservingGestureRecognizer _displayLinkDidFire:];
-[_UITouchDurationObservingGestureRecognizer setMinimumDurationRequired:];
-[_UITouchDurationObservingGestureRecognizer delayedAction];
-[_UITouchDurationObservingGestureRecognizer touchStartTimestamp];
-[_UITouchDurationObservingGestureRecognizer setTouchStartTimestamp:];
-[_UITouchDurationObservingGestureRecognizer minimumDurationRequired];
```

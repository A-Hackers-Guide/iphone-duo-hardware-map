# `_UITapTapHoldGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITapGestureRecognizer`
- 7 instance variables, 7 properties, 25 instance methods, 0 class methods

## Instance variables

```
B _isWaitingForHoldToAction;
B _isInHoldToAction;
B _isWaitingForTooSlowForDoubleTap;
i _currentNumberOfPresses;
q _gestureType;
d _startTime;
d _pressEventBeginTimestamp;
```

## Properties

```
@property (Ti,N,V_currentNumberOfPresses) currentNumberOfPresses;
@property (Td,N,V_startTime) startTime;
@property (Td,N,V_pressEventBeginTimestamp) pressEventBeginTimestamp;
@property (TB,N,V_isWaitingForHoldToAction) isWaitingForHoldToAction;
@property (TB,N,V_isInHoldToAction) isInHoldToAction;
@property (TB,N,V_isWaitingForTooSlowForDoubleTap) isWaitingForTooSlowForDoubleTap;
@property (Tq,N,V_gestureType) gestureType;
```

## Instance methods

```
-[_UITapTapHoldGestureRecognizer cancelPendingHoldToAction];
-[_UITapTapHoldGestureRecognizer isWaitingForHoldToAction];
-[_UITapTapHoldGestureRecognizer startTime];
-[_UITapTapHoldGestureRecognizer scheduleHoldToAction];
-[_UITapTapHoldGestureRecognizer pressesEnded:withEvent:];
-[_UITapTapHoldGestureRecognizer reset];
-[_UITapTapHoldGestureRecognizer setGestureType:];
-[_UITapTapHoldGestureRecognizer scheduleTooSlowForDoubleTap];
-[_UITapTapHoldGestureRecognizer setIsInHoldToAction:];
-[_UITapTapHoldGestureRecognizer isInHoldToAction];
-[_UITapTapHoldGestureRecognizer initWithTarget:action:];
-[_UITapTapHoldGestureRecognizer pressesBegan:withEvent:];
-[_UITapTapHoldGestureRecognizer _shouldFailInResponseToPresses:withEvent:];
-[_UITapTapHoldGestureRecognizer setStartTime:];
-[_UITapTapHoldGestureRecognizer gestureType];
-[_UITapTapHoldGestureRecognizer isWaitingForTooSlowForDoubleTap];
-[_UITapTapHoldGestureRecognizer setIsWaitingForHoldToAction:];
-[_UITapTapHoldGestureRecognizer cancelPendingTooSlowForDoubleTap];
-[_UITapTapHoldGestureRecognizer setIsWaitingForTooSlowForDoubleTap:];
-[_UITapTapHoldGestureRecognizer currentNumberOfPresses];
-[_UITapTapHoldGestureRecognizer tooSlowForDoubleTap:];
-[_UITapTapHoldGestureRecognizer pressEventBeginTimestamp];
-[_UITapTapHoldGestureRecognizer holdToAction:];
-[_UITapTapHoldGestureRecognizer setCurrentNumberOfPresses:];
-[_UITapTapHoldGestureRecognizer setPressEventBeginTimestamp:];
```

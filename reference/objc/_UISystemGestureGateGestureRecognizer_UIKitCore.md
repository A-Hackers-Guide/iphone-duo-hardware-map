# `_UISystemGestureGateGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 5 instance variables, 0 properties, 21 instance methods, 2 class methods

## Instance variables

```
C _systemGestureGateType;
b1 _systemGesturesRecognitionPossible;
b1 _waitingForSystemGestureStateNotification;
d _lastTouchTime;
@"NSObject<OS_dispatch_source>" _delayTimeoutTimer;
```

## Class methods

```
+[_UISystemGestureGateGestureRecognizer _supportsDefaultTouchTypes];
+[_UISystemGestureGateGestureRecognizer _supportsDefaultPressTypes];
```

## Instance methods

```
-[_UISystemGestureGateGestureRecognizer _isAllowedToReceiveGESEvents];
-[_UISystemGestureGateGestureRecognizer canPreventGestureRecognizer:];
-[_UISystemGestureGateGestureRecognizer touchesEnded:withEvent:];
-[_UISystemGestureGateGestureRecognizer canBePreventedByGestureRecognizer:];
-[_UISystemGestureGateGestureRecognizer _acceptsBeingFailureDependentOnGestureRecognizer:];
-[_UISystemGestureGateGestureRecognizer _resetGestureRecognizer];
-[_UISystemGestureGateGestureRecognizer touchesCancelled:withEvent:];
-[_UISystemGestureGateGestureRecognizer _gateGestureTypeString];
-[_UISystemGestureGateGestureRecognizer dealloc];
-[_UISystemGestureGateGestureRecognizer setDelaysTouchesEnded:];
-[_UISystemGestureGateGestureRecognizer touchesBegan:withEvent:];
-[_UISystemGestureGateGestureRecognizer initWithTarget:action:];
-[_UISystemGestureGateGestureRecognizer shouldBeRequiredToFailByGestureRecognizer:];
-[_UISystemGestureGateGestureRecognizer _notifyWindowNoLongerAwaitingSystemGestureNotification:];
-[_UISystemGestureGateGestureRecognizer _systemGestureStateChanged:];
-[_UISystemGestureGateGestureRecognizer setEnabled:];
-[_UISystemGestureGateGestureRecognizer initWithWindow:type:];
-[_UISystemGestureGateGestureRecognizer _cancelTimeoutTimerIfNeeded];
-[_UISystemGestureGateGestureRecognizer initWithCoder:];
-[_UISystemGestureGateGestureRecognizer _timeOut];
-[_UISystemGestureGateGestureRecognizer setDelaysTouchesBegan:];
```

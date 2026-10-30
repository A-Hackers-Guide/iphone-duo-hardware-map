# `_UILongPressClickInteractionDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegatePrivate`, `_UIClickInteractionDriving`
- 10 instance variables, 23 properties, 42 instance methods, 2 class methods

## Instance variables

```
Q _currentState;
{?="didUpdateHighlightProgress"B"shouldDelayGesture"B"shouldBeDelayedByGesture"B} _delegateImplements;
Q _behavior;
B _cancelsTouchesInView;
B _reachedClickDownThreshold;
@"<_UIClickInteractionDriverDelegate>" _delegate;
@"UIView" _view;
d _clickDownDuration;
@"_UITouchDurationObservingGestureRecognizer" _gestureRecognizer;
d _forceMultiplier;
```

## Properties

```
@property (T@"_UITouchDurationObservingGestureRecognizer",&,N,V_gestureRecognizer) gestureRecognizer;
@property (Td,N,V_clickDownDuration) clickDownDuration;
@property (Td,N,V_forceMultiplier) forceMultiplier;
@property (TB,N,V_reachedClickDownThreshold) reachedClickDownThreshold;
@property (Td,R,N) clickTimeoutDuration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<_UIClickInteractionDriverDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",W,N,V_view) view;
@property (Td,N) allowableMovement;
@property (TB,N,V_cancelsTouchesInView) cancelsTouchesInView;
@property (T@"UIGestureRecognizer",R,N) primaryGestureRecognizer;
@property (Td,R,N) touchDuration;
@property (TB,R,N) hasExceededAllowableMovement;
@property (TB,R,N) isCurrentlyAcceleratedByForce;
@property (TB,R,N) clicksUpAutomaticallyAfterTimeout;
@property (Td,R,N) maximumEffectProgress;
@property (TQ,R,N) inputPrecision;
@property (TQ,?,N) driverStyle;
@property (TB,?,R,N) allowsFeedback;
@property (TQ,?,N) behavior;
```

## Class methods

```
+[_UILongPressClickInteractionDriver prefersCancelsTouchesInView];
+[_UILongPressClickInteractionDriver requiresForceCapability];
```

## Instance methods

```
-[_UILongPressClickInteractionDriver allowableMovement];
-[_UILongPressClickInteractionDriver setCancelsTouchesInView:];
-[_UILongPressClickInteractionDriver _gestureRecognizerFailed:];
-[_UILongPressClickInteractionDriver inputPrecision];
-[_UILongPressClickInteractionDriver isCurrentlyAcceleratedByForce];
-[_UILongPressClickInteractionDriver gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[_UILongPressClickInteractionDriver locationInCoordinateSpace:];
-[_UILongPressClickInteractionDriver clicksUpAutomaticallyAfterTimeout];
-[_UILongPressClickInteractionDriver allowsFeedback];
-[_UILongPressClickInteractionDriver touchDuration];
-[_UILongPressClickInteractionDriver cancelInteraction];
-[_UILongPressClickInteractionDriver setAllowableMovement:];
-[_UILongPressClickInteractionDriver _handleGestureRecognizer:];
-[_UILongPressClickInteractionDriver gestureRecognizer:shouldReceiveTouch:];
-[_UILongPressClickInteractionDriver hasExceededAllowableMovement];
-[_UILongPressClickInteractionDriver maximumEffectProgress];
-[_UILongPressClickInteractionDriver primaryGestureRecognizer];
-[_UILongPressClickInteractionDriver cancelsTouchesInView];
-[_UILongPressClickInteractionDriver gestureRecognizer];
-[_UILongPressClickInteractionDriver init];
-[_UILongPressClickInteractionDriver clickTimeoutDuration];
-[_UILongPressClickInteractionDriver setView:];
-[_UILongPressClickInteractionDriver view];
-[_UILongPressClickInteractionDriver setDelegate:];
-[_UILongPressClickInteractionDriver setBehavior:];
-[_UILongPressClickInteractionDriver behavior];
-[_UILongPressClickInteractionDriver gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UILongPressClickInteractionDriver gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UILongPressClickInteractionDriver delegate];
-[_UILongPressClickInteractionDriver setGestureRecognizer:];
-[_UILongPressClickInteractionDriver description];
-[_UILongPressClickInteractionDriver clickDownDuration];
-[_UILongPressClickInteractionDriver _gestureRecognizer:canCancelGestureRecognizer:];
-[_UILongPressClickInteractionDriver forceMultiplier];
-[_UILongPressClickInteractionDriver _asyncGestureBegan];
-[_UILongPressClickInteractionDriver _notifyDelegateOfUpdatedClickDownProgress:forceAdjustedClickDownDuration:];
-[_UILongPressClickInteractionDriver _updateForActiveGestureRecognizer];
-[_UILongPressClickInteractionDriver _updateTimeoutDebugUI:];
-[_UILongPressClickInteractionDriver reachedClickDownThreshold];
-[_UILongPressClickInteractionDriver setClickDownDuration:];
-[_UILongPressClickInteractionDriver setForceMultiplier:];
-[_UILongPressClickInteractionDriver setReachedClickDownThreshold:];
```

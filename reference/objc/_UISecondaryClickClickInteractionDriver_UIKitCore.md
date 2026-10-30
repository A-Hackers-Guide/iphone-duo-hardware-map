# `_UISecondaryClickClickInteractionDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UIClickInteractionDriving`
- 8 instance variables, 19 properties, 31 instance methods, 2 class methods

## Instance variables

```
Q _currentState;
B _cancelsTouchesInView;
B _clicksUpAutomaticallyAfterTimeout;
@"<_UIClickInteractionDriverDelegate>" _delegate;
@"UIView" _view;
d _allowableMovement;
Q behavior;
@"_UISecondaryClickDriverGestureRecognizer" _gestureRecognizer;
```

## Properties

```
@property (T@"_UISecondaryClickDriverGestureRecognizer",&,N,V_gestureRecognizer) gestureRecognizer;
@property (TQ,N,Vbehavior) behavior;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<_UIClickInteractionDriverDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",W,N,V_view) view;
@property (Td,N,V_allowableMovement) allowableMovement;
@property (TB,N,V_cancelsTouchesInView) cancelsTouchesInView;
@property (T@"UIGestureRecognizer",R,N) primaryGestureRecognizer;
@property (Td,R,N) touchDuration;
@property (TB,R,N) hasExceededAllowableMovement;
@property (TB,R,N) isCurrentlyAcceleratedByForce;
@property (TB,R,N,V_clicksUpAutomaticallyAfterTimeout) clicksUpAutomaticallyAfterTimeout;
@property (Td,R,N) maximumEffectProgress;
@property (TQ,R,N) inputPrecision;
@property (TQ,?,N) driverStyle;
@property (TB,?,R,N) allowsFeedback;
```

## Class methods

```
+[_UISecondaryClickClickInteractionDriver prefersCancelsTouchesInView];
+[_UISecondaryClickClickInteractionDriver requiresForceCapability];
```

## Instance methods

```
-[_UISecondaryClickClickInteractionDriver allowableMovement];
-[_UISecondaryClickClickInteractionDriver setCancelsTouchesInView:];
-[_UISecondaryClickClickInteractionDriver _gestureRecognizerFailed:];
-[_UISecondaryClickClickInteractionDriver inputPrecision];
-[_UISecondaryClickClickInteractionDriver isCurrentlyAcceleratedByForce];
-[_UISecondaryClickClickInteractionDriver locationInCoordinateSpace:];
-[_UISecondaryClickClickInteractionDriver clicksUpAutomaticallyAfterTimeout];
-[_UISecondaryClickClickInteractionDriver allowsFeedback];
-[_UISecondaryClickClickInteractionDriver touchDuration];
-[_UISecondaryClickClickInteractionDriver cancelInteraction];
-[_UISecondaryClickClickInteractionDriver setAllowableMovement:];
-[_UISecondaryClickClickInteractionDriver _handleGestureRecognizer:];
-[_UISecondaryClickClickInteractionDriver gestureRecognizer:shouldReceiveTouch:];
-[_UISecondaryClickClickInteractionDriver hasExceededAllowableMovement];
-[_UISecondaryClickClickInteractionDriver maximumEffectProgress];
-[_UISecondaryClickClickInteractionDriver primaryGestureRecognizer];
-[_UISecondaryClickClickInteractionDriver cancelsTouchesInView];
-[_UISecondaryClickClickInteractionDriver gestureRecognizer];
-[_UISecondaryClickClickInteractionDriver init];
-[_UISecondaryClickClickInteractionDriver setView:];
-[_UISecondaryClickClickInteractionDriver _attemptSecondaryClick];
-[_UISecondaryClickClickInteractionDriver view];
-[_UISecondaryClickClickInteractionDriver setDelegate:];
-[_UISecondaryClickClickInteractionDriver setBehavior:];
-[_UISecondaryClickClickInteractionDriver behavior];
-[_UISecondaryClickClickInteractionDriver gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UISecondaryClickClickInteractionDriver gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UISecondaryClickClickInteractionDriver delegate];
-[_UISecondaryClickClickInteractionDriver setGestureRecognizer:];
-[_UISecondaryClickClickInteractionDriver driverStyle];
-[_UISecondaryClickClickInteractionDriver _gestureRecognizer:canCancelGestureRecognizer:];
```

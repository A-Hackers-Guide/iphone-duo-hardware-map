# `_UITouchDownClickInteractionDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIClickInteractionDriving`, `UIGestureRecognizerDelegate`
- 7 instance variables, 18 properties, 24 instance methods, 2 class methods

## Instance variables

```
@"_UITouchDownGestureRecognizer" _gesture;
B _cancelsTouchesInView;
B _clicksUpAutomaticallyAfterTimeout;
@"<_UIClickInteractionDriverDelegate>" _delegate;
@"UIView" _view;
d _allowableMovement;
Q _inputPrecision;
```

## Properties

```
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
@property (TQ,R,N,V_inputPrecision) inputPrecision;
@property (TQ,?,N) driverStyle;
@property (TB,?,R,N) allowsFeedback;
@property (TQ,?,N) behavior;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UITouchDownClickInteractionDriver prefersCancelsTouchesInView];
+[_UITouchDownClickInteractionDriver requiresForceCapability];
```

## Instance methods

```
-[_UITouchDownClickInteractionDriver allowableMovement];
-[_UITouchDownClickInteractionDriver setCancelsTouchesInView:];
-[_UITouchDownClickInteractionDriver inputPrecision];
-[_UITouchDownClickInteractionDriver isCurrentlyAcceleratedByForce];
-[_UITouchDownClickInteractionDriver gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[_UITouchDownClickInteractionDriver locationInCoordinateSpace:];
-[_UITouchDownClickInteractionDriver clicksUpAutomaticallyAfterTimeout];
-[_UITouchDownClickInteractionDriver allowsFeedback];
-[_UITouchDownClickInteractionDriver touchDuration];
-[_UITouchDownClickInteractionDriver cancelInteraction];
-[_UITouchDownClickInteractionDriver setAllowableMovement:];
-[_UITouchDownClickInteractionDriver _handleGestureRecognizer:];
-[_UITouchDownClickInteractionDriver hasExceededAllowableMovement];
-[_UITouchDownClickInteractionDriver maximumEffectProgress];
-[_UITouchDownClickInteractionDriver primaryGestureRecognizer];
-[_UITouchDownClickInteractionDriver cancelsTouchesInView];
-[_UITouchDownClickInteractionDriver init];
-[_UITouchDownClickInteractionDriver setView:];
-[_UITouchDownClickInteractionDriver view];
-[_UITouchDownClickInteractionDriver setDelegate:];
-[_UITouchDownClickInteractionDriver gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UITouchDownClickInteractionDriver gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UITouchDownClickInteractionDriver delegate];
-[_UITouchDownClickInteractionDriver _gestureRecognizer:canCancelGestureRecognizer:];
```

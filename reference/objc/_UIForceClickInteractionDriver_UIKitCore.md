# `_UIForceClickInteractionDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegatePrivate`, `_UIClickInteractionDriving`
- 5 instance variables, 20 properties, 25 instance methods, 2 class methods

## Instance variables

```
Q _currentState;
B _cancelsTouchesInView;
@"<_UIClickInteractionDriverDelegate>" _delegate;
@"UIView" _view;
@"UITouchForceGestureRecognizer" _gestureRecognizer;
```

## Properties

```
@property (T@"UITouchForceGestureRecognizer",&,N,V_gestureRecognizer) gestureRecognizer;
@property (Td,R,N) touchForce;
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
+[_UIForceClickInteractionDriver prefersCancelsTouchesInView];
+[_UIForceClickInteractionDriver requiresForceCapability];
```

## Instance methods

```
-[_UIForceClickInteractionDriver allowableMovement];
-[_UIForceClickInteractionDriver setCancelsTouchesInView:];
-[_UIForceClickInteractionDriver _gestureRecognizerFailed:];
-[_UIForceClickInteractionDriver inputPrecision];
-[_UIForceClickInteractionDriver isCurrentlyAcceleratedByForce];
-[_UIForceClickInteractionDriver locationInCoordinateSpace:];
-[_UIForceClickInteractionDriver clicksUpAutomaticallyAfterTimeout];
-[_UIForceClickInteractionDriver touchDuration];
-[_UIForceClickInteractionDriver cancelInteraction];
-[_UIForceClickInteractionDriver setAllowableMovement:];
-[_UIForceClickInteractionDriver _handleGestureRecognizer:];
-[_UIForceClickInteractionDriver hasExceededAllowableMovement];
-[_UIForceClickInteractionDriver maximumEffectProgress];
-[_UIForceClickInteractionDriver primaryGestureRecognizer];
-[_UIForceClickInteractionDriver cancelsTouchesInView];
-[_UIForceClickInteractionDriver gestureRecognizer];
-[_UIForceClickInteractionDriver init];
-[_UIForceClickInteractionDriver setView:];
-[_UIForceClickInteractionDriver touchForce];
-[_UIForceClickInteractionDriver view];
-[_UIForceClickInteractionDriver setDelegate:];
-[_UIForceClickInteractionDriver gestureRecognizer:shouldBeRequiredToFailByGestureRecognizer:];
-[_UIForceClickInteractionDriver delegate];
-[_UIForceClickInteractionDriver setGestureRecognizer:];
-[_UIForceClickInteractionDriver allowsRepeatedClicks];
```

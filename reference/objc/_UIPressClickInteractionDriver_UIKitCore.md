# `_UIPressClickInteractionDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UIClickInteractionDriving`
- 6 instance variables, 20 properties, 28 instance methods, 2 class methods

## Instance variables

```
B _cancelsTouchesInView;
@"<_UIClickInteractionDriverDelegate>" _delegate;
@"UIView" _view;
d _allowableMovement;
@"NSArray" _triggers;
@"_UISimplePressGestureRecognizer" _pressGR;
```

## Properties

```
@property (T@"_UISimplePressGestureRecognizer",&,N,V_pressGR) pressGR;
@property (T@"NSArray",&,N,V_triggers) triggers;
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
@property (TB,R,N) clicksUpAutomaticallyAfterTimeout;
@property (Td,R,N) maximumEffectProgress;
@property (TQ,R,N) inputPrecision;
@property (TQ,?,N) driverStyle;
@property (TB,?,R,N) allowsFeedback;
@property (TQ,?,N) behavior;
```

## Class methods

```
+[_UIPressClickInteractionDriver prefersCancelsTouchesInView];
+[_UIPressClickInteractionDriver requiresForceCapability];
```

## Instance methods

```
-[_UIPressClickInteractionDriver allowableMovement];
-[_UIPressClickInteractionDriver setCancelsTouchesInView:];
-[_UIPressClickInteractionDriver _gestureRecognizerFailed:];
-[_UIPressClickInteractionDriver inputPrecision];
-[_UIPressClickInteractionDriver setTriggers:];
-[_UIPressClickInteractionDriver isCurrentlyAcceleratedByForce];
-[_UIPressClickInteractionDriver locationInCoordinateSpace:];
-[_UIPressClickInteractionDriver clicksUpAutomaticallyAfterTimeout];
-[_UIPressClickInteractionDriver allowsFeedback];
-[_UIPressClickInteractionDriver touchDuration];
-[_UIPressClickInteractionDriver cancelInteraction];
-[_UIPressClickInteractionDriver setAllowableMovement:];
-[_UIPressClickInteractionDriver hasExceededAllowableMovement];
-[_UIPressClickInteractionDriver maximumEffectProgress];
-[_UIPressClickInteractionDriver primaryGestureRecognizer];
-[_UIPressClickInteractionDriver cancelsTouchesInView];
-[_UIPressClickInteractionDriver init];
-[_UIPressClickInteractionDriver _handlePressGesture:];
-[_UIPressClickInteractionDriver pressGR];
-[_UIPressClickInteractionDriver setView:];
-[_UIPressClickInteractionDriver triggers];
-[_UIPressClickInteractionDriver view];
-[_UIPressClickInteractionDriver setDelegate:];
-[_UIPressClickInteractionDriver setPressGR:];
-[_UIPressClickInteractionDriver _removeFromView];
-[_UIPressClickInteractionDriver delegate];
-[_UIPressClickInteractionDriver driverStyle];
-[_UIPressClickInteractionDriver _addToView:];
```

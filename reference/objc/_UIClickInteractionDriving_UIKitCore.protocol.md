# `_UIClickInteractionDriving` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 16 properties, 22 instance methods, 2 class methods

## Properties

```
@property (T@"<_UIClickInteractionDriverDelegate>",W,N) delegate;
@property (T@"UIView",W,N) view;
@property (Td,N) allowableMovement;
@property (TB,N) cancelsTouchesInView;
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
@property (class, TB,R,N) requiresForceCapability;
@property (class, TB,R,N) prefersCancelsTouchesInView;
```

## Class methods

```
+[_UIClickInteractionDriving prefersCancelsTouchesInView];
+[_UIClickInteractionDriving requiresForceCapability];
```

## Instance methods

```
-[_UIClickInteractionDriving allowableMovement];
-[_UIClickInteractionDriving setCancelsTouchesInView:];
-[_UIClickInteractionDriving inputPrecision];
-[_UIClickInteractionDriving isCurrentlyAcceleratedByForce];
-[_UIClickInteractionDriving locationInCoordinateSpace:];
-[_UIClickInteractionDriving clicksUpAutomaticallyAfterTimeout];
-[_UIClickInteractionDriving touchDuration];
-[_UIClickInteractionDriving cancelInteraction];
-[_UIClickInteractionDriving setAllowableMovement:];
-[_UIClickInteractionDriving hasExceededAllowableMovement];
-[_UIClickInteractionDriving maximumEffectProgress];
-[_UIClickInteractionDriving primaryGestureRecognizer];
-[_UIClickInteractionDriving cancelsTouchesInView];
-[_UIClickInteractionDriving setView:];
-[_UIClickInteractionDriving view];
-[_UIClickInteractionDriving setDelegate:];
-[_UIClickInteractionDriving delegate];
-[_UIClickInteractionDriving allowsFeedback];
-[_UIClickInteractionDriving setBehavior:];
-[_UIClickInteractionDriving behavior];
-[_UIClickInteractionDriving driverStyle];
-[_UIClickInteractionDriving setDriverStyle:];
```

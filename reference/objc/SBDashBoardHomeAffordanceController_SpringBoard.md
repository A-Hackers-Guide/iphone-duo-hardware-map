# `SBDashBoardHomeAffordanceController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSHomeAffordanceControlling`
- 1 instance variables, 8 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"SBNotificationHomeAffordanceController" _notificationHomeAffordanceController;
```

## Properties

```
@property (T@"UIPanGestureRecognizer",R,N) screenEdgePanGesture;
@property (T@"BSAnimationSettings",R,N) hideHomeAffordanceAnimationSettings;
@property (T@"BSAnimationSettings",R,N) unhideHomeAffordanceAnimationSettings;
@property (T@"<UIViewSpringAnimationBehaviorDescribing>",R,N) settleHomeAffordanceAnimationBehaviorDescription;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDashBoardHomeAffordanceController initWithWindowScene:];
-[SBDashBoardHomeAffordanceController hideHomeAffordanceAnimationSettings];
-[SBDashBoardHomeAffordanceController keyboardAssertionForGestureWindow:];
-[SBDashBoardHomeAffordanceController registerHomeGestureParticipant:withIdentifier:];
-[SBDashBoardHomeAffordanceController screenEdgePanGesture];
-[SBDashBoardHomeAffordanceController settleHomeAffordanceAnimationBehaviorDescription];
-[SBDashBoardHomeAffordanceController unhideHomeAffordanceAnimationSettings];
-[SBDashBoardHomeAffordanceController unregisterHomeGestureParticipant:withIdentifier:];
```

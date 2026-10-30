# `SBNotificationHomeAffordanceController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFZStackParticipantDelegate`
- 3 instance variables, 8 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"NSMapTable" _clientsToZStackParticipants;
@"SBHomeGesturePanGestureRecognizer" _screenEdgePanGesture;
```

## Properties

```
@property (T@"SBScreenEdgePanGestureRecognizer",R,N) screenEdgePanGesture;
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
-[SBNotificationHomeAffordanceController zStackParticipant:updatePreferences:];
-[SBNotificationHomeAffordanceController zStackParticipantDidChange:];
-[SBNotificationHomeAffordanceController initWithWindowScene:];
-[SBNotificationHomeAffordanceController hideHomeAffordanceAnimationSettings];
-[SBNotificationHomeAffordanceController screenEdgePanGesture];
-[SBNotificationHomeAffordanceController settleHomeAffordanceAnimationBehaviorDescription];
-[SBNotificationHomeAffordanceController unhideHomeAffordanceAnimationSettings];
-[SBNotificationHomeAffordanceController registerClient:withZStackIdentifier:];
-[SBNotificationHomeAffordanceController unregisterClient:withZStackIdentifier:];
```

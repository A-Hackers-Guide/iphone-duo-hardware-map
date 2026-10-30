# `SBNotificationPresentableViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NCNotificationPresentableViewController`
- Protocols: `SBBannerManagerPresentable`, `SBButtonEventsHandler`, `SBBarSwipeAffordanceObserver`, `SBUIPresentableLocalHomeGestureParticipant`
- 1 instance variables, 15 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"<SBUIPresentableHomeGestureContext>" _homeGestureContext;
```

## Properties

```
@property (Tq,?,R,N) presentableBehavior;
@property (T@"<BNPresentableContext>",?,W,N) presentableContext;
@property (T@"NSSet",?,R,C,N) preferredBackgroundActivitiesToSuppress;
@property (TB,?,R,N,GisDraggingDismissalEnabled) draggingDismissalEnabled;
@property (TB,?,R,N,GisDraggingInteractionEnabled) draggingInteractionEnabled;
@property (TB,?,R,N,GisTouchOutsideDismissalEnabled) touchOutsideDismissalEnabled;
@property (T@"UIViewController",?,R,N) viewController;
@property (Tq,?,R,N) presentableType;
@property (T@"NSString",R,C,N) requesterIdentifier;
@property (T@"NSString",R,C,N) requestIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBUIPresentableHomeGestureContext>",W,N,V_homeGestureContext) homeGestureContext;
```

## Instance methods

```
-[SBNotificationPresentableViewController handleVolumeDownButtonPress];
-[SBNotificationPresentableViewController handleHomeButtonLongPress];
-[SBNotificationPresentableViewController handleVoiceCommandButtonPress];
-[SBNotificationPresentableViewController longLookDidPresentForNotificationViewController:];
-[SBNotificationPresentableViewController homeGestureContext];
-[SBNotificationPresentableViewController handleHeadsetButtonPress:];
-[SBNotificationPresentableViewController handleLockButtonPress];
-[SBNotificationPresentableViewController handleVolumeUpButtonPress];
-[SBNotificationPresentableViewController homeGesturePerformedForBarSwipeAffordanceView:];
-[SBNotificationPresentableViewController shouldDismissForReason:outReason:];
-[SBNotificationPresentableViewController longLookWillPresentForNotificationViewController:];
-[SBNotificationPresentableViewController handleHomeButtonDoublePress];
-[SBNotificationPresentableViewController setHomeGestureContext:];
-[SBNotificationPresentableViewController shouldAcquireWindowLevelAssertion];
-[SBNotificationPresentableViewController longLookWillDismissForNotificationViewController:];
-[SBNotificationPresentableViewController handleHomeButtonPress];
```

# `SBBarSwipeAffordanceViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBBarSwipeAffordanceControlling`
- 1 instance variables, 14 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"SBBarSwipeAffordanceController" _barSwipeAffordanceController;
```

## Properties

```
@property (T@"SBBarSwipeAffordanceView",&,D,N) view;
@property (T@"<SBBarSwipeAffordanceControllingDelegate>",W,N) delegate;
@property (T@"SBBarSwipeAffordanceView",R,N) barSwipeAffordanceView;
@property (TB,N) wantsToBeActiveAffordance;
@property (TB,N) suppressAffordance;
@property (TB,N) allowsTouchesToPassThrough;
@property (Tq,N) activationPolicyForParticipantsBelow;
@property (TB,N) suppressSystemApertureForSystemChromeSuppression;
@property (T@"SBFZStackParticipant",R,N) zStackParticipant;
@property (T@"<SBHomeGrabberPointerClickDelegate>",W,N) pointerClickDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBarSwipeAffordanceViewController zStackParticipant];
-[SBBarSwipeAffordanceViewController setPointerClickDelegate:];
-[SBBarSwipeAffordanceViewController setSuppressAffordance:];
-[SBBarSwipeAffordanceViewController allowsTouchesToPassThrough];
-[SBBarSwipeAffordanceViewController zStackParticipant:updatePreferences:];
-[SBBarSwipeAffordanceViewController setAllowsTouchesToPassThrough:];
-[SBBarSwipeAffordanceViewController pointerClickDelegate];
-[SBBarSwipeAffordanceViewController zStackParticipantDidChange:];
-[SBBarSwipeAffordanceViewController activationPolicyForParticipantsBelow];
-[SBBarSwipeAffordanceViewController setSuppressSystemApertureForSystemChromeSuppression:];
-[SBBarSwipeAffordanceViewController _canShowWhileLocked];
-[SBBarSwipeAffordanceViewController setDelegate:];
-[SBBarSwipeAffordanceViewController barSwipeAffordanceView];
-[SBBarSwipeAffordanceViewController suppressSystemApertureForSystemChromeSuppression];
-[SBBarSwipeAffordanceViewController loadView];
-[SBBarSwipeAffordanceViewController initWithZStackParticipantIdentifier:windowScene:];
-[SBBarSwipeAffordanceViewController delegate];
-[SBBarSwipeAffordanceViewController wantsToBeActiveAffordance];
-[SBBarSwipeAffordanceViewController setActivationPolicyForParticipantsBelow:];
-[SBBarSwipeAffordanceViewController setWantsToBeActiveAffordance:];
-[SBBarSwipeAffordanceViewController suppressAffordance];
```

# `SBBarSwipeAffordanceControlling` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SBFZStackParticipantDelegate`
- 0 instance variables, 9 properties, 16 instance methods, 0 class methods

## Properties

```
@property (T@"<SBBarSwipeAffordanceControllingDelegate>",W,N) delegate;
@property (T@"SBBarSwipeAffordanceView",R,N) barSwipeAffordanceView;
@property (TB,N) wantsToBeActiveAffordance;
@property (TB,N) suppressAffordance;
@property (TB,N) allowsTouchesToPassThrough;
@property (Tq,N) activationPolicyForParticipantsBelow;
@property (TB,N) suppressSystemApertureForSystemChromeSuppression;
@property (T@"SBFZStackParticipant",R,N) zStackParticipant;
@property (T@"<SBHomeGrabberPointerClickDelegate>",W,N) pointerClickDelegate;
```

## Instance methods

```
-[SBBarSwipeAffordanceControlling zStackParticipant];
-[SBBarSwipeAffordanceControlling setPointerClickDelegate:];
-[SBBarSwipeAffordanceControlling setSuppressAffordance:];
-[SBBarSwipeAffordanceControlling allowsTouchesToPassThrough];
-[SBBarSwipeAffordanceControlling setAllowsTouchesToPassThrough:];
-[SBBarSwipeAffordanceControlling pointerClickDelegate];
-[SBBarSwipeAffordanceControlling activationPolicyForParticipantsBelow];
-[SBBarSwipeAffordanceControlling setSuppressSystemApertureForSystemChromeSuppression:];
-[SBBarSwipeAffordanceControlling setDelegate:];
-[SBBarSwipeAffordanceControlling barSwipeAffordanceView];
-[SBBarSwipeAffordanceControlling suppressSystemApertureForSystemChromeSuppression];
-[SBBarSwipeAffordanceControlling delegate];
-[SBBarSwipeAffordanceControlling wantsToBeActiveAffordance];
-[SBBarSwipeAffordanceControlling setActivationPolicyForParticipantsBelow:];
-[SBBarSwipeAffordanceControlling setWantsToBeActiveAffordance:];
-[SBBarSwipeAffordanceControlling suppressAffordance];
```

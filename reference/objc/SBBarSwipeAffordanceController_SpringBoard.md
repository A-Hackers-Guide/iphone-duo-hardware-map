# `SBBarSwipeAffordanceController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBarSwipeAffordanceControlling`
- 11 instance variables, 14 properties, 30 instance methods, 0 class methods

## Instance variables

```
q _zStackParticipantIdentifier;
B _wantsToBeActiveAffordance;
B _suppressAffordance;
B _allowsTouchesToPassThrough;
B _suppressSystemApertureForSystemChromeSuppression;
@"<SBBarSwipeAffordanceControllingDelegate>" _delegate;
@"SBBarSwipeAffordanceView" _barSwipeAffordanceView;
q _activationPolicyForParticipantsBelow;
@"<SBHomeGrabberPointerClickDelegate>" _pointerClickDelegate;
@"SBFZStackParticipant" _zStackParticipant;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBFZStackParticipant",&,N,V_zStackParticipant) zStackParticipant;
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (T@"<SBBarSwipeAffordanceControllingDelegate>",W,N,V_delegate) delegate;
@property (T@"SBBarSwipeAffordanceView",R,N,V_barSwipeAffordanceView) barSwipeAffordanceView;
@property (TB,N,V_wantsToBeActiveAffordance) wantsToBeActiveAffordance;
@property (TB,N,V_suppressAffordance) suppressAffordance;
@property (TB,N,V_allowsTouchesToPassThrough) allowsTouchesToPassThrough;
@property (Tq,N,V_activationPolicyForParticipantsBelow) activationPolicyForParticipantsBelow;
@property (TB,N,V_suppressSystemApertureForSystemChromeSuppression) suppressSystemApertureForSystemChromeSuppression;
@property (T@"<SBHomeGrabberPointerClickDelegate>",W,N,V_pointerClickDelegate) pointerClickDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBarSwipeAffordanceController zStackParticipant];
-[SBBarSwipeAffordanceController setZStackParticipant:];
-[SBBarSwipeAffordanceController setWindowScene:];
-[SBBarSwipeAffordanceController setPointerClickDelegate:];
-[SBBarSwipeAffordanceController setSuppressAffordance:];
-[SBBarSwipeAffordanceController _keyboardWillHide:];
-[SBBarSwipeAffordanceController allowsTouchesToPassThrough];
-[SBBarSwipeAffordanceController zStackParticipant:updatePreferences:];
-[SBBarSwipeAffordanceController setAllowsTouchesToPassThrough:];
-[SBBarSwipeAffordanceController pointerClickDelegate];
-[SBBarSwipeAffordanceController dealloc];
-[SBBarSwipeAffordanceController zStackParticipantDidChange:];
-[SBBarSwipeAffordanceController zStackParticipant:updateZOrderPreferences:];
-[SBBarSwipeAffordanceController activationPolicyForParticipantsBelow];
-[SBBarSwipeAffordanceController setSuppressSystemApertureForSystemChromeSuppression:];
-[SBBarSwipeAffordanceController _keyboardDidShow:];
-[SBBarSwipeAffordanceController setDelegate:];
-[SBBarSwipeAffordanceController barSwipeAffordanceView];
-[SBBarSwipeAffordanceController suppressSystemApertureForSystemChromeSuppression];
-[SBBarSwipeAffordanceController initWithZStackParticipantIdentifier:windowScene:];
-[SBBarSwipeAffordanceController delegate];
-[SBBarSwipeAffordanceController wantsToBeActiveAffordance];
-[SBBarSwipeAffordanceController windowScene];
-[SBBarSwipeAffordanceController setActivationPolicyForParticipantsBelow:];
-[SBBarSwipeAffordanceController setWantsToBeActiveAffordance:];
-[SBBarSwipeAffordanceController suppressAffordance];
-[SBBarSwipeAffordanceController _updateActiveState];
-[SBBarSwipeAffordanceController _setKeyboardHomeAffordanceVisible:];
-[SBBarSwipeAffordanceController _beginTryingToBecomeActiveAffordance];
-[SBBarSwipeAffordanceController _stopTryingToBecomeActiveAffordance];
```

# `SBPlatterHomeGestureContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBarSwipeAffordanceControllingDelegate`, `SBBarSwipeAffordanceDelegate`, `SBUIPresentableHomeGestureContext`, `SBPlatterHomeGestureViewProviding`
- 5 instance variables, 8 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBBarSwipeAffordanceController" _barSwipeAffordanceController;
@"<BSInvalidatable>" _gestureRecognizerPriorityAssertion;
B _wantsToBeActiveAffordance;
@"<SBPlatterHomeGestureContextDelegate>" _delegate;
@"<SBUIPresentableHomeGestureParticipant>" _participant;
```

## Properties

```
@property (T@"<SBUIPresentableHomeGestureParticipant>",R,W,N,V_participant) participant;
@property (T@"<SBPlatterHomeGestureContextDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,V_wantsToBeActiveAffordance) wantsToBeActiveAffordance;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) ownsHomeGesture;
```

## Instance methods

```
-[SBPlatterHomeGestureContext setWantsHomeGesture:];
-[SBPlatterHomeGestureContext ownsHomeGesture];
-[SBPlatterHomeGestureContext participant];
-[SBPlatterHomeGestureContext zStackParticipant:updatePreferences:];
-[SBPlatterHomeGestureContext barSwipeAffordanceView:systemGestureTypeForType:];
-[SBPlatterHomeGestureContext dealloc];
-[SBPlatterHomeGestureContext zStackParticipantDidChange:];
-[SBPlatterHomeGestureContext setDelegate:];
-[SBPlatterHomeGestureContext delegate];
-[SBPlatterHomeGestureContext wantsToBeActiveAffordance];
-[SBPlatterHomeGestureContext keyboardHomeAffordanceAssertionForBarSwipeAffordanceControlling:];
-[SBPlatterHomeGestureContext hideAnimationSettingsForBarSwipeAffordanceView:];
-[SBPlatterHomeGestureContext unhideAnimationSettingsForBarSwipeAffordanceView:];
-[SBPlatterHomeGestureContext platterBarSwipeAffordanceViewForParticipant:];
-[SBPlatterHomeGestureContext _setOwnsHomeGesture:];
-[SBPlatterHomeGestureContext becomeActiveAffordanceIfPossible:];
-[SBPlatterHomeGestureContext initWithParticipant:participantIdentifier:windowScene:];
```

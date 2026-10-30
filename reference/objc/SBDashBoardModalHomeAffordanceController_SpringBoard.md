# `SBDashBoardModalHomeAffordanceController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFZStackParticipantDelegate`, `SBHomeGrabberDelegate`, `CSModalHomeAffordanceControlling`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"SBFZStackParticipant" _zStackParticipant;
@"<CSModalHomeGestureParticipating>" _homeGestureParticipant;
@"SBHomeGrabberView" _homeGrabberView;
@"UIScreenEdgePanGestureRecognizer" _homeGestureRecognizer;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIScreenEdgePanGestureRecognizer",&,N,V_homeGestureRecognizer) homeGestureRecognizer;
```

## Instance methods

```
-[SBDashBoardModalHomeAffordanceController ownsHomeGesture];
-[SBDashBoardModalHomeAffordanceController zStackParticipant:updatePreferences:];
-[SBDashBoardModalHomeAffordanceController zStackParticipantDidChange:];
-[SBDashBoardModalHomeAffordanceController zStackParticipant:updateZOrderPreferences:];
-[SBDashBoardModalHomeAffordanceController initWithWindowScene:];
-[SBDashBoardModalHomeAffordanceController setNeedsUpdateZStackPreferencesWithReason:];
-[SBDashBoardModalHomeAffordanceController additionalEdgeSpacingForHomeGrabberView:];
-[SBDashBoardModalHomeAffordanceController registerHomeGestureParticipant:];
-[SBDashBoardModalHomeAffordanceController setHomeGestureRecognizer:];
-[SBDashBoardModalHomeAffordanceController unregisterHomeGestureParticipant];
-[SBDashBoardModalHomeAffordanceController homeGestureRecognizer];
-[SBDashBoardModalHomeAffordanceController setNeedsUpdateZStackZOrderPreferencesWithReason:];
```

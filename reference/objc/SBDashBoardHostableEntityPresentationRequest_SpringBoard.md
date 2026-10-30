# `SBDashBoardHostableEntityPresentationRequest`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 6 properties, 7 instance methods, 0 class methods

## Instance variables

```
B _animated;
B _isEphemeralSwitcher;
B _dismissGestureEnabled;
@"<CSHostableEntity>" _entity;
@"SBMainWorkspaceTransitionRequest" _transitionRequest;
@? _presentationCompletion;
```

## Properties

```
@property (T@"<CSHostableEntity>",R,N,V_entity) entity;
@property (T@"SBMainWorkspaceTransitionRequest",R,N,V_transitionRequest) transitionRequest;
@property (TB,R,N,V_animated) animated;
@property (TB,R,N,V_isEphemeralSwitcher) isEphemeralSwitcher;
@property (TB,R,N,V_dismissGestureEnabled) dismissGestureEnabled;
@property (T@?,R,C,N,V_presentationCompletion) presentationCompletion;
```

## Instance methods

```
-[SBDashBoardHostableEntityPresentationRequest isEphemeralSwitcher];
-[SBDashBoardHostableEntityPresentationRequest animated];
-[SBDashBoardHostableEntityPresentationRequest entity];
-[SBDashBoardHostableEntityPresentationRequest presentationCompletion];
-[SBDashBoardHostableEntityPresentationRequest dismissGestureEnabled];
-[SBDashBoardHostableEntityPresentationRequest initWithEntity:transitionRequest:animated:isEphemeralSwitcher:dismissGestureEnabled:presentationCompletion:];
-[SBDashBoardHostableEntityPresentationRequest transitionRequest];
```

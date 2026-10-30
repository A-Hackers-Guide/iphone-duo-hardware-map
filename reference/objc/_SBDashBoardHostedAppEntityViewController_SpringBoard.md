# `_SBDashBoardHostedAppEntityViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDashBoardHostedAppViewController`
- Protocols: `CSHostableEntityPresenting`
- 1 instance variables, 12 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<CSHostableEntityPresenterDelegate>" _entityPresenterDelegate;
```

## Properties

```
@property (T@"<CSHostableEntityPresenterDelegate>",W,N,V_entityPresenterDelegate) entityPresenterDelegate;
@property (Tq,?,N) hostableEntityContentMode;
@property (T@"NSSet",?,C,N) actionsToDeliverToHostableEntity;
@property (Tq,?,R,N) hostableEntityOrientation;
@property (T@"SBApplicationSceneHandle",?,R,N) sceneHandleForTraitsParticipant;
@property (T@"FBScene",?,R,N) sceneForTraitsParticipant;
@property (T@"SBHomeGrabberView",?,R,N) homeGrabberViewForTraitsParticipant;
@property (T@"UIView<SBFSwitcherIconZooming>",?,R,N) iconZoomingView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBDashBoardHostedAppEntityViewController appViewControllerShouldBackgroundApplicationOnDeactivate:];
-[_SBDashBoardHostedAppEntityViewController setEntityPresenterDelegate:];
-[_SBDashBoardHostedAppEntityViewController conformsToCSHostableEntityPresenting];
-[_SBDashBoardHostedAppEntityViewController setHostableEntityContentMode:];
-[_SBDashBoardHostedAppEntityViewController sceneHandleForTraitsParticipant];
-[_SBDashBoardHostedAppEntityViewController entityPresenterDelegate];
-[_SBDashBoardHostedAppEntityViewController homeGrabberViewForTraitsParticipant];
-[_SBDashBoardHostedAppEntityViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[_SBDashBoardHostedAppEntityViewController hostableEntityOrientation];
-[_SBDashBoardHostedAppEntityViewController invalidateForReplacementByEntity:];
-[_SBDashBoardHostedAppEntityViewController setActionsToDeliverToHostableEntity:];
-[_SBDashBoardHostedAppEntityViewController actionsToDeliverToHostableEntity];
-[_SBDashBoardHostedAppEntityViewController hostableEntityContentMode];
```

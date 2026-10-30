# `CSHostableEntityPresenting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 8 properties, 15 instance methods, 0 class methods

## Properties

```
@property (T@"<CSHostableEntityPresenterDelegate>",W,N) entityPresenterDelegate;
@property (Tq,?,N) hostableEntityContentMode;
@property (T@"NSSet",?,C,N) actionsToDeliverToHostableEntity;
@property (Tq,?,R,N) hostableEntityOrientation;
@property (T@"SBApplicationSceneHandle",?,R,N) sceneHandleForTraitsParticipant;
@property (T@"FBScene",?,R,N) sceneForTraitsParticipant;
@property (T@"SBHomeGrabberView",?,R,N) homeGrabberViewForTraitsParticipant;
@property (T@"UIView<SBFSwitcherIconZooming>",?,R,N) iconZoomingView;
```

## Instance methods

```
-[CSHostableEntityPresenting setEntityPresenterDelegate:];
-[CSHostableEntityPresenting conformsToCSHostableEntityPresenting];
-[CSHostableEntityPresenting entityPresenterDelegate];
-[CSHostableEntityPresenting iconZoomingView];
-[CSHostableEntityPresenting setHostableEntityContentMode:];
-[CSHostableEntityPresenting sceneHandleForTraitsParticipant];
-[CSHostableEntityPresenting homeGrabberViewForTraitsParticipant];
-[CSHostableEntityPresenting sceneForTraitsParticipant];
-[CSHostableEntityPresenting hostableEntityOrientation];
-[CSHostableEntityPresenting invalidateForReplacementByEntity:];
-[CSHostableEntityPresenting setActionsToDeliverToHostableEntity:];
-[CSHostableEntityPresenting actionsToDeliverToHostableEntity];
-[CSHostableEntityPresenting hostableEntityContentMode];
-[CSHostableEntityPresenting handleEntityWillDismissFromBottomSwipeGesture];
-[CSHostableEntityPresenting launchMonitorWillTerminate];
```

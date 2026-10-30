# `SBDashBoardFluidSwitcherLiveContentOverlayCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSwitcherLiveContentOverlayCoordinating`
- 6 instance variables, 10 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _liveContentOverlayUpdatesSuspended;
@"SBWindowScene" _sbWindowScene;
q _containerOrientation;
@"<SBSwitcherLiveContentOverlayCoordinatorDelegate>" _delegate;
@"<SBDashBoardFluidSwitcherLiveContentOverlayCoordinatorDataSource>" _dataSource;
@"NSMapTable" _liveContentOverlaysByLeafAppLayout;
```

## Properties

```
@property (T@"NSMapTable",&,N,V_liveContentOverlaysByLeafAppLayout) liveContentOverlaysByLeafAppLayout;
@property (T@"SBWindowScene",R,W,N,V_sbWindowScene) sbWindowScene;
@property (T@"<SBDashBoardFluidSwitcherLiveContentOverlayCoordinatorDataSource>",W,N,V_dataSource) dataSource;
@property (TB,N,GareLiveContentOverlayUpdatesSuspended,V_liveContentOverlayUpdatesSuspended) liveContentOverlayUpdatesSuspended;
@property (Tq,N,V_containerOrientation) containerOrientation;
@property (T@"<SBSwitcherLiveContentOverlayCoordinatorDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator cleanUpAfterCoordinatedLayoutStateTransitionWithContext:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator containerOrientation];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator noteKeyboardFocusDidChangeToSceneID:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator areLiveContentOverlayUpdatesSuspended];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator setLiveContentOverlayUpdatesSuspended:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator setContainerOrientation:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator appLayoutWillBecomeVisible:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator prepareForCoordinatedLayoutStateTransitionWithContext:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator appLayoutDidBecomeHidden:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator setDataSource:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator initWithWindowScene:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator invalidate];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator setDelegate:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator dataSource];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator wantsHomeAffordanceAutoHideForAppLayout:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator didRotateFromInterfaceOrientation:toInterfaceOrientation:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator appLayoutForKeyboardFocusedScene];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator willRotateFromInterfaceOrientation:toInterfaceOrientation:alongsideContainerView:animated:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator wantsEdgeProtectForHomeGestureForAppLayout:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator delegate];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator appLayoutForSceneIdentifier:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator itemContainerForAppLayout:willBeReusedForAppLayout:];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator liveContentOverlaysByLeafAppLayout];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator sbWindowScene];
-[SBDashBoardFluidSwitcherLiveContentOverlayCoordinator setLiveContentOverlaysByLeafAppLayout:];
```

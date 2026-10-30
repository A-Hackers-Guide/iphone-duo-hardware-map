# `SBSwitcherLiveContentOverlayCoordinating` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SBLayoutStateTransitionObserver`
- 0 instance variables, 3 properties, 26 instance methods, 0 class methods

## Properties

```
@property (TB,N,GareLiveContentOverlayUpdatesSuspended) liveContentOverlayUpdatesSuspended;
@property (Tq,N) containerOrientation;
@property (T@"<SBSwitcherLiveContentOverlayCoordinatorDelegate>",W,N) delegate;
```

## Instance methods

```
-[SBSwitcherLiveContentOverlayCoordinating cleanUpAfterCoordinatedLayoutStateTransitionWithContext:];
-[SBSwitcherLiveContentOverlayCoordinating containerOrientation];
-[SBSwitcherLiveContentOverlayCoordinating noteKeyboardFocusDidChangeToSceneID:];
-[SBSwitcherLiveContentOverlayCoordinating areLiveContentOverlayUpdatesSuspended];
-[SBSwitcherLiveContentOverlayCoordinating setLiveContentOverlayUpdatesSuspended:];
-[SBSwitcherLiveContentOverlayCoordinating setContainerOrientation:];
-[SBSwitcherLiveContentOverlayCoordinating appLayoutWillBecomeVisible:];
-[SBSwitcherLiveContentOverlayCoordinating prepareForCoordinatedLayoutStateTransitionWithContext:];
-[SBSwitcherLiveContentOverlayCoordinating appLayoutDidBecomeHidden:];
-[SBSwitcherLiveContentOverlayCoordinating invalidate];
-[SBSwitcherLiveContentOverlayCoordinating setDelegate:];
-[SBSwitcherLiveContentOverlayCoordinating wantsHomeAffordanceAutoHideForAppLayout:];
-[SBSwitcherLiveContentOverlayCoordinating didRotateFromInterfaceOrientation:toInterfaceOrientation:];
-[SBSwitcherLiveContentOverlayCoordinating appLayoutForKeyboardFocusedScene];
-[SBSwitcherLiveContentOverlayCoordinating willRotateFromInterfaceOrientation:toInterfaceOrientation:alongsideContainerView:animated:];
-[SBSwitcherLiveContentOverlayCoordinating wantsEdgeProtectForHomeGestureForAppLayout:];
-[SBSwitcherLiveContentOverlayCoordinating delegate];
-[SBSwitcherLiveContentOverlayCoordinating appLayoutForSceneIdentifier:];
-[SBSwitcherLiveContentOverlayCoordinating itemContainerForAppLayout:willBeReusedForAppLayout:];
-[SBSwitcherLiveContentOverlayCoordinating prepareContentOverlaysForMoveToWindowScene:];
-[SBSwitcherLiveContentOverlayCoordinating groupOpacityRequiredWhenRemovingItemContainerForLeafAppLayout:];
-[SBSwitcherLiveContentOverlayCoordinating endInteractiveDisplayModeTransitionAtMode:forAppLayout:];
-[SBSwitcherLiveContentOverlayCoordinating updateInteractiveDisplayModeTransitionProgress:forAppLayout:];
-[SBSwitcherLiveContentOverlayCoordinating beginInteractiveDisplayModeTransitionToMode:forAppLayout:];
-[SBSwitcherLiveContentOverlayCoordinating setSceneViewDisplayMode:forAppLayout:animationFactory:];
-[SBSwitcherLiveContentOverlayCoordinating willPerformNonAnimatedTransitionToInterfaceOrientation:];
```

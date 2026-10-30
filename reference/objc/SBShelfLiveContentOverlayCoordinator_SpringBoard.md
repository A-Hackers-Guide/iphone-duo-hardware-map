# `SBShelfLiveContentOverlayCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAppSwitcherSnapshotImageCacheObserver`, `SBSwitcherLiveContentOverlayCoordinating`
- 7 instance variables, 8 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _leafAppLayoutsToOverlays;
B _isSnapshotCacheObserver;
@"SBApplicationController" _applicationController;
B liveContentOverlayUpdatesSuspended;
q containerOrientation;
@"<SBSwitcherLiveContentOverlayCoordinatorDelegate>" delegate;
@"<SBShelfLiveContentOverlayCoordinatorDelegate>" _shelfDelegate;
```

## Properties

```
@property (T@"<SBShelfLiveContentOverlayCoordinatorDelegate>",R,W,N,V_shelfDelegate) shelfDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,GareLiveContentOverlayUpdatesSuspended,VliveContentOverlayUpdatesSuspended) liveContentOverlayUpdatesSuspended;
@property (Tq,N,VcontainerOrientation) containerOrientation;
@property (T@"<SBSwitcherLiveContentOverlayCoordinatorDelegate>",W,N,Vdelegate) delegate;
```

## Instance methods

```
-[SBShelfLiveContentOverlayCoordinator layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBShelfLiveContentOverlayCoordinator cleanUpAfterCoordinatedLayoutStateTransitionWithContext:];
-[SBShelfLiveContentOverlayCoordinator containerOrientation];
-[SBShelfLiveContentOverlayCoordinator layoutStateTransitionCoordinator:transitionWillEndWithTransitionContext:];
-[SBShelfLiveContentOverlayCoordinator noteKeyboardFocusDidChangeToSceneID:];
-[SBShelfLiveContentOverlayCoordinator areLiveContentOverlayUpdatesSuspended];
-[SBShelfLiveContentOverlayCoordinator setLiveContentOverlayUpdatesSuspended:];
-[SBShelfLiveContentOverlayCoordinator setContainerOrientation:];
-[SBShelfLiveContentOverlayCoordinator appLayoutWillBecomeVisible:];
-[SBShelfLiveContentOverlayCoordinator prepareForCoordinatedLayoutStateTransitionWithContext:];
-[SBShelfLiveContentOverlayCoordinator dealloc];
-[SBShelfLiveContentOverlayCoordinator appLayoutDidBecomeHidden:];
-[SBShelfLiveContentOverlayCoordinator didUpdateCacheEntry:];
-[SBShelfLiveContentOverlayCoordinator invalidate];
-[SBShelfLiveContentOverlayCoordinator setDelegate:];
-[SBShelfLiveContentOverlayCoordinator layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBShelfLiveContentOverlayCoordinator wantsHomeAffordanceAutoHideForAppLayout:];
-[SBShelfLiveContentOverlayCoordinator didRotateFromInterfaceOrientation:toInterfaceOrientation:];
-[SBShelfLiveContentOverlayCoordinator appLayoutForKeyboardFocusedScene];
-[SBShelfLiveContentOverlayCoordinator willRotateFromInterfaceOrientation:toInterfaceOrientation:alongsideContainerView:animated:];
-[SBShelfLiveContentOverlayCoordinator wantsEdgeProtectForHomeGestureForAppLayout:];
-[SBShelfLiveContentOverlayCoordinator delegate];
-[SBShelfLiveContentOverlayCoordinator appLayoutForSceneIdentifier:];
-[SBShelfLiveContentOverlayCoordinator itemContainerForAppLayout:willBeReusedForAppLayout:];
-[SBShelfLiveContentOverlayCoordinator _addOverlaysIfNeededForTransitionContext:];
-[SBShelfLiveContentOverlayCoordinator initWithShelfDelegate:applicationController:];
-[SBShelfLiveContentOverlayCoordinator shelfDelegate];
```

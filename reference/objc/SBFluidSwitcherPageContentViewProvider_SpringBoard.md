# `SBFluidSwitcherPageContentViewProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAppSwitcherTransientOverlayPageContentViewDelegate`
- 7 instance variables, 5 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"<SBFluidSwitcherPageContentViewProviderDelegate>" _delegate;
@"SBAppSwitcherSnapshotImageCache" _snapshotCache;
@"SBAppSwitcherSnapshotLockoutViewControllerProvider" _lockoutVCProvider;
@"NSMapTable" _pageContentViewToTransientOverlayViewController;
@"NSMutableArray" _transientOverlayPageContentViews;
@"NSMutableDictionary" _switcherServiceViewControllerMap;
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (T@"<SBFluidSwitcherPageContentViewProviderDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFluidSwitcherPageContentViewProvider _interfaceOrientation];
-[SBFluidSwitcherPageContentViewProvider init];
-[SBFluidSwitcherPageContentViewProvider setDelegate:];
-[SBFluidSwitcherPageContentViewProvider delegate];
-[SBFluidSwitcherPageContentViewProvider _applyTransientOverlayViewController:toPageContentView:];
-[SBFluidSwitcherPageContentViewProvider _containerViewController];
-[SBFluidSwitcherPageContentViewProvider _pageViewSizeForAppLayout:];
-[SBFluidSwitcherPageContentViewProvider _preferredContentInterfaceOrientationForViewController:preferredInterfaceOrientation:];
-[SBFluidSwitcherPageContentViewProvider _relinquishTransientOverlayViewController:forPageContentView:];
-[SBFluidSwitcherPageContentViewProvider _snapshotViewDelegate];
-[SBFluidSwitcherPageContentViewProvider _snapshotViewForAppLayout:setActive:];
-[SBFluidSwitcherPageContentViewProvider _viewForService:appLayout:];
-[SBFluidSwitcherPageContentViewProvider acquiredViewController:forTransientOverlayAppLayout:];
-[SBFluidSwitcherPageContentViewProvider appSwitcherTransientOverlayPageContentViewDidChangeActive:];
-[SBFluidSwitcherPageContentViewProvider appSwitcherTransientOverlayPageContentViewDidChangeContainerOrientation:];
-[SBFluidSwitcherPageContentViewProvider existingTransientOverlayViewControllerForAppLayout:];
-[SBFluidSwitcherPageContentViewProvider initWithDelegate:snapshotCache:lockoutViewProvider:applicationController:];
-[SBFluidSwitcherPageContentViewProvider isSuitableForRecycledItemContainer:];
-[SBFluidSwitcherPageContentViewProvider pageContentViewForAppLayout:setActive:];
-[SBFluidSwitcherPageContentViewProvider purgePageContentViewForAppLayout:];
-[SBFluidSwitcherPageContentViewProvider relinquishTransientOverlayViewController:];
```

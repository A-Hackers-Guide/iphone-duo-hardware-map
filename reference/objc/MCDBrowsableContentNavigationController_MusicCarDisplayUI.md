# `MCDBrowsableContentNavigationController`

- Image: [`/System/Library/PrivateFrameworks/MusicCarDisplayUI.framework/MusicCarDisplayUI`](../userland/System__Library__PrivateFrameworks__MusicCarDisplayUI.framework__MusicCarDisplayUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UITabBarController`
- Protocols: `UITabBarControllerDelegate`, `MCDPCContainerDelegate`
- 11 instance variables, 15 properties, 38 instance methods, 0 class methods

## Instance variables

```
B _hasCarScreen;
B _didFinishInitialLoad;
B _didFinishInitialViewAppear;
B _visible;
B _hasInvalidatedDummyTabs;
@"MCDPCContainer" _container;
@"UITabBarController" _tabBarController;
@"MCDPCModel" _model;
@"NSString" _bundleID;
@"CPUINowPlayingButton" _nowPlayingButton;
@"NSObject<OS_dispatch_queue>" _serialQueue;
```

## Properties

```
@property (T@"UITabBarController",&,N,V_tabBarController) tabBarController;
@property (T@"MCDPCModel",&,N,V_model) model;
@property (T@"NSString",&,N,V_bundleID) bundleID;
@property (T@"CPUINowPlayingButton",&,N,V_nowPlayingButton) nowPlayingButton;
@property (TB,N,V_hasCarScreen) hasCarScreen;
@property (T@"MCDPCContainer",&,N,V_container) container;
@property (TB,N,V_didFinishInitialLoad) didFinishInitialLoad;
@property (TB,N,V_didFinishInitialViewAppear) didFinishInitialViewAppear;
@property (TB,N,V_visible) visible;
@property (TB,N,V_hasInvalidatedDummyTabs) hasInvalidatedDummyTabs;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_serialQueue) serialQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[MCDBrowsableContentNavigationController model];
-[MCDBrowsableContentNavigationController setModel:];
-[MCDBrowsableContentNavigationController visible];
-[MCDBrowsableContentNavigationController serialQueue];
-[MCDBrowsableContentNavigationController setVisible:];
-[MCDBrowsableContentNavigationController tabBarController:didSelectViewController:];
-[MCDBrowsableContentNavigationController viewWillDisappear:];
-[MCDBrowsableContentNavigationController setBundleID:];
-[MCDBrowsableContentNavigationController setContainer:];
-[MCDBrowsableContentNavigationController setSerialQueue:];
-[MCDBrowsableContentNavigationController tabBarController];
-[MCDBrowsableContentNavigationController viewWillAppear:];
-[MCDBrowsableContentNavigationController viewDidAppear:];
-[MCDBrowsableContentNavigationController traitCollectionDidChange:];
-[MCDBrowsableContentNavigationController bundleID];
-[MCDBrowsableContentNavigationController setTabBarController:];
-[MCDBrowsableContentNavigationController container];
-[MCDBrowsableContentNavigationController didFinishInitialLoad];
-[MCDBrowsableContentNavigationController setDidFinishInitialLoad:];
-[MCDBrowsableContentNavigationController _nowPlayingButtonTapped:];
-[MCDBrowsableContentNavigationController _appRegisteredForContent:];
-[MCDBrowsableContentNavigationController _hostTabAtIndex:dummyTab:];
-[MCDBrowsableContentNavigationController _loadAllHostTabs];
-[MCDBrowsableContentNavigationController _nowPlayingDidChange:];
-[MCDBrowsableContentNavigationController _tabBarItemForViewController:fromItem:];
-[MCDBrowsableContentNavigationController _updateNowPlayingButtonVisibility];
-[MCDBrowsableContentNavigationController container:didInvalidateIndicies:];
-[MCDBrowsableContentNavigationController didFinishInitialViewAppear];
-[MCDBrowsableContentNavigationController hasCarScreen];
-[MCDBrowsableContentNavigationController hasInvalidatedDummyTabs];
-[MCDBrowsableContentNavigationController initWithBundleID:model:];
-[MCDBrowsableContentNavigationController invalidateAndReloadTabsWithCompletion:];
-[MCDBrowsableContentNavigationController nowPlayingButton];
-[MCDBrowsableContentNavigationController setDidFinishInitialViewAppear:];
-[MCDBrowsableContentNavigationController setHasCarScreen:];
-[MCDBrowsableContentNavigationController setHasInvalidatedDummyTabs:];
-[MCDBrowsableContentNavigationController setNowPlayingButton:];
-[MCDBrowsableContentNavigationController updateTitleAndTabBarItemsAtIndexes:];
```

# `SBHomeScreenViewControllerContextProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 14 instance methods, 0 class methods

## Properties

```
@property (T@"SBTodayViewController",R,N) todayViewController;
@property (T@"SBTodayViewController",R,N) coverSheetTodayViewController;
@property (T@"SBFolderController",R,N,G_openFolderController) openFolderController;
@property (T@"SBHomeScreenOverlayController",&,N) homeScreenOverlayController;
```

## Instance methods

```
-[SBHomeScreenViewControllerContextProviding libraryViewControllerForWindowScene:];
-[SBHomeScreenViewControllerContextProviding coverSheetTodayViewController];
-[SBHomeScreenViewControllerContextProviding addFloatingDockControllerObserver:];
-[SBHomeScreenViewControllerContextProviding setHomeScreenOverlayController:];
-[SBHomeScreenViewControllerContextProviding _openFolderController];
-[SBHomeScreenViewControllerContextProviding todayViewController];
-[SBHomeScreenViewControllerContextProviding homeScreenOverlayController];
-[SBHomeScreenViewControllerContextProviding dismissAppIconForceTouchControllers:];
-[SBHomeScreenViewControllerContextProviding dismissHomeScreenOverlayUsingTransitionCoordinator:];
-[SBHomeScreenViewControllerContextProviding removeFloatingDockControllerObserver:];
-[SBHomeScreenViewControllerContextProviding homeScreenViewControllerSupportsMultipleVisiblePageSlots:];
-[SBHomeScreenViewControllerContextProviding homeScreenViewControllerDidFinishOrientationTransition:];
-[SBHomeScreenViewControllerContextProviding homeScreenViewController:willTransitionToOrientation:];
-[SBHomeScreenViewControllerContextProviding updateDockEdgeForHomeScreenViewController:];
```

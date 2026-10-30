# `SBFloatingDockHomeScreenContextProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SBIconModelProviding`
- 0 instance variables, 7 properties, 8 instance methods, 0 class methods

## Properties

```
@property (T@"SBHIconManager",R,N) iconManager;
@property (T@"<SBHFocusNavigationGestureRecognizerDelegate>",R,N) navigationDelegate;
@property (T@"SBHomeScreenViewController",R,N) homeScreenViewController;
@property (T@"SBRootFolderController",R,N,G_rootFolderController) rootFolderController;
@property (T@"SBFolderController",R,N,G_openFolderController) openFolderController;
@property (TB,R,N) areAnyIconViewContextMenusShowing;
@property (Tq,R,N) transitioningToOrientation;
```

## Instance methods

```
-[SBFloatingDockHomeScreenContextProviding iconManager];
-[SBFloatingDockHomeScreenContextProviding homeScreenViewController];
-[SBFloatingDockHomeScreenContextProviding navigationDelegate];
-[SBFloatingDockHomeScreenContextProviding _openFolderController];
-[SBFloatingDockHomeScreenContextProviding _rootFolderController];
-[SBFloatingDockHomeScreenContextProviding areAnyIconViewContextMenusShowing];
-[SBFloatingDockHomeScreenContextProviding dismissAppIconForceTouchControllers:];
-[SBFloatingDockHomeScreenContextProviding transitioningToOrientation];
```

# `SBFloatingDockSuggestionsViewProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `SBIconViewQuerying`, `SBIconLocationPresenting`
- 0 instance variables, 2 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"SBFloatingDockViewController",W,N) floatingDockViewController;
@property (T@"SBDockIconListView",R,N) listView;
```

## Instance methods

```
-[SBFloatingDockSuggestionsViewProviding floatingDockViewController];
-[SBFloatingDockSuggestionsViewProviding listView];
-[SBFloatingDockSuggestionsViewProviding setFloatingDockViewController:];
-[SBFloatingDockSuggestionsViewProviding dockViewDidResignVisible];
-[SBFloatingDockSuggestionsViewProviding dockFolderDidEndTransitioning];
-[SBFloatingDockSuggestionsViewProviding dockFolderWillBeginTransitioning];
-[SBFloatingDockSuggestionsViewProviding dockViewDidBecomeVisible];
-[SBFloatingDockSuggestionsViewProviding dockViewWillBecomeVisible];
-[SBFloatingDockSuggestionsViewProviding dockViewWillResignVisible];
```

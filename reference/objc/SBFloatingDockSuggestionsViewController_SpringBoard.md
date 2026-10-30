# `SBFloatingDockSuggestionsViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBFloatingDockSuggestionsModelDelegate`, `SBLayoutStateTransitionObserver`, `SBIconViewProviding`, `SBFloatingDockSuggestionsViewProviding`, `SBIconViewQuerying`
- 13 instance variables, 19 properties, 65 instance methods, 0 class methods

## Instance variables

```
B _visible;
@"SBFloatingDockViewController" _floatingDockViewController;
@"<SBFloatingDockSuggestionsViewControllerDelegate>" _delegate;
Q _numberOfRecents;
@"<SBFloatingDockHomeScreenContextProviding>" _homeScreenContextProvider;
@"SBApplicationController" _applicationController;
@"SBAppSuggestionManager" _appSuggestionManager;
@"SBIconListModel" _suggestionsIconListModel;
@"SBFloatingDockSuggestionsModel" _suggestionsModel;
@"NSMutableArray" _deferredIconUpdates;
@"SBLayoutStateTransitionCoordinator" _layoutStateTransitionCoordinator;
q _effectiveEnvironmentMode;
@"<SBIconViewProviding>" _iconViewProvider;
```

## Properties

```
@property (T@"<SBFloatingDockHomeScreenContextProviding>",R,W,N,V_homeScreenContextProvider) homeScreenContextProvider;
@property (T@"SBApplicationController",R,N,V_applicationController) applicationController;
@property (T@"SBAppSuggestionManager",R,N,V_appSuggestionManager) appSuggestionManager;
@property (T@"SBIconListModel",R,N,V_suggestionsIconListModel) suggestionsIconListModel;
@property (T@"SBFloatingDockSuggestionsModel",R,W,N,V_suggestionsModel) suggestionsModel;
@property (T@"NSMutableArray",&,N,V_deferredIconUpdates) deferredIconUpdates;
@property (T@"SBLayoutStateTransitionCoordinator",W,N,V_layoutStateTransitionCoordinator) layoutStateTransitionCoordinator;
@property (Tq,N,V_effectiveEnvironmentMode) effectiveEnvironmentMode;
@property (TB,N,GisVisible,V_visible) visible;
@property (T@"<SBIconViewProviding>",R,W,N,V_iconViewProvider) iconViewProvider;
@property (T@"SBDockIconListView",&,N) listView;
@property (T@"<SBFloatingDockSuggestionsViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R,N,V_numberOfRecents) numberOfRecents;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBFloatingDockViewController",W,N,V_floatingDockViewController) floatingDockViewController;
@property (T@"NSSet",R,C,N) presentedIconLocations;
```

## Instance methods

```
-[SBFloatingDockSuggestionsViewController dequeueReusableIconViewOfClass:];
-[SBFloatingDockSuggestionsViewController layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBFloatingDockSuggestionsViewController configureIconView:forIcon:];
-[SBFloatingDockSuggestionsViewController _iconModelDidChange:];
-[SBFloatingDockSuggestionsViewController floatingDockViewController];
-[SBFloatingDockSuggestionsViewController isIconViewRecycled:];
-[SBFloatingDockSuggestionsViewController firstIconViewForIcon:inLocations:];
-[SBFloatingDockSuggestionsViewController applicationController];
-[SBFloatingDockSuggestionsViewController recycleIconView:];
-[SBFloatingDockSuggestionsViewController enumerateDisplayedIconViewsForIcon:usingBlock:];
-[SBFloatingDockSuggestionsViewController setVisible:];
-[SBFloatingDockSuggestionsViewController _iconForDisplayItem:];
-[SBFloatingDockSuggestionsViewController firstIconViewForIcon:];
-[SBFloatingDockSuggestionsViewController dealloc];
-[SBFloatingDockSuggestionsViewController enumerateDisplayedIconViewsUsingBlock:];
-[SBFloatingDockSuggestionsViewController setListView:];
-[SBFloatingDockSuggestionsViewController isDisplayingIcon:inLocation:];
-[SBFloatingDockSuggestionsViewController isVisible];
-[SBFloatingDockSuggestionsViewController layoutStateTransitionCoordinator];
-[SBFloatingDockSuggestionsViewController isDisplayingIcon:inLocations:];
-[SBFloatingDockSuggestionsViewController numberOfRecents];
-[SBFloatingDockSuggestionsViewController setDelegate:];
-[SBFloatingDockSuggestionsViewController layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBFloatingDockSuggestionsViewController listView];
-[SBFloatingDockSuggestionsViewController loadView];
-[SBFloatingDockSuggestionsViewController delegate];
-[SBFloatingDockSuggestionsViewController isPresentingIconLocation:];
-[SBFloatingDockSuggestionsViewController setLayoutStateTransitionCoordinator:];
-[SBFloatingDockSuggestionsViewController iconViewProvider];
-[SBFloatingDockSuggestionsViewController isDisplayingIconView:inLocation:];
-[SBFloatingDockSuggestionsViewController iconViewForIcon:location:];
-[SBFloatingDockSuggestionsViewController isDisplayingIcon:];
-[SBFloatingDockSuggestionsViewController firstIconViewForIcon:excludingLocations:];
-[SBFloatingDockSuggestionsViewController isDisplayingIconView:];
-[SBFloatingDockSuggestionsViewController setFloatingDockViewController:];
-[SBFloatingDockSuggestionsViewController presentedIconLocations];
-[SBFloatingDockSuggestionsViewController dockViewDidResignVisible];
-[SBFloatingDockSuggestionsViewController dockFolderDidEndTransitioning];
-[SBFloatingDockSuggestionsViewController dockFolderWillBeginTransitioning];
-[SBFloatingDockSuggestionsViewController dockViewDidBecomeVisible];
-[SBFloatingDockSuggestionsViewController dockViewWillBecomeVisible];
-[SBFloatingDockSuggestionsViewController dockViewWillResignVisible];
-[SBFloatingDockSuggestionsViewController _didChangeNumberOfIcons];
-[SBFloatingDockSuggestionsViewController _emitPresentedEventInvolvingContinuity:fromModel:atIndex:];
-[SBFloatingDockSuggestionsViewController _fadeInIcon:isReplacing:completion:];
-[SBFloatingDockSuggestionsViewController _fadeOutIcon:atIndex:isReplacing:completion:];
-[SBFloatingDockSuggestionsViewController _listLayoutDidChange:];
-[SBFloatingDockSuggestionsViewController _loadAndPlaceIconsInViewForDisplayItems:];
-[SBFloatingDockSuggestionsViewController _onHomescreen];
-[SBFloatingDockSuggestionsViewController _performDeferredIconUpdates];
-[SBFloatingDockSuggestionsViewController _performOrDefer:iconUpdate:];
-[SBFloatingDockSuggestionsViewController _shouldDeferUpdateInvolvingContinuity:];
-[SBFloatingDockSuggestionsViewController appSuggestionManager];
-[SBFloatingDockSuggestionsViewController deferredIconUpdates];
-[SBFloatingDockSuggestionsViewController dockSuggestionsModel:didInsertItem:atIndex:involvesContinuity:];
-[SBFloatingDockSuggestionsViewController dockSuggestionsModel:didReloadItems:withItems:];
-[SBFloatingDockSuggestionsViewController dockSuggestionsModel:didRemoveItem:atIndex:involvesContinuity:];
-[SBFloatingDockSuggestionsViewController dockSuggestionsModel:didReplaceItem:atIndex:withItem:atIndex:involvesContinuity:];
-[SBFloatingDockSuggestionsViewController effectiveEnvironmentMode];
-[SBFloatingDockSuggestionsViewController homeScreenContextProvider];
-[SBFloatingDockSuggestionsViewController initWithNumberOfRecents:homeScreenContextProvider:applicationController:layoutStateTransitionCoordinator:suggestionsModel:iconViewProvider:];
-[SBFloatingDockSuggestionsViewController setDeferredIconUpdates:];
-[SBFloatingDockSuggestionsViewController setEffectiveEnvironmentMode:];
-[SBFloatingDockSuggestionsViewController suggestionsIconListModel];
-[SBFloatingDockSuggestionsViewController suggestionsModel];
```

# `UIFindInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction`
- 13 instance variables, 16 properties, 41 instance methods, 2 class methods

## Instance variables

```
@"UIView" _view;
@"UIView" _alternateHostView;
@"UINavigationController" _hostNavigationViewController;
@"UIFindSession" _activeFindSession;
Q _lastUsedHostingStrategy;
{?="respondToPlacementChangeNotifications"b1"provideHostScrollView"b1} _privateDelegateDoes;
{?="aWebView"b1"aMailComposeView"b1} _hostViewIs;
{?="hostViewControllerHadToolbarHidden"b1} _findInteractionFlags;
@"NSString" _searchText;
@"NSString" _replacementText;
@? _optionsMenuProvider;
@"<UIFindInteractionDelegate>" _delegate;
@"_UIFindNavigatorHarness" _findNavigatorHarness;
```

## Properties

```
@property (T@"_UIFindNavigatorHarness",&,N,V_findNavigatorHarness) findNavigatorHarness;
@property (T@"UIView",W,N,G_hostView,S_setHostView:) _hostView;
@property (T@"UITextSearchOptions",R,N) _configuredSearchOptions;
@property (T@"UIView",W,N,G_hostView,S_setHostView:) _hostView;
@property (T@"UITextSearchOptions",R,N) _configuredSearchOptions;
@property (TB,R,N,GisFindNavigatorVisible) findNavigatorVisible;
@property (T@"UIFindSession",R,N,V_activeFindSession) activeFindSession;
@property (T@"NSString",C,N,V_searchText) searchText;
@property (T@"NSString",C,N,V_replacementText) replacementText;
@property (T@?,C,N,V_optionsMenuProvider) optionsMenuProvider;
@property (T@"<UIFindInteractionDelegate>",R,W,N,V_delegate) delegate;
@property (T@"UIView",R,W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIFindInteraction _globalFindBuffer];
+[UIFindInteraction _setGlobalFindBuffer:];
```

## Instance methods

```
-[UIFindInteraction searchableObject];
-[UIFindInteraction _updateHostViewConformance];
-[UIFindInteraction _keyboardDidChangePlacementNotification:];
-[UIFindInteraction _presentFindNavigatorShowingReplace:];
-[UIFindInteraction _didBeginActiveFindSession];
-[UIFindInteraction findNext];
-[UIFindInteraction _configuredSearchOptions];
-[UIFindInteraction presentFindNavigatorShowingReplace:];
-[UIFindInteraction _findNavigatorHosting];
-[UIFindInteraction _currentHostingStrategy];
-[UIFindInteraction setFindNavigatorHarness:];
-[UIFindInteraction setOptionsMenuProvider:];
-[UIFindInteraction searchText];
-[UIFindInteraction activeFindSession];
-[UIFindInteraction _findNavigatorHostingForStrategy:];
-[UIFindInteraction _setHostView:];
-[UIFindInteraction _systemInputAssistantCenterVisibilityChanged:];
-[UIFindInteraction view];
-[UIFindInteraction findNavigatorHarness];
-[UIFindInteraction willMoveToView:];
-[UIFindInteraction _findNavigatorSceneComponent];
-[UIFindInteraction setSearchText:];
-[UIFindInteraction setSearchableObject:];
-[UIFindInteraction delegate];
-[UIFindInteraction _currentFindNavigatorController];
-[UIFindInteraction replacementText];
-[UIFindInteraction initWithSessionDelegate:];
-[UIFindInteraction setReplacementText:];
-[UIFindInteraction _computedHostingStrategy];
-[UIFindInteraction _didEndActiveFindSession];
-[UIFindInteraction _willChangeNavigatorPlacement:];
-[UIFindInteraction _createActiveFindSessionIfNecessary];
-[UIFindInteraction _recomputeHostingStrategyIfNecessary];
-[UIFindInteraction dismissFindNavigator];
-[UIFindInteraction isFindNavigatorVisible];
-[UIFindInteraction _hostScrollView];
-[UIFindInteraction updateResultCount];
-[UIFindInteraction _hostView];
-[UIFindInteraction didMoveToView:];
-[UIFindInteraction findPrevious];
-[UIFindInteraction optionsMenuProvider];
```

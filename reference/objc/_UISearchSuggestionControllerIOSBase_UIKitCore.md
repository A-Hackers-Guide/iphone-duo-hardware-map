# `_UISearchSuggestionControllerIOSBase`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISearchSuggestionController`
- 3 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _hasSetUpGeometryChangeResponse;
@"UISearchTextField" _searchTextField;
@"UISearchBar" _searchBar;
```

## Properties

```
@property (TB,N,V_hasSetUpGeometryChangeResponse) hasSetUpGeometryChangeResponse;
@property (T@"UISearchTextField",R,W,N,V_searchTextField) searchTextField;
@property (T@"UISearchBar",R,W,N,V_searchBar) searchBar;
@property (TB,R,N) hasVisibleMenu;
@property (TB,R,N) shouldUseMenuIOS;
```

## Instance methods

```
-[_UISearchSuggestionControllerIOSBase suggestions];
-[_UISearchSuggestionControllerIOSBase setSuggestions:];
-[_UISearchSuggestionControllerIOSBase searchBar];
-[_UISearchSuggestionControllerIOSBase _hasVisibleMenu];
-[_UISearchSuggestionControllerIOSBase hasVisibleMenu];
-[_UISearchSuggestionControllerIOSBase shouldUseMenuIOS];
-[_UISearchSuggestionControllerIOSBase _dismissMenuAnimated:];
-[_UISearchSuggestionControllerIOSBase _geometryChanged:forAncestor:];
-[_UISearchSuggestionControllerIOSBase searchTextField];
-[_UISearchSuggestionControllerIOSBase initWithSearchTextField:];
-[_UISearchSuggestionControllerIOSBase _updateMenuWithSuggestionGroups:];
-[_UISearchSuggestionControllerIOSBase hasSetUpGeometryChangeResponse];
-[_UISearchSuggestionControllerIOSBase menuDidCloseWithAnimator:];
-[_UISearchSuggestionControllerIOSBase searchTextFieldDidGainSearchBar:];
-[_UISearchSuggestionControllerIOSBase searchTextFieldWillMoveToWindow:];
-[_UISearchSuggestionControllerIOSBase setHasSetUpGeometryChangeResponse:];
-[_UISearchSuggestionControllerIOSBase updateSuggestions:userInitiated:];
```

# `_UISearchSuggestionControllerIOS`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISearchSuggestionControllerIOSBase`
- Protocols: `UIContextMenuInteractionDelegate`, `UIGestureRecognizerDelegate`
- 2 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"UIContextMenuInteraction" _menuInteraction;
@"UITapGestureRecognizer" _suggestionsRecoveryGesture;
```

## Properties

```
@property (T@"UIContextMenuInteraction",&,N,V_menuInteraction) menuInteraction;
@property (T@"UITapGestureRecognizer",&,N,V_suggestionsRecoveryGesture) suggestionsRecoveryGesture;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UISearchSuggestionControllerIOS setMenuInteraction:];
-[_UISearchSuggestionControllerIOS contextMenuInteraction:willEndForConfiguration:animator:];
-[_UISearchSuggestionControllerIOS suggestionsRecoveryGesture];
-[_UISearchSuggestionControllerIOS _hasVisibleMenu];
-[_UISearchSuggestionControllerIOS contextMenuInteraction:configurationForMenuAtLocation:];
-[_UISearchSuggestionControllerIOS _suggestionsRecoveryGestureRecognized];
-[_UISearchSuggestionControllerIOS shouldUseMenuIOS];
-[_UISearchSuggestionControllerIOS menuInteraction];
-[_UISearchSuggestionControllerIOS _dismissMenuAnimated:];
-[_UISearchSuggestionControllerIOS gestureRecognizerShouldBegin:];
-[_UISearchSuggestionControllerIOS _suggestionsMenu];
-[_UISearchSuggestionControllerIOS initWithSearchTextField:];
-[_UISearchSuggestionControllerIOS setSuggestionsRecoveryGesture:];
-[_UISearchSuggestionControllerIOS _updateMenuWithSuggestionGroups:];
-[_UISearchSuggestionControllerIOS _contextMenuInteraction:styleForMenuWithConfiguration:];
-[_UISearchSuggestionControllerIOS updateSuggestionGroups:userInitiated:];
```

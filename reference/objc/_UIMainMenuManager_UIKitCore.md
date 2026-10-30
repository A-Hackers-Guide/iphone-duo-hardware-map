# `_UIMainMenuManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIDeferredMenuElementDelegate`
- 7 instance variables, 6 properties, 37 instance methods, 2 class methods

## Instance variables

```
@"_UIMainMenu" _cachedBaseMainMenu;
@"_UIMainMenuElementBookkeeping" _baseMenuBookkeeping;
@"NSHashTable" _observers;
@"NSMutableDictionary" _sessions;
B _isObservingMainMenuRebuilds;
@? _responderKeyboardShortcutsProvider;
@? _mainMenuProvider;
```

## Properties

```
@property (T@?,C,N,V_responderKeyboardShortcutsProvider) responderKeyboardShortcutsProvider;
@property (T@?,C,N,V_mainMenuProvider) mainMenuProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIMainMenuManager sharedManager];
+[_UIMainMenuManager existingManager];
```

## Instance methods

```
-[_UIMainMenuManager init];
-[_UIMainMenuManager deferredMenuElementWasFulfilled:];
-[_UIMainMenuManager _beginObservingMainMenuRebuildsIfNeeded];
-[_UIMainMenuManager _beginSession];
-[_UIMainMenuManager _categoryMenuIdentifierForCommand:commandState:session:];
-[_UIMainMenuManager _categoryMenuIdentifierForInvokedKeyboardShortcutMenuLeaf:session:];
-[_UIMainMenuManager _currentResponderKeyboardShortcutLeavesForSession:];
-[_UIMainMenuManager _endSessionWithIdentifier:];
-[_UIMainMenuManager _firstResponderForSession:];
-[_UIMainMenuManager _fulfillDeferredElementIfNecessary:forSession:fulfillmentHandler:];
-[_UIMainMenuManager _isCachedDeferredElementExpansionOfMainMenu:forSession:];
-[_UIMainMenuManager _isElement:directlyVisibleInTopLevelCategoryMenuForSession:];
-[_UIMainMenuManager _mainMenuFromUIMenu:fromDeferredElement:];
-[_UIMainMenuManager _mainMenuSystemDidSetNeedsRebuild:];
-[_UIMainMenuManager _menuElementFromUIMenuElement:fromDeferredElement:];
-[_UIMainMenuManager _menuElementsFromUIMenuElements:fromDeferredElement:];
-[_UIMainMenuManager _parentGroupStateForElementIdentifier:session:];
-[_UIMainMenuManager _populateState:forElements:session:];
-[_UIMainMenuManager _stateForCommand:session:];
-[_UIMainMenuManager _stateForMenu:session:];
-[_UIMainMenuManager _updateBookkeeping:forElement:];
-[_UIMainMenuManager _updateCachedBaseMainMenuIfNeeded];
-[_UIMainMenuManager _validatorForSession:];
-[_UIMainMenuManager _visibleCommandKeyboardShortcutsForSession:];
-[_UIMainMenuManager addMainMenuObserver:];
-[_UIMainMenuManager isActiveObserver:];
-[_UIMainMenuManager mainMenuProvider];
-[_UIMainMenuManager performBaseMenuRequest:];
-[_UIMainMenuManager performDeferredElementRequest:responseHandler:];
-[_UIMainMenuManager performMainMenuCommandInvocationRequest:responseHandler:];
-[_UIMainMenuManager performMainMenuStateRequest:];
-[_UIMainMenuManager performSessionRequest:];
-[_UIMainMenuManager removeMainMenuObserver:];
-[_UIMainMenuManager responderKeyboardShortcutsProvider];
-[_UIMainMenuManager setMainMenuProvider:];
-[_UIMainMenuManager setResponderKeyboardShortcutsProvider:];
-[_UIMainMenuManager userDidInvokeKeyboardShortcut:];
```

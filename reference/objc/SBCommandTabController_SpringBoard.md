# `SBCommandTabController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBCommandTabViewControllerDelegate`, `SBRecentDisplayItemsControllerDelegate`, `SBRecentDisplayItemsPersistenceDelegate`
- 16 instance variables, 6 properties, 28 instance methods, 1 class methods

## Instance variables

```
@"SBCommandTabViewController" _commandTabViewController;
@"NSTimer" _timer;
@"UIApplicationSceneDeactivationAssertion" _resignActiveAssertion;
@"<BSInvalidatable>" _keyboardFocusAssertion;
@"SBRecentDisplayItemsController" _recentDisplayItemsController;
@"NSOrderedSet" _persistedRecentDisplayItems;
@"NSMutableSet" _appsAllowedWhileHidden;
@"NSObject<OS_dispatch_queue>" _recentDisplayItemsPersistenceQueue;
@"SBRecentDisplayItemsDataStore" _dataStore;
@"SBRecentDisplayItemsDefaults" _defaults;
@"<BSInvalidatable>" _deferOrientationUpdatesAssertion;
@"PTToggleTestRecipe" _testRecipe;
@"SBWindow" _window;
@"SBWindowScene" _windowScene;
@"SBIconController" _iconController;
@"SBApplicationController" _applicationController;
```

## Properties

```
@property (T@"SBWindow",R,N,V_window) window;
@property (TB,R,N,GisVisible) visible;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBCommandTabController keyCommands];
```

## Instance methods

```
-[SBCommandTabController next];
-[SBCommandTabController previous];
-[SBCommandTabController dismiss];
-[SBCommandTabController dealloc];
-[SBCommandTabController isVisible];
-[SBCommandTabController window];
-[SBCommandTabController _sceneDidDisconnect:];
-[SBCommandTabController _clearTimer];
-[SBCommandTabController _effectiveSettingsChangedNotification:];
-[SBCommandTabController _activateWithForwardDirection:];
-[SBCommandTabController _allowAppToAppearWhileHidden:];
-[SBCommandTabController _disallowAppFromAppearingWhileHidden:];
-[SBCommandTabController _emitAnalyticsEventForDisplayItem:];
-[SBCommandTabController _showCommandTabBarAfterTimer:];
-[SBCommandTabController _showWindow:];
-[SBCommandTabController activateWithKeyCommand:];
-[SBCommandTabController dataStore:persistDisplayItems:];
-[SBCommandTabController dataStore:shouldRestorePersistedDisplayItem:];
-[SBCommandTabController initWithSceneManager:windowScene:iconController:applicationController:];
-[SBCommandTabController launchCurrentSelectedApplication];
-[SBCommandTabController persistedDisplayItemsForDataStore:];
-[SBCommandTabController recentDisplayItemsController:didRemoveItem:];
-[SBCommandTabController recentDisplayItemsController:shouldAddItem:];
-[SBCommandTabController recentDisplayItemsControllerDidUpdateDisplayItems:];
-[SBCommandTabController removeCurrentSelectedApplication];
-[SBCommandTabController selectedDisplayItem];
-[SBCommandTabController viewController:selectedApplicationWithDisplayItem:];
-[SBCommandTabController viewControllerWantsDismissal:];
```

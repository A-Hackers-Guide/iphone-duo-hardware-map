# `_UISceneUserActivityManager`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIActivityContinuationManagerApplicationContext`, `_UISceneComponentProviding`
- 8 instance variables, 7 properties, 21 instance methods, 15 class methods

## Instance variables

```
@"UIScene" _weakScene;
@"NSUserActivity" _restorationActivity;
@"NSDictionary" _connectionOptionsRestorationActivityDictionary;
@"UIActivityContinuationManager" _activityContinuationManager;
@"NSSet" _activityTypesForDefaultProgressUI;
B _initialRestorationIsFinished;
B _sceneStateTransitionIsRestorationExtendable;
B _isDisplayingActivityContinuationUI;
```

## Properties

```
@property (T@"UIActivityContinuationManager",R,N,G_activityContinuationManager) _activityContinuationManager;
@property (TB,N,G_isDisplayingActivityContinuationUI,S_setIsDisplayingActivityContinuationUI:,V_isDisplayingActivityContinuationUI) isDisplayingActivityContinuationUI;
@property (T@"UIScene",W,N,G_scene,S_setScene:) _scene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UISceneUserActivityManager _userActivityManagerForScene:];
+[_UISceneUserActivityManager _restorationUserActivityAvailableForSceneIdentifier:];
+[_UISceneUserActivityManager _getUserInfoForPersistentIdentifier:error:];
+[_UISceneUserActivityManager _activityContinuationDictionaryWithAction:sourceApplication:originatingProcess:];
+[_UISceneUserActivityManager _updatePersistedSceneSession:];
+[_UISceneUserActivityManager _saveRestorationStateForScene:];
+[_UISceneUserActivityManager _scheduleDataSaveForSceneSession:saveRestorationActivity:];
+[_UISceneUserActivityManager _showProgressForScene:whenFetchingUserActivityForTypes:];
+[_UISceneUserActivityManager _initializeUserActivityManager];
+[_UISceneUserActivityManager _getRestorationUserActivityForPersistentIdentifier:error:];
+[_UISceneUserActivityManager _deleteSceneSessionsWithPersistentIdentifiers:];
+[_UISceneUserActivityManager _getInternalUserInfoForPersistentIdentifier:error:];
+[_UISceneUserActivityManager _deleteSavedSceneSessionDirectoryWithPersistentIdentifier:];
+[_UISceneUserActivityManager _fetchSceneSessionWithPersistentIdentifier:];
+[_UISceneUserActivityManager _knownSceneSessionMap];
```

## Instance methods

```
-[_UISceneUserActivityManager _scene:willTransitionToActivationState:withReasonsMask:];
-[_UISceneUserActivityManager _scene];
-[_UISceneUserActivityManager _scene:didTransitionFromActivationState:withReasonsMask:];
-[_UISceneUserActivityManager _sceneWillInvalidate:];
-[_UISceneUserActivityManager activityContinuationManager:continueUserActivity:];
-[_UISceneUserActivityManager _isDisplayingActivityContinuationUI];
-[_UISceneUserActivityManager initWithScene:];
-[_UISceneUserActivityManager activityContinuationManager:hideProgressUIWithCompletion:];
-[_UISceneUserActivityManager _saveOrClearRestorationDictionary:forScene:];
-[_UISceneUserActivityManager activityContinuationManager:didFailToContinueUserActivityWithType:error:];
-[_UISceneUserActivityManager activityContinuationManager:displayProgressUI:dismissalHandler:];
-[_UISceneUserActivityManager activityContinuationManagerHandleErrorsByConfiguringProgressUI:];
-[_UISceneUserActivityManager _checkActivityContinuationAndBecomeCurrentIfNeeded];
-[_UISceneUserActivityManager activityContinuationManager:configureProgressUIWithError:];
-[_UISceneUserActivityManager _saveSceneRestorationState];
-[_UISceneUserActivityManager _setScene:];
-[_UISceneUserActivityManager activityContinuationManager:willContinueUserActivityWithType:];
-[_UISceneUserActivityManager activityContinuationManager:didUpdateUserActivity:];
-[_UISceneUserActivityManager _activityContinuationManager];
-[_UISceneUserActivityManager activityContinuationManagerUserCancelledError:];
-[_UISceneUserActivityManager _setIsDisplayingActivityContinuationUI:];
```

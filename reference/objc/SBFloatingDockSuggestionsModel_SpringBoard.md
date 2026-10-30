# `SBFloatingDockSuggestionsModel`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBRecentDisplayItemsPersistenceDelegate`, `SBRecentDisplayItemsControllerDelegate`, `SBIconListModelObserver`, `APSubjectMonitor`
- 24 instance variables, 24 properties, 67 instance methods, 0 class methods

## Instance variables

```
@"<BSInvalidatable>" _recentDisplayItemsStateCaptureHandle;
@"<BSInvalidatable>" _appSuggestionStateCaptureHandle;
@"<BSInvalidatable>" _displayItemsStateCaptureHandle;
@"<BSDefaultObserver>" _recentsEnabledDefaultsObserver;
B _recentsEnabled;
@"NSOrderedSet" _currentDisplayItems;
@"SBBestAppSuggestion" _currentAppSuggestion;
@"SBApplication" _requestedSuggestedApplication;
@"<SBFloatingDockSuggestionsModelDelegate>" _delegate;
Q _maxSuggestions;
@"SBAppSuggestionManager" _appSuggestionManager;
@"SBRecentDisplayItemsController" _recentsController;
@"SBRecentDisplayItemsDataStore" _recentsDataStore;
@"SBRecentDisplayItemsDefaults" _recentsDefaults;
@"SBIconListModel" _userDockListModel;
@"<SBFloatingDockHomeScreenContextProviding>" _homeScreenContextProvider;
@"SBApplicationController" _applicationController;
@"SBIconModel" _iconModel;
@"SBFloatingDockDefaults" _floatingDockDefaults;
@"NSMutableSet" _pendingSuggestionUpdateReasons;
@"NSMutableOrderedSet" _currentRecentDisplayItems;
@"NSMutableOrderedSet" _currentRecentDisplayItemsSortedByRecency;
@"PTSingleTestRecipe" _stressTestRecipe;
@"<APSubjectMonitorSubscription>" _appProtectionSubscription;
```

## Properties

```
@property (TQ,R,N,V_maxSuggestions) maxSuggestions;
@property (T@"SBAppSuggestionManager",R,N,V_appSuggestionManager) appSuggestionManager;
@property (T@"SBRecentDisplayItemsController",R,W,N,V_recentsController) recentsController;
@property (T@"SBRecentDisplayItemsDataStore",R,W,N,V_recentsDataStore) recentsDataStore;
@property (T@"SBRecentDisplayItemsDefaults",R,N,V_recentsDefaults) recentsDefaults;
@property (T@"SBIconListModel",&,N,V_userDockListModel) userDockListModel;
@property (T@"<SBFloatingDockHomeScreenContextProviding>",R,W,N,V_homeScreenContextProvider) homeScreenContextProvider;
@property (T@"SBApplicationController",R,N,V_applicationController) applicationController;
@property (T@"SBIconModel",&,N,V_iconModel) iconModel;
@property (T@"SBFloatingDockDefaults",R,N,V_floatingDockDefaults) floatingDockDefaults;
@property (TB,N,V_recentsEnabled) recentsEnabled;
@property (T@"NSMutableSet",R,N,V_pendingSuggestionUpdateReasons) pendingSuggestionUpdateReasons;
@property (T@"NSMutableOrderedSet",R,N,V_currentRecentDisplayItems) currentRecentDisplayItems;
@property (T@"NSMutableOrderedSet",R,N,V_currentRecentDisplayItemsSortedByRecency) currentRecentDisplayItemsSortedByRecency;
@property (T@"NSOrderedSet",C,N,V_currentDisplayItems) currentDisplayItems;
@property (T@"PTSingleTestRecipe",R,N,V_stressTestRecipe) stressTestRecipe;
@property (T@"<APSubjectMonitorSubscription>",R,N,V_appProtectionSubscription) appProtectionSubscription;
@property (T@"SBBestAppSuggestion",R,N,V_currentAppSuggestion) currentAppSuggestion;
@property (T@"SBApplication",&,N,V_requestedSuggestedApplication) requestedSuggestedApplication;
@property (T@"<SBFloatingDockSuggestionsModelDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFloatingDockSuggestionsModel setIconModel:];
-[SBFloatingDockSuggestionsModel _addStateCaptureHandlers];
-[SBFloatingDockSuggestionsModel iconList:didReplaceIcon:withIcon:];
-[SBFloatingDockSuggestionsModel _iconModelDidChange:];
-[SBFloatingDockSuggestionsModel _iconModelDidLayout:];
-[SBFloatingDockSuggestionsModel applicationController];
-[SBFloatingDockSuggestionsModel recentsController];
-[SBFloatingDockSuggestionsModel appProtectionSubjectsChanged:forSubscription:];
-[SBFloatingDockSuggestionsModel dealloc];
-[SBFloatingDockSuggestionsModel setDelegate:];
-[SBFloatingDockSuggestionsModel floatingDockDefaults];
-[SBFloatingDockSuggestionsModel _initializeAndObserveDefaults];
-[SBFloatingDockSuggestionsModel delegate];
-[SBFloatingDockSuggestionsModel iconList:didAddIcon:];
-[SBFloatingDockSuggestionsModel iconModel];
-[SBFloatingDockSuggestionsModel dockViewDidResignVisible];
-[SBFloatingDockSuggestionsModel maxSuggestions];
-[SBFloatingDockSuggestionsModel dockViewDidBecomeVisible];
-[SBFloatingDockSuggestionsModel recentsEnabled];
-[SBFloatingDockSuggestionsModel setRecentsEnabled:];
-[SBFloatingDockSuggestionsModel _updateCurrentDisplayItemsAfterContinuityChange:notifyDelegate:];
-[SBFloatingDockSuggestionsModel recentsDefaults];
-[SBFloatingDockSuggestionsModel _appSuggestionsChanged:];
-[SBFloatingDockSuggestionsModel _areRecentsSupported];
-[SBFloatingDockSuggestionsModel _displayItemContainedInUserDock:];
-[SBFloatingDockSuggestionsModel _displayItemForAppSuggestion:];
-[SBFloatingDockSuggestionsModel _dockListModelFromContextProvider];
-[SBFloatingDockSuggestionsModel _filterRecentDisplayItems:filteredOutItems:];
-[SBFloatingDockSuggestionsModel _handleNewRecentItem:];
-[SBFloatingDockSuggestionsModel _indexForAppSuggestion:];
-[SBFloatingDockSuggestionsModel _isPendingAppSuggestionsUpdate];
-[SBFloatingDockSuggestionsModel _moveOrAddRecentThenCull:];
-[SBFloatingDockSuggestionsModel _oldestRecent];
-[SBFloatingDockSuggestionsModel _performAppSuggestionChangedWithNewSuggestion:];
-[SBFloatingDockSuggestionsModel _reloadRecentsAndSuggestions];
-[SBFloatingDockSuggestionsModel _runStressTestWithCompletion:];
-[SBFloatingDockSuggestionsModel _setRecentsEnabled:];
-[SBFloatingDockSuggestionsModel _shouldProcessAppSuggestion:];
-[SBFloatingDockSuggestionsModel appProtectionSubscription];
-[SBFloatingDockSuggestionsModel appSuggestionManager];
-[SBFloatingDockSuggestionsModel beginPendingUpdatesForReason:];
-[SBFloatingDockSuggestionsModel currentAppSuggestion];
-[SBFloatingDockSuggestionsModel currentDisplayItems];
-[SBFloatingDockSuggestionsModel currentRecentDisplayItems];
-[SBFloatingDockSuggestionsModel currentRecentDisplayItemsSortedByRecency];
-[SBFloatingDockSuggestionsModel dataStore:persistDisplayItems:];
-[SBFloatingDockSuggestionsModel dataStore:shouldRestorePersistedDisplayItem:];
-[SBFloatingDockSuggestionsModel endPendingUpdatesForReason:];
-[SBFloatingDockSuggestionsModel homeScreenContextProvider];
-[SBFloatingDockSuggestionsModel initWithMaximumNumberOfSuggestions:homeScreenContextProvider:recentsController:recentsDataStore:recentsDefaults:floatingDockDefaults:appSuggestionManager:applicationController:];
-[SBFloatingDockSuggestionsModel pendingSuggestionUpdateReasons];
-[SBFloatingDockSuggestionsModel persistedDisplayItemsForDataStore:];
-[SBFloatingDockSuggestionsModel recentDisplayItemsController:didAddItem:];
-[SBFloatingDockSuggestionsModel recentDisplayItemsController:didAddItem:andDropItem:];
-[SBFloatingDockSuggestionsModel recentDisplayItemsController:didMoveItemToFront:];
-[SBFloatingDockSuggestionsModel recentDisplayItemsController:didRemoveItem:];
-[SBFloatingDockSuggestionsModel recentDisplayItemsController:shouldAddItem:];
-[SBFloatingDockSuggestionsModel recentDisplayItemsControllerShouldRepresentAppClipsAsWebClips:];
-[SBFloatingDockSuggestionsModel recentsDataStore];
-[SBFloatingDockSuggestionsModel requestedSuggestedApplication];
-[SBFloatingDockSuggestionsModel resetRecentsAndSuggestions];
-[SBFloatingDockSuggestionsModel setCurrentDisplayItems:];
-[SBFloatingDockSuggestionsModel setRequestedSuggestedApplication:];
-[SBFloatingDockSuggestionsModel setUserDockListModel:];
-[SBFloatingDockSuggestionsModel shouldAddItem:];
-[SBFloatingDockSuggestionsModel stressTestRecipe];
-[SBFloatingDockSuggestionsModel userDockListModel];
```

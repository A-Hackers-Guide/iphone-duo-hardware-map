# `SBIconController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `APSubjectMonitor`, `BBObserverDelegate`, `DNDModeConfigurationServiceListener`, `DNDStateUpdateListener`, `MCProfileConnectionObserver`, `SBApplicationRestrictionObserver`, `SBFolderObserver`, `SBHWidgetMetricsProviderDelegate`, `SBIconStyleObserver`, `SBProactiveHomeScreenSuggestionProviderObserver`, `SBProactiveHomeScreenUsageObserverDelegate`, `SBIconModelProviding`
- 51 instance variables, 35 properties, 142 instance methods, 2 class methods

## Instance variables

```
@"NSSet" _visibleTags;
@"NSSet" _hiddenTags;
@"SBIconModel" _iconModel;
@"BBObserver" _bbObserver;
@"NSMutableSet" _displayIDsWithBadgingEnabled;
@"SBAccountStoreManager" _accountStoreController;
@"SBSyncController" _syncController;
B _allowsUninstall;
B _sendITunesNotification;
B _showingSearch;
@"SBHLibraryCategoryMapProvider" _categoryMapProvider;
@"SBHIconImageCache" _tableUIIconImageCache;
@"SBHIconImageCache" _notificationIconImageCache;
@"SBPowerLogMetricsAggregator" _powerLogAggregator;
@"NSHashTable" _iconControllerObservers;
B _isAppAllowlistActiveAndTransient;
B _inTransientAppAllowlistCooldown;
@"SBIconVisibilityService" _iconVisibilityService;
@"<BSInvalidatable>" _stateCaptureHandlerForKeyDisplayIDsWithBadgingEnabled;
@"<BSInvalidatable>" _stateCaptureHandleForHomeScreenDefaults;
@"<BSInvalidatable>" _stateCaptureHandleForInterestingAppIconLocations;
@"PTSingleTestRecipe" _relayoutTestRecipe;
@"PTSingleTestRecipe" _toggleSearchTestRecipe;
@"PTSingleTestRecipe" _runDownloadingIconTestRecipe;
@"PTSingleTestRecipe" _runRemoveAndRestoreIconTestRecipe;
@"PTSingleTestRecipe" _organizeInFoldersTestRecipe;
@"PTDoubleTestRecipe" _shuffleStackTestRecipe;
@"SBHomeScreenConfigurationManager" _homeScreenConfigurationManager;
^{__CFRunLoopObserver=} _restrictionsUpdateRunLoopObserver;
B _hasRestrictedEnforcedLayout;
B _uninstallingSystemAppsRestricted;
B __ignoreMutatingIconListsOnApplicationInstall;
@"SBApplicationController" _applicationController;
@"SBApplicationPlaceholderController" _applicationPlaceholderController;
@"SBFAnalyticsClient" _analyticsClient;
@"SBHIconRepository" _iconRepository;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"SBWidgetMetricsServer" _widgetMetricsServer;
@"SBHIconManager" _iconManager;
@"SBProactiveHomeScreenUsageObserver" _proactiveUsageObserver;
@"SBProactiveHomeScreenSuggestionProvider" _proactiveSuggestionProvider;
@"<SBIconListLayoutProvider>" _ambientListLayoutProvider;
@"SBHWidgetMetricsProvider" _ambientWidgetMetricsProvider;
@"NSObject<OS_dispatch_queue>" _accountStoreQueue;
@"DNDStateService" _dndStateService;
@"DNDModeConfigurationService" _dndModeConfigurationService;
@"NSArray" _suggestedOnboardingStack;
q _userIconStateFileStatus;
@"<APSubjectMonitorSubscription>" _appProtectionSubjectMonitorSubscription;
@"NSMutableArray" _hiddenAppBundleIdentifiers;
@"SBAnalyticsEventsControllerForIconController" _analyticsEventsController;
```

## Properties

```
@property (T@"SBTodayViewController",R,N) coverSheetTodayViewController;
@property (T@"SBFAnalyticsClient",R,N,V_analyticsClient) analyticsClient;
@property (T@"SBApplicationPlaceholderController",R,N,V_applicationPlaceholderController) applicationPlaceholderController;
@property (T@"SBLockScreenCoordinator",R,N,V_lockScreenCoordinator) lockScreenCoordinator;
@property (TB,N,V_hasRestrictedEnforcedLayout) hasRestrictedEnforcedLayout;
@property (TB,N,GisUninstallingSystemAppsRestricted,V_uninstallingSystemAppsRestricted) uninstallingSystemAppsRestricted;
@property (T@"SBProactiveHomeScreenUsageObserver",&,N,V_proactiveUsageObserver) proactiveUsageObserver;
@property (T@"SBProactiveHomeScreenSuggestionProvider",&,N,V_proactiveSuggestionProvider) proactiveSuggestionProvider;
@property (T@"<SBIconListLayoutProvider>",&,N,V_ambientListLayoutProvider) ambientListLayoutProvider;
@property (T@"SBHWidgetMetricsProvider",&,N,V_ambientWidgetMetricsProvider) ambientWidgetMetricsProvider;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_accountStoreQueue) accountStoreQueue;
@property (T@"SBWidgetMetricsServer",R,N,V_widgetMetricsServer) widgetMetricsServer;
@property (T@"DNDStateService",&,N,V_dndStateService) dndStateService;
@property (T@"DNDModeConfigurationService",&,N,V_dndModeConfigurationService) dndModeConfigurationService;
@property (T@"NSArray",R,N,V_suggestedOnboardingStack) suggestedOnboardingStack;
@property (Tq,N,V_userIconStateFileStatus) userIconStateFileStatus;
@property (T@"<APSubjectMonitorSubscription>",R,W,N,V_appProtectionSubjectMonitorSubscription) appProtectionSubjectMonitorSubscription;
@property (T@"NSMutableArray",&,N,V_hiddenAppBundleIdentifiers) hiddenAppBundleIdentifiers;
@property (T@"SBAnalyticsEventsControllerForIconController",&,N,V_analyticsEventsController) analyticsEventsController;
@property (TB,N,S_setIgnoreMutatingIconListsOnApplicationInstall:,V__ignoreMutatingIconListsOnApplicationInstall) _ignoreMutatingIconListsOnApplicationInstall;
@property (T@"SBApplicationController",R,N,V_applicationController) applicationController;
@property (T@"SBHIconRepository",R,N,V_iconRepository) iconRepository;
@property (T@"SBHIconManager",R,N,V_iconManager) iconManager;
@property (T@"SBHIconImageCache",R,N) tableUIIconImageCache;
@property (T@"SBHIconImageCache",R,N) notificationIconImageCache;
@property (T@"SBRootFolder",R,N) rootFolder;
@property (T@"NSSet",R,C,N) visibleIconStateDisplayIdentifiers;
@property (TB,R,N,GisAppLibrarySupported) appLibrarySupported;
@property (T@"SBIconModel",R,N) iconModel;
@property (TB,R,N) shouldAddNewIconsToRootFolder;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBIconListLayoutProvider>",R,N) listLayoutProvider;
```

## Class methods

```
+[SBIconController sharedInstance];
+[SBIconController sharedInstanceIfExists];
```

## Instance methods

```
-[SBIconController observer:updateSectionInfo:];
-[SBIconController stateService:didReceiveDoNotDisturbStateUpdate:];
-[SBIconController setDndStateService:];
-[SBIconController allowsBadgingForIcon:];
-[SBIconController importIconState:];
-[SBIconController _currentFolderController];
-[SBIconController iconManager];
-[SBIconController _rootFolderDidChange];
-[SBIconController isUninstallSupportedForIcon:];
-[SBIconController coverSheetTodayViewController];
-[SBIconController isAppLibrarySupported];
-[SBIconController allowsUninstall];
-[SBIconController isHideSupportedForIcon:inLocation:];
-[SBIconController _updateAnalyticsFromIconStyleProvider:configuration:];
-[SBIconController _updateEnabledBadgesSetWithSections:];
-[SBIconController isUninstallingSystemAppsRestricted];
-[SBIconController iconPathForIconWithDisplayID:];
-[SBIconController isUninstallOrHideSupportedForIcon:inLocation:];
-[SBIconController setModel:];
-[SBIconController deleteAllWebClips];
-[SBIconController applicationRestrictionController:didUpdateVisibleTags:hiddenTags:];
-[SBIconController isTodayOverlayPresented];
-[SBIconController _iconModelDidLayout:];
-[SBIconController _handleLabelCacheMaintenanceTask:];
-[SBIconController _updateDefaultFirstPageWidgetDescriptors:withSizeClass:andGridCellInfoOptions:];
-[SBIconController analyticsEventsController];
-[SBIconController modeConfigurationService:didReceiveAvailableModesUpdate:];
-[SBIconController applicationController];
-[SBIconController iconRepository];
-[SBIconController setIconStyleProvider:];
-[SBIconController ambientWidgetMetricsProvider];
-[SBIconController _enableWidgetSuggestionsForIconsInModel:withRootFolder:];
-[SBIconController profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:];
-[SBIconController addIconControllerObserver:];
-[SBIconController hiddenAppBundleIdentifiers];
-[SBIconController succinctDescriptionBuilder];
-[SBIconController _obtainSmartStackForWidgetDiscoverabilityWithCompletionHandler:];
-[SBIconController proactiveHomeScreenSuggestionProviderDidUpdatePrediction:];
-[SBIconController dndModeConfigurationService];
-[SBIconController appProtectionSubjectsChanged:forSubscription:];
-[SBIconController _iconModelInstalledAppsDidChange:];
-[SBIconController _ignoreMutatingIconListsOnApplicationInstall];
-[SBIconController resetHomeScreenLayout];
-[SBIconController setAnalyticsEventsController:];
-[SBIconController unforbidApplicationBundleIdentifierFromLibrary:];
-[SBIconController dndStateService];
-[SBIconController _focusModeFromDoNotDisturbState:];
-[SBIconController accountStoreQueue];
-[SBIconController dealloc];
-[SBIconController _badgesAreEnabledForSectionInfo:];
-[SBIconController setHiddenAppBundleIdentifiers:];
-[SBIconController tableUIIconImageCache];
-[SBIconController displayIDsWithBadgingEnabled];
-[SBIconController removeIconControllerObserver:];
-[SBIconController _addSmartStackToTodayList:completionHandler:];
-[SBIconController _createWidgetIconWithKind:extensionBundleIdentifier:gridSize:];
-[SBIconController _featureIntroductionItemForWidgetSetupAtLocation:];
-[SBIconController applicationPlaceholderController];
-[SBIconController _setupWidgetIntroductionIfNecessary];
-[SBIconController descriptionWithMultilinePrefix:];
-[SBIconController _storeAccountDidChange:];
-[SBIconController profileConnectionDidReceiveProfileListChangedNotification:userInfo:];
-[SBIconController setProactiveSuggestionProvider:];
-[SBIconController setAmbientWidgetMetricsProvider:];
-[SBIconController suggestedOnboardingStack];
-[SBIconController _createWidgetIconWithDescriptors:gridSize:];
-[SBIconController _tryToPrepareDynamicDefaultTodayLayout];
-[SBIconController iconStyleProvider:didUpdateIconStyleConfiguration:];
-[SBIconController _prepareDefaultTodayLayoutIfNecessary];
-[SBIconController succinctDescription];
-[SBIconController _bookmarkDidUninstall:];
-[SBIconController _updateUninstallingSystemAppsRestricted];
-[SBIconController proactiveUsageObserver];
-[SBIconController _pushCurrentTagsToIconModel];
-[SBIconController appProtectionSubjectMonitorSubscription];
-[SBIconController initWithApplicationController:applicationPlaceholderController:analyticsClient:iconRepository:lockScreenCoordinator:];
-[SBIconController updateRootFolderWithCurrentDoNotDisturbState];
-[SBIconController isIconVisibleForBundleIdentifier:];
-[SBIconController visibleIconStateDisplayIdentifiers];
-[SBIconController canSaveIconState];
-[SBIconController powerLogAggregator];
-[SBIconController setUninstallingSystemAppsRestricted:];
-[SBIconController rootFolder];
-[SBIconController forbidApplicationBundleIdentifierFromLibrary:];
-[SBIconController ambientListLayoutProvider];
-[SBIconController _mutateIconListsForInstalledAppsDidChangeWithController:added:modified:removed:];
-[SBIconController proactiveSuggestionProvider];
-[SBIconController _setUpRestrictionsUpdateRunLoopObserver];
-[SBIconController resetCategories];
-[SBIconController setUserIconStateFileStatus:];
-[SBIconController setProactiveUsageObserver:];
-[SBIconController description];
-[SBIconController proactiveOnboardingDefaultStacks];
-[SBIconController isEnterpriseMultiUser];
-[SBIconController hasRestrictedEnforcedLayout];
-[SBIconController configureIconManager:];
-[SBIconController prepareForImminentExit];
-[SBIconController isUninstallSupportedForAnyIcon];
-[SBIconController _addStateCaptureHandlerForInterestingAppIconLocations];
-[SBIconController analyticsClient];
-[SBIconController _tearDownRestrictionsUpdateRunloopObserverIfNeeded];
-[SBIconController _addStateCaptureHandlerForKeyDisplayIDsWithBadgingEnabled];
-[SBIconController _updateIconModelStore];
-[SBIconController _updateTransientAppAllowlist];
-[SBIconController notificationIconImageCache];
-[SBIconController _registerAnalytics];
-[SBIconController _installedAppsDidChange:];
-[SBIconController _primaryAppleAccountDidChange:];
-[SBIconController applicationRestrictionControllerDidPostAppVisibilityUpdate:];
-[SBIconController didSaveIconState];
-[SBIconController observer:noteServerConnectionStateChanged:];
-[SBIconController setDndModeConfigurationService:];
-[SBIconController _setIgnoreMutatingIconListsOnApplicationInstall:];
-[SBIconController _applicationIconDataSourceDidChange:];
-[SBIconController applicationRestrictionControllerWillUpdateRestrictions:];
-[SBIconController _isWidgetWithContainerBundleIdentifierValid:];
-[SBIconController _addStateCaptureHandlerForHomeScreenDefaults];
-[SBIconController isUpgradeRestore];
-[SBIconController userIconStateFileStatus];
-[SBIconController widgetMetricsProvider:listLayoutProviderForScreenType:];
-[SBIconController _tryToPrepareNonDynamicDefaultTodayLayout];
-[SBIconController _createWidgetIconWithDataSource:gridSize:];
-[SBIconController widgetMetricsServer];
-[SBIconController listLayoutProvider];
-[SBIconController _allowsBadgingForApplicationBundleIdentifier:];
-[SBIconController _iconModel:wantsToRevealAnyApplicationFromIdentifiers:];
-[SBIconController folderNameForDisplayID:];
-[SBIconController libraryCategoryMapProvider];
-[SBIconController setHasRestrictedEnforcedLayout:];
-[SBIconController _updateFocusModeManagerWithDoNotDisturbState:];
-[SBIconController obtainProactiveSecondPageWidgetSuggestion];
-[SBIconController iconModel];
-[SBIconController shouldAddNewIconsToRootFolder];
-[SBIconController _backupRestoringDidChange:];
-[SBIconController lockScreenCoordinator];
-[SBIconController _foldersInList:];
-[SBIconController _registerLabelCacheMaintenanceTask];
-[SBIconController _connectedHomeScreenFocusModeManagers];
-[SBIconController proactiveHomeScreenUsageObserver:intentForWidget:ofIcon:];
-[SBIconController applicationRestrictionControllerWillPostAppVisibilityUpdate:];
-[SBIconController descriptionBuilderWithMultilinePrefix:];
-[SBIconController setAmbientListLayoutProvider:];
```

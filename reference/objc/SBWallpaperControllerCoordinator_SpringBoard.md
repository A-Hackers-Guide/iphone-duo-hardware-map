# `SBWallpaperControllerCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FCActivityManagerObserving`, `MCProfileConnectionObserver`, `SBDisplayContentModeTransitionObserver`, `SBWallpaperServerDelegate`
- 28 instance variables, 12 properties, 93 instance methods, 1 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMapTable" _lock_sceneToControllerMap;
@"NSMapTable" _lock_sceneToOrientationMap;
@"SBPosterBoardModalEditingManager" _posterBoardModalEditingManager;
@"PTSingleTestRecipe" _migrationTestRecipe;
@"PTSingleTestRecipe" _reloadTestRecipe;
@"PRSService" _posterBoardService;
@"FCActivityManager" _activityManager;
@"PRSWallpaperObserver" _posterBoardStateObserver;
@"PRSPosterConfiguration" _activeLockScreenPosterConfiguration;
@"PRSPosterConfiguration" _activeHomeScreenPosterConfiguration;
@"<PRSPosterConfigurationCacheProviding>" _posterCacheProvider;
@"PRSPosterConfiguration" _lastActiveLockScreenPosterConfiguration;
@"PRSPosterConfiguration" _lastActiveHomeScreenPosterConfiguration;
B _loadedLastActiveConfigurations;
B _updatedActiveConfigurations;
@"PBUIPosterWallpaperRemoteViewController" _posterWallpaperViewController;
B _createsPosterWallpaperViewController;
@"PBUIWallpaperConfigurationManager" _wallpaperConfigurationManager;
@"SBWallpaperController" _activeWallpaperController;
Q _transitionGeneration;
@"NSMapTable" _wallpaperServers;
@"NSMapTable" _batterySaverAnimationAssertions;
@"NSMapTable" _scaleAssertionsByController;
@"NSHashTable" _wallpaperLockScreenObservers;
@"NSHashTable" _wallpaperHomeScreenObservers;
@"SBWallpaperIconStyleCoordinator" _iconStyleCoordinator;
@"SBWallpaperServer" _legacyWallpaperServer;
```

## Properties

```
@property (T@"SBWallpaperServer",R,N,V_legacyWallpaperServer) legacyWallpaperServer;
@property (T@"PBUIPosterWallpaperRemoteViewController",R,N,V_posterWallpaperViewController) posterWallpaperViewController;
@property (T@"SBWallpaperController",W,N,V_activeWallpaperController) activeWallpaperController;
@property (T@"PRSPosterConfiguration",R,N) cachedLockScreenPosterConfiguration;
@property (T@"PRSPosterConfiguration",R,N) cachedHomeScreenPosterConfiguration;
@property (T@"PRSService",R,N,V_posterBoardService) posterBoardService;
@property (T@"PBUIWallpaperConfigurationManager",R,N,V_wallpaperConfigurationManager) wallpaperConfigurationManager;
@property (T@"SBWallpaperIconStyleCoordinator",R,N) iconStyleCoordinator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBWallpaperControllerCoordinator accessAuthenticator];
```

## Instance methods

```
-[SBWallpaperControllerCoordinator activeActivityDidChangeForManager:];
-[SBWallpaperControllerCoordinator iconStyleCoordinator];
-[SBWallpaperControllerCoordinator profileConnectionDidReceiveEffectiveSettingsChangedNotification:userInfo:];
-[SBWallpaperControllerCoordinator init];
-[SBWallpaperControllerCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBWallpaperControllerCoordinator dealloc];
-[SBWallpaperControllerCoordinator _determinedConfigurationForContext:];
-[SBWallpaperControllerCoordinator _interfaceOrientationForDeviceOrientation:];
-[SBWallpaperControllerCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBWallpaperControllerCoordinator availableActivitiesDidChangeForManager:];
-[SBWallpaperControllerCoordinator setDisplayContentModeCoordinator:];
-[SBWallpaperControllerCoordinator _normalizedBounds:forScreenBounds:];
-[SBWallpaperControllerCoordinator wallpaperConfigurationManager];
-[SBWallpaperControllerCoordinator _timeObscurableRatio];
-[SBWallpaperControllerCoordinator _screenBoundsForDisplayContext:orientation:];
-[SBWallpaperControllerCoordinator _cutoutBoundsForObstructionBounds:orientation:];
-[SBWallpaperControllerCoordinator _normalizedBounds:orientation:];
-[SBWallpaperControllerCoordinator _screenBoundsForOrientation:];
-[SBWallpaperControllerCoordinator wallpaperServer:fetchThumbnailDataForVariant:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:triggerPosterSignificantEventCompletionHandler:];
-[SBWallpaperControllerCoordinator _activePosterHasComplications];
-[SBWallpaperControllerCoordinator _activeWallpaperControllerWindowScene];
-[SBWallpaperControllerCoordinator _allWindowScenes];
-[SBWallpaperControllerCoordinator _applyCurrentMDMWallpaperPolicyToController:];
-[SBWallpaperControllerCoordinator _batterySaverModeChanged:];
-[SBWallpaperControllerCoordinator _committedInterfaceOrientationForActiveScene];
-[SBWallpaperControllerCoordinator _controlIdentityForExtensionBundleIdentifier:containerBundleIdentifier:kind:];
-[SBWallpaperControllerCoordinator _donateWallpaperViewControllerToController:];
-[SBWallpaperControllerCoordinator _handleMigrationTestRecipeAction];
-[SBWallpaperControllerCoordinator _handleReloadTestRecipeAction];
-[SBWallpaperControllerCoordinator _hasSubFullWidthLayoutForOrientation:displayContext:];
-[SBWallpaperControllerCoordinator _interfaceOrientationForDeviceOrientation:displayContext:];
-[SBWallpaperControllerCoordinator _invalidateBatterSaveAnimationAssertionForController:];
-[SBWallpaperControllerCoordinator _invalidateScaleAssertionsForController:];
-[SBWallpaperControllerCoordinator _isWallpaperObscuredOnWindowScene:];
-[SBWallpaperControllerCoordinator _loadLastActiveConfigurations];
-[SBWallpaperControllerCoordinator _mainDisplayWindowScene];
-[SBWallpaperControllerCoordinator _motionEffectsChanged];
-[SBWallpaperControllerCoordinator _normalizedCutoutFramesForElements:orientation:displayContext:];
-[SBWallpaperControllerCoordinator _notifyWhenWallpaperReadyToTransferWithTimeout:completion:];
-[SBWallpaperControllerCoordinator _offsetYForOrientation:displayContext:];
-[SBWallpaperControllerCoordinator _persistLastActiveHomeScreenPosterConfiguration:];
-[SBWallpaperControllerCoordinator _persistLastActiveLockScreenPosterConfiguration:];
-[SBWallpaperControllerCoordinator _posterQuickActionsConfigurationFromConfigurationRequest:];
-[SBWallpaperControllerCoordinator _pushPosterConfigurationToAllControllers];
-[SBWallpaperControllerCoordinator _registerStoredObserversOnPresenter];
-[SBWallpaperControllerCoordinator _suspendAnimationIfNeededForController:];
-[SBWallpaperControllerCoordinator _transferWallpaperFromController:toController:forTransitionGeneration:completion:];
-[SBWallpaperControllerCoordinator _transferWallpaperWithLockProvider:fromController:toController:forTransitionGeneration:shouldWaitForWallpaperReadiness:];
-[SBWallpaperControllerCoordinator acquireWallpaperScaleAssertion:forVariant:fromController:withAnimationFactory:];
-[SBWallpaperControllerCoordinator activeWallpaperController];
-[SBWallpaperControllerCoordinator addWallpaperObserver:forVariant:];
-[SBWallpaperControllerCoordinator allWallpaperControllers];
-[SBWallpaperControllerCoordinator cachedHomeScreenPosterConfiguration];
-[SBWallpaperControllerCoordinator cachedLockScreenPosterConfiguration];
-[SBWallpaperControllerCoordinator canDeferTransferOfWallpaperFromWindowScene:toWindowScene:];
-[SBWallpaperControllerCoordinator initWithLegacyWallpaperServer:createEditingManager:createPosterWallpaperViewController:];
-[SBWallpaperControllerCoordinator isValidServer:];
-[SBWallpaperControllerCoordinator legacyWallpaperServer];
-[SBWallpaperControllerCoordinator noteInterfaceOrientation:didCommitForScene:];
-[SBWallpaperControllerCoordinator posterBoardService];
-[SBWallpaperControllerCoordinator posterWallpaperViewController];
-[SBWallpaperControllerCoordinator receivePosterConfigurationUpdate:home:];
-[SBWallpaperControllerCoordinator registerWallpaperController:forScene:];
-[SBWallpaperControllerCoordinator removeWallpaperObserver:forVariant:];
-[SBWallpaperControllerCoordinator serverDelegateForServer:];
-[SBWallpaperControllerCoordinator setActiveWallpaperController:];
-[SBWallpaperControllerCoordinator setFencedUpdatesSuppressed:forWallpaperControllers:];
-[SBWallpaperControllerCoordinator setPosterWallpaperViewController:];
-[SBWallpaperControllerCoordinator setupWallpaperServerForScene:];
-[SBWallpaperControllerCoordinator teardownWallpaperServerForScene:];
-[SBWallpaperControllerCoordinator transferWallpaperViewControllerFromController:toController:completion:];
-[SBWallpaperControllerCoordinator transitionGeneration];
-[SBWallpaperControllerCoordinator unregisterWallpaperController:];
-[SBWallpaperControllerCoordinator wallpaperServer:fetchAdaptiveTimeBoundsForContext:timeHeight:displayContext:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:fetchAdaptiveTimeHeightLimitsForContext:displayContext:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:fetchAllLimitedOcclusionBoundsForOrientation:displayContext:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:fetchAllLockScreenContentCutoutBoundsForOrientation:displayContext:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:fetchAllLockScreenExtendedContentCutoutBoundsForOrientation:displayContext:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:fetchAllLockScreenMaximalContentCutoutBoundsForOrientation:displayContext:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:fetchAllLockScreenTimeBoundsForOrientation:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:fetchAllObscurableBoundsForOrientation:displayContext:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:fetchContentCutoutBoundsForVariant:orientation:displayContext:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:fetchLockScreenSubtitleBoundsForOrientation:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:fetchOriginalImageDataForVariant:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:fetchOriginalVideoURLDataForVariant:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:fetchSignificantEventsCounterForPosterWithIdentifier:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:handleQuickActionConfigurationRequest:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:restoreDefaultWallpaperWithCompletionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:setWallpaperColor:darkColor:forVariants:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:setWallpaperColorName:forVariants:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:setWallpaperGradient:forVariants:completionHandler:];
-[SBWallpaperControllerCoordinator wallpaperServer:setWallpaperVideoWithWallpaperMode:cropRect:wallpaperMode:completionHandler:];
```

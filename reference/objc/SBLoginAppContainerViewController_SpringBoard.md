# `SBLoginAppContainerViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBLockScreenViewControllerBase`
- Protocols: `SBLockScreenBatteryChargingViewControllerDelegate`, `SBLoginAppSceneHosterDelegate`, `PBUIWallpaperObserver`, `SBLockScreenPluginManagerDelegate`, `SBIdleTimerProviding`
- 11 instance variables, 5 properties, 63 instance methods, 0 class methods

## Instance variables

```
@"<SBLoginAppSceneHoster>" _sceneHoster;
@"SBLockScreenBatteryChargingViewController" _batteryChargingViewController;
@"SBLockScreenTemperatureWarningViewController" _thermalWarningViewController;
@"SBLoginAppContainerPluginWrapperViewController" _pluginWrapperViewController;
@"SBWindowSceneStatusBarSettingsAssertion" _statusBarAssertion;
@"NSMutableSet" _showStatusBarReasons;
@"<BSInvalidatable>" _deferOrientationUpdatesAssertion;
q _idleTimerMode;
@"SBLockScreenPluginManager" _pluginManager;
@"SBLockScreenManager" _lockScreenManager;
@"NSHashTable" _observers;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) hasIdleTimerBehaviors;
```

## Instance methods

```
-[SBLoginAppContainerViewController wallpaperDidChangeForVariant:];
-[SBLoginAppContainerViewController _updateLegibility];
-[SBLoginAppContainerViewController handleVolumeDownButtonPress];
-[SBLoginAppContainerViewController prepareForUIUnlock];
-[SBLoginAppContainerViewController suppressesScreenshots];
-[SBLoginAppContainerViewController viewWillDisappear:];
-[SBLoginAppContainerViewController dealloc];
-[SBLoginAppContainerViewController noteDeviceBlockedStatusUpdated];
-[SBLoginAppContainerViewController handleVolumeUpButtonPress];
-[SBLoginAppContainerViewController willUIUnlockFromSource:isLockScreenDisabledForAssertion:];
-[SBLoginAppContainerViewController handleHomeButtonDoublePress];
-[SBLoginAppContainerViewController viewWillAppear:];
-[SBLoginAppContainerViewController _canShowWhileLocked];
-[SBLoginAppContainerViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBLoginAppContainerViewController canBeDeactivatedForUIUnlockFromSource:];
-[SBLoginAppContainerViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBLoginAppContainerViewController disableLockScreenPluginWithContext:];
-[SBLoginAppContainerViewController loadView];
-[SBLoginAppContainerViewController shouldDisableALS];
-[SBLoginAppContainerViewController enableLockScreenPluginWithContext:];
-[SBLoginAppContainerViewController shouldAutoUnlockForSource:];
-[SBLoginAppContainerViewController hasIdleTimerBehaviors];
-[SBLoginAppContainerViewController prepareForUILock];
-[SBLoginAppContainerViewController suppressesControlCenter];
-[SBLoginAppContainerViewController startLockScreenFadeInAnimationForSource:];
-[SBLoginAppContainerViewController wallpaperLegibilitySettingsDidChange:forVariant:];
-[SBLoginAppContainerViewController shouldShowLockStatusBarTime];
-[SBLoginAppContainerViewController coordinatorRequestedIdleTimerBehavior:];
-[SBLoginAppContainerViewController _displayLayoutElementIdentifier];
-[SBLoginAppContainerViewController pluginManager:willUnloadPlugin:];
-[SBLoginAppContainerViewController _addBatteryChargingView];
-[SBLoginAppContainerViewController _cleanupBatteryChargingViewWithAnimationDuration:];
-[SBLoginAppContainerViewController _fadeViewsForChargingViewVisible:];
-[SBLoginAppContainerViewController _handleBacklightFadeEnded];
-[SBLoginAppContainerViewController _hostedAppBundleID];
-[SBLoginAppContainerViewController _hostedAppView];
-[SBLoginAppContainerViewController _hostedSceneIdentifier];
-[SBLoginAppContainerViewController _initWithSceneHoster:wallpaperController:lockScreenManager:backlightController:];
-[SBLoginAppContainerViewController _killLoginApp];
-[SBLoginAppContainerViewController _reallyAcquireStatusBarAssertionIfNecessaryInitiallyVisible:];
-[SBLoginAppContainerViewController _reallyRelinquishStatusBarAssertion];
-[SBLoginAppContainerViewController _removeBatteryChargingView];
-[SBLoginAppContainerViewController _setupLoginAppHosting];
-[SBLoginAppContainerViewController _setupLoginScene];
-[SBLoginAppContainerViewController _showOrHideThermalTrapUIAnimated:];
-[SBLoginAppContainerViewController _statusBarSettingsAssertion];
-[SBLoginAppContainerViewController _updateBatteryChargingViewAnimated:];
-[SBLoginAppContainerViewController addLoginObserver:];
-[SBLoginAppContainerViewController chargingViewControllerFadedOutContent:];
-[SBLoginAppContainerViewController initWithLockScreenManager:wallpaperController:backlightController:];
-[SBLoginAppContainerViewController loginContainerView];
-[SBLoginAppContainerViewController pluginManager:activePluginDidChange:];
-[SBLoginAppContainerViewController pluginManager:didLoadPlugin:];
-[SBLoginAppContainerViewController pluginManager:displayedPluginDidChangeFromPlugin:toPlugin:];
-[SBLoginAppContainerViewController pluginManager:displayedPluginDidUpdateAppearance:];
-[SBLoginAppContainerViewController pluginManager:plugin:handleAction:];
-[SBLoginAppContainerViewController removeLoginObserver:];
-[SBLoginAppContainerViewController requiresPasscodeInputForUIUnlockFromSource:withOptions:];
-[SBLoginAppContainerViewController sceneInvalidated];
-[SBLoginAppContainerViewController sceneUpdatedIdleTimerMode:];
-[SBLoginAppContainerViewController sceneUpdatedRotationMode:];
-[SBLoginAppContainerViewController sceneUpdatedStatusBarUserName:];
-[SBLoginAppContainerViewController sceneUpdatedWallpaperMode:];
```

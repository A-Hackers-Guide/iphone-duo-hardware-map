# `SBLockScreenCoordinator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `SBLockScreenPluginPresenting`, `SBLockScreenBiometricAuthenticationCoordinatorDelegate`, `SBBiometricUnlockBehavior`, `SBBiometricUnlockBehaviorDelegate`, `SBLockScreenActiveDisplayObserving`, `SBDisplayContentModeTransitionObserver`, `SBContinuousFoldSnapshotProviding`, `SBDoNotDisturbStateMonitorObserver`, `SBAutoUnlockRule`
- 27 instance variables, 23 properties, 100 instance methods, 0 class methods

## Instance variables

```
@"SBWindowSceneManager" _windowSceneManager;
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@"NSHashTable" _lockScreenManagers;
@"NSHashTable" _observers;
@"NSHashTable" _setupControllers;
@"SBLockScreenGlobalSuppressionAppearanceProvider" _globalSuppressionAppearanceProvider;
@"NSMapTable" _remoteContentSuppressionByToken;
@"SBFUserAuthenticationController" _userAuthenticationController;
@"SBLockScreenDisabledAssertionManager" _lockScreenDisabledAssertionManager;
@"SBLockScreenAutoUnlockAggregateRule" _autoUnlockRuleAggregator;
@"SBAutoUnlockComposableRule" _coverSheetAutoUnlockRule;
@"SBIdleTimerGlobalCoordinator" _idleTimerCoordinator;
@"CSCombinedListViewController" _combinedListViewController;
@"<SBSleepWakePolicyProviding>" _sleepWakePolicy;
@"SBPearlInterlockObserver" _pearlInterlockObserver;
@"NSMutableDictionary" _mesaAutoUnlockingDisabledAssertions;
@"NSMutableDictionary" _enabledLockScreenPlugins;
@"SBLockScreenStateCoordinator" _stateCoordinator;
@"<SBLockScreenActiveDisplayPolicyProviding>" _activeDisplayPolicy;
Q _startupTransitionState;
@"SBMesaUnlockFailureCounter" _mesaUnlockFailureCounter;
B _isChargeObservationConfigured;
@"SBLockScreenBiometricAuthenticationCoordinator" _biometricAuthenticationCoordinator;
@"SBHostedEntityTransferCoordinator" _hostedEntityTransferCoordinator;
@"<SBBiometricUnlockBehaviorDelegate>" _biometricUnlockBehaviorDelegate;
@"SBLockScreenIdleTimerCoordinator" _lockScreenIdleTimerCoordinator;
@"<SBNotificationDestination>" _notificationDestination;
```

## Properties

```
@property (T@"<SBSWidgetMetricsProviding>",R,N) widgetMetricsProvider;
@property (TB,R,N,GisAnyWindowSceneUILocked) anyWindowSceneUILocked;
@property (TB,R,N,GisAnyWindowSceneUIUnlocked) anyWindowSceneUIUnlocked;
@property (TB,R,N,GareAllWindowScenesUILocked) allWindowScenesUILocked;
@property (TB,R,N,GareAllWindowScenesUIUnlocked) allWindowScenesUIUnlocked;
@property (TB,R,N,GisAnyWindowSceneSuppressingLockButton) anyWindowSceneSuppressingLockButton;
@property (TB,R,N,GisAnyLockScreenVisible) anyLockScreenVisible;
@property (TB,R,N,GareAllLockScreensVisibleAndNotDisappearing) allLockScreensVisibleAndNotDisappearing;
@property (TB,R,N,GareAllWindowScenesInScreenOffMode) allWindowScenesInScreenOffMode;
@property (TB,R,N) hasUIEverBeenLocked;
@property (TB,R,N) isInLostMode;
@property (T@"SBLockScreenBiometricAuthenticationCoordinator",R,N,V_biometricAuthenticationCoordinator) biometricAuthenticationCoordinator;
@property (T@"SBMesaUnlockFailureCounter",R,N,V_mesaUnlockFailureCounter) mesaUnlockFailureCounter;
@property (T@"<SBLockScreenPluginPresenting>",R,N) pluginPresenter;
@property (T@"SBLockScreenIdleTimerCoordinator",R,N,V_lockScreenIdleTimerCoordinator) lockScreenIdleTimerCoordinator;
@property (TB,R,N) shouldUseLockScreenIdleTimer;
@property (T@"SBHostedEntityTransferCoordinator",R,N,V_hostedEntityTransferCoordinator) hostedEntityTransferCoordinator;
@property (T@"<SBNotificationDestination>",R,N,V_notificationDestination) notificationDestination;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBBiometricUnlockBehaviorDelegate>",W,N,V_biometricUnlockBehaviorDelegate) biometricUnlockBehaviorDelegate;
```

## Instance methods

```
-[SBLockScreenCoordinator hostedEntityTransferCoordinator];
-[SBLockScreenCoordinator isInLostMode];
-[SBLockScreenCoordinator mesaUnlockFailureCounter];
-[SBLockScreenCoordinator hasUIEverBeenLocked];
-[SBLockScreenCoordinator biometricAuthenticationCoordinator:requestsUnlockWithIntent:];
-[SBLockScreenCoordinator unlockUIFromSource:withOptions:];
-[SBLockScreenCoordinator areAllLockScreensVisibleAndNotDisappearing];
-[SBLockScreenCoordinator setSyncController:];
-[SBLockScreenCoordinator setOverrideActiveLockScreenManager:];
-[SBLockScreenCoordinator setBiometricAutoUnlockingDisabled:forReason:];
-[SBLockScreenCoordinator widgetMetricsProvider];
-[SBLockScreenCoordinator continuousFoldSnapshotConfigurationForCoordinator:transitionCoordinator:];
-[SBLockScreenCoordinator _noteAccessoryDetached:];
-[SBLockScreenCoordinator notificationDestination];
-[SBLockScreenCoordinator areAllWindowScenesInScreenOffMode];
-[SBLockScreenCoordinator _isContinuousFoldContext:];
-[SBLockScreenCoordinator _noteAccessoryAttached:];
-[SBLockScreenCoordinator _sendUILockStateChangedNotificationIfNeeded];
-[SBLockScreenCoordinator _shouldDisableALS];
-[SBLockScreenCoordinator _moveSetupViewToPrimaryWindowSceneWithContinuationLockProvider:];
-[SBLockScreenCoordinator noteContinuityDisplayWindowSceneConnectionDidChange];
-[SBLockScreenCoordinator succinctDescriptionBuilder];
-[SBLockScreenCoordinator _configFromWindowScene:];
-[SBLockScreenCoordinator removeObserver:];
-[SBLockScreenCoordinator init];
-[SBLockScreenCoordinator biometricAuthenticationCoordinatorShouldWaitToInvalidateMatchingAssertion:];
-[SBLockScreenCoordinator _lockFeaturesForRemoteLock:];
-[SBLockScreenCoordinator isAnyWindowSceneUIUnlocked];
-[SBLockScreenCoordinator displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBLockScreenCoordinator prefersContinuousSnapshotForWindowScenes:];
-[SBLockScreenCoordinator remoteLock:];
-[SBLockScreenCoordinator _updateDimmingForDNDState:];
-[SBLockScreenCoordinator displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBLockScreenCoordinator _updateBuddySuppression];
-[SBLockScreenCoordinator handleHeadsetButtonPress:];
-[SBLockScreenCoordinator biometricAuthenticationCoordinator:handleIdentityMatchSuccess:];
-[SBLockScreenCoordinator setPasscodeVisibleForActiveWindowScene:animated:];
-[SBLockScreenCoordinator setIdleTimerCoordinator:];
-[SBLockScreenCoordinator _updateSetupViewOwnershipForActiveLockScreenManager:];
-[SBLockScreenCoordinator unregisterSetupController:];
-[SBLockScreenCoordinator isSetupViewPresentedByControllerOtherThan:];
-[SBLockScreenCoordinator addLockScreenDisableAssertion:];
-[SBLockScreenCoordinator isAnyLockScreenVisible];
-[SBLockScreenCoordinator descriptionWithMultilinePrefix:];
-[SBLockScreenCoordinator isAnyWindowSceneSuppressingLockButton];
-[SBLockScreenCoordinator biometricUnlockBehavior:requestsFeedback:];
-[SBLockScreenCoordinator pluginPresenter];
-[SBLockScreenCoordinator updateRemoteContentAppearanceForToken:hidesTime:whitePointReduction:];
-[SBLockScreenCoordinator requestUserAttentionScreenWakeFromSource:reason:];
-[SBLockScreenCoordinator succinctDescription];
-[SBLockScreenCoordinator addObserver:];
-[SBLockScreenCoordinator _setupModeChanged];
-[SBLockScreenCoordinator wakeUIFromSource:withOptions:];
-[SBLockScreenCoordinator noteStartupTransitionDidBegin];
-[SBLockScreenCoordinator activeDisplayLockScreenManager];
-[SBLockScreenCoordinator _notifyCoverSheetsOfSuppressionChange];
-[SBLockScreenCoordinator _configureChargeObservationIfNeeded];
-[SBLockScreenCoordinator initWithWindowSceneManager:biometricResource:walletPreArmController:activeDisplayPolicy:];
-[SBLockScreenCoordinator lockScreenIdleTimerCoordinator];
-[SBLockScreenCoordinator _noteACStatusChanged:];
-[SBLockScreenCoordinator fingerPresenceDidChange:];
-[SBLockScreenCoordinator disableLockScreenPluginWithContext:];
-[SBLockScreenCoordinator handleMouseButtonDown:];
-[SBLockScreenCoordinator areAllWindowScenesUIUnlocked];
-[SBLockScreenCoordinator shouldUseLockScreenIdleTimer];
-[SBLockScreenCoordinator areAllWindowScenesUILocked];
-[SBLockScreenCoordinator connectedDeviceConfigurations];
-[SBLockScreenCoordinator enableLockScreenPluginWithContext:];
-[SBLockScreenCoordinator acquireStrictTouchCoverageAssertionForReason:];
-[SBLockScreenCoordinator shouldAutoUnlockForSource:];
-[SBLockScreenCoordinator _orderedTargetWindowScenesForBacklightAction:];
-[SBLockScreenCoordinator removeLockScreenManager:];
-[SBLockScreenCoordinator biometricUnlockBehaviorDelegate];
-[SBLockScreenCoordinator activeDisplayPolicy:didChangeFromLockScreenManager:toLockScreenManager:];
-[SBLockScreenCoordinator _setupControllerPresentingSetupViewOtherThan:];
-[SBLockScreenCoordinator initWithWindowSceneManager:userAuthenticationController:biometricAuthenticationCoordinator:pearlInterlockObserver:idleTimerCoordinator:displayContentModeCoordinator:sleepWakePolicy:activeDisplayPolicy:];
-[SBLockScreenCoordinator addLockScreenManager:];
-[SBLockScreenCoordinator _moveSecureAppToPrimaryWindowSceneForContext:continuationLockProvider:];
-[SBLockScreenCoordinator _orderedConnectedScenes];
-[SBLockScreenCoordinator handleBiometricEvent:];
-[SBLockScreenCoordinator _contextFromWindowScene:];
-[SBLockScreenCoordinator wakeUIFromSource:withOptions:customActionContext:];
-[SBLockScreenCoordinator connectedDisplayConfigurations];
-[SBLockScreenCoordinator handleKeyHIDEvent:];
-[SBLockScreenCoordinator doNotDisturbStateMonitor:didUpdateToState:];
-[SBLockScreenCoordinator biometricAuthenticationCoordinator];
-[SBLockScreenCoordinator _activeCoverSheetViewController];
-[SBLockScreenCoordinator registerSetupController:];
-[SBLockScreenCoordinator _lockScreenManagerForBiometricCoordinatorRequests];
-[SBLockScreenCoordinator biometricAuthenticationCoordinator:requestsAuthenticationFeedback:];
-[SBLockScreenCoordinator noteStartupTransitionWillBegin];
-[SBLockScreenCoordinator _sendStartupTransitionNotesIfNeeded:];
-[SBLockScreenCoordinator biometricUnlockBehavior:requestsUnlock:withFeedback:];
-[SBLockScreenCoordinator isAnyWindowSceneUILocked];
-[SBLockScreenCoordinator requestUserAttentionScreenWakeFromSource:reason:options:];
-[SBLockScreenCoordinator setBiometricUnlockBehaviorDelegate:];
-[SBLockScreenCoordinator removeLockScreenDisableAssertion:];
-[SBLockScreenCoordinator lockAllUIFromSource:withOptions:completion:];
-[SBLockScreenCoordinator isLockScreenDisabledForAssertion];
-[SBLockScreenCoordinator descriptionBuilderWithMultilinePrefix:];
```

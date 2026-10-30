# `SBMainWorkspace`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBWorkspace`
- Protocols: `BSTransactionObserver`, `FBSystemServiceDelegate`, `FBProcessManagerObserver`, `FBApplicationProcessObserver`, `BSWatchdogDelegate`, `FBSceneManagerObserver`, `SBBacklightCoordinatorObserver`, `SBPowerDownViewControllerDelegate`, `SBTransientOverlayScenePresenterDelegate`, `CCSModulePresentationEndpoint`, `SBControlCenterModuleTransientOverlayViewControllerDelegate`, `SBInCallPresentationManagerDelegate`, `SWSystemSleepObserver`, `SBWindowSceneAttachmentObserving`
- 22 instance variables, 14 properties, 167 instance methods, 5 class methods

## Instance variables

```
B _initialized;
@"BSEventQueueLock" _suspensionLock;
@"<BSInvalidatable>" _displayLayoutTransitionAssertion;
@"SBWorkspaceTransaction" _currentTransaction;
@"BSEventQueueLock" _currentTransactionLock;
@"BSWatchdog" _transactionWatchdog;
@"NSMutableDictionary" _extensionHandlersByType;
@"NSMutableSet" _activeSuspendedWorkspaceTransitions;
@"SBIdleTimerCoordinatorHelper" _idleTimerCoordinatorHelper;
@"SBPowerDownViewController" _powerDownViewController;
@"SBHomeHardwareButtonLongPressDurationAssertion" _powerDownLongPressDurationAssertion;
@"SBControlCenterModuleTransientOverlayViewController" _presentedControlCenterModuleTransientOverlayViewController;
@"NSMutableSet" _ocelotRepairRequests;
@"SBFocusModesHomeScreenSettingsManager" _focusModesHomeScreenSnapshotManager;
@"SBUntrustedURLLaunchThrottle" _untrustedURLLaunchThrottle;
@"SBApplicationController" _applicationController;
@"<SBIdleTimerProviding>" _activeIdleTimerProvider;
@"SBPIPControllerCoordinator" _pipCoordinator;
@"SBBackgroundMultitaskingManager" _backgroundMultitaskingManager;
@"SBInCallPresentationManager" _inCallPresentationManager;
@"SBTransientOverlayPresentationManager" _transientOverlayPresentationManager;
@"FBSceneManager" _sceneManager;
```

## Properties

```
@property (T@"SBBackgroundMultitaskingManager",R,N,V_backgroundMultitaskingManager) backgroundMultitaskingManager;
@property (T@"SBPIPControllerCoordinator",R,N,V_pipCoordinator) pipCoordinator;
@property (T@"SBInCallPresentationManager",R,N,V_inCallPresentationManager) inCallPresentationManager;
@property (T@"SBTransientOverlayPresentationManager",R,N,V_transientOverlayPresentationManager) transientOverlayPresentationManager;
@property (T@"SBWorkspaceTransaction",&,N,V_currentTransaction) currentTransaction;
@property (T@"FBSceneManager",R,N,V_sceneManager) sceneManager;
@property (T@"<SBIdleTimerProviding>",&,N,G_activeIdleTimerProvider,S_setActiveIdleTimerProvider:,V_activeIdleTimerProvider) activeIdleTimerProvider;
@property (TB,R,N,GisSpringBoardActive) springBoardActive;
@property (T@"<SBIdleTimerCoordinating>",&,N) idleTimerCoordinator;
@property (TB,R,N,GisPowerDownTransientOverlayTopmost) powerDownTransientOverlayFrontmost;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBMainWorkspace sharedInstance];
+[SBMainWorkspace debugDescription];
+[SBMainWorkspace sharedInstanceIfExists];
+[SBMainWorkspace _instanceIfExists];
+[SBMainWorkspace _sharedInstanceWithNilCheckPolicy:];
```

## Instance methods

```
-[SBMainWorkspace _suspend];
-[SBMainWorkspace systemSleepMonitorDidWakeFromSleep:];
-[SBMainWorkspace requestTransitionWithOptions:builder:validator:];
-[SBMainWorkspace _selectTransactionForTransientOverlayPresentationRequest:];
-[SBMainWorkspace defaultShouldAutorotateForTransientOverlayScenePresenter:];
-[SBMainWorkspace transientOverlayPresentationManager];
-[SBMainWorkspace _addStateCaptureHandlers];
-[SBMainWorkspace createRequestWithOptions:];
-[SBMainWorkspace inCallPresentationManager:interfaceOrientationForTransientOverlayPresentationInWindowScene:];
-[SBMainWorkspace canExecuteTransitionRequest:];
-[SBMainWorkspace currentTransaction];
-[SBMainWorkspace _canAppWithBundleIdentifier:requestMovingContentToSceneOpenApplicationOptions:];
-[SBMainWorkspace sceneManager];
-[SBMainWorkspace systemSleepMonitor:prepareForSleepWithCompletion:];
-[SBMainWorkspace _attemptUnlockToApplication:showPasscode:origin:givenOrigin:options:targetWindowScene:completion:];
-[SBMainWorkspace _resumeIfNeeded];
-[SBMainWorkspace idleTimerProvider:didProposeBehavior:forReason:];
-[SBMainWorkspace _sceneComparatorForApplication:keyboardFocusScene:];
-[SBMainWorkspace registerHandler:forExtensionPoint:];
-[SBMainWorkspace transientOverlayScenePresenter:didDismissViewController:wasTopmostPresentation:];
-[SBMainWorkspace _executeApplicationTransitionRequest:];
-[SBMainWorkspace dismissTransientOverlayViewController:animated:completion:];
-[SBMainWorkspace pipCoordinator];
-[SBMainWorkspace debugDescription];
-[SBMainWorkspace presentTransientOverlayViewController:originatingProcess:animated:completion:];
-[SBMainWorkspace transactionDidComplete:];
-[SBMainWorkspace inCallPresentationManager];
-[SBMainWorkspace isPowerDownTransientOverlayTopmost];
-[SBMainWorkspace _handleTrustedOpenRequestForApplication:options:activationSettings:origin:withResult:];
-[SBMainWorkspace setPipCoordinator:];
-[SBMainWorkspace watchdogFired:];
-[SBMainWorkspace transientOverlayScenePresenter:willPresentViewController:];
-[SBMainWorkspace applicationProcessDidExit:withContext:];
-[SBMainWorkspace _destroyApplicationSceneEntity:];
-[SBMainWorkspace init];
-[SBMainWorkspace _handleOpenApplicationRequest:options:activationSettings:origin:withResult:];
-[SBMainWorkspace applicationProcessWillLaunch:];
-[SBMainWorkspace _applicationForIdentifier:];
-[SBMainWorkspace windowSceneDidDisconnect:];
-[SBMainWorkspace processManager:didAddProcess:];
-[SBMainWorkspace powerDownViewControllerRequestsDismissal:];
-[SBMainWorkspace process:stateDidChangeFromState:toState:];
-[SBMainWorkspace transientOverlayScenePresenter:acquireBannerLongLookWindowLevelAssertionWithReason:windowLevel:];
-[SBMainWorkspace _parseShellArguments:];
-[SBMainWorkspace _transactionForTransitionRequest:];
-[SBMainWorkspace dealloc];
-[SBMainWorkspace transientOverlayScenePresenter:acquireSiriWindowLevelAssertionWithReason:windowLevel:];
-[SBMainWorkspace _canExecuteTransitionRequest:forExecution:];
-[SBMainWorkspace initWithApplicationController:inCallPresentationManager:transientOverlayPresentationManager:];
-[SBMainWorkspace transientOverlayScenePresenter:acquireProximitySensorEnabledAssertionWithReason:];
-[SBMainWorkspace _determineSourceForTransitionRequest:];
-[SBMainWorkspace transientOverlayScenePresenterRequestsSiriDismissal:animated:];
-[SBMainWorkspace systemService:isPasscodeLockedOrBlockedWithResult:];
-[SBMainWorkspace setIdleTimerCoordinator:];
-[SBMainWorkspace _targetWindowSceneForApplication:options:settings:requireForeground:targetDisplayConfiguration:error:];
-[SBMainWorkspace inCallPresentationManagerRequestsHandlingOfDeferredUILock:];
-[SBMainWorkspace _selectTransactionForAppRelaunch:];
-[SBMainWorkspace powerDownViewControllerDidDisappear:];
-[SBMainWorkspace transactionForTransitionRequest:];
-[SBMainWorkspace _isResumed];
-[SBMainWorkspace bannerLongLookPresentationObservationTokenForTransientOverlayScenePresenter:];
-[SBMainWorkspace transientOverlayScenePresenter:newSceneDeactivationAssertionWithReason:];
-[SBMainWorkspace _cleanupForRemovedAppEntity:];
-[SBMainWorkspace systemSleepMonitorWillWakeFromSleep:];
-[SBMainWorkspace _finishInitialization];
-[SBMainWorkspace dismissTransientOverlayPresentationsAnimated:windowScene:filter:];
-[SBMainWorkspace _activeIdleTimerProvider];
-[SBMainWorkspace _canImplicitlyUnlockAtLockScreenWhileAuthenticatedFromOrigin:givenOrigin:trustedRequest:outReason:];
-[SBMainWorkspace watchdogStarted:];
-[SBMainWorkspace createRequestForApplicationActivation:options:];
-[SBMainWorkspace dismissAllTransientOverlayPresentationsAnimated:];
-[SBMainWorkspace isSpringBoardActive];
-[SBMainWorkspace presentPowerDownTransientOverlay];
-[SBMainWorkspace _executeTransitionRequest:options:validator:];
-[SBMainWorkspace _validateRequestToOpenApplication:options:origin:error:];
-[SBMainWorkspace _applicationProcessExited:withContext:];
-[SBMainWorkspace presentModuleWithIdentifier:options:completion:];
-[SBMainWorkspace transientOverlayScenePresenter:preferredWhitePointAdaptivityStyleDidChangeWithAnimationSettings:];
-[SBMainWorkspace transientOverlayScenePresenterRequestsControlCenterDismissal:animated:];
-[SBMainWorkspace transientOverlayScenePresenter:acquireInteractiveScreenshotGestureDisabledAssertionWithReason:];
-[SBMainWorkspace processDidExit:];
-[SBMainWorkspace idleTimerCoordinator];
-[SBMainWorkspace controlCenterPresentationObservationTokenForTransientOverlayScenePresenter:];
-[SBMainWorkspace currentStatusBarSettingsForTransientOverlayScenePresenter:];
-[SBMainWorkspace isApplicationRunningAsViewService:];
-[SBMainWorkspace _selectTransactionForReturningToTheLockScreenWithRequest:];
-[SBMainWorkspace _handlerForExtensionPoint:];
-[SBMainWorkspace transientOverlayScenePresenter:acquireHideAppStatusBarAssertionWithReason:animated:];
-[SBMainWorkspace processManager:didRemoveProcess:];
-[SBMainWorkspace _handleUntrustedOpenRequestForApplication:options:activationSettings:origin:withResult:];
-[SBMainWorkspace _alertItemForPreventingLaunchOfApp:fromTrustState:];
-[SBMainWorkspace requestTransitionWithOptions:displayConfiguration:builder:validator:];
-[SBMainWorkspace executeTransitionRequest:withValidator:];
-[SBMainWorkspace backgroundMultitaskingManager];
-[SBMainWorkspace requestTransitionWithBuilder:];
-[SBMainWorkspace systemService:prepareForShutdownWithOptions:origin:];
-[SBMainWorkspace _selectTransactionForAppEntityRemoved:];
-[SBMainWorkspace _addRequestCompletionBlock:toTransaction:];
-[SBMainWorkspace _initializeAndObserveDefaults];
-[SBMainWorkspace transientOverlayScenePresenterRequestsAppIconForceTouchDismissal:animated:];
-[SBMainWorkspace _cleanupAppRepairRequest:];
-[SBMainWorkspace executeTransitionRequest:];
-[SBMainWorkspace systemService:canActivateApplication:withResult:];
-[SBMainWorkspace transientOverlayScenePresenter:unregisterCoverSheetExternalBehaviorProvider:];
-[SBMainWorkspace _coversheetDidDismiss];
-[SBMainWorkspace _siriWorkspaceTransitionOptionsFromOpenApplicationOptions:];
-[SBMainWorkspace _noteDidWakeFromSleep];
-[SBMainWorkspace transientOverlayScenePresenter:acquireDeviceOrientationUpdateDeferralAssertionWithReason:];
-[SBMainWorkspace createRequestWithOptions:displayConfiguration:];
-[SBMainWorkspace _dismissPresentedControlCenterModule:];
-[SBMainWorkspace transientOverlayScenePresenter:acquireDisableAutoUnlockAssertionWithReason:];
-[SBMainWorkspace hasIdleTimerBehaviors];
-[SBMainWorkspace _proposeIdleTimerBehaviorForReason:];
-[SBMainWorkspace inCallPresentationManager:interfaceOrientationForBannerPresentationInWindowScene:];
-[SBMainWorkspace powerDownViewControllerRequestsPowerDown:];
-[SBMainWorkspace backlightCoordinator:didUpdateAggregateBacklightState:fromSource:];
-[SBMainWorkspace transientOverlayScenePresenter:shouldResignFirstResponderForKeyWindow:];
-[SBMainWorkspace initWithEventQueue:];
-[SBMainWorkspace setCurrentTransaction:];
-[SBMainWorkspace _executeSuspendedTransactionForRequest:];
-[SBMainWorkspace _handleSetupExited:];
-[SBMainWorkspace _activateApplicationFromAccessibility:];
-[SBMainWorkspace _broadcastCurrentTransaction];
-[SBMainWorkspace applicationProcessDebuggingStateDidChange:];
-[SBMainWorkspace _selectTransactionForAppActivationUnderMainScreenLock:withResult:];
-[SBMainWorkspace systemService:handleOpenApplicationRequest:withCompletion:];
-[SBMainWorkspace _preflightWebBrowserApplication:url:outError:];
-[SBMainWorkspace systemService:handleActions:origin:withResult:];
-[SBMainWorkspace _removeApplicationEntities:withDestructionIntent:completion:];
-[SBMainWorkspace inCallPresentationManager:createPresentationSessionWithSceneHandle:];
-[SBMainWorkspace _selectTransactionForAppActivationUnderMainScreenLockRequest:];
-[SBMainWorkspace transientOverlayScenePresenter:acquireControlCenterWindowLevelAssertionWithReason:windowLevel:];
-[SBMainWorkspace _handleUserActionRequest:options:activationSettings:origin:withResult:];
-[SBMainWorkspace _preflightTransitionRequest:forExecution:];
-[SBMainWorkspace _defaultSiriWorkspaceTransitionOptions];
-[SBMainWorkspace siriPresentationObservationTokenForTransientOverlayScenePresenter:];
-[SBMainWorkspace dismissPowerDownTransientOverlayWithCompletion:];
-[SBMainWorkspace _setCurrentTransactionForRequest:fallbackProvider:];
-[SBMainWorkspace _isLaunchingApplicationAfterSetupForRequestWithBundleIdentifier:options:origin:];
-[SBMainWorkspace windowSceneDidConnect:];
-[SBMainWorkspace _coversheetDidPresent];
-[SBMainWorkspace isKeyboardVisibleForSpringBoardForTransientOverlayScenePresenter:];
-[SBMainWorkspace transientOverlayScenePresenter:shouldRestoreFirstResponderForKeyWindow:];
-[SBMainWorkspace _selectTransactionForAppActivationRequest:];
-[SBMainWorkspace backlightCoordinator:willUpdateAggregateBacklightState:fromSource:];
-[SBMainWorkspace _updateActivationSettings:forRequestWithOptions:clientProcess:application:];
-[SBMainWorkspace applicationProcessDidLaunch:];
-[SBMainWorkspace _setActiveIdleTimerProvider:];
-[SBMainWorkspace unregisterHandler:forExtensionPoint:];
-[SBMainWorkspace _generateIdleTimerBehaviorForReason:];
-[SBMainWorkspace _executeTransientOverlayTransitionRequest:];
-[SBMainWorkspace defaultSupportedInterfaceOrientationsForTransientOverlayScenePresenter:];
-[SBMainWorkspace presentTransientOverlayViewController:animated:completion:];
-[SBMainWorkspace systemServiceApplicationInfoProvider:];
-[SBMainWorkspace systemSleepMonitorSleepRequestAborted:];
-[SBMainWorkspace controlCenterModuleTransientOverlayViewControllerNeedsDismissal:];
-[SBMainWorkspace transientOverlayScenePresenter:registerCoverSheetExternalBehaviorProvider:];
-[SBMainWorkspace requestTransitionWithOptions:displayConfiguration:builder:];
-[SBMainWorkspace createRequestForApplicationActivation:withDisplayConfiguration:options:];
-[SBMainWorkspace defaultPreferredInterfaceOrientationForPresentationForTransientOverlayScenePresenter:];
-[SBMainWorkspace coordinatorRequestedIdleTimerBehavior:];
-[SBMainWorkspace _targetWindowSceneForApplication:preferringDisplay:requireForeground:options:];
-[SBMainWorkspace systemServicePrepareForExit:andRelaunch:];
-[SBMainWorkspace transientOverlayScenePresenter:acquireWallpaperAnimationSuspensionAssertionForWallpaperController:withReason:];
-[SBMainWorkspace _handleBuddyLaunchFinished];
-[SBMainWorkspace _selectTransactionForReturningToTheLockScreenAndForceToBuddy:];
-[SBMainWorkspace _removeApplicationEntitiesFromWorkspace:error:];
```

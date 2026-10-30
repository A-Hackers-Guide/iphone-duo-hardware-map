# `SBAlertItemsController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `SBDisplayContentModeTransitionObserver`
- 28 instance variables, 11 properties, 81 instance methods, 1 class methods

## Instance variables

```
@"SBUserSessionController" _userSessionController;
@"SBRestartManager" _restartManager;
@"SBApplicationController" _applicationController;
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@"SBAlertItemsObjectQueue" _alertItemsQueue;
@"SBAlertItemsObjectQueue" _superModalItemsQueue;
@"NSMutableSet" _pendedAlertsToReenqueuePostDismissal;
@"NSMutableOrderedSet" _alertItemPresentations;
@"NSMutableOrderedSet" _superModalAlertItemPresentations;
@"NSMutableSet" _activePresenters;
@"NSMutableSet" _forceAlertsToPendReasons;
@"NSMapTable" _suppressionAssertionReasons;
@"NSHashTable" _observers;
B _inUILockedMode;
B _isContinuityDisplaySceneConnected;
B _isProcessingQueue;
B _delayProcessingQueue;
B _suppressAlertsForKeynote;
@"<BSInvalidatable>" _stateCaptureBlock;
@"<BSInvalidatable>" _systemModalAlertVisibleAssertion;
@"SBModalAlertPresenter" _systemModalAlertPresenter;
@"FBSDisplayLayoutMonitor" _layoutMonitor;
@"SBWindowSceneManager" _windowSceneManager;
@"<SBAlertItemPresenter><SBFLockScreenActionProvider>" _lockScreenModalAlertItemPresenter;
@"<SBAlertItemPresenter>" _lockScreenNotificationsAlertItemPresenter;
@"<SBAlertItemPresenter>" _unlockedNotificationsAlertItemPresenter;
@"<SBAlertItemPresenter>" _systemApertureAlertItemPresenter;
@"<SBAlertItemPresenter>" _unlockedAlertItemPresenter;
```

## Properties

```
@property (T@"SBModalAlertPresenter",&,N,G_systemModalAlertPresenter,S_setSystemModalAlertPresenter:,V_systemModalAlertPresenter) systemModalAlertPresenter;
@property (T@"SBWindowSceneManager",W,N,V_windowSceneManager) windowSceneManager;
@property (T@"<SBAlertItemPresenter><SBFLockScreenActionProvider>",&,N,V_lockScreenModalAlertItemPresenter) lockScreenModalAlertItemPresenter;
@property (T@"<SBAlertItemPresenter>",&,N,V_lockScreenNotificationsAlertItemPresenter) lockScreenNotificationsAlertItemPresenter;
@property (T@"<SBAlertItemPresenter>",&,N,V_unlockedNotificationsAlertItemPresenter) unlockedNotificationsAlertItemPresenter;
@property (T@"<SBAlertItemPresenter>",&,N,V_systemApertureAlertItemPresenter) systemApertureAlertItemPresenter;
@property (T@"<SBAlertItemPresenter>",&,N,V_unlockedAlertItemPresenter) unlockedAlertItemPresenter;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBAlertItemsController sharedInstance];
```

## Instance methods

```
-[SBAlertItemsController succinctDescriptionBuilder];
-[SBAlertItemsController removeObserver:];
-[SBAlertItemsController windowSceneDidDisconnect:];
-[SBAlertItemsController displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBAlertItemsController dealloc];
-[SBAlertItemsController displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBAlertItemsController _updateActiveDestinations];
-[SBAlertItemsController descriptionWithMultilinePrefix:];
-[SBAlertItemsController succinctDescription];
-[SBAlertItemsController addObserver:];
-[SBAlertItemsController windowSceneManager];
-[SBAlertItemsController setWindowSceneManager:];
-[SBAlertItemsController description];
-[SBAlertItemsController descriptionBuilderWithMultilinePrefix:];
-[SBAlertItemsController _notifyObservers:];
-[SBAlertItemsController activateAlertItem:];
-[SBAlertItemsController deactivateAlertItem:reason:];
-[SBAlertItemsController _silencingHardwareButtonPressed:];
-[SBAlertItemsController deactivateAlertItem:];
-[SBAlertItemsController activatePendedAlertsIfNecessary];
-[SBAlertItemsController hasVisibleAlert];
-[SBAlertItemsController setForceAlertsToPend:forReason:];
-[SBAlertItemsController _activeCallStateDidChange:];
-[SBAlertItemsController _activePresenterForAlertItem:];
-[SBAlertItemsController _buddyDidExit];
-[SBAlertItemsController _clearAllQueuedAlertItems];
-[SBAlertItemsController _deactivateAlertItem:reason:animated:];
-[SBAlertItemsController _deactivateAlertItem:reason:animated:alertDismissCompletion:];
-[SBAlertItemsController _dismissAlertItem:fromPresenter:forReason:animated:completion:];
-[SBAlertItemsController _enumeratePresentationsWithType:usingBlock:];
-[SBAlertItemsController _enumerateWithDirection:presentationsWithType:usingBlock:];
-[SBAlertItemsController _hasActivePresentationsThatPresentModally];
-[SBAlertItemsController _hasPresentationForPresenter:];
-[SBAlertItemsController _hasVisibleModalAlertOfType:];
-[SBAlertItemsController _hasVisibleModalAlertOfType:forWindowScene:];
-[SBAlertItemsController _isAlertItemPresentable:outReasonsNotPresentable:];
-[SBAlertItemsController _performBatchActions:animated:processQueue:];
-[SBAlertItemsController _presentAlertItem:withPresenter:animated:];
-[SBAlertItemsController _presentationForAlertItem:];
-[SBAlertItemsController _presentedAlertItemForPresenter:];
-[SBAlertItemsController _presenterForAlertItem:];
-[SBAlertItemsController _processAlertItemQueuesAnimated:];
-[SBAlertItemsController _processAlertItemsFromQueue:animated:];
-[SBAlertItemsController _reallyDeactivateAlertItem:forReason:deactivateBlock:];
-[SBAlertItemsController _setSystemModalAlertPresenter:];
-[SBAlertItemsController _shouldPendAlertItem:outReasonsPended:];
-[SBAlertItemsController _systemModalAlertPresenter];
-[SBAlertItemsController activateAlertItem:animated:];
-[SBAlertItemsController alertItemsOfClass:];
-[SBAlertItemsController canDeactivateAlertForMenuClickOrSystemGesture];
-[SBAlertItemsController captureSuppressionAssertion:reason:];
-[SBAlertItemsController convertLockedAlertsToUnlockedAlerts];
-[SBAlertItemsController convertUnlockedAlertsToLockedAlerts];
-[SBAlertItemsController deactivateAlertForMenuClickOrSystemGestureWithAnimation:];
-[SBAlertItemsController deactivateAlertItem:reason:animated:];
-[SBAlertItemsController deactivateAlertItemsOfClass:];
-[SBAlertItemsController deactivateAlertItemsOfClass:reason:];
-[SBAlertItemsController deactivateAlertItemsOfClass:reason:animated:];
-[SBAlertItemsController hasAlertOfClass:];
-[SBAlertItemsController hasAlerts];
-[SBAlertItemsController hasLockScreenModalAlert];
-[SBAlertItemsController hasVisibleAlertForWindowScene:];
-[SBAlertItemsController hasVisibleModalAlert];
-[SBAlertItemsController hasVisibleSuperModalAlert];
-[SBAlertItemsController initWithUserSessionController:restartManager:applicationController:displayContentModeCoordinator:];
-[SBAlertItemsController lockScreenModalAlertItemPresenter];
-[SBAlertItemsController lockScreenNotificationsAlertItemPresenter];
-[SBAlertItemsController moveActiveUnlockedAlertsToPendingWithAnimation:completion:];
-[SBAlertItemsController presentedAlertItems];
-[SBAlertItemsController setInUILockedMode:];
-[SBAlertItemsController setIsContinuityDisplaySceneConnected:];
-[SBAlertItemsController setLockScreenModalAlertItemPresenter:];
-[SBAlertItemsController setLockScreenNotificationsAlertItemPresenter:];
-[SBAlertItemsController setSystemApertureAlertItemPresenter:];
-[SBAlertItemsController setUnlockedAlertItemPresenter:];
-[SBAlertItemsController setUnlockedNotificationsAlertItemPresenter:];
-[SBAlertItemsController systemApertureAlertItemPresenter];
-[SBAlertItemsController unlockedAlertItemPresenter];
-[SBAlertItemsController unlockedNotificationsAlertItemPresenter];
-[SBAlertItemsController visibleAlertItem];
-[SBAlertItemsController windowSceneDidConnect:withSharedModalAlertItemPresenter:];
```

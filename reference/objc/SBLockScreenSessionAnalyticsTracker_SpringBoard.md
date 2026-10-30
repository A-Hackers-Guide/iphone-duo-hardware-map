# `SBLockScreenSessionAnalyticsTracker`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSCoverSheetViewControllerObserver`, `CSExternalEventHandling`, `SBAmbientPresentationObserver`, `SBBacklightCoordinatorObserver`, `SBLockScreenCoordinatorObserving`, `SBSecureAppObserver`, `SBUIBiometricResourceObserver`, `SBUIPhoneUnlockWithWatchControllerObserver`
- 20 instance variables, 6 properties, 38 instance methods, 0 class methods

## Instance variables

```
@"SBBacklightCoordinator" _backlightCoordinator;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"<SBLockScreenActiveDisplayPolicyProviding>" _activeDisplayPolicy;
@"<SBUIBiometricResource>" _biometricResource;
@"SBUIPhoneUnlockWithWatchController" _phoneUnlockWithWatchController;
@"SBSecureAppManager" _secureAppManager;
@"NSNotificationCenter" _notificationCenter;
@"<SBLockScreenSessionAnalyticsEnvironment>" _environment;
@"<SBLockScreenSessionAnalyticsReporting>" _reporter;
@"SBLockScreenSessionAnalyticsCollector" _collector;
@"_SBLockScreenSessionAnalyticsEventForwarder" _analyticsEventForwarder;
@"NSHashTable" _coverSheetViewControllers;
@"NSHashTable" _ambientPresentationControllers;
@"CSCoverSheetViewController" _cameraCoverSheetViewController;
@"NSMutableArray" _activeSecureAppTypes;
q _pendingDismissalMethod;
q _pendingLaunchOrigin;
q _pendingDismissalDestination;
q _pendingTapToWakeLocation;
B _backlightActive;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
```

## Instance methods

```
-[SBLockScreenSessionAnalyticsTracker handleEvent:];
-[SBLockScreenSessionAnalyticsTracker wouldHandleButtonEvent:];
-[SBLockScreenSessionAnalyticsTracker dealloc];
-[SBLockScreenSessionAnalyticsTracker ambientPresentationController:didUpdatePresented:];
-[SBLockScreenSessionAnalyticsTracker lockScreenCoordinator:didAddLockScreenManager:];
-[SBLockScreenSessionAnalyticsTracker _lockScreenUIWillDismiss:];
-[SBLockScreenSessionAnalyticsTracker backlightCoordinator:didUpdateAggregateBacklightState:fromSource:];
-[SBLockScreenSessionAnalyticsTracker conformsToCSEventHandling];
-[SBLockScreenSessionAnalyticsTracker coverSheetIdentifier];
-[SBLockScreenSessionAnalyticsTracker _ambientPresentationControllerDidConnect:];
-[SBLockScreenSessionAnalyticsTracker lockScreenCoordinator:didRemoveLockScreenManager:];
-[SBLockScreenSessionAnalyticsTracker secureAppOfTypeDidEnd:];
-[SBLockScreenSessionAnalyticsTracker backlightCoordinator:willUpdateAggregateBacklightState:fromSource:];
-[SBLockScreenSessionAnalyticsTracker participantState];
-[SBLockScreenSessionAnalyticsTracker secureAppOfTypeDidBegin:];
-[SBLockScreenSessionAnalyticsTracker biometricResource:observeEvent:];
-[SBLockScreenSessionAnalyticsTracker phoneUnlockWithWatchControllerAttemptFailed:withError:];
-[SBLockScreenSessionAnalyticsTracker phoneUnlockWithWatchControllerAttemptSucceeded:];
-[SBLockScreenSessionAnalyticsTracker coverSheetViewControllerDidSettleOnPage:mainPage:];
-[SBLockScreenSessionAnalyticsTracker _willExecuteNotificationAction:];
-[SBLockScreenSessionAnalyticsTracker _willUnlockToLaunchApplication:];
-[SBLockScreenSessionAnalyticsTracker _authenticationRequestCompleted:];
-[SBLockScreenSessionAnalyticsTracker _didFailToUnlockToLaunchApplication:];
-[SBLockScreenSessionAnalyticsTracker _isActiveDisplayAmbientPresentationController:];
-[SBLockScreenSessionAnalyticsTracker _isActiveDisplayCoverSheet:];
-[SBLockScreenSessionAnalyticsTracker _isActiveDisplayLockScreenManager:];
-[SBLockScreenSessionAnalyticsTracker _isShowingLockScreen];
-[SBLockScreenSessionAnalyticsTracker _lockScreenUIDidDismiss:];
-[SBLockScreenSessionAnalyticsTracker _noteCurrentSecureApp];
-[SBLockScreenSessionAnalyticsTracker _prepareForSessionStart];
-[SBLockScreenSessionAnalyticsTracker _redirectNotificationToMainThreadIfNeeded:selector:];
-[SBLockScreenSessionAnalyticsTracker _resetPendingDismissal];
-[SBLockScreenSessionAnalyticsTracker _restToOpenDidFire:];
-[SBLockScreenSessionAnalyticsTracker _tapToWakeDidRecognizeTap:];
-[SBLockScreenSessionAnalyticsTracker _userDismissGestureDidBegin:];
-[SBLockScreenSessionAnalyticsTracker handleAnalyticsBackendEventType:];
-[SBLockScreenSessionAnalyticsTracker initWithBacklightCoordinator:lockScreenCoordinator:activeDisplayPolicy:];
-[SBLockScreenSessionAnalyticsTracker initWithBacklightCoordinator:lockScreenCoordinator:activeDisplayPolicy:biometricResource:phoneUnlockWithWatchController:secureAppManager:notificationCenter:analyticsBackend:environment:reporter:timeProvider:];
```

# `SBNCAlertingController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NCAlertingController`, `CSAlertingControlling`, `SBWindowSceneAttachmentObserving`
- 7 instance variables, 11 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"SBNCSoundController" _soundController;
@"SBNCScreenController" _screenController;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"SBCommunicationPolicyManager" _communicationPolicyManager;
@"SBApplicationController" _applicationController;
@"NCNotificationRequest" _activeRequestWithRealerts;
@"NSMutableSet" _realertTimers;
```

## Properties

```
@property (T@"SBNCSoundController",&,N,V_soundController) soundController;
@property (T@"SBNCScreenController",&,N,V_screenController) screenController;
@property (T@"SBLockScreenCoordinator",&,N,V_lockScreenCoordinator) lockScreenCoordinator;
@property (T@"SBCommunicationPolicyManager",&,N,V_communicationPolicyManager) communicationPolicyManager;
@property (T@"SBApplicationController",&,N,V_applicationController) applicationController;
@property (T@"NCNotificationRequest",&,N,V_activeRequestWithRealerts) activeRequestWithRealerts;
@property (T@"NSMutableSet",&,N,V_realertTimers) realertTimers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBNCAlertingController applicationController];
-[SBNCAlertingController _activeAlertDestinationsInRequestDestinations:];
-[SBNCAlertingController _alertNowForNotificationRequest:];
-[SBNCAlertingController _killRealertsForNotificationRequest:];
-[SBNCAlertingController init];
-[SBNCAlertingController killAlertsForNotificationRequest:];
-[SBNCAlertingController killRealerts];
-[SBNCAlertingController windowSceneDidDisconnect:];
-[SBNCAlertingController realertTimers];
-[SBNCAlertingController _scheduleRealertsForNotificationRequest:];
-[SBNCAlertingController alertOnPresentationForNotificationRequest:presentingDestination:];
-[SBNCAlertingController setApplicationController:];
-[SBNCAlertingController _shouldScreenTimeSuppressNotificationRequest:];
-[SBNCAlertingController screenController];
-[SBNCAlertingController alertOnPostForNotificationRequest:forRequestDestinations:];
-[SBNCAlertingController _isBundleIdentifierBlockedForCommunicationPolicy:];
-[SBNCAlertingController setScreenController:];
-[SBNCAlertingController _shouldScreenTimeSuppressNotificationsForBundleIdentifier:];
-[SBNCAlertingController _lockStateChanged];
-[SBNCAlertingController soundController];
-[SBNCAlertingController _isBundleIdentifierBlockedForScreenTimeExpiration:];
-[SBNCAlertingController _shouldRealert];
-[SBNCAlertingController _hardwareButtonPressed:];
-[SBNCAlertingController resetAutomaticLockStateForNotificationRequest:];
-[SBNCAlertingController setCommunicationPolicyManager:];
-[SBNCAlertingController activeRequestWithRealerts];
-[SBNCAlertingController setActiveRequestWithRealerts:];
-[SBNCAlertingController setRealertTimers:];
-[SBNCAlertingController communicationPolicyManager];
-[SBNCAlertingController windowSceneDidConnect:];
-[SBNCAlertingController setSoundController:];
-[SBNCAlertingController _alertNowForNotificationRequest:presentingDestination:];
-[SBNCAlertingController _notificationCenterDidPresent];
-[SBNCAlertingController lockScreenCoordinator];
-[SBNCAlertingController _realertTimerFired:];
-[SBNCAlertingController setLockScreenCoordinator:];
-[SBNCAlertingController initWithSoundController:screenController:lockScreenCoordinator:communicationPolicyManager:applicationController:];
```

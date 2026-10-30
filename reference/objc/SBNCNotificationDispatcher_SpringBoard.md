# `SBNCNotificationDispatcher`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSCoverSheetViewControllerObserver`, `SBUnlockRequestHandling`, `SBFNotificationExtensionVisibilityProviding`, `CSNCNotificationDispatching`, `SBWindowSceneAttachmentObserving`
- 16 instance variables, 23 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"SBNotificationBannerDestination" _bannerDestination;
@"SBWalletNotificationSource" _walletNotificationSource;
@"SBNotificationCenterDestination" _notificationCenterDestination;
@"NCNotificationDispatcher" _dispatcher;
@"SBNCNotificationDispatcherDelegate" _dispatcherDelegate;
@"NCBulletinNotificationSource" _notificationSource;
@"SBUserAlertNotificationSource" _userNotificationAlertSource;
@"SBUserAlertNotificationSource" _unlockedBannerAlertSource;
@"SBApplicationController" _applicationController;
@"SBWindowSceneManager" _windowSceneManager;
@"SBBacklightCoordinator" _backlightCoordinator;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"SBNotificationCarPlayDestination" _carDestination;
@"SBCommunicationPolicyManager" _communicationPolicyManager;
@"SBNCAlertingController" _alertingController;
@"NSHashTable" _windowScenes;
```

## Properties

```
@property (T@"NCNotificationDispatcher",&,N,V_dispatcher) dispatcher;
@property (T@"SBNCNotificationDispatcherDelegate",&,N,V_dispatcherDelegate) dispatcherDelegate;
@property (T@"NCBulletinNotificationSource",&,N,V_notificationSource) notificationSource;
@property (T@"SBUserAlertNotificationSource",&,N,V_userNotificationAlertSource) userNotificationAlertSource;
@property (T@"SBUserAlertNotificationSource",&,N,V_unlockedBannerAlertSource) unlockedBannerAlertSource;
@property (T@"SBApplicationController",&,N,V_applicationController) applicationController;
@property (T@"SBWindowSceneManager",&,N,V_windowSceneManager) windowSceneManager;
@property (T@"SBBacklightCoordinator",&,N,V_backlightCoordinator) backlightCoordinator;
@property (T@"SBLockScreenCoordinator",&,N,V_lockScreenCoordinator) lockScreenCoordinator;
@property (T@"SBNotificationCarPlayDestination",&,N,V_carDestination) carDestination;
@property (T@"SBCommunicationPolicyManager",&,N,V_communicationPolicyManager) communicationPolicyManager;
@property (T@"SBNCAlertingController",&,N,V_alertingController) alertingController;
@property (T@"NSHashTable",&,N,V_windowScenes) windowScenes;
@property (T@"SBNotificationBannerDestination",R,N,V_bannerDestination) bannerDestination;
@property (T@"<SBNotificationDestination>",R,N) dashBoardDestination;
@property (T@"SBWalletNotificationSource",R,N,V_walletNotificationSource) walletNotificationSource;
@property (T@"SBNotificationCenterDestination",R,N,V_notificationCenterDestination) notificationCenterDestination;
@property (TB,R,N) isCarDestinationActive;
@property (T@"BSServiceConnectionEndpoint",R,N) carOpenServiceEndpoint;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBNCNotificationDispatcher dispatcher];
-[SBNCNotificationDispatcher bannerDestination];
-[SBNCNotificationDispatcher setNotificationSource:];
-[SBNCNotificationDispatcher unlockWithRequest:completion:];
-[SBNCNotificationDispatcher applicationController];
-[SBNCNotificationDispatcher coverSheetViewController:didChangeActiveBehavior:];
-[SBNCNotificationDispatcher setDispatcher:];
-[SBNCNotificationDispatcher isNotificationContentExtensionVisible:];
-[SBNCNotificationDispatcher windowSceneDidDisconnect:];
-[SBNCNotificationDispatcher setApplicationController:];
-[SBNCNotificationDispatcher dashBoardDestination];
-[SBNCNotificationDispatcher initWithWindowSceneManager:backlightCoordinator:lockScreenCoordinator:applicationController:];
-[SBNCNotificationDispatcher _setupNewDestinationsForDispatcher:];
-[SBNCNotificationDispatcher unlockedBannerAlertSource];
-[SBNCNotificationDispatcher _updateActiveDestinations];
-[SBNCNotificationDispatcher notificationCenterDestination];
-[SBNCNotificationDispatcher setAlertingController:];
-[SBNCNotificationDispatcher alertingController];
-[SBNCNotificationDispatcher setWindowScenes:];
-[SBNCNotificationDispatcher windowSceneManager];
-[SBNCNotificationDispatcher userNotificationAlertSource];
-[SBNCNotificationDispatcher windowScenes];
-[SBNCNotificationDispatcher walletNotificationSource];
-[SBNCNotificationDispatcher _carPlayDestinationAvailabilityDidChange];
-[SBNCNotificationDispatcher setBacklightCoordinator:];
-[SBNCNotificationDispatcher setCarDestination:];
-[SBNCNotificationDispatcher _lockScreenWantsBanners];
-[SBNCNotificationDispatcher setWindowSceneManager:];
-[SBNCNotificationDispatcher notificationSource];
-[SBNCNotificationDispatcher isCarDestinationActive];
-[SBNCNotificationDispatcher setCommunicationPolicyManager:];
-[SBNCNotificationDispatcher setUnlockedBannerAlertSource:];
-[SBNCNotificationDispatcher communicationPolicyManager];
-[SBNCNotificationDispatcher windowSceneDidConnect:];
-[SBNCNotificationDispatcher _aggregateLockStateDidChange];
-[SBNCNotificationDispatcher backlightCoordinator];
-[SBNCNotificationDispatcher lockScreenCoordinator];
-[SBNCNotificationDispatcher setLockScreenCoordinator:];
-[SBNCNotificationDispatcher carOpenServiceEndpoint];
-[SBNCNotificationDispatcher setDispatcherDelegate:];
-[SBNCNotificationDispatcher keyWindowForScreen:];
-[SBNCNotificationDispatcher carDestination];
-[SBNCNotificationDispatcher dispatcherDelegate];
-[SBNCNotificationDispatcher setUserNotificationAlertSource:];
```

# `SBDashBoardApplicationInformer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSApplicationInforming`
- 4 instance variables, 5 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"SBSyncController" _syncController;
@"NSHashTable" _observers;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDashBoardApplicationInformer _installedApplicationsDidChange:];
-[SBDashBoardApplicationInformer dealloc];
-[SBDashBoardApplicationInformer _isBundleIdentifierBlockedForCommunicationPolicy:];
-[SBDashBoardApplicationInformer windowScene];
-[SBDashBoardApplicationInformer addApplicationInformationObserver:];
-[SBDashBoardApplicationInformer applicationExistsForBundleIdentifier:];
-[SBDashBoardApplicationInformer isBundleIdentifierBlockedForScreenTimeExpiration:];
-[SBDashBoardApplicationInformer isBundleIdentifierClock:];
-[SBDashBoardApplicationInformer isBundleIdentifierUserVisible:];
-[SBDashBoardApplicationInformer isInstallingApplicationWithBundleIdentifier:];
-[SBDashBoardApplicationInformer isSystemRestoringFromBackup];
-[SBDashBoardApplicationInformer removeApplicationInformationObserver:];
-[SBDashBoardApplicationInformer shouldScreenTimeSuppressNotificationsForBundleIdentifier:];
-[SBDashBoardApplicationInformer _screenTimeNotificationPolicyDidChange:];
-[SBDashBoardApplicationInformer initWithWindowScene:syncController:applicationController:];
-[SBDashBoardApplicationInformer isBundleIdentifierWallet:];
```

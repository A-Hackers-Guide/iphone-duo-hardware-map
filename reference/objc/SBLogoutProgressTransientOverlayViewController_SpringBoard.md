# `SBLogoutProgressTransientOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransientOverlayViewController`
- Protocols: `CSExternalBehaviorProviding`
- 8 instance variables, 13 properties, 36 instance methods, 0 class methods

## Instance variables

```
@"SBLogoutDebugBlockingViewController" _debugTasksViewController;
@"SBMultiUserDefaults" _multiUserDefaults;
@"SBPlatformController" _platformController;
@"SBLogoutProgressView" _progressView;
@"MTMaterialView" _overlayMaterialView;
@"<SBLogoutProgressDataSource>" _dataSource;
@"UMUser" _user;
@"<SBLogoutProgressDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBLogoutProgressDataSource>",W,N,V_dataSource) dataSource;
@property (T@"<SBLogoutProgressDelegate>",W,N,V_delegate) delegate;
@property (T@"UMUser",R,N,V_user) user;
@property (Tq,R,N) scrollingStrategy;
@property (Tq,R,N) notificationBehavior;
@property (TQ,R,N) restrictedCapabilities;
@property (Tq,R,N) proximityDetectionMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
```

## Instance methods

```
-[SBLogoutProgressTransientOverlayViewController _updateLegibility];
-[SBLogoutProgressTransientOverlayViewController conformsToCSBehaviorProviding];
-[SBLogoutProgressTransientOverlayViewController newTransientOverlayPresentationTransitionCoordinator];
-[SBLogoutProgressTransientOverlayViewController setContainerOrientation:];
-[SBLogoutProgressTransientOverlayViewController idleTimerDuration];
-[SBLogoutProgressTransientOverlayViewController newTransientOverlayDismissalTransitionCoordinator];
-[SBLogoutProgressTransientOverlayViewController proximityDetectionMode];
-[SBLogoutProgressTransientOverlayViewController viewDidLoad];
-[SBLogoutProgressTransientOverlayViewController setDataSource:];
-[SBLogoutProgressTransientOverlayViewController _legibilitySettings];
-[SBLogoutProgressTransientOverlayViewController viewDidLayoutSubviews];
-[SBLogoutProgressTransientOverlayViewController viewWillAppear:];
-[SBLogoutProgressTransientOverlayViewController shouldDisableControlCenter];
-[SBLogoutProgressTransientOverlayViewController _canShowWhileLocked];
-[SBLogoutProgressTransientOverlayViewController setDelegate:];
-[SBLogoutProgressTransientOverlayViewController dataSource];
-[SBLogoutProgressTransientOverlayViewController isContentOpaque];
-[SBLogoutProgressTransientOverlayViewController user];
-[SBLogoutProgressTransientOverlayViewController scrollingStrategy];
-[SBLogoutProgressTransientOverlayViewController notificationBehavior];
-[SBLogoutProgressTransientOverlayViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBLogoutProgressTransientOverlayViewController refreshData];
-[SBLogoutProgressTransientOverlayViewController delegate];
-[SBLogoutProgressTransientOverlayViewController viewDidDisappear:];
-[SBLogoutProgressTransientOverlayViewController conformsToCSExternalBehaviorProviding];
-[SBLogoutProgressTransientOverlayViewController idleTimerMode];
-[SBLogoutProgressTransientOverlayViewController coverSheetIdentifier];
-[SBLogoutProgressTransientOverlayViewController preferredStatusBarStyle];
-[SBLogoutProgressTransientOverlayViewController idleWarnMode];
-[SBLogoutProgressTransientOverlayViewController participantState];
-[SBLogoutProgressTransientOverlayViewController restrictedCapabilities];
-[SBLogoutProgressTransientOverlayViewController _updateData];
-[SBLogoutProgressTransientOverlayViewController _supportsDebugUI];
-[SBLogoutProgressTransientOverlayViewController _updateDebugTasksViewControllerSizeFromSize:];
-[SBLogoutProgressTransientOverlayViewController initWithUserAccount:];
-[SBLogoutProgressTransientOverlayViewController prepareForRestart];
```

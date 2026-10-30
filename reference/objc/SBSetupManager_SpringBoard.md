# `SBSetupManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBAppInteractionEventSourceObserving`, `SBFloatingDockControllerObserver`
- 12 instance variables, 11 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"<SBAppInteractionEventSourceProviding>" _appInteractionEventSourceProvider;
@"<SBFAuthenticationStatusProvider>" _authenticationStatusProvider;
@"SBApplicationController" _appController;
@"SBLockdownManager" _lockdownManager;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"SBUserSessionController" _userSessionController;
Q _setupRequiredReason;
B _inSetupModeReadyToExit;
B _setupWantedForDeviceMigration;
@"<BSInvalidatable>" _deferOrientationUpdatesAssertion;
@"NSHashTable" _floatingDockControllers;
@"NSMapTable" _floatingDockBehaviorAssertionsByFloatingDockController;
```

## Properties

```
@property (T@"NSHashTable",R,N,V_floatingDockControllers) floatingDockControllers;
@property (T@"NSMapTable",R,N,V_floatingDockBehaviorAssertionsByFloatingDockController) floatingDockBehaviorAssertionsByFloatingDockController;
@property (TB,N,GisInSetupModeReadyToExit,V_inSetupModeReadyToExit) inSetupModeReadyToExit;
@property (TB,R,N,GisInSetupMode) inSetupMode;
@property (TB,N,GisDeferringDeviceOrientationUpdates) deferringDeviceOrientationUpdates;
@property (TB,R,N,GisInSetupModeForDeviceMigration) inSetupModeForDeviceMigration;
@property (TB,R,N) shouldShowGreetingOnCoverSheet;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSetupManager dealloc];
-[SBSetupManager floatingDockControllerDidRegister:];
-[SBSetupManager _isInSetupMode];
-[SBSetupManager isInSetupMode];
-[SBSetupManager isInSetupModeForDeviceMigration];
-[SBSetupManager _invalidateFloatingDockBehaviorAssertions];
-[SBSetupManager _setSetupRequiredReason:];
-[SBSetupManager _setupProcessChangedNotificationReceived:];
-[SBSetupManager _takeFloatingDockBehaviorAssertionForFloatingDockController:];
-[SBSetupManager _takeFloatingDockBehaviorAssertions];
-[SBSetupManager _toggleSetupForMigrationNeeded:forReason:];
-[SBSetupManager eventSource:didBeginTransitionToMode:withLayoutState:activatingElement:triggeredBy:];
-[SBSetupManager floatingDockBehaviorAssertionsByFloatingDockController];
-[SBSetupManager floatingDockControllers];
-[SBSetupManager initWithApplicationController:appInteractionEventSourceProvider:authenticationStatusProvider:lockdownManager:lockScreenCoordinator:userSessionController:];
-[SBSetupManager isDeferringDeviceOrientationUpdates];
-[SBSetupManager isInSetupModeReadyToExit];
-[SBSetupManager noteAuthenticationSucceededWithPasscode:];
-[SBSetupManager postLaunchCompleteNotificationForSetup];
-[SBSetupManager setDeferringDeviceOrientationUpdates:];
-[SBSetupManager setInSetupModeReadyToExit:];
-[SBSetupManager setupHasFinishedRestoringFromBackup];
-[SBSetupManager shouldShowGreetingOnCoverSheet];
-[SBSetupManager updateInSetupMode];
```

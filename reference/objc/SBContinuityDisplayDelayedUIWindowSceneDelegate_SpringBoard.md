# `SBContinuityDisplayDelayedUIWindowSceneDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractWindowSceneDelegate`
- Protocols: `SBContinuitySessionOrientationDelegate`, `SBContinuitySessionStateObserver`, `SBTraitsContinuityDisplayPipelineManagerOrientationDelegate`, `SBContinuitySessionSceneDelegate`
- 19 instance variables, 5 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"SBTraitsWindowParticipantDelegate" _traitsWindowParticipantsDelegate;
@"SBTraitsContinuityDisplayPipelineManager" _traitsDisplayPipelineManager;
@"SBExternalDisplayWallpaperController" _wallpaperController;
@"SBHomeScreenController" _homeScreenController;
@"SBWindowSceneStatusBarSettingsAssertion" _showStatusBarAssertion;
@"<BSDefaultObserver>" _displayModeSettingsToken;
@"<BSInvalidatable>" _eventRoutingAssertion;
@"NSObject<OS_os_transaction>" _increasedMemoryLimitsTransaction;
B _initializedUI;
@"SBWindowScene" _connectingScene;
@"UISceneSession" _connectingSceneSession;
@"UISceneConnectionOptions" _connectingSceneConnectionOptions;
@"SBContinuitySession" _continuitySession;
@"<BSInvalidatable>" _continuitySessionManagerRegistration;
@"<BSInvalidatable>" _disableDynamicLightingAssertion;
@"<BSInvalidatable>" _systemEdgeGesturesIgnoreHIDEdgeFlagsAssertion;
@"SBApplicationController" _applicationController;
@"SBWindowSceneStatusBarManager" _statusBarManager;
@"UIWindow" _roiWindow;
```

## Properties

```
@property (T@"SBContinuitySession",R,N) connectedSession;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBContinuityDisplayDelayedUIWindowSceneDelegate _individuallyManagedRoles];
```

## Instance methods

```
-[SBContinuityDisplayDelayedUIWindowSceneDelegate _traitsDelegateForWindowRole:];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate sceneDidDisconnect:];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate init];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate _configureForConnectingWindowScene:windowSceneContext:];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate _shouldManageParticipantWithRole:];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate _windowSceneShouldResizeWindowsForScreenBoundsChange:];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate _displayLayoutPublisherForConnectingWindowScene:];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate scene:willConnectToSession:options:];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate _createTraitsPipelineManagerForWindowScene:];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate sceneWillEnterForeground:];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate _initializeUIIfNecessaryForReason:];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate _tearDownUIAndInvalidateIfNecessaryForReason:];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate conformsToContinuitySessionSceneDelegate];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate connectedSession];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate continuitySession:didUpdateHostedInterfaceOrientation:];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate continuitySessionDidUpdateState:];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate didConnectToSession:];
-[SBContinuityDisplayDelayedUIWindowSceneDelegate setInterfaceOrientation:supportedInterfaceOrientations:];
```

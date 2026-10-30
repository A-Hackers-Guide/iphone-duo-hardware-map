# `SBExternalDisplayWindowSceneDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractWindowSceneDelegate`
- Protocols: `SBBacklightControllerObserver`
- 13 instance variables, 4 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"SBTraitsWindowParticipantDelegate" _traitsWindowParticipantsDelegate;
@"SBApplicationController" _applicationController;
@"SBTraitsExternalDisplayPipelineManager" _traitsExternalPipelineManager;
@"SBExtendedDisplayController" _extendedDisplayController;
@"SBExternalDisplayWallpaperController" _wallpaperController;
@"SBExternalDisplayCoverSheetController" _coverSheetController;
@"SBHomeScreenController" _homeScreenController;
@"SBWindowSceneStatusBarSettingsAssertion" _showStatusBarAssertion;
@"<BSDefaultObserver>" _displayModeSettingsToken;
@"<BSInvalidatable>" _eventRoutingAssertion;
@"NSObject<OS_os_transaction>" _increasedMemoryLimitsTransaction;
@"<FBSDisplayLayoutPublishing>" _displayLayoutPublisher;
@"SBWindowSceneStatusBarManager" _statusBarManager;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBExternalDisplayWindowSceneDelegate _individuallyManagedRoles];
```

## Instance methods

```
-[SBExternalDisplayWindowSceneDelegate _traitsDelegateForWindowRole:];
-[SBExternalDisplayWindowSceneDelegate sceneDidDisconnect:];
-[SBExternalDisplayWindowSceneDelegate init];
-[SBExternalDisplayWindowSceneDelegate _configureForConnectingWindowScene:windowSceneContext:];
-[SBExternalDisplayWindowSceneDelegate _shouldManageParticipantWithRole:];
-[SBExternalDisplayWindowSceneDelegate _displayLayoutPublisherForConnectingWindowScene:];
-[SBExternalDisplayWindowSceneDelegate scene:willConnectToSession:options:];
-[SBExternalDisplayWindowSceneDelegate _createTraitsPipelineManagerForWindowScene:];
```

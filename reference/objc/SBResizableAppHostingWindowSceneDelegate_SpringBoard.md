# `SBResizableAppHostingWindowSceneDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractWindowSceneDelegate`
- Protocols: `SBAppResizingCoordinatorObserver`
- 9 instance variables, 4 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"SBTraitsWindowParticipantDelegate" _traitsWindowParticipantsDelegate;
@"SBTraitsPipelineManager" _traitsPipelineManager;
@"FBSDisplayLayoutPublisher" _displayLayoutPublisher;
@"SBWindowScene" _windowScene;
@"SBWindowSceneContext" _windowSceneContext;
@"SBAppResizingCoordinator" _appResizingCoordinator;
@"SBAppResizingService" _resizingService;
@"UIWindow" _roiWindow;
@"NSMutableDictionary" _windowSceneIdentifiersToShieldWindows;
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
+[SBResizableAppHostingWindowSceneDelegate _individuallyManagedRoles];
```

## Instance methods

```
-[SBResizableAppHostingWindowSceneDelegate _traitsDelegateForWindowRole:];
-[SBResizableAppHostingWindowSceneDelegate sceneDidDisconnect:];
-[SBResizableAppHostingWindowSceneDelegate init];
-[SBResizableAppHostingWindowSceneDelegate _configureForConnectingWindowScene:windowSceneContext:];
-[SBResizableAppHostingWindowSceneDelegate _shouldManageParticipantWithRole:];
-[SBResizableAppHostingWindowSceneDelegate _displayLayoutPublisherForConnectingWindowScene:];
-[SBResizableAppHostingWindowSceneDelegate _createTraitsPipelineManagerForWindowScene:];
-[SBResizableAppHostingWindowSceneDelegate _createShieldWindowForWindowScene:];
-[SBResizableAppHostingWindowSceneDelegate _removeShieldWindowForWindowScene:];
-[SBResizableAppHostingWindowSceneDelegate _uiSceneConnected:];
-[SBResizableAppHostingWindowSceneDelegate _uiSceneDisconnected:];
-[SBResizableAppHostingWindowSceneDelegate resizingCoordinator:didUpdateActiveSession:];
```

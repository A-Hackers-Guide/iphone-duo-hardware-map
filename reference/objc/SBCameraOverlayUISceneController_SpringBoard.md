# `SBCameraOverlayUISceneController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSystemUISceneController`
- Protocols: `SBCameraViewfinderMonitorObserver`, `SBPhysicalButtonSceneOverrideObserver`, `SBFZStackParticipantDelegate`
- 9 instance variables, 4 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"SBSingleSceneController" _sceneController;
@"SBPhysicalButtonSceneOverrideManager" _physicalButtonOverrideManager;
@"<BSInvalidatable>" _physicalButtonOverrideObserver;
@"_SBCameraOverlayRequest" _activeOverlayRequester;
@"SBSUIFeaturePolicyHostComponent" _featurePolicyComponent;
@"SBCameraViewfinderMonitor" _viewfinderMonitor;
@"<SBCameraViewfinderMonitoring>" _viewfinderObsserver;
@"NSMapTable" _zStackParticipantsByWindowScene;
@"NSMapTable" _zStackPhysicalButtonPolicyAssistantsByWindowScene;
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
+[SBCameraOverlayUISceneController _setupInfo];
```

## Instance methods

```
-[SBCameraOverlayUISceneController _updateForegroundScenes];
-[SBCameraOverlayUISceneController destroyScenesWithPersistentIdentifiers:processIdentity:completion:];
-[SBCameraOverlayUISceneController initWithSceneWorkspaceIdentifier:clientProcessIdentity:sceneVendingPolicy:traitsRole:jobLabel:level:];
-[SBCameraOverlayUISceneController zStackParticipant:updatePreferences:];
-[SBCameraOverlayUISceneController cameraViewfinderMonitorSessionDidBegin:auditToken:];
-[SBCameraOverlayUISceneController windowSceneDidDisconnect:];
-[SBCameraOverlayUISceneController cameraViewfinderMonitorSessionDidEnd:auditToken:];
-[SBCameraOverlayUISceneController dealloc];
-[SBCameraOverlayUISceneController physicalButtonSceneOverridesDidChange:];
-[SBCameraOverlayUISceneController scenePresenter:willDismissScene:];
-[SBCameraOverlayUISceneController zStackParticipantDidChange:];
-[SBCameraOverlayUISceneController _reevaluteCameraOverlaySessionRequestForReason:];
-[SBCameraOverlayUISceneController _setActiveOverlayRequest:];
-[SBCameraOverlayUISceneController scenePresenter:didPresentScene:];
-[SBCameraOverlayUISceneController _reasonToDropCameraOverlaySessionRequest];
-[SBCameraOverlayUISceneController _activeWindowScene];
-[SBCameraOverlayUISceneController _isDefaultPresenterDelegate];
-[SBCameraOverlayUISceneController _activateSession:];
-[SBCameraOverlayUISceneController _activeOverlayRequest];
-[SBCameraOverlayUISceneController windowSceneDidConnect:];
-[SBCameraOverlayUISceneController _updateActiveOverlayRequestSceneSettingsOnOverlayScene];
-[SBCameraOverlayUISceneController cameraViewfinderMonitorSessionWillBegin:auditToken:];
```

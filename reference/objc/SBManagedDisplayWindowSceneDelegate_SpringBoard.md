# `SBManagedDisplayWindowSceneDelegate`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBAbstractWindowSceneDelegate`
- 13 instance variables, 0 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"SBTraitsWindowParticipantDelegate" _traitsWindowParticipantsDelegate;
@"SBApplicationController" _applicationController;
@"SBTraitsEmbeddedDisplayPipelineManager" _traitsEmbeddedPipelineManager;
@"SBRecordingIndicatorDisplayPowerManager" _indicatorDisplayPowerManager;
@"SBManagedDisplayController" _managedDisplayController;
@"SBProductivityGestureController" _productivityGestureController;
@"SBCaptureButtonDispatchingDeferrer" _captureButtonDispatchingDeferrer;
@"SBWidgetExtensionDebuggingController" _widgetDebuggingController;
@"FBSDisplayLayoutPublisher" _displayLayoutPublisher;
@"<BSInvalidatable>" _systemEdgeGesturesIgnoreHIDEdgeFlagsAssertion;
@"SBWindowSceneStatusBarSettingsAssertion" _showStatusBarAssertion;
@"SBBacklightDimTouchSuppressor" _backlightDimTouchSuppressor;
@? _startupCompletionAfterAllEmbeddedScenesConnectBlock;
```

## Class methods

```
+[SBManagedDisplayWindowSceneDelegate _individuallyManagedRoles];
+[SBManagedDisplayWindowSceneDelegate _windowWillBecomeHiddenExemptRoles];
```

## Instance methods

```
-[SBManagedDisplayWindowSceneDelegate completeStartupAfterAllEmbeddedScenesConnect];
-[SBManagedDisplayWindowSceneDelegate _traitsDelegateForWindowRole:];
-[SBManagedDisplayWindowSceneDelegate sceneDidDisconnect:];
-[SBManagedDisplayWindowSceneDelegate init];
-[SBManagedDisplayWindowSceneDelegate _configureForConnectingWindowScene:windowSceneContext:];
-[SBManagedDisplayWindowSceneDelegate _shouldManageParticipantWithRole:];
-[SBManagedDisplayWindowSceneDelegate _shouldHandleWindowWillBecomeHiddenForRole:];
-[SBManagedDisplayWindowSceneDelegate _displayLayoutPublisherForConnectingWindowScene:];
-[SBManagedDisplayWindowSceneDelegate scene:willConnectToSession:options:];
-[SBManagedDisplayWindowSceneDelegate _createTraitsPipelineManagerForWindowScene:];
-[SBManagedDisplayWindowSceneDelegate initializeProductivityGestureControllerIfNecessary];
```

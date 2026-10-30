# `SBCameraHardwareButton`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHIDButtonStateDelegate`, `PTSettingsKeyObserver`, `SBSceneManagerObserver`, `SBPhysicalButtonSceneOverrideObserver`, `SBHardwareButtonColluding`
- 30 instance variables, 6 properties, 37 instance methods, 0 class methods

## Instance variables

```
B _disableDeferringToApplications;
B _shouldUsePocketStateDetection;
i _lastCameraApplicationPID;
@"SBHardwareButtonCoordinator" _hardwareButtonCoordinator;
@"<BSInvalidatable>" _dispatchingRuleAssertion;
@"<BSInvalidatable>" _deferringRuleAssertion;
@"<BSInvalidatable>" _physicalButtonOverrideObserver;
@"NSMutableIndexSet" _allCameraShutterButtonPIDs;
@"NSMutableIndexSet" _foregroundCameraShutterButtonPIDs;
@"NSMutableIndexSet" _foregroundPendingRemovalCameraShutterButtonPIDs;
@"BSMutableIntegerMap" _deferringTokensPerPID;
@"SBHIDButtonStateArbiter" _buttonArbiter;
@"RBSProcessMonitor" _processMonitor;
@"CMPocketStateManager" _pocketStateManager;
@"_SBCameraLaunchCondition" _shouldLaunchCameraCondition;
@"_SBCameraLaunchCondition" _longPressCondition;
@"_SBCameraLaunchCondition" _outOfPocketCondition;
@"BSAbsoluteMachTimer" _longPressCancellationTimer;
@"FBScene" _physicalButtonOverrideScene;
d _longPressCancellationTimeout;
@"BKSHIDEventDeliveryManager" _deliveryManager;
@"SBApplicationController" _applicationController;
@"SBCameraActivationManager" _activationManager;
@"SBLockScreenCoordinator" _lockScreenCoordinator;
@"SBBacklightCoordinator" _backlightCoordinator;
@"SBProximitySensorManager" _proximitySensorManager;
@"SBSceneManager" _sceneManager;
@"SBWindowSceneManager" _windowSceneManager;
@"SBCameraHardwareButtonSettings" _settings;
@"SBCameraHardwareButtonDefaults" _defaults;
```

## Properties

```
@property (TB,N,V_disableDeferringToApplications) disableDeferringToApplications;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBHardwareButtonCoordinator",&,N,V_hardwareButtonCoordinator) hardwareButtonCoordinator;
```

## Instance methods

```
-[SBCameraHardwareButton _deferCameraPressesToSpringBoard];
-[SBCameraHardwareButton _deferCameraPressesToPID:];
-[SBCameraHardwareButton sceneManager:didAddExternalForegroundApplicationSceneHandle:];
-[SBCameraHardwareButton setDisableDeferringToApplications:];
-[SBCameraHardwareButton _deferToForegroundApp];
-[SBCameraHardwareButton sceneManager:didRemoveExternalForegroundApplicationSceneHandle:];
-[SBCameraHardwareButton hardwareButtonIdentifier];
-[SBCameraHardwareButton _longPressDidCancel];
-[SBCameraHardwareButton dealloc];
-[SBCameraHardwareButton _process:stateDidUpdate:];
-[SBCameraHardwareButton physicalButtonSceneOverridesDidChange:];
-[SBCameraHardwareButton disableDeferringToApplications];
-[SBCameraHardwareButton cancelHardwareButtonPress];
-[SBCameraHardwareButton initWithActivationManager:applicationController:backlightCoordinator:lockScreenCoordinator:windowSceneManager:];
-[SBCameraHardwareButton settings:changedValueForKey:];
-[SBCameraHardwareButton performActionsForButtonUp:];
-[SBCameraHardwareButton _reconfigureProcessMonitorForPredicates:];
-[SBCameraHardwareButton _stopWaitingForLongPressCancellation];
-[SBCameraHardwareButton performActionsForButtonDown:];
-[SBCameraHardwareButton _deferToPhysicalOverrideScene];
-[SBCameraHardwareButton _updateCameraDeferringRule];
-[SBCameraHardwareButton removeProcessRequestingCameraButton:];
-[SBCameraHardwareButton _shouldDeferToNonSpringBoardProcess];
-[SBCameraHardwareButton _shouldDeferToCoverSheetCamera];
-[SBCameraHardwareButton _reconfigureProcessMonitor];
-[SBCameraHardwareButton _notifyCoreAnalyticsCameraDidLaunchToLockScreen:screenWasOff:];
-[SBCameraHardwareButton setHardwareButtonCoordinator:];
-[SBCameraHardwareButton performActionsForButtonLongPress:];
-[SBCameraHardwareButton _updateSettingsForReason:];
-[SBCameraHardwareButton _deferCameraPressesToCameraApplication];
-[SBCameraHardwareButton _deferCameraPressesToApplication:];
-[SBCameraHardwareButton hardwareButtonCoordinator];
-[SBCameraHardwareButton handleButtonEvent:];
-[SBCameraHardwareButton _isCoverSheetCameraVisible];
-[SBCameraHardwareButton _startWaitingForLongPressCancellation];
-[SBCameraHardwareButton _launchCameraIfReady];
-[SBCameraHardwareButton addProcessRequestingCameraButton:token:];
```

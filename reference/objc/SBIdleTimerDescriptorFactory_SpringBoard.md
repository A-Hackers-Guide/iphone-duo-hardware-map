# `SBIdleTimerDescriptorFactory`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 13 instance variables, 10 properties, 46 instance methods, 1 class methods

## Instance variables

```
@"SBIdleTimerGlobalStateMonitor" _stateMonitor;
@"SBPrototypeController" _override_prototypeController;
@"SBIdleTimerSettings" _override_idleTimerPrototypeSettings;
@"SBLockScreenCoordinator" _override_lockScreenCoordinator;
@"SBIdleTimerDefaults" _override_idleTimerDefaults;
@"SBMainWorkspace" _override_mainWorkspace;
@"SBUIBiometricResource" _override_biometricResource;
@"SBTelephonyManager" _override_telephonyManager;
@"SBConferenceManager" _override_conferenceManager;
q _override_effectiveHomeButtonType;
i _previousShouldUseAttentionSensorAccess;
@"SpringBoard" _springBoard;
@"SBAlertItemsController" _alertItemsController;
```

## Properties

```
@property (T@"SpringBoard",&,N,G_springBoard,S_setSpringBoard:,V_springBoard) springBoard;
@property (T@"SBAlertItemsController",&,N,G_alertItemsController,S_setAlertItemsController:,V_alertItemsController) alertItemsController;
@property (T@"SBPrototypeController",&,N,G_prototypeController,S_setPrototypeController:,V_override_prototypeController) prototypeController;
@property (T@"SBIdleTimerSettings",&,N,G_idleTimerPrototypeSettings,S_setIdleTimerPrototypeSettings:,V_override_idleTimerPrototypeSettings) idleTimerPrototypeSettings;
@property (T@"SBLockScreenCoordinator",&,N,G_lockScreenCoordinator,S_setLockScreenCoordinator:,V_override_lockScreenCoordinator) lockScreenCoordinator;
@property (T@"SBMainWorkspace",&,N,G_mainWorkspace,S_setMainWorkspace:,V_override_mainWorkspace) mainWorkspace;
@property (T@"SBUIBiometricResource",&,N,G_biometricResource,S_setBiometricResource:,V_override_biometricResource) biometricResource;
@property (T@"SBTelephonyManager",&,N,G_telephonyManager,S_setTelephonyManager:,V_override_telephonyManager) telephonyManager;
@property (T@"SBConferenceManager",&,N,G_conferenceManager,S_setConferenceManager:,V_override_conferenceManager) conferenceManager;
@property (Tq,N,G_effectiveHomeButtonType,S_setEffectiveHomeButtonType:) effectiveHomeButtonType;
```

## Class methods

```
+[SBIdleTimerDescriptorFactory disabledIdleTimerDescriptor];
```

## Instance methods

```
-[SBIdleTimerDescriptorFactory _telephonyManager];
-[SBIdleTimerDescriptorFactory _conferenceManager];
-[SBIdleTimerDescriptorFactory _setPrototypeController:];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForTelephony:];
-[SBIdleTimerDescriptorFactory _prototypeController];
-[SBIdleTimerDescriptorFactory _allowExtendedLiftToWakeTimer];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForActiveClientConfiguration:];
-[SBIdleTimerDescriptorFactory _lockScreenCoordinator];
-[SBIdleTimerDescriptorFactory sanitizeDescriptorForLockscreenDefaults:];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForPowerDefaults:];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForWarnInterval:];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForPrototypeSettingsDisable:];
-[SBIdleTimerDescriptorFactory _alertItemsController];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForBatterySaverMode:];
-[SBIdleTimerDescriptorFactory _biometricResource];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsWithCustomTimeouts:fromBehavior:];
-[SBIdleTimerDescriptorFactory _setEffectiveHomeButtonType:];
-[SBIdleTimerDescriptorFactory initWithGlobalStateMonitor:];
-[SBIdleTimerDescriptorFactory _setMainWorkspace:];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForAutoLockTimeout:];
-[SBIdleTimerDescriptorFactory sanitizeTotalDuration:];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForFaceDown:];
-[SBIdleTimerDescriptorFactory _setConferenceManager:];
-[SBIdleTimerDescriptorFactory _setSpringBoard:];
-[SBIdleTimerDescriptorFactory _effectiveHomeButtonType];
-[SBIdleTimerDescriptorFactory _isIdleDurationForever:];
-[SBIdleTimerDescriptorFactory _shouldUseAttentionSensor];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForPrototypeSettingsOverride:];
-[SBIdleTimerDescriptorFactory _setLockScreenCoordinator:];
-[SBIdleTimerDescriptorFactory _idleTimerPrototypeSettings];
-[SBIdleTimerDescriptorFactory idleTimerDescriptorForBehavior:];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForDuration:descriptor:];
-[SBIdleTimerDescriptorFactory _setTelephonyManager:];
-[SBIdleTimerDescriptorFactory _mainWorkspace];
-[SBIdleTimerDescriptorFactory sanitizeWarnInterval:];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForUnlockedWithMesa:];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForDefaultWarnInterval:];
-[SBIdleTimerDescriptorFactory _setIdleTimerPrototypeSettings:];
-[SBIdleTimerDescriptorFactory _springBoard];
-[SBIdleTimerDescriptorFactory sanitizeSettingsAfterSetup:duration:];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForThermalBlockedMode:];
-[SBIdleTimerDescriptorFactory sanitizeSettingsAfterInitialSetup:];
-[SBIdleTimerDescriptorFactory _setBiometricResource:];
-[SBIdleTimerDescriptorFactory _updateIdleTimerSettingsWarnInterval:totalInterval:];
-[SBIdleTimerDescriptorFactory updateIdleTimerSettingsForSecurityDefaults:];
-[SBIdleTimerDescriptorFactory _setAlertItemsController:];
```

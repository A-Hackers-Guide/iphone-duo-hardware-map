# `SBSystemServiceServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSServiceFacility`
- 8 instance variables, 8 properties, 96 instance methods, 1 class methods

## Instance variables

```
@"<SBSystemServiceServerAppSwitcherDelegate>" _appSwitcherDelegate;
@"<SBSystemServiceServerBiometricsDelegate>" _biometricsDelegate;
@"<SBSystemServiceServerHardwareButtonDelegate>" _hardwareButtonDelegate;
@"<SBSystemServiceServerSoftwareUpdateDelegate>" _softwareUpdateDelegate;
@"<SBSystemServiceServerTestAutomationDelegate>" _testAutomationDelegate;
@"<SBSystemServiceServerStateDumpDelegate>" _stateDumpDelegate;
@"<SBSystemServiceServerSystemApertureStateDumpDelegate>" _systemApertureStateDumpDelegate;
@"<SBSystemServiceServerMenuBarDelegate>" _menuBarDelegate;
```

## Properties

```
@property (T@"<SBSystemServiceServerAppSwitcherDelegate>",W,N,V_appSwitcherDelegate) appSwitcherDelegate;
@property (T@"<SBSystemServiceServerBiometricsDelegate>",W,N,V_biometricsDelegate) biometricsDelegate;
@property (T@"<SBSystemServiceServerHardwareButtonDelegate>",W,N,V_hardwareButtonDelegate) hardwareButtonDelegate;
@property (T@"<SBSystemServiceServerSoftwareUpdateDelegate>",W,N,V_softwareUpdateDelegate) softwareUpdateDelegate;
@property (T@"<SBSystemServiceServerTestAutomationDelegate>",W,N,V_testAutomationDelegate) testAutomationDelegate;
@property (T@"<SBSystemServiceServerStateDumpDelegate>",W,N,V_stateDumpDelegate) stateDumpDelegate;
@property (T@"<SBSystemServiceServerSystemApertureStateDumpDelegate>",W,N,V_systemApertureStateDumpDelegate) systemApertureStateDumpDelegate;
@property (T@"<SBSystemServiceServerMenuBarDelegate>",W,N,V_menuBarDelegate) menuBarDelegate;
```

## Class methods

```
+[SBSystemServiceServer sharedInstance];
```

## Instance methods

```
-[SBSystemServiceServer dealloc];
-[SBSystemServiceServer _init];
-[SBSystemServiceServer testAutomationDelegate];
-[SBSystemServiceServer noteClientDidDisconnect:];
-[SBSystemServiceServer noteDidReceiveMessage:withType:fromClient:];
-[SBSystemServiceServer menuBarDelegate];
-[SBSystemServiceServer systemApertureStateDumpDelegate];
-[SBSystemServiceServer _handleBiometricsFetchUnlockCredentialSetMessage:fromClient:];
-[SBSystemServiceServer _handleHardwareButtonAcquireAssertionMessage:fromClient:];
-[SBSystemServiceServer _handleHardwareButtonGetHapticType:fromClient:];
-[SBSystemServiceServer _handleHardwareButtonGetHintViewsSupported:fromClient:];
-[SBSystemServiceServer _handleHardwareButtonGetToggleButtonState:fromClient:];
-[SBSystemServiceServer _handleHardwareButtonRegisterAssociatedHintView:fromClient:];
-[SBSystemServiceServer _handleHardwareButtonRequestSystemGlowEffect:fromClient:];
-[SBSystemServiceServer _handleHardwareButtonSetHapticType:fromClient:];
-[SBSystemServiceServer _handleHardwareButtonSetPressEventMask:fromClient:];
-[SBSystemServiceServer _handleHardwareButtonSetRequestsHIDEvents:fromClient:];
-[SBSystemServiceServer _handleHardwareButtonUpdateHintContentVisibility:fromClient:];
-[SBSystemServiceServer _handleHardwareButtonUpdateSystemGlowStyle:fromClient:];
-[SBSystemServiceServer _handleLoadStashedSwitcherModelFromPath:fromClient:];
-[SBSystemServiceServer _handleMenuBarServiceClientMessageTypeQuerySupported:fromClient:];
-[SBSystemServiceServer _handleMenuBarServiceClientMessageTypeToggleVisibility:fromClient:];
-[SBSystemServiceServer _handleRequestAppSwitcherAppearanceForHiddenApp:fromClient:];
-[SBSystemServiceServer _handleRequestAppSwitcherResetLayoutAttributes:fromClient:];
-[SBSystemServiceServer _handleRequestAppSwitcherUpdateWindowingMode:fromClient:];
-[SBSystemServiceServer _handleSoftwareUpdateGetPasscodePolicy:fromClient:];
-[SBSystemServiceServer _handleSoftwareUpdateSetPasscodePolicy:fromClient:];
-[SBSystemServiceServer _handleStashSwitcherModelToPath:fromClient:];
-[SBSystemServiceServer _handleStateDumpServiceAvailableDomains:fromClient:];
-[SBSystemServiceServer _handleStateDumpServiceClientMessageTypeDisableRemoteStateDump:fromClient:];
-[SBSystemServiceServer _handleStateDumpServiceClientMessageTypeDisableRemoteStreaming:fromClient:];
-[SBSystemServiceServer _handleStateDumpServiceClientMessageTypeEnableRemoteStateDump:fromClient:];
-[SBSystemServiceServer _handleStateDumpServiceClientMessageTypeEnableRemoteStreaming:fromClient:];
-[SBSystemServiceServer _handleStateDumpServiceClientMessageTypeStateDump:fromClient:];
-[SBSystemServiceServer _handleStateDumpServiceClientMessageTypeStateDumpToFile:fromClient:];
-[SBSystemServiceServer _handleStateDumpServiceLastNEntries:fromClient:];
-[SBSystemServiceServer _handleStateDumpServiceStartWritingForDomain:fromClient:];
-[SBSystemServiceServer _handleSystemApertureRequestStateDump:fromClient:];
-[SBSystemServiceServer _handleSystemApertureRequestToWriteStateDumpToFile:fromClient:];
-[SBSystemServiceServer _handleTestAutomationAddSpecificWidgetStackToPageWithSize:fromClient:];
-[SBSystemServiceServer _handleTestAutomationAddSpecificWidgetToPageWithSize:fromClient:];
-[SBSystemServiceServer _handleTestAutomationAddWidgetsToEachPage:fromClient:];
-[SBSystemServiceServer _handleTestAutomationBlockApplicationForScreenTime:fromClient:];
-[SBSystemServiceServer _handleTestAutomationClearAllUserNotifications:fromClient:];
-[SBSystemServiceServer _handleTestAutomationEnterLostMode:fromClient:];
-[SBSystemServiceServer _handleTestAutomationExitLostMode:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetActiveDisplayWindowSceneDisplayIdentifier:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetButterflySplitViewStronglyPaired:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetChamoisPrefersDockHidden:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetChamoisPrefersStripHidden:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetChamoisWindowingUIEnabled:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetDeviceOrientation:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetDeviceOrientationForSystemSpaceOrientation:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetDevicePose:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetDeviceSupportsSystemAperture:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetScencesForBundleIdentifier:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetSpringBoardFrameRecording:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetSystemApertureModelStateDump:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetSystemApertureStateDump:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetSystemSpaceOrientationForDeviceOrientation:fromClient:];
-[SBSystemServiceServer _handleTestAutomationGetWidgetControllerStateDump:fromClient:];
-[SBSystemServiceServer _handleTestAutomationRequestHUDHiddenAssertion:fromClient:];
-[SBSystemServiceServer _handleTestAutomationRequestReachabilityEnabledAssertion:fromClient:];
-[SBSystemServiceServer _handleTestAutomationResetToHomeScreen:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetAccessoryAttachedState:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetAlertState:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetAmbientPresentationState:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetChamoisPrefersDockHidden:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetChamoisPrefersStripHidden:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetChamoisWindowingUIEnabled:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetDeviceOrientation:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetDevicePoseOverride:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetHiddenFeatureState:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetIdleTimerState:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetMallocStackLoggingState:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetOrientationLockState:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetReachabilityActiveState:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetSpringBoardAnimationFrameRecording:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetSystemApertureUnderAutomationTesting:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetTestRunnerRecoveryApplicationBundleIdentifier:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSetUserPresenceDetectedSinceWake:fromClient:];
-[SBSystemServiceServer _handleTestAutomationSuspendAllDisplays:fromClient:];
-[SBSystemServiceServer _handleTestAutomationTogglePictureInPictureProminence:fromClient:];
-[SBSystemServiceServer appSwitcherDelegate];
-[SBSystemServiceServer biometricsDelegate];
-[SBSystemServiceServer hardwareButtonDelegate];
-[SBSystemServiceServer setAppSwitcherDelegate:];
-[SBSystemServiceServer setBiometricsDelegate:];
-[SBSystemServiceServer setHardwareButtonDelegate:];
-[SBSystemServiceServer setMenuBarDelegate:];
-[SBSystemServiceServer setSoftwareUpdateDelegate:];
-[SBSystemServiceServer setStateDumpDelegate:];
-[SBSystemServiceServer setSystemApertureStateDumpDelegate:];
-[SBSystemServiceServer setTestAutomationDelegate:];
-[SBSystemServiceServer softwareUpdateDelegate];
-[SBSystemServiceServer stateDumpDelegate];
```

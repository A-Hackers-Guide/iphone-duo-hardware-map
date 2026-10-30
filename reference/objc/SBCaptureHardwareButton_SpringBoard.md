# `SBCaptureHardwareButton`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBHIDButtonStateDelegate`, `SBPhysicalButtonSceneOverrideObserver`, `SBFZStackParticipantObserver`, `PTSettingsKeyObserver`, `SBDisplayContentModeTransitionObserver`, `SBHardwareButtonColluding`, `SBCaptureButtonScanningModeResource`
- 38 instance variables, 5 properties, 46 instance methods, 0 class methods

## Instance variables

```
@"BSCompoundAssertion" _buttonScanningActiveAssertion;
@"<BSInvalidatable>" _underlyingButtonPowerAssertion;
@"<BSInvalidatable>" _clientRequestedButtonPowerAssertion;
@"<BSInvalidatable>" _launchGracePeriodButtonPowerAssertion;
@"NSArray" _buttonEventRequestingScenes;
@"NSArray" _physicalButtonSceneTargets;
@"NSArray" _foregroundCaptureSceneTargets;
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@"SBFZStackResolver" _observedZStackResolver;
@"SBWindowScene" _mainWindowScene;
@"SBWindowScene" _windowScene;
@"SBPhysicalButtonSceneOverrideManager" _physicalButtonOverrideManager;
@"<BSInvalidatable>" _physicalButtonOverrideObserver;
@"SBCameraActivationManager" _activationManager;
@"SBCaptureButtonSuppressionManager" _suppressionManager;
@"SBCaptureButtonAppConfigurationCoordinator" _configurationCoordinator;
@"NSMutableDictionary" _appActivatorsBySceneIdentifier;
@"SBCaptureButtonRestrictionCoordinator" _restrictionCoordinator;
@"SBCaptureHardwareButtonFullPressRecognizer" _captureButtonRecognizer;
@"SBCaptureButtonSettings" _settings;
@"<BSInvalidatable>" _buttonActiveAssertion;
@"<SBPhysicalButtonCompletionHandling>" _overrideButtonUpHandler;
@"SBSetupManager" _setupManager;
@"SBFUserAuthenticationController" _authenticationController;
@"<SBHUDControlling>" _hudController;
Q _bufferedPressAbsoluteTimestamp;
@"NSString" _captureAppBundleIdentifierForBufferedPress;
@"BSAbsoluteMachTimer" _longPressTimer;
@"BSAbsoluteMachTimer" _nextClickDownTimer;
q _clickCountToActivateApp;
q _remainingClicksDownToActivateApp;
q _remainingClicksUpToActivateApp;
@"<BSInvalidatable>" _hintDropletAssertion;
@"NSMutableSet" _ignoreButtonUpReasons;
@"NSUserDefaults" _cameraDefaults;
d _lastActivationTime;
@"SBHardwareButtonCoordinator" _hardwareButtonCoordinator;
@"SBHIDButtonStateArbiter" _simulationButtonArbiter;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBHardwareButtonCoordinator",&,N,V_hardwareButtonCoordinator) hardwareButtonCoordinator;
```

## Instance methods

```
-[SBCaptureHardwareButton zStackParticipantWithIdentifier:settingsDidChange:];
-[SBCaptureHardwareButton _processZStackParticipantSettings:];
-[SBCaptureHardwareButton zStackParticipantWithIdentifier:wasAcquiredWithSettings:];
-[SBCaptureHardwareButton displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBCaptureHardwareButton hardwareButtonIdentifier];
-[SBCaptureHardwareButton dealloc];
-[SBCaptureHardwareButton displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBCaptureHardwareButton physicalButtonSceneOverridesDidChange:];
-[SBCaptureHardwareButton cancelHardwareButtonPress];
-[SBCaptureHardwareButton settings:changedValueForKey:];
-[SBCaptureHardwareButton performActionsForButtonUp:];
-[SBCaptureHardwareButton performActionsForButtonDown:];
-[SBCaptureHardwareButton setHardwareButtonCoordinator:];
-[SBCaptureHardwareButton performActionsForButtonLongPress:];
-[SBCaptureHardwareButton hardwareButtonCoordinator];
-[SBCaptureHardwareButton _configureForWindowScene:];
-[SBCaptureHardwareButton _waitingForCaptureAppActivation];
-[SBCaptureHardwareButton _appActivator];
-[SBCaptureHardwareButton _attemptButtonActivationWithClickCountToActivate:atTimestamp:forDownTimestamp:isAccessibilityEvent:];
-[SBCaptureHardwareButton _bufferPressForBundleIdentifier:timestamp:];
-[SBCaptureHardwareButton _captureButtonGestureRecognizerAction:];
-[SBCaptureHardwareButton _captureButtonWindowScene];
-[SBCaptureHardwareButton _clickGesture];
-[SBCaptureHardwareButton _configureButtonProcessor];
-[SBCaptureHardwareButton _doubleClickInterval];
-[SBCaptureHardwareButton _ensureAppActivatorForWindowScene:];
-[SBCaptureHardwareButton _handleButtonDownAtTimestamp:isAccessibilityEvent:];
-[SBCaptureHardwareButton _handleButtonUpAtTimestamp:forDownTimestamp:isAccessibilityEvent:];
-[SBCaptureHardwareButton _handleLongPressAtTimestamp:forDownTimestamp:];
-[SBCaptureHardwareButton _ignoreNextButtonUpForReason:];
-[SBCaptureHardwareButton _invalidateBufferedPress];
-[SBCaptureHardwareButton _isVisionIntelligenceSupported];
-[SBCaptureHardwareButton _mitigateAccidentalDisplaySwapLaunchOnWindowScene:];
-[SBCaptureHardwareButton _nextClickTimeoutDidFire];
-[SBCaptureHardwareButton _physicalButtonTargetMatchesExpectedTargetScene];
-[SBCaptureHardwareButton _postBufferedPress];
-[SBCaptureHardwareButton _reevaluateButtonScanState];
-[SBCaptureHardwareButton _resetNextClickTimer];
-[SBCaptureHardwareButton _sendCameraCaptureButtonDownToSceneOverride];
-[SBCaptureHardwareButton _sendCaptureIntentToEligibleForegroundScene];
-[SBCaptureHardwareButton _shouldContinueAfterProcessingStateForClickDown];
-[SBCaptureHardwareButton _stopIgnoringNextButtonUp];
-[SBCaptureHardwareButton captureButtonAppActivatorLaunchDidComplete:];
-[SBCaptureHardwareButton requestActiveScanningModeForReason:];
-[SBCaptureHardwareButton requestActiveScanningModeUntilSceneAcquisition:];
-[SBCaptureHardwareButton simulateClickActivationLaunchForBundleIdentifier:completion:];
```

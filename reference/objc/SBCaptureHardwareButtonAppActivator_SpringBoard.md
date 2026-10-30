# `SBCaptureHardwareButtonAppActivator`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBCaptureButtonSuppressionManagerObserver`, `SBLayoutStateTransitionObserver`, `SBCaptureButtonSessionDelegate`, `BSInvalidatable`
- 52 instance variables, 5 properties, 62 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"SBLayoutStateTransitionCoordinator" _layoutStateTransitionCoordinator;
@"SBCameraActivationManager" _activationManager;
@"SBCaptureButtonSuppressionManager" _suppressionManager;
@"SBSetupManager" _setupManager;
@"SBFUserAuthenticationController" _authenticationController;
@"NSString" _bundleIDForCurrentActivation;
@"NSString" _prewarmedBundleIdentifier;
@"<SBCaptureButtonScanningModeResource>" _scanningModeAssertionProvider;
@"<SBHardwareButtonLaunchPreludeAnimationToken>" _activeLaunchAnimationPreludeToken;
@"<BSInvalidatable>" _buttonDownScanningRequest;
@"SBCaptureHardwareButtonScanningPowerLinkedTimer" _prewarmLockoutTimer;
@"SBCaptureHardwareButtonScanningPowerLinkedTimer" _expansionAnimationYAndScaleComponentsLockoutTimer;
@"SBCaptureHardwareButtonScanningPowerLinkedTimer" _launchGracePeriodActiveTimer;
@"BSAbsoluteMachTimer" _deferredLaunchAfterButtonUpGracePeriodTimer;
Q _machAbsoluteButtonPressDownTimeForDeferredLaunches;
d _gracePeriodForVOUnobstructionAfterRelease;
d _honorFaceDownDuration;
d _lastUnsuppressEventTimestamp;
B _isWaitingForButtonUpToPerformLaunch;
B _valid;
B _launchPendedDueToButtonDownWhileSuppressed;
q _unlockedEnvironmentMode;
@"<BSInvalidatable>" _hintDropletAssertion;
@"SBCaptureButtonSettings" _settings;
@"SBDeviceStationaryMotionDetector" _stationaryDeviceMotionDetector;
d _timeSinceLastStationary;
d _timeSinceLastNonStationary;
d _lastStationarySquelchTimestamp;
@"SBDeviceMotionDetector" _deviceMotionDetector;
@"SBCaptureButtonCoachingController" _coachingController;
@"SBCaptureButtonDefaults" _captureButtonDefaults;
@"<BSDefaultObserver>" _captureButtonDefaultsObserver;
B _disableStationaryDetection;
B _disableWakeWhenDim;
B _disableDirectLaunchAfterUnsuppress;
B _allowLaunchIfUnobstructedWhileButtonDown;
B _allowLaunchIfUnobstructedPromptlyAfterButtonUp;
B _enableCameraPose;
B _waitingForActivationCompletion;
i _consoleModeNotifyToken;
B _isConsoleModeActive;
B _disablePreLaunchCaptureButtonSuppression;
Q _consoleModeActiveStreakCount;
@"NSArray" _behaviors;
@"BCBatteryDeviceController" _batteryDeviceController;
B _isLongPressActivation;
B _preparedForCurrentActivation;
d _lastClickAgainSquelchTimestamp;
@"SiriTostadaSource" _siriTostadaSource;
@"NSUUID" _siriTostadaActivationIdentifier;
@"SBCaptureButtonSession" _session;
```

## Properties

```
@property (T@"SBCaptureButtonSession",&,N,V_session) session;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCaptureHardwareButtonAppActivator layoutStateTransitionCoordinator:transitionDidBeginWithTransitionContext:];
-[SBCaptureHardwareButtonAppActivator dealloc];
-[SBCaptureHardwareButtonAppActivator _cancel];
-[SBCaptureHardwareButtonAppActivator setSession:];
-[SBCaptureHardwareButtonAppActivator invalidate];
-[SBCaptureHardwareButtonAppActivator session];
-[SBCaptureHardwareButtonAppActivator _prewarmCameraForBundleIdentifier:];
-[SBCaptureHardwareButtonAppActivator _timeSinceLastStationarySquelch];
-[SBCaptureHardwareButtonAppActivator _attemptCameraAppLaunchSequence];
-[SBCaptureHardwareButtonAppActivator _initiateLaunchAnimationPrelude];
-[SBCaptureHardwareButtonAppActivator __clickAgainCoachingText];
-[SBCaptureHardwareButtonAppActivator __consoleModeCoachingText];
-[SBCaptureHardwareButtonAppActivator _abortVisionIntelligence];
-[SBCaptureHardwareButtonAppActivator _activateVisionIntelligenceWithCompletion:];
-[SBCaptureHardwareButtonAppActivator _beginObservingConsoleMode];
-[SBCaptureHardwareButtonAppActivator _behaviorsPolicy];
-[SBCaptureHardwareButtonAppActivator _cancelCameraPrewarmForBundleIdentifier:];
-[SBCaptureHardwareButtonAppActivator _cancelHintingDroplet];
-[SBCaptureHardwareButtonAppActivator _cancelLaunchAnimation];
-[SBCaptureHardwareButtonAppActivator _coachingStringForCoachIntent:];
-[SBCaptureHardwareButtonAppActivator _consoleModeDidChange];
-[SBCaptureHardwareButtonAppActivator _createCaptureButtonDefaultsObserver];
-[SBCaptureHardwareButtonAppActivator _deferredLaunchTimeoutDidOccur];
-[SBCaptureHardwareButtonAppActivator _foregoundAppBundleID];
-[SBCaptureHardwareButtonAppActivator _handleButtonUpInteraction:];
-[SBCaptureHardwareButtonAppActivator _handleCaptureButtonInteraction:];
-[SBCaptureHardwareButtonAppActivator _handleStationaryCallbackWithTimeSinceLastStationary:timeSinceLastNonStationary:];
-[SBCaptureHardwareButtonAppActivator _initiateLaunchAnimationExpansion];
-[SBCaptureHardwareButtonAppActivator _invalidateDeferredLaunchTimer];
-[SBCaptureHardwareButtonAppActivator _invalidateExpansionAnimationYAndScaleComponentsLockoutTimer];
-[SBCaptureHardwareButtonAppActivator _invalidateLaunchGracePeriodTimer];
-[SBCaptureHardwareButtonAppActivator _invalidatePrewarmLockoutTimer];
-[SBCaptureHardwareButtonAppActivator _invalidateVisionIntelligenceActivation];
-[SBCaptureHardwareButtonAppActivator _isInSwitcher];
-[SBCaptureHardwareButtonAppActivator _isOverUnlockedApplication];
-[SBCaptureHardwareButtonAppActivator _isVisionIntelligenceEnabled];
-[SBCaptureHardwareButtonAppActivator _launchCaptureApp];
-[SBCaptureHardwareButtonAppActivator _launchGracePeriodTimeoutDidOccur];
-[SBCaptureHardwareButtonAppActivator _prepareConfirmedLaunchSequenceForButtonDown:];
-[SBCaptureHardwareButtonAppActivator _prewarmLockoutTimeoutDidOccur];
-[SBCaptureHardwareButtonAppActivator _prewarmVisionIntelligenceActivation];
-[SBCaptureHardwareButtonAppActivator _setupCaptureButtonBehaviors];
-[SBCaptureHardwareButtonAppActivator _showHintingDroplet];
-[SBCaptureHardwareButtonAppActivator _startDeferredLaunchTimerWithTimeout:];
-[SBCaptureHardwareButtonAppActivator _startLaunchGracePeriodTimerWithTimeout:];
-[SBCaptureHardwareButtonAppActivator _startPrewarmLockoutTimerWithTimeout:];
-[SBCaptureHardwareButtonAppActivator _suppressionManagerDidUnsuppress:];
-[SBCaptureHardwareButtonAppActivator _takeButtonDownPowerAssertion];
-[SBCaptureHardwareButtonAppActivator _timeSinceLastViewUnobstructed];
-[SBCaptureHardwareButtonAppActivator _updateCaptureButtonDefaults];
-[SBCaptureHardwareButtonAppActivator _updateStationarySquelchTimestampInContext:timeSinceLastStationarySquelch:];
-[SBCaptureHardwareButtonAppActivator _updateStationaryState];
-[SBCaptureHardwareButtonAppActivator activateForGesture:atMachAbsoluteTime:pressDuration:suppressionOptions:];
-[SBCaptureHardwareButtonAppActivator cancelActivationForGesture:];
-[SBCaptureHardwareButtonAppActivator captureButtonSuppressionManager:event:];
-[SBCaptureHardwareButtonAppActivator deviceStationaryDetectionStationaryDebounceInterval];
-[SBCaptureHardwareButtonAppActivator initWithSettingsSnapshot:windowScene:scanModeResource:activationManager:suppressionManager:setupManager:authenticationController:HUDController:];
-[SBCaptureHardwareButtonAppActivator isActivationInProgress];
-[SBCaptureHardwareButtonAppActivator prepareForGesture:forAppBundleID:atMachAbsoluteTime:suppressionOptions:];
-[SBCaptureHardwareButtonAppActivator sealSessionAsUnintentionalDueToDisplaySwap];
-[SBCaptureHardwareButtonAppActivator sessionDidFinalize:];
-[SBCaptureHardwareButtonAppActivator windowSceneForCaptureButtonSession:];
```

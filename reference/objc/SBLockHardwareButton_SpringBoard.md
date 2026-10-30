# `SBLockHardwareButton`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHardwareButtonGestureParametersProviderBase`
- Protocols: `UIGestureRecognizerDelegate`, `SBHardwareButtonGestureParametersObserver`, `SBPressPrecedenceArbiter`, `SBHardwareButtonColluding`
- 24 instance variables, 28 properties, 76 instance methods, 0 class methods

## Instance variables

```
d _lastPressDownTime;
B _lastPressBeganDuringHingeMotion;
@"SBHardwareButtonCoordinator" _hardwareButtonCoordinator;
@"SBLockHardwareButtonActions" _buttonActions;
@"SBSystemGestureManager" _systemGestureManager;
@"SBHardwareButtonGestureParameters" _buttonGestureParameters;
@"SBPressGestureRecognizer" _buttonDownGestureRecognizer;
@"SBClickGestureRecognizer" _singlePressGestureRecognizer;
@"SBLongPressGestureRecognizer" _longPressGestureRecognizer;
@"SBClickGestureRecognizer" _doublePressGestureRecognizer;
@"SBClickGestureRecognizer" _triplePressGestureRecognizer;
@"SBClickGestureRecognizer" _quadruplePressGestureRecognizer;
@"SBLongPressGestureRecognizer" _terminalLockLongPressGestureRecognizer;
@"UIGestureRecognizer" _screenshotGestureRecognizer;
@"SBLongPressGestureRecognizer" _shutdownGestureRecognizer;
@"SBHomeHardwareButton" _homeHardwareButton;
@"SBVolumeHardwareButton" _volumeHardwareButton;
@"<BSInvalidatable>" _buttonActiveAssertion;
q _homeButtonType;
Q _configuredMaximumPressCount;
Q _currentPressCount;
d _pressSequenceDownTimestamp;
d _lastPressDownTimestamp;
d _lastPressUpTimestamp;
```

## Properties

```
@property (T@"SBSystemGestureManager",&,N,V_systemGestureManager) systemGestureManager;
@property (T@"SBLockHardwareButtonActions",&,N,V_buttonActions) buttonActions;
@property (T@"SBHardwareButtonGestureParameters",&,N,V_buttonGestureParameters) buttonGestureParameters;
@property (T@"SBPressGestureRecognizer",&,N,V_buttonDownGestureRecognizer) buttonDownGestureRecognizer;
@property (T@"SBClickGestureRecognizer",&,N,V_singlePressGestureRecognizer) singlePressGestureRecognizer;
@property (T@"SBLongPressGestureRecognizer",&,N,V_longPressGestureRecognizer) longPressGestureRecognizer;
@property (T@"SBClickGestureRecognizer",&,N,V_doublePressGestureRecognizer) doublePressGestureRecognizer;
@property (T@"SBClickGestureRecognizer",&,N,V_triplePressGestureRecognizer) triplePressGestureRecognizer;
@property (T@"SBClickGestureRecognizer",&,N,V_quadruplePressGestureRecognizer) quadruplePressGestureRecognizer;
@property (T@"SBLongPressGestureRecognizer",&,N,V_terminalLockLongPressGestureRecognizer) terminalLockLongPressGestureRecognizer;
@property (T@"UIGestureRecognizer",W,N,V_screenshotGestureRecognizer) screenshotGestureRecognizer;
@property (T@"SBLongPressGestureRecognizer",W,N,V_shutdownGestureRecognizer) shutdownGestureRecognizer;
@property (T@"SBHomeHardwareButton",W,N,V_homeHardwareButton) homeHardwareButton;
@property (T@"SBVolumeHardwareButton",W,N,V_volumeHardwareButton) volumeHardwareButton;
@property (T@"<BSInvalidatable>",&,N,V_buttonActiveAssertion) buttonActiveAssertion;
@property (Tq,N,V_homeButtonType) homeButtonType;
@property (TQ,N,V_configuredMaximumPressCount) configuredMaximumPressCount;
@property (TQ,N,V_currentPressCount) currentPressCount;
@property (Td,N,V_pressSequenceDownTimestamp) pressSequenceDownTimestamp;
@property (Td,N,V_lastPressDownTimestamp) lastPressDownTimestamp;
@property (Td,N,V_lastPressUpTimestamp) lastPressUpTimestamp;
@property (TB,N,V_lastPressBeganDuringHingeMotion) lastPressBeganDuringHingeMotion;
@property (TB,R,N) isButtonDown;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBHardwareButtonCoordinator",&,N,V_hardwareButtonCoordinator) hardwareButtonCoordinator;
```

## Instance methods

```
-[SBLockHardwareButton _cancelLongPressRecognizer:];
-[SBLockHardwareButton longPress:];
-[SBLockHardwareButton _gestureRecognizerFailed:];
-[SBLockHardwareButton setSystemGestureManager:];
-[SBLockHardwareButton gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[SBLockHardwareButton setHomeHardwareButton:];
-[SBLockHardwareButton setButtonActiveAssertion:];
-[SBLockHardwareButton setCurrentPressCount:];
-[SBLockHardwareButton setDoublePressGestureRecognizer:];
-[SBLockHardwareButton _createGestureRecognizers];
-[SBLockHardwareButton lastPressDownTimestamp];
-[SBLockHardwareButton setShutdownGestureRecognizer:];
-[SBLockHardwareButton homeHardwareButton];
-[SBLockHardwareButton longPressGestureRecognizer];
-[SBLockHardwareButton pressSequenceDownTimestamp];
-[SBLockHardwareButton triplePress:];
-[SBLockHardwareButton setLastPressBeganDuringHingeMotion:];
-[SBLockHardwareButton lastPressBeganDuringHingeMotion];
-[SBLockHardwareButton buttonGestureParameters];
-[SBLockHardwareButton initWithScreenshotGestureRecognizer:shutdownGestureRecognizer:proximitySensorCoordinator:hardwareButtonsSystemGestureManager:homeHardwareButton:volumeHardwareButton:homeButtonType:];
-[SBLockHardwareButton hardwareButtonIdentifier];
-[SBLockHardwareButton lastPressUpTimestamp];
-[SBLockHardwareButton setButtonActions:];
-[SBLockHardwareButton quadruplePress:];
-[SBLockHardwareButton cancelLongPress];
-[SBLockHardwareButton buttonDown:];
-[SBLockHardwareButton cancelHardwareButtonPress];
-[SBLockHardwareButton setTriplePressGestureRecognizer:];
-[SBLockHardwareButton singlePress:];
-[SBLockHardwareButton screenshotRecognizerDidRecognize:];
-[SBLockHardwareButton hardwareButtonGestureParameters];
-[SBLockHardwareButton configuredMaximumPressCount];
-[SBLockHardwareButton volumeHardwareButton];
-[SBLockHardwareButton provider:didUpdateButtonGestureParameters:];
-[SBLockHardwareButton gestureRecognizerShouldBegin:];
-[SBLockHardwareButton terminalLockLongPressGestureRecognizer];
-[SBLockHardwareButton shutdownGestureRecognizer];
-[SBLockHardwareButton systemGestureManager];
-[SBLockHardwareButton quadruplePressGestureRecognizer];
-[SBLockHardwareButton setSinglePressGestureRecognizer:];
-[SBLockHardwareButton _shouldRunActions];
-[SBLockHardwareButton isButtonDown];
-[SBLockHardwareButton setLastPressDownTimestamp:];
-[SBLockHardwareButton setButtonDownGestureRecognizer:];
-[SBLockHardwareButton setButtonGestureParameters:];
-[SBLockHardwareButton doublePress:];
-[SBLockHardwareButton homeButtonType];
-[SBLockHardwareButton _cancelGestureRecognizer:];
-[SBLockHardwareButton gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBLockHardwareButton screenshotGestureRecognizer];
-[SBLockHardwareButton setLastPressUpTimestamp:];
-[SBLockHardwareButton buttonDownGestureRecognizer];
-[SBLockHardwareButton setHardwareButtonCoordinator:];
-[SBLockHardwareButton _updatePressCountForDownEvent];
-[SBLockHardwareButton reverseFadeOutIfNeeded];
-[SBLockHardwareButton currentPressCount];
-[SBLockHardwareButton buttonActions];
-[SBLockHardwareButton singlePressGestureRecognizer];
-[SBLockHardwareButton setConfiguredMaximumPressCount:];
-[SBLockHardwareButton setLongPressGestureRecognizer:];
-[SBLockHardwareButton setVolumeHardwareButton:];
-[SBLockHardwareButton setScreenshotGestureRecognizer:];
-[SBLockHardwareButton preemptablePressGestureRecognizers];
-[SBLockHardwareButton buttonActiveAssertion];
-[SBLockHardwareButton hardwareButtonCoordinator];
-[SBLockHardwareButton setTerminalLockLongPressGestureRecognizer:];
-[SBLockHardwareButton triplePressGestureRecognizer];
-[SBLockHardwareButton terminalLockLongPress:];
-[SBLockHardwareButton setQuadruplePressGestureRecognizer:];
-[SBLockHardwareButton _reconfigureButtonGestureRecognizers];
-[SBLockHardwareButton _pressesOverlapHingeMotion];
-[SBLockHardwareButton forceResetSequenceDidBegin];
-[SBLockHardwareButton initWithScreenshotGestureRecognizer:shutdownGestureRecognizer:proximitySensorCoordinator:hardwareButtonsSystemGestureManager:homeHardwareButton:volumeHardwareButton:buttonActions:homeButtonType:createGestures:];
-[SBLockHardwareButton setPressSequenceDownTimestamp:];
-[SBLockHardwareButton setHomeButtonType:];
-[SBLockHardwareButton doublePressGestureRecognizer];
```

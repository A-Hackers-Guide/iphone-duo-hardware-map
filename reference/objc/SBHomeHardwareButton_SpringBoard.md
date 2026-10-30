# `SBHomeHardwareButton`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `SBHardwareButtonGestureParametersObserver`, `SBHardwareButtonColluding`
- 14 instance variables, 18 properties, 67 instance methods, 0 class methods

## Instance variables

```
@"<BSInvalidatable>" _fingerDetectEnabledAssertion;
@"NSMutableSet" _hintSuppressionAssertions;
@"NSMutableOrderedSet" _longPressDurationAssertions;
B _longPressDidOccur;
@"SBHardwareButtonCoordinator" _hardwareButtonCoordinator;
@"SBHomeHardwareButtonActions" _buttonActions;
@"SBHardwareButtonGestureParameters" _buttonGestureParameters;
@"SBHomeHardwareButtonGestureRecognizerConfiguration" _gestureRecognizerConfiguration;
@"UIGestureRecognizer" _screenshotGestureRecognizer;
q _homeButtonType;
q _maximumPressCount;
q _maximumTapCount;
@"NSMutableDictionary" _emulatedPerSenderDownCount;
@"BKSButtonHapticsDefinition" _buttonDefinition;
```

## Properties

```
@property (T@"SBHomeHardwareButtonActions",&,N,V_buttonActions) buttonActions;
@property (T@"SBHardwareButtonGestureParameters",&,N,V_buttonGestureParameters) buttonGestureParameters;
@property (T@"SBHomeHardwareButtonGestureRecognizerConfiguration",&,N,V_gestureRecognizerConfiguration) gestureRecognizerConfiguration;
@property (T@"UIGestureRecognizer",W,N,V_screenshotGestureRecognizer) screenshotGestureRecognizer;
@property (Tq,N,V_homeButtonType) homeButtonType;
@property (Tq,N,V_maximumPressCount) maximumPressCount;
@property (Tq,N,V_maximumTapCount) maximumTapCount;
@property (TB,N,V_longPressDidOccur) longPressDidOccur;
@property (T@"NSMutableDictionary",&,N,V_emulatedPerSenderDownCount) emulatedPerSenderDownCount;
@property (T@"BKSButtonHapticsDefinition",&,N,V_buttonDefinition) buttonDefinition;
@property (TB,R,N,GisButtonDown) buttonDown;
@property (TB,R,N) supportsAcceleratedAppDismiss;
@property (Tq,N) hapticType;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBHardwareButtonCoordinator",&,N,V_hardwareButtonCoordinator) hardwareButtonCoordinator;
```

## Instance methods

```
-[SBHomeHardwareButton _longPressGestureRecognizerShouldBegin:];
-[SBHomeHardwareButton longPress:];
-[SBHomeHardwareButton initWithScreenshotGestureRecognizer:hardwareButtonsSystemGestureManager:homeButtonType:];
-[SBHomeHardwareButton setGestureRecognizerConfiguration:];
-[SBHomeHardwareButton gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[SBHomeHardwareButton longPressDidOccur];
-[SBHomeHardwareButton _terminateHomeButtonEventAtCount:];
-[SBHomeHardwareButton acceleratedSinglePressUp:];
-[SBHomeHardwareButton gestureRecognizerConfiguration];
-[SBHomeHardwareButton initWithScreenshotGestureRecognizer:homeButtonType:buttonActions:gestureRecognizerConfiguration:];
-[SBHomeHardwareButton performWhenMenuButtonIsUpUsingBlock:];
-[SBHomeHardwareButton buttonGestureParameters];
-[SBHomeHardwareButton addHintSuppressionAssertion:];
-[SBHomeHardwareButton hardwareButtonIdentifier];
-[SBHomeHardwareButton performAfterMenuButtonUpIsHandledUsingBlock:];
-[SBHomeHardwareButton setButtonActions:];
-[SBHomeHardwareButton _processDoubleDownAndDoubleUpSimultaneously];
-[SBHomeHardwareButton _createGestureRecognizersWithConfiguration:];
-[SBHomeHardwareButton cancelLongPress];
-[SBHomeHardwareButton cancelHardwareButtonPress];
-[SBHomeHardwareButton initialButtonUp:];
-[SBHomeHardwareButton setLongPressDidOccur:];
-[SBHomeHardwareButton doubleTapUp:];
-[SBHomeHardwareButton screenshotRecognizerDidRecognize:];
-[SBHomeHardwareButton _singlePressUp:];
-[SBHomeHardwareButton maximumPressCount];
-[SBHomeHardwareButton setButtonDefinition:];
-[SBHomeHardwareButton provider:didUpdateButtonGestureParameters:];
-[SBHomeHardwareButton removeHintSuppressionAssertion:];
-[SBHomeHardwareButton _reconfigureHomeButton];
-[SBHomeHardwareButton emulateHomeButtonEventsIfNeeded:];
-[SBHomeHardwareButton supportsAcceleratedAppDismiss];
-[SBHomeHardwareButton setMaximumPressCount:];
-[SBHomeHardwareButton gestureRecognizerShouldBegin:];
-[SBHomeHardwareButton triplePressUp:];
-[SBHomeHardwareButton setHapticType:];
-[SBHomeHardwareButton initialButtonDown:];
-[SBHomeHardwareButton isButtonDown];
-[SBHomeHardwareButton setButtonGestureParameters:];
-[SBHomeHardwareButton _setFingerDetectionEnabled:];
-[SBHomeHardwareButton homeButtonType];
-[SBHomeHardwareButton _cancelGestureRecognizer:];
-[SBHomeHardwareButton gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBHomeHardwareButton screenshotGestureRecognizer];
-[SBHomeHardwareButton doublePressDown:];
-[SBHomeHardwareButton setHardwareButtonCoordinator:];
-[SBHomeHardwareButton _acceleratedSinglePressRecognizerShouldBegin];
-[SBHomeHardwareButton _isMenuDoublePressDisabled];
-[SBHomeHardwareButton buttonActions];
-[SBHomeHardwareButton _reconfigureGestureRecognizersForNewMaximumTapCount:oldMaximumTapCount:];
-[SBHomeHardwareButton _startObservingReconfigurationTriggers];
-[SBHomeHardwareButton buttonDefinition];
-[SBHomeHardwareButton configureForwardingToLockButton:];
-[SBHomeHardwareButton addLongPressDurationAssertion:];
-[SBHomeHardwareButton setScreenshotGestureRecognizer:];
-[SBHomeHardwareButton hapticType];
-[SBHomeHardwareButton emulatedPerSenderDownCount];
-[SBHomeHardwareButton setEmulatedPerSenderDownCount:];
-[SBHomeHardwareButton maximumTapCount];
-[SBHomeHardwareButton _reconfigureGestureRecognizersForNewMaximumPressCount:oldMaximumPressCount:];
-[SBHomeHardwareButton hardwareButtonCoordinator];
-[SBHomeHardwareButton setMaximumTapCount:];
-[SBHomeHardwareButton _isMenuDoublePressAllowed:];
-[SBHomeHardwareButton doublePressUp:];
-[SBHomeHardwareButton singlePressUp:];
-[SBHomeHardwareButton setHomeButtonType:];
-[SBHomeHardwareButton removeLongPressDurationAssertion:];
```

# `SBVolumeHardwareButton`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayContentModeTransitionObserver`, `UIGestureRecognizerDelegate`, `SBPressPrecedenceArbiter`, `SBHardwareButtonColluding`
- 14 instance variables, 9 properties, 27 instance methods, 0 class methods

## Instance variables

```
q _homeButtonType;
@"SBSystemGestureManager" _systemGestureManager;
@"SBPressGestureRecognizer" _volumeIncreaseButtonPressGestureRecognizer;
@"SBPressGestureRecognizer" _volumeDecreaseButtonPressGestureRecognizer;
@"SBPressGestureRecognizer" _rawVolumeButtonPressGestureRecognizer;
@"UIGestureRecognizer" _screenshotGestureRecognizer;
@"UIGestureRecognizer" _shutdownGestureRecognizer;
@"<BSInvalidatable>" _volumeIncreaseActiveAssertion;
@"<BSInvalidatable>" _volumeDecreaseActiveAssertion;
@"SBHardwareButtonCoordinator" _hardwareButtonCoordinator;
@"NSHashTable" _volumePressBandits;
@"SBPressSequenceObserver" _volumeIncreaseSequenceObserver;
@"SBPressSequenceObserver" _volumeDecreaseSequenceObserver;
@"SBVolumeHardwareButtonActions" _buttonActions;
```

## Properties

```
@property (T@"SBPressSequenceObserver",R,N,V_volumeIncreaseSequenceObserver) volumeIncreaseSequenceObserver;
@property (T@"SBPressSequenceObserver",R,N,V_volumeDecreaseSequenceObserver) volumeDecreaseSequenceObserver;
@property (T@"SBVolumeHardwareButtonActions",R,N,V_buttonActions) buttonActions;
@property (T@"NSHashTable",W,N,V_volumePressBandits) volumePressBandits;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"SBHardwareButtonCoordinator",&,N,V_hardwareButtonCoordinator) hardwareButtonCoordinator;
```

## Instance methods

```
-[SBVolumeHardwareButton gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[SBVolumeHardwareButton _createGestureRecognizers];
-[SBVolumeHardwareButton displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBVolumeHardwareButton hardwareButtonIdentifier];
-[SBVolumeHardwareButton dealloc];
-[SBVolumeHardwareButton displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBVolumeHardwareButton cancelHardwareButtonPress];
-[SBVolumeHardwareButton gestureRecognizerShouldBegin:];
-[SBVolumeHardwareButton gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBVolumeHardwareButton setHardwareButtonCoordinator:];
-[SBVolumeHardwareButton buttonActions];
-[SBVolumeHardwareButton preemptablePressGestureRecognizers];
-[SBVolumeHardwareButton hardwareButtonCoordinator];
-[SBVolumeHardwareButton _logVolumeButtonWithObserver:down:];
-[SBVolumeHardwareButton _rawVolumeDecreasePress:physicalButtonKind:];
-[SBVolumeHardwareButton _rawVolumeIncreasePress:physicalButtonKind:];
-[SBVolumeHardwareButton _rawVolumePress:];
-[SBVolumeHardwareButton addVolumePressBandit:];
-[SBVolumeHardwareButton cancelVolumePress];
-[SBVolumeHardwareButton initWithScreenshotGestureRecognizer:shutdownGestureRecognizer:hardwareButtonsSystemGestureManager:homeButtonType:];
-[SBVolumeHardwareButton removeVolumePressBandit:];
-[SBVolumeHardwareButton setVolumePressBandits:];
-[SBVolumeHardwareButton volumeDecreasePress:];
-[SBVolumeHardwareButton volumeDecreaseSequenceObserver];
-[SBVolumeHardwareButton volumeIncreasePress:];
-[SBVolumeHardwareButton volumeIncreaseSequenceObserver];
-[SBVolumeHardwareButton volumePressBandits];
```

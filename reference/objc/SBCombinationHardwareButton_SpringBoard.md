# `SBCombinationHardwareButton`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `SBHardwareButtonGestureParametersObserver`, `SBSOSLockGestureObserverDelegate`, `SBSOSClawGestureObserverDelegate`, `SBPressPrecedenceArbiter`, `SBHardwareButtonColluding`
- 14 instance variables, 5 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _screenshotDisableAssertions;
d _threeButtonChordStartTimestamp;
@"SBHardwareButtonCoordinator" _hardwareButtonCoordinator;
@"SBSystemGestureManager" _systemGestureManager;
@"SBCombinationHardwareButtonActions" _buttonActions;
@"SBClickGestureRecognizer" _screenshotGestureRecognizer;
@"SBHomeHardwareButton" _homeHardwareButton;
@"SBLockHardwareButton" _lockHardwareButton;
@"SBVolumeHardwareButton" _volumeHardwareButton;
@"SBProximitySensorCoordinator" _proximitySensorCoordinator;
@"SBPressGestureRecognizer" _sosGestureRecognizer;
@"SBSOSClawGestureObserver" _sosClawGestureObserver;
@"SBSOSLockGestureObserver" _sosLockGestureObserver;
@"SBLongPressGestureRecognizer" _shutdownGestureRecognizer;
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
-[SBCombinationHardwareButton gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[SBCombinationHardwareButton _configureGestureRecognizers];
-[SBCombinationHardwareButton _setScreenshotDisabled:forReason:];
-[SBCombinationHardwareButton shutdownGesture:];
-[SBCombinationHardwareButton sosLockTriggerDidBecomeActive:];
-[SBCombinationHardwareButton sosGesture:];
-[SBCombinationHardwareButton sosClawDidTriggerSOS:completion:];
-[SBCombinationHardwareButton hardwareButtonIdentifier];
-[SBCombinationHardwareButton sosClawDidBecomeInactive:];
-[SBCombinationHardwareButton dealloc];
-[SBCombinationHardwareButton sosLockTriggerDidBecomeInactive:];
-[SBCombinationHardwareButton screenshotGesture:];
-[SBCombinationHardwareButton cancelHardwareButtonPress];
-[SBCombinationHardwareButton provider:didUpdateButtonGestureParameters:];
-[SBCombinationHardwareButton _sosTriggerMechanismDidChange];
-[SBCombinationHardwareButton gestureRecognizerShouldBegin:];
-[SBCombinationHardwareButton _configureSOSGestureBehaviors];
-[SBCombinationHardwareButton gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBCombinationHardwareButton setHardwareButtonCoordinator:];
-[SBCombinationHardwareButton sosLockDidTriggerSOS:completion:];
-[SBCombinationHardwareButton preemptablePressGestureRecognizers];
-[SBCombinationHardwareButton hardwareButtonCoordinator];
-[SBCombinationHardwareButton sosClawAutoCallInteractiveStateChanged:interacting:];
-[SBCombinationHardwareButton initWithScreenshotGestureRecognizer:shutdownGestureRecognizer:homeHardwareButton:lockHardwareButton:volumeHardwareButton:proximitySensorCoordinator:hardwareButtonsSystemGestureManager:];
-[SBCombinationHardwareButton sosClawDidBecomeActive:];
```

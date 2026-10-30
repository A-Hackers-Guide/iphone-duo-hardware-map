# `SBLiftToWakeController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSBacklightStateObserving`, `SBBacklightControllerObserver`, `CMWakeGestureDelegate`
- 12 instance variables, 7 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"CMWakeGestureManager" _wakeGestureManager;
q _wakeGestureState;
@"NSHashTable" _observers;
@"SBIdleTimerDefaults" _idleTimerDefaults;
B _screenOn;
B _isEnabled;
B _observingCMWakeGestureManager;
@"BSCompoundAssertion" _bumpToWakeAssertions;
@"BSCompoundAssertion" _disableLiftToWakeAssertions;
@"SBWakeDebounceFilter" _bumpToWakeDebounceFilter;
@"NSObject<OS_dispatch_queue>" _wakeGestureManagerQueue;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBIdleTimerDefaults",&,N,G_idleTimerDefaults,S_setIdleTimerDefaults:,V_idleTimerDefaults) idleTimerDefaults;
@property (TB,R,N,GisEnabled,V_isEnabled) enabled;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLiftToWakeController _loggingIdentifier];
-[SBLiftToWakeController backlightController:willTransitionToBacklightState:source:];
-[SBLiftToWakeController initWithBacklightController:];
-[SBLiftToWakeController _isObservingWakeGestureManager];
-[SBLiftToWakeController _screenTurnedOff];
-[SBLiftToWakeController removeObserver:];
-[SBLiftToWakeController initWithBacklightController:idleTimerDefaults:];
-[SBLiftToWakeController backlight:didCompleteUpdateToState:forEvent:];
-[SBLiftToWakeController acquireBumpToWakeEnableAssertionForReason:];
-[SBLiftToWakeController _setIdleTimerDefaults:];
-[SBLiftToWakeController isEnabled];
-[SBLiftToWakeController addObserver:];
-[SBLiftToWakeController _startObservingIfNecessary];
-[SBLiftToWakeController _stopObservingBumpsIfNecessary];
-[SBLiftToWakeController wakeGestureManager:didUpdateWakeGestureEvent:];
-[SBLiftToWakeController acquireDisableLiftToWakeAssertionForReason:];
-[SBLiftToWakeController _ignoredTransition:];
-[SBLiftToWakeController _screenTurnedOn];
-[SBLiftToWakeController _startObservingBumpsIfNecessary];
-[SBLiftToWakeController _idleTimerDefaults];
-[SBLiftToWakeController description];
-[SBLiftToWakeController _stopObservingIfNecessary];
-[SBLiftToWakeController _reconsiderEnablement];
-[SBLiftToWakeController _sendTransitionToObservers:deviceOrientation:];
-[SBLiftToWakeController windowScene];
-[SBLiftToWakeController _sendIgnoredTransitionToObservers:];
```

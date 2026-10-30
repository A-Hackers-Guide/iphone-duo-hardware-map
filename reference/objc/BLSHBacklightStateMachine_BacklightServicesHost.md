# `BLSHBacklightStateMachine`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightHostObserving`, `BLSHBacklightPlatformProviderObserver`, `BLSHDisableAlwaysOnProvider`, `BLSHBacklightHostInternalTelemetrySource`, `BLSHBacklightHostObserving`, `BLSHOnSystemSleepActionDelegate`, `BLSBacklightProxy`, `BLSHBacklightHostObservable_Private`
- 27 instance variables, 20 properties, 37 instance methods, 0 class methods

## Instance variables

```
@"<BLSHOSDisplayInterfaceProviding>" _display;
@"NSString" _displayLoggingName;
@"<BLSHOSInterfaceProviding>" _osInterfaceProvider;
@"BLSHOnSystemSleepAction" _sleepAction;
@? _lock_sleepActionCompletion;
@"BLSBacklightChangeEvent" _lock_transitioningEvent;
@"BLSAssertion" _lock_flipbookPowerSavingAssertion;
@"<BLSHSystemActivityAsserting>" _lock_activeOnAPAwakeAssertion;
Q _lock_activeOnAPAwakeAssertionAcquireTime;
@"<BSInvalidatable>" _lock_unexpectedSleepDebounceTimer;
@"<BLSHSystemActivityAsserting>" _lock_performEventAPAwakeAssertion;
@"<BSTimerScheduleQuerying><BSInvalidatable>" _lock_activeOnAPAwakeTimeoutTimer;
@"NSMapTable" _lock_observers;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
Q _lock_nextEventID;
q _lock_activityState;
B _lock_alwaysOnEnabledResolved;
B _lock_alwaysOnEnabledByPlatform;
B _lock_alwaysOnDisabledByAssertion;
B _lock_alwaysOnEnabledAfterInitialization;
B _lock_notifyingObserversWillTransitionToState;
B _suppressionSupported;
B _deviceSupportsAlwaysOn;
@"<BLSHBacklightHostTelemetryDelegate>" _telemetryDelegate;
@"<BLSHBacklightHostTelemetryDelegate>" _internalTelemetryDelegate;
@"BLSBacklightChangeEvent" _activeTransitionEvent;
@"<BLSHBacklightStateMachineEventPerforming>" _eventPerformer;
```

## Properties

```
@property (Tq,R,N) backlightState;
@property (TB,R,N,GisTransitioning) transitioning;
@property (T@"BLSBacklightChangeEvent",R,N,V_activeTransitionEvent) activeTransitionEvent;
@property (T@"<BLSHBacklightStateMachineEventPerforming>",R,N,V_eventPerformer) eventPerformer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,GisAlwaysOnDisabledByAssertion) alwaysOnDisabledByAssertion;
@property (T@"<BLSDisplay>",R,N) display;
@property (T@"<BLSHBacklightHostTelemetryDelegate>",W,V_internalTelemetryDelegate) internalTelemetryDelegate;
@property (T@"<BLSHBacklightHostTelemetryDelegate>",W,V_telemetryDelegate) telemetryDelegate;
@property (Tq,R,N) backlightDisplayMode;
@property (TQ,R,N) backlightStateChangeTimestamp;
@property (T@"NSString",R,C,N) backlightStateDescription;
@property (Tq,R,N) flipbookState;
@property (TB,R,N,GisAlwaysOnEnabled) alwaysOnEnabled;
@property (TB,R,N) deviceSupportsAlwaysOn;
@property (Tq,R,N) settledBacklightState;
@property (Tq,R,N) targetBacklightDisplayMode;
```

## Instance methods

```
-[BLSHBacklightStateMachine backlight:didCompleteUpdateToState:forEvents:abortedEvents:];
-[BLSHBacklightStateMachine setTelemetryDelegate:];
-[BLSHBacklightStateMachine backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:];
-[BLSHBacklightStateMachine display];
-[BLSHBacklightStateMachine registerHandlersForService:];
-[BLSHBacklightStateMachine deviceSupportsAlwaysOn];
-[BLSHBacklightStateMachine backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:];
-[BLSHBacklightStateMachine setInternalTelemetryDelegate:];
-[BLSHBacklightStateMachine backlightStateChangeTimestamp];
-[BLSHBacklightStateMachine isAlwaysOnEnabled];
-[BLSHBacklightStateMachine backlightDisplayMode];
-[BLSHBacklightStateMachine initForDisplay:platformProvider:eventPerformer:osInterfaceProvider:];
-[BLSHBacklightStateMachine internalTelemetryDelegate];
-[BLSHBacklightStateMachine removeObserver:];
-[BLSHBacklightStateMachine isTransitioning];
-[BLSHBacklightStateMachine telemetryDelegate];
-[BLSHBacklightStateMachine systemSleepAction:systemWillWakeForReason:];
-[BLSHBacklightStateMachine performChangeRequest:];
-[BLSHBacklightStateMachine dealloc];
-[BLSHBacklightStateMachine flipbookState];
-[BLSHBacklightStateMachine platformProvider:didChangeAlwaysOnSetting:];
-[BLSHBacklightStateMachine backlightStateDescription];
-[BLSHBacklightStateMachine eventPerformer];
-[BLSHBacklightStateMachine setAlwaysOnDisabledByAssertion:];
-[BLSHBacklightStateMachine addObserver:];
-[BLSHBacklightStateMachine backlightState];
-[BLSHBacklightStateMachine activeTransitionEvent];
-[BLSHBacklightStateMachine isAlwaysOnDisabledByAssertion];
-[BLSHBacklightStateMachine performUnexpectedSleepRequest:];
-[BLSHBacklightStateMachine backlight:didUpdateVisualContentsToBeginTransitionToState:forEvents:abortedEvents:];
-[BLSHBacklightStateMachine settledBacklightState];
-[BLSHBacklightStateMachine targetBacklightDisplayMode];
-[BLSHBacklightStateMachine backlight:rampingToBrightnessCurve:withDuration:forEvents:abortedEvents:];
-[BLSHBacklightStateMachine platformProviderDidDetectSignificantUserInteraction:];
-[BLSHBacklightStateMachine backlight:didCompleteUpdateToFlipbookState:forEvents:abortedEvents:];
-[BLSHBacklightStateMachine systemSleepAction:performWithCompletion:];
-[BLSHBacklightStateMachine addObserver:forBacklight:];
```

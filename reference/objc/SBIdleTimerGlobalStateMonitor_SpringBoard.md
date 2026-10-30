# `SBIdleTimerGlobalStateMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBBacklightCoordinatorObserver`, `SBPocketStateMonitorObserver`, `_SBIdleTimerGlobalSettingMonitorDelegate`, `SBIdleTimerServiceDelegate`, `SBFThermalConditionObserver`, `SBBacklightControllerObserver`, `SBDisplayContentModeTransitionObserver`
- 20 instance variables, 19 properties, 36 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _observerLock;
@"NSHashTable" _observers;
@"SBIdleTimerService" _idleTimerService;
@"SBLocalDefaults" _localDefaults;
@"<SBFThermalBlockProvider>" _thermalBlockProvider;
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@? _dontLockEver;
@? _dontDimOrLockOnAC;
@? _disableAttentionAwareness;
@? _minimumLockscreenIdleTime;
@"_SBIdleTimerGlobalNumericSettingMonitor" _autoLockTimeoutMonitor;
@"_SBIdleTimerGlobalBoolSettingMonitor" _batterySaverModeMonitor;
@"_SBIdleTimerGlobalBoolSettingMonitor" _onACPowerMonitor;
q _pocketState;
B _autoDimDisabled;
B _thermalBlocked;
B _screenIsOn;
@"<BSInvalidatable>" _stateCaptureAssertion;
B _faceDownOnTable;
@"SBBacklightCoordinator" _backlightCoordinator;
```

## Properties

```
@property (Tq,R,N,V_pocketState) pocketState;
@property (TB,R,N) dontLockEver;
@property (TB,R,N) dontDimOrLockOnAC;
@property (TB,R,N) disableAttentionAwareness;
@property (Td,R,N) minimumLockscreenIdleTime;
@property (TB,R,N,GisScreenOn) screenOn;
@property (T@"NSNumber",R,N) autoLockTimeout;
@property (TB,R,N,GisBatterySaverModeActive) batterySaverModeActive;
@property (TB,R,N,GisOnACPower) onACPower;
@property (TB,R,N,GisFaceDownOnTable,V_faceDownOnTable) faceDownOnTable;
@property (TB,R,N,GisAutoDimDisabled) autoDimDisabled;
@property (T@"SBIdleTimerAggregatedClientConfiguration",R,N) aggregatedClientConfiguration;
@property (TB,R,N,GisThermalBlocked) thermalBlocked;
@property (Tq,R,N) primarySurfaceType;
@property (T@"SBBacklightCoordinator",&,N,V_backlightCoordinator) backlightCoordinator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIdleTimerGlobalStateMonitor _addStateCaptureHandlers];
-[SBIdleTimerGlobalStateMonitor isScreenOn];
-[SBIdleTimerGlobalStateMonitor pocketStateMonitor:pocketStateDidChangeFrom:to:];
-[SBIdleTimerGlobalStateMonitor _stateCaptureDescription];
-[SBIdleTimerGlobalStateMonitor removeObserver:];
-[SBIdleTimerGlobalStateMonitor displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBIdleTimerGlobalStateMonitor isBatterySaverModeActive];
-[SBIdleTimerGlobalStateMonitor minimumLockscreenIdleTime];
-[SBIdleTimerGlobalStateMonitor dealloc];
-[SBIdleTimerGlobalStateMonitor displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBIdleTimerGlobalStateMonitor _boolMonitorForProperty:inDefaults:fetchingWith:];
-[SBIdleTimerGlobalStateMonitor initWithLocalDefaults:profileConnection:pocketStateMonitor:chargingController:idleTimerService:thermalBlockProvider:displayContentModeCoordinator:];
-[SBIdleTimerGlobalStateMonitor idleTimerServiceTimeoutAssertionsDidChange:fromClient:];
-[SBIdleTimerGlobalStateMonitor disableAttentionAwareness];
-[SBIdleTimerGlobalStateMonitor dontDimOrLockOnAC];
-[SBIdleTimerGlobalStateMonitor idleTimerGlobalSettingMonitor:changedForReason:];
-[SBIdleTimerGlobalStateMonitor _evaluateBacklightState];
-[SBIdleTimerGlobalStateMonitor autoLockTimeout];
-[SBIdleTimerGlobalStateMonitor addObserver:];
-[SBIdleTimerGlobalStateMonitor _timeIntervalMonitorForProperty:inDefaults:fetchingWith:];
-[SBIdleTimerGlobalStateMonitor _updateFaceDownOnTable];
-[SBIdleTimerGlobalStateMonitor setBacklightCoordinator:];
-[SBIdleTimerGlobalStateMonitor isAutoDimDisabled];
-[SBIdleTimerGlobalStateMonitor thermalBlockStatusChanged:];
-[SBIdleTimerGlobalStateMonitor isThermalBlocked];
-[SBIdleTimerGlobalStateMonitor _updateObserversForReason:];
-[SBIdleTimerGlobalStateMonitor isOnACPower];
-[SBIdleTimerGlobalStateMonitor _updateAutoDimDisabled];
-[SBIdleTimerGlobalStateMonitor backlightCoordinator:didUpdateAggregateBacklightState:fromSource:];
-[SBIdleTimerGlobalStateMonitor aggregatedClientConfiguration];
-[SBIdleTimerGlobalStateMonitor isFaceDownOnTable];
-[SBIdleTimerGlobalStateMonitor primarySurfaceType];
-[SBIdleTimerGlobalStateMonitor backlightCoordinator];
-[SBIdleTimerGlobalStateMonitor backlightCoordinator:willUpdateAggregateBacklightState:fromSource:];
-[SBIdleTimerGlobalStateMonitor dontLockEver];
-[SBIdleTimerGlobalStateMonitor pocketState];
```

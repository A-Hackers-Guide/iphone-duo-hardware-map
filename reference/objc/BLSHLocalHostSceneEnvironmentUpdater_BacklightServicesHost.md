# `BLSHLocalHostSceneEnvironmentUpdater`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightEnvironmentStateMachineDelegate`, `BLSHBacklightInactiveEnvironmentSessionUpdating`, `BLSHBacklightSceneHostEnvironmentObserver`, `BLSHDisplayFlipbookStateProvider`, `BLSBacklightSceneEnvironmentUpdating`
- 15 instance variables, 8 properties, 29 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BLSHBacklightEnvironmentSessionProviding>" _sessionProvider;
@"<BLSBacklightSceneEnvironment_Private>" _localHostEnvironment;
@"<BLSHOSTimerProviding>" _osTimerProvider;
@"<BLSHInactiveBudgetPolicing_Private>" _inactiveBudgetPolicy;
@"BLSHBacklightInactiveEnvironmentSession" _lock_inactiveEnvSession;
@"BLSHBacklightEnvironmentPresentation" _lock_updatingToPresentation;
@"BLSHBacklightEnvironmentStateMachine" _environmentStateMachine;
@"NSMutableSet" _lock_timelinesCalculators;
@"BLSBacklightSceneUpdate" _lock_sceneUpdateForPerformingEvent;
@"BLSBacklightChangeEvent" _lock_localTriggerEventForPerformingEvent;
@"BLSHCriticalAssertTester" _criticalAssertTester;
Q _lock_nextEventID;
Q _stateHandler;
q _backlightState;
```

## Properties

```
@property (Tq,R,N,V_backlightState) backlightState;
@property (T@"NSString",R,C,N) delegateLoggingName;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisFlipbook) flipbook;
@property (TB,R,N,GflipbookUsesLowPowerRendering) flipbookUsesLowPowerRendering;
```

## Instance methods

```
-[BLSHLocalHostSceneEnvironmentUpdater hostEnvironment:hostDidSet1HzFlipbook:];
-[BLSHLocalHostSceneEnvironmentUpdater flipbookUsesLowPowerRendering];
-[BLSHLocalHostSceneEnvironmentUpdater hostEnvironment:invalidateContentForReason:];
-[BLSHLocalHostSceneEnvironmentUpdater environmentStateMachine:didUpdateToPresentation:];
-[BLSHLocalHostSceneEnvironmentUpdater isFlipbook];
-[BLSHLocalHostSceneEnvironmentUpdater dealloc];
-[BLSHLocalHostSceneEnvironmentUpdater delegateLoggingName];
-[BLSHLocalHostSceneEnvironmentUpdater environmentStateMachine:didCompleteUpdateToState:];
-[BLSHLocalHostSceneEnvironmentUpdater backlightState];
-[BLSHLocalHostSceneEnvironmentUpdater performDesiredFidelityRequest:];
-[BLSHLocalHostSceneEnvironmentUpdater performFrameSpecifiersRequest:];
-[BLSHLocalHostSceneEnvironmentUpdater updatedEnvironmentWithDelta:backlightSceneUpdate:];
-[BLSHLocalHostSceneEnvironmentUpdater description];
-[BLSHLocalHostSceneEnvironmentUpdater environmentStateMachine:didBeginUpdateToState:];
-[BLSHLocalHostSceneEnvironmentUpdater environmentStateMachine:didUpdateFlipbookVisualState:specifier:];
-[BLSHLocalHostSceneEnvironmentUpdater inactiveEnvironmentSession:updateToPresentation:];
-[BLSHLocalHostSceneEnvironmentUpdater environmentStateMachine:didUpdateToSpecifier:];
-[BLSHLocalHostSceneEnvironmentUpdater ensureInactiveEnvSessionCreated];
-[BLSHLocalHostSceneEnvironmentUpdater _lock_update1HzFromPresentation:];
-[BLSHLocalHostSceneEnvironmentUpdater aggregateDesiredFidelityForBacklightState:withCompletion:];
-[BLSHLocalHostSceneEnvironmentUpdater destroyInactiveEnvSession];
-[BLSHLocalHostSceneEnvironmentUpdater ensureAlwaysOnSessionCreated];
-[BLSHLocalHostSceneEnvironmentUpdater initWithSessionProvider:localHostEnvironment:osTimerProvider:];
-[BLSHLocalHostSceneEnvironmentUpdater onMain_ensureInactiveEnvSessionCreated];
-[BLSHLocalHostSceneEnvironmentUpdater performBlockWithSubhostedEnvironments:];
-[BLSHLocalHostSceneEnvironmentUpdater performWithSubhostedEnvironmentsFromPresentationEntries:block:];
-[BLSHLocalHostSceneEnvironmentUpdater resetAllLocalHostBudgetsForReason:];
-[BLSHLocalHostSceneEnvironmentUpdater subHostedHostEnvironments];
-[BLSHLocalHostSceneEnvironmentUpdater timelinesForDateInterval:previousPresentationDate:localHostEnvironment:shouldReset:completion:];
```

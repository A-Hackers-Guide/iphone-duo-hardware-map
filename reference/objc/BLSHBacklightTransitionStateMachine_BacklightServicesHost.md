# `BLSHBacklightTransitionStateMachine`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightInactiveEnvironmentSessionUpdating`, `BLSHBacklightDisplayStateMachineDelegate`, `BLSHBacklightEnvironmentStateMachineDelegate`, `BLSHDisplayFlipbookStateProvider`, `BLSHDisableFlipbookProvider`, `BLSHBacklightSceneHostEnvironmentObserver`, `BLSHHostEnvironmentAmendSceneSettingsDelegate`, `BLSHAlwaysOnPresentationEngineDelegate`, `BLSHGlobalUnrestrictedFramerateProvider`, `BLSHGlobalHighLuminanceAlwaysOnProvider`, `BLSHGlobalCacheFlipbookOnDisplayWakeProvider`, `BLSHBacklightStateMachineEventPerforming`, `BLSHWatchdogDelegate`, `BLSFlipbookDiagnosticsProviding`
- 48 instance variables, 31 properties, 65 instance methods, 0 class methods

## Instance variables

```
@"<BLSHOSDisplayInterfaceProviding>" _display;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BLSHInactiveBudgetPolicing_Private>" _inactiveBudgetPolicy;
@"<BLSHOSInterfaceProviding>" _osInterfaceProvider;
@"BLSHBacklightEnvironmentStateMachine" _environmentStateMachine;
@"BLSHAlwaysOnPresentationEngine" _alwaysOnPresentationEngine;
@"<BLSHWatchdogInvalidatable>" _onMain_watchdogTimer;
@"BLSAssertion" _touchLockAssertion;
@"<BLSHBacklightHostObserving>" _lock_performerDelegate;
q _lock_backlightState;
Q _backlightStateChangeTimestamp;
@"<BLSHSystemActivityAsserting>" _transitionAPAwakeAssertion;
@"<BLSHResourceArbitrating>" _flipbookArbiter;
@"<BLSHResourceOwning>" _lock_flipbookToken;
@"<BLSDisplayPowerResourceHint>" _powerResourceHint;
@"BLSHPresentationDateSpecifier" _lock_stopEngineOnScreenSpecifier;
@"<BLSHPendingOperation>" _lock_pendingEnvironmentUpdate;
@"BLSHPendingUpdatePresentation" _lock_pendingUpdatePresentation;
@"BLSHPendingUpdateToSpecifier" _lock_pendingUpdateToSpecifier;
@"BLSHPendingUpdateDisplayMode" _lock_pendingUpdateDisplayMode;
@"BLSHEnsureFlipbookCurrentOperation" _lock_ensureFlipbookCurrentOperation;
@"BLSHBacklightInactiveEnvironmentSession" _lock_session;
@"BLSHBacklightAggregateState" _currentState;
@"BLSHBacklightMutableTargetState" _lock_targetState;
@"BLSBacklightChangeEvent" _pendingPrewarmedEvent;
@"NSMutableArray" _lock_queuedEventsToPerform;
@"NSMutableArray" _lock_activeEvents;
@"NSMutableArray" _lock_abortedEvents;
Q _stateHandler;
@"NSString" _displayLoggingName;
q _lastSteadyStateFlipbookState;
q _lock_settledBacklightState;
q _lock_lastNotifiedTargetDisplayMode;
q _lock_lastNotifiedCompletedDisplayMode;
B _flipbookSupported;
B _lock_didNotifyDisplayModeTransitionStartedButNotCompleted;
B _lock_forcedUnanimated;
B _lock_animating;
B _lock_globalCacheFlipbook;
B _lock_cacheFlipbook;
B _lock_flipbookIsStale;
B _lock_alwaysOnSuppressed;
B _lock_globalUnrestrictedFramerate;
B _lock_globalHighLuminanceAlwaysOn;
B _lock_flipbookDisabled;
B _lock_safeToUnblank;
@"<BLSHBacklightPlatformProvider>" _platformProvider;
@"BLSHBacklightDisplayStateMachine" _displayStateMachine;
```

## Properties

```
@property (T@"BLSHAlwaysOnPresentationEngine",R,N,V_alwaysOnPresentationEngine) alwaysOnPresentationEngine;
@property (Tq,R,N) backlightState;
@property (TB,R,N,GisTransitioning) transitioning;
@property (T@"BLSHBacklightInactiveEnvironmentSession",R,N) session;
@property (T@"<BLSHBacklightPlatformProvider>",R,N,V_platformProvider) platformProvider;
@property (T@"BLSHBacklightDisplayStateMachine",R,N,V_displayStateMachine) displayStateMachine;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) delegateLoggingName;
@property (TB,R,N,GisFlipbook) flipbook;
@property (TB,R,N,GflipbookUsesLowPowerRendering) flipbookUsesLowPowerRendering;
@property (TB,N,GisFlipbookDisabled) flipbookDisabled;
@property (T@"<BLSDisplay>",R,N) display;
@property (TB,N,GisGlobalUnrestrictedFramerate) globalUnrestrictedFramerate;
@property (TB,N,GisGlobalHighLuminanceAlwaysOn) globalHighLuminanceAlwaysOn;
@property (TB,N) globalCacheFlipbookOnDisplayWake;
@property (TQ,R,N) backlightStateChangeTimestamp;
@property (T@"NSString",R,C,N) backlightStateDescription;
@property (T@"<BLSHBacklightHostObserving>",W,N) performerDelegate;
@property (TB,N) safeToUnblank;
@property (TB,N,GisAlwaysOnSuppressed) alwaysOnSuppressed;
@property (Tq,R,N) settledBacklightState;
@property (Tq,R,N) targetBacklightDisplayMode;
@property (Tq,R,N) backlightDisplayMode;
@property (Tq,R,N) flipbookState;
@property (TB,R,N,GisAlwaysOnEnabled) alwaysOnEnabled;
@property (TB,R,N) deviceSupportsAlwaysOn;
@property (Td,?,N,SsetCBTransitionsDelayForTesting:) cbTransitionsDelayForTesting;
@property (Td,?,N,SsetCATransitionsDelayForTesting:) caTransitionsDelayForTesting;
```

## Instance methods

```
-[BLSHBacklightTransitionStateMachine flipbookUsesLowPowerRendering];
-[BLSHBacklightTransitionStateMachine frameOnGlassWhenFlipbookLastCancelled];
-[BLSHBacklightTransitionStateMachine display];
-[BLSHBacklightTransitionStateMachine environmentStateMachine:didUpdateToPresentation:];
-[BLSHBacklightTransitionStateMachine registerHandlersForService:];
-[BLSHBacklightTransitionStateMachine deviceSupportsAlwaysOn];
-[BLSHBacklightTransitionStateMachine prewarmEvent:];
-[BLSHBacklightTransitionStateMachine backlightStateChangeTimestamp];
-[BLSHBacklightTransitionStateMachine setGlobalHighLuminanceAlwaysOn:];
-[BLSHBacklightTransitionStateMachine isAlwaysOnEnabled];
-[BLSHBacklightTransitionStateMachine backlightDisplayMode];
-[BLSHBacklightTransitionStateMachine debugDescription];
-[BLSHBacklightTransitionStateMachine isFlipbook];
-[BLSHBacklightTransitionStateMachine identifier];
-[BLSHBacklightTransitionStateMachine removeObserver:];
-[BLSHBacklightTransitionStateMachine displayState:didUpdateToMode:];
-[BLSHBacklightTransitionStateMachine hostEnvironment:hostDidSetUnrestrictedFramerateUpdates:];
-[BLSHBacklightTransitionStateMachine presentationEngine:didInvalidateContentForEnvironment:reason:];
-[BLSHBacklightTransitionStateMachine isTransitioning];
-[BLSHBacklightTransitionStateMachine platformProvider];
-[BLSHBacklightTransitionStateMachine dealloc];
-[BLSHBacklightTransitionStateMachine flipbookState];
-[BLSHBacklightTransitionStateMachine setGlobalUnrestrictedFramerate:];
-[BLSHBacklightTransitionStateMachine delegateLoggingName];
-[BLSHBacklightTransitionStateMachine alwaysOnPresentationEngine];
-[BLSHBacklightTransitionStateMachine backlightStateDescription];
-[BLSHBacklightTransitionStateMachine setSafeToUnblank:];
-[BLSHBacklightTransitionStateMachine addObserver:];
-[BLSHBacklightTransitionStateMachine environmentStateMachine:didCompleteUpdateToState:];
-[BLSHBacklightTransitionStateMachine backlightState];
-[BLSHBacklightTransitionStateMachine initForDisplay:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:];
-[BLSHBacklightTransitionStateMachine frameWithUUID:];
-[BLSHBacklightTransitionStateMachine isGlobalHighLuminanceAlwaysOn];
-[BLSHBacklightTransitionStateMachine isGlobalUnrestrictedFramerate];
-[BLSHBacklightTransitionStateMachine performEvent:];
-[BLSHBacklightTransitionStateMachine performerDelegate];
-[BLSHBacklightTransitionStateMachine hostEnvironment:didAmendSceneSettings:];
-[BLSHBacklightTransitionStateMachine setFlipbookDisabled:];
-[BLSHBacklightTransitionStateMachine frameOnGlassNow];
-[BLSHBacklightTransitionStateMachine hostEnvironment:hostDidSetAlwaysOnEnabledForEnvironment:];
-[BLSHBacklightTransitionStateMachine settledBacklightState];
-[BLSHBacklightTransitionStateMachine abortContextForTimer:];
-[BLSHBacklightTransitionStateMachine isFlipbookDisabled];
-[BLSHBacklightTransitionStateMachine setAlwaysOnSuppressed:];
-[BLSHBacklightTransitionStateMachine targetBacklightDisplayMode];
-[BLSHBacklightTransitionStateMachine hostEnvironment:hostDidSetHighLuminanceAlwaysOn:];
-[BLSHBacklightTransitionStateMachine description];
-[BLSHBacklightTransitionStateMachine environmentStateMachine:didBeginUpdateToState:];
-[BLSHBacklightTransitionStateMachine hasEnsureFlipbookCurrent];
-[BLSHBacklightTransitionStateMachine presentationEngine:didUpdateToCurrentWithSpecifier:];
-[BLSHBacklightTransitionStateMachine environmentStateMachine:didUpdateFlipbookVisualState:specifier:];
-[BLSHBacklightTransitionStateMachine setGlobalCacheFlipbookOnDisplayWake:];
-[BLSHBacklightTransitionStateMachine displayStateMachine];
-[BLSHBacklightTransitionStateMachine session];
-[BLSHBacklightTransitionStateMachine inactiveEnvironmentSession:updateToPresentation:];
-[BLSHBacklightTransitionStateMachine isAlwaysOnSuppressed];
-[BLSHBacklightTransitionStateMachine osInterfaceProvider];
-[BLSHBacklightTransitionStateMachine hostEnvironment:hostDidSetLiveUpdating:];
-[BLSHBacklightTransitionStateMachine allFlipbookFrames];
-[BLSHBacklightTransitionStateMachine displayState:isUpdatingToBrightnessCurve:withDuration:];
-[BLSHBacklightTransitionStateMachine globalCacheFlipbookOnDisplayWake];
-[BLSHBacklightTransitionStateMachine hostEnvironment:hostDidSetCacheFlipbookOnDisplayWake:];
-[BLSHBacklightTransitionStateMachine environmentStateMachine:didUpdateToSpecifier:];
-[BLSHBacklightTransitionStateMachine safeToUnblank];
-[BLSHBacklightTransitionStateMachine setPerformerDelegate:];
```

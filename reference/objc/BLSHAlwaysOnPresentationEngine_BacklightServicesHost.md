# `BLSHAlwaysOnPresentationEngine`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHEngineRequestDatesOperationDelegate`, `BLSHEngineRenderFlipbookSessionDelegate`, `BLSHBacklightInactiveEnvironmentSessionObserving`, `BLSHOnSystemSleepActionDelegate`, `BLSHAlwaysFillFlipbookProvider`, `BLSHPseudoFlipbookProvider`, `BLSHGlobal1HzFlipbookProvider`, `BLSHDisableLowPowerRenderingProvider`, `BLSHFlipbookPowerSavingProviding`, `BLSHBacklightSceneHostEnvironmentObserver`, `BLSFlipbookDiagnosticsProviding`
- 48 instance variables, 17 properties, 55 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BLSHOSDisplayInterfaceProviding>" _display;
@"NSString" _displayLoggingName;
@"<BLSHAlwaysOnPresentationEngineDelegate>" _delegate;
@"<BLSHOSInterfaceProviding>" _osInterfaceProvider;
@"BLSHEngineEnvironmentObserverHelper" _environmentObserverHelper;
@"<BLSHInactiveBudgetPolicing_Private>" _inactiveBudgetPolicy;
@"<BLSHInactiveBudgetPolicing_Private>" _realInactiveBudgetPolicy;
@"<BLSHInactiveBudgetPolicing_Private>" _nullInactiveBudgetPolicy;
@"<BLSHFlipbookTelemetry>" _flipbookTelemetryDelegate;
@"BLSHOnSystemSleepAction" _sleepAction;
@? _lock_sleepActionCompletion;
@"BLSHFlipbookSpecification" _flipbookSpecification;
@"<BLSHFlipbook>" _lock_flipbook;
@"<BLSHRenderedFlipbookFrame>" _lock_frameOnGlassWhenFlipbookLastCancelledAndReset;
@"<BLSHRenderedFlipbookFrame>" _lock_frameOnGlassWhenFlipbookCancelled;
@"BLSHFlipbookPowerSavingProvider" _flipbookPowerSavingProvider;
@"BLSHFlipbookHistory" _renderedFlipbookHistory;
@"BLSHFlipbookWatchdog" _flipbookWatchdog;
@"BLSHDateSpecifierModel" _lock_presentationDatesModel;
@"BLSHBacklightInactiveEnvironmentSession" _lock_inactiveSession;
@"BLSHEngineRequestDatesOperation" _lock_requestDatesOperation;
@"BLSHPresentationDateSpecifier" _lock_lastLiveSpecifier;
@"NSDateInterval" _lock_lastRequestInterval;
@"BLSHPresentationUpdates" _lock_cachedFlipbookUpdates;
@"BLSHPresentationDateSpecifier" _lock_preparingToRenderSpecifier;
@"BLSHPresentationDateSpecifier" _lock_renderingSpecifier;
@"BLSHEngineRenderFlipbookSession" _lock_renderFlipbookSession;
@"<BLSHPreventSystemSleepAsserting>" _lock_renderFlipbookSessionPowerAssertion;
@"<BLSHPreventSystemSleepAsserting>" _lock_livePowerAssertion;
@"<BSTimerScheduleQuerying><BSInvalidatable>" _lock_timer;
@"NSDate" _lock_serviceNextUpdatesStart;
Q _stateHandler;
Q _lock_renderingSpecifier_backoffTime;
q _lock_engineState;
q _lock_fillFlipbookState;
d _lock_sleepRequestedTime;
B _lock_shouldNotifyFlipbookCurrent;
B _lock_onStandby;
B _lock_suppressed;
B _lock_requestDatesOperationDidTimeout;
B _lock_alwaysFillFlipbook;
B _lock_usePseudoFlipbook;
B _lock_global1HzFlipbook;
B _lock_1HzFlipbook;
B _lock_flipbookUsesLowPowerRendering;
B _lock_lowPowerRenderingDisabled;
B _lock_cacheFlipbook;
```

## Properties

```
@property (Tq,R,N) engineState;
@property (TB,R,N,GisSuppressed) suppressed;
@property (T@"<BLSHRenderedFlipbookFrame>",R,N) onGlassFlipbookFrame;
@property (TB,N,GisOnStandby) onStandby;
@property (TB,N) alwaysFillFlipbook;
@property (TB,N) cacheFlipbook;
@property (T@"BLSHBacklightInactiveEnvironmentSession",&,N) inactiveSession;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N,GisUsingPseudoFlipbook) usePseudoFlipbook;
@property (TB,R,N,GflipbookUsesLowPowerRendering) flipbookUsesLowPowerRendering;
@property (TB,R,N,GisFlipbookPowerSavingEnabled) flipbookPowerSavingEnabled;
@property (T@"<BLSDisplay>",R,N) display;
@property (TB,N,GisGlobal1HzFlipbook) global1HzFlipbook;
@property (TB,N,GisLowPowerRenderingDisabled) lowPowerRenderingDisabled;
```

## Instance methods

```
-[BLSHAlwaysOnPresentationEngine isSuppressed];
-[BLSHAlwaysOnPresentationEngine startLiveUpdates];
-[BLSHAlwaysOnPresentationEngine didEndInactiveEnvironmentSession:];
-[BLSHAlwaysOnPresentationEngine hostEnvironment:hostDidSet1HzFlipbook:];
-[BLSHAlwaysOnPresentationEngine flipbookUsesLowPowerRendering];
-[BLSHAlwaysOnPresentationEngine frameOnGlassWhenFlipbookLastCancelled];
-[BLSHAlwaysOnPresentationEngine hostEnvironment:invalidateContentForReason:];
-[BLSHAlwaysOnPresentationEngine renderFramesSession:beganRenderingSpecifier:timedOutEnvironments:];
-[BLSHAlwaysOnPresentationEngine display];
-[BLSHAlwaysOnPresentationEngine registerHandlersForService:];
-[BLSHAlwaysOnPresentationEngine incrementDisablePowerSavingUsageCountForReason:];
-[BLSHAlwaysOnPresentationEngine isOnStandby];
-[BLSHAlwaysOnPresentationEngine isGlobal1HzFlipbook];
-[BLSHAlwaysOnPresentationEngine debugDescription];
-[BLSHAlwaysOnPresentationEngine hostEnvironment:hostDidSetUnrestrictedFramerateUpdates:];
-[BLSHAlwaysOnPresentationEngine engineState];
-[BLSHAlwaysOnPresentationEngine systemSleepAction:systemWillWakeForReason:];
-[BLSHAlwaysOnPresentationEngine dealloc];
-[BLSHAlwaysOnPresentationEngine inactiveSession];
-[BLSHAlwaysOnPresentationEngine setCacheFlipbook:];
-[BLSHAlwaysOnPresentationEngine renderFramesSession:failedToRenderSpecifier:error:timedOutEnvironments:];
-[BLSHAlwaysOnPresentationEngine setFlipbookTelemetryDelegate:];
-[BLSHAlwaysOnPresentationEngine setUsePseudoFlipbook:];
-[BLSHAlwaysOnPresentationEngine setGlobal1HzFlipbook:];
-[BLSHAlwaysOnPresentationEngine frameWithUUID:];
-[BLSHAlwaysOnPresentationEngine requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:];
-[BLSHAlwaysOnPresentationEngine isFlipbookPowerSavingEnabled];
-[BLSHAlwaysOnPresentationEngine frameOnGlassNow];
-[BLSHAlwaysOnPresentationEngine hostEnvironment:hostDidSetAlwaysOnEnabledForEnvironment:];
-[BLSHAlwaysOnPresentationEngine suppressForReason:];
-[BLSHAlwaysOnPresentationEngine setOnStandby:];
-[BLSHAlwaysOnPresentationEngine flipbook];
-[BLSHAlwaysOnPresentationEngine stopForReason:];
-[BLSHAlwaysOnPresentationEngine description];
-[BLSHAlwaysOnPresentationEngine inactiveEnvironmentSession:didUpdateToPresentation:];
-[BLSHAlwaysOnPresentationEngine decrementDisablePowerSavingUsageCountForReason:];
-[BLSHAlwaysOnPresentationEngine requestDatesOperation:didTimeoutPendingEnvironments:];
-[BLSHAlwaysOnPresentationEngine setAlwaysFillFlipbook:];
-[BLSHAlwaysOnPresentationEngine cacheFlipbook];
-[BLSHAlwaysOnPresentationEngine setInactiveSession:];
-[BLSHAlwaysOnPresentationEngine initForDisplay:delegate:platformProvider:osInterfaceProvider:inactiveBudgetPolicy:];
-[BLSHAlwaysOnPresentationEngine alwaysFillFlipbook];
-[BLSHAlwaysOnPresentationEngine purgeFlipbook];
-[BLSHAlwaysOnPresentationEngine inactiveEnvironmentSession:willUpdateToPresentation:];
-[BLSHAlwaysOnPresentationEngine isUsingPseudoFlipbook];
-[BLSHAlwaysOnPresentationEngine onGlassFlipbookFrame];
-[BLSHAlwaysOnPresentationEngine systemSleepAction:performWithCompletion:];
-[BLSHAlwaysOnPresentationEngine startFlipbookAndEnsureCurrent];
-[BLSHAlwaysOnPresentationEngine suspendForReason:];
-[BLSHAlwaysOnPresentationEngine hostEnvironment:hostDidSetLowPowerRenderingRequested:];
-[BLSHAlwaysOnPresentationEngine allFlipbookFrames];
-[BLSHAlwaysOnPresentationEngine isLowPowerRenderingDisabled];
-[BLSHAlwaysOnPresentationEngine invalidateOnGlassFlipbookFrame];
-[BLSHAlwaysOnPresentationEngine setLowPowerRenderingDisabled:];
-[BLSHAlwaysOnPresentationEngine renderFramesSession:didRenderFrame:timedOutEnvironments:];
```

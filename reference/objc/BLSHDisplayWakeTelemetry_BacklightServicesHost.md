# `BLSHDisplayWakeTelemetry`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightHostTelemetryDelegate`, `BLSHDisableCommitOnWakeMeasurementProvider`
- 15 instance variables, 5 properties, 24 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BLSHPendingBacklightTelemetryEvent" _pendingBacklightTelemetryEvent;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _pendingBacklightTelemetryEventLock;
@"NSString" _faceDescription;
@"NSArray" _complicationDescriptions;
@"NSMutableDictionary" _lock_pendingWakeTelemetryTrackers;
@"BLSHBacklightWakeTelemetryTracker" _lock_activeWakeTelemetryTracker;
B _lock_commitOnWakeMeasurementDisabled;
@"<BLSHTelemetryServicePlatformDelegate>" _platformDelegate;
{?="hasBacklightEventMethod"B"hasBacklightEventTelemetryEnabledMethod"B"hasBacklightEventPowerLogPayloadMethod"B} _delegateFlags;
@"<BLSHBacklightHostTelemetrySource>" _telemetrySource;
@"<BLSHTelemetryServiceSending>" _telemetryService;
@"NSString" _displayIdentifier;
i _surfaceType;
B _backlightEventTelemetryEnabled;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,GisCommitOnWakeMeasurementDisabled) commitOnWakeMeasurementDisabled;
```

## Instance methods

```
-[BLSHDisplayWakeTelemetry backlightTelemetrySource:willUpdateDisplayForState:forEvent:];
-[BLSHDisplayWakeTelemetry startObserving];
-[BLSHDisplayWakeTelemetry backlightTelemetrySource:didAcquireSystemActivityWithError:isActive:details:forEvent:];
-[BLSHDisplayWakeTelemetry backlightTelemetrySource:hadExistingSystemActivityForEvent:];
-[BLSHDisplayWakeTelemetry backlightTelemetrySource:didCompleteUpdateToFlipbookState:forEvent:];
-[BLSHDisplayWakeTelemetry setPlatformDelegate:];
-[BLSHDisplayWakeTelemetry backlightTelemetrySource:didCompleteUpdateToState:forEvents:abortedEvents:];
-[BLSHDisplayWakeTelemetry backlightTelemetrySource:didUnblankToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:];
-[BLSHDisplayWakeTelemetry backlightTelemetrySource:didUpdateVisualContentsToBeginTransitionToState:forEvents:abortedEvents:];
-[BLSHDisplayWakeTelemetry backlightTelemetrySource:willPerformEvent:];
-[BLSHDisplayWakeTelemetry _commonInitWithTelemetrySource:telemetryService:];
-[BLSHDisplayWakeTelemetry _donateBacklightStateChangeForState:startMachTime:endMachTime:changeEvent:];
-[BLSHDisplayWakeTelemetry _eventNameForBacklightState:];
-[BLSHDisplayWakeTelemetry _handleBacklightDidCompleteUpdateToState:updateTime:originatingTime:forEvents:abortedEvents:];
-[BLSHDisplayWakeTelemetry _handleBacklightNewState:sourceEvent:explanation:startedAtContinuousTime:];
-[BLSHDisplayWakeTelemetry _handleBacklightNewState:sourceEvent:explanation:startedAtContinuousTime:changeEvent:];
-[BLSHDisplayWakeTelemetry _handleBacklightNewState:startedAtContinuousTime:event:];
-[BLSHDisplayWakeTelemetry _logAbortedEventsAnalytics:context:targetState:];
-[BLSHDisplayWakeTelemetry _logBacklightTelemetryEventForPendingEvent:duration:endTimestamp:];
-[BLSHDisplayWakeTelemetry initWithPlatformDelegate:];
-[BLSHDisplayWakeTelemetry initWithPlatformDelegate:telemetrySource:];
-[BLSHDisplayWakeTelemetry initWithPlatformDelegate:telemetrySource:telemetryService:];
-[BLSHDisplayWakeTelemetry isCommitOnWakeMeasurementDisabled];
-[BLSHDisplayWakeTelemetry setCommitOnWakeMeasurementDisabled:];
```

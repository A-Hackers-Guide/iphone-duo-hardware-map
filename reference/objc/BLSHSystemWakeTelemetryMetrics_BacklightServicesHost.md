# `BLSHSystemWakeTelemetryMetrics`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHSystemWakeTelemetryMetricsReading`
- 40 instance variables, 44 properties, 81 instance methods, 0 class methods

## Instance variables

```
I _displayOnCount;
I _displayOffCount;
I _enteringAOTCount;
I _changedSettingsWhileOffCount;
I _wakeCount;
I _sleepOver2mCount;
I _sleepOver3mCount;
I _sleepOver4mCount;
I _sleepOver5mCount;
I _sleepOver6mCount;
I _sleepCount;
I _possibleCount;
I _confirmedPossibleCount;
I _rejectedPossibleCount;
I _expiredPossibleCount;
I _noTimeSetCount;
I _rtcAlarmsCount;
I _softwareRequestCount;
I _invalidatedFramesUpTo2mStale;
I _invalidatedFramesUpTo3mStale;
I _invalidatedFramesUpTo4mStale;
I _invalidatedFramesUpTo5mStale;
I _invalidatedFramesUpTo6mStale;
I _discardedFramesUpTo2mStale;
I _discardedFramesUpTo3mStale;
I _discardedFramesUpTo4mStale;
I _discardedFramesUpTo5mStale;
I _discardedFramesUpTo6mStale;
I _renderedFrameCount;
I _renderedPartialMinuteCount;
Q _startContinuousSeconds;
Q _endContinuousSeconds;
d _secondsDisplayOn;
d _secondsDisplayOff;
d _secondsShowingAOT;
d _totalTimeSeconds;
Q _renderedPresentationSeconds;
d _flipbookLayoutSeconds;
d _flipbookRenderSeconds;
@"NSDictionary" _platformContext;
```

## Properties

```
@property (TQ,N,V_startContinuousSeconds) startContinuousSeconds;
@property (TQ,N,V_endContinuousSeconds) endContinuousSeconds;
@property (TI,N,V_displayOnCount) displayOnCount;
@property (Td,N,V_secondsDisplayOn) secondsDisplayOn;
@property (TI,N,V_displayOffCount) displayOffCount;
@property (Td,N,V_secondsDisplayOff) secondsDisplayOff;
@property (TI,N,V_enteringAOTCount) enteringAOTCount;
@property (Td,N,V_secondsShowingAOT) secondsShowingAOT;
@property (TI,N,V_changedSettingsWhileOffCount) changedSettingsWhileOffCount;
@property (TI,N,V_wakeCount) wakeCount;
@property (Td,N,V_totalTimeSeconds) totalTimeSeconds;
@property (TI,N,V_sleepOver2mCount) sleepOver2mCount;
@property (TI,N,V_sleepOver3mCount) sleepOver3mCount;
@property (TI,N,V_sleepOver4mCount) sleepOver4mCount;
@property (TI,N,V_sleepOver5mCount) sleepOver5mCount;
@property (TI,N,V_sleepOver6mCount) sleepOver6mCount;
@property (TI,N,V_sleepCount) sleepCount;
@property (TI,N,V_possibleCount) possibleCount;
@property (TI,N,V_confirmedPossibleCount) confirmedPossibleCount;
@property (TI,N,V_rejectedPossibleCount) rejectedPossibleCount;
@property (TI,N,V_expiredPossibleCount) expiredPossibleCount;
@property (TI,N,V_noTimeSetCount) noTimeSetCount;
@property (TI,N,V_rtcAlarmsCount) rtcAlarmsCount;
@property (TI,N,V_softwareRequestCount) softwareRequestCount;
@property (TI,N,V_invalidatedFramesUpTo2mStale) invalidatedFramesUpTo2mStale;
@property (TI,N,V_invalidatedFramesUpTo3mStale) invalidatedFramesUpTo3mStale;
@property (TI,N,V_invalidatedFramesUpTo4mStale) invalidatedFramesUpTo4mStale;
@property (TI,N,V_invalidatedFramesUpTo5mStale) invalidatedFramesUpTo5mStale;
@property (TI,N,V_invalidatedFramesUpTo6mStale) invalidatedFramesUpTo6mStale;
@property (TI,N,V_discardedFramesUpTo2mStale) discardedFramesUpTo2mStale;
@property (TI,N,V_discardedFramesUpTo3mStale) discardedFramesUpTo3mStale;
@property (TI,N,V_discardedFramesUpTo4mStale) discardedFramesUpTo4mStale;
@property (TI,N,V_discardedFramesUpTo5mStale) discardedFramesUpTo5mStale;
@property (TI,N,V_discardedFramesUpTo6mStale) discardedFramesUpTo6mStale;
@property (TI,N,V_renderedFrameCount) renderedFrameCount;
@property (TI,N,V_renderedPartialMinuteCount) renderedPartialMinuteCount;
@property (TQ,N,V_renderedPresentationSeconds) renderedPresentationSeconds;
@property (Td,N,V_flipbookLayoutSeconds) flipbookLayoutSeconds;
@property (Td,N,V_flipbookRenderSeconds) flipbookRenderSeconds;
@property (T@"NSDictionary",C,N,V_platformContext) platformContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHSystemWakeTelemetryMetrics sleepOver5mCount];
-[BLSHSystemWakeTelemetryMetrics setEnteringAOTCount:];
-[BLSHSystemWakeTelemetryMetrics setDiscardedFramesUpTo3mStale:];
-[BLSHSystemWakeTelemetryMetrics setDiscardedFramesUpTo2mStale:];
-[BLSHSystemWakeTelemetryMetrics setDiscardedFramesUpTo6mStale:];
-[BLSHSystemWakeTelemetryMetrics invalidatedFramesUpTo5mStale];
-[BLSHSystemWakeTelemetryMetrics setDiscardedFramesUpTo4mStale:];
-[BLSHSystemWakeTelemetryMetrics serializedPayload];
-[BLSHSystemWakeTelemetryMetrics wakeCount];
-[BLSHSystemWakeTelemetryMetrics enteringAOTCount];
-[BLSHSystemWakeTelemetryMetrics setRenderedFrameCount:];
-[BLSHSystemWakeTelemetryMetrics discardedFramesUpTo3mStale];
-[BLSHSystemWakeTelemetryMetrics setRenderedPartialMinuteCount:];
-[BLSHSystemWakeTelemetryMetrics setInvalidatedFramesUpTo6mStale:];
-[BLSHSystemWakeTelemetryMetrics setDiscardedFramesUpTo5mStale:];
-[BLSHSystemWakeTelemetryMetrics setSecondsShowingAOT:];
-[BLSHSystemWakeTelemetryMetrics sleepOver4mCount];
-[BLSHSystemWakeTelemetryMetrics setRtcAlarmsCount:];
-[BLSHSystemWakeTelemetryMetrics discardedFramesUpTo4mStale];
-[BLSHSystemWakeTelemetryMetrics noTimeSetCount];
-[BLSHSystemWakeTelemetryMetrics setEndContinuousSeconds:];
-[BLSHSystemWakeTelemetryMetrics flipbookLayoutSeconds];
-[BLSHSystemWakeTelemetryMetrics startContinuousSeconds];
-[BLSHSystemWakeTelemetryMetrics setSleepCount:];
-[BLSHSystemWakeTelemetryMetrics setInvalidatedFramesUpTo2mStale:];
-[BLSHSystemWakeTelemetryMetrics displayOffCount];
-[BLSHSystemWakeTelemetryMetrics invalidatedFramesUpTo2mStale];
-[BLSHSystemWakeTelemetryMetrics setRejectedPossibleCount:];
-[BLSHSystemWakeTelemetryMetrics sleepOver6mCount];
-[BLSHSystemWakeTelemetryMetrics totalTimeSeconds];
-[BLSHSystemWakeTelemetryMetrics discardedFramesUpTo6mStale];
-[BLSHSystemWakeTelemetryMetrics discardedFramesUpTo5mStale];
-[BLSHSystemWakeTelemetryMetrics confirmedPossibleCount];
-[BLSHSystemWakeTelemetryMetrics setSleepOver4mCount:];
-[BLSHSystemWakeTelemetryMetrics setInvalidatedFramesUpTo5mStale:];
-[BLSHSystemWakeTelemetryMetrics setDisplayOnCount:];
-[BLSHSystemWakeTelemetryMetrics flipbookRenderSeconds];
-[BLSHSystemWakeTelemetryMetrics setPlatformContext:];
-[BLSHSystemWakeTelemetryMetrics setSoftwareRequestCount:];
-[BLSHSystemWakeTelemetryMetrics expiredPossibleCount];
-[BLSHSystemWakeTelemetryMetrics invalidatedFramesUpTo3mStale];
-[BLSHSystemWakeTelemetryMetrics displayOnCount];
-[BLSHSystemWakeTelemetryMetrics setStartContinuousSeconds:];
-[BLSHSystemWakeTelemetryMetrics platformContext];
-[BLSHSystemWakeTelemetryMetrics setSleepOver5mCount:];
-[BLSHSystemWakeTelemetryMetrics setInvalidatedFramesUpTo3mStale:];
-[BLSHSystemWakeTelemetryMetrics setTotalTimeSeconds:];
-[BLSHSystemWakeTelemetryMetrics setPossibleCount:];
-[BLSHSystemWakeTelemetryMetrics setExpiredPossibleCount:];
-[BLSHSystemWakeTelemetryMetrics renderedFrameCount];
-[BLSHSystemWakeTelemetryMetrics setRenderedPresentationSeconds:];
-[BLSHSystemWakeTelemetryMetrics setFlipbookLayoutSeconds:];
-[BLSHSystemWakeTelemetryMetrics rtcAlarmsCount];
-[BLSHSystemWakeTelemetryMetrics setSecondsDisplayOff:];
-[BLSHSystemWakeTelemetryMetrics invalidatedFramesUpTo4mStale];
-[BLSHSystemWakeTelemetryMetrics secondsDisplayOn];
-[BLSHSystemWakeTelemetryMetrics softwareRequestCount];
-[BLSHSystemWakeTelemetryMetrics sleepOver3mCount];
-[BLSHSystemWakeTelemetryMetrics setSleepOver2mCount:];
-[BLSHSystemWakeTelemetryMetrics setNoTimeSetCount:];
-[BLSHSystemWakeTelemetryMetrics changedSettingsWhileOffCount];
-[BLSHSystemWakeTelemetryMetrics rejectedPossibleCount];
-[BLSHSystemWakeTelemetryMetrics setInvalidatedFramesUpTo4mStale:];
-[BLSHSystemWakeTelemetryMetrics setSleepOver6mCount:];
-[BLSHSystemWakeTelemetryMetrics endContinuousSeconds];
-[BLSHSystemWakeTelemetryMetrics renderedPartialMinuteCount];
-[BLSHSystemWakeTelemetryMetrics renderedPresentationSeconds];
-[BLSHSystemWakeTelemetryMetrics secondsDisplayOff];
-[BLSHSystemWakeTelemetryMetrics possibleCount];
-[BLSHSystemWakeTelemetryMetrics sleepOver2mCount];
-[BLSHSystemWakeTelemetryMetrics setWakeCount:];
-[BLSHSystemWakeTelemetryMetrics setChangedSettingsWhileOffCount:];
-[BLSHSystemWakeTelemetryMetrics secondsShowingAOT];
-[BLSHSystemWakeTelemetryMetrics setConfirmedPossibleCount:];
-[BLSHSystemWakeTelemetryMetrics discardedFramesUpTo2mStale];
-[BLSHSystemWakeTelemetryMetrics setSecondsDisplayOn:];
-[BLSHSystemWakeTelemetryMetrics setSleepOver3mCount:];
-[BLSHSystemWakeTelemetryMetrics setFlipbookRenderSeconds:];
-[BLSHSystemWakeTelemetryMetrics setDisplayOffCount:];
-[BLSHSystemWakeTelemetryMetrics invalidatedFramesUpTo6mStale];
-[BLSHSystemWakeTelemetryMetrics sleepCount];
```

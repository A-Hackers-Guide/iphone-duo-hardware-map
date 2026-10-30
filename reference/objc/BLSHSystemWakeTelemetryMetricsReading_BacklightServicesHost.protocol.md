# `BLSHSystemWakeTelemetryMetricsReading` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 40 properties, 41 instance methods, 0 class methods

## Properties

```
@property (TQ,R,N) startContinuousSeconds;
@property (TQ,R,N) endContinuousSeconds;
@property (TI,R,N) displayOnCount;
@property (Td,R,N) secondsDisplayOn;
@property (TI,R,N) displayOffCount;
@property (Td,R,N) secondsDisplayOff;
@property (TI,R,N) enteringAOTCount;
@property (Td,R,N) secondsShowingAOT;
@property (TI,R,N) changedSettingsWhileOffCount;
@property (TI,R,N) wakeCount;
@property (Td,R,N) totalTimeSeconds;
@property (TI,R,N) sleepOver2mCount;
@property (TI,R,N) sleepOver3mCount;
@property (TI,R,N) sleepOver4mCount;
@property (TI,R,N) sleepOver5mCount;
@property (TI,R,N) sleepOver6mCount;
@property (TI,R,N) sleepCount;
@property (TI,R,N) possibleCount;
@property (TI,R,N) confirmedPossibleCount;
@property (TI,R,N) rejectedPossibleCount;
@property (TI,R,N) expiredPossibleCount;
@property (TI,R,N) noTimeSetCount;
@property (TI,R,N) rtcAlarmsCount;
@property (TI,R,N) softwareRequestCount;
@property (TI,R,N) invalidatedFramesUpTo2mStale;
@property (TI,R,N) invalidatedFramesUpTo3mStale;
@property (TI,R,N) invalidatedFramesUpTo4mStale;
@property (TI,R,N) invalidatedFramesUpTo5mStale;
@property (TI,R,N) invalidatedFramesUpTo6mStale;
@property (TI,R,N) discardedFramesUpTo2mStale;
@property (TI,R,N) discardedFramesUpTo3mStale;
@property (TI,R,N) discardedFramesUpTo4mStale;
@property (TI,R,N) discardedFramesUpTo5mStale;
@property (TI,R,N) discardedFramesUpTo6mStale;
@property (TI,R,N) renderedFrameCount;
@property (TI,R,N) renderedPartialMinuteCount;
@property (TQ,R,N) renderedPresentationSeconds;
@property (Td,R,N) flipbookLayoutSeconds;
@property (Td,R,N) flipbookRenderSeconds;
@property (T@"NSDictionary",C,N) platformContext;
```

## Instance methods

```
-[BLSHSystemWakeTelemetryMetricsReading sleepOver5mCount];
-[BLSHSystemWakeTelemetryMetricsReading invalidatedFramesUpTo5mStale];
-[BLSHSystemWakeTelemetryMetricsReading wakeCount];
-[BLSHSystemWakeTelemetryMetricsReading enteringAOTCount];
-[BLSHSystemWakeTelemetryMetricsReading discardedFramesUpTo3mStale];
-[BLSHSystemWakeTelemetryMetricsReading sleepOver4mCount];
-[BLSHSystemWakeTelemetryMetricsReading discardedFramesUpTo4mStale];
-[BLSHSystemWakeTelemetryMetricsReading noTimeSetCount];
-[BLSHSystemWakeTelemetryMetricsReading flipbookLayoutSeconds];
-[BLSHSystemWakeTelemetryMetricsReading startContinuousSeconds];
-[BLSHSystemWakeTelemetryMetricsReading displayOffCount];
-[BLSHSystemWakeTelemetryMetricsReading invalidatedFramesUpTo2mStale];
-[BLSHSystemWakeTelemetryMetricsReading sleepOver6mCount];
-[BLSHSystemWakeTelemetryMetricsReading totalTimeSeconds];
-[BLSHSystemWakeTelemetryMetricsReading discardedFramesUpTo6mStale];
-[BLSHSystemWakeTelemetryMetricsReading discardedFramesUpTo5mStale];
-[BLSHSystemWakeTelemetryMetricsReading confirmedPossibleCount];
-[BLSHSystemWakeTelemetryMetricsReading flipbookRenderSeconds];
-[BLSHSystemWakeTelemetryMetricsReading setPlatformContext:];
-[BLSHSystemWakeTelemetryMetricsReading expiredPossibleCount];
-[BLSHSystemWakeTelemetryMetricsReading invalidatedFramesUpTo3mStale];
-[BLSHSystemWakeTelemetryMetricsReading displayOnCount];
-[BLSHSystemWakeTelemetryMetricsReading platformContext];
-[BLSHSystemWakeTelemetryMetricsReading renderedFrameCount];
-[BLSHSystemWakeTelemetryMetricsReading rtcAlarmsCount];
-[BLSHSystemWakeTelemetryMetricsReading invalidatedFramesUpTo4mStale];
-[BLSHSystemWakeTelemetryMetricsReading secondsDisplayOn];
-[BLSHSystemWakeTelemetryMetricsReading softwareRequestCount];
-[BLSHSystemWakeTelemetryMetricsReading sleepOver3mCount];
-[BLSHSystemWakeTelemetryMetricsReading changedSettingsWhileOffCount];
-[BLSHSystemWakeTelemetryMetricsReading rejectedPossibleCount];
-[BLSHSystemWakeTelemetryMetricsReading endContinuousSeconds];
-[BLSHSystemWakeTelemetryMetricsReading renderedPartialMinuteCount];
-[BLSHSystemWakeTelemetryMetricsReading renderedPresentationSeconds];
-[BLSHSystemWakeTelemetryMetricsReading secondsDisplayOff];
-[BLSHSystemWakeTelemetryMetricsReading possibleCount];
-[BLSHSystemWakeTelemetryMetricsReading sleepOver2mCount];
-[BLSHSystemWakeTelemetryMetricsReading secondsShowingAOT];
-[BLSHSystemWakeTelemetryMetricsReading discardedFramesUpTo2mStale];
-[BLSHSystemWakeTelemetryMetricsReading invalidatedFramesUpTo6mStale];
-[BLSHSystemWakeTelemetryMetricsReading sleepCount];
```

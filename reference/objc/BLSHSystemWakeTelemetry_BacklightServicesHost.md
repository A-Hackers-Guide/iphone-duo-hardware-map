# `BLSHSystemWakeTelemetry`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightHostObserving`, `SWSystemSleepObserver`, `BLSBacklightStateObserving`, `BLSHFlipbookTelemetry`
- 27 instance variables, 5 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"<BLSHTelemetryServicePlatformDelegate>" _platformDelegate;
@"<BLSHBacklightHostObservable>" _backlightHost;
@"<BLSHOSInterfaceProviding>" _osInterfaceProvider;
@"<BLSHTelemetryServiceSending>" _telemetryService;
@"<BLSHSystemSleepMonitoring>" _systemSleepObserver;
{IOPMAOTMetrics="sleepCount"I"possibleCount"I"confirmedPossibleCount"I"rejectedPossibleCount"I"expiredPossibleCount"I"noTimeSetCount"I"rtcAlarmsCount"I"softwareRequestCount"I"totalTime"Q"kernelWakeReason"[24[64c]]"kernelSleepTime"[24Q]"kernelWakeTime"[24Q]} _accumulatedMetrics;
{?="hasSystemWakeMetricsMethod"B"hasSystemWakeMetricsPowerLogMethod"B"hasSystemWakeMetricsEventKeyMethod"B} _delegateFlags;
@"BLSHSystemWakeTelemetryMetrics" _currentMetrics;
@"NSString" _systemWakeMetricsEventKey;
B _blsTelemetryEnabled;
@"<BSTimerScheduleQuerying><BSCancellable><BSInvalidatable>" _timer;
d _accumulatedFlipbookLayoutDuration;
d _accumulatedFlipbookRenderDuration;
d _accumulatedSecondsDisplayOn;
d _accumulatedSecondsDisplayOff;
d _accumulatedSecondsShowingAOT;
Q _loggedToTelemtryAccumulateTime;
Q _lastTelemtryAccumulateTime;
Q _willSleepTime;
Q _hasPoweredOnTime;
Q _backlightOnStartTime;
Q _backlightOffStartTime;
Q _wakeNumber;
Q _completedWakeNumber;
B _serviceStarted;
B _isAOT;
AB _didFinalLog;
```

## Properties

```
@property (T@"<BLSHTelemetryServicePlatformDelegate>",W,N) platformDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHSystemWakeTelemetry defaultServiceWithDelegate:];
```

## Instance methods

```
-[BLSHSystemWakeTelemetry stopObserving];
-[BLSHSystemWakeTelemetry backlight:didUpdateToDisplayMode:fromDisplayMode:activeEvents:abortedEvents:];
-[BLSHSystemWakeTelemetry backlight:willUpdateToDisplayMode:fromDisplayMode:forEvents:abortedEvents:];
-[BLSHSystemWakeTelemetry initWithDelegate:];
-[BLSHSystemWakeTelemetry startObserving];
-[BLSHSystemWakeTelemetry init];
-[BLSHSystemWakeTelemetry dealloc];
-[BLSHSystemWakeTelemetry logTelemetryForRenderSession:];
-[BLSHSystemWakeTelemetry logTelemetryForRequestDates:];
-[BLSHSystemWakeTelemetry logTelemetryForInvalidation:];
-[BLSHSystemWakeTelemetry backlight:didChangeAlwaysOnEnabled:];
-[BLSHSystemWakeTelemetry setPlatformDelegate:];
-[BLSHSystemWakeTelemetry platformDelegate];
-[BLSHSystemWakeTelemetry observesUpdateToDisplayMode];
-[BLSHSystemWakeTelemetry _commonInitWithBacklightHost:osInterfaceProvider:telemetryService:];
-[BLSHSystemWakeTelemetry _resetAccumulatedMetrics];
-[BLSHSystemWakeTelemetry _scheduleMetricsTimer];
-[BLSHSystemWakeTelemetry accumulateMetrics:];
-[BLSHSystemWakeTelemetry accumulateOffDuration:isAOT:];
-[BLSHSystemWakeTelemetry accumulateOnDuration:];
-[BLSHSystemWakeTelemetry gatherTelemetryForWakeNumber:];
-[BLSHSystemWakeTelemetry initWithPlatformDelegate:backlightHost:osInterfaceProvider:telemetryService:];
-[BLSHSystemWakeTelemetry logMetricsTimerFired];
```

# `BLSHBacklightEventMetrics`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightEventMetricsReading`
- 25 instance variables, 29 properties, 52 instance methods, 0 class methods

## Instance variables

```
B _wasInactiveOn;
B _beforeKernelWake;
B _didTimeoutSystemActivity;
B _timeoutTriggeredBlackFlash;
B _systemActivityAcquisitionSuccess;
B _systemActivityAcquisitionSkipped;
i _performEventCount;
i _completedEventsCount;
i _abortedEventsCount;
q _eventType;
d _durationSeconds;
@"NSString" _sourceEvent;
@"NSNumber" _sourceEventValue;
@"NSString" _explanation;
@"NSString" _wakeReason;
@"NSString" _endpoint;
d _secondsAfterKernelWake;
Q _pageinDiff;
Q _compressionsDiff;
d _allEventsToWakeDurationSeconds;
d _didCompleteDurationSeconds;
d _systemActivityAcquisitionSeconds;
@"<SWSystemActivityAcquisitionDetails>" _systemActivityAcquisitionDetails;
@"NSString" _displayIdentifier;
@"NSDictionary" _platformContext;
```

## Properties

```
@property (Tq,N,V_eventType) eventType;
@property (Td,N,V_durationSeconds) durationSeconds;
@property (T@"NSString",C,N,V_sourceEvent) sourceEvent;
@property (T@"NSNumber",C,N,V_sourceEventValue) sourceEventValue;
@property (T@"NSString",C,N,V_explanation) explanation;
@property (T@"NSString",C,N,V_wakeReason) wakeReason;
@property (TB,N,V_wasInactiveOn) wasInactiveOn;
@property (T@"NSString",C,N,V_endpoint) endpoint;
@property (TB,N,V_beforeKernelWake) beforeKernelWake;
@property (Td,N,V_secondsAfterKernelWake) secondsAfterKernelWake;
@property (TQ,N,V_pageinDiff) pageinDiff;
@property (TQ,N,V_compressionsDiff) compressionsDiff;
@property (Ti,N,V_performEventCount) performEventCount;
@property (Ti,N,V_completedEventsCount) completedEventsCount;
@property (Ti,N,V_abortedEventsCount) abortedEventsCount;
@property (Td,N,V_allEventsToWakeDurationSeconds) allEventsToWakeDurationSeconds;
@property (Td,N,V_didCompleteDurationSeconds) didCompleteDurationSeconds;
@property (Td,N,V_systemActivityAcquisitionSeconds) systemActivityAcquisitionSeconds;
@property (TB,N,V_didTimeoutSystemActivity) didTimeoutSystemActivity;
@property (TB,N,V_timeoutTriggeredBlackFlash) timeoutTriggeredBlackFlash;
@property (TB,N,V_systemActivityAcquisitionSuccess) systemActivityAcquisitionSuccess;
@property (TB,N,V_systemActivityAcquisitionSkipped) systemActivityAcquisitionSkipped;
@property (T@"<SWSystemActivityAcquisitionDetails>",&,N,V_systemActivityAcquisitionDetails) systemActivityAcquisitionDetails;
@property (T@"NSString",C,N,V_displayIdentifier) displayIdentifier;
@property (T@"NSDictionary",C,N,V_platformContext) platformContext;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHBacklightEventMetrics eventType];
-[BLSHBacklightEventMetrics setDisplayIdentifier:];
-[BLSHBacklightEventMetrics setEndpoint:];
-[BLSHBacklightEventMetrics setEventType:];
-[BLSHBacklightEventMetrics setExplanation:];
-[BLSHBacklightEventMetrics explanation];
-[BLSHBacklightEventMetrics serializedPayload];
-[BLSHBacklightEventMetrics endpoint];
-[BLSHBacklightEventMetrics sourceEvent];
-[BLSHBacklightEventMetrics durationSeconds];
-[BLSHBacklightEventMetrics setPlatformContext:];
-[BLSHBacklightEventMetrics platformContext];
-[BLSHBacklightEventMetrics displayIdentifier];
-[BLSHBacklightEventMetrics stringForEventType:];
-[BLSHBacklightEventMetrics setWakeReason:];
-[BLSHBacklightEventMetrics wakeReason];
-[BLSHBacklightEventMetrics setSourceEvent:];
-[BLSHBacklightEventMetrics abortedEventsCount];
-[BLSHBacklightEventMetrics allEventsToWakeDurationSeconds];
-[BLSHBacklightEventMetrics beforeKernelWake];
-[BLSHBacklightEventMetrics completedEventsCount];
-[BLSHBacklightEventMetrics compressionsDiff];
-[BLSHBacklightEventMetrics didCompleteDurationSeconds];
-[BLSHBacklightEventMetrics didTimeoutSystemActivity];
-[BLSHBacklightEventMetrics pageinDiff];
-[BLSHBacklightEventMetrics performEventCount];
-[BLSHBacklightEventMetrics secondsAfterKernelWake];
-[BLSHBacklightEventMetrics setAbortedEventsCount:];
-[BLSHBacklightEventMetrics setAllEventsToWakeDurationSeconds:];
-[BLSHBacklightEventMetrics setBeforeKernelWake:];
-[BLSHBacklightEventMetrics setCompletedEventsCount:];
-[BLSHBacklightEventMetrics setCompressionsDiff:];
-[BLSHBacklightEventMetrics setDidCompleteDurationSeconds:];
-[BLSHBacklightEventMetrics setDidTimeoutSystemActivity:];
-[BLSHBacklightEventMetrics setDurationSeconds:];
-[BLSHBacklightEventMetrics setPageinDiff:];
-[BLSHBacklightEventMetrics setPerformEventCount:];
-[BLSHBacklightEventMetrics setSecondsAfterKernelWake:];
-[BLSHBacklightEventMetrics setSourceEventValue:];
-[BLSHBacklightEventMetrics setSystemActivityAcquisitionDetails:];
-[BLSHBacklightEventMetrics setSystemActivityAcquisitionSeconds:];
-[BLSHBacklightEventMetrics setSystemActivityAcquisitionSkipped:];
-[BLSHBacklightEventMetrics setSystemActivityAcquisitionSuccess:];
-[BLSHBacklightEventMetrics setTimeoutTriggeredBlackFlash:];
-[BLSHBacklightEventMetrics setWasInactiveOn:];
-[BLSHBacklightEventMetrics sourceEventValue];
-[BLSHBacklightEventMetrics systemActivityAcquisitionDetails];
-[BLSHBacklightEventMetrics systemActivityAcquisitionSeconds];
-[BLSHBacklightEventMetrics systemActivityAcquisitionSkipped];
-[BLSHBacklightEventMetrics systemActivityAcquisitionSuccess];
-[BLSHBacklightEventMetrics timeoutTriggeredBlackFlash];
-[BLSHBacklightEventMetrics wasInactiveOn];
```

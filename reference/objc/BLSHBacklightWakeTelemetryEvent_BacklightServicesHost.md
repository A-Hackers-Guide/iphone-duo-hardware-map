# `BLSHBacklightWakeTelemetryEvent`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 19 instance variables, 19 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _wasInactiveOn;
B _beforeKernelWake;
B _didTimeoutSystemActivty;
B _timeoutTriggeredBlackFlash;
B _systemActivityAcquisitionSuccess;
B _systemActivityAcquisitionSkipped;
i _performEventCount;
i _completedEventsCount;
i _abortedEventsCount;
d _wakeDurationSeconds;
Q _endpoint;
@"NSString" _wakeReason;
d _secondsAfterKernelWake;
Q _pageinDiff;
Q _compressionsDiff;
d _allEventsToWakeDurationSeconds;
d _didCompleteDurationSeconds;
d _systemActivityAcquisitionSeconds;
@"<SWSystemActivityAcquisitionDetails>" _systemActivityAcquisitionDetails;
```

## Properties

```
@property (Td,R,N,V_wakeDurationSeconds) wakeDurationSeconds;
@property (TB,R,N,V_wasInactiveOn) wasInactiveOn;
@property (TQ,R,N,V_endpoint) endpoint;
@property (T@"NSString",R,C,N,V_wakeReason) wakeReason;
@property (TB,R,N,V_beforeKernelWake) beforeKernelWake;
@property (Td,R,N,V_secondsAfterKernelWake) secondsAfterKernelWake;
@property (TQ,R,N,V_pageinDiff) pageinDiff;
@property (TQ,R,N,V_compressionsDiff) compressionsDiff;
@property (Ti,R,N,V_performEventCount) performEventCount;
@property (Ti,R,N,V_completedEventsCount) completedEventsCount;
@property (Ti,R,N,V_abortedEventsCount) abortedEventsCount;
@property (Td,R,N,V_allEventsToWakeDurationSeconds) allEventsToWakeDurationSeconds;
@property (Td,R,N,V_didCompleteDurationSeconds) didCompleteDurationSeconds;
@property (Td,R,N,V_systemActivityAcquisitionSeconds) systemActivityAcquisitionSeconds;
@property (TB,R,N,V_didTimeoutSystemActivty) didTimeoutSystemActivty;
@property (TB,R,N,V_timeoutTriggeredBlackFlash) timeoutTriggeredBlackFlash;
@property (TB,R,N,V_systemActivityAcquisitionSuccess) systemActivityAcquisitionSuccess;
@property (T@"<SWSystemActivityAcquisitionDetails>",R,N,V_systemActivityAcquisitionDetails) systemActivityAcquisitionDetails;
@property (TB,R,N,V_systemActivityAcquisitionSkipped) systemActivityAcquisitionSkipped;
```

## Instance methods

```
-[BLSHBacklightWakeTelemetryEvent endpoint];
-[BLSHBacklightWakeTelemetryEvent description];
-[BLSHBacklightWakeTelemetryEvent wakeReason];
-[BLSHBacklightWakeTelemetryEvent abortedEventsCount];
-[BLSHBacklightWakeTelemetryEvent allEventsToWakeDurationSeconds];
-[BLSHBacklightWakeTelemetryEvent beforeKernelWake];
-[BLSHBacklightWakeTelemetryEvent completedEventsCount];
-[BLSHBacklightWakeTelemetryEvent compressionsDiff];
-[BLSHBacklightWakeTelemetryEvent didCompleteDurationSeconds];
-[BLSHBacklightWakeTelemetryEvent didTimeoutSystemActivty];
-[BLSHBacklightWakeTelemetryEvent initWithWakeDurationSeconds:wasInactiveOn:endpoint:wakeReason:beforeKernelWake:secondsAfterKernelWake:pageinDiff:compressionsDiff:performEventCount:completedEventsCount:abortedEventsCount:allEventsToWakeDurationSeconds:didCompleteDurationSeconds:systemActivityAcquisitionSeconds:didTimeoutSystemActivty:timeoutTriggerdBlackFlash:systemActivityAcquisitionSuccess:systemActivityAcquisitionDetails:systemActivityAcquisitionSkipped:];
-[BLSHBacklightWakeTelemetryEvent pageinDiff];
-[BLSHBacklightWakeTelemetryEvent performEventCount];
-[BLSHBacklightWakeTelemetryEvent secondsAfterKernelWake];
-[BLSHBacklightWakeTelemetryEvent systemActivityAcquisitionDetails];
-[BLSHBacklightWakeTelemetryEvent systemActivityAcquisitionSeconds];
-[BLSHBacklightWakeTelemetryEvent systemActivityAcquisitionSkipped];
-[BLSHBacklightWakeTelemetryEvent systemActivityAcquisitionSuccess];
-[BLSHBacklightWakeTelemetryEvent timeoutTriggeredBlackFlash];
-[BLSHBacklightWakeTelemetryEvent wakeDurationSeconds];
-[BLSHBacklightWakeTelemetryEvent wasInactiveOn];
```

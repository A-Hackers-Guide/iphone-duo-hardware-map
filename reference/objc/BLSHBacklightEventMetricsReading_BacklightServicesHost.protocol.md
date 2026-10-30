# `BLSHBacklightEventMetricsReading` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 23 properties, 24 instance methods, 0 class methods

## Properties

```
@property (Tq,R,N) eventType;
@property (Td,R,N) durationSeconds;
@property (T@"NSString",R,C,N) sourceEvent;
@property (T@"NSString",R,C,N) explanation;
@property (T@"NSString",R,C,N) wakeReason;
@property (TB,R,N) wasInactiveOn;
@property (T@"NSString",R,C,N) endpoint;
@property (TB,R,N) beforeKernelWake;
@property (Td,R,N) secondsAfterKernelWake;
@property (TQ,R,N) pageinDiff;
@property (TQ,R,N) compressionsDiff;
@property (Ti,R,N) performEventCount;
@property (Ti,R,N) completedEventsCount;
@property (Ti,R,N) abortedEventsCount;
@property (Td,R,N) allEventsToWakeDurationSeconds;
@property (Td,R,N) didCompleteDurationSeconds;
@property (Td,R,N) systemActivityAcquisitionSeconds;
@property (TB,R,N) didTimeoutSystemActivity;
@property (TB,R,N) timeoutTriggeredBlackFlash;
@property (TB,R,N) systemActivityAcquisitionSuccess;
@property (TB,R,N) systemActivityAcquisitionSkipped;
@property (T@"<SWSystemActivityAcquisitionDetails>",R,N) systemActivityAcquisitionDetails;
@property (T@"NSDictionary",C,N) platformContext;
```

## Instance methods

```
-[BLSHBacklightEventMetricsReading eventType];
-[BLSHBacklightEventMetricsReading explanation];
-[BLSHBacklightEventMetricsReading endpoint];
-[BLSHBacklightEventMetricsReading sourceEvent];
-[BLSHBacklightEventMetricsReading durationSeconds];
-[BLSHBacklightEventMetricsReading setPlatformContext:];
-[BLSHBacklightEventMetricsReading platformContext];
-[BLSHBacklightEventMetricsReading wakeReason];
-[BLSHBacklightEventMetricsReading abortedEventsCount];
-[BLSHBacklightEventMetricsReading allEventsToWakeDurationSeconds];
-[BLSHBacklightEventMetricsReading beforeKernelWake];
-[BLSHBacklightEventMetricsReading completedEventsCount];
-[BLSHBacklightEventMetricsReading compressionsDiff];
-[BLSHBacklightEventMetricsReading didCompleteDurationSeconds];
-[BLSHBacklightEventMetricsReading didTimeoutSystemActivity];
-[BLSHBacklightEventMetricsReading pageinDiff];
-[BLSHBacklightEventMetricsReading performEventCount];
-[BLSHBacklightEventMetricsReading secondsAfterKernelWake];
-[BLSHBacklightEventMetricsReading systemActivityAcquisitionDetails];
-[BLSHBacklightEventMetricsReading systemActivityAcquisitionSeconds];
-[BLSHBacklightEventMetricsReading systemActivityAcquisitionSkipped];
-[BLSHBacklightEventMetricsReading systemActivityAcquisitionSuccess];
-[BLSHBacklightEventMetricsReading timeoutTriggeredBlackFlash];
-[BLSHBacklightEventMetricsReading wasInactiveOn];
```

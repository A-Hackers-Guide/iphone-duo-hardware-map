# `BLSHEngineRequestDatesOperation`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 19 instance variables, 14 properties, 17 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BLSAssertion" _lock_flipbookPowerSavingAssertion;
@"NSMutableSet" _lock_pendingEnvironments;
@"<BSTimerScheduleQuerying><BSCancellable><BSInvalidatable>" _lock_timeoutTimer;
@"<BLSHEngineRequestDatesOperationDelegate>" _lock_delegate;
@"<BLSHOSTimerProviding>" _osTimerProvider;
@"NSArray" _lock_environmentIdentifiers;
I _lock_environmentCount;
@"NSDate" _lock_beginDate;
d _lock_beginTime;
d _lock_shortestInterval;
d _lock_averageInterval;
d _lock_longestInterval;
B _lock_complete;
B _lock_begun;
B _lock_didReset;
B _lock_timedOut;
B _lock_invalidated;
@"NSDateInterval" _requestInterval;
```

## Properties

```
@property (T@"NSDateInterval",R,N,V_requestInterval) requestInterval;
@property (TB,R,N,GisComplete) complete;
@property (T@"NSArray",R,N) environmentIdentifiers;
@property (TI,R,N) environmentCount;
@property (Td,R,N) shortestInterval;
@property (Td,R,N) averageInterval;
@property (Td,R,N) longestInterval;
@property (TB,R,N) didReset;
@property (T@"NSDate",R,N) beginDate;
@property (Td,R,N) beginTimestamp;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHEngineRequestDatesOperation isComplete];
-[BLSHEngineRequestDatesOperation beginDate];
-[BLSHEngineRequestDatesOperation debugDescription];
-[BLSHEngineRequestDatesOperation dealloc];
-[BLSHEngineRequestDatesOperation invalidate];
-[BLSHEngineRequestDatesOperation description];
-[BLSHEngineRequestDatesOperation didReset];
-[BLSHEngineRequestDatesOperation requestInterval];
-[BLSHEngineRequestDatesOperation beginTimestamp];
-[BLSHEngineRequestDatesOperation averageInterval];
-[BLSHEngineRequestDatesOperation longestInterval];
-[BLSHEngineRequestDatesOperation environmentIdentifiers];
-[BLSHEngineRequestDatesOperation shortestInterval];
-[BLSHEngineRequestDatesOperation beginOperationWithIntervals:shouldReset:];
-[BLSHEngineRequestDatesOperation environmentCount];
-[BLSHEngineRequestDatesOperation initWithRequestInterval:delegate:osTimerProvider:];
-[BLSHEngineRequestDatesOperation telemetryDataWithEndTime:];
```

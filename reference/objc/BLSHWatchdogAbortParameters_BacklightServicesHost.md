# `BLSHWatchdogAbortParameters`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _isPotentialHang;
B _sleepImminentSinceScheduled;
@"<BLSHWatchdogDelegate>" _delegate;
@"<BLSHWatchdogAbortContext>" _abortContext;
@"SWSystemSleepMonitorAggregateState" _sleepMonitorAggregateState;
Q _abortTimestamp;
@"NSString" _explanation;
```

## Properties

```
@property (T@"<BLSHWatchdogDelegate>",W,N,V_delegate) delegate;
@property (T@"<BLSHWatchdogAbortContext>",&,N,V_abortContext) abortContext;
@property (TB,N,V_isPotentialHang) isPotentialHang;
@property (T@"SWSystemSleepMonitorAggregateState",&,N,V_sleepMonitorAggregateState) sleepMonitorAggregateState;
@property (TB,N,V_sleepImminentSinceScheduled) sleepImminentSinceScheduled;
@property (TQ,N,V_abortTimestamp) abortTimestamp;
@property (T@"NSString",C,N,V_explanation) explanation;
```

## Instance methods

```
-[BLSHWatchdogAbortParameters setExplanation:];
-[BLSHWatchdogAbortParameters explanation];
-[BLSHWatchdogAbortParameters setDelegate:];
-[BLSHWatchdogAbortParameters delegate];
-[BLSHWatchdogAbortParameters isPotentialHang];
-[BLSHWatchdogAbortParameters setSleepImminentSinceScheduled:];
-[BLSHWatchdogAbortParameters abortContext];
-[BLSHWatchdogAbortParameters abortTimestamp];
-[BLSHWatchdogAbortParameters initWithDelegate:abortContext:isPotentialHang:sleepMonitorAggregateState:sleepImminentSinceScheduled:explanation:];
-[BLSHWatchdogAbortParameters setAbortContext:];
-[BLSHWatchdogAbortParameters setAbortTimestamp:];
-[BLSHWatchdogAbortParameters setIsPotentialHang:];
-[BLSHWatchdogAbortParameters setSleepMonitorAggregateState:];
-[BLSHWatchdogAbortParameters sleepImminentSinceScheduled];
-[BLSHWatchdogAbortParameters sleepMonitorAggregateState];
```

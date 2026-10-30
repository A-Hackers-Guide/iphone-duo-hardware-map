# `BLSHLocalHostSceneEnvironmentUpdaterTimelinesCalculator`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHEngineRequestDatesOperationDelegate`
- 13 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableSet" _lock_timelines;
@"NSMutableDictionary" _lock_incompleteTimelineEntriesForDateInterval;
@"BLSHEngineRequestDatesOperation" _lock_requestDatesOperation;
B _lock_requestDatesOperationComplete;
B _lock_localHostEnvTimelinesComplete;
@"NSDateInterval" _dateInterval;
@"NSDate" _previousPresentationDate;
@"<BLSBacklightSceneEnvironment>" _localHostEnvironment;
@"NSArray" _subHostedHostEnvironments;
@"<BLSHOSTimerProviding>" _osTimerProvider;
B _shouldReset;
@? _lock_completion;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHLocalHostSceneEnvironmentUpdaterTimelinesCalculator requestDatesOperation:environment:didProvideSpecifiers:forPresentationInterval:isComplete:];
-[BLSHLocalHostSceneEnvironmentUpdaterTimelinesCalculator requestDatesOperation:didTimeoutPendingEnvironments:];
-[BLSHLocalHostSceneEnvironmentUpdaterTimelinesCalculator lock_completeAllTimelineEntries];
-[BLSHLocalHostSceneEnvironmentUpdaterTimelinesCalculator calculateWithCompletion:];
-[BLSHLocalHostSceneEnvironmentUpdaterTimelinesCalculator callCompletionIfDone];
```

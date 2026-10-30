# `BLSHAggregateSystemActivityAssertion`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHIndividualSystemActivityAssertionAggregator`, `BLSHSystemActivityAssertionConfiguring`
- 10 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"<BLSHOSInterfaceProviding>" _osInterfaceProvider;
@"<BLSHSystemActivityAsserting>" _lock_systemActivityAssertion;
@"<SWSystemActivityAcquisitionDetails>" _lock_systemActivityAcquisitionDetails;
@"NSHashTable" _lock_individualAssertions;
@? _lock_acquisitionHandler;
Q _stateHandler;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _initializing;
B _acquireWaitsToAbortSleepRequested;
B _acquireWaitsToAbortSleepImminent;
```

## Properties

```
@property (TB,R,N,GisActive) active;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHAggregateSystemActivityAssertion setAcquireWaitsToAbortSleepRequested:];
-[BLSHAggregateSystemActivityAssertion dealloc];
-[BLSHAggregateSystemActivityAssertion setAcquireWaitsToAbortSleepImminent:];
-[BLSHAggregateSystemActivityAssertion description];
-[BLSHAggregateSystemActivityAssertion isActive];
-[BLSHAggregateSystemActivityAssertion initWithConfigurator:];
-[BLSHAggregateSystemActivityAssertion _lock_addSystemActivityAcquisitionHandler:];
-[BLSHAggregateSystemActivityAssertion acquireIndividualAssertion:handler:];
-[BLSHAggregateSystemActivityAssertion didAcquireSystemActivityIsActive:error:details:];
-[BLSHAggregateSystemActivityAssertion invalidateIndividualAssertion:];
-[BLSHAggregateSystemActivityAssertion performConfigurator:];
-[BLSHAggregateSystemActivityAssertion setOSInterfaceProvider:];
```

# `BLSHAggregateProcessAssertion`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 9 instance variables, 5 properties, 9 instance methods, 3 class methods

## Instance variables

```
@"NSMapTable" _lock_aggregated;
@"RBSAssertion" _lock_rbsAssertion;
@"BLSHAggregatedProcessAssertion" _lock_acquiredAssertion;
@"BLSHDurationCalculator" _lock_durationCalculator;
B _lock_invalidated;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
Q _stateHandler;
d _initTimestamp;
@"RBSProcessIdentity" _processIdentity;
```

## Properties

```
@property (T@"RBSProcessIdentity",R,C,N,V_processIdentity) processIdentity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHAggregateProcessAssertion acquireAggregatedAssertion:completion:];
+[BLSHAggregateProcessAssertion classLock_aggregateForProcessIdentity:shouldCreate:];
+[BLSHAggregateProcessAssertion invalidateAggregatedAssertion:];
```

## Instance methods

```
-[BLSHAggregateProcessAssertion processIdentity];
-[BLSHAggregateProcessAssertion stateDataWithHints:];
-[BLSHAggregateProcessAssertion debugDescription];
-[BLSHAggregateProcessAssertion dealloc];
-[BLSHAggregateProcessAssertion initWithProcessIdentity:];
-[BLSHAggregateProcessAssertion invalidate];
-[BLSHAggregateProcessAssertion acquireAggregatedAssertion:completion:];
-[BLSHAggregateProcessAssertion invalidateAggregatedAssertion:];
-[BLSHAggregateProcessAssertion isCurrentRBSAssertion:];
```

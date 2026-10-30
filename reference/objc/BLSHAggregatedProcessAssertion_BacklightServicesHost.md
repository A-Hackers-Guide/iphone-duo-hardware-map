# `BLSHAggregatedProcessAssertion`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 6 instance variables, 8 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"BLSHAggregateProcessAssertion" _aggregate;
B _invalidated;
B _shouldFaultOnFailureToAcquire;
@"RBSProcessIdentity" _processIdentity;
@"NSString" _explanation;
d _duration;
```

## Properties

```
@property (T@"RBSProcessIdentity",R,C,N,V_processIdentity) processIdentity;
@property (T@"NSString",R,C,N,V_explanation) explanation;
@property (Td,R,N,V_duration) duration;
@property (TB,V_shouldFaultOnFailureToAcquire) shouldFaultOnFailureToAcquire;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHAggregatedProcessAssertion processIdentity];
-[BLSHAggregatedProcessAssertion explanation];
-[BLSHAggregatedProcessAssertion dealloc];
-[BLSHAggregatedProcessAssertion duration];
-[BLSHAggregatedProcessAssertion invalidate];
-[BLSHAggregatedProcessAssertion description];
-[BLSHAggregatedProcessAssertion acquireWithCompletion:];
-[BLSHAggregatedProcessAssertion createRBSAssertion];
-[BLSHAggregatedProcessAssertion initWithExplanation:processIdentity:duration:];
-[BLSHAggregatedProcessAssertion setShouldFaultOnFailureToAcquire:];
-[BLSHAggregatedProcessAssertion shouldFaultOnFailureToAcquire];
```

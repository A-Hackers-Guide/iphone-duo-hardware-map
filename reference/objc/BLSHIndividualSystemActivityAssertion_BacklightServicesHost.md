# `BLSHIndividualSystemActivityAssertion`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHSystemActivityAsserting`
- 3 instance variables, 6 properties, 6 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BLSHIndividualSystemActivityAssertionAggregator>" _lock_aggregator;
@"NSString" _identifier;
```

## Properties

```
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (TB,R,N,GisActive) active;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHIndividualSystemActivityAssertion identifier];
-[BLSHIndividualSystemActivityAssertion acquireWithTimeout:handler:];
-[BLSHIndividualSystemActivityAssertion dealloc];
-[BLSHIndividualSystemActivityAssertion invalidate];
-[BLSHIndividualSystemActivityAssertion isActive];
-[BLSHIndividualSystemActivityAssertion initWithWithIdentifier:aggregator:];
```

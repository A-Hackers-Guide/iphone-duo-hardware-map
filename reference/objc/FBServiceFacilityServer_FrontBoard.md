# `FBServiceFacilityServer`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSServiceConnectionListenerDelegate`, `FBSServiceFacilityManaging`
- 7 instance variables, 5 properties, 12 instance methods, 2 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BSServiceDomainSpecification" _domain;
@"BSServiceConnectionListener" _serviceListener;
@"NSMutableDictionary" _lock_facilitiesByIdentifier;
@"NSMutableSet" _lock_completedMilestones;
@"NSMutableDictionary" _lock_suspendedFacilitiesByIdentifier;
@"NSMutableSet" _lock_pendingConnects;
```

## Properties

```
@property (T@"BSServiceDomainSpecification",R,C,N,V_domain) domain;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBServiceFacilityServer sharedInstance];
+[FBServiceFacilityServer sharedInstanceDomain];
```

## Instance methods

```
-[FBServiceFacilityServer listener:didReceiveConnection:withContext:];
-[FBServiceFacilityServer domain];
-[FBServiceFacilityServer init];
-[FBServiceFacilityServer dealloc];
-[FBServiceFacilityServer run];
-[FBServiceFacilityServer _initWithDomain:];
-[FBServiceFacilityServer removeFacility:];
-[FBServiceFacilityServer addFacility:];
-[FBServiceFacilityServer _facilityQueue_facility:handleMessage:client:];
-[FBServiceFacilityServer _lock_areFacilityPrerequisitesSatisfied:];
-[FBServiceFacilityServer _lock_evaluateSuspendedFacility:];
-[FBServiceFacilityServer noteMilestoneReached:];
```

# `BLSHLocalAssertionService`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHAssertionAttributeHandlerService`
- 12 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _attributeHandlers;
@"NSMapTable" _activeAssertions;
@"NSMutableArray" _pausedAssertions;
@"NSMutableArray" _lock_longHeldAssertionHistory;
@"NSMutableSet" _queue_deferredAcquisitionAssertions;
@"NSHashTable" _observers;
@"BLSHAggregatedSystemActivityAssertionFactory" _aggregatedAssertionFactory;
Q _stateHandler;
@"NSObject<OS_dispatch_workloop>" _rootWorkloop;
@"NSObject<OS_dispatch_queue>" _queue;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"<BLSHOSInterfaceProviding>" _osInterfaceProvider;
```

## Properties

```
@property (T@"<BLSHOSInterfaceProviding>",R,N,V_osInterfaceProvider) osInterfaceProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHLocalAssertionService removeObserver:];
-[BLSHLocalAssertionService restartAssertionTimeoutTimer:];
-[BLSHLocalAssertionService acquireAssertion:];
-[BLSHLocalAssertionService addObserver:];
-[BLSHLocalAssertionService replaceWithService:];
-[BLSHLocalAssertionService cancelAssertion:withError:];
-[BLSHLocalAssertionService osInterfaceProvider];
-[BLSHLocalAssertionService pauseAssertion:];
-[BLSHLocalAssertionService initWithOSInterfaceProvider:];
-[BLSHLocalAssertionService registerAttributeHandler:];
-[BLSHLocalAssertionService resumeAssertion:];
-[BLSHLocalAssertionService willCancelAssertion:];
```

# `BLSAssertion`

- Image: [`/System/Library/PrivateFrameworks/BacklightServices.framework/BacklightServices`](../userland/System__Library__PrivateFrameworks__BacklightServices.framework__BacklightServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSAssertionServiceResponding`, `BSCancellable`, `BSInvalidatable`
- 16 instance variables, 14 properties, 28 instance methods, 2 class methods

## Instance variables

```
@"BLSAssertionIdentifier" _identifier;
@"BLSAssertionAcquisitionObserver" _acquisitionObserver;
@"NSHashTable" _observers;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_acquired;
B _lock_paused;
B _lock_everPaused;
B _lock_invalidated;
Q _lock_localState;
d _lock_accumulatedUnpausedDuration;
Q _lock_requestedMachContinuousTime;
Q _lock_acquiredMachContinuousTime;
Q _lock_unpauseMachContinuousTime;
Q _lock_canceledMachContinuousTime;
@"BLSAssertionDescriptor" _descriptor;
@"<BLSAssertionService>" _service;
```

## Properties

```
@property (T@"<BLSAssertionService>",&,V_service) service;
@property (T@"NSString",R,C,N) explanation;
@property (T@"NSArray",R,C,N) attributes;
@property (TB,R,N,GisAcquired) acquired;
@property (TB,R,N,GisPaused) paused;
@property (TB,R,N,GisActive) active;
@property (T@"BLSAssertionDescriptor",R,N,V_descriptor) descriptor;
@property (T@"BLSAssertionIdentifier",&,N) identifier;
@property (TQ,R,N) acquisitionState;
@property (Td,R,N) activeDuration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSAssertion acquireWithExplanation:observer:attributes:];
+[BLSAssertion setDefaultService:];
```

## Instance methods

```
-[BLSAssertion isPaused];
-[BLSAssertion descriptor];
-[BLSAssertion identifier];
-[BLSAssertion removeObserver:];
-[BLSAssertion setService:];
-[BLSAssertion explanation];
-[BLSAssertion serviceDidAcquire];
-[BLSAssertion dealloc];
-[BLSAssertion acquireWithObserver:];
-[BLSAssertion serviceDidCancelWithError:];
-[BLSAssertion restartTimeoutTimer];
-[BLSAssertion activeDuration];
-[BLSAssertion addObserver:];
-[BLSAssertion invalidate];
-[BLSAssertion setIdentifier:];
-[BLSAssertion serviceFailedToAcquireWithError:];
-[BLSAssertion service];
-[BLSAssertion initWithExplanation:attributes:];
-[BLSAssertion description];
-[BLSAssertion isAcquired];
-[BLSAssertion attributes];
-[BLSAssertion isActive];
-[BLSAssertion acquireWithCompletion:];
-[BLSAssertion cancel];
-[BLSAssertion serviceDidResume];
-[BLSAssertion serviceWillCancel];
-[BLSAssertion acquisitionState];
-[BLSAssertion serviceDidPause];
```

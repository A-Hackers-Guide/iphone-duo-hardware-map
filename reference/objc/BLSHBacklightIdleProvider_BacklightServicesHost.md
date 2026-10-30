# `BLSHBacklightIdleProvider`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSHBacklightHostObserving`, `BLSHUserIdleProvidingDelegate`, `BSInvalidatable`
- 17 instance variables, 11 properties, 23 instance methods, 4 class methods

## Instance variables

```
@"<BLSHUserIdleProviding>" _lock_idleProvider;
@"<BLSHBacklightHostObservable><BLSBacklightChangeRequestable>" _backlightHost;
q _lock_targetIdleBacklightState;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
d _lock_idleTimeout;
d _lock_nonInteractiveIdleTimeout;
q _lock_previousBacklightState;
B _lock_started;
B _lock_active;
B _lock_suspended;
B _lock_suppressed;
B _lock_idle;
B _lock_pendingIdleInactiveRequest;
B _lock_didStartTransitionToNewState;
B _lock_userActivityOccured;
B _lock_invalidated;
@"<BLSHBacklightIdleProviderDelegate>" _delegate;
```

## Properties

```
@property (TB,N,GisActive) active;
@property (T@"<BLSHBacklightIdleProviderDelegate>",W,N,V_delegate) delegate;
@property (Td,N) idleTimeout;
@property (Td,N) nonInteractiveIdleTimeout;
@property (Tq,N) targetIdleState;
@property (TB,R,N,GisIdle) idle;
@property (TB,R,N,GhasUserActivityOccured) userActivityOccured;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BLSHBacklightIdleProvider sharedProvider];
+[BLSHBacklightIdleProvider createProviderforDisplay:withLocalAssertionService:];
+[BLSHBacklightIdleProvider createSharedProviderWithLocalAssertionService:];
+[BLSHBacklightIdleProvider providerForDisplay:];
```

## Instance methods

```
-[BLSHBacklightIdleProvider backlight:didCompleteUpdateToState:forEvents:abortedEvents:];
-[BLSHBacklightIdleProvider setSuspended:];
-[BLSHBacklightIdleProvider isIdle];
-[BLSHBacklightIdleProvider idleTimeout];
-[BLSHBacklightIdleProvider dealloc];
-[BLSHBacklightIdleProvider start];
-[BLSHBacklightIdleProvider reset];
-[BLSHBacklightIdleProvider setActive:];
-[BLSHBacklightIdleProvider setIdleTimeout:];
-[BLSHBacklightIdleProvider invalidate];
-[BLSHBacklightIdleProvider setDelegate:];
-[BLSHBacklightIdleProvider delegate];
-[BLSHBacklightIdleProvider isActive];
-[BLSHBacklightIdleProvider backlightHost:willTransitionToState:forEvent:];
-[BLSHBacklightIdleProvider targetIdleState];
-[BLSHBacklightIdleProvider hasUserActivityOccured];
-[BLSHBacklightIdleProvider idleProviderDidIdle:];
-[BLSHBacklightIdleProvider idleProviderDidUnidle:];
-[BLSHBacklightIdleProvider initWithLocalAssertionService:idleProvider:backlightHost:];
-[BLSHBacklightIdleProvider nonInteractiveIdleTimeout];
-[BLSHBacklightIdleProvider setNonInteractiveIdleTimeout:];
-[BLSHBacklightIdleProvider setTargetIdleState:];
-[BLSHBacklightIdleProvider signalUserActivityOccurred];
```

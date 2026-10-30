# `BLSHAssertionProxy`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BLSAssertionServiceResponding`, `BSInvalidatable`
- 12 instance variables, 10 properties, 16 instance methods, 0 class methods

## Instance variables

```
d _lock_accumulatedUnpausedDuration;
Q _lock_acquiredMachContinuousTime;
Q _lock_unpauseMachContinuousTime;
Q _lock_canceledMachContinuousTime;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_valid;
B _lock_acquired;
B _lock_paused;
B _lock_everPaused;
@"BLSAssertionIdentifier" _identifier;
@"BLSAssertionDescriptor" _descriptor;
@"<BLSXPCAssertionServiceClientInterface>" _remoteTarget;
```

## Properties

```
@property (T@"BLSAssertionIdentifier",&,N,V_identifier) identifier;
@property (T@"BLSAssertionDescriptor",R,N,V_descriptor) descriptor;
@property (T@"<BLSXPCAssertionServiceClientInterface>",R,N,V_remoteTarget) remoteTarget;
@property (TB,R,N,GisAcquired) acquired;
@property (TQ,R,N) acquisitionState;
@property (Td,R,N) activeDuration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BLSHAssertionProxy descriptor];
-[BLSHAssertionProxy identifier];
-[BLSHAssertionProxy serviceDidAcquire];
-[BLSHAssertionProxy serviceDidCancelWithError:];
-[BLSHAssertionProxy activeDuration];
-[BLSHAssertionProxy invalidate];
-[BLSHAssertionProxy setIdentifier:];
-[BLSHAssertionProxy serviceFailedToAcquireWithError:];
-[BLSHAssertionProxy description];
-[BLSHAssertionProxy isAcquired];
-[BLSHAssertionProxy serviceDidResume];
-[BLSHAssertionProxy serviceWillCancel];
-[BLSHAssertionProxy acquisitionState];
-[BLSHAssertionProxy serviceDidPause];
-[BLSHAssertionProxy remoteTarget];
-[BLSHAssertionProxy initWithIdentifier:descriptor:remoteTarget:];
```

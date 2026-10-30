# `BLSHPresentationUpdates`

- Image: [`/System/Library/PrivateFrameworks/BacklightServicesHost.framework/BacklightServicesHost`](../userland/System__Library__PrivateFrameworks__BacklightServicesHost.framework__BacklightServicesHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSDate" _startDate;
@"NSMutableArray" _updates;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _invalidated;
@"NSDate" _nextUpdatesStart;
```

## Properties

```
@property (TB,R,N,GisCompleted) completed;
@property (T@"NSDate",R,N,V_nextUpdatesStart) nextUpdatesStart;
@property (TQ,R,N) count;
```

## Instance methods

```
-[BLSHPresentationUpdates isCompleted];
-[BLSHPresentationUpdates dealloc];
-[BLSHPresentationUpdates count];
-[BLSHPresentationUpdates invalidate];
-[BLSHPresentationUpdates description];
-[BLSHPresentationUpdates dequeueAllUpdates];
-[BLSHPresentationUpdates dequeueNextUpdate];
-[BLSHPresentationUpdates initWithStartDate:updates:nextUpdatesStart:];
-[BLSHPresentationUpdates isValidWithNowDate:];
-[BLSHPresentationUpdates nextUpdatesStart];
-[BLSHPresentationUpdates peekNextUpdate];
```

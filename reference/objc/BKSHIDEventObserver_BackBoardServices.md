# `BKSHIDEventObserver`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKSHIDEventObserverClientInterface`
- 12 instance variables, 6 properties, 16 instance methods, 1 class methods

## Instance variables

```
B _isNonLaunchingServer;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
B _lock_waitingOnServerHandshake;
B _lock_hasReceivedLatestDeferringObservationsFromServer;
@"NSMapTable" _lock_deferringAssertionsToObservers;
@"NSMapTable" _lock_observerToLastSeenDeferringObservations;
@"NSSet" _lock_deferringObservations;
@"NSMutableSet" _lock_chainObserverContainers;
@"NSDictionary" _lock_identityToChainMatches;
@"NSMutableSet" _lock_allChainObserverPredicates;
@"NSMutableArray" _lock_reachabilitySubscriptions;
@"BSServiceInitiatingConnection" _connection;
```

## Properties

```
@property (T@"NSSet",R,D,N) deferringObservations;
@property (TB,R,N) hasReceivedLatestDeferringObservationsFromServer;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDEventObserver sharedInstance];
```

## Instance methods

```
-[BKSHIDEventObserver didUpdateDeferringChains:withReply:];
-[BKSHIDEventObserver addObservingClient:forChainObserver:];
-[BKSHIDEventObserver _lock_shouldObserveDeferringChanges];
-[BKSHIDEventObserver init];
-[BKSHIDEventObserver reachableObservedTargetsDidChange:forTargets:];
-[BKSHIDEventObserver _observationsFromChains:];
-[BKSHIDEventObserver deferringObservations];
-[BKSHIDEventObserver addReachabilityObservationForTarget:respectingConstraints:handler:];
-[BKSHIDEventObserver _lock_postReachabilityTargetsToServer];
-[BKSHIDEventObserver hasReceivedLatestDeferringObservationsFromServer];
-[BKSHIDEventObserver _lock_dispatchReachabilityForStatuses:callouts:];
-[BKSHIDEventObserver _lock_resetChainObserverPredicates];
-[BKSHIDEventObserver addReachabilityObservationForTarget:handler:];
-[BKSHIDEventObserver _lock_postObservingStateToServerIncludingNegative:];
-[BKSHIDEventObserver _initWithConnectionFactory:];
-[BKSHIDEventObserver addDeferringObserver:];
```

# `BKHIDEventDeliveryObserverService`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKHIDEventDeliveryResolutionObserver`
- 9 instance variables, 5 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"BKHIDDomainServiceServer" _server;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"BSMutableIntegerMap" _lock_observationsByPID;
@"NSMutableSet" _lock_deferringChainObserverConnections;
@"NSMutableSet" _lock_reachabilityObserverConnections;
@"NSSet" _lock_allReachabilityTargets;
@"NSMutableDictionary" _lock_identityToChain;
Q _lock_chainPublicationSeed;
@"BKHIDEventDeliveryManager" _deliveryManager;
```

## Properties

```
@property (T@"BKHIDEventDeliveryManager",W,N,V_deliveryManager) deliveryManager;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKHIDEventDeliveryObserverService connectionDidTerminate:];
-[BKHIDEventDeliveryObserverService initWithServer:];
-[BKHIDEventDeliveryObserverService deliveryManager];
-[BKHIDEventDeliveryObserverService connection:setObservesDeferringChanges:];
-[BKHIDEventDeliveryObserverService connection:setReachabilityObservationTargets:];
-[BKHIDEventDeliveryObserverService deliveryChainDidUpdate:forIdentity:reason:];
-[BKHIDEventDeliveryObserverService initWithDomainServiceServer:];
-[BKHIDEventDeliveryObserverService reachabilityObservationTargets];
-[BKHIDEventDeliveryObserverService reachableObservationTargetsDidChange:reason:];
-[BKHIDEventDeliveryObserverService setDeliveryManager:];
```

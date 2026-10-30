# `CAMPeopleProximityController`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMPeopleProximityScannerDelegate`, `CAMPeopleProximityControllerProtocol`
- 10 instance variables, 14 properties, 31 instance methods, 0 class methods

## Instance variables

```
B _queue_hasDiscoveredFirstPerson;
B _queue_hasDiscoveredFirstPersonNearby;
# _proximityScannerClass;
@"<CAMPeopleProximityDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
@"NSObject<OS_dispatch_queue>" _queue;
Q _queue_discoveryState;
@"NSSet" _queue_identities;
@"CNContactStore" _queue_contactStore;
@"<CAMPeopleProximityScanner>" _queue_proximityScanner;
```

## Properties

```
@property (T@"<CAMPeopleProximityDelegate>",W,N,V_delegate) delegate;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_delegateQueue) delegateQueue;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_queue) queue;
@property (TQ,N,V_queue_discoveryState) queue_discoveryState;
@property (T@"NSSet",&,N,V_queue_identities) queue_identities;
@property (T@"CNContactStore",&,N,V_queue_contactStore) queue_contactStore;
@property (TB,N,V_queue_hasDiscoveredFirstPerson) queue_hasDiscoveredFirstPerson;
@property (TB,N,V_queue_hasDiscoveredFirstPersonNearby) queue_hasDiscoveredFirstPersonNearby;
@property (T@"<CAMPeopleProximityScanner>",&,N,V_queue_proximityScanner) queue_proximityScanner;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T#,&,N,V_proximityScannerClass) proximityScannerClass;
```

## Instance methods

```
-[CAMPeopleProximityController queue];
-[CAMPeopleProximityController setDelegate:];
-[CAMPeopleProximityController setDelegateQueue:];
-[CAMPeopleProximityController delegate];
-[CAMPeopleProximityController delegateQueue];
-[CAMPeopleProximityController initWithDelegate:delegateQueue:];
-[CAMPeopleProximityController setQueue:];
-[CAMPeopleProximityController stopDiscovery];
-[CAMPeopleProximityController _queue_handleFinishedWaitingForScanner:];
-[CAMPeopleProximityController _queue_handleScannerDidStop];
-[CAMPeopleProximityController _queue_startDiscoveryForIdentities:];
-[CAMPeopleProximityController _queue_stopDiscovery];
-[CAMPeopleProximityController peopleProximityScanner:didDiscoverIdentity:distance:rssi:];
-[CAMPeopleProximityController peopleProximityScanner:didLoseIdentity:];
-[CAMPeopleProximityController peopleProximityScanner:shouldDiscoverIdentity:];
-[CAMPeopleProximityController peopleProximityScannerDidStopDiscovery:];
-[CAMPeopleProximityController proximityScannerClass];
-[CAMPeopleProximityController queue_contactStore];
-[CAMPeopleProximityController queue_discoveryState];
-[CAMPeopleProximityController queue_hasDiscoveredFirstPerson];
-[CAMPeopleProximityController queue_hasDiscoveredFirstPersonNearby];
-[CAMPeopleProximityController queue_identities];
-[CAMPeopleProximityController queue_proximityScanner];
-[CAMPeopleProximityController setProximityScannerClass:];
-[CAMPeopleProximityController setQueue_contactStore:];
-[CAMPeopleProximityController setQueue_discoveryState:];
-[CAMPeopleProximityController setQueue_hasDiscoveredFirstPerson:];
-[CAMPeopleProximityController setQueue_hasDiscoveredFirstPersonNearby:];
-[CAMPeopleProximityController setQueue_identities:];
-[CAMPeopleProximityController setQueue_proximityScanner:];
-[CAMPeopleProximityController startDiscoveryForIdentities:];
```

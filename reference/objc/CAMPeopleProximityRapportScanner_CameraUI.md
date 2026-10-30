# `CAMPeopleProximityRapportScanner`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMPeopleProximityScanner`
- 6 instance variables, 11 properties, 23 instance methods, 0 class methods

## Instance variables

```
I __queue_peopleDiscoverySessionID;
@"<CAMPeopleProximityScannerDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _queue;
@"RPPeopleDiscovery" __queue_peopleDiscovery;
@"NSMutableDictionary" __queue_discoveredPersons;
@"NSMutableDictionary" __queue_discoveredIdentities;
```

## Properties

```
@property (T@"RPPeopleDiscovery",&,N,V__queue_peopleDiscovery) _queue_peopleDiscovery;
@property (T@"NSMutableDictionary",&,N,V__queue_discoveredPersons) _queue_discoveredPersons;
@property (T@"NSMutableDictionary",&,N,V__queue_discoveredIdentities) _queue_discoveredIdentities;
@property (TI,N,V__queue_peopleDiscoverySessionID) _queue_peopleDiscoverySessionID;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@"<CAMPeopleProximityScannerDelegate>",R,W,N,V_delegate) delegate;
@property (TB,R,N) isScanning;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMPeopleProximityRapportScanner isScanning];
-[CAMPeopleProximityRapportScanner dealloc];
-[CAMPeopleProximityRapportScanner initWithQueue:delegate:];
-[CAMPeopleProximityRapportScanner queue];
-[CAMPeopleProximityRapportScanner delegate];
-[CAMPeopleProximityRapportScanner stopDiscovery];
-[CAMPeopleProximityRapportScanner _queue_peopleDiscoverySessionID];
-[CAMPeopleProximityRapportScanner set_queue_discoveredIdentities:];
-[CAMPeopleProximityRapportScanner _queue_discoveredIdentities];
-[CAMPeopleProximityRapportScanner _queue_discoveredPersons];
-[CAMPeopleProximityRapportScanner _queue_discoveryActivatedWithError:timeout:peopleDiscoverySessionID:];
-[CAMPeopleProximityRapportScanner _queue_discoveryInterruptedWithPeopleDiscoverySessionID:];
-[CAMPeopleProximityRapportScanner _queue_discoveryInvalidatedWithPeopleDiscoverySessionID:];
-[CAMPeopleProximityRapportScanner _queue_discoveryPersonChanged:withChangeFlags:peopleDiscoverySessionID:];
-[CAMPeopleProximityRapportScanner _queue_discoveryPersonFound:peopleDiscoverySessionID:];
-[CAMPeopleProximityRapportScanner _queue_discoveryPersonLost:peopleDiscoverySessionID:];
-[CAMPeopleProximityRapportScanner _queue_discoveryTimeoutForSessionID:];
-[CAMPeopleProximityRapportScanner _queue_peopleDiscovery];
-[CAMPeopleProximityRapportScanner _queue_shouldAdvertisePerson:];
-[CAMPeopleProximityRapportScanner set_queue_discoveredPersons:];
-[CAMPeopleProximityRapportScanner set_queue_peopleDiscovery:];
-[CAMPeopleProximityRapportScanner set_queue_peopleDiscoverySessionID:];
-[CAMPeopleProximityRapportScanner startDiscoveryWithScanRate:timeout:];
```

# `CAMPeopleProximityDeviceScanner`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CAMPeopleProximityScanner`
- 6 instance variables, 11 properties, 20 instance methods, 0 class methods

## Instance variables

```
I __queue_sessionID;
@"<CAMPeopleProximityScannerDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _queue;
@"SFDeviceDiscovery" __queue_deviceDiscovery;
@"NSMutableDictionary" __queue_discoveredDevices;
@"NSMutableDictionary" __queue_discoveredIdentities;
```

## Properties

```
@property (T@"SFDeviceDiscovery",&,N,V__queue_deviceDiscovery) _queue_deviceDiscovery;
@property (T@"NSMutableDictionary",&,N,V__queue_discoveredDevices) _queue_discoveredDevices;
@property (T@"NSMutableDictionary",&,N,V__queue_discoveredIdentities) _queue_discoveredIdentities;
@property (TI,N,V__queue_sessionID) _queue_sessionID;
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
-[CAMPeopleProximityDeviceScanner isScanning];
-[CAMPeopleProximityDeviceScanner dealloc];
-[CAMPeopleProximityDeviceScanner initWithQueue:delegate:];
-[CAMPeopleProximityDeviceScanner queue];
-[CAMPeopleProximityDeviceScanner delegate];
-[CAMPeopleProximityDeviceScanner stopDiscovery];
-[CAMPeopleProximityDeviceScanner set_queue_discoveredIdentities:];
-[CAMPeopleProximityDeviceScanner _queue_deviceDiscovery];
-[CAMPeopleProximityDeviceScanner _queue_discoveredDevices];
-[CAMPeopleProximityDeviceScanner _queue_discoveredIdentities];
-[CAMPeopleProximityDeviceScanner _queue_discoveryActivatedWithError:sessionID:];
-[CAMPeopleProximityDeviceScanner _queue_discoveryDeviceFound:sessionID:];
-[CAMPeopleProximityDeviceScanner _queue_discoveryDeviceLost:sessionID:];
-[CAMPeopleProximityDeviceScanner _queue_discoveryInterruptedWithPeopleDiscoverySessionID:];
-[CAMPeopleProximityDeviceScanner _queue_discoveryTimeoutForSessionID:];
-[CAMPeopleProximityDeviceScanner _queue_sessionID];
-[CAMPeopleProximityDeviceScanner set_queue_deviceDiscovery:];
-[CAMPeopleProximityDeviceScanner set_queue_discoveredDevices:];
-[CAMPeopleProximityDeviceScanner set_queue_sessionID:];
-[CAMPeopleProximityDeviceScanner startDiscoveryWithScanRate:timeout:];
```

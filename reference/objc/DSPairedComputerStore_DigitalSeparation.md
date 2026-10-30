# `DSPairedComputerStore`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `DSPairedComputerStoreProtocol`
- 3 instance variables, 7 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"DSRemotePairingWrapper" _remotePairing;
@"DSRemotePairingStore" _remotePairingStore;
@"NSObject<OS_dispatch_queue>" _workQueue;
```

## Properties

```
@property (T@"DSRemotePairingWrapper",&,N,V_remotePairing) remotePairing;
@property (T@"DSRemotePairingStore",&,N,V_remotePairingStore) remotePairingStore;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_workQueue) workQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[DSPairedComputerStore setWorkQueue:];
-[DSPairedComputerStore init];
-[DSPairedComputerStore workQueue];
-[DSPairedComputerStore fetchPairedDevicesOnQueue:completion:];
-[DSPairedComputerStore remotePairing];
-[DSPairedComputerStore setRemotePairing:];
-[DSPairedComputerStore fetchWifiSyncStatus];
-[DSPairedComputerStore remotePairingStore];
-[DSPairedComputerStore removeAllPairedDevicesOnQueue:completion:];
-[DSPairedComputerStore removeComputersFromRemotePairing:withCompletion:];
-[DSPairedComputerStore removePairedDevices:onQueue:withCompletion:];
-[DSPairedComputerStore setRemotePairingStore:];
```

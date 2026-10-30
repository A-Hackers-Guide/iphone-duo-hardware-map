# `ACCBLEPairingProviderInternal`

- Image: [`/System/Library/PrivateFrameworks/AccessoryBLEPairing.framework/AccessoryBLEPairing`](../userland/System__Library__PrivateFrameworks__AccessoryBLEPairing.framework__AccessoryBLEPairing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 36 instance methods, 1 class methods

## Instance variables

```
i _lastScorpiusDetectType;
i _accDetectToken;
@"NSMutableDictionary" _delegateList;
@"NSLock" _delegateListLock;
@"NSString" _providerUID;
@"NSXPCConnection" _serverConnection;
@"<ACCBLEPairingXPCServerProtocol>" _remoteObject;
@"NSMutableDictionary" _accessories;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_delegateList) delegateList;
@property (T@"NSLock",&,N,V_delegateListLock) delegateListLock;
@property (T@"NSString",&,N,V_providerUID) providerUID;
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<ACCBLEPairingXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"NSMutableDictionary",&,N,V_accessories) accessories;
@property (Ti,N,V_accDetectToken) accDetectToken;
@property (Ti,N,V_lastScorpiusDetectType) lastScorpiusDetectType;
```

## Class methods

```
+[ACCBLEPairingProviderInternal SharedInstance];
```

## Instance methods

```
-[ACCBLEPairingProviderInternal connectToServer];
-[ACCBLEPairingProviderInternal setRemoteObject:];
-[ACCBLEPairingProviderInternal serverConnection];
-[ACCBLEPairingProviderInternal dealloc];
-[ACCBLEPairingProviderInternal accessories];
-[ACCBLEPairingProviderInternal providerUID];
-[ACCBLEPairingProviderInternal remoteObject];
-[ACCBLEPairingProviderInternal setAccessories:];
-[ACCBLEPairingProviderInternal setServerConnection:];
-[ACCBLEPairingProviderInternal setProviderUID:];
-[ACCBLEPairingProviderInternal initSharedInstance];
-[ACCBLEPairingProviderInternal accessoryBLEPairingDataUpdate:blePairingUUID:pairType:pairData:];
-[ACCBLEPairingProviderInternal accDetectToken];
-[ACCBLEPairingProviderInternal accessoryBLEPairingAttached:blePairingUUID:accInfoDict:supportedPairTypes:];
-[ACCBLEPairingProviderInternal accessoryBLEPairingDetachAll];
-[ACCBLEPairingProviderInternal accessoryBLEPairingDetached:blePairingUUID:];
-[ACCBLEPairingProviderInternal accessoryBLEPairingFinished:blePairingUUID:];
-[ACCBLEPairingProviderInternal accessoryBLEPairingInfoUpdate:blePairingUUID:pairType:pairInfoList:];
-[ACCBLEPairingProviderInternal accessoryBLEPairingNoAccessories];
-[ACCBLEPairingProviderInternal accessoryBLEPairingStateUpdate:blePairingUUID:validMask:btRadioOn:pairingState:pairingModeOn:];
-[ACCBLEPairingProviderInternal delegateList];
-[ACCBLEPairingProviderInternal delegateListLock];
-[ACCBLEPairingProviderInternal devicePairingData:blePairingUUID:pairType:pairData:];
-[ACCBLEPairingProviderInternal deviceStateUpdate:blePairingUUID:bRadioOn:pairState:bPairModeOn:];
-[ACCBLEPairingProviderInternal deviceUpdatePairingInfo:blePairingUUID:pairType:pairInfo:];
-[ACCBLEPairingProviderInternal getAccDetectType:];
-[ACCBLEPairingProviderInternal lastScorpiusDetectType];
-[ACCBLEPairingProviderInternal registerDelegate:provider:forUUID:];
-[ACCBLEPairingProviderInternal setAccDetectToken:];
-[ACCBLEPairingProviderInternal setDelegateList:];
-[ACCBLEPairingProviderInternal setDelegateListLock:];
-[ACCBLEPairingProviderInternal setLastScorpiusDetectType:];
-[ACCBLEPairingProviderInternal startBLEUpdates:blePairingUUID:pairType:bRadioUpdatesOn:bPairInfoUpdatesOn:];
-[ACCBLEPairingProviderInternal stopBLEUpdates:blePairingUUID:];
-[ACCBLEPairingProviderInternal unregisterDelegateForUUID:];
-[ACCBLEPairingProviderInternal updateResolvedAccessoryBTAddress:blePairingUUID:btAddress:];
```

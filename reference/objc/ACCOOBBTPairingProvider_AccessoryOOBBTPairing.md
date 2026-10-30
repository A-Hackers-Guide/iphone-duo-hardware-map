# `ACCOOBBTPairingProvider`

- Image: [`/System/Library/PrivateFrameworks/AccessoryOOBBTPairing.framework/AccessoryOOBBTPairing`](../userland/System__Library__PrivateFrameworks__AccessoryOOBBTPairing.framework__AccessoryOOBBTPairing.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"<ACCOOBBTPairingProviderProtocol>" _delegate;
@"NSString" _providerUID;
@"NSXPCConnection" _serverConnection;
@"<ACCOOBBTPairingXPCServerProtocol>" _remoteObject;
@"NSMutableDictionary" _accessories;
```

## Properties

```
@property (T@"NSString",&,N,V_providerUID) providerUID;
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<ACCOOBBTPairingXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"NSMutableDictionary",&,N,V_accessories) accessories;
@property (T@"<ACCOOBBTPairingProviderProtocol>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[ACCOOBBTPairingProvider initWithDelegate:];
-[ACCOOBBTPairingProvider connectToServer];
-[ACCOOBBTPairingProvider setRemoteObject:];
-[ACCOOBBTPairingProvider serverConnection];
-[ACCOOBBTPairingProvider dealloc];
-[ACCOOBBTPairingProvider accessories];
-[ACCOOBBTPairingProvider providerUID];
-[ACCOOBBTPairingProvider remoteObject];
-[ACCOOBBTPairingProvider setDelegate:];
-[ACCOOBBTPairingProvider setAccessories:];
-[ACCOOBBTPairingProvider delegate];
-[ACCOOBBTPairingProvider setServerConnection:];
-[ACCOOBBTPairingProvider setProviderUID:];
-[ACCOOBBTPairingProvider accessoryInfoDictionaryForLogging:];
-[ACCOOBBTPairingProvider accessoryOOBBTPairingAttached:accInfoDict:];
-[ACCOOBBTPairingProvider accessoryOOBBTPairingBTAccessoryInfo:oobBtPairingUID:accessoryMacAddr:deviceClass:];
-[ACCOOBBTPairingProvider accessoryOOBBTPairingCompletionStatus:oobBtPairingUID:accessoryMacAddr:result:];
-[ACCOOBBTPairingProvider accessoryOOBBTPairingDetachAll];
-[ACCOOBBTPairingProvider accessoryOOBBTPairingDetached:];
-[ACCOOBBTPairingProvider legacyConnectionIDForAccessoryUID:connectionID:];
-[ACCOOBBTPairingProvider linkKeyInfo:oobBtPairingUID:linkKey:deviceMacAddr:];
-[ACCOOBBTPairingProvider requestLegacyConnectionIDForAccessoryUID:];
-[ACCOOBBTPairingProvider startOOBBTPairing:];
-[ACCOOBBTPairingProvider stopOOBBTPairing:];
```

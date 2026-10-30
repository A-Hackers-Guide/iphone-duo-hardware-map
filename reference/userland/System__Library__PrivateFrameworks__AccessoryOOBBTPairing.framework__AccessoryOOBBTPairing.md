# `/System/Library/PrivateFrameworks/AccessoryOOBBTPairing.framework/AccessoryOOBBTPairing`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (4)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 2 classes, 3 protocols, 59 methods, 10 properties

### Class pages

Every class and protocol, with its methods: [`ACCOOBBTPairingAccessory`](../objc/ACCOOBBTPairingAccessory_AccessoryOOBBTPairing.md), [`ACCOOBBTPairingProvider`](../objc/ACCOOBBTPairingProvider_AccessoryOOBBTPairing.md), [`ACCOOBBTPairingXPCClientProtocol`](../objc/ACCOOBBTPairingXPCClientProtocol_AccessoryOOBBTPairing.protocol.md), [`ACCOOBBTPairingXPCServerProtocol`](../objc/ACCOOBBTPairingXPCServerProtocol_AccessoryOOBBTPairing.protocol.md), [`NSObject`](../objc/NSObject_AccessoryOOBBTPairing.protocol.md)

### Classes

`ACCOOBBTPairingAccessory`, `ACCOOBBTPairingProvider`

### Protocols

`ACCOOBBTPairingXPCClientProtocol`, `ACCOOBBTPairingXPCServerProtocol`, `NSObject`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",&,N,V_accessoryUID) accessoryUID;
@property (T@"NSString",&,N,V_providerUID) providerUID;
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<ACCOOBBTPairingXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"NSMutableDictionary",&,N,V_accessories) accessories;
@property (T@"<ACCOOBBTPairingProviderProtocol>",W,N,V_delegate) delegate;
```

## Strings (89)

```
ACCOOBBTPairingCarPlaySupported
General
Endpoint
%lu bytes
com.apple.iap2d.btpairing.connect
ACCOOBBTPairingAccSerialNum
IAPAppAccessoryOOBBTPairingConnectionIDKey
v12@?0i8
ACCOOBBTPairingComponentInfoUID
com.apple.accessories.oobbtpairing
ACCOOBBTPairingAccHwVer
ACCOOBBTPairing2Supported
IAPAppAccessoryOOBBTPairingCompletionMACAddressKey
Connection
com.apple.accessories.oobbtpairing.availability-changed
ACCOOBBTPairingAccName
ACCOOBBTPairingDisplayName
ACCOOBBTPairingComponentInfoID
ACCOOBBTPairingComponentInfoMacAddr
IAPAppAccessoryOOBBTPairingCompletionStatusKey
_SetupAvailabilityChangedHandlerForServiceEntry
ACCOOBBTPairingAccModel
ACCOOBBTPairingCertSerial
IAPAppAccessoryOOBBTPairingCompletionNotification
v8@?0
v16@?0@\"NSError\"8
null
accessoryServer_isServerAvailableForServiceEntry
com.apple.accessories.frameworks
ACCOOBBTPairingComponentInfoName
com.apple.accessories.signposts
<ACCOOBBTPairingAccessory>[%@]
v12@?0B8
ACCOOBBTPairingAccFwVer
ACCOOBBTPairingCertData
<Undefined>
Transport
ACCOOBBTPairingAccManufacturer
accessoryOOBBTPairingAttached: accessory %@ (%@) already exists!
accessoryOOBBTPairingDetachAll: notify detach of %lu accessories!
accessoryOOBBTPairingBTAccessoryInfo: accessory %@, oobBtPairingUID %@ accessoryMacAddr %@ deviceClass=%d, accessory=%@
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
Created log object %s: %s
Server availability changed! State: %d
Getting remote object...
shouldStayConnected: %d
%@
ACCOOBBTPairingProvider connectToServer, _providerUID=%@, NOT accessoryServer_isServerAvailable()
XPC connection interrupted!
ACCOOBBTPairingProvider init, _providerUID=%@
Trying to connect to server...
Connecting to XPC server...
XPC connection invalidated!
stopOOBBTPairing: %@, _remoteObject nil, _providerUID=%@
accessoryOOBBTPairingDetached: accessory %@, _accessories=%@
accessoryOOBBTPairingDetachAll: accessory %@
linkKeyInfo: %@ oobBtPairingUID: %@ linkKey:len=%lu deviceMacAddr: %@
legacyConnectionIDForAccessoryUID: accessory %@ (%@) does not exist!
Unregister AvailabilityChangedHandler (%d, %s)
%s cannot get server state (%d, %s)
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
accessoryOOBBTPairingAttached: accessory %@, accessory=%@ accInfoDict=%@
accessoryOOBBTPairingCompletionStatus: accessory %@ (%@) does not exist!
startOOBBTPairing: %@
requestLegacyConnectionIDForAccessoryUID: %@, _remoteObject nil, _providerUID=%@
Register AvailabilityChangedHandler (%d, %s)
%s (%d)
ACCOOBBTPairingProvider connectToServer, _providerUID=%@
XPC connection error!
accessoryOOBBTPairingBTAccessoryInfo: accessory %@ (%@) does not exist!
legacyConnectionIDForAccessoryUID: accessory %@, connectionID=%u, accessory=%@
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
Failed to create os_log_t object %s: %s!
Created %d log object(s)!
ACCOOBBTPairingProvider connectToServer, _providerUID=%@, IS accessoryServer_isServerAvailable()
requestLegacyConnectionIDForAccessoryUID: %@
%s (%d, %s)
%s did not register for notification (%d, %s), token (%d)
accessoryOOBBTPairingAttached: accessory %@, _accessories=%@
accessoryOOBBTPairingDetached: accessory %@, accessory=%@
accessoryOOBBTPairingCompletionStatus: accessory %@, oobBtPairingUID %@, accessoryMacAddr %@, result=%d, accessory=%@
stopOOBBTPairing: %@
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Call initConnection to remoteObject=%@
accessoryOOBBTPairingDetached: accessory %@ (%@) does not exist!
startOOBBTPairing: %@, _remoteObject nil, _providerUID=%@
linkKeyInfo: %@, _remoteObject nil, _providerUID=%@
AccessoryServerAvailabilityChangedHandler already set! (%d, %s)
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
```

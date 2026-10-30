# `/System/Library/PrivateFrameworks/AccessoryBLEPairing.framework/AccessoryBLEPairing`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (4)

- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 4 classes, 3 protocols, 103 methods, 23 properties

### Class pages

Every class and protocol, with its methods: [`ACCBLEPairingAccessory`](../objc/ACCBLEPairingAccessory_AccessoryBLEPairing.md), [`ACCBLEPairingDelegateReference`](../objc/ACCBLEPairingDelegateReference_AccessoryBLEPairing.md), [`ACCBLEPairingProvider`](../objc/ACCBLEPairingProvider_AccessoryBLEPairing.md), [`ACCBLEPairingProviderInternal`](../objc/ACCBLEPairingProviderInternal_AccessoryBLEPairing.md), [`ACCBLEPairingXPCClientProtocol`](../objc/ACCBLEPairingXPCClientProtocol_AccessoryBLEPairing.protocol.md), [`ACCBLEPairingXPCServerProtocol`](../objc/ACCBLEPairingXPCServerProtocol_AccessoryBLEPairing.protocol.md), [`NSObject`](../objc/NSObject_AccessoryBLEPairing.protocol.md)

### Classes

`ACCBLEPairingAccessory`, `ACCBLEPairingDelegateReference`, `ACCBLEPairingProvider`, `ACCBLEPairingProviderInternal`

### Protocols

`ACCBLEPairingXPCClientProtocol`, `ACCBLEPairingXPCServerProtocol`, `NSObject`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",&,N,V_accessoryUID) accessoryUID;
@property (TB,N,V_desiredBLEPairingState) desiredBLEPairingState;
@property (T@"NSDictionary",&,N,V_accInfo) accInfo;
@property (T@"NSData",&,N,V_blePairingUUID) blePairingUUID;
@property (T@"NSData",&,N,V_supportedPairTypes) supportedPairTypes;
@property (TB,N,V_blePairingFinished) blePairingFinished;
@property (T@"<ACCBLEPairingProviderProtocol>",W,N,V_delegate) delegate;
@property (T@"ACCBLEPairingProvider",W,N,V_provider) provider;
@property (T@"NSString",&,N,V_delegateUUID) delegateUUID;
@property (T@"<ACCBLEPairingProviderProtocol>",W,N,V_delegate) delegate;
@property (Ti,N) lastScorpiusDetectType;
@property (T@"NSMutableDictionary",&,N,V_delegateList) delegateList;
@property (T@"NSLock",&,N,V_delegateListLock) delegateListLock;
@property (T@"NSString",&,N,V_providerUID) providerUID;
@property (T@"NSXPCConnection",&,N,V_serverConnection) serverConnection;
@property (T@"<ACCBLEPairingXPCServerProtocol>",&,N,V_remoteObject) remoteObject;
@property (T@"NSMutableDictionary",&,N,V_accessories) accessories;
@property (Ti,N,V_accDetectToken) accDetectToken;
@property (Ti,N,V_lastScorpiusDetectType) lastScorpiusDetectType;
```

## Strings (149)

```
Server availability changed! State: %d UID: %@
ACCBLEPairingProvider connectToServer, _providerUID=%@, IS accessoryServer_isServerAvailable()
Getting remote object...
%s:%d call blePairingNoAccessories, delegate=%@, provider=%@
accessoryBLEPairingAttached: accessory %@, blePairingUUID %@, accessory=%@
accessoryBLEPairingDetachAll: accessory %@
accessoryBLEPairingFinished: delegate doesn't respond to blePairing:pairingFinished:blePairingUUID:, provider = %@, delegate = %@
updateResolvedAccessoryBTAddress: invalid btAddress length %lu
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
%s (%d, %s)
EXIT object detect notification handler, %@
ACCBLEPairingProvider dealloc, %@
Unregister AvailabilityChangedHandler (%d, %s)
accessoryBLEPairingDetached: accessory %@ (%@) does not exist!
accessoryBLEPairingNoAccessories
accessoryBLEPairingInfoUpdate: accessory %@, blePairingUUID %@, pairType=%d pairInfoList=%@, call delegate=%@, provider=%@
accessoryBLEPairingFinished: accessory %@, blePairingUUID %@, accessory=%@
deviceStateUpdate: %@, blePairingUUID %@, bRadioOn=%d pairState=%d bPairModeOn=%d
%s: delegateUUID %@, updateResolvedAccessoryBTAddress: %@, blePairingUUID %@, resolvedAccessoryBTAddress length=%lu
%s: delegateUUID %@, stopBLEUpdates: %@, blePairingUUID %@
%s (%d)
accessoryBLEPairingDataUpdate: accessory %@, blePairingUUID %@, pairType=%d pairData=%@, call delegate=%@, provider=%@
lastDetectType %d -> %d
%s:%d NOT accessoryServer_isServerAvailable(), delegate=%@, provider=%@
accessoryBLEPairingDetached: accessory %@, blePairingUUID %@, accessory=%@
accessoryBLEPairingDetached: accessory %@, blePairingUUID %@, call delegate=%@, provider=%@
accessoryBLEPairingFinished: accessory %@, blePairingUUID %@, _delegateList=%@
Trying to connect to server...
XPC connection interrupted!
accessoryBLEPairingAttached: accessory %@, blePairingUUID %@, accessory=%@, accInfoDict=%@, supportedPairTypes=%@
accessoryBLEPairingDataUpdate: accessory %@, blePairingUUID %@, pairType=%d pairData=%@, accessory=%@
deviceStateUpdate: %@, _remoteObject nil, _providerUID=%@
updateResolvedAccessoryBTAddress: %@, _remoteObject nil, _providerUID=%@
%s:%d result %d 
%s:%d call accessoryAttached: accessory %@, blePairingUUID %@, call delegate=%@, provider=%@
Call initConnection to remoteObject=%@
startBLEUpdates: %@, _remoteObject nil, _providerUID=%@
updateResolvedAccessoryBTAddress: %@, blePairingUUID %@, resolvedAccessoryBTAddress=%@
stopBLEUpdates: %@, blePairingUUID %@
stopBLEUpdates: %@, _remoteObject nil, _providerUID=%@
%s: delegateUUID %@, deviceStateUpdate: %@, blePairingUUID %@, bRadioOn=%d pairState=%d bPairModeOn=%d
%s: delegateUUID %@, deviceUpdatePairingInfo: %@, blePairingUUID %@, pairType=%d pairInfo=%@
%@
ACCBLEPairingProvider connectToServer, _providerUID=%@, NOT accessoryServer_isServerAvailable()
accessoryBLEPairingAttached: accessory %@, blePairingUUID %@, call delegate=%@, provider=%@
%s:%d  %d -> %d 
Register AvailabilityChangedHandler (%d, %s)
ACCBLEPairingProvider connectToServer, _providerUID=%@
accessoryBLEPairingStateUpdate: accessory %@, blePairingUUID %@, validMask=%x btRadioOn=%d pairingState=%d pairingModeOn=%d, accessory=%@
devicePairingData: %@, _remoteObject nil, _providerUID=%@
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Created %d log object(s)!
Category missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
BLEPairingProvider delegate respond to blePairing:accessoryDetect:, delegate = %@, provider = %@
accessoryBLEPairingDetached: EXIT, accessory %@, blePairingUUID %@, accessory %@
accessoryBLEPairingStateUpdate: accessory %@, blePairingUUID %@, validMask=%x btRadioOn=%d pairingState=%d pairingModeOn=%d, call delegate=%@, provider=%@
accessoryBLEPairingStateUpdate: EXIT, accessory %@, blePairingUUID %@, validMask=%x btRadioOn=%d pairingState=%d pairingModeOn=%d, accessory=%@
accessoryBLEPairingFinished: accessory %@ (%@) does not exist!
devicePairingData: %@, blePairingUUID %@, pairType=%d pairData=%@
ACCBLEPairingProvider init, %@
%s:%d, delegate %@, uuid %@
accessoryBLEPairingNoAccessories, call delegate=%@, provider=%@
accessoryBLEPairingInfoUpdate: accessory %@, blePairingUUID %@, pairType=%d pairInfoList=%@, accessory=%@
accessoryBLEPairingDataUpdate: accessory %@ (%@) does not exist!
accessoryBLEPairingFinished: EXIT, accessory %@, blePairingUUID %@, accessory=%@
deviceUpdatePairingInfo: %@, blePairingUUID %@, pairType=%d pairInfo=%@
deviceUpdatePairingInfo: %@, _remoteObject nil, _providerUID=%@
%s: delegateUUID %@, startBLEUpdates: %@, blePairingUUID %@, pairType=%d bRadioUpdatesOn=%d bPairInfoUpdatesOn=%d
accessoryBLEPairingFinished: delegate respond to blePairing:pairingFinished:blePairingUUID:, provider =%@, delegate = %@
ACCBLEPairingProvider init, _providerUID=%@, %p
Connecting to XPC server...
XPC connection error!
accessoryBLEPairingStateUpdate: accessory %@ (%@) does not exist!
AccessoryServerAvailabilityChangedHandler already set! (%d, %s)
Created log object %s: %s
Failed to create os_log_t object %s: %s!
BLEPairingProvider delegate doesn't respond to blePairing:accessoryDetect:, delegate = %@, provider = %@
%s:%d call pairingFinished: accessory %@, blePairingUUID %@, call delegate=%@, provider=%@
shouldStayConnected: %d
accessoryBLEPairingDetachAll: notify detach of %lu accessories!
accessoryBLEPairingDetachAll: EXIT, notify detach of %lu accessories!
accessoryBLEPairingInfoUpdate: accessory %@ (%@) does not exist!
Subsystem missing for logging module %d!\n(Check LoggingSignpostModuleEntry_t table)
accessoryBLEPairingDataUpdate: EXIT, accessory %@, blePairingUUID %@, pairType=%d pairData=%@, accessory=%@
XPC connection invalidated!
accessoryBLEPairingInfoUpdate: EXIT, accessory %@, blePairingUUID %@, pairType=%d pairInfoList=%@, accessory=%@
startBLEUpdates: %@, blePairingUUID %@, pairType=%d bRadioUpdatesOn=%d bPairInfoUpdatesOn=%d
%s: delegateUUID %@, devicePairingData: %@, blePairingUUID %@, pairType=%d pairData=%@
ACCBLEPairingAccessory init, accessoryUID %@, blePairingUUID %@, accInfo %@, supportedPairTypes %@
accessoryBLEPairingAttached: accessory %@ (%@) already exists!
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
ACCBLEPairingProvider dealloc, _providerUID %@
%s:%d, uuid %@
%s cannot get server state (%d, %s)
%s did not register for notification (%d, %s), token (%d)
IAPAppBTPairingUUIDKey
IAPAppBTPairingRadioStateKey
IAPAppBTPairingPairStateKey
v12@?0B8
com.apple.accessories.blepairing
-[ACCBLEPairingProvider setLastScorpiusDetectType:]
com.apple.iap2d.btpairing.connect
IAPAppBTPairingDidConnectKey
IAPAppBTPairingPairInfoArrayKey
IAPAppBTPairingAccDeviceUID
IAPAppBTPairingAccVendorID
com.apple.accessories.scp.objdetect
IAPAppBTPairingDidUpdateStateKey
IAPAppBTPairingAccPlatformID
IAPAppBTPairingAccName
<Undefined>
Connection
Transport
-[ACCBLEPairingProvider deviceStateUpdate:blePairingUUID:bRadioOn:pairState:bPairModeOn:]
v8@?0
v12@?0i8
-[ACCBLEPairingProvider lastScorpiusDetectType]
IAPAppBTPairingDidDisconnectKey
IAPAppBTPairingPairDataKey
IAPAppBTPairingAccProductID
accessoryServer_isServerAvailableForServiceEntry
-[ACCBLEPairingProvider deviceUpdatePairingInfo:blePairingUUID:pairType:pairInfo:]
IAPAppBTPairingSupports2WayKey
IAPAppBTPairingAccHwVer
_SetupAvailabilityChangedHandlerForServiceEntry
Endpoint
IAPAppBTPairingAccManufacturer
-[ACCBLEPairingProvider devicePairingData:blePairingUUID:pairType:pairData:]
IAPAppBTPairingIsSupportedKey
IAPAppBTPairingDidSendPairDataKey
IAPAppBTPairingPairModeKey
IAPAppBTPairingAccSerialNum
IAPAppBTPairingAccFwPendingVer
null
-[ACCBLEPairingProviderInternal unregisterDelegateForUUID:]
v16@?0@\"NSError\"8
IAPAppBTPairingAccModel
IAPAppBTPairingTypesSupportedKey
IAPAppBTPairingAccFwVer
com.apple.accessories.frameworks
General
com.apple.accessories.signposts
com.apple.accessories.blepairing.availability-changed
-[ACCBLEPairingProvider startBLEUpdates:blePairingUUID:pairType:bRadioUpdatesOn:bPairInfoUpdatesOn:]
-[ACCBLEPairingProviderInternal registerDelegate:provider:forUUID:]
-[ACCBLEPairingProvider updateResolvedAccessoryBTAddress:blePairingUUID:btAddress:]
-[ACCBLEPairingProvider stopBLEUpdates:blePairingUUID:]
IAPAppBTPairingDidSendPairInfoKey
IAPAppBTPairingConnectionIDKey
```

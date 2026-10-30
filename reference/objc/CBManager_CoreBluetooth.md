# `CBManager`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBXpcConnectionDelegate`, `CBPairingAgentParentDelegate`
- 17 instance variables, 19 properties, 65 instance methods, 6 class methods

## Instance variables

```
@"CBXpcConnection" _connection;
@"CBPairingAgent" _pairingAgent;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _cnxDict;
B _tccComplete;
B _tccApproved;
B _tccRequired;
B _tccAbort;
q _state;
@"NSData" _advertisingAddress;
q _advertisingAddressType;
@"NSData" _nonConnectableAdvertisingAddress;
q _nonConnectableAdvertisingAddressType;
@"NSData" _nonConnectableSecondaryAdvertisingAddress;
q _nonConnectableSecondaryAdvertisingAddressType;
@"NSString" _localAddressString;
@"NSString" _localName;
```

## Properties

```
@property (Tq,N,V_state) state;
@property (TB,N,V_tccComplete) tccComplete;
@property (TB,N,V_tccApproved) tccApproved;
@property (TB,N,V_tccRequired) tccRequired;
@property (TB,N,V_tccAbort) tccAbort;
@property (T@"CBPairingAgent",R,&,D,N) sharedPairingAgent;
@property (T@"NSData",C,N,V_advertisingAddress) advertisingAddress;
@property (Tq,R,N,V_advertisingAddressType) advertisingAddressType;
@property (T@"NSData",C,N,V_nonConnectableAdvertisingAddress) nonConnectableAdvertisingAddress;
@property (Tq,R,N,V_nonConnectableAdvertisingAddressType) nonConnectableAdvertisingAddressType;
@property (T@"NSData",C,N,V_nonConnectableSecondaryAdvertisingAddress) nonConnectableSecondaryAdvertisingAddress;
@property (Tq,R,N,V_nonConnectableSecondaryAdvertisingAddressType) nonConnectableSecondaryAdvertisingAddressType;
@property (T@"NSString",R,V_localAddressString) localAddressString;
@property (T@"NSString",R,V_localName) localName;
@property (Tq,R,N) authorization;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBManager authorization];
+[CBManager retrieveCurrentProcessSessionCount];
+[CBManager getTCCServer];
+[CBManager tccAvailable];
+[CBManager checkIfExtension];
+[CBManager preflightCheckForTCC];
```

## Instance methods

```
-[CBManager performTCCCheck];
-[CBManager retrieveBundle:sessionCountWithCompletion:];
-[CBManager isMsgAllowedAlways:];
-[CBManager handlePairingAgentMsg:args:];
-[CBManager handleMsg:args:];
-[CBManager tccRequired];
-[CBManager nonConnectableSecondaryAdvertisingAddressType];
-[CBManager _handleAdvertisingAddressChanged:];
-[CBManager setAdvertisingAddress:];
-[CBManager extractLocalDeviceStatesDictionary:];
-[CBManager getCBPrivacySupported];
-[CBManager setWHBMsgReplyHandler:];
-[CBManager tccComplete];
-[CBManager authorization];
-[CBManager sendMsg:args:withReply:];
-[CBManager handleStateUpdatedMsg:];
-[CBManager setNonConnectableAdvertisingAddress:];
-[CBManager advertisingAddress];
-[CBManager startWithQueue:options:sessionType:];
-[CBManager setTccComplete:];
-[CBManager setState:];
-[CBManager setNonConnectableSecondaryAdvertisingAddress:];
-[CBManager checkForTCC];
-[CBManager setTccAbort:];
-[CBManager getLocalDeviceState];
-[CBManager setTccApproved:];
-[CBManager removeWhbRemoteId:];
-[CBManager nonConnectableAdvertisingAddressType];
-[CBManager nonConnectableSecondaryAdvertisingAddress];
-[CBManager sendSyncMsg:args:];
-[CBManager xpcConnectionIsInvalid];
-[CBManager advertisingAddressType];
-[CBManager sendDebugSyncMsg:args:];
-[CBManager sendDebugMsg:args:];
-[CBManager setTccRequired:];
-[CBManager getWhbLocalIdForRemoteId:];
-[CBManager checkBTTCCAuth];
-[CBManager closeL2CAPChannelForPeerUUID:withPsm:];
-[CBManager xpcConnectionDidReset];
-[CBManager tccAbort];
-[CBManager isMsgAllowedWhenOff:];
-[CBManager createCnxWithInfo:];
-[CBManager queryBluetoothStatus:completion:];
-[CBManager didReceiveForwardedMessageForCBManager:];
-[CBManager tccApproved];
-[CBManager nonConnectableAdvertisingAddress];
-[CBManager setConnectionTargetQueue:];
-[CBManager initInternal];
-[CBManager doneWithTCC];
-[CBManager handleLocalDeviceStateUpdatedMsg:];
-[CBManager retrieveSupportedResources:subKey:completion:];
-[CBManager sendRawCommand:data:completionHandler:];
-[CBManager getCnxInstanceForIdentifier:];
-[CBManager removeCnxInstanceForIdentifier:];
-[CBManager setWhbLocalId:forRemoteId:];
-[CBManager localName];
-[CBManager triggerBTErrorReport:];
-[CBManager getCurrentQueue];
-[CBManager sharedPairingAgent];
-[CBManager dealloc];
-[CBManager xpcConnectionDidReceiveMsg:args:];
-[CBManager sendMsg:args:];
-[CBManager peerWithInfo:];
-[CBManager localAddressString];
-[CBManager state];
```

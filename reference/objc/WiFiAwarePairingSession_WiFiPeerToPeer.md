# `WiFiAwarePairingSession`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiP2PXPCConnectionDelegate`, `WiFiAwarePairingXPCDelegate`
- 8 instance variables, 10 properties, 27 instance methods, 1 class methods

## Instance variables

```
@"WiFiP2PXPCConnection" _xpcConnection;
@"NSObject<OS_os_log>" _logger;
C _publishID;
q _role;
@"WiFiAwarePairingConfig" _pairingConfig;
@"<WiFiAwarePairingDelegate>" _delegate;
@"WiFiAwareDiscoveryResult" _discoveryResult;
@"WiFiMACAddress" _initiatorAddress;
```

## Properties

```
@property (Tq,N,V_role) role;
@property (T@"WiFiAwarePairingConfig",R,N,V_pairingConfig) pairingConfig;
@property (T@"<WiFiAwarePairingDelegate>",W,N,V_delegate) delegate;
@property (T@"WiFiAwareDiscoveryResult",&,N,V_discoveryResult) discoveryResult;
@property (TC,N,V_publishID) publishID;
@property (T@"WiFiMACAddress",&,N,V_initiatorAddress) initiatorAddress;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[WiFiAwarePairingSession WiFiAwarePairingRoleToString:];
```

## Instance methods

```
-[WiFiAwarePairingSession handleError:];
-[WiFiAwarePairingSession deactivate];
-[WiFiAwarePairingSession startConnectionUsingProxy:completionHandler:];
-[WiFiAwarePairingSession remoteObjectInterface];
-[WiFiAwarePairingSession exportedInterface];
-[WiFiAwarePairingSession setDelegate:];
-[WiFiAwarePairingSession exportedObject];
-[WiFiAwarePairingSession role];
-[WiFiAwarePairingSession delegate];
-[WiFiAwarePairingSession setRole:];
-[WiFiAwarePairingSession description];
-[WiFiAwarePairingSession discoveryResult];
-[WiFiAwarePairingSession initWithPairingConfig:delegate:];
-[WiFiAwarePairingSession pairWithDiscoveryResult:];
-[WiFiAwarePairingSession publishID];
-[WiFiAwarePairingSession setDiscoveryResult:];
-[WiFiAwarePairingSession initiatorAddress];
-[WiFiAwarePairingSession setInitiatorAddress:];
-[WiFiAwarePairingSession activateForPublishID:initiatorAddress:];
-[WiFiAwarePairingSession pairingConfig];
-[WiFiAwarePairingSession pairingDidFailTo:error:];
-[WiFiAwarePairingSession pairingDidSucceedWithDeviceInfo:pairingStoreID:];
-[WiFiAwarePairingSession requiresPINDisplay:];
-[WiFiAwarePairingSession requiresPINInputWithCompletionHandler:];
-[WiFiAwarePairingSession requiresPassphraseDisplay:];
-[WiFiAwarePairingSession requiresPassphraseInputWithCompletionHandler:];
-[WiFiAwarePairingSession setPublishID:];
```

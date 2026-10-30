# `AWDLServiceDiscoveryManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AWDLServiceDiscoveryManagerXPCDelegate`
- 6 instance variables, 4 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSLock" _lock;
@"NSXPCConnection" _xpcConnection;
i _notifyToken;
B _attemptedReconnect;
@"NSMutableArray" _activeTrafficRegistrations;
q _suspendCount;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AWDLServiceDiscoveryManager connectionInvalidated];
-[AWDLServiceDiscoveryManager init];
-[AWDLServiceDiscoveryManager dealloc];
-[AWDLServiceDiscoveryManager _retryConnection];
-[AWDLServiceDiscoveryManager addAWDLDiscoveryClient:forService:error:];
-[AWDLServiceDiscoveryManager removeAWDLDiscoveryClient:forService:error:];
-[AWDLServiceDiscoveryManager clearTrafficRegistration:error:];
-[AWDLServiceDiscoveryManager performRealtimeConnectivityCheckWithConfiguration:error:];
-[AWDLServiceDiscoveryManager setTrafficRegistration:error:];
-[AWDLServiceDiscoveryManager setTrafficRegistration:onInvalidationHandler:error:];
-[AWDLServiceDiscoveryManager _destroyConnection];
-[AWDLServiceDiscoveryManager _removeFirstTrafficRegistrationMatching:];
-[AWDLServiceDiscoveryManager _requiresConnection];
-[AWDLServiceDiscoveryManager _usingAWDLDiscoveryManagerProxy:onSuccess:error:];
-[AWDLServiceDiscoveryManager getActiveTrafficRegistrationWithCompletionHandler:];
-[AWDLServiceDiscoveryManager invalidatedActiveTrafficRegistration:];
-[AWDLServiceDiscoveryManager queryAirPlayConnectivityWithConfiguration:error:];
-[AWDLServiceDiscoveryManager refreshAWDLDiscoveryActivityForService:error:];
-[AWDLServiceDiscoveryManager resumeAWDLWithError:];
-[AWDLServiceDiscoveryManager suspendAWDLWithError:];
```

# `WiFiP2PDNSServiceDiscoveryManager`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiP2PDNSServiceDiscoveryXPCDelegate`, `WiFiP2PXPCConnectionDelegate`
- 4 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _useWiFiAware;
@? _serviceCallback;
@"NSMutableArray" _registeredServices;
@"WiFiP2PXPCConnection" _xpcConnection;
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
-[WiFiP2PDNSServiceDiscoveryManager startConnectionUsingProxy:completionHandler:];
-[WiFiP2PDNSServiceDiscoveryManager remoteObjectInterface];
-[WiFiP2PDNSServiceDiscoveryManager exportedInterface];
-[WiFiP2PDNSServiceDiscoveryManager exportedObject];
-[WiFiP2PDNSServiceDiscoveryManager handleConnectionEstablishedWithProxy:];
-[WiFiP2PDNSServiceDiscoveryManager handleEventType:keyData:valueData:];
-[WiFiP2PDNSServiceDiscoveryManager initUsingWiFiAware:serviceCallback:];
-[WiFiP2PDNSServiceDiscoveryManager startServiceDiscoveryWithConfiguration:];
-[WiFiP2PDNSServiceDiscoveryManager startServiceDiscoveryWithConfiguration:completionHandler:];
-[WiFiP2PDNSServiceDiscoveryManager stopServiceDiscoveryWithConfiguration:];
```

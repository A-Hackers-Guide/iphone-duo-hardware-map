# `WiFiP2PXPCConnection`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 1 properties, 15 instance methods, 14 class methods

## Instance variables

```
Q _endpointType;
@"NSObject<OS_dispatch_queue>" _queue;
q _retryTimeout;
@"NSXPCConnection" _connection;
@ _remoteObject;
i _notifyToken;
@"NSObject<OS_dispatch_source>" _retryTimer;
@"NSMutableArray" _queuedRequests;
@"<WiFiP2PXPCConnectionDelegate>" _delegate;
```

## Properties

```
@property (T@"<WiFiP2PXPCConnectionDelegate>",W,V_delegate) delegate;
```

## Class methods

```
+[WiFiP2PXPCConnection defaultRetryTimeout];
+[WiFiP2PXPCConnection supportsWiFiP2P];
+[WiFiP2PXPCConnection wifiPeerToPeerWorkloop];
+[WiFiP2PXPCConnection wifip2pRemoteXPCInterface];
+[WiFiP2PXPCConnection convertError:];
+[WiFiP2PXPCConnection weakExportedObjectProxy:];
+[WiFiP2PXPCConnection localization];
+[WiFiP2PXPCConnection directRequestOnEndpointType:error:requesting:];
+[WiFiP2PXPCConnection wifiPeerToPeerAvailableNotification];
+[WiFiP2PXPCConnection wifip2pExportedXPCInterfaceFor:];
+[WiFiP2PXPCConnection frameworkBundle];
+[WiFiP2PXPCConnection directQueryOnEndpointType:exportedObject:withExportedInterface:error:querying:];
+[WiFiP2PXPCConnection endpointForEndpointType:];
+[WiFiP2PXPCConnection directQueryOnEndpointType:error:querying:];
```

## Instance methods

```
-[WiFiP2PXPCConnection handleError:];
-[WiFiP2PXPCConnection withRemoteObjectProxy:clientErrorHandler:];
-[WiFiP2PXPCConnection stop];
-[WiFiP2PXPCConnection dealloc];
-[WiFiP2PXPCConnection start];
-[WiFiP2PXPCConnection initWithEndpointType:queue:retryTimeout:];
-[WiFiP2PXPCConnection attemptConnection];
-[WiFiP2PXPCConnection handleConnectionInvalidated];
-[WiFiP2PXPCConnection invalidate];
-[WiFiP2PXPCConnection setDelegate:];
-[WiFiP2PXPCConnection cleanUpRemovingNotifyToken:];
-[WiFiP2PXPCConnection delegate];
-[WiFiP2PXPCConnection withRemoteObjectProxy:];
-[WiFiP2PXPCConnection withRemoteObjectProxy:clientCompletionHandler:];
-[WiFiP2PXPCConnection reconnectOnAvailableNotification];
```

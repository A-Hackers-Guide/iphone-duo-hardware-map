# `WiFiAwareSubscriber`

- Image: [`/System/Library/PrivateFrameworks/WiFiPeerToPeer.framework/WiFiPeerToPeer`](../userland/System__Library__PrivateFrameworks__WiFiPeerToPeer.framework__WiFiPeerToPeer.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WiFiAwareSubscriberXPCDelegate`, `WiFiP2PXPCConnectionDelegate`
- 5 instance variables, 6 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"WiFiP2PXPCConnection" _xpcConnection;
@"NSNumber" _subscribeID;
@"NSObject<OS_os_log>" _logger;
@"<WiFiAwareSubscriberDelegate>" _delegate;
@"WiFiAwareSubscribeConfiguration" _configuration;
```

## Properties

```
@property (T@"<WiFiAwareSubscriberDelegate>",W,N,V_delegate) delegate;
@property (T@"WiFiAwareSubscribeConfiguration",R,N,V_configuration) configuration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[WiFiAwareSubscriber handleError:];
-[WiFiAwareSubscriber startConnectionUsingProxy:completionHandler:];
-[WiFiAwareSubscriber stop];
-[WiFiAwareSubscriber remoteObjectInterface];
-[WiFiAwareSubscriber start];
-[WiFiAwareSubscriber exportedInterface];
-[WiFiAwareSubscriber initWithConfiguration:];
-[WiFiAwareSubscriber setDelegate:];
-[WiFiAwareSubscriber configuration];
-[WiFiAwareSubscriber exportedObject];
-[WiFiAwareSubscriber delegate];
-[WiFiAwareSubscriber description];
-[WiFiAwareSubscriber sendMessage:toPeerAddress:withInstanceID:completionHandler:];
-[WiFiAwareSubscriber sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:completionHandler:];
-[WiFiAwareSubscriber updateTimeout:completionHandler:];
-[WiFiAwareSubscriber subscribeStartedWithInstanceID:];
-[WiFiAwareSubscriber sendDataBlobForMulticastSession:toPeerAddress:usingMulticastAddress:usingiGTK:completionHandler:];
-[WiFiAwareSubscriber subscribeDetectedMulticastError:fromMulticastSender:];
-[WiFiAwareSubscriber subscribeFailedToStartWithError:];
-[WiFiAwareSubscriber subscribeLostDiscoveryResultForPublishID:address:];
-[WiFiAwareSubscriber subscribeReceivedDataBlobForMulticastSession:fromPeer:];
-[WiFiAwareSubscriber subscribeReceivedDiscoveryResult:];
-[WiFiAwareSubscriber subscribeReceivedMessage:fromPublishID:address:];
-[WiFiAwareSubscriber subscribeTerminatedWithReason:];
```

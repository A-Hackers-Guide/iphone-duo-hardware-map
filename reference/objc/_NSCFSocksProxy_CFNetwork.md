# `_NSCFSocksProxy`

- Image: [`/System/Library/Frameworks/CFNetwork.framework/CFNetwork`](../userland/System__Library__Frameworks__CFNetwork.framework__CFNetwork.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSProxyConnectionDelegate`
- 7 instance variables, 4 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
i _outPort;
@"NSString" _outHost;
@"__CFN_SocksHandshake" _socksHandshake;
@"NSProxyConnection" _inbound;
@"NSProxyConnection" _outbound;
@"NSDictionary" _configuration;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_NSCFSocksProxy handleIncomingConnection:queue:configuration:];
```

## Instance methods

```
-[_NSCFSocksProxy cleanup];
-[_NSCFSocksProxy dealloc];
-[_NSCFSocksProxy connected:];
-[_NSCFSocksProxy outboundConnectionCompleteWithError:];
-[_NSCFSocksProxy outboundConnectionReceivedData:handler:];
```

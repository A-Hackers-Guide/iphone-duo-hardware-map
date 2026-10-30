# `SecKeyProxy`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCListenerDelegate`
- 6 instance variables, 7 properties, 11 instance methods, 4 class methods

## Instance variables

```
@ _key;
@"NSData" _certificate;
@"NSXPCListener" _listener;
Aq _clientCount;
@? _clientConnectionHandler;
@? _clientDisconnectionHandler;
```

## Properties

```
@property (T@"NSXPCListenerEndpoint",R,N) endpoint;
@property (T@?,C,N) clientConnectionHandler;
@property (T@?,C,N) clientDisconnectionHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SecKeyProxy createIdentityFromEndpoint:error:];
+[SecKeyProxy createItemFromEndpoint:certificate:error:];
+[SecKeyProxy createKeyFromEndpoint:error:];
+[SecKeyProxy targetForKey:error:];
```

## Instance methods

```
-[SecKeyProxy listener:shouldAcceptNewConnection:];
-[SecKeyProxy dealloc];
-[SecKeyProxy endpoint];
-[SecKeyProxy invalidate];
-[SecKeyProxy initWithIdentity:];
-[SecKeyProxy initWithKey:];
-[SecKeyProxy clientConnectionHandler];
-[SecKeyProxy clientDisconnectionHandler];
-[SecKeyProxy initWithKey:certificate:];
-[SecKeyProxy setClientConnectionHandler:];
-[SecKeyProxy setClientDisconnectionHandler:];
```

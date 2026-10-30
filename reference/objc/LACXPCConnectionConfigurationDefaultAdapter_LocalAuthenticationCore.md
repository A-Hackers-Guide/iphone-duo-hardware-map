# `LACXPCConnectionConfigurationDefaultAdapter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACXPCConnectionConfiguration`
- 5 instance variables, 9 properties, 7 instance methods, 0 class methods

## Instance variables

```
@ _exportedObject;
@"NSNumber" _connectionUID;
@"NSXPCInterface" _exportedInterface;
@"NSXPCInterface" _remoteObjectInterface;
@"NSObject<OS_dispatch_queue>" _replyQueue;
```

## Properties

```
@property (T@"NSNumber",&,N,V_connectionUID) connectionUID;
@property (T@,R,N,V_exportedObject) exportedObject;
@property (T@"NSXPCInterface",R,N,V_exportedInterface) exportedInterface;
@property (T@"NSXPCInterface",R,N,V_remoteObjectInterface) remoteObjectInterface;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_replyQueue) replyQueue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACXPCConnectionConfigurationDefaultAdapter remoteObjectInterface];
-[LACXPCConnectionConfigurationDefaultAdapter exportedInterface];
-[LACXPCConnectionConfigurationDefaultAdapter exportedObject];
-[LACXPCConnectionConfigurationDefaultAdapter replyQueue];
-[LACXPCConnectionConfigurationDefaultAdapter initWithRemoteObjectInterface:exportedInterface:exportedObject:replyQueue:];
-[LACXPCConnectionConfigurationDefaultAdapter connectionUID];
-[LACXPCConnectionConfigurationDefaultAdapter setConnectionUID:];
```

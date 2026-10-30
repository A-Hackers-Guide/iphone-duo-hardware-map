# `LACXPCConnectionDefaultAdapter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACXPCConnection`
- 2 instance variables, 7 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"<LACXPCConnectionDelegate>" delegate;
@"NSXPCConnection" _connection;
```

## Properties

```
@property (T@"NSXPCConnection",R,N,V_connection) connection;
@property (T@"<LACXPCConnectionDelegate>",W,N,Vdelegate) delegate;
@property (T@,R,N) remoteObject;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACXPCConnectionDefaultAdapter hasEntitlement:];
-[LACXPCConnectionDefaultAdapter initWithListenerEndpoint:];
-[LACXPCConnectionDefaultAdapter configureWithConfiguration:];
-[LACXPCConnectionDefaultAdapter initWithMachServiceName:options:];
-[LACXPCConnectionDefaultAdapter initWithConnection:];
-[LACXPCConnectionDefaultAdapter remoteObject];
-[LACXPCConnectionDefaultAdapter invalidate];
-[LACXPCConnectionDefaultAdapter setDelegate:];
-[LACXPCConnectionDefaultAdapter activate];
-[LACXPCConnectionDefaultAdapter connection];
-[LACXPCConnectionDefaultAdapter delegate];
-[LACXPCConnectionDefaultAdapter synchronousRemoteObjectWithErrorHandler:];
-[LACXPCConnectionDefaultAdapter remoteObjectWithErrorHandler:];
```

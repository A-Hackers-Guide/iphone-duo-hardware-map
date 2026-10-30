# `LACServiceXPCClient`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACXPCConnectionDelegate`
- 5 instance variables, 4 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"<LACServiceXPCEndpointProvider>" _endpointProvider;
@"NSXPCInterface" _remoteObjectInterface;
@"NSString" _serviceIdentifier;
@"<LACXPCConnection>" _connection;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _connectionLock;
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
-[LACServiceXPCClient synchronousRemoteObjectProxyWithErrorHandler:];
-[LACServiceXPCClient remoteObjectProxyWithErrorHandler:];
-[LACServiceXPCClient _connectionWithErrorHandler:];
-[LACServiceXPCClient _handleConnectionClose];
-[LACServiceXPCClient connectionDidActivate:];
-[LACServiceXPCClient connectionDidInterrupt:];
-[LACServiceXPCClient connectionDidInvalidate:];
-[LACServiceXPCClient initWithEndpointProvider:remoteObjectInterface:serviceIdentifier:];
```

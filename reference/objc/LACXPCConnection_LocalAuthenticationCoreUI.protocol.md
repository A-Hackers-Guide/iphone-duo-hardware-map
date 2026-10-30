# `LACXPCConnection` (protocol)

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCoreUI.framework/LocalAuthenticationCoreUI`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCoreUI.framework__LocalAuthenticationCoreUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 9 instance methods, 0 class methods

## Properties

```
@property (T@"<LACXPCConnectionDelegate>",W,N) delegate;
@property (T@,R,N) remoteObject;
```

## Instance methods

```
-[LACXPCConnection hasEntitlement:];
-[LACXPCConnection configureWithConfiguration:];
-[LACXPCConnection remoteObject];
-[LACXPCConnection invalidate];
-[LACXPCConnection setDelegate:];
-[LACXPCConnection activate];
-[LACXPCConnection delegate];
-[LACXPCConnection synchronousRemoteObjectWithErrorHandler:];
-[LACXPCConnection remoteObjectWithErrorHandler:];
```

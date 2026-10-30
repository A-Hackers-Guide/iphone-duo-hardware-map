# `LACUserInterfaceRemoteUIAdapter`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACRemoteUIClientProtocol`, `LACXPCConnectionDelegate`, `LACUserInterface`
- 5 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<LACXPCConnection>" _connection;
@"<LACUserInterfaceConnectionProviding>" _connectionProvider;
I _currentRequestId;
@? _handler;
@"NSObject<OS_dispatch_queue>" _replyQueue;
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
-[LACUserInterfaceRemoteUIAdapter terminateWithReason:];
-[LACUserInterfaceRemoteUIAdapter _finishWithError:];
-[LACUserInterfaceRemoteUIAdapter dealloc];
-[LACUserInterfaceRemoteUIAdapter connectionDidActivate:];
-[LACUserInterfaceRemoteUIAdapter connectionDidInterrupt:];
-[LACUserInterfaceRemoteUIAdapter connectionDidInvalidate:];
-[LACUserInterfaceRemoteUIAdapter _activateConnectionForRequest:];
-[LACUserInterfaceRemoteUIAdapter initWithConnectionProvider:replyQueue:];
-[LACUserInterfaceRemoteUIAdapter processRequest:completion:];
-[LACUserInterfaceRemoteUIAdapter uiDismissedForRequest:error:];
```

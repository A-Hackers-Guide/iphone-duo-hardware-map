# `LACServiceBase`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACService`, `NSXPCListenerDelegate`
- 6 instance variables, 9 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _clients;
B _terminating;
@"LACThreadSafeDictionary" _vendedListeners;
@"<LACServiceManager>" manager;
@"NSString" _serviceID;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (TQ,R,N) clientsCount;
@property (T@"<LACServiceManager>",W,N,Vmanager) manager;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (Td,R,N) listenerTimeout;
@property (T@"NSString",R,N,V_serviceID) serviceID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[LACServiceBase serviceID];
-[LACServiceBase listener:shouldAcceptNewConnection:];
-[LACServiceBase init];
-[LACServiceBase setManager:];
-[LACServiceBase dealloc];
-[LACServiceBase exportedInterface];
-[LACServiceBase queue];
-[LACServiceBase manager];
-[LACServiceBase exportedObject];
-[LACServiceBase clientsCount];
-[LACServiceBase listenerTimeout];
-[LACServiceBase _assertRunningInCorrectQueue];
-[LACServiceBase _checkAndShutdownIfNeeded];
-[LACServiceBase _disconnectClient:];
-[LACServiceBase _handleListenerTimeout:];
-[LACServiceBase createEndpoint];
```

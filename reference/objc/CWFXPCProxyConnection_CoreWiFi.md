# `CWFXPCProxyConnection`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSXPCProxyCreating`
- 4 instance variables, 1 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"CWFXPCProxy" _XPCProxy;
@"CWFXPCProxy" _synchronousXPCProxy;
@"NSObject<OS_dispatch_queue>" _queue;
@? _invalidationHandler;
```

## Properties

```
@property (T@?,C,V_invalidationHandler) invalidationHandler;
```

## Instance methods

```
-[CWFXPCProxyConnection suspend];
-[CWFXPCProxyConnection setInvalidationHandler:];
-[CWFXPCProxyConnection synchronousRemoteObjectProxyWithErrorHandler:];
-[CWFXPCProxyConnection remoteObjectProxyWithErrorHandler:];
-[CWFXPCProxyConnection invalidate];
-[CWFXPCProxyConnection activate];
-[CWFXPCProxyConnection invalidationHandler];
-[CWFXPCProxyConnection remoteObjectProxy];
-[CWFXPCProxyConnection resume];
-[CWFXPCProxyConnection initWithForwardingTarget:];
```

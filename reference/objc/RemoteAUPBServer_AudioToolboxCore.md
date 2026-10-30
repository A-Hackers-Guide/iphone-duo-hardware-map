# `RemoteAUPBServer`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSXPCConnection" xpcConnection;
@"<AUPBServing>" proxyInterface;
^{OpaqueAUPBServer=} ref;
{vector<NSObject<OS_dispatch_semaphore> *, std::allocator<NSObject<OS_dispatch_semaphore> *>>="__begin_"^@"__end_"^@""{?="__cap_"^@}} replySemas;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,VxpcConnection) xpcConnection;
@property (T@"<AUPBServing>",&,N,VproxyInterface) proxyInterface;
@property (T^{OpaqueAUPBServer=},N,Vref) ref;
```

## Instance methods

```
-[RemoteAUPBServer setXpcConnection:];
-[RemoteAUPBServer dealloc];
-[RemoteAUPBServer xpcConnection];
-[RemoteAUPBServer description];
-[RemoteAUPBServer ref];
-[RemoteAUPBServer setRef:];
-[RemoteAUPBServer addSema:];
-[RemoteAUPBServer proxyInterface];
-[RemoteAUPBServer removeSema:];
-[RemoteAUPBServer setProxyInterface:];
-[RemoteAUPBServer signalAllSemaphores];
```

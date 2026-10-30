# `SideBarFileDispatcherAPI`

- Image: [`/System/Library/PrivateFrameworks/SidebarFileDispatcher.framework/SidebarFileDispatcher`](../userland/System__Library__PrivateFrameworks__SidebarFileDispatcher.framework__SidebarFileDispatcher.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSXPCConnection" _connectionToService;
@"NSObject<OS_dispatch_queue>" _connectionQueue;
```

## Properties

```
@property (T@"NSXPCConnection",&,N,V_connectionToService) connectionToService;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_connectionQueue) connectionQueue;
```

## Class methods

```
+[SideBarFileDispatcherAPI sharedDispatcher];
```

## Instance methods

```
-[SideBarFileDispatcherAPI connectionQueue];
-[SideBarFileDispatcherAPI setConnectionQueue:];
-[SideBarFileDispatcherAPI init];
-[SideBarFileDispatcherAPI invalidate];
-[SideBarFileDispatcherAPI connection];
-[SideBarFileDispatcherAPI connectionToService];
-[SideBarFileDispatcherAPI setConnectionToService:];
-[SideBarFileDispatcherAPI processSidebarBuffer:bufferSizeBytes:NVMeDeviceID:sbarLba:reply:];
```

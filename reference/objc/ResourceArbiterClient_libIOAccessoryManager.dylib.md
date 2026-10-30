# `ResourceArbiterClient`

- Image: [`/usr/lib/libIOAccessoryManager.dylib`](../userland/usr__lib__libIOAccessoryManager.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BaseResourceArbiterClient`
- 9 instance variables, 5 properties, 13 instance methods, 0 class methods

## Instance variables

```
I _ioConnect;
^{IONotificationPort=} _ioNotificationPort;
I _ioNotificationObject;
@"NSObject<OS_dispatch_queue>" _notificationPortQueue;
B _resourceAccessStatus;
I _ioService;
i _clientPriority;
i _pendingResourceRequest;
@"NSObject<OS_dispatch_semaphore>" _sema;
```

## Properties

```
@property (TI,R,N,V_ioService) ioService;
@property (Ti,R,N,V_clientPriority) clientPriority;
@property (Ti,R,N,V_pendingResourceRequest) pendingResourceRequest;
@property (TB,R,N,V_resourceAccessStatus) resourceAccessStatus;
@property (T@"NSObject<OS_dispatch_semaphore>",R,N,V_sema) sema;
```

## Instance methods

```
-[ResourceArbiterClient dealloc];
-[ResourceArbiterClient sema];
-[ResourceArbiterClient clientPriority];
-[ResourceArbiterClient initWithID:];
-[ResourceArbiterClient ioService];
-[ResourceArbiterClient asynchRequestResourceAccess:];
-[ResourceArbiterClient releaseResourceAccess];
-[ResourceArbiterClient resourceAccessRevoked];
-[ResourceArbiterClient synchRequestResourceAccess];
-[ResourceArbiterClient _processResourceAccessStatus:];
-[ResourceArbiterClient pendingResourceRequest];
-[ResourceArbiterClient resourceAccessGranted];
-[ResourceArbiterClient resourceAccessStatus];
```

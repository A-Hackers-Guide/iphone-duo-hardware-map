# `ACCTransportIOAccessoryBase`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/IOAccessoryManager.transport/IOAccessoryManager`](../userland/System__Library__CoreAccessories__PlugIns__Transports__IOAccessoryManager.transport__IOAccessoryManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
I _ioConnect;
^{IONotificationPort=} _ioNotificationPort;
I _ioNotificationObject;
@"NSObject<OS_dispatch_queue>" _notificationPortQueue;
I _ioService;
i _ioServiceClassType;
i _primaryPortNumber;
I _upstreamManagerService;
```

## Properties

```
@property (TI,N,V_upstreamManagerService) upstreamManagerService;
@property (Ti,N,V_primaryPortNumber) primaryPortNumber;
@property (TI,R,N,V_ioService) ioService;
@property (Ti,R,N,V_ioServiceClassType) ioServiceClassType;
```

## Instance methods

```
-[ACCTransportIOAccessoryBase dealloc];
-[ACCTransportIOAccessoryBase transportClassTerminated];
-[ACCTransportIOAccessoryBase ioService];
-[ACCTransportIOAccessoryBase initWithIOAccessoryClass:ioService:];
-[ACCTransportIOAccessoryBase ioServiceClassType];
-[ACCTransportIOAccessoryBase primaryPortNumber];
-[ACCTransportIOAccessoryBase setPrimaryPortNumber:];
-[ACCTransportIOAccessoryBase setUpstreamManagerService:];
-[ACCTransportIOAccessoryBase transmitData:];
-[ACCTransportIOAccessoryBase upstreamManagerService];
```

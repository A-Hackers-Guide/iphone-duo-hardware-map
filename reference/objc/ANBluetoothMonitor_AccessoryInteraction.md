# `ANBluetoothMonitor`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
^{BTSessionImpl=} _session;
@? _connectionStateupdateHandler;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (T@?,C,V_connectionStateupdateHandler) connectionStateupdateHandler;
```

## Instance methods

```
-[ANBluetoothMonitor initWithQueue:];
-[ANBluetoothMonitor dealloc];
-[ANBluetoothMonitor queue];
-[ANBluetoothMonitor setQueue:];
-[ANBluetoothMonitor configureBluetoothSession];
-[ANBluetoothMonitor connectionStateupdateHandler];
-[ANBluetoothMonitor onBluetoothServiceUpdateForDevice:services:eventType:event:result:];
-[ANBluetoothMonitor onBluetoothSession:event:result:];
-[ANBluetoothMonitor setConnectionStateupdateHandler:];
```

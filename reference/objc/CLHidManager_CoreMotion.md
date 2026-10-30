# `CLHidManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"<CLHidManagerDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
@"HIDManager" _manager;
@"NSMutableArray" _clientDevices;
```

## Properties

```
@property (T@"<CLHidManagerDelegate>",N,V_delegate) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_delegateQueue) delegateQueue;
@property (T@"HIDManager",R,N,V_manager) manager;
@property (T@"NSMutableArray",&,N,V_clientDevices) clientDevices;
```

## Instance methods

```
-[CLHidManager initWithDelegate:queue:];
-[CLHidManager dealloc];
-[CLHidManager manager];
-[CLHidManager setDelegate:];
-[CLHidManager delegate];
-[CLHidManager delegateQueue];
-[CLHidManager activateClientDevice:];
-[CLHidManager clientDeviceMatchingDict:];
-[CLHidManager clientDeviceMatchingHIDDevice:];
-[CLHidManager clientDevices];
-[CLHidManager deviceForMatchingDictionary:];
-[CLHidManager hidDeviceFromEnumeratedDevicesMatching:];
-[CLHidManager registerForDeviceMatching:];
-[CLHidManager sendMonitorUpdateForDevice:added:];
-[CLHidManager setClientDevices:];
-[CLHidManager unregisterForDeviceMatching:];
-[CLHidManager updateClientDeviceWithHidDevice:added:];
```

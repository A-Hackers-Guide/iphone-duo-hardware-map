# `HIDTimeSync`

- Image: [`/System/Library/PrivateFrameworks/HID.framework/HID`](../userland/System__Library__PrivateFrameworks__HID.framework__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 4 properties, 22 instance methods, 5 class methods

## Instance variables

```
AI _state;
@"HIDDevice" _device;
@"HIDEventService" _service;
@"HIDServiceClient" _client;
^{IONotificationPort=} _propertyPort;
I _propertyNotify;
@"NSObject<OS_dispatch_queue>" _queue;
@? _eventHandler;
@? _cancelHandler;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_queue) queue;
@property (T@?,R,N,V_eventHandler) eventHandler;
@property (T@?,R,N,V_cancelHandler) cancelHandler;
@property (TI,N) state;
```

## Class methods

```
+[HIDTimeSync findDeviceForServiceID:];
+[HIDTimeSync timeSyncFromHIDDevice:];
+[HIDTimeSync timeSyncFromHIDEventService:];
+[HIDTimeSync timeSyncFromHIDServiceClient:];
+[HIDTimeSync timeSyncFromProtocol:];
```

## Instance methods

```
-[HIDTimeSync properties];
-[HIDTimeSync eventHandler];
-[HIDTimeSync setState:];
-[HIDTimeSync setEventHandler:];
-[HIDTimeSync init];
-[HIDTimeSync initInternal];
-[HIDTimeSync dealloc];
-[HIDTimeSync queue];
-[HIDTimeSync setDispatchQueue:];
-[HIDTimeSync setCancelHandler:];
-[HIDTimeSync activate];
-[HIDTimeSync cancel];
-[HIDTimeSync state];
-[HIDTimeSync handleCancel];
-[HIDTimeSync cancelHandler];
-[HIDTimeSync dataFromSyncedTime:error:];
-[HIDTimeSync findDevice];
-[HIDTimeSync handleActivate];
-[HIDTimeSync handlePropertyUpdate:];
-[HIDTimeSync registerPropertyNotification:];
-[HIDTimeSync setProviderProperty:forKey:];
-[HIDTimeSync syncedTimeFromData:error:];
```

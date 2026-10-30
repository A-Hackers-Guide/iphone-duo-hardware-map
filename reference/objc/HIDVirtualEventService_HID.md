# `HIDVirtualEventService`

- Image: [`/System/Library/PrivateFrameworks/HID.framework/HID`](../userland/System__Library__PrivateFrameworks__HID.framework__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
Ai _state;
@"<HIDVirtualEventServiceDelegate>" _delegate;
@"HIDEventSystemClient" _client;
@"HIDServiceClient" _serviceClient;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T@"HIDEventSystemClient",&,V_client) client;
@property (T@"HIDServiceClient",&,V_serviceClient) serviceClient;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
@property (TQ,R) serviceID;
@property (T@"<HIDVirtualEventServiceDelegate>",W,V_delegate) delegate;
```

## Instance methods

```
-[HIDVirtualEventService dispatchEvent:];
-[HIDVirtualEventService serviceID];
-[HIDVirtualEventService init];
-[HIDVirtualEventService setServiceClient:];
-[HIDVirtualEventService dealloc];
-[HIDVirtualEventService queue];
-[HIDVirtualEventService setClient:];
-[HIDVirtualEventService setDispatchQueue:];
-[HIDVirtualEventService setCancelHandler:];
-[HIDVirtualEventService setDelegate:];
-[HIDVirtualEventService activate];
-[HIDVirtualEventService delegate];
-[HIDVirtualEventService description];
-[HIDVirtualEventService serviceClient];
-[HIDVirtualEventService cancel];
-[HIDVirtualEventService client];
-[HIDVirtualEventService setQueue:];
```

# `HIDManager`

- Image: [`/System/Library/PrivateFrameworks/HID.framework/HID`](../userland/System__Library__PrivateFrameworks__HID.framework__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 1 properties, 19 instance methods, 0 class methods

## Instance variables

```
^{__IOHIDManager=} _manager;
@? _elementHandler;
@? _deviceNotificationHandler;
@? _inputReportHandler;
@? _cancelHandler;
B _activated;
{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I} _handlerLock;
```

## Properties

```
@property (T@"NSArray",R) devices;
```

## Instance methods

```
-[HIDManager propertyForKey:];
-[HIDManager open];
-[HIDManager setProperty:forKey:];
-[HIDManager close];
-[HIDManager init];
-[HIDManager dealloc];
-[HIDManager setDispatchQueue:];
-[HIDManager setCancelHandler:];
-[HIDManager initWithOptions:];
-[HIDManager devices];
-[HIDManager activate];
-[HIDManager description];
-[HIDManager cancel];
-[HIDManager setDeviceMatching:];
-[HIDManager setDeviceNotificationHandler:];
-[HIDManager setInputReportHandler:];
-[HIDManager setInputElementMatching:];
-[HIDManager openWithOptions:];
-[HIDManager setInputElementHandler:];
```

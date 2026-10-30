# `HIDEventSystemClient`

- Image: [`/System/Library/PrivateFrameworks/HID.framework/HID`](../userland/System__Library__PrivateFrameworks__HID.framework__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 1 properties, 18 instance methods, 0 class methods

## Instance variables

```
^{__IOHIDEventSystemClient=} _client;
@? _eventHandler;
@? _resetHandler;
@? _filterHandler;
@? _serviceHandler;
@? _propertyChangedHandler;
@? _cancelHandler;
B _activated;
{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I} _handlerLock;
```

## Properties

```
@property (T@"NSArray",R) services;
```

## Instance methods

```
-[HIDEventSystemClient propertyForKey:];
-[HIDEventSystemClient setProperty:forKey:];
-[HIDEventSystemClient setMatching:];
-[HIDEventSystemClient setResetHandler:];
-[HIDEventSystemClient setEventHandler:];
-[HIDEventSystemClient services];
-[HIDEventSystemClient setServiceNotificationHandler:];
-[HIDEventSystemClient initWithType:];
-[HIDEventSystemClient dealloc];
-[HIDEventSystemClient setDispatchQueue:];
-[HIDEventSystemClient setCancelHandler:];
-[HIDEventSystemClient setPropertyChangedHandler:matching:];
-[HIDEventSystemClient activate];
-[HIDEventSystemClient description];
-[HIDEventSystemClient initWithType:andAttributes:];
-[HIDEventSystemClient setEventFilterHandler:];
-[HIDEventSystemClient cancel];
-[HIDEventSystemClient client];
```

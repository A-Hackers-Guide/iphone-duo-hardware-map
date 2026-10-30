# `IOHIDObsoleteDeviceClass`

- Image: [`/System/Library/PrivateFrameworks/HID.framework/HID`](../userland/System__Library__PrivateFrameworks__HID.framework__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOHIDDeviceClass`
- 9 instance variables, 0 properties, 11 instance methods, 0 class methods

## Instance variables

```
^{IOHIDDeviceInterface122=^v^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?} _interface;
^{IONotificationPort=} _notifyPort;
I _notification;
^? _removalCallback;
^v _removalTarget;
^v _removalRefcon;
^? _reportCallback;
^v _reportCallbackTarget;
^v _reportCallbackRefcon;
```

## Instance methods

```
-[IOHIDObsoleteDeviceClass init];
-[IOHIDObsoleteDeviceClass copyMatchingElements:element:];
-[IOHIDObsoleteDeviceClass getElementValue:value:options:];
-[IOHIDObsoleteDeviceClass allocQueue];
-[IOHIDObsoleteDeviceClass dealloc];
-[IOHIDObsoleteDeviceClass allocOutputTransaction];
-[IOHIDObsoleteDeviceClass start:service:];
-[IOHIDObsoleteDeviceClass queryInterface:outInterface:];
-[IOHIDObsoleteDeviceClass setElementValue:value:];
-[IOHIDObsoleteDeviceClass setInterruptReportHandlerCallback:reportBufferSize:callback:callbackTarget:callbackRefcon:];
-[IOHIDObsoleteDeviceClass setRemovalCallback:removalTarget:removalRefcon:];
```

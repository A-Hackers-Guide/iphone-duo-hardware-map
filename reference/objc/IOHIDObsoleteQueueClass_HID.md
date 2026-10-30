# `IOHIDObsoleteQueueClass`

- Image: [`/System/Library/PrivateFrameworks/HID.framework/HID`](../userland/System__Library__PrivateFrameworks__HID.framework__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOHIDQueueClass`
- 4 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
^{IOHIDQueueInterface=^v^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?} _interface;
^? _eventCallback;
^v _eventCallbackTarget;
^v _eventCallbackRefcon;
```

## Instance methods

```
-[IOHIDObsoleteQueueClass initWithDevice:];
-[IOHIDObsoleteQueueClass dealloc];
-[IOHIDObsoleteQueueClass getNextEvent:];
-[IOHIDObsoleteQueueClass queryInterface:outInterface:];
-[IOHIDObsoleteQueueClass setEventCallout:callbackTarget:callbackRefcon:];
```

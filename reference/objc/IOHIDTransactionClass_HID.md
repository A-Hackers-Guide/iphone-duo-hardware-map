# `IOHIDTransactionClass`

- Image: [`/System/Library/PrivateFrameworks/HID.framework/HID`](../userland/System__Library__PrivateFrameworks__HID.framework__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOHIDIUnknown2`
- 6 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
^{IOHIDDeviceTransactionInterface=^v^?^?^?^?^?^?^?^?^?^?^?^?^?} _interface;
I _direction;
@"NSMutableArray" _elements;
{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I} _callbackLock;
@"NSMutableSet" _pendingCallbacks;
@"IOHIDDeviceClass" _device;
```

## Instance methods

```
-[IOHIDTransactionClass removeElement:];
-[IOHIDTransactionClass initWithDevice:];
-[IOHIDTransactionClass clear];
-[IOHIDTransactionClass setDevice:];
-[IOHIDTransactionClass addElement:];
-[IOHIDTransactionClass device];
-[IOHIDTransactionClass dealloc];
-[IOHIDTransactionClass setDirection:];
-[IOHIDTransactionClass queryInterface:outInterface:];
-[IOHIDTransactionClass getAsyncEventSource:];
-[IOHIDTransactionClass commit:timeout:callback:options:];
-[IOHIDTransactionClass containsElement:value:];
-[IOHIDTransactionClass getDirection:];
-[IOHIDTransactionClass getValue:value:options:];
-[IOHIDTransactionClass setValue:value:options:];
```

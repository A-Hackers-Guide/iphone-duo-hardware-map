# `IOHIDQueueClass`

- Image: [`/System/Library/PrivateFrameworks/HID.framework/HID`](../userland/System__Library__PrivateFrameworks__HID.framework__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOHIDIUnknown2`
- 16 instance variables, 0 properties, 20 instance methods, 0 class methods

## Instance variables

```
^{IOHIDDeviceQueueInterface=^v^?^?^?^?^?^?^?^?^?^?^?^?^?} _queue;
@"IOHIDDeviceClass" _device;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _queueLock;
I _port;
^{__CFMachPort=} _machPort;
^{__CFRunLoopSource=} _runLoopSource;
^{_IODataQueueMemory=III[1{_IODataQueueEntry=I[4C]}]} _queueMemory;
Q _queueMemorySize;
B _queueSizeChanged;
I _lastTail;
I _depth;
Q _queueToken;
^? _valueAvailableCallback;
^v _valueAvailableContext;
^v _usageAnalytics;
^{_IOHIDQueueHeader=AQ} _queueHeader;
```

## Instance methods

```
-[IOHIDQueueClass setDepth:];
-[IOHIDQueueClass removeElement:];
-[IOHIDQueueClass queueCallback:msg:size:info:];
-[IOHIDQueueClass initWithDevice:];
-[IOHIDQueueClass addElement:];
-[IOHIDQueueClass stop];
-[IOHIDQueueClass dealloc];
-[IOHIDQueueClass start];
-[IOHIDQueueClass initWithDevice:port:source:];
-[IOHIDQueueClass copyNextValue:];
-[IOHIDQueueClass mapMemory];
-[IOHIDQueueClass updateUsageAnalytics];
-[IOHIDQueueClass getDepth:];
-[IOHIDQueueClass containsElement:pValue:];
-[IOHIDQueueClass signalQueueEmpty];
-[IOHIDQueueClass unmapMemory];
-[IOHIDQueueClass setupAnalytics];
-[IOHIDQueueClass queryInterface:outInterface:];
-[IOHIDQueueClass getAsyncEventSource:];
-[IOHIDQueueClass setValueAvailableCallback:context:];
```

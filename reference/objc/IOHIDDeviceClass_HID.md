# `IOHIDDeviceClass`

- Image: [`/System/Library/PrivateFrameworks/HID.framework/HID`](../userland/System__Library__PrivateFrameworks__HID.framework__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOHIDPlugin`
- 22 instance variables, 4 properties, 36 instance methods, 0 class methods

## Instance variables

```
I _service;
I _port;
^{__CFRunLoopSource=} _runLoopSource;
@"IOHIDQueueClass" _queue;
^{IOHIDDeviceTimeStampedDeviceInterface=^v^?^?^?^?^?^?^?^?^?^?^?^?^?^?^?} _device;
I _connect;
{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I} _deviceLock;
^{__CFMachPort=} _machPort;
B _opened;
B _tccRequested;
B _tccGranted;
@"NSArray" _elements;
@"NSArray" _sortedElements;
@"NSArray" _reportElements;
@"NSMutableDictionary" _properties;
{os_unfair_recursive_lock_s="ourl_lock"{os_unfair_lock_s="_os_unfair_lock_opaque"I}"ourl_count"I} _callbackLock;
^? _inputReportCallback;
^? _inputReportTimestampCallback;
^v _inputReportContext;
* _inputReportBuffer;
q _inputReportBufferLength;
@"NSMutableSet" _pendingCallbacks;
```

## Properties

```
@property (TI,R,V_port) port;
@property (T^{__CFRunLoopSource=},R,V_runLoopSource) runLoopSource;
@property (TI,R,V_connect) connect;
@property (TI,R,V_service) service;
```

## Instance methods

```
-[IOHIDDeviceClass connect];
-[IOHIDDeviceClass setValue:value:timeout:callback:context:options:];
-[IOHIDDeviceClass close:];
-[IOHIDDeviceClass open:];
-[IOHIDDeviceClass createReportElements:outError:];
-[IOHIDDeviceClass stop];
-[IOHIDDeviceClass initWithFactory:];
-[IOHIDDeviceClass copyMatchingElements:elements:options:];
-[IOHIDDeviceClass dealloc];
-[IOHIDDeviceClass setInputReportWithTimeStampCallback:reportLength:callback:context:options:];
-[IOHIDDeviceClass initQueue];
-[IOHIDDeviceClass setInputReportCallback:reportLength:callback:context:options:];
-[IOHIDDeviceClass initElements];
-[IOHIDDeviceClass setProperty:property:];
-[IOHIDDeviceClass getElement:];
-[IOHIDDeviceClass getValue:value:timeout:callback:context:options:];
-[IOHIDDeviceClass getElementCount:andReportCount:];
-[IOHIDDeviceClass elementsSortedByCookie:];
-[IOHIDDeviceClass copyObsoleteDictionary:];
-[IOHIDDeviceClass runLoopSource];
-[IOHIDDeviceClass port];
-[IOHIDDeviceClass propertyForElementKey:];
-[IOHIDDeviceClass start:service:];
-[IOHIDDeviceClass service];
-[IOHIDDeviceClass valueAvailableCallback:];
-[IOHIDDeviceClass initConnect];
-[IOHIDDeviceClass initPort];
-[IOHIDDeviceClass releaseReport:];
-[IOHIDDeviceClass createElements:outError:];
-[IOHIDDeviceClass probe:service:outScore:];
-[IOHIDDeviceClass queryInterface:outInterface:];
-[IOHIDDeviceClass getProperty:property:];
-[IOHIDDeviceClass getAsyncEventSource:];
-[IOHIDDeviceClass getPort];
-[IOHIDDeviceClass getReport:reportID:report:reportLength:timeout:callback:context:options:];
-[IOHIDDeviceClass setReport:reportID:report:reportLength:timeout:callback:context:options:];
```

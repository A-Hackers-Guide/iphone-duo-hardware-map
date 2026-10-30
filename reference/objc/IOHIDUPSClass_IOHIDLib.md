# `IOHIDUPSClass`

- Image: [`/System/Library/Extensions/IOHIDFamily.kext/PlugIns/IOHIDLib.plugin/IOHIDLib`](../userland/System__Library__Extensions__IOHIDFamily.kext__PlugIns__IOHIDLib.plugin__IOHIDLib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `IOHIDPlugin`
- 18 instance variables, 0 properties, 21 instance methods, 0 class methods

## Instance variables

```
^{IOUPSPlugInInterface_v140=^v^?^?^?^?^?^?^?^?^?} _ups;
^^{IOHIDDeviceTimeStampedDeviceInterface} _device;
^^{IOHIDDeviceQueueInterface} _queue;
^^{IOHIDDeviceTransactionInterface} _transaction;
@"NSMutableDictionary" _properties;
@"NSMutableSet" _capabilities;
@"NSMutableDictionary" _upsEvent;
@"NSMutableDictionary" _upsUpdatedEvent;
@"NSMutableDictionary" _debugInformation;
{?="input"@"NSMutableArray""output"@"NSMutableArray""feature"@"NSMutableArray"} _elements;
@"NSMutableArray" _commandElements;
@"NSMutableArray" _eventElements;
^? _eventCallback;
^v _eventTarget;
^v _eventRefcon;
@"NSTimer" _timer;
^{__CFRunLoopSource=} _runLoopSource;
d _powerFeaturePollInterval;
```

## Instance methods

```
-[IOHIDUPSClass init];
-[IOHIDUPSClass stop];
-[IOHIDUPSClass dealloc];
-[IOHIDUPSClass start:service:];
-[IOHIDUPSClass valueAvailableCallback:];
-[IOHIDUPSClass probe:service:outScore:];
-[IOHIDUPSClass queryInterface:outInterface:];
-[IOHIDUPSClass sendCommand:];
-[IOHIDUPSClass updateEvent];
-[IOHIDUPSClass pollEventUpdate];
-[IOHIDUPSClass updateElements:];
-[IOHIDUPSClass setEventCallback:target:refcon:];
-[IOHIDUPSClass copyElements:psKey:];
-[IOHIDUPSClass createAsyncEventSource:];
-[IOHIDUPSClass getCapabilities:];
-[IOHIDUPSClass getEvent:];
-[IOHIDUPSClass getProperties:];
-[IOHIDUPSClass initialEventUpdate];
-[IOHIDUPSClass latestElement:psKey:];
-[IOHIDUPSClass parseElements:];
-[IOHIDUPSClass parseProperties:];
```

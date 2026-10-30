# `/System/Library/CoreAccessories/PlugIns/Features/HID.feature/HID`

iOS 27.2 dyld shared cache image. Version `1219.52.1.0.0`. **[DSC]**

## Linked libraries (6)

- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/PrivateFrameworks/AccessoryHID.framework/AccessoryHID`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`

## Objective-C: 3 classes, 4 protocols, 94 methods, 36 properties

### Class pages

Every class and protocol, with its methods: [`ACCFeaturePluginHID`](../objc/ACCFeaturePluginHID_HID.md), [`ACCFeaturePluginHIDDescriptor`](../objc/ACCFeaturePluginHIDDescriptor_HID.md), [`ACCFeaturePluginHIDProvider`](../objc/ACCFeaturePluginHIDProvider_HID.md), [`ACCFeaturePluginProtocol`](../objc/ACCFeaturePluginProtocol_HID.protocol.md), [`ACCPluginProtocol`](../objc/ACCPluginProtocol_HID.protocol.md), [`AccessoryHIDClientProtocol`](../objc/AccessoryHIDClientProtocol_HID.protocol.md), [`NSObject`](../objc/NSObject_HID.protocol.md)

### Classes

`ACCFeaturePluginHID`, `ACCFeaturePluginHIDDescriptor`, `ACCFeaturePluginHIDProvider`

### Protocols

`ACCFeaturePluginProtocol`, `ACCPluginProtocol`, `AccessoryHIDClientProtocol`, `NSObject`

### Properties

```
@property (T@"NSString",R,N) pluginName;
@property (TB,R,N) isRunning;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,N,V_isRunning) isRunning;
@property (T@"ACCFeaturePluginHIDProvider",&,N,V_hidProvider) hidProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) pluginName;
@property (TB,N,V_isShuttingDown) isShuttingDown;
@property (TC,N,V_getReportID) getReportID;
@property (Ti,N,V_getReportType) getReportType;
@property (T@"NSMutableData",&,N,V_getReportBuffer) getReportBuffer;
@property (Ti,N,V_getReportResult) getReportResult;
@property (T^{__IOHIDUserDevice=},N,V_deviceRef) deviceRef;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_hidCallbackQueue) hidCallbackQueue;
@property (T@"NSObject<OS_dispatch_semaphore>",&,N,V_getReportSemaphore) getReportSemaphore;
@property (T@"NSObject<OS_dispatch_source>",&,N,V_registerDeviceMatchingTimerSource) registerDeviceMatchingTimerSource;
@property (T@?,C,N,V_sendOutReport) sendOutReport;
@property (T@?,C,N,V_sendGetReport) sendGetReport;
@property (T@?,C,N,V_sendComponentUpdate) sendComponentUpdate;
@property (T^{__IOHIDEventSystemClient=},V_hidEventSystemClientRef) hidEventSystemClientRef;
@property (TB,N,V_isReady) isReady;
@property (T@"NSMutableArray",&,N,V_initialReportCache) initialReportCache;
@property (T@"NSString",R,N,V_hidDeviceUUIDStr) hidDeviceUUIDStr;
@property (T@"NSMutableArray",&,N,V_descriptorUUIDs) descriptorUUIDs;
@property (T@"AccessoryHIDClient",&,V_hidClient) hidClient;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_hidProviderLock) hidProviderLock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Strings (55)

```
(null)
YES
VendorID
<%@: %p> isRunning: %s
-[ACCFeaturePluginHIDDescriptor initWithDecriptorInfo:sendOutReport:sendGetReport:sendComponentUpdate:]
HIDDeviceQueue%@
%02X
CountryCode
IAPHIDAccessoryCategory
Transport
Manufacturer
__hidServiceRegisteredCallback
com.apple.accessories.feature-plugins
<print error>
hidProviderSerialQueue
v24@?0@\"NSString\"8@\"NSData\"16
ProductID
SerialNumber
ReportDescriptor
Authenticated
PhysicalDeviceUniqueID
v8@?0
v32@?0@\"NSString\"8@\"NSNumber\"16@\"NSNumber\"24
<Undefined>
%02X 
NO
v20@?0@\"NSString\"8B16
VersionNumber
Product
IAPHIDServiceRegistryEntryID
General
stop registerDeviceMatchingTimer, %@
handleHIDComponentUpdate: not ready, remove %lu cached reports.
Starting HID feature plugin...
Make sure you have called init_logging()!\ngLogObjects: %p, gNumLogObjects: %d
%s: descriptorInfo %@ 
IOHIDUserDeviceCreate failed
IOHIDUserDeviceCreate failed to create hidProperties dictionary
ERROR: _hidEventSystemClientRef not NULL after CFReleaseSafe
reportLength < 0, not sending report
reportLength < 0, not requesting hid report
Stopping HID feature plugin...
registerDeviceMatchingTimer fired! %@ call handleHIDComponentUpdate true
Finished running _hidCallbackQueue
handling HID report failed 0x%x.
handleHIDComponentUpdate: ready, handle %lu cached reports.
%s: descriptorUUID %@, target (%d), service %@
Category missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Failed to create os_log_t object %s: %s!
start registerDeviceMatchingTimer, %@
handling HID report failed, not ready and no cache.
handleHIDComponentUpdate: ready, no cached reports.
Subsystem missing for logging module %d!\n(Check LoggingModuleEntry_t table)
Created log object %s: %s
Created %d log object(s)!
```

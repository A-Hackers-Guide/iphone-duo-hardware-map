# `ACCFeaturePluginHIDDescriptor`

- Image: [`/System/Library/CoreAccessories/PlugIns/Features/HID.feature/HID`](../userland/System__Library__CoreAccessories__PlugIns__Features__HID.feature__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 16 instance variables, 16 properties, 40 instance methods, 0 class methods

## Instance variables

```
B _isShuttingDown;
C _getReportID;
B _isReady;
i _getReportType;
i _getReportResult;
@"NSString" _hidDeviceUUIDStr;
@"NSMutableData" _getReportBuffer;
^{__IOHIDUserDevice=} _deviceRef;
@"NSObject<OS_dispatch_queue>" _hidCallbackQueue;
@"NSObject<OS_dispatch_semaphore>" _getReportSemaphore;
@"NSObject<OS_dispatch_source>" _registerDeviceMatchingTimerSource;
@? _sendOutReport;
@? _sendGetReport;
@? _sendComponentUpdate;
^{__IOHIDEventSystemClient=} _hidEventSystemClientRef;
@"NSMutableArray" _initialReportCache;
```

## Properties

```
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
```

## Instance methods

```
-[ACCFeaturePluginHIDDescriptor isReady];
-[ACCFeaturePluginHIDDescriptor setIsReady:];
-[ACCFeaturePluginHIDDescriptor dealloc];
-[ACCFeaturePluginHIDDescriptor deviceRef];
-[ACCFeaturePluginHIDDescriptor isShuttingDown];
-[ACCFeaturePluginHIDDescriptor setIsShuttingDown:];
-[ACCFeaturePluginHIDDescriptor getReportBuffer];
-[ACCFeaturePluginHIDDescriptor handleInReport:];
-[ACCFeaturePluginHIDDescriptor getReportResult];
-[ACCFeaturePluginHIDDescriptor setGetReportID:];
-[ACCFeaturePluginHIDDescriptor getReportID];
-[ACCFeaturePluginHIDDescriptor getReportSemaphore];
-[ACCFeaturePluginHIDDescriptor getReportType];
-[ACCFeaturePluginHIDDescriptor handleGetReport:reportID:report:];
-[ACCFeaturePluginHIDDescriptor handleGetReportResponse:reportID:report:];
-[ACCFeaturePluginHIDDescriptor handleHIDComponentUpdate:];
-[ACCFeaturePluginHIDDescriptor handleOutReport:];
-[ACCFeaturePluginHIDDescriptor hidCallbackQueue];
-[ACCFeaturePluginHIDDescriptor hidDeviceUUIDStr];
-[ACCFeaturePluginHIDDescriptor hidEventSystemClientRef];
-[ACCFeaturePluginHIDDescriptor initWithDecriptorInfo:sendOutReport:sendGetReport:sendComponentUpdate:];
-[ACCFeaturePluginHIDDescriptor initialReportCache];
-[ACCFeaturePluginHIDDescriptor registerDeviceMatchingTimerSource];
-[ACCFeaturePluginHIDDescriptor removeDescriptor];
-[ACCFeaturePluginHIDDescriptor sendComponentUpdate];
-[ACCFeaturePluginHIDDescriptor sendGetReport];
-[ACCFeaturePluginHIDDescriptor sendOutReport];
-[ACCFeaturePluginHIDDescriptor setDeviceRef:];
-[ACCFeaturePluginHIDDescriptor setGetReportBuffer:];
-[ACCFeaturePluginHIDDescriptor setGetReportResult:];
-[ACCFeaturePluginHIDDescriptor setGetReportSemaphore:];
-[ACCFeaturePluginHIDDescriptor setGetReportType:];
-[ACCFeaturePluginHIDDescriptor setHidCallbackQueue:];
-[ACCFeaturePluginHIDDescriptor setHidEventSystemClientRef:];
-[ACCFeaturePluginHIDDescriptor setInitialReportCache:];
-[ACCFeaturePluginHIDDescriptor setRegisterDeviceMatchingTimerSource:];
-[ACCFeaturePluginHIDDescriptor setSendComponentUpdate:];
-[ACCFeaturePluginHIDDescriptor setSendGetReport:];
-[ACCFeaturePluginHIDDescriptor setSendOutReport:];
-[ACCFeaturePluginHIDDescriptor startHIDEventSystemListener:];
```

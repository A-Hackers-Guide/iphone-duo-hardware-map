# `HIDRemoteDevice`

- Image: [`/System/Library/PrivateFrameworks/RemoteHID.framework/RemoteHID`](../userland/System__Library__PrivateFrameworks__RemoteHID.framework__RemoteHID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `HIDUserDevice`
- 15 instance variables, 15 properties, 36 instance methods, 0 class methods

## Instance variables

```
C _transportVersion;
C _side;
B _enableTS;
B _cancelled;
B _waitForReport;
I _propertyNotify;
i _lastSetReportStatus;
I _handleReportCount;
I _handleReportError;
Q _endpointID;
Q _deviceID;
^{IONotificationPort=} _propertyPort;
@"HIDRemoteEndpoint" _endpoint;
@"NSObject<OS_dispatch_semaphore>" _semaphore;
@"NSData" _lastGetReport;
```

## Properties

```
@property (TB,V_cancelled) cancelled;
@property (T@"NSObject<OS_dispatch_semaphore>",&,V_semaphore) semaphore;
@property (T@"NSData",&,V_lastGetReport) lastGetReport;
@property (Ti,V_lastSetReportStatus) lastSetReportStatus;
@property (TB,V_waitForReport) waitForReport;
@property (TI,V_handleReportCount) handleReportCount;
@property (TI,V_handleReportError) handleReportError;
@property (TQ,V_endpointID) endpointID;
@property (TQ,V_deviceID) deviceID;
@property (TC,V_transportVersion) transportVersion;
@property (TC,V_side) side;
@property (T^{IONotificationPort=},V_propertyPort) propertyPort;
@property (TI,V_propertyNotify) propertyNotify;
@property (TB,V_enableTS) enableTS;
@property (T@"HIDRemoteEndpoint",&,V_endpoint) endpoint;
```

## Instance methods

```
-[HIDRemoteDevice cancelled];
-[HIDRemoteDevice initWithProperties:];
-[HIDRemoteDevice setEndpoint:];
-[HIDRemoteDevice semaphore];
-[HIDRemoteDevice setCancelled:];
-[HIDRemoteDevice deviceID];
-[HIDRemoteDevice side];
-[HIDRemoteDevice endpoint];
-[HIDRemoteDevice setDeviceID:];
-[HIDRemoteDevice description];
-[HIDRemoteDevice endpointID];
-[HIDRemoteDevice setEndpointID:];
-[HIDRemoteDevice setSemaphore:];
-[HIDRemoteDevice setSide:];
-[HIDRemoteDevice enableTS];
-[HIDRemoteDevice getLastGetReport];
-[HIDRemoteDevice getLastSetReportStatus];
-[HIDRemoteDevice getReportHandler:reportID:report:reportLength:];
-[HIDRemoteDevice handleReportCount];
-[HIDRemoteDevice handleReportError];
-[HIDRemoteDevice lastGetReport];
-[HIDRemoteDevice lastSetReportStatus];
-[HIDRemoteDevice propertyNotify];
-[HIDRemoteDevice propertyPort];
-[HIDRemoteDevice setEnableTS:];
-[HIDRemoteDevice setHandleReportCount:];
-[HIDRemoteDevice setHandleReportError:];
-[HIDRemoteDevice setLastGetReport:];
-[HIDRemoteDevice setLastSetReportStatus:];
-[HIDRemoteDevice setPropertyNotify:];
-[HIDRemoteDevice setPropertyPort:];
-[HIDRemoteDevice setReportHandler:reportID:status:];
-[HIDRemoteDevice setTransportVersion:];
-[HIDRemoteDevice setWaitForReport:];
-[HIDRemoteDevice transportVersion];
-[HIDRemoteDevice waitForReport];
```

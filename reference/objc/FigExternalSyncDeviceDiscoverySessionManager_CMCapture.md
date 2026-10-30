# `FigExternalSyncDeviceDiscoverySessionManager`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 18 instance methods, 2 class methods

## Instance variables

```
I _firstMatchIterator;
I _serviceNotification;
^{IONotificationPort=} _ioServiceNotificationPort;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableDictionary" _managedExternalSyncDevices;
@"NSMutableDictionary" _activeClients;
B _observingSSAMEvents;
```

## Class methods

```
+[FigExternalSyncDeviceDiscoverySessionManager initialize];
+[FigExternalSyncDeviceDiscoverySessionManager sharedFigExternalSyncDeviceDiscoverySessionManager];
```

## Instance methods

```
-[FigExternalSyncDeviceDiscoverySessionManager _removeDevice:];
-[FigExternalSyncDeviceDiscoverySessionManager observeValueForKeyPath:ofObject:change:context:];
-[FigExternalSyncDeviceDiscoverySessionManager init];
-[FigExternalSyncDeviceDiscoverySessionManager dealloc];
-[FigExternalSyncDeviceDiscoverySessionManager _currentDevices];
-[FigExternalSyncDeviceDiscoverySessionManager _activateSyncDevices];
-[FigExternalSyncDeviceDiscoverySessionManager _addDevice:];
-[FigExternalSyncDeviceDiscoverySessionManager _deactivateSyncDevices];
-[FigExternalSyncDeviceDiscoverySessionManager _forceNotifyDelegatesDevicesChanged];
-[FigExternalSyncDeviceDiscoverySessionManager _handleDeviceEvent:];
-[FigExternalSyncDeviceDiscoverySessionManager _setupDeviceDeviceManagmentMonitoring];
-[FigExternalSyncDeviceDiscoverySessionManager _setupDeviceObservationNotifications];
-[FigExternalSyncDeviceDiscoverySessionManager _teardownDeviceDeviceManagmentMonitoring];
-[FigExternalSyncDeviceDiscoverySessionManager _teardownDeviceObservationNotifications];
-[FigExternalSyncDeviceDiscoverySessionManager currentDevices];
-[FigExternalSyncDeviceDiscoverySessionManager deviceDisconnectedEvent:];
-[FigExternalSyncDeviceDiscoverySessionManager registerClient:delegate:];
-[FigExternalSyncDeviceDiscoverySessionManager unregisterAndCleanupClient:];
```

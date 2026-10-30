# `USBCameraKitHubMonitor`

- Image: [`/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit`](../userland/System__Library__CoreAccessories__PlugIns__Platform__IOKit.platform__IOKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 32 instance variables, 32 properties, 78 instance methods, 1 class methods

## Instance variables

```
B _ioUSBCameraKitHubCurrentNeedUpdate;
B _ioUSBCameraKitHubOverCurrentDetected;
I _ioUSB20CameraKitHubNotification;
I _ioUSB20CameraKitHubService;
I _ioUSB20CameraKitHubMatchIterator;
I _ioUSB20CameraKitHubTerminateIterator;
I _ioUSB20CameraKitHubCurrentNeeded;
I _ioUSB20CameraKitHubPortCurrentAllocation;
I _ioUSB20CameraKitHubPortFailedRequestedPower;
I _ioUSB20CameraKitHubExtraRequestedPower;
I _ioUSB20CameraKitHubPortNotification;
I _ioUSB20CameraKitHubPortService;
I _ioUSB20CameraKitHubPortMatchIterator;
I _ioUSB20CameraKitHubPortTerminateIterator;
I _ioUSB30CameraKitHubNotification;
I _ioUSB30CameraKitHubService;
I _ioUSB30CameraKitHubMatchIterator;
I _ioUSB30CameraKitHubTerminateIterator;
I _ioUSB30CameraKitHubCurrentNeeded;
I _ioUSB30CameraKitHubPortCurrentAllocation;
I _ioUSB30CameraKitHubPortFailedRequestedPower;
I _ioUSB30CameraKitHubPortNotification;
I _ioUSB30CameraKitHubPortService;
I _ioUSB30CameraKitHubPortMatchIterator;
I _ioUSB30CameraKitHubPortTerminateIterator;
I _ioUSBCameraKitHubTotalCurrent;
^{IONotificationPort=} _ioUSB20CameraKitHubNotifyPort;
^{IONotificationPort=} _ioUSB20CameraKitHubPortNotifyPort;
^{IONotificationPort=} _ioUSB30CameraKitHubNotifyPort;
^{IONotificationPort=} _ioUSB30CameraKitHubPortNotifyPort;
q _once;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Properties

```
@property (T^{IONotificationPort=},V_ioUSB20CameraKitHubNotifyPort) ioUSB20CameraKitHubNotifyPort;
@property (TI,V_ioUSB20CameraKitHubNotification) ioUSB20CameraKitHubNotification;
@property (TI,V_ioUSB20CameraKitHubService) ioUSB20CameraKitHubService;
@property (TI,V_ioUSB20CameraKitHubMatchIterator) ioUSB20CameraKitHubMatchIterator;
@property (TI,V_ioUSB20CameraKitHubTerminateIterator) ioUSB20CameraKitHubTerminateIterator;
@property (TI,V_ioUSB20CameraKitHubCurrentNeeded) ioUSB20CameraKitHubCurrentNeeded;
@property (TI,V_ioUSB20CameraKitHubPortCurrentAllocation) ioUSB20CameraKitHubPortCurrentAllocation;
@property (TI,V_ioUSB20CameraKitHubPortFailedRequestedPower) ioUSB20CameraKitHubPortFailedRequestedPower;
@property (TI,V_ioUSB20CameraKitHubExtraRequestedPower) ioUSB20CameraKitHubExtraRequestedPower;
@property (T^{IONotificationPort=},V_ioUSB20CameraKitHubPortNotifyPort) ioUSB20CameraKitHubPortNotifyPort;
@property (TI,V_ioUSB20CameraKitHubPortNotification) ioUSB20CameraKitHubPortNotification;
@property (TI,V_ioUSB20CameraKitHubPortService) ioUSB20CameraKitHubPortService;
@property (TI,V_ioUSB20CameraKitHubPortMatchIterator) ioUSB20CameraKitHubPortMatchIterator;
@property (TI,V_ioUSB20CameraKitHubPortTerminateIterator) ioUSB20CameraKitHubPortTerminateIterator;
@property (T^{IONotificationPort=},V_ioUSB30CameraKitHubNotifyPort) ioUSB30CameraKitHubNotifyPort;
@property (TI,V_ioUSB30CameraKitHubNotification) ioUSB30CameraKitHubNotification;
@property (TI,V_ioUSB30CameraKitHubService) ioUSB30CameraKitHubService;
@property (TI,V_ioUSB30CameraKitHubMatchIterator) ioUSB30CameraKitHubMatchIterator;
@property (TI,V_ioUSB30CameraKitHubTerminateIterator) ioUSB30CameraKitHubTerminateIterator;
@property (TI,V_ioUSB30CameraKitHubCurrentNeeded) ioUSB30CameraKitHubCurrentNeeded;
@property (TI,V_ioUSB30CameraKitHubPortCurrentAllocation) ioUSB30CameraKitHubPortCurrentAllocation;
@property (TI,V_ioUSB30CameraKitHubPortFailedRequestedPower) ioUSB30CameraKitHubPortFailedRequestedPower;
@property (T^{IONotificationPort=},V_ioUSB30CameraKitHubPortNotifyPort) ioUSB30CameraKitHubPortNotifyPort;
@property (TI,V_ioUSB30CameraKitHubPortNotification) ioUSB30CameraKitHubPortNotification;
@property (TI,V_ioUSB30CameraKitHubPortService) ioUSB30CameraKitHubPortService;
@property (TI,V_ioUSB30CameraKitHubPortMatchIterator) ioUSB30CameraKitHubPortMatchIterator;
@property (TI,V_ioUSB30CameraKitHubPortTerminateIterator) ioUSB30CameraKitHubPortTerminateIterator;
@property (TI,V_ioUSBCameraKitHubTotalCurrent) ioUSBCameraKitHubTotalCurrent;
@property (TB,V_ioUSBCameraKitHubCurrentNeedUpdate) ioUSBCameraKitHubCurrentNeedUpdate;
@property (TB,V_ioUSBCameraKitHubOverCurrentDetected) ioUSBCameraKitHubOverCurrentDetected;
@property (Tq,V_once) once;
@property (T@"NSObject<OS_dispatch_queue>",&,V_queue) queue;
```

## Class methods

```
+[USBCameraKitHubMonitor sharedMonitor];
```

## Instance methods

```
-[USBCameraKitHubMonitor init];
-[USBCameraKitHubMonitor dealloc];
-[USBCameraKitHubMonitor queue];
-[USBCameraKitHubMonitor setQueue:];
-[USBCameraKitHubMonitor ioUSB20CameraKitHubNotification];
-[USBCameraKitHubMonitor ioUSB30CameraKitHubNotification];
-[USBCameraKitHubMonitor _powerPostCCKHubChangeNotification];
-[USBCameraKitHubMonitor _setOvercurrentSiphoning:forUUID:];
-[USBCameraKitHubMonitor _updateSiphoningValuesFromDrivers:];
-[USBCameraKitHubMonitor getUSBHubSiphoningCurrentActualRequirementInmA:];
-[USBCameraKitHubMonitor getUSBHubSiphoningCurrentRequirementInmA:];
-[USBCameraKitHubMonitor getUSBHubUnitLoadInmA:];
-[USBCameraKitHubMonitor initUSBCameraKitHubNotifications:];
-[USBCameraKitHubMonitor ioUSB20CameraKitHubCurrentNeeded];
-[USBCameraKitHubMonitor ioUSB20CameraKitHubExtraRequestedPower];
-[USBCameraKitHubMonitor ioUSB20CameraKitHubMatchIterator];
-[USBCameraKitHubMonitor ioUSB20CameraKitHubNotifyPort];
-[USBCameraKitHubMonitor ioUSB20CameraKitHubPortCurrentAllocation];
-[USBCameraKitHubMonitor ioUSB20CameraKitHubPortFailedRequestedPower];
-[USBCameraKitHubMonitor ioUSB20CameraKitHubPortMatchIterator];
-[USBCameraKitHubMonitor ioUSB20CameraKitHubPortNotification];
-[USBCameraKitHubMonitor ioUSB20CameraKitHubPortNotifyPort];
-[USBCameraKitHubMonitor ioUSB20CameraKitHubPortService];
-[USBCameraKitHubMonitor ioUSB20CameraKitHubPortTerminateIterator];
-[USBCameraKitHubMonitor ioUSB20CameraKitHubService];
-[USBCameraKitHubMonitor ioUSB20CameraKitHubTerminateIterator];
-[USBCameraKitHubMonitor ioUSB30CameraKitHubCurrentNeeded];
-[USBCameraKitHubMonitor ioUSB30CameraKitHubMatchIterator];
-[USBCameraKitHubMonitor ioUSB30CameraKitHubNotifyPort];
-[USBCameraKitHubMonitor ioUSB30CameraKitHubPortCurrentAllocation];
-[USBCameraKitHubMonitor ioUSB30CameraKitHubPortFailedRequestedPower];
-[USBCameraKitHubMonitor ioUSB30CameraKitHubPortMatchIterator];
-[USBCameraKitHubMonitor ioUSB30CameraKitHubPortNotification];
-[USBCameraKitHubMonitor ioUSB30CameraKitHubPortNotifyPort];
-[USBCameraKitHubMonitor ioUSB30CameraKitHubPortService];
-[USBCameraKitHubMonitor ioUSB30CameraKitHubPortTerminateIterator];
-[USBCameraKitHubMonitor ioUSB30CameraKitHubService];
-[USBCameraKitHubMonitor ioUSB30CameraKitHubTerminateIterator];
-[USBCameraKitHubMonitor ioUSBCameraKitHubCurrentNeedUpdate];
-[USBCameraKitHubMonitor ioUSBCameraKitHubOverCurrentDetected];
-[USBCameraKitHubMonitor ioUSBCameraKitHubTotalCurrent];
-[USBCameraKitHubMonitor once];
-[USBCameraKitHubMonitor overcurrentState:];
-[USBCameraKitHubMonitor resetOvercurrentSiphoning:];
-[USBCameraKitHubMonitor setIoUSB20CameraKitHubCurrentNeeded:];
-[USBCameraKitHubMonitor setIoUSB20CameraKitHubExtraRequestedPower:];
-[USBCameraKitHubMonitor setIoUSB20CameraKitHubMatchIterator:];
-[USBCameraKitHubMonitor setIoUSB20CameraKitHubNotification:];
-[USBCameraKitHubMonitor setIoUSB20CameraKitHubNotifyPort:];
-[USBCameraKitHubMonitor setIoUSB20CameraKitHubPortCurrentAllocation:];
-[USBCameraKitHubMonitor setIoUSB20CameraKitHubPortFailedRequestedPower:];
-[USBCameraKitHubMonitor setIoUSB20CameraKitHubPortMatchIterator:];
-[USBCameraKitHubMonitor setIoUSB20CameraKitHubPortNotification:];
-[USBCameraKitHubMonitor setIoUSB20CameraKitHubPortNotifyPort:];
-[USBCameraKitHubMonitor setIoUSB20CameraKitHubPortService:];
-[USBCameraKitHubMonitor setIoUSB20CameraKitHubPortTerminateIterator:];
-[USBCameraKitHubMonitor setIoUSB20CameraKitHubService:];
-[USBCameraKitHubMonitor setIoUSB20CameraKitHubTerminateIterator:];
-[USBCameraKitHubMonitor setIoUSB30CameraKitHubCurrentNeeded:];
-[USBCameraKitHubMonitor setIoUSB30CameraKitHubMatchIterator:];
-[USBCameraKitHubMonitor setIoUSB30CameraKitHubNotification:];
-[USBCameraKitHubMonitor setIoUSB30CameraKitHubNotifyPort:];
-[USBCameraKitHubMonitor setIoUSB30CameraKitHubPortCurrentAllocation:];
-[USBCameraKitHubMonitor setIoUSB30CameraKitHubPortFailedRequestedPower:];
-[USBCameraKitHubMonitor setIoUSB30CameraKitHubPortMatchIterator:];
-[USBCameraKitHubMonitor setIoUSB30CameraKitHubPortNotification:];
-[USBCameraKitHubMonitor setIoUSB30CameraKitHubPortNotifyPort:];
-[USBCameraKitHubMonitor setIoUSB30CameraKitHubPortService:];
-[USBCameraKitHubMonitor setIoUSB30CameraKitHubPortTerminateIterator:];
-[USBCameraKitHubMonitor setIoUSB30CameraKitHubService:];
-[USBCameraKitHubMonitor setIoUSB30CameraKitHubTerminateIterator:];
-[USBCameraKitHubMonitor setIoUSBCameraKitHubCurrentNeedUpdate:];
-[USBCameraKitHubMonitor setIoUSBCameraKitHubOverCurrentDetected:];
-[USBCameraKitHubMonitor setIoUSBCameraKitHubTotalCurrent:];
-[USBCameraKitHubMonitor setOnce:];
-[USBCameraKitHubMonitor setOvercurrentSiphoning:];
-[USBCameraKitHubMonitor supportsUSB20CameraKitHub:];
-[USBCameraKitHubMonitor supportsUSB30CameraKitHub:];
```

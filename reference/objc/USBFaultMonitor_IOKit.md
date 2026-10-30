# `USBFaultMonitor`

- Image: [`/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit`](../userland/System__Library__CoreAccessories__PlugIns__Platform__IOKit.platform__IOKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 0 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _usbFaultStates;
@"NSMutableDictionary" _usbFaultStatesSent;
@"NSMutableDictionary" _requestedUSBFaultNotifications;
^{IONotificationPort=} _ioUSBCardReaderNotifyPort;
I _ioUSBCardReaderNotification;
I _ioUSBCardReaderService;
I _ioUSBCardReaderMatchIterator;
I _ioUSBCardReaderTerminateIterator;
Q _uid;
@"NSMutableArray" _registeredUUIDs;
```

## Class methods

```
+[USBFaultMonitor sharedMonitor];
```

## Instance methods

```
-[USBFaultMonitor init];
-[USBFaultMonitor dealloc];
-[USBFaultMonitor initFaultConditionNotifications];
-[USBFaultMonitor checkUSBCardReaderProperty:];
-[USBFaultMonitor getFaultState:];
-[USBFaultMonitor registerFaultInterest:];
-[USBFaultMonitor sendUSBFaultNotification];
-[USBFaultMonitor setFaultState:flag:];
-[USBFaultMonitor startFaultMonitoringForUUID:];
-[USBFaultMonitor stopFaultMonitoringForUUID:];
```

# `USBCableTypeMonitor`

- Image: [`/System/Library/CoreAccessories/PlugIns/Platform/IOKit.platform/IOKit`](../userland/System__Library__CoreAccessories__PlugIns__Platform__IOKit.platform__IOKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 7 instance methods, 2 class methods

## Instance variables

```
Q _uid;
@"NSMutableArray" _registeredUUIDs;
^{IONotificationPort=} _ioUSB30XHCIRemovablePortNotifyPort;
I _ioUSB30XHCIRemovablePortNotification;
I _ioUSB30XHCIRemovablePortService;
I _ioUSB30XHCIRemovablePortMatchIterator;
I _ioUSB30XHCIRemovablePortTerminateIterator;
```

## Class methods

```
+[USBCableTypeMonitor sharedMonitor];
+[USBCableTypeMonitor usbCableType];
```

## Instance methods

```
-[USBCableTypeMonitor init];
-[USBCableTypeMonitor dealloc];
-[USBCableTypeMonitor stopCableTypeMonitoringForUUID:];
-[USBCableTypeMonitor cleanupUSB30XHCIRemovablePortNotifications];
-[USBCableTypeMonitor initUSB30XHCIRemovablePortNotifications];
-[USBCableTypeMonitor sendUSBCableTypeChangedNotification];
-[USBCableTypeMonitor startCableTypeMonitoringForUUID:];
```

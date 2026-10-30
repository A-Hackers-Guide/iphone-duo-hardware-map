# `AccessoryUSBBillboardDeviceListener`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost`](../userland/System__Library__CoreAccessories__PlugIns__Transports__USBHost.transport__USBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 20 instance methods, 0 class methods

## Instance variables

```
B _started;
I _billboardAddedIterator;
I _billboardRemovedIterator;
I _accessoryUSBBillboardDeviceVIDPID;
^{IONotificationPort=} _appleUSBHostBillboardDeviceNotify;
@"NSObject<OS_dispatch_queue>" _accessoryUSBBillboardDeviceListenerQueue;
@"NSMutableSet" _accessoryUSBBillboardDeviceRegistryIDs;
```

## Properties

```
@property (T^{IONotificationPort=},N,V_appleUSBHostBillboardDeviceNotify) appleUSBHostBillboardDeviceNotify;
@property (TI,N,V_billboardAddedIterator) billboardAddedIterator;
@property (TI,N,V_billboardRemovedIterator) billboardRemovedIterator;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_accessoryUSBBillboardDeviceListenerQueue) accessoryUSBBillboardDeviceListenerQueue;
@property (TI,N,V_accessoryUSBBillboardDeviceVIDPID) accessoryUSBBillboardDeviceVIDPID;
@property (TB,N,V_started) started;
@property (T@"NSMutableSet",&,N,V_accessoryUSBBillboardDeviceRegistryIDs) accessoryUSBBillboardDeviceRegistryIDs;
```

## Instance methods

```
-[AccessoryUSBBillboardDeviceListener setStarted:];
-[AccessoryUSBBillboardDeviceListener dealloc];
-[AccessoryUSBBillboardDeviceListener started];
-[AccessoryUSBBillboardDeviceListener AppleUSBHostBillboardDeviceServiceArrived:];
-[AccessoryUSBBillboardDeviceListener AppleUSBHostBillboardDeviceServiceTerminated:];
-[AccessoryUSBBillboardDeviceListener accessoryUSBBillboardDeviceListenerQueue];
-[AccessoryUSBBillboardDeviceListener accessoryUSBBillboardDeviceRegistryIDs];
-[AccessoryUSBBillboardDeviceListener accessoryUSBBillboardDeviceVIDPID];
-[AccessoryUSBBillboardDeviceListener appleUSBHostBillboardDeviceNotify];
-[AccessoryUSBBillboardDeviceListener billboardAddedIterator];
-[AccessoryUSBBillboardDeviceListener billboardRemovedIterator];
-[AccessoryUSBBillboardDeviceListener initWithVID:PID:];
-[AccessoryUSBBillboardDeviceListener setAccessoryUSBBillboardDeviceListenerQueue:];
-[AccessoryUSBBillboardDeviceListener setAccessoryUSBBillboardDeviceRegistryIDs:];
-[AccessoryUSBBillboardDeviceListener setAccessoryUSBBillboardDeviceVIDPID:];
-[AccessoryUSBBillboardDeviceListener setAppleUSBHostBillboardDeviceNotify:];
-[AccessoryUSBBillboardDeviceListener setBillboardAddedIterator:];
-[AccessoryUSBBillboardDeviceListener setBillboardRemovedIterator:];
-[AccessoryUSBBillboardDeviceListener startDetectUSBBillboardDevice];
-[AccessoryUSBBillboardDeviceListener stopDetectUSBBillboardDevice];
```

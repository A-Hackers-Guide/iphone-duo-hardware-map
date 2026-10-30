# `AccessoryUSBBillboardDeviceManager`

- Image: [`/System/Library/CoreAccessories/PlugIns/Transports/USBHost.transport/USBHost`](../userland/System__Library__CoreAccessories__PlugIns__Transports__USBHost.transport__USBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 1 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSMutableDictionary" _usbBillboardDeviceListeners;
@"NSMutableDictionary" _detectedBillboardDevices;
@"NSObject<OS_dispatch_queue>" _accessoryUSBBillboardDeviceListenerQueue;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",R,N,V_accessoryUSBBillboardDeviceListenerQueue) accessoryUSBBillboardDeviceListenerQueue;
```

## Class methods

```
+[AccessoryUSBBillboardDeviceManager sharedManager];
+[AccessoryUSBBillboardDeviceManager vidpidRequiresNotSupportedPrompt:];
```

## Instance methods

```
-[AccessoryUSBBillboardDeviceManager init];
-[AccessoryUSBBillboardDeviceManager dealloc];
-[AccessoryUSBBillboardDeviceManager stopDetectUSBBillboardDeviceAll];
-[AccessoryUSBBillboardDeviceManager AppleUSBHostBillboardDeviceServiceArrived:vidpid:];
-[AccessoryUSBBillboardDeviceManager AppleUSBHostBillboardDeviceServiceTerminated:vidpid:];
-[AccessoryUSBBillboardDeviceManager accessoryUSBBillboardDeviceListenerQueue];
-[AccessoryUSBBillboardDeviceManager copyDetectedBillboardDevices];
-[AccessoryUSBBillboardDeviceManager isStartedDetectUSBBillboardDeviceWithVID:PID:];
-[AccessoryUSBBillboardDeviceManager startDetectUSBBillboardDeviceWithVID:PID:];
-[AccessoryUSBBillboardDeviceManager stopDetectUSBBillboardDeviceWithVID:PID:];
```

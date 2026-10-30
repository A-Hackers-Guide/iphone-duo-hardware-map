# `CBDeviceReporting` (protocol)

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 4 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@?,C,N) deviceFoundHandler;
@property (T@?,C,N) deviceLostHandler;
@property (T@?,C,N) deviceRemoteHostStateHandler;
@property (T@"NSArray",R,C) discoveredDevices;
```

## Instance methods

```
-[CBDeviceReporting discoveredDevices];
-[CBDeviceReporting deviceFoundHandler];
-[CBDeviceReporting deviceLostHandler];
-[CBDeviceReporting setDeviceFoundHandler:];
-[CBDeviceReporting setDeviceLostHandler:];
-[CBDeviceReporting setDeviceRemoteHostStateHandler:];
-[CBDeviceReporting deviceRemoteHostStateHandler];
```

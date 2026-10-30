# `IOUSBHostIOSource`

- Image: [`/System/Library/PrivateFrameworks/IOUSBHost.framework/IOUSBHost`](../userland/System__Library__PrivateFrameworks__IOUSBHost.framework__IOUSBHost.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 6 properties, 11 instance methods, 0 class methods

## Instance variables

```
I _debugLoggingMask;
@"IOUSBHostInterface" _hostInterface;
Q _deviceAddress;
Q _endpointAddress;
```

## Properties

```
@property (TI,V_debugLoggingMask) debugLoggingMask;
@property (T@"IOUSBHostInterface",&,V_hostInterface) hostInterface;
@property (TQ,V_deviceAddress) deviceAddress;
@property (TQ,V_endpointAddress) endpointAddress;
@property (TI,R) ioConnection;
@property (T^{IONotificationPort=},R) ioNotificationPortRef;
```

## Instance methods

```
-[IOUSBHostIOSource deviceAddress];
-[IOUSBHostIOSource setDeviceAddress:];
-[IOUSBHostIOSource hostInterface];
-[IOUSBHostIOSource endpointAddress];
-[IOUSBHostIOSource debugLoggingMask];
-[IOUSBHostIOSource initWithHostInterface:endpointAddress:deviceAddress:];
-[IOUSBHostIOSource ioConnection];
-[IOUSBHostIOSource ioNotificationPortRef];
-[IOUSBHostIOSource setDebugLoggingMask:];
-[IOUSBHostIOSource setEndpointAddress:];
-[IOUSBHostIOSource setHostInterface:];
```

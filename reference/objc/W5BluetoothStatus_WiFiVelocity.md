# `W5BluetoothStatus`

- Image: [`/System/Library/PrivateFrameworks/WiFiVelocity.framework/WiFiVelocity`](../userland/System__Library__PrivateFrameworks__WiFiVelocity.framework__WiFiVelocity.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 21 instance methods, 1 class methods

## Instance variables

```
B _powerOn;
B _isDiscoverable;
B _isConnectable;
B _isScanning;
@"NSString" _address;
@"NSArray" _devices;
```

## Properties

```
@property (TB,N,V_powerOn) powerOn;
@property (T@"NSString",C,N,V_address) address;
@property (TB,N,V_isDiscoverable) isDiscoverable;
@property (TB,N,V_isConnectable) isConnectable;
@property (TB,N,V_isScanning) isScanning;
@property (T@"NSArray",C,N,V_devices) devices;
```

## Class methods

```
+[W5BluetoothStatus supportsSecureCoding];
```

## Instance methods

```
-[W5BluetoothStatus isDiscoverable];
-[W5BluetoothStatus powerOn];
-[W5BluetoothStatus setIsScanning:];
-[W5BluetoothStatus address];
-[W5BluetoothStatus setDevices:];
-[W5BluetoothStatus isScanning];
-[W5BluetoothStatus setAddress:];
-[W5BluetoothStatus dealloc];
-[W5BluetoothStatus isConnectable];
-[W5BluetoothStatus devices];
-[W5BluetoothStatus encodeWithCoder:];
-[W5BluetoothStatus conformsToProtocol:];
-[W5BluetoothStatus hash];
-[W5BluetoothStatus description];
-[W5BluetoothStatus initWithCoder:];
-[W5BluetoothStatus copyWithZone:];
-[W5BluetoothStatus isEqual:];
-[W5BluetoothStatus setPowerOn:];
-[W5BluetoothStatus isEqualToBluetoothStatus:];
-[W5BluetoothStatus setIsConnectable:];
-[W5BluetoothStatus setIsDiscoverable:];
```

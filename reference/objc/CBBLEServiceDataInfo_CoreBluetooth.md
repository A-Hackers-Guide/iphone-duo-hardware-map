# `CBBLEServiceDataInfo`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
B _connectable;
S _serviceUUID16;
@"NSData" _serviceData;
```

## Properties

```
@property (T@"NSData",C,N,V_serviceData) serviceData;
@property (TS,N,V_serviceUUID16) serviceUUID16;
@property (TB,N,V_connectable) connectable;
```

## Instance methods

```
-[CBBLEServiceDataInfo connectable];
-[CBBLEServiceDataInfo setConnectable:];
-[CBBLEServiceDataInfo setServiceData:];
-[CBBLEServiceDataInfo serviceData];
-[CBBLEServiceDataInfo serviceUUID16];
-[CBBLEServiceDataInfo setServiceUUID16:];
```

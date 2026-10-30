# `CBAdvertisingAddressReporting` (protocol)

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 3 properties, 4 instance methods, 0 class methods

## Properties

```
@property (T@?,C,N) advertisingAddressChangedHandler;
@property (T@"NSData",R,C,N) advertisingAddressDataConnectable;
@property (T@"NSData",R,C,N) advertisingAddressDataNonConnectable;
```

## Instance methods

```
-[CBAdvertisingAddressReporting advertisingAddressDataNonConnectable];
-[CBAdvertisingAddressReporting advertisingAddressDataConnectable];
-[CBAdvertisingAddressReporting advertisingAddressChangedHandler];
-[CBAdvertisingAddressReporting setAdvertisingAddressChangedHandler:];
```

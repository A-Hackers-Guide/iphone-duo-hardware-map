# `_ACCBluetoothStatusComponent`

- Image: [`/System/Library/CoreAccessories/PlugIns/Platform/Platform-Bluetooth.platform/Platform-Bluetooth`](../userland/System__Library__CoreAccessories__PlugIns__Platform__Platform-Bluetooth.platform__Platform-Bluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 12 instance methods, 1 class methods

## Instance variables

```
B _needToUnplugBTDevice;
@"NSString" _accessoryUID;
@"NSString" _componentUID;
@"NSData" _macAddr;
@"NSString" _name;
^{BTAccessoryManagerImpl=} _btAccessoryManager;
^{BTDeviceImpl=} _btDevice;
```

## Properties

```
@property (T@"NSString",R,N,V_accessoryUID) accessoryUID;
@property (T@"NSString",R,N,V_componentUID) componentUID;
@property (T@"NSData",R,N,V_macAddr) macAddr;
@property (T@"NSString",R,N,V_name) name;
@property (T^{BTAccessoryManagerImpl=},N,V_btAccessoryManager) btAccessoryManager;
@property (T^{BTDeviceImpl=},N,V_btDevice) btDevice;
@property (TB,N,V_needToUnplugBTDevice) needToUnplugBTDevice;
```

## Class methods

```
+[_ACCBluetoothStatusComponent createComponentFromDict:];
```

## Instance methods

```
-[_ACCBluetoothStatusComponent description];
-[_ACCBluetoothStatusComponent name];
-[_ACCBluetoothStatusComponent btDevice];
-[_ACCBluetoothStatusComponent setBtDevice:];
-[_ACCBluetoothStatusComponent accessoryUID];
-[_ACCBluetoothStatusComponent macAddr];
-[_ACCBluetoothStatusComponent btAccessoryManager];
-[_ACCBluetoothStatusComponent componentUID];
-[_ACCBluetoothStatusComponent initWithUID:macAddr:name:forAccessoryUID:];
-[_ACCBluetoothStatusComponent needToUnplugBTDevice];
-[_ACCBluetoothStatusComponent setBtAccessoryManager:];
-[_ACCBluetoothStatusComponent setNeedToUnplugBTDevice:];
```

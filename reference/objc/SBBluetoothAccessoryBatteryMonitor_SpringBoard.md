# `SBBluetoothAccessoryBatteryMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BCBatteryDeviceObserving`
- 3 instance variables, 4 properties, 5 instance methods, 0 class methods

## Instance variables

```
@"NSMutableSet" _accessoryNamesInLowPower;
@"SBAlertItemsController" _alertItemsController;
@"BCBatteryDeviceController" _batteryDeviceController;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBluetoothAccessoryBatteryMonitor connectedDevicesDidChange:];
-[SBBluetoothAccessoryBatteryMonitor description];
-[SBBluetoothAccessoryBatteryMonitor descriptionBuilder];
-[SBBluetoothAccessoryBatteryMonitor _popLowPowerAlertForAccessoryIfNecessary:];
-[SBBluetoothAccessoryBatteryMonitor initWithAlertItemsController:];
```

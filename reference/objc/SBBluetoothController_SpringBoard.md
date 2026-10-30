# `SBBluetoothController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"CBDiscovery" _discovery;
i _latestBatteryLevel;
B _couldReportBatteryLevel;
@"NSMutableArray" _devices;
B _tetheringConnected;
```

## Instance methods

```
-[SBBluetoothController batteryLevel];
-[SBBluetoothController dealloc];
-[SBBluetoothController bluetoothDeviceEndedVoiceControl:];
-[SBBluetoothController bluetoothDeviceInitiatedVoiceControl:];
-[SBBluetoothController canReportBatteryLevel];
-[SBBluetoothController cbDeviceForAudioRoute:];
-[SBBluetoothController firstCBDeviceToReportBatteryLevel];
-[SBBluetoothController hasConnectedDevice];
-[SBBluetoothController iapDeviceChanged:];
-[SBBluetoothController indexOfDevice:];
-[SBBluetoothController noteDevicesChanged];
-[SBBluetoothController startWatchingForDevices];
-[SBBluetoothController stopWatchingForDevices];
-[SBBluetoothController tetheringConnected];
-[SBBluetoothController updateBattery];
-[SBBluetoothController updateTetheringConnected];
```

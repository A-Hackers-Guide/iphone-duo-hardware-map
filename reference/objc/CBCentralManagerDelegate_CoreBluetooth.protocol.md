# `CBCentralManagerDelegate` (protocol)

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance methods

```
-[CBCentralManagerDelegate centralManagerDidUpdateState:];
-[CBCentralManagerDelegate centralManager:didConnectPeripheral:];
-[CBCentralManagerDelegate centralManager:didDisconnectPeripheral:error:];
-[CBCentralManagerDelegate centralManager:didDiscoverPeripheral:advertisementData:RSSI:];
-[CBCentralManagerDelegate centralManager:connectionEventDidOccur:forPeripheral:];
-[CBCentralManagerDelegate centralManager:didFailToConnectPeripheral:error:];
-[CBCentralManagerDelegate centralManager:didDisconnectPeripheral:timestamp:isReconnecting:error:];
-[CBCentralManagerDelegate centralManager:didUpdateANCSAuthorizationForPeripheral:];
-[CBCentralManagerDelegate centralManager:willRestoreState:];
```

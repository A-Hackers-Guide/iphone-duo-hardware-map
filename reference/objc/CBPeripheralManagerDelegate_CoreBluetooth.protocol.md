# `CBPeripheralManagerDelegate` (protocol)

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 0 properties, 12 instance methods, 0 class methods

## Instance methods

```
-[CBPeripheralManagerDelegate peripheralManagerDidUpdateState:];
-[CBPeripheralManagerDelegate peripheralManager:didAddService:error:];
-[CBPeripheralManagerDelegate peripheralManager:didPublishL2CAPChannel:error:];
-[CBPeripheralManagerDelegate peripheralManager:didOpenL2CAPChannel:error:];
-[CBPeripheralManagerDelegate peripheralManager:didUnpublishL2CAPChannel:error:];
-[CBPeripheralManagerDelegate peripheralManager:didReceiveReadRequest:];
-[CBPeripheralManagerDelegate peripheralManager:didReceiveWriteRequests:];
-[CBPeripheralManagerDelegate peripheralManagerIsReadyToUpdateSubscribers:];
-[CBPeripheralManagerDelegate peripheralManager:central:didUnsubscribeFromCharacteristic:];
-[CBPeripheralManagerDelegate peripheralManagerDidStartAdvertising:error:];
-[CBPeripheralManagerDelegate peripheralManager:central:didSubscribeToCharacteristic:];
-[CBPeripheralManagerDelegate peripheralManager:willRestoreState:];
```

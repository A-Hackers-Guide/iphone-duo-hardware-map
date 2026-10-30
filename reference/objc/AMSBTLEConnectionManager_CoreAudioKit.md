# `AMSBTLEConnectionManager`

- Image: [`/System/Library/Frameworks/CoreAudioKit.framework/CoreAudioKit`](../userland/System__Library__Frameworks__CoreAudioKit.framework__CoreAudioKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBCentralManagerDelegate`, `CBPeripheralDelegate`
- 9 instance variables, 5 properties, 28 instance methods, 0 class methods

## Instance variables

```
@"CBCentralManager" centralManager;
@"NSMutableArray" peripheralList;
@"NSMutableArray" connectedBTPeripherals;
@"NSMutableArray" connectedAMSPeripherals;
@"NSTimer" refreshTimer;
@"NSTimer" connectionTimer;
@"<BTLEConnectionTable>" controller;
q centralState;
B isAdvertising;
```

## Properties

```
@property (T@"NSMutableArray",R,VperipheralList) peripheralList;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AMSBTLEConnectionManager startTimer];
-[AMSBTLEConnectionManager centralManager:didConnectPeripheral:];
-[AMSBTLEConnectionManager centralManager:didDisconnectPeripheral:error:];
-[AMSBTLEConnectionManager centralManager:didDiscoverPeripheral:advertisementData:RSSI:];
-[AMSBTLEConnectionManager centralManagerDidUpdateState:];
-[AMSBTLEConnectionManager bluetoothState];
-[AMSBTLEConnectionManager stopScan];
-[AMSBTLEConnectionManager initWithUIController:];
-[AMSBTLEConnectionManager dealloc];
-[AMSBTLEConnectionManager timerFired:];
-[AMSBTLEConnectionManager centralManager:didFailToConnectPeripheral:error:];
-[AMSBTLEConnectionManager peripheral:didDiscoverServices:];
-[AMSBTLEConnectionManager peripheral:didDiscoverCharacteristicsForService:error:];
-[AMSBTLEConnectionManager peripheral:didUpdateValueForCharacteristic:error:];
-[AMSBTLEConnectionManager centralManager:didRetrievePeripherals:];
-[AMSBTLEConnectionManager startScan];
-[AMSBTLEConnectionManager amsPeripheralForCBPeripheral:];
-[AMSBTLEConnectionManager checkAlreadyConnectedPeripherals];
-[AMSBTLEConnectionManager connectionTimerFired:];
-[AMSBTLEConnectionManager createPeripheralList];
-[AMSBTLEConnectionManager isLECapableHardware];
-[AMSBTLEConnectionManager killTimer];
-[AMSBTLEConnectionManager midiDeviceForUUID:];
-[AMSBTLEConnectionManager peripheralIsConnectedCentral:];
-[AMSBTLEConnectionManager peripheralList];
-[AMSBTLEConnectionManager removeAMSPeripheralForCBPeripheral:];
-[AMSBTLEConnectionManager setUIController:];
-[AMSBTLEConnectionManager updateAdvertisingState:];
```

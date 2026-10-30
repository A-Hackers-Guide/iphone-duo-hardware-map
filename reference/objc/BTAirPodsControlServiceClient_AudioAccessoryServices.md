# `BTAirPodsControlServiceClient`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBCentralManagerDelegate`, `CBPeripheralDelegate`
- 16 instance variables, 8 properties, 34 instance methods, 0 class methods

## Instance variables

```
@"CBCharacteristic" _airpodsCaseControlCharacteristicObj;
@"CBUUID" _airpodsCaseControlCharacteristicUUID;
@"CBService" _airpodsCaseControlServiceObj;
@"CBUUID" _airpodsCaseControlServiceUUID;
@"CBCentralManager" _centralManager;
B _connected;
B _invalidateCalled;
@"NSUUID" _peerUUID;
@"CBPeripheral" _peripheral;
@"NSMutableArray" _requestArray;
@"BTAirPodsControlRequest" _requestCurrent;
i _state;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@"CBDevice" _peerDevice;
@"NSString" _deviceSN;
@"NSString" _deviceUUID;
```

## Properties

```
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@"CBDevice",&,N,V_peerDevice) peerDevice;
@property (T@"NSString",&,N,V_deviceSN) deviceSN;
@property (T@"NSString",&,N,V_deviceUUID) deviceUUID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BTAirPodsControlServiceClient centralManager:didConnectPeripheral:];
-[BTAirPodsControlServiceClient _run];
-[BTAirPodsControlServiceClient dispatchQueue];
-[BTAirPodsControlServiceClient centralManagerDidUpdateState:];
-[BTAirPodsControlServiceClient deviceUUID];
-[BTAirPodsControlServiceClient init];
-[BTAirPodsControlServiceClient _invalidate];
-[BTAirPodsControlServiceClient setDispatchQueue:];
-[BTAirPodsControlServiceClient invalidate];
-[BTAirPodsControlServiceClient setPeerDevice:];
-[BTAirPodsControlServiceClient setDeviceUUID:];
-[BTAirPodsControlServiceClient _reportError:];
-[BTAirPodsControlServiceClient centralManager:didFailToConnectPeripheral:error:];
-[BTAirPodsControlServiceClient peerDevice];
-[BTAirPodsControlServiceClient peripheral:didDiscoverServices:];
-[BTAirPodsControlServiceClient centralManager:didUpdateFindMyPeripherals:];
-[BTAirPodsControlServiceClient peripheral:didDiscoverCharacteristicsForService:error:];
-[BTAirPodsControlServiceClient peripheral:didUpdateNotificationStateForCharacteristic:error:];
-[BTAirPodsControlServiceClient peripheral:didUpdateValueForCharacteristic:error:];
-[BTAirPodsControlServiceClient peripheral:didWriteValueForCharacteristic:error:];
-[BTAirPodsControlServiceClient _abortRequestsWithError:];
-[BTAirPodsControlServiceClient _completeRequest:error:];
-[BTAirPodsControlServiceClient _runConnectStart];
-[BTAirPodsControlServiceClient _runInit];
-[BTAirPodsControlServiceClient getSilentModeWithCompletionHandler:];
-[BTAirPodsControlServiceClient setDeviceSN:];
-[BTAirPodsControlServiceClient setSilentMode:completionHandler:];
-[BTAirPodsControlServiceClient isFindmyManaged];
-[BTAirPodsControlServiceClient _runDiscoverCharacteristicsStart];
-[BTAirPodsControlServiceClient _runDiscoverServicesStart];
-[BTAirPodsControlServiceClient _runProcessRequest:];
-[BTAirPodsControlServiceClient _runProcessRequests];
-[BTAirPodsControlServiceClient _setupTimeoutForRequest:];
-[BTAirPodsControlServiceClient deviceSN];
```

# `AADeviceManager`

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `AAServicesXPCClientInterface`
- 20 instance variables, 14 properties, 60 instance methods, 1 class methods

## Instance variables

```
B _activateCalled;
@? _activateCompletion;
@"NSMutableDictionary" _batteryDictionary;
@"NSMutableDictionary" _deviceDictionary;
B _invalidateCalled;
B _invalidateDone;
B _resetOngoing;
@"NSXPCConnection" _xpcCnx;
I _headGestureUpdateFlags;
I _clientID;
@? _deviceBatteryInfoUpdatedHandler;
@? _deviceBatteryInfoLostHandler;
@? _deviceFoundHandler;
@? _deviceLostHandler;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _headGestureUpdatedHandler;
@? _interruptionHandler;
@? _invalidationHandler;
@"NSXPCListenerEndpoint" _testListenerEndpoint;
@"AAServicesDaemon" _internalServicesDaemon;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (T@"NSXPCListenerEndpoint",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (T@"AAServicesDaemon",&,N,V_internalServicesDaemon) internalServicesDaemon;
@property (TB,R,N) direct;
@property (T@?,C,N,V_deviceBatteryInfoUpdatedHandler) deviceBatteryInfoUpdatedHandler;
@property (T@?,C,N,V_deviceBatteryInfoLostHandler) deviceBatteryInfoLostHandler;
@property (T@?,C,N,V_deviceFoundHandler) deviceFoundHandler;
@property (T@?,C,N,V_deviceLostHandler) deviceLostHandler;
@property (T@"NSArray",R,C) discoveredDevices;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_headGestureUpdatedHandler) headGestureUpdatedHandler;
@property (TI,N,V_headGestureUpdateFlags) headGestureUpdateFlags;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
```

## Class methods

```
+[AADeviceManager supportsSecureCoding];
```

## Instance methods

```
-[AADeviceManager setDeviceBatteryInfoLostHandler:];
-[AADeviceManager testListenerEndpoint];
-[AADeviceManager discoveredDevices];
-[AADeviceManager _invalidateDirect];
-[AADeviceManager fetchPairedAudioAccessoryDevices];
-[AADeviceManager clientID];
-[AADeviceManager fetchAudioAccessoryDeviceForBTAddress:];
-[AADeviceManager dispatchQueue];
-[AADeviceManager _reset];
-[AADeviceManager deviceFoundHandler];
-[AADeviceManager _ensureXPCStarted];
-[AADeviceManager fetchAudioAccessoryDeviceForIdentifier:];
-[AADeviceManager activateWithCompletion:];
-[AADeviceManager setTestListenerEndpoint:];
-[AADeviceManager setClientID:];
-[AADeviceManager aaServicesRequireReset];
-[AADeviceManager deviceHeadGestureDetected:];
-[AADeviceManager setDeviceBatteryInfoUpdatedHandler:];
-[AADeviceManager setInvalidationHandler:];
-[AADeviceManager init];
-[AADeviceManager deviceLostHandler];
-[AADeviceManager setDeviceFoundHandler:];
-[AADeviceManager _activateXPC:reactivate:];
-[AADeviceManager _activateDirect:];
-[AADeviceManager setDeviceLostHandler:];
-[AADeviceManager fetchAccessoryFeatureFlagConfigurationsWithError:];
-[AADeviceManager sendDeviceConfig:identifier:completion:];
-[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForAddress:];
-[AADeviceManager setInternalServicesDaemon:];
-[AADeviceManager _syncXPCFetchAADeviceBatteryInfoForIdentifier:];
-[AADeviceManager interruptionHandler];
-[AADeviceManager setDispatchQueue:];
-[AADeviceManager headGestureUpdateFlags];
-[AADeviceManager invalidate];
-[AADeviceManager _activate:];
-[AADeviceManager fetchAADeviceBatteryInfoForAddress:];
-[AADeviceManager _interrupted];
-[AADeviceManager direct];
-[AADeviceManager setHeadGestureUpdateFlags:];
-[AADeviceManager fetchAADeviceBatteryInfoForIdentifier:];
-[AADeviceManager encodeWithCoder:];
-[AADeviceManager deviceBatteryInfoUpdatedHandler];
-[AADeviceManager setInterruptionHandler:];
-[AADeviceManager _reportError:];
-[AADeviceManager deviceBatteryInfoLostHandler];
-[AADeviceManager headGestureUpdatedHandler];
-[AADeviceManager description];
-[AADeviceManager deviceManagerFoundDevice:];
-[AADeviceManager deviceManagerLostDevice:];
-[AADeviceManager initWithCoder:];
-[AADeviceManager deviceManagerFoundBatteryInfo:];
-[AADeviceManager invalidationHandler];
-[AADeviceManager internalServicesDaemon];
-[AADeviceManager _sendDeviceConfigDirect:identifier:completion:];
-[AADeviceManager deviceManagerLostBatteryInfo:];
-[AADeviceManager _invalidated];
-[AADeviceManager _sendDeviceConfigXPC:identifier:completion:];
-[AADeviceManager sendDeviceConfig:device:completion:];
-[AADeviceManager setHeadGestureUpdatedHandler:];
-[AADeviceManager isTemporaryPairingConnectionAllowed];
```

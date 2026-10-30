# `CBSpatialInteractionSession`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CUXPCCodable`, `CBActivatable`, `CBDeviceReporting`, `CBErrorReporting`, `CBInterruptable`, `CBLabelable`, `CBStateReporting`, `CBSystemOverridable`
- 48 instance variables, 38 properties, 108 instance methods, 2 class methods

## Instance variables

```
B _activateCalled;
@? _activateCompletion;
@"NSObject<OS_dispatch_source>" _advertiseRateTimer;
B _changesPending;
@"NSMutableDictionary" _deviceMap;
B _direct;
B _invalidateCalled;
B _invalidateDone;
@"NSMutableDictionary" _peerMap;
^{LogCategory=ii*I**i^{LogCategory}^{LogOutput}^{LogOutput}QQII*^{LogCategoryPrivate}} _ucat;
@"NSObject<OS_xpc_object>" _xpcCnx;
B _enableEPAForLEAdvertisement;
c _bleRSSIThresholdHint;
C _bleRSSIThresholdOrder;
I _systemOverrideFlags;
i _advertiseRate;
I _controlFlags;
i _scanRate;
i _scanRateOverride;
i _scanRateScreenOff;
I _uwbTokenFlags;
I _clientID;
I _internalFlags;
q _bluetoothState;
@? _bluetoothStateChangedHandler;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _deviceFoundHandler;
@? _deviceLostHandler;
@? _deviceRemoteHostStateHandler;
@? _errorHandler;
@? _interruptionHandler;
@? _invalidationHandler;
@"NSString" _label;
@? _systemOverrideHandler;
@? _advertisingAddressChangedHandler;
@"NSData" _advertisingAddressData;
@? _aopDataHandler;
@? _measurementHandler;
@? _tokenChangedHandler;
@"NSData" _tokenData;
@"NSData" _uwbConfigData;
@"NSData" _presenceConfigData;
@"NSData" _clientIrkData;
@"NSData" _clientIdentifierData;
@"CBSpatialInteractionFilter" _filter;
@"NSData" _identifierData;
@"NSData" _irkData;
@"NSObject<OS_xpc_object>" _testListenerEndpoint;
```

## Properties

```
@property (T@"NSData",C,N,V_advertisingAddressData) advertisingAddressData;
@property (TI,N,V_clientID) clientID;
@property (T@"NSData",C,N,V_identifierData) identifierData;
@property (TI,N,V_internalFlags) internalFlags;
@property (T@"NSData",C,N,V_irkData) irkData;
@property (Ti,N,V_scanRateOverride) scanRateOverride;
@property (T@"NSObject<OS_xpc_object>",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (T@"NSData",C,N,V_tokenData) tokenData;
@property (Ti,N,V_advertiseRate) advertiseRate;
@property (T@?,C,N,V_advertisingAddressChangedHandler) advertisingAddressChangedHandler;
@property (T@?,C,N,V_aopDataHandler) aopDataHandler;
@property (TI,N,V_controlFlags) controlFlags;
@property (TB,N,V_enableEPAForLEAdvertisement) enableEPAForLEAdvertisement;
@property (T@?,C,N,V_measurementHandler) measurementHandler;
@property (Ti,N,V_scanRate) scanRate;
@property (Ti,N,V_scanRateScreenOff) scanRateScreenOff;
@property (T@?,C,N,V_tokenChangedHandler) tokenChangedHandler;
@property (T@"NSData",C,V_uwbConfigData) uwbConfigData;
@property (T@"NSData",C,V_presenceConfigData) presenceConfigData;
@property (TI,N,V_uwbTokenFlags) uwbTokenFlags;
@property (Tc,N,V_bleRSSIThresholdHint) bleRSSIThresholdHint;
@property (TC,N,V_bleRSSIThresholdOrder) bleRSSIThresholdOrder;
@property (T@"NSData",C,V_clientIrkData) clientIrkData;
@property (T@"NSData",C,V_clientIdentifierData) clientIdentifierData;
@property (T@"CBSpatialInteractionFilter",C,N,V_filter) filter;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@?,C,N,V_deviceFoundHandler) deviceFoundHandler;
@property (T@?,C,N,V_deviceLostHandler) deviceLostHandler;
@property (T@?,C,N,V_deviceRemoteHostStateHandler) deviceRemoteHostStateHandler;
@property (T@"NSArray",R,C) discoveredDevices;
@property (T@?,C,N,V_errorHandler) errorHandler;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@"NSString",C,N,V_label) label;
@property (Tq,R,N,V_bluetoothState) bluetoothState;
@property (T@?,C,N,V_bluetoothStateChangedHandler) bluetoothStateChangedHandler;
@property (TI,R,N,V_systemOverrideFlags) systemOverrideFlags;
@property (T@?,C,N,V_systemOverrideHandler) systemOverrideHandler;
```

## Class methods

```
+[CBSpatialInteractionSession advertisingAddressInstanceToUse];
+[CBSpatialInteractionSession dictionaryWithTokenData:error:];
```

## Instance methods

```
-[CBSpatialInteractionSession encodeWithXPCObject:];
-[CBSpatialInteractionSession _activateDirectStart];
-[CBSpatialInteractionSession _lostAllDevices];
-[CBSpatialInteractionSession testListenerEndpoint];
-[CBSpatialInteractionSession discoveredDevices];
-[CBSpatialInteractionSession _invalidateDirect];
-[CBSpatialInteractionSession _xpcReceivedMessage:];
-[CBSpatialInteractionSession setInternalFlags:];
-[CBSpatialInteractionSession internalFlags];
-[CBSpatialInteractionSession _activateXPCStart:];
-[CBSpatialInteractionSession _xpcReceivedPowerStateChanged:];
-[CBSpatialInteractionSession clientID];
-[CBSpatialInteractionSession dispatchQueue];
-[CBSpatialInteractionSession bleRSSIThresholdHint];
-[CBSpatialInteractionSession _activate];
-[CBSpatialInteractionSession filter];
-[CBSpatialInteractionSession setAdvertiseRate:];
-[CBSpatialInteractionSession setControlFlags:];
-[CBSpatialInteractionSession setFilter:];
-[CBSpatialInteractionSession initWithXPCObject:error:];
-[CBSpatialInteractionSession deviceFoundHandler];
-[CBSpatialInteractionSession setBluetoothStateChangedHandler:];
-[CBSpatialInteractionSession _ensureXPCStarted];
-[CBSpatialInteractionSession activateWithCompletion:];
-[CBSpatialInteractionSession bluetoothStateChangedHandler];
-[CBSpatialInteractionSession descriptionWithLevel:];
-[CBSpatialInteractionSession bluetoothState];
-[CBSpatialInteractionSession setTestListenerEndpoint:];
-[CBSpatialInteractionSession setClientID:];
-[CBSpatialInteractionSession setBleRSSIThresholdHint:];
-[CBSpatialInteractionSession setSystemOverrideHandler:];
-[CBSpatialInteractionSession setInvalidationHandler:];
-[CBSpatialInteractionSession setIdentifierData:];
-[CBSpatialInteractionSession init];
-[CBSpatialInteractionSession label];
-[CBSpatialInteractionSession advertiseRate];
-[CBSpatialInteractionSession deviceLostHandler];
-[CBSpatialInteractionSession _xpcReceivedDeviceFound:];
-[CBSpatialInteractionSession setBleRSSIThresholdOrder:];
-[CBSpatialInteractionSession setLabel:];
-[CBSpatialInteractionSession setDeviceFoundHandler:];
-[CBSpatialInteractionSession setDeviceLostHandler:];
-[CBSpatialInteractionSession _xpcReceivedEvent:];
-[CBSpatialInteractionSession dealloc];
-[CBSpatialInteractionSession _update];
-[CBSpatialInteractionSession interruptionHandler];
-[CBSpatialInteractionSession _xpcReceivedAdvertisingAddressChanged:];
-[CBSpatialInteractionSession systemOverrideFlags];
-[CBSpatialInteractionSession setDispatchQueue:];
-[CBSpatialInteractionSession _updateIfNeededWithBlock:];
-[CBSpatialInteractionSession enableEPAForLEAdvertisement];
-[CBSpatialInteractionSession invalidate];
-[CBSpatialInteractionSession setDeviceRemoteHostStateHandler:];
-[CBSpatialInteractionSession identifierData];
-[CBSpatialInteractionSession scanRateOverride];
-[CBSpatialInteractionSession controlFlags];
-[CBSpatialInteractionSession _interrupted];
-[CBSpatialInteractionSession setScanRate:];
-[CBSpatialInteractionSession setInterruptionHandler:];
-[CBSpatialInteractionSession advertisingAddressChangedHandler];
-[CBSpatialInteractionSession _xpcReceivedDeviceLost:];
-[CBSpatialInteractionSession description];
-[CBSpatialInteractionSession setAdvertisingAddressChangedHandler:];
-[CBSpatialInteractionSession invalidationHandler];
-[CBSpatialInteractionSession _xpcReceivedSystemOverrideChanged:];
-[CBSpatialInteractionSession setErrorHandler:];
-[CBSpatialInteractionSession _invalidated];
-[CBSpatialInteractionSession bleRSSIThresholdOrder];
-[CBSpatialInteractionSession setEnableEPAForLEAdvertisement:];
-[CBSpatialInteractionSession deviceRemoteHostStateHandler];
-[CBSpatialInteractionSession scanRate];
-[CBSpatialInteractionSession setScanRateOverride:];
-[CBSpatialInteractionSession errorHandler];
-[CBSpatialInteractionSession systemOverrideHandler];
-[CBSpatialInteractionSession irkData];
-[CBSpatialInteractionSession measurementHandler];
-[CBSpatialInteractionSession setIrkData:];
-[CBSpatialInteractionSession setMeasurementHandler:];
-[CBSpatialInteractionSession setTokenData:];
-[CBSpatialInteractionSession tokenData];
-[CBSpatialInteractionSession _activateXPCCompleted:reactivate:];
-[CBSpatialInteractionSession _addPeerToken:userInfo:completion:];
-[CBSpatialInteractionSession _reAddTokens];
-[CBSpatialInteractionSession _xpcReceivedAOPData:];
-[CBSpatialInteractionSession addPeerToken:completion:];
-[CBSpatialInteractionSession addPeerToken:userInfo:completion:];
-[CBSpatialInteractionSession advertisingAddressData];
-[CBSpatialInteractionSession aopDataHandler];
-[CBSpatialInteractionSession clientIdentifierData];
-[CBSpatialInteractionSession clientIrkData];
-[CBSpatialInteractionSession matchesWithDevice:];
-[CBSpatialInteractionSession presenceConfigData];
-[CBSpatialInteractionSession removePeerToken:completion:];
-[CBSpatialInteractionSession scanRateScreenOff];
-[CBSpatialInteractionSession setAdvertiseRate:timeout:];
-[CBSpatialInteractionSession setAdvertisingAddressData:];
-[CBSpatialInteractionSession setAopDataHandler:];
-[CBSpatialInteractionSession setClientIdentifierData:];
-[CBSpatialInteractionSession setClientIrkData:];
-[CBSpatialInteractionSession setPresenceConfigData:];
-[CBSpatialInteractionSession setScanRateScreenOff:];
-[CBSpatialInteractionSession setTokenChangedHandler:];
-[CBSpatialInteractionSession setUwbConfigData:];
-[CBSpatialInteractionSession setUwbTokenFlags:];
-[CBSpatialInteractionSession tokenChangedHandler];
-[CBSpatialInteractionSession updateWithSession:];
-[CBSpatialInteractionSession uwbConfigData];
-[CBSpatialInteractionSession uwbTokenFlags];
```

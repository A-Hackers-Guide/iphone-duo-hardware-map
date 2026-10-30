# `CBServer`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBPairingAgentDelegate`, `CBPeripheralManagerDelegate`, `CBActivatable`, `CBErrorReporting`, `CBLabelable`, `CBStateReporting`
- 18 instance variables, 16 properties, 42 instance methods, 0 class methods

## Instance variables

```
B _activateCalled;
@? _activateCompletion;
@"NSMutableSet" _connections;
B _invalidateCalled;
@"CBPeripheralManager" _peripheralManager;
^{LogCategory=ii*I**i^{LogCategory}^{LogOutput}^{LogOutput}QQII*^{LogCategoryPrivate}} _ucat;
S _bleListenPSM;
S _bleListeningPSM;
I _serverFlags;
q _bluetoothState;
@? _bluetoothStateChangedHandler;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _errorHandler;
@? _invalidationHandler;
@"NSString" _label;
@? _acceptHandler;
@"NSData" _tempLTK;
@? _configChangedHandler;
```

## Properties

```
@property (T@?,C,N,V_acceptHandler) acceptHandler;
@property (TS,N,V_bleListenPSM) bleListenPSM;
@property (TS,R,N,V_bleListeningPSM) bleListeningPSM;
@property (TI,N,V_serverFlags) serverFlags;
@property (T@"NSData",&,N,V_tempLTK) tempLTK;
@property (T@?,C,N,V_configChangedHandler) configChangedHandler;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@?,C,N,V_errorHandler) errorHandler;
@property (T@"NSString",C,N,V_label) label;
@property (Tq,R,N,V_bluetoothState) bluetoothState;
@property (T@?,C,N,V_bluetoothStateChangedHandler) bluetoothStateChangedHandler;
```

## Instance methods

```
-[CBServer dispatchQueue];
-[CBServer setBluetoothStateChangedHandler:];
-[CBServer peripheralManagerDidUpdateState:];
-[CBServer activateWithCompletion:];
-[CBServer bluetoothStateChangedHandler];
-[CBServer pairingSetOOBEnabled:peer:completionHandler:];
-[CBServer bluetoothState];
-[CBServer setInvalidationHandler:];
-[CBServer init];
-[CBServer label];
-[CBServer _invalidate];
-[CBServer setLabel:];
-[CBServer dealloc];
-[CBServer configChangedHandler];
-[CBServer pairingAgent:peerDidRequestPairing:type:passkey:];
-[CBServer peripheralManager:didPublishL2CAPChannel:error:];
-[CBServer peripheralManager:didOpenL2CAPChannel:error:];
-[CBServer pairingAgent:peerDidFailToCompletePairing:error:];
-[CBServer setConfigChangedHandler:];
-[CBServer setBleListenPSM:];
-[CBServer pairingAgent:peerDidUnpair:];
-[CBServer setDispatchQueue:];
-[CBServer invalidate];
-[CBServer peripheralManager:didUnpublishL2CAPChannel:error:];
-[CBServer setAcceptHandler:];
-[CBServer acceptHandler];
-[CBServer setTempLTK:];
-[CBServer pairingGenerateOOBDataForPeer:completionHandler:];
-[CBServer _reportError:];
-[CBServer pairingAgent:peerDidCompletePairing:];
-[CBServer description];
-[CBServer bleListeningPSM];
-[CBServer _activateWithCompletion:];
-[CBServer invalidationHandler];
-[CBServer serverFlags];
-[CBServer setErrorHandler:];
-[CBServer tempLTK];
-[CBServer bleListenPSM];
-[CBServer _startIfNeeded];
-[CBServer setServerFlags:];
-[CBServer _handleConnectionInvalidated:];
-[CBServer errorHandler];
```

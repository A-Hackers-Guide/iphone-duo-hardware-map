# `CBConnection`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBCentralManagerDelegate`, `CBPeripheralDelegate`, `CUReadWriteRequestable`, `CBPairingAgentDelegate`, `CUXPCCodable`, `CBActivatable`, `CBErrorReporting`, `CBInterruptable`, `CBLabelable`, `CBPairable`, `CBConnectionRSSIMonitoring`, `CBReadWriteRequestable`, `CBStateReporting`, `CBRemotable`, `CBUseCaseable`
- 57 instance variables, 37 properties, 137 instance methods, 5 class methods

## Instance variables

```
B _activateCalled;
@? _activateCompletion;
@"NSUUID" _blePeerUUID;
@"CBCentralManager" _centralManager;
@"NSObject<OS_dispatch_source>" _connectTimeoutTimer;
B _guardConnected;
B _invalidateCalled;
B _invalidateDone;
B _ownsSocketFD;
@"NSData" _pairingOOBData;
q _pairingType;
@"CBPeripheral" _peripheral;
@"NSObject<OS_dispatch_source>" _readSource;
C _readSuspended;
@"CBReadRequest" _readRequestCurrent;
@"NSMutableArray" _readRequests;
i _socketFD;
i _state;
@"NSObject<OS_dispatch_source>" _writeSource;
C _writeSuspended;
@"CBWriteRequest" _writeRequestCurrent;
@"NSMutableArray" _writeRequests;
^{LogCategory=ii*I**i^{LogCategory}^{LogOutput}^{LogOutput}QQII*^{LogCategoryPrivate}} _ucat;
@"NSObject<OS_xpc_object>" _xpcCnx;
S _blePSM;
I _useCase;
I _connectionFlags;
I _serviceFlags;
I _clientID;
I _internalFlags;
q _bluetoothState;
@? _bluetoothStateChangedHandler;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _errorHandler;
@? _interruptionHandler;
@? _invalidationHandler;
@? _pairingCompletedHandler;
@? _pairingPromptHandler;
@? _connectionRSSIMonitoringHandler;
@"NSString" _label;
@"CBDevice" _remoteDevice;
@"NSArray" _useCaseClientIDs;
q _connectionLatency;
q _connectionScanDutyCycle;
d _connectTimeoutSeconds;
@"CBDevice" _peerDevice;
@"NSData" _tempLTK;
@"NSString" _clientBundleID;
q _clientUseCase;
d _connectedTime;
@"CBL2CAPChannel" _l2capChannel;
@"CBServer" _server;
@? _serverInvalidationHandler;
@"NSArray" _serviceUUIDs;
@? _xpcForwardMessageReceiveHandler;
@"NSObject<OS_xpc_object>" _xpcListenerEndpoint;
@? _xpcSendEventHandler;
```

## Properties

```
@property (TI,N,V_clientID) clientID;
@property (Td,N,V_connectedTime) connectedTime;
@property (TI,N,V_internalFlags) internalFlags;
@property (T@"CBL2CAPChannel",&,N,V_l2capChannel) l2capChannel;
@property (T@"CBServer",&,N,V_server) server;
@property (T@?,C,N,V_serverInvalidationHandler) serverInvalidationHandler;
@property (T@"NSArray",C,N,V_serviceUUIDs) serviceUUIDs;
@property (T@?,C,N,V_xpcForwardMessageReceiveHandler) xpcForwardMessageReceiveHandler;
@property (T@"NSObject<OS_xpc_object>",&,N,V_xpcListenerEndpoint) xpcListenerEndpoint;
@property (T@?,C,N,V_xpcSendEventHandler) xpcSendEventHandler;
@property (TS,N,V_blePSM) blePSM;
@property (TI,N,V_connectionFlags) connectionFlags;
@property (Tq,N,V_connectionLatency) connectionLatency;
@property (Tq,N,V_connectionScanDutyCycle) connectionScanDutyCycle;
@property (Td,N,V_connectTimeoutSeconds) connectTimeoutSeconds;
@property (T@"CBDevice",&,N,V_peerDevice) peerDevice;
@property (TI,N,V_serviceFlags) serviceFlags;
@property (T@"NSData",&,N,V_tempLTK) tempLTK;
@property (T@"NSString",C,N,V_clientBundleID) clientBundleID;
@property (Tq,N,V_clientUseCase) clientUseCase;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@?,C,N,V_errorHandler) errorHandler;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@"NSString",C,N,V_label) label;
@property (T@?,C,N,V_pairingCompletedHandler) pairingCompletedHandler;
@property (T@?,C,N,V_pairingPromptHandler) pairingPromptHandler;
@property (T@?,C,N,V_connectionRSSIMonitoringHandler) connectionRSSIMonitoringHandler;
@property (Tq,R,N,V_bluetoothState) bluetoothState;
@property (T@?,C,N,V_bluetoothStateChangedHandler) bluetoothStateChangedHandler;
@property (T@"CBDevice",&,N,V_remoteDevice) remoteDevice;
@property (TI,N,V_useCase) useCase;
@property (T@"NSArray",C,N,V_useCaseClientIDs) useCaseClientIDs;
```

## Class methods

```
+[CBConnection scalablePipeDeregisterRequestID:];
+[CBConnection scalablePipeHandleResponse:responseError:requestID:xpcEvent:];
+[CBConnection scalablePipeHandleXPCEvent:];
+[CBConnection scalablePipeRegisterRequestID:options:dispatchQueue:requestHandler:];
+[CBConnection selfConnectedPairAndReturnError:];
```

## Instance methods

```
-[CBConnection useCase];
-[CBConnection _activateXPCCompleted:];
-[CBConnection clientBundleID];
-[CBConnection encodeWithXPCObject:];
-[CBConnection centralManager:didConnectPeripheral:];
-[CBConnection _run];
-[CBConnection remoteDevice];
-[CBConnection setRemoteDevice:];
-[CBConnection xpcReceivedMessage:];
-[CBConnection _xpcReceivedMessage:];
-[CBConnection setInternalFlags:];
-[CBConnection internalFlags];
-[CBConnection readWithRequest:];
-[CBConnection _activateXPCStart:];
-[CBConnection clientID];
-[CBConnection dispatchQueue];
-[CBConnection centralManagerDidUpdateState:];
-[CBConnection _completeReadRequest:error:];
-[CBConnection _prepareWriteRequest:error:];
-[CBConnection initWithXPCObject:error:];
-[CBConnection setServer:];
-[CBConnection setBluetoothStateChangedHandler:];
-[CBConnection _ensureXPCStarted];
-[CBConnection activateWithCompletion:];
-[CBConnection bluetoothStateChangedHandler];
-[CBConnection server];
-[CBConnection bluetoothState];
-[CBConnection setClientID:];
-[CBConnection setInvalidationHandler:];
-[CBConnection updateWithXPCSubscriberInfo:];
-[CBConnection init];
-[CBConnection label];
-[CBConnection _abortReadsWithError:];
-[CBConnection _invalidate];
-[CBConnection setLabel:];
-[CBConnection _prepareReadRequest:];
-[CBConnection dealloc];
-[CBConnection pairingAgent:peerDidRequestPairing:type:passkey:];
-[CBConnection xpcListenerEndpoint];
-[CBConnection pairingAgent:peerDidFailToCompletePairing:error:];
-[CBConnection setServiceUUIDs:];
-[CBConnection interruptionHandler];
-[CBConnection setUseCaseClientIDs:];
-[CBConnection pairingAgent:peerDidUnpair:];
-[CBConnection setDispatchQueue:];
-[CBConnection useCaseClientIDs];
-[CBConnection writeWithRequest:];
-[CBConnection serviceUUIDs];
-[CBConnection invalidate];
-[CBConnection setClientBundleID:];
-[CBConnection setPeerDevice:];
-[CBConnection setTempLTK:];
-[CBConnection _interrupted];
-[CBConnection _completeWriteRequest:error:];
-[CBConnection setUseCase:];
-[CBConnection setInterruptionHandler:];
-[CBConnection _reportError:];
-[CBConnection pairingAgent:peerDidCompletePairing:];
-[CBConnection description];
-[CBConnection _processWrites];
-[CBConnection setXpcListenerEndpoint:];
-[CBConnection _activateWithCompletion:];
-[CBConnection invalidationHandler];
-[CBConnection setErrorHandler:];
-[CBConnection tempLTK];
-[CBConnection centralManager:didFailToConnectPeripheral:error:];
-[CBConnection _invalidated];
-[CBConnection errorHandler];
-[CBConnection peerDevice];
-[CBConnection _abortWritesWithError:];
-[CBConnection centralManager:didDisconnectPeripheral:timestamp:isReconnecting:error:];
-[CBConnection peripheral:didOpenL2CAPChannel:error:];
-[CBConnection _startConnectingAndReturnError:];
-[CBConnection _processReadStatus];
-[CBConnection _processReads:];
-[CBConnection _runConnectStart];
-[CBConnection _runSetupChannel];
-[CBConnection _setupIOAndReturnError:];
-[CBConnection activateDirectAndReturnError:];
-[CBConnection clientUseCase];
-[CBConnection connectionLatency];
-[CBConnection l2capChannel];
-[CBConnection pairingPromptHandler];
-[CBConnection serverInvalidationHandler];
-[CBConnection setClientUseCase:];
-[CBConnection setConnectionLatency:];
-[CBConnection setL2capChannel:];
-[CBConnection setPairingPromptHandler:];
-[CBConnection setServerInvalidationHandler:];
-[CBConnection writeEndOfDataWithCompletion:];
-[CBConnection setBlePSM:];
-[CBConnection _cleanupSocket];
-[CBConnection setConnectTimeoutSeconds:];
-[CBConnection setConnectionFlags:];
-[CBConnection disconnectWithCompletion:];
-[CBConnection setServiceFlags:];
-[CBConnection connectionRSSIMonitoringHandler];
-[CBConnection isBLEHIDAutoAcceptWithCBDevice:];
-[CBConnection xpcForwardMessageReceiveHandler];
-[CBConnection connectionFlags];
-[CBConnection _pairWithOOBData:];
-[CBConnection _pairingGenerateOOBDataWithCompletionHandler:];
-[CBConnection _pairingPerformActionBLE:withOptions:completionHandler:];
-[CBConnection _pairingPerformActionClassic:completionHandler:];
-[CBConnection _pairingPerformActionClassic:withOptions:completionHandler:];
-[CBConnection _pairingSetOOBEnabled:completionHandler:];
-[CBConnection _scalablePipeHandleXPCResponse:requestID:responseHandler:];
-[CBConnection _scalablePipeSendRequestID:request:options:responseHandler:];
-[CBConnection blePSM];
-[CBConnection configureRSSIMonitoring:completion:];
-[CBConnection connectTimeoutSeconds];
-[CBConnection connectedTime];
-[CBConnection connectionScanDutyCycle];
-[CBConnection initWithXPCEventRepresentation:error:];
-[CBConnection isBLEHIDWithCBDevice:];
-[CBConnection pairWithOOBData:];
-[CBConnection pairingCompletedHandler];
-[CBConnection pairingGenerateOOBDataWithCompletionHandler:];
-[CBConnection pairingPerformAction:completionHandler:];
-[CBConnection pairingPerformAction:withOptions:completionHandler:];
-[CBConnection pairingSetOOBEnabled:completionHandler:];
-[CBConnection readWithCBReadRequest:];
-[CBConnection scalablePipeSendRequestID:request:options:responseHandler:];
-[CBConnection serviceFlags];
-[CBConnection setConnectedTime:];
-[CBConnection setConnectionRSSIMonitoringHandler:];
-[CBConnection setConnectionScanDutyCycle:];
-[CBConnection setPairingCompletedHandler:];
-[CBConnection setXpcForwardMessageReceiveHandler:];
-[CBConnection setXpcSendEventHandler:];
-[CBConnection writeWithCBWriteRequest:];
-[CBConnection xpcForwardMessage:];
-[CBConnection xpcReceivedConnectionRSSIMonitoringData:];
-[CBConnection xpcReceivedForwardedEvent:];
-[CBConnection xpcReceivedPairingCompleted:];
-[CBConnection xpcReceivedPairingPrompt:];
-[CBConnection xpcSendEventHandler];
```

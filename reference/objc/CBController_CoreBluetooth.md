# `CBController`

- Image: [`/System/Library/Frameworks/CoreBluetooth.framework/CoreBluetooth`](../userland/System__Library__Frameworks__CoreBluetooth.framework__CoreBluetooth.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBXPCReceivable`, `CUXPCCodable`, `CBActivatable`, `CBErrorReporting`, `CBInterruptable`, `CBLabelable`, `CBStateReporting`, `CBRemotable`
- 29 instance variables, 20 properties, 88 instance methods, 20 class methods

## Instance variables

```
B _activateAssertionCalled;
B _activateCalled;
@? _activateCompletion;
B _changesPending;
B _direct;
B _invalidateCalled;
B _invalidateDone;
^{LogCategory=ii*I**i^{LogCategory}^{LogOutput}^{LogOutput}QQII*^{LogCategoryPrivate}} _ucat;
@"NSObject<OS_xpc_object>" _xpcCnx;
C _LPMCompletionTimeoutSeconds;
i _discoverableState;
i _inquiryState;
I _assertionFlags;
I _clientID;
I _internalFlags;
q _bluetoothState;
@? _bluetoothStateChangedHandler;
@"NSObject<OS_dispatch_queue>" _dispatchQueue;
@? _errorHandler;
@? _interruptionHandler;
@? _invalidationHandler;
@"NSString" _label;
@"CBDevice" _remoteDevice;
@? _discoverableStateChangedHandler;
@? _inquiryStateChangedHandler;
@? _relayMessageHandler;
@? _tipiChangedHandler;
@"NSString" _appID;
@"NSObject<OS_xpc_object>" _testListenerEndpoint;
```

## Properties

```
@property (T@"NSString",C,N,V_appID) appID;
@property (TI,N,V_assertionFlags) assertionFlags;
@property (TI,N,V_clientID) clientID;
@property (TI,N,V_internalFlags) internalFlags;
@property (T@"NSObject<OS_xpc_object>",&,N,V_testListenerEndpoint) testListenerEndpoint;
@property (Ti,R,N,V_discoverableState) discoverableState;
@property (T@?,C,N,V_discoverableStateChangedHandler) discoverableStateChangedHandler;
@property (Ti,R,N,V_inquiryState) inquiryState;
@property (T@?,C,N,V_inquiryStateChangedHandler) inquiryStateChangedHandler;
@property (T@?,C,N,V_relayMessageHandler) relayMessageHandler;
@property (T@?,C,N,V_tipiChangedHandler) tipiChangedHandler;
@property (TC,R,N,V_LPMCompletionTimeoutSeconds) LPMCompletionTimeoutSeconds;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V_dispatchQueue) dispatchQueue;
@property (T@?,C,N,V_invalidationHandler) invalidationHandler;
@property (T@?,C,N,V_errorHandler) errorHandler;
@property (T@?,C,N,V_interruptionHandler) interruptionHandler;
@property (T@"NSString",C,N,V_label) label;
@property (Tq,R,N,V_bluetoothState) bluetoothState;
@property (T@?,C,N,V_bluetoothStateChangedHandler) bluetoothStateChangedHandler;
@property (T@"CBDevice",&,N,V_remoteDevice) remoteDevice;
```

## Class methods

```
+[CBController featureFlags];
+[CBController controllerInfoAndReturnError:];
+[CBController nonBluetoothPointingDeviceCount];
+[CBController nonBluetoothKeyboardDeviceCount];
+[CBController bluetoothKeyboardDeviceCount];
+[CBController bluetoothModificationAllowed];
+[CBController bluetoothPointingDeviceCount];
+[CBController controllerInfoWithEndpoint:error:];
+[CBController getAllowedToPowerOffBluetoothState];
+[CBController numberOfKeyboardDevices];
+[CBController numberOfPointingDevices];
+[CBController performDeviceRequest:device:error:];
+[CBController performDeviceRequest:device:xpcEndpoint:error:];
+[CBController readPrefKeys:error:];
+[CBController safeToPowerOffBluetooth];
+[CBController setBluetoothModificationAllowed:error:];
+[CBController setOfflineAdvertisingParams:];
+[CBController systemHasOnlyBluetoothKeyboardDevices];
+[CBController systemHasOnlyBluetoothPointingDevices];
+[CBController writePrefKey:value:error:];
```

## Instance methods

```
-[CBController _activateXPCCompleted:];
-[CBController encodeWithXPCObject:];
-[CBController _activateDirectStart];
-[CBController inquiryState];
-[CBController remoteDevice];
-[CBController setRemoteDevice:];
-[CBController testListenerEndpoint];
-[CBController xpcReceivedMessage:];
-[CBController _invalidateDirect];
-[CBController setAppID:];
-[CBController _xpcReceivedMessage:];
-[CBController setInternalFlags:];
-[CBController appID];
-[CBController internalFlags];
-[CBController _activateXPCStart:];
-[CBController _xpcReceivedPowerStateChanged:];
-[CBController setRelayMessageHandler:];
-[CBController clientID];
-[CBController dispatchQueue];
-[CBController _activate];
-[CBController setLowPowerModeWithReason:completion:];
-[CBController initWithXPCObject:error:];
-[CBController setBluetoothStateChangedHandler:];
-[CBController _ensureXPCStarted];
-[CBController activateWithCompletion:];
-[CBController bluetoothStateChangedHandler];
-[CBController setPowerState:completion:];
-[CBController descriptionWithLevel:];
-[CBController setDiscoverableStateChangedHandler:];
-[CBController bluetoothState];
-[CBController tipiChangedHandler];
-[CBController setTestListenerEndpoint:];
-[CBController setClientID:];
-[CBController discoverableState];
-[CBController getPowerStateWithCompletion:];
-[CBController inquiryStateChangedHandler];
-[CBController setInvalidationHandler:];
-[CBController init];
-[CBController label];
-[CBController sendConversationDetectMessage:device:completionHandler:];
-[CBController setLabel:];
-[CBController modifyDevice:peerSourceDevice:peerSourceState:requestFlags:completionHandler:];
-[CBController dealloc];
-[CBController _xpcReceivedTipiChanged:];
-[CBController updateIdentities:completion:];
-[CBController _update];
-[CBController getControllerInfoWithCompletion:];
-[CBController diagnosticControl:completion:];
-[CBController assertionFlags];
-[CBController _xpcReceivedInquiryStateChanged:];
-[CBController interruptionHandler];
-[CBController setDispatchQueue:];
-[CBController _updateIfNeededWithBlock:];
-[CBController setTipiChangedHandler:];
-[CBController invalidate];
-[CBController _xpcReceivedRelayMessage:];
-[CBController performDeviceRequest:device:completion:];
-[CBController sendRelayMessageType:messageData:conduitDevice:destinationDevice:completionHandler:];
-[CBController modifyDevice:peerSourceDevice:peerSourceState:completionHandler:];
-[CBController _interrupted];
-[CBController getControllerSettingsWithCompletionHandler:];
-[CBController relayMessageHandler];
-[CBController _xpcReceivedDiscoverableStateChanged:];
-[CBController setAssertionFlags:];
-[CBController setInterruptionHandler:];
-[CBController LPMCompletionTimeoutSeconds];
-[CBController activateAssertionWithFlags:completion:];
-[CBController _activateAssertionWithFlagsDirect:completion:];
-[CBController diagnosticShow:completion:];
-[CBController modifyDevice:settings:completion:];
-[CBController description];
-[CBController diagnosticLog:completion:];
-[CBController resetCBExtensionID:completionHandler:];
-[CBController setLowPowerModeWithReason:error:];
-[CBController modifyDevice:connectionPriorityDevices:timeoutSeconds:completionHandler:];
-[CBController setLowPowerModeWithParams:params:completion:];
-[CBController invalidationHandler];
-[CBController modifyDevice:completion:];
-[CBController deleteDevice:completion:];
-[CBController _activateAssertionWithFlagsXPC:completion:];
-[CBController setErrorHandler:];
-[CBController discoverableStateChangedHandler];
-[CBController _invalidated];
-[CBController getDevicesWithFlags:completionHandler:];
-[CBController sendSmartRoutingInformation:device:completionHandler:];
-[CBController modifyControllerSettings:completionHandler:];
-[CBController errorHandler];
-[CBController setInquiryStateChangedHandler:];
```

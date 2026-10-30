# `BluetoothManager`

- Image: [`/System/Library/PrivateFrameworks/BluetoothManager.framework/BluetoothManager`](../userland/System__Library__PrivateFrameworks__BluetoothManager.framework__BluetoothManager.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 1 properties, 78 instance methods, 4 class methods

## Instance variables

```
^{BTLocalDeviceImpl=} _localDevice;
^{BTSessionImpl=} _session;
i _available;
i _state;
B _airplaneMode;
B _audioConnected;
B _scanningEnabled;
B _scanningInProgress;
I _scanningServiceMask;
^{BTDiscoveryAgentImpl=} _discoveryAgent;
^{BTPairingAgentImpl=} _pairingAgent;
^{BTAccessoryManagerImpl=} _accessoryManager;
@"NSMutableDictionary" _btAddrDict;
@"NSMutableDictionary" _btDeviceDict;
B _denylistEnabled;
```

## Properties

```
@property (TB,N,V_denylistEnabled) denylistEnabled;
```

## Class methods

```
+[BluetoothManager sharedInstance];
+[BluetoothManager lastInitError];
+[BluetoothManager setSharedInstanceQueue:];
+[BluetoothManager sharedInstanceQueue];
```

## Instance methods

```
-[BluetoothManager connected];
-[BluetoothManager powered];
-[BluetoothManager setDiscoverable:];
-[BluetoothManager connectable];
-[BluetoothManager isDiscoverable];
-[BluetoothManager setPowered:];
-[BluetoothManager _removeDevice:];
-[BluetoothManager connectDevice:];
-[BluetoothManager _postNotification:];
-[BluetoothManager deviceScanningEnabled];
-[BluetoothManager powerState];
-[BluetoothManager devicePairingEnabled];
-[BluetoothManager cancelPairing];
-[BluetoothManager postNotification:];
-[BluetoothManager isServiceSupported:];
-[BluetoothManager enabled];
-[BluetoothManager bluetoothState];
-[BluetoothManager connectedDeviceNamesThatMayBeDenylisted];
-[BluetoothManager resetDeviceScanning];
-[BluetoothManager setDeviceScanningEnabled:];
-[BluetoothManager _scanForServices:withMode:];
-[BluetoothManager connectedDevices];
-[BluetoothManager connectingDevices];
-[BluetoothManager bluetoothStateActionWithCompletion:];
-[BluetoothManager postNotificationName:object:];
-[BluetoothManager init];
-[BluetoothManager spatialAudioPlatformSupport];
-[BluetoothManager setPincode:forDevice:];
-[BluetoothManager _updateBluetoothState];
-[BluetoothManager bluetoothStateAction];
-[BluetoothManager isAnyoneAdvertising];
-[BluetoothManager disconnectDevicePhysicalLink:];
-[BluetoothManager dealloc];
-[BluetoothManager setConnectable:];
-[BluetoothManager acceptSSP:forDevice:];
-[BluetoothManager deviceFromIdentifier:];
-[BluetoothManager isAnyoneScanning];
-[BluetoothManager _notifyFirstDeviceUnlockCompleted];
-[BluetoothManager _connectabilityChanged];
-[BluetoothManager showPowerPrompt];
-[BluetoothManager startVoiceCommand:];
-[BluetoothManager maskLocalDeviceEvents:];
-[BluetoothManager _attach];
-[BluetoothManager _setScanState:];
-[BluetoothManager available];
-[BluetoothManager _powerChanged];
-[BluetoothManager endVoiceCommand:];
-[BluetoothManager setAudioConnected:];
-[BluetoothManager _restartScan];
-[BluetoothManager _pairedStatusChanged];
-[BluetoothManager deviceScanningInProgress];
-[BluetoothManager scanForServices:];
-[BluetoothManager addDeviceIfNeeded:];
-[BluetoothManager disconnectDevice:];
-[BluetoothManager _advertisingChanged];
-[BluetoothManager setEnabled:];
-[BluetoothManager pairedNonAppleHAEDevices];
-[BluetoothManager denylistEnabled];
-[BluetoothManager _connectedStatusChanged];
-[BluetoothManager audioConnected];
-[BluetoothManager _setup:];
-[BluetoothManager setDevicePairingEnabled:];
-[BluetoothManager unpairDevice:];
-[BluetoothManager _cleanup:];
-[BluetoothManager scanForConnectableDevices:];
-[BluetoothManager enableTestMode];
-[BluetoothManager pairedDevices];
-[BluetoothManager deviceFromAddressString:];
-[BluetoothManager postNotificationName:object:error:];
-[BluetoothManager _accessoryManager];
-[BluetoothManager _postNotificationWithArray:];
-[BluetoothManager _discoveryStateChanged];
-[BluetoothManager wasDeviceDiscovered:];
-[BluetoothManager localAddress];
-[BluetoothManager _updateAirplaneModeStatus];
-[BluetoothManager setDenylistEnabled:];
-[BluetoothManager _updateDenylistMode];
-[BluetoothManager connectDevice:withServices:];
```

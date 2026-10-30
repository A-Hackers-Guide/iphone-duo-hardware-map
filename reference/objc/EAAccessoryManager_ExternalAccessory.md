# `EAAccessoryManager`

- Image: [`/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory`](../userland/System__Library__Frameworks__ExternalAccessory.framework__ExternalAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `EABluetoothAccessoryPickerDelegate`, `ACCExternalAccessoryProviderProtocol`
- 10 instance variables, 5 properties, 93 instance methods, 6 class methods

## Instance variables

```
@"NSMutableArray" _connectedAccessories;
@"NSMutableArray" _sequesteredAccessories;
@"NSString" _selectedBluetoothAddress;
@? _pickerCompletion;
B _sequesterNewAccessories;
@"NSTimer" _pickerTimer;
@"NSRecursiveLock" _pickerLock;
@"NSObject<OS_dispatch_queue>" _connectionQueue;
@"NSString" _managerInstanceUUID;
@"EABluetoothAccessoryPicker" _picker;
```

## Properties

```
@property (T@"NSArray",R,N) connectedAccessories;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[EAAccessoryManager sharedAccessoryManager];
+[EAAccessoryManager accessoryDictionaryForLogging:];
+[EAAccessoryManager isLoggingEnabled];
+[EAAccessoryManager accessibilityStartListening];
+[EAAccessoryManager accessibilityStopListening];
+[EAAccessoryManager registerCapabilities:];
```

## Instance methods

```
-[EAAccessoryManager _applicationWillEnterForeground:];
-[EAAccessoryManager _applicationDidEnterBackground:];
-[EAAccessoryManager initiateConnectionToIPAccessory:];
-[EAAccessoryManager authCertSerialNumberForLegacyConnectionID:];
-[EAAccessoryManager sendGPRMCDataStatus:ValueV:ValueX:forUUID:];
-[EAAccessoryManager sendWiredCarPlayAvailable:usbIdentifier:wirelessCarPlayAvailable:bluetoothIdentifier:themeAssetsAvailable:forUUID:];
-[EAAccessoryManager createEASessionForProtocol:accessoryUUID:withReply:];
-[EAAccessoryManager _locationNmeaDataAvailableForAccessory:];
-[EAAccessoryManager accessibilitySystemPropertyRequest:];
-[EAAccessoryManager _cleanUpForTaskSuspendWithTaskIdentifier:];
-[EAAccessoryManager handleIncomingExternalAccessoryData:forEASessionIdentifier:withReply:];
-[EAAccessoryManager _nmeaFilteringSupportChanged:];
-[EAAccessoryManager registerForLocalNotifications];
-[EAAccessoryManager disconnectIPAccessory:];
-[EAAccessoryManager availableAccessories];
-[EAAccessoryManager accessibilitySystemPropertyChange:];
-[EAAccessoryManager initialEAAccessoriesAttachedAfterClientConnection:];
-[EAAccessoryManager stopDestinationSharingForUUID:];
-[EAAccessoryManager init];
-[EAAccessoryManager _connectedAccessories];
-[EAAccessoryManager stopIPAccessoryDiscovery];
-[EAAccessoryManager _notifyObserversThatAccessoryDisconnectedWithUserInfo:];
-[EAAccessoryManager destinationInformation:forAccessoryUUID:];
-[EAAccessoryManager connectedAccessories];
-[EAAccessoryManager _integrateSequesteredAccessories];
-[EAAccessoryManager dealloc];
-[EAAccessoryManager setAreLocationAccessoriesEnabled:];
-[EAAccessoryManager accessibilityAction:];
-[EAAccessoryManager _initFromSingletonCreationMethod];
-[EAAccessoryManager startIPAccessoryDiscovery];
-[EAAccessoryManager appDeclaresProtocol:];
-[EAAccessoryManager _pointOfInterestStatusReceived:];
-[EAAccessoryManager endSession:forConnectionID:];
-[EAAccessoryManager EAAccessoryLeft:];
-[EAAccessoryManager startDestinationSharingForUUID:options:];
-[EAAccessoryManager pointOfInterestSelection:];
-[EAAccessoryManager showBluetoothAccessoryPickerWithNameFilter:completion:];
-[EAAccessoryManager vehicleStatusUpdate:forAccessoryUUID:];
-[EAAccessoryManager currentVehicleInformation:];
-[EAAccessoryManager _ephemerisURLAvailable:];
-[EAAccessoryManager stopLocationForConnectedAccessories];
-[EAAccessoryManager wakeAccessoryWithToken:];
-[EAAccessoryManager _externalAccessoryConnectedNotificationHandler:];
-[EAAccessoryManager _ephemerisURLAvailableForAccessory:];
-[EAAccessoryManager sendWiredCarPlayAvailable:usbIdentifier:wirelessCarPlayAvailable:bluetoothIdentifier:forUUID:];
-[EAAccessoryManager sendOutgoingEAData:forSessionUUID:];
-[EAAccessoryManager nmeaSentenceArrived:forAccessoryUUID:withTimestamps:];
-[EAAccessoryManager _externalAccessoryDisconnected:];
-[EAAccessoryManager setShouldAllowCppRuntime:];
-[EAAccessoryManager accessibilityContextChange:];
-[EAAccessoryManager _findExtraAccessoriesContainedOnlyInEA:];
-[EAAccessoryManager unregisterForLocalNotifications];
-[EAAccessoryManager _locationPointDataAvailable:];
-[EAAccessoryManager openCompleteForSession:connectionID:];
-[EAAccessoryManager _gpsTimeRequested:];
-[EAAccessoryManager _findExtraAccessoriesContainedOnlyIniAP:];
-[EAAccessoryManager shouldAllowInternalProtocols];
-[EAAccessoryManager closeInputStreamForEASessionUUID:];
-[EAAccessoryManager _timeSyncInfoUpdated:];
-[EAAccessoryManager _removeAlliAPAccessoriesFromArray:notifyClients:];
-[EAAccessoryManager devicePicker:didSelectAddress:errorCode:];
-[EAAccessoryManager shouldAllowCppRuntime];
-[EAAccessoryManager openSessionFromAppToAccessory:];
-[EAAccessoryManager saveEASession:forEASessionUUID:];
-[EAAccessoryManager authCertForLegacyConnectionID:];
-[EAAccessoryManager EAAccessoryArrived:];
-[EAAccessoryManager sendDeviceIdentifierNotification:usbIdentifier:forUUID:];
-[EAAccessoryManager _checkForConnectedAccessories:backgroundTaskIdentifier:];
-[EAAccessoryManager _handleAccessoryNotificationTimeout:];
-[EAAccessoryManager areLocationAccessoriesEnabled];
-[EAAccessoryManager _externalAccessoryConnected:];
-[EAAccessoryManager _nmeaFilteringSupportChangedForAccessory:];
-[EAAccessoryManager destinationSharingStatus:forDestinationUUID:supportedParams:forUUID:];
-[EAAccessoryManager processIDIsUsingAccessory:];
-[EAAccessoryManager _OOBBTPairingCompletionStatusReceived:];
-[EAAccessoryManager accessoryClosedEASession:];
-[EAAccessoryManager sendNMEAFilterList:forUUID:];
-[EAAccessoryManager startLocationForConnectedAccessories];
-[EAAccessoryManager openSessionFromAccessoryToApp:];
-[EAAccessoryManager _locationPointDataAvailableForAccessory:];
-[EAAccessoryManager resumeEASessionData:];
-[EAAccessoryManager updateAccessoryInfo:];
-[EAAccessoryManager setShouldAllowInternalProtocols:];
-[EAAccessoryManager accessibilityItemPropertyRequest:];
-[EAAccessoryManager _iapServerDied:];
-[EAAccessoryManager _cameraInfoUpdated:];
-[EAAccessoryManager _externalAccessoryReconnected:];
-[EAAccessoryManager _gpsTimeRequestedForAccessory:];
-[EAAccessoryManager _vehicleDataUpdated:];
-[EAAccessoryManager closeEASessionForEASessionUUID:];
-[EAAccessoryManager _externalAccessoryUpdated:];
-[EAAccessoryManager _locationNmeaDataAvailable:];
-[EAAccessoryManager requestIAPAccessoryWiFiCredentials:];
```

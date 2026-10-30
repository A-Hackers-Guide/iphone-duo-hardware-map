# `EAAccessory`

- Image: [`/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory`](../userland/System__Library__Frameworks__ExternalAccessory.framework__ExternalAccessory.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 11 properties, 114 instance methods, 0 class methods

## Instance variables

```
@"EAAccessoryInternal" _internal;
```

## Properties

```
@property (TB,R,N,GisConnected) connected;
@property (TQ,R,N) connectionID;
@property (T@"NSString",R,N) manufacturer;
@property (T@"NSString",R,N) name;
@property (T@"NSString",R,N) modelNumber;
@property (T@"NSString",R,N) serialNumber;
@property (T@"NSString",R,N) firmwareRevision;
@property (T@"NSString",R,N) hardwareRevision;
@property (T@"NSString",R,N) dockType;
@property (T@"NSArray",R,N) protocolStrings;
@property (T@"<EAAccessoryDelegate>",N) delegate;
```

## Instance methods

```
-[EAAccessory modelNumber];
-[EAAccessory regionCode];
-[EAAccessory isConnected];
-[EAAccessory _shortDescription];
-[EAAccessory macAddress];
-[EAAccessory init];
-[EAAccessory dealloc];
-[EAAccessory transportType];
-[EAAccessory manufacturer];
-[EAAccessory serialNumber];
-[EAAccessory firmwareRevision];
-[EAAccessory setDelegate:];
-[EAAccessory bonjourName];
-[EAAccessory ppid];
-[EAAccessory delegate];
-[EAAccessory supportsCarPlay];
-[EAAccessory description];
-[EAAccessory connectionID];
-[EAAccessory name];
-[EAAccessory _setConnected:];
-[EAAccessory classType];
-[EAAccessory certData];
-[EAAccessory supportsLocation];
-[EAAccessory protocolStrings];
-[EAAccessory accessoryCapabilities];
-[EAAccessory beginOOBBTPairingWithCompletionBlock:];
-[EAAccessory coreAccessoriesPrimaryUUID];
-[EAAccessory destinationSharingOptions];
-[EAAccessory getVehicleInfoData];
-[EAAccessory hardwareRevision];
-[EAAccessory requestIAPAccessoryWiFiCredentials];
-[EAAccessory sendDeviceIdentifierNotification:usbIdentifier:];
-[EAAccessory supportsCarPlayAppLinks];
-[EAAccessory supportsCarPlayConnectionRequest];
-[EAAccessory supportsOOBBTPairing];
-[EAAccessory supportsOOBBTPairing2];
-[EAAccessory supportsUSBCarPlay];
-[EAAccessory supportsWirelessCarPlay];
-[EAAccessory vehicleInfoInitialData];
-[EAAccessory _endSession:];
-[EAAccessory firmwareRevisionActive];
-[EAAccessory firmwareRevisionPending];
-[EAAccessory setDestinationSharingOptions:];
-[EAAccessory captureStillImage:forCameraIds:];
-[EAAccessory eqNames];
-[EAAccessory hasIPConnection];
-[EAAccessory stopCameraUpdates:forCameraIds:];
-[EAAccessory updateSystemProperty:withValue:];
-[EAAccessory _removeSession:];
-[EAAccessory addNMEASentence:withTimestamps:];
-[EAAccessory eqIndex];
-[EAAccessory getEphemerisExpirationInterval:];
-[EAAccessory protocolDetails];
-[EAAccessory _OOBBTPairingCompletedWithStatus:forAccessoryWithMACAddress:];
-[EAAccessory _addSession:];
-[EAAccessory _createWakeToken];
-[EAAccessory _initWithAccessory:];
-[EAAccessory _internalConnectionID];
-[EAAccessory _internalNotPresentInIAPAccessoriesArray];
-[EAAccessory _openCompleteForSession:];
-[EAAccessory _protocolIDForProtocolString:];
-[EAAccessory _setNotPresentInIAPAccessoriesArray:];
-[EAAccessory _updateAccessoryInfo:];
-[EAAccessory accessoryHasNMEASentencesAvailable];
-[EAAccessory allPublicProtocolStrings];
-[EAAccessory audioPorts];
-[EAAccessory cameraComponents];
-[EAAccessory certSerial];
-[EAAccessory containsSameProtocolsAsiAPAccessoryProtocols:];
-[EAAccessory createdByCoreAccessories];
-[EAAccessory dictionaryWithLowercaseKeys:];
-[EAAccessory dockType];
-[EAAccessory getEphemerisRecommendRefreshInterval:];
-[EAAccessory getEphemerisURL:];
-[EAAccessory getIAPTimeSyncInfo:completionHandler:];
-[EAAccessory getNMEASentence:];
-[EAAccessory getNMEATimestampAverageSamples];
-[EAAccessory isAvailableOverBonjour];
-[EAAccessory locationSentenceTypesMask];
-[EAAccessory logNMEATimestampDelays:timestamps:];
-[EAAccessory pointOfInterestHandoffEnabled];
-[EAAccessory preferredApp];
-[EAAccessory resetIAPTimeSyncKalmanFilter];
-[EAAccessory sendDestinationInformation:identifier:];
-[EAAccessory sendEphemeris:];
-[EAAccessory sendEphemerisPointDataGpsWeek:gpsTOW:latitude:longitude:accuracy:];
-[EAAccessory sendGPRMCDataStatusValueA:ValueV:ValueX:];
-[EAAccessory sendGpsWeek:gpsTOW:];
-[EAAccessory sendPointOfInterestInformation:identifier:];
-[EAAccessory sendWiredCarPlayAvailable:usbIdentifier:wirelessCarPlayAvailable:bluetoothIdentifier:];
-[EAAccessory setCameraComponents:];
-[EAAccessory setCameraProperties:forCameraId:withProperties:];
-[EAAccessory setEqIndex:];
-[EAAccessory setEqNames:];
-[EAAccessory setIAPTimeSyncParams:];
-[EAAccessory setLocationSentenceTypesMask:];
-[EAAccessory setNMEASentencesToFilter:];
-[EAAccessory setPointOfInterestHandoffEnabled:];
-[EAAccessory setVehicleInfoSupportedTypes:];
-[EAAccessory setVehicleInfovehicleInfoInitialData:];
-[EAAccessory shouldBeHiddenFromUI];
-[EAAccessory startCameraInfo:forCameraIds:];
-[EAAccessory startCameraUpdates:forCameraIds:withProperties:withCapabilities:];
-[EAAccessory startLivePreview:forCameraIds:];
-[EAAccessory stopCameraInfo:forCameraIds:];
-[EAAccessory stopLivePreview:forCameraIds:];
-[EAAccessory supportsAccessibility];
-[EAAccessory supportsCamera];
-[EAAccessory supportsDestinationSharing];
-[EAAccessory supportsPointOfInterest];
-[EAAccessory supportsPublicIap];
-[EAAccessory updateItemProperty:withValue:];
-[EAAccessory vehicleInfoSupportedTypes];
-[EAAccessory wakeToken];
```

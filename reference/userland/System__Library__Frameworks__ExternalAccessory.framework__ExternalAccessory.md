# `/System/Library/Frameworks/ExternalAccessory.framework/ExternalAccessory`

iOS 27.2 dyld shared cache image. Version `462.40.2.0.0`. **[DSC]**

## Linked libraries (15)

- `/System/Library/PrivateFrameworks/AppSupport.framework/AppSupport`
- `/System/Library/Frameworks/Security.framework/Security`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/PrivateFrameworks/IAP.framework/IAP`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libc++.1.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/PrivateFrameworks/SoftLinking.framework/SoftLinking`
- `/usr/lib/swift/libswiftCore.dylib`
- `/usr/lib/swift/libswiftCoreFoundation.dylib`
- `/usr/lib/swift/libswiftDispatch.dylib`
- `/usr/lib/swift/libswiftObjectiveC.dylib`
- `/usr/lib/swift/libswiftXPC.dylib`
- `/usr/lib/swift/libswift_Builtin_float.dylib`

## Objective-C: 11 classes, 4 protocols, 449 methods, 88 properties

### Class pages

Every class and protocol, with its methods: [`ACCExternalAccessoryProviderProtocol`](../objc/ACCExternalAccessoryProviderProtocol_ExternalAccessory.protocol.md), [`BTDevicePickerDelegate`](../objc/BTDevicePickerDelegate_ExternalAccessory.protocol.md), [`EAAccessory`](../objc/EAAccessory_ExternalAccessory.md), [`EAAccessoryInternal`](../objc/EAAccessoryInternal_ExternalAccessory.md), [`EAAccessoryManager`](../objc/EAAccessoryManager_ExternalAccessory.md), [`EABluetoothAccessoryPicker`](../objc/EABluetoothAccessoryPicker_ExternalAccessory.md), [`EABluetoothAccessoryPickerDelegate`](../objc/EABluetoothAccessoryPickerDelegate_ExternalAccessory.protocol.md), [`EAInputStream`](../objc/EAInputStream_ExternalAccessory.md), [`EAOutputStream`](../objc/EAOutputStream_ExternalAccessory.md), [`EAPostAlert`](../objc/EAPostAlert_ExternalAccessory.md), [`EASession`](../objc/EASession_ExternalAccessory.md), [`EAWiFiUnconfiguredAccessory`](../objc/EAWiFiUnconfiguredAccessory_ExternalAccessory.md), [`EAWiFiUnconfiguredAccessoryBrowser`](../objc/EAWiFiUnconfiguredAccessoryBrowser_ExternalAccessory.md), [`NSObject`](../objc/NSObject_ExternalAccessory.protocol.md), [`WACLogging`](../objc/WACLogging_ExternalAccessory.md)

### Classes

`EAAccessory`, `EAAccessoryInternal`, `EAAccessoryManager`, `EABluetoothAccessoryPicker`, `EAInputStream`, `EAOutputStream`, `EAPostAlert`, `EASession`, `EAWiFiUnconfiguredAccessory`, `EAWiFiUnconfiguredAccessoryBrowser`, `WACLogging`

### Protocols

`ACCExternalAccessoryProviderProtocol`, `BTDevicePickerDelegate`, `EABluetoothAccessoryPickerDelegate`, `NSObject`

### Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
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
@property (TB,V_connected) connected;
@property (TI,V_connectionID) connectionID;
@property (T@"NSString",C,V_manufacturer) manufacturer;
@property (T@"NSString",C,V_name) name;
@property (T@"NSString",C,V_modelNumber) modelNumber;
@property (T@"NSString",C,V_serialNumber) serialNumber;
@property (T@"NSString",C,V_firmwareRevisionActive) firmwareRevisionActive;
@property (T@"NSString",C,V_firmwareRevisionPending) firmwareRevisionPending;
@property (T@"NSString",C,V_hardwareRevision) hardwareRevision;
@property (T@"NSString",C,V_dockType) dockType;
@property (Tq,V_transportType) transportType;
@property (T@"NSString",C,V_macAddress) macAddress;
@property (T@"NSString",C,V_preferredApp) preferredApp;
@property (T@"NSData",C,V_certSerial) certSerial;
@property (T@"NSData",C,V_certData) certData;
@property (T@"NSString",C,V_ppid) ppid;
@property (T@"NSString",C,V_regionCode) regionCode;
@property (T@"NSDictionary",C,V_protocolDetails) protocolDetails;
@property (T@"NSString",C,V_coreAccessoryPrimaryUUID) coreAccessoryPrimaryUUID;
@property (Ti,V_classType) classType;
@property (T@"NSDictionary",&,V_audioPorts) audioPorts;
@property (TI,V_capabilities) capabilities;
@property (TB,V_notPresentInIAPAccessoriesArray) notPresentInIAPAccessoriesArray;
@property (T@"NSArray",R) sessionsList;
@property (T@"NSArray",&,V_eqNames) eqNames;
@property (TI,V_eqIndex) eqIndex;
@property (Ti,V_locationSentenceTypesMask) locationSentenceTypesMask;
@property (T@"NSDictionary",&,V_vehicleInfoSupportedTypes) vehicleInfoSupportedTypes;
@property (T@"NSDictionary",&,V_vehicleInfoInitialData) vehicleInfoInitialData;
@property (T@"NSArray",&,V_cameraComponents) cameraComponents;
@property (T@"NSMutableArray",&,V_enqueuedNMEASentences) enqueuedNMEASentences;
@property (T@"NSMutableArray",&,V_enqueuedNMEATimestamps) enqueuedNMEATimestamps;
@property (TQ,V_nmeaSentenceAddCounter) nmeaSentenceAddCounter;
@property (TQ,V_nmeaSentenceGetCounter) nmeaSentenceGetCounter;
@property (T@"NSDictionary",&,V_protocols) protocols;
@property (T@"NSNumber",&,V_highestXPCDelay) highestXPCDelay;
@property (T@"NSNumber",&,V_highestFrameworkDelay) highestFrameworkDelay;
@property (T@"NSNumber",&,V_averageXPCDelay) averageXPCDelay;
@property (T@"NSNumber",&,V_averageFrameworkDelay) averageFrameworkDelay;
@property (T@"<EAAccessoryDelegate>",V_delegate) delegate;
@property (T@"NSString",C,V_bonjourName) bonjourName;
@property (TB,V_hasIPConnection) hasIPConnection;
@property (TB,V_isAvailableOverBonjour) isAvailableOverBonjour;
@property (TB,V_pointOfInterestHandoffEnabled) pointOfInterestHandoffEnabled;
@property (TB,V_createdByCoreAccessories) createdByCoreAccessories;
@property (T@?,C,V_pairingCompletionBlock) pairingCompletionBlock;
@property (T@?,C,V_WiFiCredentialsCompletionBlock) WiFiCredentialsCompletionBlock;
@property (TQ,V_destinationSharingOptions) destinationSharingOptions;
@property (T@"NSArray",R,N) connectedAccessories;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<EABluetoothAccessoryPickerDelegate>",N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Ti,V_zeroBytesReadCount) zeroBytesReadCount;
@property (T@"EAAccessory",R,N,V_accessory) accessory;
@property (T@"NSString",R,N,V_protocolString) protocolString;
@property (T@"NSInputStream",R,N,V_inputStream) inputStream;
@property (T@"NSOutputStream",R,N,V_outputStream) outputStream;
@property (T@"NSString",R,C,N,V_name) name;
@property (T@"NSString",R,C,N,V_manufacturer) manufacturer;
@property (T@"NSString",R,C,N,V_model) model;
@property (T@"NSString",R,C,N,V_ssid) ssid;
@property (T@"NSString",R,C,N,V_macAddress) macAddress;
@property (TQ,R,N,V_properties) properties;
@property (T@"NSObject<OS_dispatch_queue>",&,V_delegateQueue) delegateQueue;
@property (T@"NSPredicate",&,V_accessorySearchPredicate) accessorySearchPredicate;
@property (T@"<EAWiFiUnconfiguredAccessoryBrowserDelegate>",W,N,V_delegate) delegate;
@property (T@"NSSet",R,C,V_unconfiguredAccessories) unconfiguredAccessories;
```

## Swift types (3)

`ExternalAccessory.AccessoryDidConnectMessage`, `ExternalAccessory.AccessoryDidDisconnectMessage`, `conformance`

## Strings (477)

```
EAAccessoryDestinationStatusIdentifierKey
kCFAccessoryPortPropertyAudioLatencyInSeconds
EAAccessoryDidReceiveLocationPointDataNotification
/System/Library/Frameworks/UIKit.framework/UIKit
[#ExternalAccessory] Added accessory connectionID %lu, UUID %@
UIApplicationWillEnterForegroundNotification
v32@?0B8B12Q16@\"NSString\"24
wacSupportsSpruce
EAAccessoryPortPropertyChangedNotification
kCFAccessoryPortA2DPOut
kCFAccessoryPortPropertyNumSupportedSampleRates
[#ExternalAccessory] %s:%s-%d accessory connectionID %@ found in iap's connected accessories, so accessory will be advertised\n
link
[#Location] setNMEASentencesToFilter: created by core accessories, set NMEA senteneces to filter
OKAY_STRING
EATimeSyncInfoOffsetEstimate
[#ExternalAccessory] %s: %@
EATimeSyncInfoMeasurementInterval
EAWiFiUnconfiguredAccessoryBrowserFinishedConfiguringAccessoryNotification
EAAccessoryKey
[#ExternalAccessory] %s:%d ending background task identifier=%lu _backgroundTask=%lu
EAElectricVehicleChargingInfoPowerTypeKey
heightKey
EACameraExposureMode
mobile
[#BTPicker] %s isRunningOnMac
[#ExternalAccessory] %s:%s-%d found accessory %@ in iAP with different EA Protocols than EA Accessory %@
[#ExternalAccessory] Call sendWiredCarPlayAvailable:usbIdentifier:wirelessCarPlayAvailable:bluetoothIdentifier:forUUID: for accessoryUUID %@
EAVehicleInfoPowerForConnectorTypeGBT_ACKey
[#ExternalAccessory] success opening read stream for connectionID=%u and sessionID=%u
EACameraMinimumISO
  firmwareRevisionActive: %@ \n
wacManufacturerName
[#ExternalAccessory] %@: _backgroundTask not 0, %lu
EACameraSupportedImageCaptureFormat
  manufacturer: %@ \n
WAC: Browser: _handleBrowserDidUpdateState: %d
[#ExternalAccessory] %s:%s-%d found accessory %@ in iAP not contained in EA (total found count is %lu)
[#ExternalAccessory] %s:%s-%d advertising accessory reconnection for userInfo %@\n
v12@?0B8
[#ExternalAccessory] ERROR - opening session failed
staticText
EA_BackgroundTask
Could not load source: %ld
### bundlePath: %@
wacModelName
com.apple.%d.%d.%d.listenQueue
EAAccessoryDidConnectNotification
[#ExternalAccessory] %@: created new backgroundTask %lu
[#ExternalAccessory] found an iAP accessory created by CoreAccessories, connectionID %lu
[#ExternalAccessory] address is nil = %@
EAAccessoryAccessibilityResponseKey
EAVehicleInfoRangeCNGKey
EAVehicleInfoHasLowDistanceRangeDieselKey
%02X
-[EASession dealloc]
EAVehicleInfoRangeGasolineKey
EACameraHeight
UIKit.framework
EACameraActiveImageCaptureFormatIndex
EAAccessoryDidDisconnectNotification
EABluetoothAccessoryPickerErrorDomain
EAVehicleInfoPowerForConnectorTypeCHAdeMOKey
EAWiFiUnconfiguredAccessoryConfigured
EACameraCodec
  protocols: %@ \n
IAPAppAccessoryCertDataKey
keyboardKey
[#ExternalAccessory] %s:%s returning accessory capabilities 0x%X
[#Location] (%d/%llu/%llu/%d) addNMEASentence: %@, enqueued count %lu
[#ExternalAccessory] Done attaching initialConnectedAccessories
[#Location] %s: Cannot find accessory for UUID %@, skip nmeaSentence %@, timestamps %@
[#ExternalAccessory] __EAAuthSerialStringGetterCB: %u
EACameraFocusAreaOfInterest
  connectionID:%lu \n
MobileCoreServices
[#ExternalAccessory] ERROR - %s:%s - %d failed to write %lu bytes (wrote %d) with error %d
#
EAWiFiUnconfiguredAccessoriesAddedOrRemovedSet
v8@?0
%@ {\n  accessory:%@\n  protocolString:%@\n  inputStream:%@\n  outputStream: %@\n}
EAAccessoryCameraInfoNotification
EAAccessoryAccessibilitySystemPropertyKey
Unable to find class %s
kCFAccessoryPortPropertySupportedSampleRatesInHz
[#ExternalAccessory] %s isRunningOnMac
EAVehicleInfoIsVehicleParkedKey
[#ExternalAccessory] On: %d Unregistering. RegisteredForLocalNotifications Count: %d
[#ExternalAccessory] Removing EASession %@ from list of sessionUUIDs
ACCExternalAccessoryProtocolIndex
EACameraHorizontalResolution
WAC: Browser: _handleRemovedAccessoriesNotification: %@
pointYKey
EAVehicleInfoPowerForConnectorTypeGBT_DCKey
EAVehicleInfoDisplayedBatteryPercentageKey
[#BTPicker] ERROR: wakeSelectedBluetoothAccessories method is disabled!
EAVehicleInfoPowerForConnectorTypeCCS2Key
kCFAccessoryPortPropertyCurrentSampleRate
[#ExternalAccessory] released _sockListenSource
  dockType: %@ \n
[#ExternalAccessory] %s:%s supports Public iAP but has no public EA protocols
[#ExternalAccessory] Found iap accessory for connection id %lu
[#Location] (%d/%llu/%llu/%d) getNMEASentence: %@, enqueued count %lu
System
Library
com.apple.private.externalaccessory.showallaccessories
EAVehicleInfoInsideTemperatureKey
Class getBTDevicePickerClass(void)_block_invoke
[#ExternalAccessory] ERROR - %s:%s - %d can't schedule callback, runloop is NULL
CoreAccessories.framework
kCFAccessoryPortPropertyVolumeControlIsSupported
}
EAAccessoryDestinationStatusNotification
[#ExternalAccessory] Call sendDeviceIdentifierNotification:usbIdentifier:forUUID: for accessoryUUID %@
com.apple.EA.accessoryListLock
button
EAVehicleInfoPowerForConnectorTypeNACS_AsCKey
EAVehicleInfoHasLowDistanceRangeGasolineKey
WAC: Browser: ERROR: Unable to find EAWiFiUnconfiguredAccessoryBrowserManager class
EAAccessoryIsReconnecting
[#ExternalAccessory] SecTaskCopyValueForEntitlement failed for \"%@\", error:%@
[#ExternalAccessory] New Address: %@ Saved address: %@ Bool: %u\n
[#Location] areLocationAccessoriesEnabled %d -> %d
[#ExternalAccessory] ERROR - %s:%s - %d failed to write because stream does not have space available
-[EAOutputStream _scheduleCallback]
EAVehicleInfoPowerForConnectorTypeCCS1Key
EAVehicleInfoRangeDieselKey
com.apple.ExternalAccessory
EAIPAccessoryNotAvailableNotification
-[EAAccessoryManager _findExtraAccessoriesContainedOnlyInEA:]
EAAccessoryReConnectOnEnterForeground
LogEAEvents
EAAccessoryDidReceiveEphemerisURLNotification
  connected:%@ \n
  firmwareRevisionPending: %@ \n
-[EAAccessory accessoryCapabilities]
[#ExternalAccessory] [#Location] Starting location for accessory UUID %@
[#Location] send %@, userInfo %@
ACCExternalAccessoryProtocolFirmwareVersionActive
EACameraFocusMode
WAC: Browser: _handlePurgeAccessoriesSetNotification. Purging: %@
SpringBoardServices.framework
widthKey
sound
EAAccessoryAccessibilityContextKey
[#ExternalAccessory] %@: ending expired background task for _backgroundTask %lu, resetting back to 0
[#ExternalAccessory] %s:%s-%d reRegisterForNotifications
[#ExternalAccessory] Client read %d bytes from file descriptor, for [_session _sessionID] %d 0x%X, zeroBytesReadCount %d, cancel sockListenSource
ACCDestinationSharingOptionsKey
[#VehicleInfoStatus] For %@ - %@ (transport %@), No vehicle information found when converting iAP accessory to EA accessory
[#ExternalAccessory] tx data: failed because of broken pipe, assume success\n
BTDevicePicker
EAWiFiUnconfiguredAccessoriesRemovedNotification
[#ExternalAccessory] %s:%s found whitelisted protocol %@
[#ExternalAccessory] CoreAccessories accessoryInfo for departure = %@
[#ExternalAccessory] %s _backgroundTask(%lu) != identifier(%lu)
EACameraInfoCameraCapabilities
kCFAccessoryPortDisplayPort
-[EAAccessoryManager _checkForConnectedAccessories:backgroundTaskIdentifier:]_block_invoke
selected
EAElectricVehicleChargingComponentsKey
EAVehicleInfoMaxRangeCNGKey
EAAccessoryManagerInitException
[#VehicleInfoStatus] No accessory found for vehicle status update, ignoring, %@
[#ExternalAccessory] %s:%s-%d __capabilities = 0x%X, EAAccessoryCapabilitiesKeepSessionsOpenWhenSuspended = 0x%X, EAAccessoryCapabilitiesKeepSessionsOpenInBackground = 0x%X
[#ExternalAccessory] _externalAccessoryConnected: userInfo %@
[#ExternalAccessory] %s - %s - %d Closing _sock = %d for session %d
EACameraBitDepth
EATimeSyncInfoUncertaintyThreshold
kCFAccessoryPortPropertyIsActive
EAVehicleInfoMapsDisplayNameKey
[#ExternalAccessory] Returning connectedAccessories count %lu
com.apple.EA.connectionQueue
-[EAOutputStream write:maxLength:]
[#BTPicker] No BTDevicePicker class exists!
EAWiFiUnconfiguredAccessoryBrowserConfigurationStatus
PrivateFrameworks
[#ExternalAccessory] CoreAccessories accessoryInfo for arrival = %@
kCFAccessoryPortLineOut
[#ExternalAccessory] %s:%d ERROR: CFUserNotificationCreate returned NULL! notificationDict=%@
-[EAAccessoryManager vehicleStatusUpdate:forAccessoryUUID:]
BLUETOOTH_PICKER_UNAVAILABLE_MSG
[#ExternalAccessory] ERROR - could not find protocolID for protocolString %@
EAVehicleInfoMaxRangeGasolineKey
EACameraSupportedLivePreviewFormat
%@ { \n
[#ExternalAccessory] On: %d RegisteredForLocalNotifications Count: %d
[#ExternalAccessory] %@: background task expired, _backgroundTask %lu
[#ExternalAccessory] __EAAuthDataGetterCB: %u
[#ExternalAccessory] %s ending backgroundTask %lu
[#ExternalAccessory] __EAAuthSerialStringGetterCB: falied to get accessory for %u, connectedAccessories=%@
EAVehicleInfoMaxBatteryChargeKey
  hardwareRevision: %@ \n
wacFriendlyName
DebugWACLogging
[#ExternalAccessory] no ACCExternalAccessoryProviderClass
[#ExternalAccessory] Added iapConnectedAccessory connectionID %lu
-[EAAccessory supportsPublicIap]
com.apple.iPodOut
-init not supported. use -initWithAccessory:forProtocol.
mediaSession
EAAccessoryPointOfInterestIntentKey
[#ExternalAccessory] Call requestIAPAccessoryWiFiCredentials for accessory UUID %@
EACameraName
CoreAccessories
-[EAAccessoryManager _applicationWillEnterForeground:]
[#Location] Checking for connected accessories, stopping location for accessory UUID %@
[#ExternalAccessory] EAAccessory not created by CoreAccessories, no value for key kACCExternalAccessoryPrimaryUUID
EAAccessoryTimeSyncInfoUpdate
  regioncode: %@ \n
wacMACAddress
EAElectricVehicleChargingInfoMinimumVoltageKey
kCFAccessoryPortHFP
[#ExternalAccessory] %s disconnecting accessory %@
EAAccessoryDidRequestGPSTimeNotification
  certData: %lu bytes \n
-[EAAccessoryManager _removeAlliAPAccessoriesFromArray:notifyClients:]
EAVehicleInfoOutsideTemperatureKey
UISupportedExternalAccessoryProtocols
[#ExternalAccessory] Found ea accessory %@ for connection id %lu
EAVehicleInfoChargingParameterKey
  serialNumber: %@ \n
[#ExternalAccessory] Found ea accessory %@ for accessoryUUID %@
[#ExternalAccessory] accessoryd sessionResult = %d, useSocketInterace = %d, sessionID = 0x%llX
scaleFactorKey
EAVehicleInfoMakeKey
/Library/Caches/com.apple.xbs/64A9CE47-66B8-44B2-AEF8-07E8E0F98FC8/TemporaryDirectory.9fSknA/Sources/ExternalAccessory/EAAccessory.mm
YES
EAAccessoryNMEASentenceFilteringSupportChangedNotification
EAVehicleInfoMaxRangeElectricKey
WAC: Browser: _handleBrowserFinishedConfiguring: %@
[#ExternalAccessory] %s: found an iAP accessory to remove, index %d, connectionID %lu, shouldNotifyClients = %d
[#ExternalAccessory] %s:%s-%d releasing _inputFromAccBuffer and _inputFromAccQueue
EAVehicleInfoIsColdTemperatureIndicatorOnKey
WAC: Browser: stopSearchingForAccessories
EAConnectionIDKey
com.apple.update
UIKitApplication
[#ExternalAccessory] initialConnectedAccessories count %lu
EAVehicleInfoActiveConnectorKey
EACameraInfoCameraProperties
EAWiFiUnconfiguredAccessory: Name=%@ Manufacturer=%@ Model=%@ MAC=%@ SSID=%@ Properties=%d
[#ExternalAccessory] %s: shouldNotifyClients %d, accessories (count %lu)
EABluetoothAccessoryPicker.m
EAAccessoryDestinationStatusDidSucceedKey
[#ExternalAccessory] %s backgroundTask(%lu) != identifier(%lu)
[#ExternalAccessory] %s - %s - %d _sock for session %d ALREADY CLOSED
[#ExternalAccessory] %s initializing (%p) with uuid %@
EASessionInitException
EAAccessorySpeakerMenuEQIndexKey
EAElectricVehicleChargingInfoConnectorTypeKey
  certSerial: %lu bytes \n
wacSSID
  modelNumber: %@ \n
EASessionOpenCompletedNotification
[#ExternalAccessory] socketPath from app = %s
-init is not supported. Use +sharedAccessoryManager.
[#ExternalAccessory] no eaSessionUUID to close stream
com.apple.EA.pickerLock
AppleLanguages
[#VehicleInfoStatus] Found accessory for vehicle status update, %@
[#Location] Sending NMEA filter list to accessory UUID %@
%lu bytes
kACCExternalAccessoryTransportType
[#ExternalAccessory] Getting incoming data, but stream status %lu isn't valid...not saving
+[EAPostAlert EANotificationPostAccessoryNotification:forMsg:forDefaultButton:withAlternateButton:forNotification:withCallback:andTimeout:]
EAIPAccessoryConnectionCompleteNotification
[#ExternalAccessory] [#Location] skip startLocationInformationForAccessoryUUID, enable %d, accessory UUID %@ (support %d, coreAccessories %d)
[#ExternalAccessory] %s backgroundTask = %lu, resetting back to 0
EACameraHorizontalOrigin
SpringBoardServices
[#Location] Current delays: XPC: %f Framework: %f, Highest: XPC: %@ Framework: %@, Average: XPC: %@ Framework: %@, Sentence: %@
EAInputStream.m
kCFAccessoryPortUSBOut
[#ExternalAccessory] %s inBackground %d, identifier %lu
[#ExternalAccessory] %s-%d Received notification of accessory connection
[#ExternalAccessory] %s:%s-%d accessory connectionID %u disconnected %@\n
EACameraISO
[#ExternalAccessory] __EAAuthDataGetterCB: falied to get accessory for %u, connectedAccessories=%@
-init not supported. EAAccessoryManager is responsible for creating all objects.
XPC_SERVICE_NAME
[#ExternalAccessory] On: %d Accessory Disconnected. UUID %@ connectionID %lu createdByCoreAccessories %d. RegisteredForLocalNotifications Count: %d
EAAccessoryCleanUpForTaskSuspend
adjustable
EAAccessoryAccessibilityItemPropertyKey
BLUETOOTH_ACCESSORY_PICKER_TITLE
IAPAppAccessoryCertSerialNumberKey
-[EAAccessoryManager _externalAccessoryConnectedNotificationHandler:]
[#ExternalAccessory] connection ID %lu not found in ea accessories list
v32@?0@8@16^B24
### %@
-[EAAccessoryManager _applicationDidEnterBackground:]
[#Location] EA detach in progress, logging remaining NMEA Sentences
[#VehicleInfoStatus] No accessory to get currentVehicleInformation. accessory UUID %@
EAVehicleInfoRangeKey
EATimeSyncOffsetMeasurementInterval
[#ExternalAccessory] %s attaching accessory %@
[#ExternalAccessory] On: %d Accessory Connected. InternalNotPresentIniAPAccArray: %d
[#ExternalAccessory] ERROR - %s:%s - %d unable to close session for _accessory=%p and sessionID=%lu
EAVehicleInfoConsumptionParameterKey
EATimeSyncOffsetUncertaintyThreshold
[#ExternalAccessory] %s: shouldNotifyClients %d, accessories (count %lu) %@
-[EAAccessoryManager _externalAccessoryConnected:]_block_invoke
[#ExternalAccessory] Handling _iapServerDied, _connectedAccessories count = %lu, notification %@
[#ExternalAccessory] Checking for connected accessories, starting location for accessory UUID %@
[#VehicleInfoStatus] For %@ - %@ (transport %@), Found initialVehicleInfoDictionary %@
[#ExternalAccessory] Error - socket failed: %d - %s\n
  ppid: %@ \n
BLUETOOTH_PICKER_UNAVAILABLE_TITLE
should be able to make run loop source
EACameraVerticalResolution
EATimeSyncInfoOffsetUncertainty
-[EAAccessoryManager _cleanUpForTaskSuspendWithTaskIdentifier:]
[#ExternalAccessory] On: %d Posting EA DidConnect Notification for Accessory with UUID: %@ connectionID %lu createdByCoreAccessories %d
EAAccessoryAccessibilityActionKey
pointXKey
[#ExternalAccessory] %s:%s Found accessory %@  in EA not contained in iAP, needs to be detached, (total found count is %lu)
[#VehicleInfoStatus] Call currentVehicleInformation for accessory UUID %@
-[EAInputStream _scheduleCallback]
[#ExternalAccessory] ERROR - unable to make write socket nonblocking: %u
summaryText
EAWiFiUnconfiguredAccessoryBrowserState
UIApplicationDidEnterBackgroundNotification
EAWiFiUnconfiguredAccessoryBrowserDidUpdateState
kCFAccessoryPortPropertyIsConnected
[#ExternalAccessory] _connectedAccessories (%lu)
[#ExternalAccessory] ERROR - sock can not connect: %u
EAVehicleInfoPowerForConnectorTypeJ1772Key
EACameraActiveLivePreviewFormatIndex
EACameraExposureAreaOfInterest
EAAccessoryDestinationStatusParametersUsedKey
-[EAAccessoryManager nmeaSentenceArrived:forAccessoryUUID:withTimestamps:]
EAElectricVehicleChargingInfoMaximumCurrentKey
EAWiFiUnconfiguredAccessoriesAddedNotification
UIKit
EAIPAccessoryAvailableNotification
EAAccessoryReConnect
[#ExternalAccessory] %s:%s-%d skipping attach notification\n
[#ExternalAccessory] accessoryUUID %@ not found in ea accessories list
voiceOverVolumeKey
EAVehicleInfoMaxRangeDieselKey
[#ExternalAccessory] ERROR: No connectionIDObject in EAAccessoryLeft
[#ExternalAccessory] %s: connectionID %llu
%s/ea.%lu
wacSupportsAirPlay
kCFAccessoryPortPropertyIsVoiceSignalProcessingSupported
NO
[#ExternalAccessory] %s:%s-%d accessory connectionID %@ not found in iap's list of connected accessories\n
[#Location] EA detach sentence logging done!
Localization
EAAccessorySelectedKey
EAOutputStream.m
[#ExternalAccessory] On: %d Accessory Connected with UUID %@ connectionID %lu createdByCoreAccessories %d. RegisteredForLocalNotifications Count: %d
EAVehicleInfoPowerForConnectorTypeNACS_DCKey
VisualVoicemail
[#ExternalAccessory] ERROR - opening session failed as protocol %@ is not declared in Info.plist
EACameraVerticalOrigin
WAC: Browser: _handleNewAccessoriesNotification: %@
com.apple.external-accessory.wireless-configuration
textKey
[#Location] setNMEASentencesToFilter: not created by core accessories
void *CoreBluetoothUILibrary(void)
ACCExternalAccessoryProtocolDetailsKey
external-accessory
-[EAAccessoryManager _checkForConnectedAccessories:backgroundTaskIdentifier:]
[#ExternalAccessory] connection ID %lu not found in iap accessories list
EAAccessorySpeakerMenuEQNamesKey
EAVehicleInfoYearKey
[#ExternalAccessory] Adding protocol to array %@
[#ExternalAccessory] iapConnectedAccessories count = %lu, managerUUID %@
EAAccessoryVehicleDataUpdate
EAVehicleInfoSupportedChargingConnectorsBitMaskKey
ACCExternalAccessoryProtocolEndpointUUID
ExternalAccessoryWACUIBits.bundle
### principle:  %@
ACCExternalAccessoryProvider
EAAccessoryDidReceiveNMEASentenceNotification
ACCExternalAccessoryProtocolFirmwareVersionPending
[#Location] An NMEA sentence was not timestamped!
[#ExternalAccessory] No CoreAccessories kACCExternalAccessoryPrimaryUUID
kCFAccessoryPortUSBIn
kACCExternalAccessoryPrimaryUUID
EAVehicleInfoModelKey
EAVehicleInfoRangeElectricKey
FrontBoardServices.framework
[#ExternalAccessory] accessory disconnect failed because accessory with connectionID %u was not found
image
EAVehicleInfoHasLowDistanceRangeElectricKey
EAElectricVehicleChargingInfoMaximumVoltageKey
DismissOnLock
EAVehicleInfoDisplayNameKey
[#VehicleInfoStatus] %s: accessory UUID %@, vehicleStatusUpdate %@
-[EAAccessoryManager _externalAccessoryReconnected:]
kACCExternalAccessoryPPIDKey
backButton
EAVehicleInfoIsChargingKey
-[EAAccessory allPublicProtocolStrings]
-[EAAccessoryManager showBluetoothAccessoryPickerWithNameFilter:completion:]
[#ExternalAccessory] Timed out waiting for iAP device to appear
kACCExternalAccessoryRegionCodeKey
EAAccessoryNMEASentenceFromAccessoryKey
EAVehicleInfoPowerForConnectorTypeTeslaKey
EAWiFiUnconfiguredAccessoryBrowserPurgeAccessoriesSet
EAAccessoryInitException
%s
EAAccessoryMacAddress
EAAccessoryPointOfInterestBufferIDKey
EAVehicleInfoEngineTypeBitmaskKey
EAVehicleInfoSiriNameKey
NMEATimestampAverageSamples
wacDeviceID
Frameworks
CarKit
/Library/Caches/com.apple.xbs/64A9CE47-66B8-44B2-AEF8-07E8E0F98FC8/TemporaryDirectory.9fSknA/Sources/ExternalAccessory/EAInputStream.m
[#ExternalAccessory] canceling _sockListenSource
[#ExternalAccessory] WARNING: -sendPointOfInterestInformation:identifier is deprecated and will be removed!
[#ExternalAccessory] %@: background task already expired
-[EAAccessoryManager _externalAccessoryDisconnected:]
[#ExternalAccessory] eaAccessory CoreAccessoryPrimaryUUID = %@
deleteKey
EAVehicleInfoVehicleColorHexCodeKey
com.apple.ExternalAccessory.WACUI
-[EAAccessoryManager _initFromSingletonCreationMethod]
touchPhaseKey
EAAccessoryPointOfInterestKey
EAVehicleInfoHasLowDistanceRangeKey
### bundle:     %@
VisualVoicemail.framework
UIApplication
EACameraMaximumISO
searchField
kCFAccessoryPortPropertyAutoPlayOnConnect
/Library/Caches/com.apple.xbs/64A9CE47-66B8-44B2-AEF8-07E8E0F98FC8/TemporaryDirectory.9fSknA/Sources/ExternalAccessory/EAAccessoryManager.m
[#ExternalAccessory] %s:%s-%d accessory connectionID %u tagged as not found in IAP, skipping disconnect\n
[#ExternalAccessory] accessory disconnect received without connection ID
[#ExternalAccessory] Call sendWiredCarPlayAvailable:usbIdentifier:wirelessCarPlayAvailable:bluetoothIdentifier:themeAssetsAvailable:forUUID: for accessoryUUID %@
updatesFrequently
EACameraIdentifier
EACameraWidth
WAC: Browser: startSearchingForAccessories
CarKit.framework
UIBackgroundModes
/Library/Caches/com.apple.xbs/64A9CE47-66B8-44B2-AEF8-07E8E0F98FC8/TemporaryDirectory.9fSknA/Sources/ExternalAccessory/EASession.m
notEnabled
kCFAccessoryPortPropertyVolumeScalar
[#ExternalAccessory] %s backgroundTask %lu, resetting back to 0
EAVehicleInfoHasLowDistanceRangeCNGKey
[#ExternalAccessory] Some sort of error sending outgoing EA data for eaSessionUUID %@
map
EAVehicleInfoPowerForConnectorTypeMennekesKey
  name: %@ \n
com.apple.accessory.cli.*
EAAccessoryUpdateNotification
kCFAccessoryPortLineIn
-[EAAccessoryManager _findExtraAccessoriesContainedOnlyIniAP:]
EAAccessoryDidReceiveEphemerisRefreshInterval
speakingRateKey
EAVehicleInfoMinBatteryChargeKey
EAVehicleInfoCurrentBatteryChargeKey
WAC: Browser: configureAccessory: %@
[#ExternalAccessory] Handling _iapServerDied: __iapdCrashed %d -> %d, __iap2dStartedSinceLastAppExecution %d -> %d, __iapdStartedSinceLastAppExecution %d -> %d
[#ExternalAccessory] _applicationDidEnterBackground, %@
[#BTPicker] Address: %s Error code: %lu\n
wacSupportsSecureWAC
MobileCoreServices.framework
kCFAccessoryPortA2DPIn
kCFAccessoryPortPropertyFullDuplexIsSupported
/Library/Caches/com.apple.xbs/64A9CE47-66B8-44B2-AEF8-07E8E0F98FC8/TemporaryDirectory.9fSknA/Sources/ExternalAccessory/EAOutputStream.m
%@
WAC: Browser: ERROR: Unable to load EA WAC UI bundle.
EAIPAccessoryDisconnectedNotification
com.apple.logging
EACameraLensPosition
FrontBoardServices
-[EAInputStream dealloc]
voiceOverEnabledKey
softlink:r:path:/System/Library/PrivateFrameworks/CoreBluetoothUI.framework/CoreBluetoothUI
```

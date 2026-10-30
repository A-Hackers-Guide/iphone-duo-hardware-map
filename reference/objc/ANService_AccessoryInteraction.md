# `ANService`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ANSystemMonitorDelegate`, `_TtP20AccessoryInteraction48ANAccessoryFirmwareUpdateManagerDelegateProtocol_`, `ANDeviceDelegate`, `RadiosPreferencesDelegate`, `UARPControllerDelegateProtocol`, `ANServiceProtocol`
- 35 instance variables, 5 properties, 189 instance methods, 1 class methods

## Instance variables

```
@"ANAppMonitor" _appMonitor;
@"ANDeviceManager" _deviceManager;
@"NSMutableDictionary" _taskClientMap;
@"NSMutableSet" _clients;
@"NSMutableSet" _playSoundNotificationLeechClients;
@"NSMutableSet" _multiPartStatusNotificationClients;
@"NSMutableSet" _roseOnForClientOnDevice;
@"<ANClientProtocol>" _activeRangingClient;
@"NSMutableDictionary" _firmwareUpdateClientMap;
@"NSMutableSet" _connectionStateChangeClients;
@"ANMetricManager" _metricManager;
@"<ANCommuteMetricManagerProtocol>" _commuteMetricManager;
@"ANSystemMonitor" _systemMonitor;
@"UARPController" _uarpController;
@"NSMutableDictionary" _pendingTaskMap;
@"NSObject<OS_dispatch_queue>" _queue;
@"NSMutableArray" _devicesUndergoingFirmwareUpdate;
@"<ANScannerClientProtocol>" _scannerClient;
@"RadiosPreferences" _radiosPreferences;
@"NSUUID" _eventCounterDeviceUUID;
@"SPKeyReconciler" _keyReconciler;
@"NSMutableDictionary" _assetIdMap;
@"SPOwnerInterface" _spOwnerInterface;
@"<SPFirmwareUpdateSessionProtocol>" _spFirmwareUpdateSession;
q _assetLocationType;
i _stopUARPCaptureToken;
@"NSMutableDictionary" _localFirmwareUpdateAssetMap;
@"NSURL" _localHawkeyeFirmwareDirectory;
B _runningFindMyCertificationAssistant;
d _carLastScanned;
@"NSDateFormatter" _advTimeFormat;
@"ANLongHeldConnectionDetection" _longHeldConnectionDetection;
@"_TtC20AccessoryInteraction17ANMeDeviceMonitor" _meDeviceMonitor;
@"_TtC20AccessoryInteraction32ANAccessoryFirmwareUpdateManager<_TtP20AccessoryInteraction40ANAccessoryFirmwareUpdateManagerProtocol_>" _accessoryFirmwareUpdateManager;
@"<ANClientProtocol>" _shimDelegate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<ANClientProtocol>",N,V_shimDelegate) shimDelegate;
```

## Class methods

```
+[ANService convertBatteryStatus:];
```

## Instance methods

```
-[ANService requestDisconnectionForDevice:];
-[ANService systemWillSleep:];
-[ANService initWithQueue:];
-[ANService airplaneModeChanged];
-[ANService clientIdentifier];
-[ANService submitFirmwareVersionsForOwnedTags];
-[ANService cancelConnectionTimeoutForPeripheral:];
-[ANService submitFWUPCompletionMetricWithEventData:deviceUuid:];
-[ANService getDeviceUUID:];
-[ANService onObservationForDeviceWithIdentifier:type:date:];
-[ANService scanForNearbyOwner];
-[ANService endService];
-[ANService assetAvailablityUpdateForAccessoryID:assetID:];
-[ANService firmwareStagingComplete:assetID:withStatus:];
-[ANService firmwareStagingProgress:assetID:bytesSent:bytesTotal:];
-[ANService firmwareUpdateResult:vendorSpecificStatus:error:];
-[ANService sendMessageToAccessory:uarpMsg:error:];
-[ANService stagedFirmwareApplicationComplete:withStatus:];
-[ANService getGroupStatusForTag:forClient:];
-[ANService getMultiStatusForTag:forClient:];
-[ANService teardownClient:];
-[ANService beginServiceWithScannerClient:zoneMonitor:commuteMetricManager:];
-[ANService deviceUndergoingFirmwareUpdate:];
-[ANService performTask:forClient:onDevice:];
-[ANService systemConnectivity:isConnected:];
-[ANService _attachTAUnknownBeaconToDurianDevice:];
-[ANService _convertTASPAdvertisementDeviceTypeToSPBeaconType:];
-[ANService abortFirmwareUpdateForDevice:forClient:];
-[ANService attemptFirmwareUpdateConnectionWithDeviceUuid:];
-[ANService cleanUpTAUnknownBeaconRecord:];
-[ANService completeFetchFindingCapabilities:client:data:opcode:];
-[ANService completeRangingConfigure:client:data:opcode:];
-[ANService completeRangingDeinit:client:data:opcode:];
-[ANService completeRangingInit:client:data:opcode:];
-[ANService completeRangingStart:client:data:opcode:];
-[ANService configureNBRangingOnDevice:withParams:forClient:];
-[ANService configureRangingWithMacAddress:countryCode:uwbChannel:acqPreamble:trackingPreamble:interval:onTag:forClient:];
-[ANService connectToTag:forClient:];
-[ANService debugPerformAggressiveScan];
-[ANService deinitRangingOnTag:forClient:];
-[ANService device:checkForEchoOfOpcode:fromAck:];
-[ANService device:didAcknowledgeCommandForTask:];
-[ANService device:didCompleteTask:withCompletionCommand:];
-[ANService device:didFailToCompleteTask:withError:andDisconnect:];
-[ANService device:didPrepareForRangingWithError:withConnectionInterval:];
-[ANService device:didReceiveGroupRelationStatus:andMainteanceStatus:];
-[ANService device:didReceiveHawkeyeDataFragment:duringActiveTask:];
-[ANService device:didReceiveInvalidDataWithError:];
-[ANService device:didReceiveKeyRollIndex:];
-[ANService device:didReceiveRangingResponse:withOpcode:];
-[ANService device:didUpdateActivePeripheral:withError:];
-[ANService didFailFirmwareUpdateForDevice:withError:];
-[ANService didFailToConnectDevice:withError:];
-[ANService didReceiveUarpMessage:fromDevice:];
-[ANService didReceiveUarpMessageFromAccessory:fromDevice:];
-[ANService didRetrievePersonalizationInfo:forDevice:error:];
-[ANService didUpdateFirmwareForDevice:error:];
-[ANService didUpdateVehicularState:];
-[ANService disconnectFromTag:forClient:];
-[ANService dumpLogsOfType:forTag:forClient:];
-[ANService fetchAISAccessoryCapabilitiesForDevice:forClient:];
-[ANService fetchAISAccessoryCapabilitiesForTAUnknownBeacon:forClient:];
-[ANService fetchAISAccessoryCategoryForDevice:forClient:];
-[ANService fetchAISAccessoryCategoryForTAUnknownBeacon:forClient:];
-[ANService fetchAISBatteryLevelForDevice:forClient:];
-[ANService fetchAISBatteryLevelForTAUnknownBeacon:forClient:];
-[ANService fetchAISBatteryTypeForDevice:forClient:];
-[ANService fetchAISBatteryTypeForTAUnknownBeacon:forClient:];
-[ANService fetchAISFirmwareVersionForDevice:forClient:];
-[ANService fetchAISFirmwareVersionForTAUnknownBeacon:forClient:];
-[ANService fetchAISManufacturerNameForDevice:forClient:];
-[ANService fetchAISManufacturerNameForTAUnknownBeacon:forClient:];
-[ANService fetchAISModelNameForDevice:forClient:];
-[ANService fetchAISModelNameForTAUnknownBeacon:forClient:];
-[ANService fetchAISNetworkIDForDevice:forClient:];
-[ANService fetchAISNetworkIDForTAUnknownBeacon:forClient:];
-[ANService fetchAISProductDataForDevice:forClient:];
-[ANService fetchAISProductDataForTAUnknownBeacon:forClient:];
-[ANService fetchAISProtocolImplementationForDevice:forClient:];
-[ANService fetchAISProtocolImplementationForTAUnknownBeacon:forClient:];
-[ANService fetchAISSerialNumberForDevice:forClient:];
-[ANService fetchAISSerialNumberForTAUnknownBeacon:forClient:];
-[ANService fetchAccelerometerModeOnTag:forClient:];
-[ANService fetchAccelerometerOrientationModeConfigurationOnTag:forClient:];
-[ANService fetchAccelerometerSlopeModeConfigurationOnTag:forClient:];
-[ANService fetchAccessoryInformation:client:];
-[ANService fetchBatteryStateFromTag:forClient:];
-[ANService fetchConnectionStateForTag:forClient:];
-[ANService fetchFindingCapabilitiesOnTag:forClient:];
-[ANService fetchFirmwareVersionFromTag:forClient:includeCrashLogs:];
-[ANService fetchHawkeyeAISAccessoryCapabilitiesForDevice:forClient:];
-[ANService fetchHawkeyeAISAccessoryCapabilitiesForTAUnknownBeacon:forClient:];
-[ANService fetchHawkeyeAISAccessoryCategoryForDevice:forClient:];
-[ANService fetchHawkeyeAISAccessoryCategoryForTAUnknownBeacon:forClient:];
-[ANService fetchHawkeyeAISBatteryTypeForDevice:forClient:];
-[ANService fetchHawkeyeAISFindMyVersionForDevice:forClient:];
-[ANService fetchHawkeyeAISFirmwareVersionForDevice:forClient:];
-[ANService fetchHawkeyeAISFirmwareVersionForTAUnknownBeacon:forClient:];
-[ANService fetchHawkeyeAISManufacturerNameForDevice:forClient:];
-[ANService fetchHawkeyeAISManufacturerNameForTAUnknownBeacon:forClient:];
-[ANService fetchHawkeyeAISModelColorCodeForDevice:forClient:];
-[ANService fetchHawkeyeAISModelNameForDevice:forClient:];
-[ANService fetchHawkeyeAISModelNameForTAUnknownBeacon:forClient:];
-[ANService fetchHawkeyeAISProductDataForDevice:forClient:];
-[ANService fetchHawkeyeAISProductDataForTAUnknownBeacon:forClient:];
-[ANService fetchHawkeyeCurrentPrimaryKey:forClient:];
-[ANService fetchHawkeyeSerialNumber:forClient:];
-[ANService fetchHawkeyeiCloudIdentifier:forClient:];
-[ANService fetchTxPowerForDevice:forClient:asOwner:];
-[ANService fetchUserStatsWithPersistence:fromTag:forClient:];
-[ANService fetchWhetherLocalFirmwareAssetIsInUseForProductGroup:andProductNumber:forClient:];
-[ANService findMyAppDidBackgroundOrExit];
-[ANService getDevicesForProductGroup:andProductNumber:];
-[ANService getLastCarScanTime];
-[ANService getPersonalizationInfoForDevice:forClient:];
-[ANService getUarpAccessoryForDevice:];
-[ANService handleCompletionForPoshTask:withCompletionCommand:onDevice:];
-[ANService induceCrashOnTag:forClient:];
-[ANService informCoreUarpOfAssetChangeForProductGroup:andProductNumber:];
-[ANService initRangingWithMacAddress:onTag:forClient:];
-[ANService isBackgroundTask:];
-[ANService isPoshTask:];
-[ANService notifyClientOnNewFirmwareVersionWithDeviceUuid:newVersion:];
-[ANService notifyMaintenanceStateForAccessory:isMaintained:];
-[ANService onAdvertisement:reconciledInformation:];
-[ANService onAdvertisementBufferEmptied];
-[ANService onAggressiveScanEnded];
-[ANService onAggressiveScanStarted];
-[ANService onConnectionStateChangeForDeviceWithUUID:fromState:toState:];
-[ANService onFirstUnlock];
-[ANService onObservationForDeviceWithUUID:type:];
-[ANService onVehicularState];
-[ANService playSoundSequence:onTag:forClient:];
-[ANService playUnauthorizedSoundSequence:onTag:forClient:];
-[ANService poshTaskRequiringCompletionCommand:];
-[ANService prepareRangingOnTag:forClient:];
-[ANService registerMultiPartStatusNotificationForClient:];
-[ANService registerPlaySoundLeechNotificationsforClient:];
-[ANService releaseExtension:];
-[ANService requestDiscoveryScan];
-[ANService retryBeaconRecordFWVersionUpdateIfNeeded:];
-[ANService rollWildKeyOnTag:forClient:];
-[ANService sendConnectionMetrics:forDevice:];
-[ANService sendConnectionMetricsForDevice:withDuration:];
-[ANService sendFirmwareUpdateMetrics:forDevice:];
-[ANService sendUARPMessageToAccessoryWithDeviceUuid:uarpMsg:];
-[ANService setAccelerometerOrientationModeConfiguration:onTag:forClient:];
-[ANService setAccelerometerSlopeModeConfiguration:onTag:forClient:];
-[ANService setBatteryStatus:onTag:forClient:];
-[ANService setHawkeyeTestMode:onTag:forClient:];
-[ANService setHawkeyeUTMotionConfigWithSeparatedUTTimeoutSeconds:separatedUTBackoffTimeoutSeconds:forDevice:forClient:];
-[ANService setKeyRollInterval:onTag:forClient:];
-[ANService setNearOwnerTimeout:onTag:forClient:];
-[ANService setObfuscatedIdentifier:onTag:forClient:];
-[ANService setShimDelegate:];
-[ANService setTagType:onTag:forClient:];
-[ANService setUnauthorizedPlaySoundRateLimit:onTag:forClient:];
-[ANService setWildModeConfiguration:onTag:forClient:];
-[ANService shimDelegate];
-[ANService shouldDisconnectReconnectForDevice:];
-[ANService startAggressiveAdvertisingForDevice:withTimeout:forClient:];
-[ANService startEventCounterOnTag:forClient:];
-[ANService startMonitoringAirTagForFirmwareUpdate:];
-[ANService startMonitoringConnectionStateChangeForClient:];
-[ANService startMonitoringDeviceForFirmwareUpdate:];
-[ANService startNBRangingOnTag:withIRK:forClient:];
-[ANService startNBRangingOnTag:withIRK:fragmentCount:forClient:];
-[ANService startRangingWithTargetEventCounter:onTag:forClient:];
-[ANService startUnauthorizedAggressiveAdvertisingForDevice:forClient:];
-[ANService stopAggressiveAdvertisingForDevice:forClient:];
-[ANService stopEventCounterOnTag:forClient:];
-[ANService stopMonitoringAirTagForFirmwareUpdate:];
-[ANService stopMonitoringConnectionStateChangeForClient:];
-[ANService stopMonitoringDeviceForFirmwareUpdate:];
-[ANService stopPlayingSoundOnTag:forClient:];
-[ANService stopPlayingUnauthorizedSoundOnTag:forClient:];
-[ANService stopRangingOnTag:forClient:];
-[ANService systemCoexImpact:toState:];
-[ANService systemMetricHeartbeat];
-[ANService systemWaking:atTime:];
-[ANService teardownConnectionWithDeviceUuid:];
-[ANService unpairFromTag:forClient:];
-[ANService unpairFromTagWithAddress:forClient:];
-[ANService unregisterMultiPartStatusNotificationForClient:];
-[ANService unregisterPlaySoundLeechNotificationsforClient:];
-[ANService updateFirmwareForDevice:withAssetURL:forClient:];
-[ANService updateSystemLoiType:isEntry:];
-[ANService useDefaultFirmwareAssetSourceForProductGroup:andProductNumber:forClient:];
-[ANService useLocalFirmwareAssetFromUrl:forProductGroup:forProductNumber:withSandboxExtension:forClient:];
```

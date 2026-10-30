# `CLFindMyAccessoryManager`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 97 instance methods, 2 class methods

## Instance variables

```
@"<CLFindMyAccessoryManagerDelegate>" _delegate;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
{unique_ptr<CLConnectionClient, std::default_delete<CLConnectionClient>>=""{?="__ptr_"^{CLConnectionClient}}} _connection;
@"CLFindMyAccessoryFragmentAccumulator" _accumulator;
```

## Properties

```
@property (T@"<CLFindMyAccessoryManagerDelegate>",W,N,V_delegate) delegate;
```

## Class methods

```
+[CLFindMyAccessoryManager checkAvailabilityForPairedOwnerInformationControlPointMessages:messageName:];
+[CLFindMyAccessoryManager errorFromFragmentationStatus:];
```

## Instance methods

```
-[CLFindMyAccessoryManager handleMessage:];
-[CLFindMyAccessoryManager connectDevice:];
-[CLFindMyAccessoryManager sendMessage:];
-[CLFindMyAccessoryManager init];
-[CLFindMyAccessoryManager dealloc];
-[CLFindMyAccessoryManager handleInterruption];
-[CLFindMyAccessoryManager setDelegate:];
-[CLFindMyAccessoryManager disconnectDevice:];
-[CLFindMyAccessoryManager delegate];
-[CLFindMyAccessoryManager initWithDelegate:delegateQueue:];
-[CLFindMyAccessoryManager fetchAISProtocolImplementation:];
-[CLFindMyAccessoryManager fetchTxPowerFromDevice:asOwner:];
-[CLFindMyAccessoryManager initRangingOnDevice:macAddress:];
-[CLFindMyAccessoryManager fetchFirmwareVersionFromDevice:];
-[CLFindMyAccessoryManager initAccumulator];
-[CLFindMyAccessoryManager startNBRangingOnDevice:withIRK:];
-[CLFindMyAccessoryManager configureNBRangingOnDevice:withParams:];
-[CLFindMyAccessoryManager configureRangingOnDevice:macAddress:countryCode:uwbChannel:acqPreamble:trackingPreamble:interval:];
-[CLFindMyAccessoryManager deinitRangingOnDevice:];
-[CLFindMyAccessoryManager dumpLogDataOfType:fromDevice:];
-[CLFindMyAccessoryManager fetchAISAccessoryCapabilities:];
-[CLFindMyAccessoryManager fetchAISAccessoryCategory:];
-[CLFindMyAccessoryManager fetchAISBatteryLevel:];
-[CLFindMyAccessoryManager fetchAISBatteryType:];
-[CLFindMyAccessoryManager fetchAISFirmwareVersion:];
-[CLFindMyAccessoryManager fetchAISForTAUnknownBeacon:macAddress:deviceType:];
-[CLFindMyAccessoryManager fetchAISManufacturerName:];
-[CLFindMyAccessoryManager fetchAISModelName:];
-[CLFindMyAccessoryManager fetchAISNetworkID:];
-[CLFindMyAccessoryManager fetchAISProductData:];
-[CLFindMyAccessoryManager fetchAISSerialNumber:];
-[CLFindMyAccessoryManager fetchAccelerometerOrientationModeConfigurationForDevice:];
-[CLFindMyAccessoryManager fetchAccelerometerSlopeModeConfigurationForDevice:];
-[CLFindMyAccessoryManager fetchAccessoryInformationForDevice:];
-[CLFindMyAccessoryManager fetchBatteryStatusForDevice:];
-[CLFindMyAccessoryManager fetchConnectionStateForDevice:];
-[CLFindMyAccessoryManager fetchFindingCapabilities:];
-[CLFindMyAccessoryManager fetchHawkeyeAISAccessoryCapabilities:];
-[CLFindMyAccessoryManager fetchHawkeyeAISAccessoryCategory:];
-[CLFindMyAccessoryManager fetchHawkeyeAISBatteryType:];
-[CLFindMyAccessoryManager fetchHawkeyeAISFindMyVersion:];
-[CLFindMyAccessoryManager fetchHawkeyeAISManufacturerName:];
-[CLFindMyAccessoryManager fetchHawkeyeAISModelColorCode:];
-[CLFindMyAccessoryManager fetchHawkeyeAISModelName:];
-[CLFindMyAccessoryManager fetchHawkeyeAISProductData:];
-[CLFindMyAccessoryManager fetchHawkeyeCurrentPrimaryKey:];
-[CLFindMyAccessoryManager fetchHawkeyeSerialNumber:];
-[CLFindMyAccessoryManager fetchHawkeyeiCloudIdentifier:];
-[CLFindMyAccessoryManager fetchStatusOfUTEnablementRequirements];
-[CLFindMyAccessoryManager fetchTxPower:];
-[CLFindMyAccessoryManager fetchUserStatsWithPersistence:fromDevice:];
-[CLFindMyAccessoryManager forceSurfaceStagedDetections:deviceType:detailsBitmask:];
-[CLFindMyAccessoryManager getMultiPartStatusFromDevice:];
-[CLFindMyAccessoryManager getMultiStatusFromDevice:];
-[CLFindMyAccessoryManager induceCrashOnDevice:];
-[CLFindMyAccessoryManager performAggressiveScanForDurianService];
-[CLFindMyAccessoryManager performAggressiveScanForSeparationAlerts];
-[CLFindMyAccessoryManager performAggressiveScanForTrackingAvoidance];
-[CLFindMyAccessoryManager performHELEScanForTrackingAvoidance];
-[CLFindMyAccessoryManager performLongAggressiveScanForSeparationAlerts];
-[CLFindMyAccessoryManager prepareRangingOnDevice:];
-[CLFindMyAccessoryManager rollWildKeyOnDevice:];
-[CLFindMyAccessoryManager scanForHELE];
-[CLFindMyAccessoryManager scanForNearbyDevicesLong];
-[CLFindMyAccessoryManager scanForNearbyOwner];
-[CLFindMyAccessoryManager sendMessage:withPayload:];
-[CLFindMyAccessoryManager setAccelerometerOrientationModeConfiguration:forDevice:];
-[CLFindMyAccessoryManager setAccelerometerSlopeModeConfiguration:forDevice:];
-[CLFindMyAccessoryManager setBatteryStatus:forDevice:];
-[CLFindMyAccessoryManager setDeviceType:onDevice:];
-[CLFindMyAccessoryManager setHawkeyeTestMode:forDevice:];
-[CLFindMyAccessoryManager setHawkeyeUTMotionConfigWithSeparatedUTTimeoutSeconds:separatedUTBackoffTimeoutSeconds:forDevice:];
-[CLFindMyAccessoryManager setKeyRollInterval:onDevice:];
-[CLFindMyAccessoryManager setNearOwnerTimeout:onDevice:];
-[CLFindMyAccessoryManager setObfuscatedIdentifier:onDevice:];
-[CLFindMyAccessoryManager setUnauthorizedPlaySoundRateLimit:forDevice:];
-[CLFindMyAccessoryManager setWildConfiguration:onDevice:];
-[CLFindMyAccessoryManager stageTADetection:deviceType:detailsBitmask:shouldRemoveDevice:];
-[CLFindMyAccessoryManager startAggressiveAdvertisingOnDevice:withTimeout:];
-[CLFindMyAccessoryManager startEventCounterForDevice:];
-[CLFindMyAccessoryManager startMonitoringForAvengerAdvertisementsForBTFinding];
-[CLFindMyAccessoryManager startNBRangingOnDevice:withIRK:fragmentCount:];
-[CLFindMyAccessoryManager startPlayingSoundSequence:onDevice:];
-[CLFindMyAccessoryManager startPlayingUnauthorizedSoundOnDevice:];
-[CLFindMyAccessoryManager startPlayingUnauthorizedSoundSequence:onDevice:];
-[CLFindMyAccessoryManager startRangingOnDevice:targetEventCounter:];
-[CLFindMyAccessoryManager startUnauthorizedAggressiveAdvertisingOnDevice:];
-[CLFindMyAccessoryManager stopAggressiveAdvertisingOnDevice:];
-[CLFindMyAccessoryManager stopEventCounterForDevice:];
-[CLFindMyAccessoryManager stopLongAggressiveScanForSeparationAlerts];
-[CLFindMyAccessoryManager stopMonitoringForAvengerAdvertisementsForBTFinding];
-[CLFindMyAccessoryManager stopPlayingSoundOnDevice:];
-[CLFindMyAccessoryManager stopPlayingUnauthorizedSoundOnDevice:];
-[CLFindMyAccessoryManager stopRangingOnDevice:];
-[CLFindMyAccessoryManager stopScanForNearbyDevicesLong];
-[CLFindMyAccessoryManager unpairFromDevice:];
-[CLFindMyAccessoryManager unpairFromDeviceWithAddress:];
```

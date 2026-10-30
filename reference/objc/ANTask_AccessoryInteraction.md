# `ANTask`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 9 properties, 29 instance methods, 140 class methods

## Instance variables

```
Q _creationTime;
Q _startTime;
Q _completionTime;
B _expectsResponse;
B _requiresMutex;
B _completeOnPreemption;
B _cancelled;
@"NSUUID" _uuid;
@"ANCommand" _command;
Q _context;
q _desiredLatency;
```

## Properties

```
@property (T@"NSUUID",R,V_uuid) uuid;
@property (T@"ANCommand",&,V_command) command;
@property (TB,V_expectsResponse) expectsResponse;
@property (TB,V_requiresMutex) requiresMutex;
@property (TB,R,V_completeOnPreemption) completeOnPreemption;
@property (Tq,R) timeoutSeconds;
@property (TQ,R,V_context) context;
@property (TB,R,GisCancelled,V_cancelled) cancelled;
@property (Tq,R,V_desiredLatency) desiredLatency;
```

## Class methods

```
+[ANTask initRosePoshTaskWithParameters:];
+[ANTask setMutexAction:];
+[ANTask startUnauthorizedShortSoundTask];
+[ANTask induceCrashTask];
+[ANTask rollWildKeyTask];
+[ANTask setMaxConnectionsTaskWithCount:];
+[ANTask startNonOwnerShortSoundPoshTask];
+[ANTask checkCrashesTask];
+[ANTask configureNBRangingHawkeyeTaskWithParameters:];
+[ANTask configureNBRangingNonOwnerPoshTaskWithPayload:];
+[ANTask configureRangingHawkeyeTaskWithPayload:];
+[ANTask configureRangingNonOwnerPoshTaskWithPayload:];
+[ANTask configureRangingNonOwnerTaskWithPayload:];
+[ANTask configureSeparatedStateHawkeyeTaskWithConfiguration:currentIndex:];
+[ANTask deinitRangingHawkeyeTask];
+[ANTask deinitRangingNonOwnerPoshTask];
+[ANTask deinitRangingNonOwnerTask];
+[ANTask dumpNordicCrashesTask];
+[ANTask dumpNordicLogsTask];
+[ANTask dumpRoseCrashesTask];
+[ANTask dumpRoseLogsTask];
+[ANTask enablePersistentConnectionsHawkeyeTask:];
+[ANTask fetchAccelerometerModeTask];
+[ANTask fetchAccelerometerOrientationModeConfigurationTask];
+[ANTask fetchAccelerometerSlopeModeConfigurationTask];
+[ANTask fetchAccessoryCapabilitiesGATTTask];
+[ANTask fetchAccessoryCategoryGATTTask];
+[ANTask fetchBatteryLevelGATTTask];
+[ANTask fetchBatteryStatusTask];
+[ANTask fetchBatteryTypeGATTTask];
+[ANTask fetchCurrentKeyIndexTask];
+[ANTask fetchFindMyVersionGATTTask];
+[ANTask fetchFindingCapabilitiesHawkeyeTaskWithPayload:];
+[ANTask fetchFindingCapabilitiesNonOwnerPoshTaskWithPayload:];
+[ANTask fetchFindingCapabilitiesTaskWithPayload:];
+[ANTask fetchFirmwareVersionGATTTask];
+[ANTask fetchFirmwareVersionTaskWithCrashLogs:];
+[ANTask fetchHardwareFaultStatusTask];
+[ANTask fetchHeleAccessoryCapabilitiesTask];
+[ANTask fetchHeleBatteryLevelTask];
+[ANTask fetchHeleFirmwareVersionTask];
+[ANTask fetchManufacturerNameGATTTask];
+[ANTask fetchModelColorCodeGATTTask];
+[ANTask fetchModelNameGATTTask];
+[ANTask fetchMultiStatusTask];
+[ANTask fetchNonOwnerAccessoryCapabilitiesPoshTask];
+[ANTask fetchNonOwnerAccessoryCapabilitiesTask];
+[ANTask fetchNonOwnerAccessoryCategoryPoshTask];
+[ANTask fetchNonOwnerAccessoryCategoryTask];
+[ANTask fetchNonOwnerBatteryLevelPoshTask];
+[ANTask fetchNonOwnerBatteryLevelTask];
+[ANTask fetchNonOwnerBatteryTypePoshTask];
+[ANTask fetchNonOwnerBatteryTypeTask];
+[ANTask fetchNonOwnerFindMyVersionTask];
+[ANTask fetchNonOwnerFirmwareVersionPoshTask];
+[ANTask fetchNonOwnerFirmwareVersionTask];
+[ANTask fetchNonOwnerManufacturerNamePoshTask];
+[ANTask fetchNonOwnerManufacturerNameTask];
+[ANTask fetchNonOwnerModelNamePoshTask];
+[ANTask fetchNonOwnerModelNameTask];
+[ANTask fetchNonOwnerNetworkIdPoshTask];
+[ANTask fetchNonOwnerProductDataPoshTask];
+[ANTask fetchNonOwnerProductDataTask];
+[ANTask fetchNonOwnerProtocolImplementationPoshTask];
+[ANTask fetchNonOwnerSerialNumberPoshTask];
+[ANTask fetchNonOwnerTxPowerTask];
+[ANTask fetchProductDataGATTTask];
+[ANTask fetchTxPowerGATTTask];
+[ANTask fetchTxPowerTask];
+[ANTask fetchUserStatsTaskWithPersistence_v0:context:];
+[ANTask fetchUserStatsTaskWithPersistence_v1:context:];
+[ANTask fetchUserStatsTaskWithPersistence_v2:context:];
+[ANTask fetchUserStatsTaskWithPersistence_v3:context:];
+[ANTask fwdlAbortTask];
+[ANTask getCurrentPrimaryKeyTask];
+[ANTask getGroupStatusHawkeyeTask];
+[ANTask getMultiStatusHawkeyeTask];
+[ANTask getSerialNumberTask];
+[ANTask getiCloudIdentifierTask];
+[ANTask initRangingHawkeyeTask];
+[ANTask initRoseNonOwnerTaskWithParameters:];
+[ANTask initRoseTaskWithParameters:];
+[ANTask latchSeparatedKeyHawkeyeTask];
+[ANTask leashDisableTask];
+[ANTask leashTask];
+[ANTask placeholderHawkeyeTask];
+[ANTask placeholderHawkeyeTaskWithIntent:];
+[ANTask resetHawkeyeTask];
+[ANTask retrieveLogsHawkeyeTask];
+[ANTask sendUARPMessageTaskWithPayloadForAirTag:];
+[ANTask sendUARPMessageTaskWithPayloadForHawkeye:];
+[ANTask setAbsoluteWildModeConfigurationTaskWithConfiguration:context:];
+[ANTask setAccelerometerOrientationModeConfigurationTaskWithConfiguration:];
+[ANTask setAccelerometerSlopeModeConfigurationTaskWithConfiguration:];
+[ANTask setBatteryStatusTaskWithBatteryStatus:];
+[ANTask setCentralReferenceTimeTask];
+[ANTask setHawkeyeUTMotionConfigWithSeparatedUTTimeoutSeconds:separatedUTBackoffTimeoutSeconds:];
+[ANTask setKeyRotationTimeoutHawkeyeTaskWithTimeout:];
+[ANTask setKeyRotationTimeoutTaskWithTimeout:];
+[ANTask setMaxConnectionsHawkeyeTaskWithCount:];
+[ANTask setMutexAction:withLatency:];
+[ANTask setNearOwnerTimeoutTaskWithTimeout:];
+[ANTask setNearbyTimeoutHawkeyeTaskWithTimeout:asHele:];
+[ANTask setObfuscatedIdentifierTaskWithIdentifier:];
+[ANTask setRoseNBRangingParametersTaskWithParameters:];
+[ANTask setRoseRangingParametersTaskWithParameters:];
+[ANTask setTagTypeTaskWithType:];
+[ANTask setUnauthorizedPlaySoundRateLimitTask:];
+[ANTask setUtcHawkeyeTask];
+[ANTask setWildModeConfigurationTaskWithConfiguration:];
+[ANTask startAggressiveAdvertisingTaskWithTimeout:];
+[ANTask startNBRangingHawkeyeTaskWithIRK:];
+[ANTask startNBRangingNonOwnerPoshTaskWithIRK:fragmentCount:];
+[ANTask startNonOwnerAggressiveAdvertisingTask];
+[ANTask startNonOwnerPoshAggressiveAdvertisingTask];
+[ANTask startNonOwnerShortSoundHawkeyeTask];
+[ANTask startNonOwnerSoundHawkeyeTask];
+[ANTask startNonOwnerSoundPoshTask];
+[ANTask startRangingHawkeyeTaskWithTargetEventCounter:];
+[ANTask startRangingNonOwnerPoshTaskWithTargetEventCounter:];
+[ANTask startRangingNonOwnerTaskWithTargetEventCounter:];
+[ANTask startRoseNBRangingTaskWithIRK:fragmentCount:];
+[ANTask startRoseRangingTaskWithParameters:];
+[ANTask startShortSoundHawkeyeTask];
+[ANTask startSoundHawkeyeTask];
+[ANTask startSoundSequenceTaskWithEncodedSequence:];
+[ANTask startUnauthorizedSoundTask];
+[ANTask stopAggressiveAdvertisingTask];
+[ANTask stopNonOwnerSoundHawkeyeTask];
+[ANTask stopNonOwnerSoundPoshTask];
+[ANTask stopRangingHawkeyeTask];
+[ANTask stopRangingNonOwnerPoshTask];
+[ANTask stopRangingNonOwnerTask];
+[ANTask stopRoseRangingTask];
+[ANTask stopRoseTaskWithParameters:];
+[ANTask stopSoundHawkeyeTask];
+[ANTask stopSoundTask];
+[ANTask testModeTask:];
+[ANTask unpairHawkeyeTask];
+[ANTask unpairTask];
```

## Instance methods

```
-[ANTask creationTime];
-[ANTask uuid];
-[ANTask init];
-[ANTask startTime];
-[ANTask dealloc];
-[ANTask command];
-[ANTask isCancelled];
-[ANTask complete];
-[ANTask completionTime];
-[ANTask willStart];
-[ANTask timeoutSeconds];
-[ANTask cancel];
-[ANTask context];
-[ANTask setCommand:];
-[ANTask executionDuration];
-[ANTask expectsResponse];
-[ANTask setExpectsResponse:];
-[ANTask completeOnPreemption];
-[ANTask desiredLatency];
-[ANTask initWithCommand:desiredLatency:expectsResponse:completeOnPreemption:requiresMutex:];
-[ANTask initWithCommand:desiredLatency:expectsResponse:completeOnPreemption:requiresMutex:context:];
-[ANTask isMutexProtectedRangingTask];
-[ANTask isMutexProtectedSoundTask];
-[ANTask queueDuration];
-[ANTask requiresMutex];
-[ANTask setRequiresMutex:];
-[ANTask shouldCompleteOnPreemptionByTask:];
-[ANTask shouldPreemptTask:];
-[ANTask translatedOpcode];
```

# `CLLocationInternalClient`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 114 instance methods, 1 class methods

## Instance variables

```
@"NSXPCConnection" _connection;
```

## Class methods

```
+[CLLocationInternalClient sharedServiceClient];
```

## Instance methods

```
-[CLLocationInternalClient configure:];
-[CLLocationInternalClient setIsEligibleForAlwaysAuthorizationRequest:forBundleID:orBundlePath:replyBlock:];
-[CLLocationInternalClient setTemporaryAuthorizationGranted:forBundleID:orBundlePath:orAuditToken:byLocationButton:voiceInteractionEnabled:];
-[CLLocationInternalClient checkAndExerciseAuthorizationForBundleID:orBundlePath:services:error:];
-[CLLocationInternalClient dumpLogs:];
-[CLLocationInternalClient startStopAdvertisingBeacon:power:];
-[CLLocationInternalClient getEEDCloakingKey:];
-[CLLocationInternalClient notifyWeatherForecast:airQualityConditions:hourlyForecasts:dailyForecasts:latitude:longitude:];
-[CLLocationInternalClient shutdownDaemon];
-[CLLocationInternalClient copyRecentLocationsBufferStatus];
-[CLLocationInternalClient dynamicallyReduceAccuracyForLocation:completion:];
-[CLLocationInternalClient enableGnssRestrictedMode];
-[CLLocationInternalClient copyNearbyAssetSettings];
-[CLLocationInternalClient getAuthorizationStatus:forBundleID:orBundlePath:];
-[CLLocationInternalClient copyTechnologiesInUse];
-[CLLocationInternalClient getAccessoryMotionSensorLogs];
-[CLLocationInternalClient getPinnedLocationAuthorizationState:];
-[CLLocationInternalClient setMapMatchingRouteHint:count:routingType:stepType:];
-[CLLocationInternalClient getAuthorizationStatusForApp:withAuditToken:];
-[CLLocationInternalClient getPrecisionPermission:forBundleID:orBundlePath:];
-[CLLocationInternalClient pingDaemon];
-[CLLocationInternalClient clearLocationAuthorizations];
-[CLLocationInternalClient setLearnedRoutesAccess:forBundleID:orBundlePath:];
-[CLLocationInternalClient copyNearbyAssetSettingsOfAccessoryFile:];
-[CLLocationInternalClient fetchRecentLocationAtMachContinuousTime:];
-[CLLocationInternalClient copyMonitoredRegionsForBundleIdentifier:orBundlePath:];
-[CLLocationInternalClient getStatusBarIconState];
-[CLLocationInternalClient setGestureServiceEnabled:];
-[CLLocationInternalClient getGroundAltitudeForBundleID:orBundlePath:location:groundAltitude:];
-[CLLocationInternalClient updatePillButtonChoiceForOutstandingPrompt:];
-[CLLocationInternalClient setAuthorizationStatusByType:withCorrectiveCompensation:andZoneIdentifier:andSubIdentityIdentifier:forBundleID:orBundlePath:];
-[CLLocationInternalClient gyroCalibrationDatabaseWipe];
-[CLLocationInternalClient notifyPassKitPayment:transaction:info:];
-[CLLocationInternalClient copyRoutineAssetSettingsWithCompatibilityVersion:contentVersion:];
-[CLLocationInternalClient getEmergencyLocationSettingsCompatibilityVersion:andContentVersion:];
-[CLLocationInternalClient setTemporaryAuthorizationStatusForBundleId:orBundlePath:statusData:];
-[CLLocationInternalClient getEEDEmergencyContactNames:];
-[CLLocationInternalClient registerCircularInterestZoneWithId:latitude:longitude:radius:serviceMaskOperator:provenanceType:forBundleId:orBundlePath:error:];
-[CLLocationInternalClient applyArchivedAuthorizationDecisions:];
-[CLLocationInternalClient getAccessoryTypeBitSet];
-[CLLocationInternalClient tearDownLocationAuthPromptForBundleID:orBundlePath:];
-[CLLocationInternalClient getIncidentalUseMode:forBundleID:orBundlePath:];
-[CLLocationInternalClient copyActiveClientsUsingLocation];
-[CLLocationInternalClient clearLocationAuthorizationForLoctoolWithBundleId:orBundlePath:];
-[CLLocationInternalClient setAuthorizationStatus:withCorrectiveCompensation:forBundleID:orBundlePath:];
-[CLLocationInternalClient copyGnssBandsInUse];
-[CLLocationInternalClient getLocationServicesEnabled:];
-[CLLocationInternalClient copyAuthorizationFromBundleID:toBundleID:];
-[CLLocationInternalClient setTemporaryPreciseAuthorizationGranted:forBundleID:orBundlePath:];
-[CLLocationInternalClient gyroCalibrationDatabaseSupportsMiniCalibration:];
-[CLLocationInternalClient setTrackRunHint:];
-[CLLocationInternalClient setRelevance:forInterestZoneWithId:registeredForBundleId:orBundlePath:error:];
-[CLLocationInternalClient setLocationDefaultForKey:value:];
-[CLLocationInternalClient fetchRecentLocationAtCfAbsoluteTime:];
-[CLLocationInternalClient copyActivityAlarms];
-[CLLocationInternalClient copyInternalState];
-[CLLocationInternalClient checkAndExerciseLearnedRoutesAuthorizationForBundleID:orBundlePath:replyBlock:];
-[CLLocationInternalClient clearLocationAuthorizationForBundleId:orBundlePath:];
-[CLLocationInternalClient getGyroCalibrationDatabaseNumTemperatures:];
-[CLLocationInternalClient shouldDisplayEEDUI];
-[CLLocationInternalClient getGestureServiceEnabled:];
-[CLLocationInternalClient setPrivateMode:];
-[CLLocationInternalClient deleteCurrentEmergencyLocationAsset];
-[CLLocationInternalClient setLocationServicesEnabled:];
-[CLLocationInternalClient getGyroCalibrationDatabaseBiasFit:atTemperature:];
-[CLLocationInternalClient getArchivedAuthorizationDecisionsWithError:];
-[CLLocationInternalClient deleteInterestZoneWithId:registeredForBundleId:orBundlePath:error:];
-[CLLocationInternalClient connection];
-[CLLocationInternalClient getMotionSensorLogs];
-[CLLocationInternalClient requestRouteReconstructionForPedestrian];
-[CLLocationInternalClient disableGnssRestrictedMode];
-[CLLocationInternalClient insertGyroCalibrationDatabaseBiasEstimateIfValid:temperature:variance:timestamp:];
-[CLLocationInternalClient promoteSystemServiceWithBundlePath:];
-[CLLocationInternalClient setPinnedLocationAuthorization:];
-[CLLocationInternalClient triggerExpiredAuthorizationPurgeOnClientManager];
-[CLLocationInternalClient setSupportedAuthorizationMask:forBundleID:orBundlePath:replyBlock:];
-[CLLocationInternalClient getAccessoryPASCDTransmissionState];
-[CLLocationInternalClient setBackgroundIndicatorForBundleID:orBundlePath:enabled:];
-[CLLocationInternalClient copyLastLog];
-[CLLocationInternalClient asynchronousRemoteObject];
-[CLLocationInternalClient synchronousRemoteObject];
-[CLLocationInternalClient getLocationDefaultForKey:];
-[CLLocationInternalClient setIncidentalUseMode:forBundleID:orBundlePath:];
-[CLLocationInternalClient triggerRecentLocationsRevisedFromMachContinuousTime:toMachContinuousTime:];
-[CLLocationInternalClient isEligibleForAlwaysAuthorizationRequestForBundleID:orBundlePath:replyBlock:];
-[CLLocationInternalClient copyAppsUsingLocation];
-[CLLocationInternalClient getControlPlaneStatusReportClear:startTime:endTime:latitude:longitude:altitude:accuracy:vunc:status:];
-[CLLocationInternalClient setLocationButtonUseMode:forBundleID:orBundlePath:];
-[CLLocationInternalClient getLocationForBundleID:orBundlePath:dynamicAccuracyReductionEnabled:allowsAlteredAccessoryLocations:location:];
-[CLLocationInternalClient performMigration];
-[CLLocationInternalClient getTemporaryAuthorizationStatusForBundleId:orBundlePath:error:];
-[CLLocationInternalClient getPipelinedCache];
-[CLLocationInternalClient updatePromptedLatitude:longitude:];
-[CLLocationInternalClient fetchRecentLocationsInLastSeconds:];
-[CLLocationInternalClient forceAuthSync:];
-[CLLocationInternalClient setClientQuarantined:forBundleID:orBundlePath:];
-[CLLocationInternalClient displayStatistics];
-[CLLocationInternalClient getAuthorizationPromptMapDisplayEnabled:];
-[CLLocationInternalClient setAuthorizationPromptMapDisplayEnabled:];
-[CLLocationInternalClient getPrivateMode];
-[CLLocationInternalClient timeZoneAtLocation:];
-[CLLocationInternalClient copyZaxisStats];
-[CLLocationInternalClient reportLocationUtilityEvent:atDate:];
-[CLLocationInternalClient timeSyncMachTimeStamp:oscarTimeStamp:];
-[CLLocationInternalClient getVisitHistoryAccessAllowedTime:forBundleID:orBundlePath:];
-[CLLocationInternalClient getLearnedRoutesAccess:forBundleID:orBundlePath:];
-[CLLocationInternalClient getVisitHistoryAccess:forBundleID:orBundlePath:];
-[CLLocationInternalClient checkAndExercisePushClientAuthorizationForBundleID:replyBlock:];
-[CLLocationInternalClient setStatusBarIconEnabled:forEntityClass:];
-[CLLocationInternalClient setVisitHistoryAccess:forBundleID:orBundlePath:];
-[CLLocationInternalClient getOdometryBatchedLocations];
-[CLLocationInternalClient getStatusBarIconEnabled:forEntityClass:];
-[CLLocationInternalClient registerPhenolicInterestZoneWithId:phenolicLocation:serviceMaskOperator:provenanceType:forBundleId:orBundlePath:error:];
-[CLLocationInternalClient modifyOrSetAuthorizationTime:forBundleID:orBundlePath:];
```

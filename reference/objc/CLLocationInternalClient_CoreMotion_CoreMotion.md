# `CLLocationInternalClient_CoreMotion`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 108 instance methods, 1 class methods

## Instance variables

```
@"NSXPCConnection" _connection;
```

## Class methods

```
+[CLLocationInternalClient_CoreMotion sharedServiceClient];
```

## Instance methods

```
-[CLLocationInternalClient_CoreMotion configure:];
-[CLLocationInternalClient_CoreMotion setIsEligibleForAlwaysAuthorizationRequest:forBundleID:orBundlePath:replyBlock:];
-[CLLocationInternalClient_CoreMotion setTemporaryAuthorizationGranted:forBundleID:orBundlePath:orAuditToken:byLocationButton:voiceInteractionEnabled:];
-[CLLocationInternalClient_CoreMotion checkAndExerciseAuthorizationForBundleID:orBundlePath:services:error:];
-[CLLocationInternalClient_CoreMotion dumpLogs:];
-[CLLocationInternalClient_CoreMotion startStopAdvertisingBeacon:power:];
-[CLLocationInternalClient_CoreMotion getEEDCloakingKey:];
-[CLLocationInternalClient_CoreMotion notifyWeatherForecast:airQualityConditions:hourlyForecasts:dailyForecasts:latitude:longitude:];
-[CLLocationInternalClient_CoreMotion shutdownDaemon];
-[CLLocationInternalClient_CoreMotion dynamicallyReduceAccuracyForLocation:completion:];
-[CLLocationInternalClient_CoreMotion enableGnssRestrictedMode];
-[CLLocationInternalClient_CoreMotion copyNearbyAssetSettings];
-[CLLocationInternalClient_CoreMotion getAuthorizationStatus:forBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion copyTechnologiesInUse];
-[CLLocationInternalClient_CoreMotion getAccessoryMotionSensorLogs];
-[CLLocationInternalClient_CoreMotion getPinnedLocationAuthorizationState:];
-[CLLocationInternalClient_CoreMotion setMapMatchingRouteHint:count:routingType:stepType:];
-[CLLocationInternalClient_CoreMotion getAuthorizationStatusForApp:withAuditToken:];
-[CLLocationInternalClient_CoreMotion getPrecisionPermission:forBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion pingDaemon];
-[CLLocationInternalClient_CoreMotion clearLocationAuthorizations];
-[CLLocationInternalClient_CoreMotion setLearnedRoutesAccess:forBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion copyNearbyAssetSettingsOfAccessoryFile:];
-[CLLocationInternalClient_CoreMotion copyMonitoredRegionsForBundleIdentifier:orBundlePath:];
-[CLLocationInternalClient_CoreMotion getStatusBarIconState];
-[CLLocationInternalClient_CoreMotion setGestureServiceEnabled:];
-[CLLocationInternalClient_CoreMotion getGroundAltitudeForBundleID:orBundlePath:location:groundAltitude:];
-[CLLocationInternalClient_CoreMotion updatePillButtonChoiceForOutstandingPrompt:];
-[CLLocationInternalClient_CoreMotion setAuthorizationStatusByType:withCorrectiveCompensation:andZoneIdentifier:andSubIdentityIdentifier:forBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion gyroCalibrationDatabaseWipe];
-[CLLocationInternalClient_CoreMotion notifyPassKitPayment:transaction:info:];
-[CLLocationInternalClient_CoreMotion copyRoutineAssetSettingsWithCompatibilityVersion:contentVersion:];
-[CLLocationInternalClient_CoreMotion getEmergencyLocationSettingsCompatibilityVersion:andContentVersion:];
-[CLLocationInternalClient_CoreMotion setTemporaryAuthorizationStatusForBundleId:orBundlePath:statusData:];
-[CLLocationInternalClient_CoreMotion getEEDEmergencyContactNames:];
-[CLLocationInternalClient_CoreMotion registerCircularInterestZoneWithId:latitude:longitude:radius:serviceMaskOperator:provenanceType:forBundleId:orBundlePath:error:];
-[CLLocationInternalClient_CoreMotion applyArchivedAuthorizationDecisions:];
-[CLLocationInternalClient_CoreMotion getAccessoryTypeBitSet];
-[CLLocationInternalClient_CoreMotion tearDownLocationAuthPromptForBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion getIncidentalUseMode:forBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion copyActiveClientsUsingLocation];
-[CLLocationInternalClient_CoreMotion clearLocationAuthorizationForLoctoolWithBundleId:orBundlePath:];
-[CLLocationInternalClient_CoreMotion setAuthorizationStatus:withCorrectiveCompensation:forBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion copyGnssBandsInUse];
-[CLLocationInternalClient_CoreMotion getLocationServicesEnabled:];
-[CLLocationInternalClient_CoreMotion copyAuthorizationFromBundleID:toBundleID:];
-[CLLocationInternalClient_CoreMotion setTemporaryPreciseAuthorizationGranted:forBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion gyroCalibrationDatabaseSupportsMiniCalibration:];
-[CLLocationInternalClient_CoreMotion setTrackRunHint:];
-[CLLocationInternalClient_CoreMotion setRelevance:forInterestZoneWithId:registeredForBundleId:orBundlePath:error:];
-[CLLocationInternalClient_CoreMotion setLocationDefaultForKey:value:];
-[CLLocationInternalClient_CoreMotion copyActivityAlarms];
-[CLLocationInternalClient_CoreMotion copyInternalState];
-[CLLocationInternalClient_CoreMotion checkAndExerciseLearnedRoutesAuthorizationForBundleID:orBundlePath:replyBlock:];
-[CLLocationInternalClient_CoreMotion clearLocationAuthorizationForBundleId:orBundlePath:];
-[CLLocationInternalClient_CoreMotion getGyroCalibrationDatabaseNumTemperatures:];
-[CLLocationInternalClient_CoreMotion shouldDisplayEEDUI];
-[CLLocationInternalClient_CoreMotion getGestureServiceEnabled:];
-[CLLocationInternalClient_CoreMotion setPrivateMode:];
-[CLLocationInternalClient_CoreMotion deleteCurrentEmergencyLocationAsset];
-[CLLocationInternalClient_CoreMotion setLocationServicesEnabled:];
-[CLLocationInternalClient_CoreMotion getGyroCalibrationDatabaseBiasFit:atTemperature:];
-[CLLocationInternalClient_CoreMotion getArchivedAuthorizationDecisionsWithError:];
-[CLLocationInternalClient_CoreMotion deleteInterestZoneWithId:registeredForBundleId:orBundlePath:error:];
-[CLLocationInternalClient_CoreMotion connection];
-[CLLocationInternalClient_CoreMotion getMotionSensorLogs];
-[CLLocationInternalClient_CoreMotion disableGnssRestrictedMode];
-[CLLocationInternalClient_CoreMotion insertGyroCalibrationDatabaseBiasEstimateIfValid:temperature:variance:timestamp:];
-[CLLocationInternalClient_CoreMotion promoteSystemServiceWithBundlePath:];
-[CLLocationInternalClient_CoreMotion setPinnedLocationAuthorization:];
-[CLLocationInternalClient_CoreMotion triggerExpiredAuthorizationPurgeOnClientManager];
-[CLLocationInternalClient_CoreMotion setSupportedAuthorizationMask:forBundleID:orBundlePath:replyBlock:];
-[CLLocationInternalClient_CoreMotion getAccessoryPASCDTransmissionState];
-[CLLocationInternalClient_CoreMotion setBackgroundIndicatorForBundleID:orBundlePath:enabled:];
-[CLLocationInternalClient_CoreMotion copyLastLog];
-[CLLocationInternalClient_CoreMotion asynchronousRemoteObject];
-[CLLocationInternalClient_CoreMotion synchronousRemoteObject];
-[CLLocationInternalClient_CoreMotion getLocationDefaultForKey:];
-[CLLocationInternalClient_CoreMotion setIncidentalUseMode:forBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion isEligibleForAlwaysAuthorizationRequestForBundleID:orBundlePath:replyBlock:];
-[CLLocationInternalClient_CoreMotion copyAppsUsingLocation];
-[CLLocationInternalClient_CoreMotion getControlPlaneStatusReportClear:startTime:endTime:latitude:longitude:altitude:accuracy:vunc:status:];
-[CLLocationInternalClient_CoreMotion setLocationButtonUseMode:forBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion getLocationForBundleID:orBundlePath:dynamicAccuracyReductionEnabled:allowsAlteredAccessoryLocations:location:];
-[CLLocationInternalClient_CoreMotion performMigration];
-[CLLocationInternalClient_CoreMotion getTemporaryAuthorizationStatusForBundleId:orBundlePath:error:];
-[CLLocationInternalClient_CoreMotion getPipelinedCache];
-[CLLocationInternalClient_CoreMotion updatePromptedLatitude:longitude:];
-[CLLocationInternalClient_CoreMotion forceAuthSync:];
-[CLLocationInternalClient_CoreMotion setClientQuarantined:forBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion displayStatistics];
-[CLLocationInternalClient_CoreMotion getAuthorizationPromptMapDisplayEnabled:];
-[CLLocationInternalClient_CoreMotion setAuthorizationPromptMapDisplayEnabled:];
-[CLLocationInternalClient_CoreMotion getPrivateMode];
-[CLLocationInternalClient_CoreMotion timeZoneAtLocation:];
-[CLLocationInternalClient_CoreMotion copyZaxisStats];
-[CLLocationInternalClient_CoreMotion reportLocationUtilityEvent:atDate:];
-[CLLocationInternalClient_CoreMotion timeSyncMachTimeStamp:oscarTimeStamp:];
-[CLLocationInternalClient_CoreMotion getVisitHistoryAccessAllowedTime:forBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion getLearnedRoutesAccess:forBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion getVisitHistoryAccess:forBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion checkAndExercisePushClientAuthorizationForBundleID:replyBlock:];
-[CLLocationInternalClient_CoreMotion setStatusBarIconEnabled:forEntityClass:];
-[CLLocationInternalClient_CoreMotion setVisitHistoryAccess:forBundleID:orBundlePath:];
-[CLLocationInternalClient_CoreMotion getOdometryBatchedLocations];
-[CLLocationInternalClient_CoreMotion getStatusBarIconEnabled:forEntityClass:];
-[CLLocationInternalClient_CoreMotion registerPhenolicInterestZoneWithId:phenolicLocation:serviceMaskOperator:provenanceType:forBundleId:orBundlePath:error:];
-[CLLocationInternalClient_CoreMotion modifyOrSetAuthorizationTime:forBundleID:orBundlePath:];
```

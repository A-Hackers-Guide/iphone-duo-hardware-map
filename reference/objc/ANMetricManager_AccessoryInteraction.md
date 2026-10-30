# `ANMetricManager`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 52 instance methods, 8 class methods

## Instance variables

```
@"NSString" _lastLeashBreakAccessoryType;
d _systemWakeTime;
d _lastLeashBreak;
d _currLeashBreakAPWakeDelta;
d _visitTransitionTime;
d _lastLeashStateVisitStateForAccessoriesMetricsSubmission;
@"ANPlatform" _platform;
q _maintenanceSubmissionCount;
```

## Properties

```
@property (Tq,N,V_maintenanceSubmissionCount) maintenanceSubmissionCount;
@property (T@"NSString",&,V_lastLeashBreakAccessoryType) lastLeashBreakAccessoryType;
@property (Td,N,V_systemWakeTime) systemWakeTime;
@property (Td,N,V_lastLeashBreak) lastLeashBreak;
@property (Td,N,V_currLeashBreakAPWakeDelta) currLeashBreakAPWakeDelta;
@property (Td,N,V_visitTransitionTime) visitTransitionTime;
@property (Td,N,V_lastLeashStateVisitStateForAccessoriesMetricsSubmission) lastLeashStateVisitStateForAccessoriesMetricsSubmission;
@property (T@"ANPlatform",R,N,V_platform) platform;
```

## Class methods

```
+[ANMetricManager getBinForValue:fromBins:];
+[ANMetricManager loiTypeForSoundEventOnDevice:];
+[ANMetricManager submitConnectionAttemptEvent:numberBTConnectionAttempts:connectionReason:deviceType:];
+[ANMetricManager submitConnectionAttemptForDevice:withOutcome:];
+[ANMetricManager submitConnectionAttemptSuccessEvent:krMaterial:connectionReason:deviceType:];
+[ANMetricManager submitConnectionForDevice:withDuration:];
+[ANMetricManager submitFWUPCompletionMetricWithEventData:deviceUuid:serialNumber:productId:];
+[ANMetricManager submitKeyFetchEvent:numberMaterials:isDrift:deviceType:];
```

## Instance methods

```
-[ANMetricManager initWithPlatform:];
-[ANMetricManager submitMaintenanceMetrics:forDevice:withReason:andCategory:andDuration:leashable:];
-[ANMetricManager init];
-[ANMetricManager submitCarMaintConnectionMetrics:];
-[ANMetricManager platform];
-[ANMetricManager dealloc];
-[ANMetricManager submitMaintenanceTimerPowerLog:actualInterval:];
-[ANMetricManager setLastLeashBreakAccessoryType:];
-[ANMetricManager assembleCommonConnectionEventDataWithMetrics:forDevice:];
-[ANMetricManager currLeashBreakAPWakeDelta];
-[ANMetricManager encodeTransmitPower:];
-[ANMetricManager getTimeSinceLastLeashedWithVisitStateMetricsSubmission];
-[ANMetricManager lastLeashBreak];
-[ANMetricManager lastLeashBreakAccessoryType];
-[ANMetricManager lastLeashStateVisitStateForAccessoriesMetricsSubmission];
-[ANMetricManager maintenanceSubmissionCount];
-[ANMetricManager normalizeLeashedTimesToDay:withObservationDuration:];
-[ANMetricManager redactedSerialNumber:];
-[ANMetricManager redactedSerialNumberForDevice:];
-[ANMetricManager setCurrLeashBreakAPWakeDelta:];
-[ANMetricManager setLastLeashBreak:];
-[ANMetricManager setLastLeashStateVisitStateForAccessoriesMetricsSubmission:];
-[ANMetricManager setMaintenanceSubmissionCount:];
-[ANMetricManager setSystemWakeTime:];
-[ANMetricManager setVisitTransitionTime:];
-[ANMetricManager submitAccessoryObservationLocationRecencyAccuracyMetrics:withLocation:withHorizontalAccuracy:withRecency:inVisit:];
-[ANMetricManager submitBeaconLocationMetric:type:timestampAdjusted:forDevice:];
-[ANMetricManager submitCAConnectionMetrics:forDevice:];
-[ANMetricManager submitCAFirmwareUpdateMetrics:forDevice:];
-[ANMetricManager submitCAMaintenanceMetrics:];
-[ANMetricManager submitCarMaintMetrics:];
-[ANMetricManager submitConnectionMetrics:forDevice:];
-[ANMetricManager submitConnectionWatchdogMetricsWithLatency:timeConnected:accessoryTypeName:];
-[ANMetricManager submitCustomerNordicCrash:roseCrashes:firmwareVersion:device:];
-[ANMetricManager submitDailyTimeLeashedWithVisitStatePerAccessory:withTimeLeashedInside:withTimeLeashedOutside:seenDuringMetricsDuration:forAccessory:];
-[ANMetricManager submitDailyTimeTraveledPerAccessory:forAccessory:];
-[ANMetricManager submitFirmwareUpdateMetrics:forDevice:];
-[ANMetricManager submitFirmwareVersionsForOwnedTag:firmwareVersion:serialNumber:productId:];
-[ANMetricManager submitHardwareFaultsMetrics:serialNumber:isSharedWithUser:isMeDevice:firmwareVersion:];
-[ANMetricManager submitMaintenanceMetrics:];
-[ANMetricManager submitNonTimerMaintenanceMetricsForDevice:proactive:];
-[ANMetricManager submitPendingConnectionAttemptMetrics:attemptDuration:connectionReason:deviceType:];
-[ANMetricManager submitPowerLogConnectionMetrics:forDevice:];
-[ANMetricManager submitPowerLogEvent:data:];
-[ANMetricManager submitPowerLogMaintenanceMetrics:];
-[ANMetricManager submitSpeakerTamperingMetricsForDevice:];
-[ANMetricManager submitSystemWakeLeashBreakMetricsPerAccessoryAtLoi:forLeashBreak:];
-[ANMetricManager submitTaskMetricsForDevice:task:completed:error:];
-[ANMetricManager submitUnexpectedMissingBeaconMetrics:disconnected:];
-[ANMetricManager submitUserStats:payload:];
-[ANMetricManager systemWakeTime];
-[ANMetricManager visitTransitionTime];
```

# `ANAirTagDevice`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `ANDevice`
- 0 instance variables, 0 properties, 37 instance methods, 0 class methods

## Instance methods

```
-[ANAirTagDevice communicationProtocol];
-[ANAirTagDevice getRangingStatusForOpcode:data:];
-[ANAirTagDevice createConfigureNBRangingTaskOnDevice:withParams:];
-[ANAirTagDevice createConfigureRangingTaskWithMacAddress:countryCode:uwbChannel:acqPreamble:trackingPreamble:interval:];
-[ANAirTagDevice createDeinitRangingTask];
-[ANAirTagDevice createDumpLogsTaskOfType:];
-[ANAirTagDevice createFetchAccelerometerModeTask];
-[ANAirTagDevice createFetchAccelerometerOrientationModeTaskWithConfiguration];
-[ANAirTagDevice createFetchAccelerometerSlopeModeTaskWithConfiguration];
-[ANAirTagDevice createFetchBatteryStatusTask];
-[ANAirTagDevice createFetchFindingCapabilitiesTask];
-[ANAirTagDevice createFetchFirmwareVersionTaskWithCrashLogs:];
-[ANAirTagDevice createFetchUserStatsTaskWithPersistence:context:];
-[ANAirTagDevice createGetMultiStatusTask];
-[ANAirTagDevice createInduceCrashTask];
-[ANAirTagDevice createInitRangingTaskWithMacAddress:];
-[ANAirTagDevice createPlaySoundTaskWithSequence:];
-[ANAirTagDevice createPlayUnauthorizedSoundTaskWithSequence:];
-[ANAirTagDevice createRollWildKeyTask];
-[ANAirTagDevice createSetAccelerometerOrientationModeTaskWithConfiguration:];
-[ANAirTagDevice createSetAccelerometerSlopeModeTaskWithConfiguration:];
-[ANAirTagDevice createSetBatteryStatusTaskWithStatus:];
-[ANAirTagDevice createSetKeyRollTimeoutTaskWithInterval:];
-[ANAirTagDevice createSetMaxConnectionsTaskWithCount:];
-[ANAirTagDevice createSetNearOwnerTimeoutTaskInSeconds:];
-[ANAirTagDevice createSetObfuscatedIdentifierTaskWithIdentifier:];
-[ANAirTagDevice createSetPersistentConnectionTaskWithState:];
-[ANAirTagDevice createSetTagTypeTaskWithType:];
-[ANAirTagDevice createSetUnauthorizedPlaySoundRateLimitTask:];
-[ANAirTagDevice createSetWildModeTaskWithConfiguration:];
-[ANAirTagDevice createStartNBRangingTaskWithIRK:fragmentCount:];
-[ANAirTagDevice createStartRangingTaskWithTargetEventCounter:];
-[ANAirTagDevice createStopPlayingSoundTask];
-[ANAirTagDevice createStopRangingTask];
-[ANAirTagDevice createUnpairDeviceTask];
-[ANAirTagDevice getMultiStatusFromData:];
-[ANAirTagDevice getRangeEndReasonForOpcode:data:];
```

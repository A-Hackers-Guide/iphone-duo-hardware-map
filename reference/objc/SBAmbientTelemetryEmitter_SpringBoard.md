# `SBAmbientTelemetryEmitter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 17 instance methods, 19 class methods

## Instance variables

```
@"PRSPosterConfiguration" _activePosterConfiguration;
@"AMAmbientDefaults" _ambientDefaults;
@"NSDate" _ambientPresentationTimestamp;
@"NSDate" _ambientActiveFaceTimestamp;
@"NSDate" _ambientActiveFaceSceenOffTimestamp;
@"NSTimer" _ambientEnabledDailyTimer;
@"NSUUID" _sessionId;
```

## Class methods

```
+[SBAmbientTelemetryEmitter _ambientCoreAnalyticsSystemEventForBumpIgnored:sessionIdString:];
+[SBAmbientTelemetryEmitter _ambientActiveFaceTypeForConfiguration:];
+[SBAmbientTelemetryEmitter _ambientClockFaceDescriptorForConfiguration:];
+[SBAmbientTelemetryEmitter _ambientCoreAnalyticsActiveFaceDescription:duration:sessionIdString:];
+[SBAmbientTelemetryEmitter _ambientCoreAnalyticsActiveFaceDescription:screenOffDuration:sessionIdString:];
+[SBAmbientTelemetryEmitter _ambientCoreAnalyticsAmbientEnabled:userTriggered:];
+[SBAmbientTelemetryEmitter _ambientCoreAnalyticsConfigurationUpdateForEventType:activeFace:metadata:sessionIdString:timeOfDay:];
+[SBAmbientTelemetryEmitter _ambientCoreAnalyticsSystemEventForSleepSuppressionActive:sessionIdString:];
+[SBAmbientTelemetryEmitter _ambientCoreAnalyticsTotalAmbientDuration:sessionIdString:];
+[SBAmbientTelemetryEmitter _ambientCoreAnalyticsUserSettingsForAmbientDefaults:userTriggered:];
+[SBAmbientTelemetryEmitter _ambientPhotosFaceDescriptorForConfiguration:];
+[SBAmbientTelemetryEmitter _ambientPowerLogActiveFaceUpdateWithFaceType:activeFaceDescriptor:];
+[SBAmbientTelemetryEmitter _ambientPowerLogAmbientModeEnabled:];
+[SBAmbientTelemetryEmitter _ambientPowerLogAmbientMotionToWakeEnabled:];
+[SBAmbientTelemetryEmitter _ambientPowerLogAmbientPresented:displayStyle:];
+[SBAmbientTelemetryEmitter _ambientPowerLogLifetimePresentationCounterUpdate:];
+[SBAmbientTelemetryEmitter _ambientPowerLogWithEventName:dictionary:];
+[SBAmbientTelemetryEmitter _ambientTimeOfDay];
+[SBAmbientTelemetryEmitter _faceDescriptionFromConfiguration:];
```

## Instance methods

```
-[SBAmbientTelemetryEmitter dealloc];
-[SBAmbientTelemetryEmitter _updateTotalDurationLoggingForAmbientPresented:sessionIdString:];
-[SBAmbientTelemetryEmitter _logAmbientEnabled:userTriggered:];
-[SBAmbientTelemetryEmitter _logAmbientUserSettingsUserTriggered:];
-[SBAmbientTelemetryEmitter _setupAmbientEnabledDailyTimerForLogging];
-[SBAmbientTelemetryEmitter _setupAmbientEnabledLogging];
-[SBAmbientTelemetryEmitter _setupUserSettingUpdateLogging];
-[SBAmbientTelemetryEmitter _updateActiveFaceDurationForPreviousConfiguration:currentConfiguration:sessionIdString:];
-[SBAmbientTelemetryEmitter _updateActiveFaceScreenOffForBacklightState:forConfiguration:sessionIdString:];
-[SBAmbientTelemetryEmitter _updateSessionIdForAmbientPresented:];
-[SBAmbientTelemetryEmitter initWithAmbientDefaults:];
-[SBAmbientTelemetryEmitter logTelemetryForAmbientConfigurationUpdate:metadata:];
-[SBAmbientTelemetryEmitter logTelemetryForAmbientPresented:displayStyle:];
-[SBAmbientTelemetryEmitter logTelemetryForAmbientPresented:withBacklightState:screenOffWithConfiguration:];
-[SBAmbientTelemetryEmitter logTelemetryForBumpEventIgnored:];
-[SBAmbientTelemetryEmitter logTelemetryForMotionToWakeEnabled:];
-[SBAmbientTelemetryEmitter logTelemetryForSleepSuppressionActive:];
```

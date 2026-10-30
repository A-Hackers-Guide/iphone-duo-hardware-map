# `ANSettings`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 20 properties, 35 instance methods, 24 class methods

## Instance variables

```
@"<ANSettingsAccessorProtocol>" _accessor;
@"ANPlatform" _platform;
@"<ANSystemUtilsProtocol>" _systemUtils;
```

## Properties

```
@property (T@"NSDictionary",R) settingsDictionary;
@property (TB,R) testOnLaunch;
@property (TB,R) runningFindMyCertificationAssistant;
@property (TB,R) longHeldConnectionNotificationEnable;
@property (Ti,R) longHeldConnectionTimeThresholdOverride;
@property (T@"NSDate",R) longHeldConnectionLastNotificationTimestamp;
@property (Td,R) longHeldConnectionNotificationThreshold;
@property (T@"NSData",R) multiStatusResponseOverride;
@property (T@"NSData",R) hardwareFaultStatusResponseOverride;
@property (T@"NSString",R) coreAnalyticsSalt90Day;
@property (Ti,R) maintenanceIntervalOverride;
@property (T@"NSString",R) testMode;
@property (Ti,R) hawkeyeTestMode;
@property (T@"NSString",R) staticMACAddr;
@property (T@"NSString",R) staticLTK;
@property (TB,R) migrationDependencyControllerTestOnLaunch;
@property (Ti,R) maxPeripheralCountForForcedHeleMaintenance;
@property (Td,R) lastFirmwareVersionForAllTagsSubmission;
@property (Ti,R) firmwareVersionForAllTagsMetricsBackOff;
@property (Td,R) lastTravelingWithAccessoriesMetricsSubmission;
```

## Class methods

```
+[ANSettings sharedInstance];
+[ANSettings forceEnablePosh];
+[ANSettings dataProtectionShadowModeEnabled];
+[ANSettings alignmentIntervalOverride];
+[ANSettings allowBeaconsChangedPopup];
+[ANSettings beaconsChangedPopupBackoff];
+[ANSettings connectionsWatchdogTimeoutOverride];
+[ANSettings crashAlertEnabled];
+[ANSettings dailyTimeTravelWithAccessoriesSubmissionCadence];
+[ANSettings debounceTimerOverride];
+[ANSettings estimatedLocationAtDateEnabled];
+[ANSettings forceDisReconnect];
+[ANSettings forceEnableLeash];
+[ANSettings forceExtendedRange];
+[ANSettings forceNonAppleConnections];
+[ANSettings initializeSharedInstanceWithPlatform:systemUtils:];
+[ANSettings lastKnownLocationEnabled];
+[ANSettings migrationDependencyControllerTestInput];
+[ANSettings nearOwnerTimeoutOverride];
+[ANSettings setMaxConnectionsOverride];
+[ANSettings stressConfig];
+[ANSettings uarpAssetLocationType];
+[ANSettings uarpPacketCaptureEnabled];
+[ANSettings useDataProtectionMonitor];
```

## Instance methods

```
-[ANSettings dataForKey:defaultValue:];
-[ANSettings testMode];
-[ANSettings boolForKey:defaultValue:];
-[ANSettings dealloc];
-[ANSettings intForKey:defaultValue:];
-[ANSettings doubleForKey:defaultValue:];
-[ANSettings stringForKey:defaultValue:];
-[ANSettings setObject:forKey:];
-[ANSettings settingsDictionary];
-[ANSettings numberForKey:defaultValue:];
-[ANSettings hawkeyeTestMode];
-[ANSettings coreAnalyticsSalt90Day];
-[ANSettings firmwareVersionForAllTagsMetricsBackOff];
-[ANSettings hardwareFaultStatusResponseOverride];
-[ANSettings initWithAccessor:platform:systemUtils:];
-[ANSettings lastFirmwareVersionForAllTagsSubmission];
-[ANSettings lastTravelingWithAccessoriesMetricsSubmission];
-[ANSettings longHeldConnectionLastNotificationTimestamp];
-[ANSettings longHeldConnectionNotificationEnable];
-[ANSettings longHeldConnectionNotificationThreshold];
-[ANSettings longHeldConnectionTimeThresholdOverride];
-[ANSettings maintenanceIntervalOverride];
-[ANSettings maxPeripheralCountForForcedHeleMaintenance];
-[ANSettings migrationDependencyControllerTestOnLaunch];
-[ANSettings multiStatusResponseOverride];
-[ANSettings objectForKey:defaultValue:nilOrTypeOfClass:];
-[ANSettings runTestMode];
-[ANSettings runningFindMyCertificationAssistant];
-[ANSettings setCoreAnalyticsSalt90Day:];
-[ANSettings setLastFirmwareVersionForAllTagsSubmission:];
-[ANSettings setLongHeldConnectionLastNotificationTimestamp:];
-[ANSettings setTravelingWithAccessoriesMetricsSubmission:];
-[ANSettings staticLTK];
-[ANSettings staticMACAddr];
-[ANSettings testOnLaunch];
```

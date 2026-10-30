# `AAServicesXPCDaemonInterface` (protocol)

- Image: [`/System/Library/PrivateFrameworks/AudioAccessoryServices.framework/AudioAccessoryServices`](../userland/System__Library__PrivateFrameworks__AudioAccessoryServices.framework__AudioAccessoryServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- 0 instance variables, 0 properties, 49 instance methods, 0 class methods

## Instance methods

```
-[AAServicesXPCDaemonInterface setMuteAction:auditToken:bundleIdentifier:];
-[AAServicesXPCDaemonInterface forceLaunchProxCard:completion:];
-[AAServicesXPCDaemonInterface deviceManagerUpdate:completion:];
-[AAServicesXPCDaemonInterface activateAppleCareAccessoryControl:completion:];
-[AAServicesXPCDaemonInterface activeHRMSessionChanged:hrmState:completion:];
-[AAServicesXPCDaemonInterface areHeadphonesNearbyAndEligibleToPlay:completion:];
-[AAServicesXPCDaemonInterface assetManagerShowDownloadNotificationForBTAddress:completionHandler:];
-[AAServicesXPCDaemonInterface audioRoutingControlActivate:completion:];
-[AAServicesXPCDaemonInterface audioSessionControlActivate:completion:];
-[AAServicesXPCDaemonInterface audioSessionControlUpdate:];
-[AAServicesXPCDaemonInterface deviceManagerActivate:completion:];
-[AAServicesXPCDaemonInterface deviceManagerFetchAADeviceBatteryInfoForAddress:deviceHandler:];
-[AAServicesXPCDaemonInterface deviceManagerFetchAADeviceBatteryInfoForIdentifier:deviceHandler:];
-[AAServicesXPCDaemonInterface deviceManagerFetchAccessoryFeatureFlagConfiguration:];
-[AAServicesXPCDaemonInterface deviceManagerFetchAudioAccessoryDeviceForBTAddress:deviceHandler:];
-[AAServicesXPCDaemonInterface deviceManagerFetchAudioAccessoryDeviceForIdentifier:deviceHandler:];
-[AAServicesXPCDaemonInterface deviceManagerFetchPairedAudioAccessoryDevices:];
-[AAServicesXPCDaemonInterface deviceManagerSendDeviceConfig:identifier:completion:];
-[AAServicesXPCDaemonInterface getConversationAwarenessStateForDeviceAddress:btAddress:completion:];
-[AAServicesXPCDaemonInterface getSleepStateForDeviceAddress:btAddress:completion:];
-[AAServicesXPCDaemonInterface headphoneActivityProviderActivate:completion:];
-[AAServicesXPCDaemonInterface headphoneActivityProviderGetActivityFlagStateForDeviceAddress:completion:];
-[AAServicesXPCDaemonInterface headphoneActivityProviderGetDetailedCASignalStateForDeviceAddress:completion:];
-[AAServicesXPCDaemonInterface informDRClientSensorDataAvailable:dataTypes:completion:];
-[AAServicesXPCDaemonInterface informDRClientSensorDataUnavailable:dataTypes:completion:];
-[AAServicesXPCDaemonInterface injectActivityFlagToDevice:forDeviceAddress:];
-[AAServicesXPCDaemonInterface injectActivityFlagToDevice:forDeviceAddress:completion:];
-[AAServicesXPCDaemonInterface injectTestActivityFlag:forDeviceAddress:];
-[AAServicesXPCDaemonInterface injectTestActivityFlag:forDeviceAddress:completion:];
-[AAServicesXPCDaemonInterface injectTestSignal:forDeviceAddress:];
-[AAServicesXPCDaemonInterface injectTestSignal:forDeviceAddress:completion:];
-[AAServicesXPCDaemonInterface isTemporaryPairingConnectionAllowed:];
-[AAServicesXPCDaemonInterface launchProxCard:completion:];
-[AAServicesXPCDaemonInterface prewarmAudioAccessoriesForFitnessWorkout:];
-[AAServicesXPCDaemonInterface proxCardUserActionOnHeadphone:btAddress:withAction:completion:];
-[AAServicesXPCDaemonInterface sendAppleCareAccessoryConfiguration:btAddress:control:completion:];
-[AAServicesXPCDaemonInterface sensorServiceActivate:completion:];
-[AAServicesXPCDaemonInterface sensorServiceSendPTEvent:value:completion:];
-[AAServicesXPCDaemonInterface set3PDeviceInEarState:inEarStatePrimary:inEarStateSecondary:];
-[AAServicesXPCDaemonInterface set3PDeviceProperty:property:value:];
-[AAServicesXPCDaemonInterface setHijackBlockingMode:mode:completion:];
-[AAServicesXPCDaemonInterface subscribeActivityFlagState];
-[AAServicesXPCDaemonInterface subscribeDetailedCASignalState];
-[AAServicesXPCDaemonInterface systemStateMonitorActivate:completion:];
-[AAServicesXPCDaemonInterface systemStateMonitorFetchHealthKitDataWriteAllowedForDevice:completionHandler:];
-[AAServicesXPCDaemonInterface systemStateMonitorFetchPairedHRMDevices:];
-[AAServicesXPCDaemonInterface systemStateMonitorReportActiveHRMDeviceChanged:withSREnabled:];
-[AAServicesXPCDaemonInterface systemStateMonitorReportSiriHijackEligibilityChanged:];
-[AAServicesXPCDaemonInterface systemStateMonitorShowFitEducationNotificationForIdentifier:completionHandler:];
```

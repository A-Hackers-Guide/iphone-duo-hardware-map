# `PLConfigAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- 9 instance variables, 9 properties, 74 instance methods, 21 class methods

## Instance variables

```
@"PLCFNotificationOperatorComposition" _notificationKeyboardClicks;
@"PLCFNotificationOperatorComposition" _notificationKeyboardHaptics;
@"PLXPCListenerOperatorComposition" _continuityCameraNotification;
@"PLXPCListenerOperatorComposition" _ambientModeListener;
@"PLXPCListenerOperatorComposition" _buddyDataListener;
@"PLCFNotificationOperatorComposition" _consoleModeListener;
@"PLIOKitOperatorComposition" _iokitExpertDevice;
@"PLCFNotificationOperatorComposition" _sysdiagnoseStartListener;
@"PLCFNotificationOperatorComposition" _sysdiagnoseStopListener;
```

## Properties

```
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationKeyboardClicks) notificationKeyboardClicks;
@property (T@"PLCFNotificationOperatorComposition",R,V_notificationKeyboardHaptics) notificationKeyboardHaptics;
@property (T@"PLXPCListenerOperatorComposition",R,V_continuityCameraNotification) continuityCameraNotification;
@property (T@"PLXPCListenerOperatorComposition",R,V_ambientModeListener) ambientModeListener;
@property (T@"PLXPCListenerOperatorComposition",R,V_buddyDataListener) buddyDataListener;
@property (T@"PLCFNotificationOperatorComposition",&,V_consoleModeListener) consoleModeListener;
@property (T@"PLIOKitOperatorComposition",R,V_iokitExpertDevice) iokitExpertDevice;
@property (T@"PLCFNotificationOperatorComposition",&,V_sysdiagnoseStartListener) sysdiagnoseStartListener;
@property (T@"PLCFNotificationOperatorComposition",&,V_sysdiagnoseStopListener) sysdiagnoseStopListener;
```

## Class methods

```
+[PLConfigAgent entryEventPointDefinitions];
+[PLConfigAgent entryEventForwardDefinitions];
+[PLConfigAgent entryEventBackwardDefinitions];
+[PLConfigAgent entryEventNoneDefinitions];
+[PLConfigAgent load];
+[PLConfigAgent defaults];
+[PLConfigAgent entryEventForwardDefinitionFeatureFlag];
+[PLConfigAgent entryEventNoneDefinitionConfig];
+[PLConfigAgent getOSVersionNumber];
+[PLConfigAgent accountingGroupDefinitions];
+[PLConfigAgent railDefinitions];
+[PLConfigAgent entryEventForwardDefinitionAmbientMode];
+[PLConfigAgent entryEventForwardDefintionRinger];
+[PLConfigAgent resetRAPIDTaskingConfig];
+[PLConfigAgent getVersionDirectory:];
+[PLConfigAgent entryEventForwardDefinitionContinuityCamera];
+[PLConfigAgent entryEventNoneDefinitionAdapterInformation];
+[PLConfigAgent entryEventNoneDefinitionPairedDeviceConfig];
+[PLConfigAgent entryEventForwardDefinitionKeyboardClicks];
+[PLConfigAgent entryEventForwardDefinitionKeyboardHaptics];
+[PLConfigAgent removeFilesFromPath:withMaxFiles:];
```

## Instance methods

```
-[PLConfigAgent logEventForwardSysdiagnoseEvent:];
-[PLConfigAgent logDeviceCapability];
-[PLConfigAgent seedGroup];
-[PLConfigAgent ambientModeListener];
-[PLConfigAgent setConsoleModeListener:];
-[PLConfigAgent setSysdiagnoseStartListener:];
-[PLConfigAgent logLastBackupTime];
-[PLConfigAgent init];
-[PLConfigAgent logToPPSBuild:atDate:];
-[PLConfigAgent logUserspaceReboot];
-[PLConfigAgent logInstallType:];
-[PLConfigAgent logAndUpdateLastBuild:];
-[PLConfigAgent autolockTime];
-[PLConfigAgent logEventPointFeatureFlags:];
-[PLConfigAgent continuityCameraNotification];
-[PLConfigAgent dealloc];
-[PLConfigAgent initOperatorDependancies];
-[PLConfigAgent getMemorySize];
-[PLConfigAgent notificationKeyboardHaptics];
-[PLConfigAgent iokitExpertDevice];
-[PLConfigAgent logEventNoneBuddyData:];
-[PLConfigAgent logEventForwardAmbientModeEnabled:];
-[PLConfigAgent getDeviceType];
-[PLConfigAgent hwConfig];
-[PLConfigAgent logIcloudAccountType];
-[PLConfigAgent baseband];
-[PLConfigAgent getCoverGlass];
-[PLConfigAgent getDeviceSerialNumber];
-[PLConfigAgent logSystemReboot];
-[PLConfigAgent copyPowerlogsForPreUpgradeOSVersion:];
-[PLConfigAgent logConfigEntryToCA:];
-[PLConfigAgent logLastUpgradeSystemTimestamp];
-[PLConfigAgent sysdiagnoseStartListener];
-[PLConfigAgent rootInstalled];
-[PLConfigAgent getOSVariant];
-[PLConfigAgent logEventNonePairedDeviceConfig];
-[PLConfigAgent sysdiagnoseStopListener];
-[PLConfigAgent getShutdownBootReason:];
-[PLConfigAgent fileSizeSafeguards];
-[PLConfigAgent volumeFreespace:];
-[PLConfigAgent logAndUpdateLastUpgradeTime:];
-[PLConfigAgent notificationKeyboardClicks];
-[PLConfigAgent disableCABlanking];
-[PLConfigAgent deviceShutdownReasons];
-[PLConfigAgent logDeviceDiskSize];
-[PLConfigAgent logEventForwardRingerState];
-[PLConfigAgent checkAndUpdateOSVersion:];
-[PLConfigAgent logCPUCoreConfig];
-[PLConfigAgent logEventForwardContinuityCamera:];
-[PLConfigAgent logEventForwardConsoleMode];
-[PLConfigAgent logEventForwardKeyboardHaptics];
-[PLConfigAgent logConfigEntry:];
-[PLConfigAgent getMDMStatus];
-[PLConfigAgent logConfigToBGSQL:];
-[PLConfigAgent buddyDataListener];
-[PLConfigAgent cleanupOldPowerlogs];
-[PLConfigAgent getEnclosureMaterial];
-[PLConfigAgent hasEmbeddedSIM];
-[PLConfigAgent setSysdiagnoseStopListener:];
-[PLConfigAgent log];
-[PLConfigAgent consoleModeListener];
-[PLConfigAgent pairStatusDidChange:];
-[PLConfigAgent logEventNoneConfig];
-[PLConfigAgent logEntryToCA:];
-[PLConfigAgent noWatchdogs];
-[PLConfigAgent bootArgs];
-[PLConfigAgent hwBoardRevision];
-[PLConfigAgent deviceName];
-[PLConfigAgent getUpgradeType];
-[PLConfigAgent maintainPreUpgradePowerlogs:];
-[PLConfigAgent getPerfLevelsCount];
-[PLConfigAgent getSplatVersionString];
-[PLConfigAgent logEventForwardKeyboardClicks];
-[PLConfigAgent getCoreCount:];
```

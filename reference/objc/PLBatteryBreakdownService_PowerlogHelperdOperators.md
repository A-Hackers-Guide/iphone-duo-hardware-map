# `PLBatteryBreakdownService`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLService`
- 17 instance variables, 17 properties, 91 instance methods, 9 class methods

## Instance variables

```
B _showGizmoQualifier;
B _hasHomeKitActivity;
@"NSSet" _rootNodeNames;
@"NSSet" _nonAppNames;
@"NSSet" _intermediateRootNodes;
@"NSSet" _deletedAppNames;
@"NSSet" _deletedAppClipNames;
@"NSSet" _webAppNames;
@"NSDictionary" _nodeIDToNodeName;
@"NSDictionary" _installedBundleIDToDisplayName;
@"NSDictionary" _installedPluginBundleIDToPluginEntry;
@"NSDictionary" _gizmoDaemonToAppBundleID;
@"NSDictionary" _gizmoIDSTopicToAppBundleID;
@"NSDictionary" _rootNodeNameToRootNodeEnergyKey;
@"NSDictionary" _givenNameToMappedName;
d _totalEnergyDay;
d _totalEnergyWeek;
```

## Properties

```
@property (T@"NSSet",&,N,V_rootNodeNames) rootNodeNames;
@property (T@"NSSet",&,N,V_nonAppNames) nonAppNames;
@property (T@"NSSet",&,N,V_intermediateRootNodes) intermediateRootNodes;
@property (T@"NSSet",&,N,V_deletedAppNames) deletedAppNames;
@property (T@"NSSet",&,N,V_deletedAppClipNames) deletedAppClipNames;
@property (T@"NSSet",&,N,V_webAppNames) webAppNames;
@property (T@"NSDictionary",&,N,V_nodeIDToNodeName) nodeIDToNodeName;
@property (T@"NSDictionary",&,N,V_installedBundleIDToDisplayName) installedBundleIDToDisplayName;
@property (T@"NSDictionary",&,N,V_installedPluginBundleIDToPluginEntry) installedPluginBundleIDToPluginEntry;
@property (T@"NSDictionary",&,N,V_gizmoDaemonToAppBundleID) gizmoDaemonToAppBundleID;
@property (T@"NSDictionary",&,N,V_gizmoIDSTopicToAppBundleID) gizmoIDSTopicToAppBundleID;
@property (T@"NSDictionary",&,N,V_rootNodeNameToRootNodeEnergyKey) rootNodeNameToRootNodeEnergyKey;
@property (T@"NSDictionary",&,N,V_givenNameToMappedName) givenNameToMappedName;
@property (TB,V_showGizmoQualifier) showGizmoQualifier;
@property (Td,V_totalEnergyDay) totalEnergyDay;
@property (Td,V_totalEnergyWeek) totalEnergyWeek;
@property (TB,V_hasHomeKitActivity) hasHomeKitActivity;
```

## Class methods

```
+[PLBatteryBreakdownService load];
+[PLBatteryBreakdownService defaults];
+[PLBatteryBreakdownService installedPlugins];
+[PLBatteryBreakdownService appNameForBundleID:];
+[PLBatteryBreakdownService canSetQualifier:forBundleID:];
+[PLBatteryBreakdownService combineQualifiers:];
+[PLBatteryBreakdownService pluginEntryFromRecord:];
+[PLBatteryBreakdownService rootNodeQualificationNameWithQualificationName:withRootNodeName:];
+[PLBatteryBreakdownService whereValidName];
```

## Instance methods

```
-[PLBatteryBreakdownService isBackgroundRefreshEnabled:];
-[PLBatteryBreakdownService clearState];
-[PLBatteryBreakdownService appTypeForName:];
-[PLBatteryBreakdownService computeTotalBackgroundDuration:];
-[PLBatteryBreakdownService deletedAppNames];
-[PLBatteryBreakdownService rootNodeNameToRootNodeEnergyKey];
-[PLBatteryBreakdownService totalEnergyWeek];
-[PLBatteryBreakdownService computeTotalForegroundDuration:];
-[PLBatteryBreakdownService setNonAppNames:];
-[PLBatteryBreakdownService setWebAppNames:];
-[PLBatteryBreakdownService addForegroundAndBackgroundDurations:withRange:withQueryType:];
-[PLBatteryBreakdownService addNotificationValues:withRange:withQueryType:];
-[PLBatteryBreakdownService adjustBackgroundTimesWithEnergyEntries:];
-[PLBatteryBreakdownService adjustExtensionBackgroundTimeWithEnergyEntries:];
-[PLBatteryBreakdownService adjustFGBGTimeForNonAppEnergyEntry:];
-[PLBatteryBreakdownService adjustForegroundTimesWithEnergyEntries:];
-[PLBatteryBreakdownService applyDynamicNameTransformationsWithEnergyEntries:];
-[PLBatteryBreakdownService applyStaticNameTransformationsWithEnergyEntries:];
-[PLBatteryBreakdownService batteryBreakdownWithTimeRange:withDataRange:withEntryTimeInterval:withQueryType:];
-[PLBatteryBreakdownService batteryBreakdownWithTimeRange:withDataRange:withEntryTimeInterval:withQueryType:withTotalSumEnergyRatioCutOff:];
-[PLBatteryBreakdownService bundleIDsForMappedName:];
-[PLBatteryBreakdownService checkHomeKitEvents];
-[PLBatteryBreakdownService combineDuplicatesWithEnergyEntries:];
-[PLBatteryBreakdownService deletedAppClipNames];
-[PLBatteryBreakdownService determineDisplayNamesWithEnergyEntries:];
-[PLBatteryBreakdownService energyEntriesWithRange:withEntryTimeInterval:withQueryType:];
-[PLBatteryBreakdownService energyMetricBucketForRootNodeID:];
-[PLBatteryBreakdownService filterEnergyEntriesBasedOnTime:withQueryType:];
-[PLBatteryBreakdownService filterWithEnergyEntries:withQueryType:];
-[PLBatteryBreakdownService getLastUpgradeTimestamp];
-[PLBatteryBreakdownService getUpgradeDataWithLastUpgradeTimestamp:withFirstEntryTimestampFromDB:withNow:withBeforeUpgrade:withRange:];
-[PLBatteryBreakdownService getUsageDataWithStartTime:withMidTime:withEndTime:];
-[PLBatteryBreakdownService getfirstEntryTimestampFromDb];
-[PLBatteryBreakdownService givenNameToMappedName];
-[PLBatteryBreakdownService gizmoDaemonToAppBundleID];
-[PLBatteryBreakdownService gizmoIDSTopicToAppBundleID];
-[PLBatteryBreakdownService hasHomeKitActivity];
-[PLBatteryBreakdownService inDemoMode];
-[PLBatteryBreakdownService installedBundleIDToDisplayName];
-[PLBatteryBreakdownService installedPluginBundleIDToPluginEntry];
-[PLBatteryBreakdownService intermediateRootNodes];
-[PLBatteryBreakdownService isBackgroundLocationUsageAlwaysEnabled:withLocationDict:];
-[PLBatteryBreakdownService isForegroundOnlyBucket:];
-[PLBatteryBreakdownService mapCloudDocsToAppsWithEnergyEntries:];
-[PLBatteryBreakdownService mapDeletedAppsWithEnergyEntries:];
-[PLBatteryBreakdownService mapGizmoToAppsWithEnergyEntries:];
-[PLBatteryBreakdownService mapPluginsToAppsWithEnergyEntries:];
-[PLBatteryBreakdownService minimumRequiredQueryTypeForAppType:];
-[PLBatteryBreakdownService nodeIDToNodeName];
-[PLBatteryBreakdownService nonAppNames];
-[PLBatteryBreakdownService nonAppRuntimeWithEventForwardTableName:withRange:andIdentificationKey:];
-[PLBatteryBreakdownService nonAppsRuntimesWithRange:];
-[PLBatteryBreakdownService nonNullValue:withKey:];
-[PLBatteryBreakdownService pluginBundleIDsforBundleID:];
-[PLBatteryBreakdownService populateBLDKeysWithEnergyEntries:];
-[PLBatteryBreakdownService populateEnergyBucketKeysWithEntries:];
-[PLBatteryBreakdownService populateRootNodeEnergyKeysWithEnergyEntries:];
-[PLBatteryBreakdownService qualifiersWithEnergyEntry:bucketSize:andTotalEnergy:];
-[PLBatteryBreakdownService reaccountBackupRestoreWithEnergyEntries:];
-[PLBatteryBreakdownService reaccountExchangeEntriesWithEnergyEntries:];
-[PLBatteryBreakdownService removeNodesNotToShowInInternalUI:withQueryType:];
-[PLBatteryBreakdownService rootNodeNames];
-[PLBatteryBreakdownService setDeletedAppClipNames:];
-[PLBatteryBreakdownService setDeletedAppNames:];
-[PLBatteryBreakdownService setGivenNameToMappedName:];
-[PLBatteryBreakdownService setGizmoDaemonToAppBundleID:];
-[PLBatteryBreakdownService setGizmoIDSTopicToAppBundleID:];
-[PLBatteryBreakdownService setHasHomeKitActivity:];
-[PLBatteryBreakdownService setInstalledBundleIDToDisplayName:];
-[PLBatteryBreakdownService setInstalledPluginBundleIDToPluginEntry:];
-[PLBatteryBreakdownService setIntermediateRootNodes:];
-[PLBatteryBreakdownService setNodeIDToNodeName:];
-[PLBatteryBreakdownService setRootNodeNameToRootNodeEnergyKey:];
-[PLBatteryBreakdownService setRootNodeNames:];
-[PLBatteryBreakdownService setShowGizmoQualifier:];
-[PLBatteryBreakdownService setTotalEnergyDay:];
-[PLBatteryBreakdownService setTotalEnergyWeek:];
-[PLBatteryBreakdownService shouldShowBatteryBreakdownWithTotalSumEnergy:withtotalSumEnergyRatioCutOff:];
-[PLBatteryBreakdownService shouldShowUpgradeInsightWithQueryType:];
-[PLBatteryBreakdownService shouldSuggestAutoBrightnessWithEnergyEntries:andSavedEnergyPercent:];
-[PLBatteryBreakdownService shouldSuggestAutoLockWithEnergyEntries:andSavedEnergyPercent:];
-[PLBatteryBreakdownService shouldSuggestBackgroundCPUWithEnergyEntries:];
-[PLBatteryBreakdownService shouldSuggestBackgroundLocationWithEnergyEntries:];
-[PLBatteryBreakdownService shouldSuggestReduceBrightnessWithEnergyEntries:andSavedEnergyPercent:];
-[PLBatteryBreakdownService showGizmoQualifier];
-[PLBatteryBreakdownService showRootNodesInInternal];
-[PLBatteryBreakdownService suggestionsWithEnergyEntries:];
-[PLBatteryBreakdownService totalEnergyDay];
-[PLBatteryBreakdownService totalSumEnergyRatioCutOff];
-[PLBatteryBreakdownService wasGizmoConnectedInRange:];
-[PLBatteryBreakdownService webAppNames];
```

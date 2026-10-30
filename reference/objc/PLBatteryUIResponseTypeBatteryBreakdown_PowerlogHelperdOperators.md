# `PLBatteryUIResponseTypeBatteryBreakdown`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 32 instance variables, 36 properties, 162 instance methods, 1 class methods

## Instance variables

```
B _isDynamicEnd;
B _hasHomeKit;
B _gizmoConnected;
B _isSlopAdjustmentEnabled;
B _excludeTimeOnCharger;
s _percentageOption;
@"PLBatteryUIResponderService" _responderService;
@"NSMutableArray" _buckets;
@"NSDate" _start;
@"NSDate" _end;
@"NSDate" _monotonicNow;
d _bucketSize;
d _dynamicEndOffset;
@"NSSet" _rootNodeBundleIDs;
@"NSSet" _nonAppBundleIDs;
@"NSSet" _webAppBundleIDs;
@"NSSet" _deletedAppBundleIDs;
@"NSSet" _deletedAppClipBundleIDs;
@"NSSet" _exchangeBundleIDs;
@"NSDictionary" _nodeIDsToNodeNames;
@"NSDictionary" _bundleIDsToDisplayNames;
@"NSDictionary" _bundleIDsToReplacementBundleIDs;
@"NSDictionary" _bundleIDsToForegroundTimes;
@"NSDictionary" _bundleIDsToBackgroundTimes;
@"NSDictionary" _bundleIDsToEnergyKeyForSlopAdjustment;
@"NSDictionary" _pluginBundleIDsToEntries;
@"NSDictionary" _lastBatteryEntry;
@"NSSet" _intermediateRootNodes;
@"NSDictionary" _rootNodeIDToRootNodeEnergyKeys;
d _lastUpgradeTimestamp;
d _dataDuration;
@"NSArray" _uiLevelDrainEntries;
```

## Properties

```
@property (T@"NSMutableArray",&,V_buckets) buckets;
@property (T@"NSDate",&,V_start) start;
@property (T@"NSDate",&,V_end) end;
@property (T@"NSDate",&,V_monotonicNow) monotonicNow;
@property (Td,V_bucketSize) bucketSize;
@property (TB,V_isDynamicEnd) isDynamicEnd;
@property (Td,V_dynamicEndOffset) dynamicEndOffset;
@property (T@"NSSet",&,V_rootNodeBundleIDs) rootNodeBundleIDs;
@property (T@"NSSet",&,V_nonAppBundleIDs) nonAppBundleIDs;
@property (T@"NSSet",&,V_webAppBundleIDs) webAppBundleIDs;
@property (T@"NSSet",&,V_deletedAppBundleIDs) deletedAppBundleIDs;
@property (T@"NSSet",&,V_deletedAppClipBundleIDs) deletedAppClipBundleIDs;
@property (T@"NSSet",&,V_exchangeBundleIDs) exchangeBundleIDs;
@property (T@"NSDictionary",&,V_nodeIDsToNodeNames) nodeIDsToNodeNames;
@property (T@"NSDictionary",&,V_bundleIDsToDisplayNames) bundleIDsToDisplayNames;
@property (T@"NSDictionary",&,V_bundleIDsToReplacementBundleIDs) bundleIDsToReplacementBundleIDs;
@property (T@"NSDictionary",&,V_bundleIDsToForegroundTimes) bundleIDsToForegroundTimes;
@property (T@"NSDictionary",&,V_bundleIDsToBackgroundTimes) bundleIDsToBackgroundTimes;
@property (T@"NSDictionary",&,V_bundleIDsToEnergyKeyForSlopAdjustment) bundleIDsToEnergyKeyForSlopAdjustment;
@property (T@"NSDictionary",&,V_pluginBundleIDsToEntries) pluginBundleIDsToEntries;
@property (T@"NSDictionary",&,V_lastBatteryEntry) lastBatteryEntry;
@property (T@"NSSet",&,V_intermediateRootNodes) intermediateRootNodes;
@property (T@"NSDictionary",&,V_rootNodeIDToRootNodeEnergyKeys) rootNodeIDToRootNodeEnergyKeys;
@property (TB,V_hasHomeKit) hasHomeKit;
@property (TB,V_gizmoConnected) gizmoConnected;
@property (TB,V_isSlopAdjustmentEnabled) isSlopAdjustmentEnabled;
@property (Ts,V_percentageOption) percentageOption;
@property (TB,V_excludeTimeOnCharger) excludeTimeOnCharger;
@property (Td,V_lastUpgradeTimestamp) lastUpgradeTimestamp;
@property (Td,V_dataDuration) dataDuration;
@property (T@"NSArray",&,V_uiLevelDrainEntries) uiLevelDrainEntries;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLBatteryUIResponseTypeBatteryBreakdown flagZeroUISOCDrainEntryWithBucket:];
```

## Instance methods

```
-[PLBatteryUIResponseTypeBatteryBreakdown configure:];
-[PLBatteryUIResponseTypeBatteryBreakdown dependencies];
-[PLBatteryUIResponseTypeBatteryBreakdown buckets];
-[PLBatteryUIResponseTypeBatteryBreakdown start];
-[PLBatteryUIResponseTypeBatteryBreakdown end];
-[PLBatteryUIResponseTypeBatteryBreakdown coalesce];
-[PLBatteryUIResponseTypeBatteryBreakdown setEnd:];
-[PLBatteryUIResponseTypeBatteryBreakdown result];
-[PLBatteryUIResponseTypeBatteryBreakdown setStart:];
-[PLBatteryUIResponseTypeBatteryBreakdown setBuckets:];
-[PLBatteryUIResponseTypeBatteryBreakdown run];
-[PLBatteryUIResponseTypeBatteryBreakdown addQualifiers:];
-[PLBatteryUIResponseTypeBatteryBreakdown hasHomeKit];
-[PLBatteryUIResponseTypeBatteryBreakdown setHasHomeKit:];
-[PLBatteryUIResponseTypeBatteryBreakdown bucketSize];
-[PLBatteryUIResponseTypeBatteryBreakdown dataDuration];
-[PLBatteryUIResponseTypeBatteryBreakdown addTotalEnergy:];
-[PLBatteryUIResponseTypeBatteryBreakdown adjustRuntimes:];
-[PLBatteryUIResponseTypeBatteryBreakdown applyDisplayNameTransformation:];
-[PLBatteryUIResponseTypeBatteryBreakdown initBackgroundLocationAudioTime];
-[PLBatteryUIResponseTypeBatteryBreakdown nonAppBundleIDs];
-[PLBatteryUIResponseTypeBatteryBreakdown webAppBundleIDs];
-[PLBatteryUIResponseTypeBatteryBreakdown addTotals:with:];
-[PLBatteryUIResponseTypeBatteryBreakdown applyDynamicNameTransformation:];
-[PLBatteryUIResponseTypeBatteryBreakdown buildEnergyEntriesWithRootNodes:andQualificationNodes:andRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown bundleIDsToReplacementBundleIDs];
-[PLBatteryUIResponseTypeBatteryBreakdown addEntryTypes:];
-[PLBatteryUIResponseTypeBatteryBreakdown addErrorCode:];
-[PLBatteryUIResponseTypeBatteryBreakdown addFgEnergyForMetrics:qualificationID:rootNodeQualificationEnergy:energyEntry:];
-[PLBatteryUIResponseTypeBatteryBreakdown addRNEForMetrics:rootNodeEnergy:energyEntry:];
-[PLBatteryUIResponseTypeBatteryBreakdown addTotals:];
-[PLBatteryUIResponseTypeBatteryBreakdown adjustEnergyValues:];
-[PLBatteryUIResponseTypeBatteryBreakdown adjustExtensionBackgroundTimeWithEnergyEntries:];
-[PLBatteryUIResponseTypeBatteryBreakdown applySlopAdjustment:];
-[PLBatteryUIResponseTypeBatteryBreakdown applyStaticNameTransformation:];
-[PLBatteryUIResponseTypeBatteryBreakdown bgLocationAudioTimeApps:];
-[PLBatteryUIResponseTypeBatteryBreakdown bgLocationAudioTimeRuntimes:bundleID:];
-[PLBatteryUIResponseTypeBatteryBreakdown buildBucketWithEnergyEntries:andRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown buildBucketsForRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown buildUtilityCache];
-[PLBatteryUIResponseTypeBatteryBreakdown bundleIDsToBackgroundTimes];
-[PLBatteryUIResponseTypeBatteryBreakdown bundleIDsToDisplayNames];
-[PLBatteryUIResponseTypeBatteryBreakdown bundleIDsToEnergyKeyForSlopAdjustment];
-[PLBatteryUIResponseTypeBatteryBreakdown bundleIDsToForegroundTimes];
-[PLBatteryUIResponseTypeBatteryBreakdown canSetQualifier:forBundleID:];
-[PLBatteryUIResponseTypeBatteryBreakdown cleanEntries:];
-[PLBatteryUIResponseTypeBatteryBreakdown collapseEnergyEntries:];
-[PLBatteryUIResponseTypeBatteryBreakdown combineQualifiers:];
-[PLBatteryUIResponseTypeBatteryBreakdown computeNumberOfBuckets];
-[PLBatteryUIResponseTypeBatteryBreakdown createPerAppBreakdown:];
-[PLBatteryUIResponseTypeBatteryBreakdown deletedAppBundleIDs];
-[PLBatteryUIResponseTypeBatteryBreakdown deletedAppClipBundleIDs];
-[PLBatteryUIResponseTypeBatteryBreakdown dynamicEndOffset];
-[PLBatteryUIResponseTypeBatteryBreakdown enumerateBucketsUsingBlock:];
-[PLBatteryUIResponseTypeBatteryBreakdown exchangeBundleIDs];
-[PLBatteryUIResponseTypeBatteryBreakdown excludeTimeOnCharger];
-[PLBatteryUIResponseTypeBatteryBreakdown filterEnergyEntries:];
-[PLBatteryUIResponseTypeBatteryBreakdown filterEnergyEntriesWithRuntimes:];
-[PLBatteryUIResponseTypeBatteryBreakdown filterFgBg:filterArray:];
-[PLBatteryUIResponseTypeBatteryBreakdown generateRange:withDataRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown getAppRuntimesInRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown getBatteryMaximumCapacityPercentWithError:];
-[PLBatteryUIResponseTypeBatteryBreakdown getBundleIDToBackgroundTimeMap];
-[PLBatteryUIResponseTypeBatteryBreakdown getBundleIDToDisplayNameMap];
-[PLBatteryUIResponseTypeBatteryBreakdown getBundleIDToForegroundTimeMap];
-[PLBatteryUIResponseTypeBatteryBreakdown getBundleIDToReplacementBundleIDMap];
-[PLBatteryUIResponseTypeBatteryBreakdown getBundleIDsToEnergyKeyForSlopAdjustmentMap];
-[PLBatteryUIResponseTypeBatteryBreakdown getDataDurationFromRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown getDataRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown getDeletedAppBundleIDs];
-[PLBatteryUIResponseTypeBatteryBreakdown getDeletedAppClipBundleIDs];
-[PLBatteryUIResponseTypeBatteryBreakdown getDrainPerBucketIn:];
-[PLBatteryUIResponseTypeBatteryBreakdown getEnergyEntry:forBundleID:];
-[PLBatteryUIResponseTypeBatteryBreakdown getEnergyMetricBucketForRootNodeID:];
-[PLBatteryUIResponseTypeBatteryBreakdown getEnergyToRemoveForSlopAdjustment:withEnergyKey:forBucket:];
-[PLBatteryUIResponseTypeBatteryBreakdown getExchangeBundleIDs];
-[PLBatteryUIResponseTypeBatteryBreakdown getInstalledPluginEntries];
-[PLBatteryUIResponseTypeBatteryBreakdown getIntermediateRootNodes];
-[PLBatteryUIResponseTypeBatteryBreakdown getLastBatteryEntry];
-[PLBatteryUIResponseTypeBatteryBreakdown getNodeEntriesForEntryKey:withRange:andTimeInterval:];
-[PLBatteryUIResponseTypeBatteryBreakdown getNodeIDToNodeNameMap];
-[PLBatteryUIResponseTypeBatteryBreakdown getNonAppBundleIDs];
-[PLBatteryUIResponseTypeBatteryBreakdown getNonAppRuntimesInRange:withNow:];
-[PLBatteryUIResponseTypeBatteryBreakdown getNonAppRuntimesWith:identificationKey:andRange:withNow:];
-[PLBatteryUIResponseTypeBatteryBreakdown getNotificationEntriesInRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown getPluginBundleIDToEntryMap];
-[PLBatteryUIResponseTypeBatteryBreakdown getQualificationNodeEntriesInRange:withTimeInterval:];
-[PLBatteryUIResponseTypeBatteryBreakdown getRootNodeBundleIDs];
-[PLBatteryUIResponseTypeBatteryBreakdown getRootNodeEntriesInRange:withTimeInterval:];
-[PLBatteryUIResponseTypeBatteryBreakdown getRootNodeIDToRootNodeEnergyKeys];
-[PLBatteryUIResponseTypeBatteryBreakdown getStaticData];
-[PLBatteryUIResponseTypeBatteryBreakdown getWebAppBundleIDs];
-[PLBatteryUIResponseTypeBatteryBreakdown getWidgetTypeForEnergyEntry:];
-[PLBatteryUIResponseTypeBatteryBreakdown getWidgetTypeForHostName:];
-[PLBatteryUIResponseTypeBatteryBreakdown getWidgetUpdateTypeToCount:inRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown gizmoConnected];
-[PLBatteryUIResponseTypeBatteryBreakdown gizmoConnectedInRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown hasHomeKitEvents];
-[PLBatteryUIResponseTypeBatteryBreakdown identifyBucket:withRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown initializeBucketsWithRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown intermediateRootNodes];
-[PLBatteryUIResponseTypeBatteryBreakdown isDynamicEnd];
-[PLBatteryUIResponseTypeBatteryBreakdown isSlopAdjustmentEnabled];
-[PLBatteryUIResponseTypeBatteryBreakdown lastBatteryEntry];
-[PLBatteryUIResponseTypeBatteryBreakdown lastUpgradeTimestamp];
-[PLBatteryUIResponseTypeBatteryBreakdown monotonicNow];
-[PLBatteryUIResponseTypeBatteryBreakdown nodeIDsToNodeNames];
-[PLBatteryUIResponseTypeBatteryBreakdown normalizeBucket:to:];
-[PLBatteryUIResponseTypeBatteryBreakdown normalizeForBucket:with:];
-[PLBatteryUIResponseTypeBatteryBreakdown ongoingUpdateRestoreEntryInitializer];
-[PLBatteryUIResponseTypeBatteryBreakdown ongoingUpdateRestoreTransformations:];
-[PLBatteryUIResponseTypeBatteryBreakdown percentageOption];
-[PLBatteryUIResponseTypeBatteryBreakdown pluginBundleIDsToEntries];
-[PLBatteryUIResponseTypeBatteryBreakdown populateBLDKeysWithEnergyEntries:];
-[PLBatteryUIResponseTypeBatteryBreakdown populateBackgroundLocationAudioTime:bundleID:];
-[PLBatteryUIResponseTypeBatteryBreakdown populateEnergyBucketKeysWithEntries:];
-[PLBatteryUIResponseTypeBatteryBreakdown populateInternalRootNodeEnergyKeys:];
-[PLBatteryUIResponseTypeBatteryBreakdown prepareBucketsWithRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown processAppTimeEntries:inRange:withAppArray:];
-[PLBatteryUIResponseTypeBatteryBreakdown processNotificationEntries:inRange:withAppArray:];
-[PLBatteryUIResponseTypeBatteryBreakdown processQualificationNodes:inRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown processRootNodes:inRange:];
-[PLBatteryUIResponseTypeBatteryBreakdown reaccountBackupRestore:];
-[PLBatteryUIResponseTypeBatteryBreakdown reaccountExchangeEntries:];
-[PLBatteryUIResponseTypeBatteryBreakdown responderService];
-[PLBatteryUIResponseTypeBatteryBreakdown rootNodeBundleIDs];
-[PLBatteryUIResponseTypeBatteryBreakdown rootNodeIDToRootNodeEnergyKeys];
-[PLBatteryUIResponseTypeBatteryBreakdown setBucketSize:];
-[PLBatteryUIResponseTypeBatteryBreakdown setBundleIDsToBackgroundTimes:];
-[PLBatteryUIResponseTypeBatteryBreakdown setBundleIDsToDisplayNames:];
-[PLBatteryUIResponseTypeBatteryBreakdown setBundleIDsToEnergyKeyForSlopAdjustment:];
-[PLBatteryUIResponseTypeBatteryBreakdown setBundleIDsToForegroundTimes:];
-[PLBatteryUIResponseTypeBatteryBreakdown setBundleIDsToReplacementBundleIDs:];
-[PLBatteryUIResponseTypeBatteryBreakdown setDataDuration:];
-[PLBatteryUIResponseTypeBatteryBreakdown setDeletedAppBundleIDs:];
-[PLBatteryUIResponseTypeBatteryBreakdown setDeletedAppClipBundleIDs:];
-[PLBatteryUIResponseTypeBatteryBreakdown setDynamicEndOffset:];
-[PLBatteryUIResponseTypeBatteryBreakdown setExchangeBundleIDs:];
-[PLBatteryUIResponseTypeBatteryBreakdown setExcludeTimeOnCharger:];
-[PLBatteryUIResponseTypeBatteryBreakdown setGizmoConnected:];
-[PLBatteryUIResponseTypeBatteryBreakdown setIntermediateRootNodes:];
-[PLBatteryUIResponseTypeBatteryBreakdown setIsDynamicEnd:];
-[PLBatteryUIResponseTypeBatteryBreakdown setIsSlopAdjustmentEnabled:];
-[PLBatteryUIResponseTypeBatteryBreakdown setLastBatteryEntry:];
-[PLBatteryUIResponseTypeBatteryBreakdown setLastUpgradeTimestamp:];
-[PLBatteryUIResponseTypeBatteryBreakdown setMonotonicNow:];
-[PLBatteryUIResponseTypeBatteryBreakdown setNodeIDsToNodeNames:];
-[PLBatteryUIResponseTypeBatteryBreakdown setNonAppBundleIDs:];
-[PLBatteryUIResponseTypeBatteryBreakdown setPercentageOption:];
-[PLBatteryUIResponseTypeBatteryBreakdown setPluginBundleIDsToEntries:];
-[PLBatteryUIResponseTypeBatteryBreakdown setResponderService:];
-[PLBatteryUIResponseTypeBatteryBreakdown setRootNodeBundleIDs:];
-[PLBatteryUIResponseTypeBatteryBreakdown setRootNodeIDToRootNodeEnergyKeys:];
-[PLBatteryUIResponseTypeBatteryBreakdown setUiLevelDrainEntries:];
-[PLBatteryUIResponseTypeBatteryBreakdown setWebAppBundleIDs:];
-[PLBatteryUIResponseTypeBatteryBreakdown shouldShowBreakdown:];
-[PLBatteryUIResponseTypeBatteryBreakdown stringifyKeysForDict:];
-[PLBatteryUIResponseTypeBatteryBreakdown transformCloudDocs:];
-[PLBatteryUIResponseTypeBatteryBreakdown transformDeletedApps:];
-[PLBatteryUIResponseTypeBatteryBreakdown transformGizmoDaemons:];
-[PLBatteryUIResponseTypeBatteryBreakdown transformPlugins:withBucket:];
-[PLBatteryUIResponseTypeBatteryBreakdown uiLevelDrainEntries];
```

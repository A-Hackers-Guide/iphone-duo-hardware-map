# `PLBatteryUIResponseTypeDrainComparisonSummary`

- Image: [`/System/Library/PrivateFrameworks/PowerlogHelperdOperators.framework/PowerlogHelperdOperators`](../userland/System__Library__PrivateFrameworks__PowerlogHelperdOperators.framework__PowerlogHelperdOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PLBatteryUIResponseProtocol`
- 13 instance variables, 17 properties, 54 instance methods, 0 class methods

## Instance variables

```
B _suggest;
i _comparisonType;
@"PLBatteryUIResponderService" _responderService;
@"NSNumber" _averageDrainRate;
@"NSDictionary" _nodeIDToNodeNameMap;
@"NSDictionary" _bundleIDToDisplayNameMap;
@"NSDictionary" _installedPluginToParentIDMap;
@"NSArray" _accumulatedDrainFromCache;
@"NSArray" _breakdownFromCache;
@"NSArray" _accumulatedDynamicDrainFromCache;
@"NSArray" _dynamicBreakdownFromCache;
@"NSArray" _buckets;
@"NSArray" _resultArray;
```

## Properties

```
@property (T@"NSNumber",&,V_averageDrainRate) averageDrainRate;
@property (Ti,V_comparisonType) comparisonType;
@property (T@"NSDictionary",&,V_nodeIDToNodeNameMap) nodeIDToNodeNameMap;
@property (T@"NSDictionary",&,V_bundleIDToDisplayNameMap) bundleIDToDisplayNameMap;
@property (T@"NSDictionary",&,V_installedPluginToParentIDMap) installedPluginToParentIDMap;
@property (T@"NSArray",&,V_accumulatedDrainFromCache) accumulatedDrainFromCache;
@property (T@"NSArray",&,V_breakdownFromCache) breakdownFromCache;
@property (T@"NSArray",&,V_accumulatedDynamicDrainFromCache) accumulatedDynamicDrainFromCache;
@property (T@"NSArray",&,V_dynamicBreakdownFromCache) dynamicBreakdownFromCache;
@property (T@"NSArray",&,V_buckets) buckets;
@property (TB,V_suggest) suggest;
@property (T@"NSArray",&,V_resultArray) resultArray;
@property (T@"PLBatteryUIResponderService",&,V_responderService) responderService;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PLBatteryUIResponseTypeDrainComparisonSummary configure:];
-[PLBatteryUIResponseTypeDrainComparisonSummary dependencies];
-[PLBatteryUIResponseTypeDrainComparisonSummary buckets];
-[PLBatteryUIResponseTypeDrainComparisonSummary coalesce];
-[PLBatteryUIResponseTypeDrainComparisonSummary result];
-[PLBatteryUIResponseTypeDrainComparisonSummary comparisonType];
-[PLBatteryUIResponseTypeDrainComparisonSummary setComparisonType:];
-[PLBatteryUIResponseTypeDrainComparisonSummary setBuckets:];
-[PLBatteryUIResponseTypeDrainComparisonSummary run];
-[PLBatteryUIResponseTypeDrainComparisonSummary resultArray];
-[PLBatteryUIResponseTypeDrainComparisonSummary getEnergyForQualificationID:withAppWithBundleID:inDateInterval:];
-[PLBatteryUIResponseTypeDrainComparisonSummary getInstalledPluginToParentIDMap];
-[PLBatteryUIResponseTypeDrainComparisonSummary setResultArray:];
-[PLBatteryUIResponseTypeDrainComparisonSummary suggest];
-[PLBatteryUIResponseTypeDrainComparisonSummary accumulatedDrainFromCache];
-[PLBatteryUIResponseTypeDrainComparisonSummary accumulatedDynamicDrainFromCache];
-[PLBatteryUIResponseTypeDrainComparisonSummary averageDrainRate];
-[PLBatteryUIResponseTypeDrainComparisonSummary breakdownFromCache];
-[PLBatteryUIResponseTypeDrainComparisonSummary bundleIDToDisplayNameMap];
-[PLBatteryUIResponseTypeDrainComparisonSummary bundleIDsToSkipMapping];
-[PLBatteryUIResponseTypeDrainComparisonSummary comparisonDateIntervalsWithTargetStartTime:withEndTime:withIndex:];
-[PLBatteryUIResponseTypeDrainComparisonSummary createAnomalousAppEntriesFrom:];
-[PLBatteryUIResponseTypeDrainComparisonSummary createAppDataMapForComparisonDateIntervals:currentDateInterval:targetTopApps:];
-[PLBatteryUIResponseTypeDrainComparisonSummary dynamicBreakdownFromCache];
-[PLBatteryUIResponseTypeDrainComparisonSummary getAnomalousAppsForTargetComparison:comparedTo:];
-[PLBatteryUIResponseTypeDrainComparisonSummary getBundleIDToDisplayNameMap];
-[PLBatteryUIResponseTypeDrainComparisonSummary getDrainPerBucketForDays:];
-[PLBatteryUIResponseTypeDrainComparisonSummary getEnergyForAppWithBundleID:inDateInterval:];
-[PLBatteryUIResponseTypeDrainComparisonSummary getEnergyForAppWithBundleID:inDateInterval:forRootNodes:];
-[PLBatteryUIResponseTypeDrainComparisonSummary getEnergyForAppWithBundleID:inDateIntervals:];
-[PLBatteryUIResponseTypeDrainComparisonSummary getNodeIDToNodeNameMap];
-[PLBatteryUIResponseTypeDrainComparisonSummary getParentBundleIDForBundleID:];
-[PLBatteryUIResponseTypeDrainComparisonSummary getUsageTimesForAppWithBundleID:inDateInterval:];
-[PLBatteryUIResponseTypeDrainComparisonSummary getUsageTimesForAppWithBundleID:inDateIntervals:];
-[PLBatteryUIResponseTypeDrainComparisonSummary installedPluginToParentIDMap];
-[PLBatteryUIResponseTypeDrainComparisonSummary intervalSummaryItems:];
-[PLBatteryUIResponseTypeDrainComparisonSummary isDateIntervalAnomalous:comparedTo:];
-[PLBatteryUIResponseTypeDrainComparisonSummary middayFromMidnight:];
-[PLBatteryUIResponseTypeDrainComparisonSummary noBackgroundBundleIDs];
-[PLBatteryUIResponseTypeDrainComparisonSummary nodeIDToNodeNameMap];
-[PLBatteryUIResponseTypeDrainComparisonSummary responderService];
-[PLBatteryUIResponseTypeDrainComparisonSummary setAccumulatedDrainFromCache:];
-[PLBatteryUIResponseTypeDrainComparisonSummary setAccumulatedDynamicDrainFromCache:];
-[PLBatteryUIResponseTypeDrainComparisonSummary setAverageDrainRate:];
-[PLBatteryUIResponseTypeDrainComparisonSummary setBreakdownFromCache:];
-[PLBatteryUIResponseTypeDrainComparisonSummary setBundleIDToDisplayNameMap:];
-[PLBatteryUIResponseTypeDrainComparisonSummary setDynamicBreakdownFromCache:];
-[PLBatteryUIResponseTypeDrainComparisonSummary setInstalledPluginToParentIDMap:];
-[PLBatteryUIResponseTypeDrainComparisonSummary setNodeIDToNodeNameMap:];
-[PLBatteryUIResponseTypeDrainComparisonSummary setResponderService:];
-[PLBatteryUIResponseTypeDrainComparisonSummary setSuggest:];
-[PLBatteryUIResponseTypeDrainComparisonSummary shouldShowAnomalousQualifier:forBundleID:];
-[PLBatteryUIResponseTypeDrainComparisonSummary sortedAppEnergyArrayFromAppDataMap:];
-[PLBatteryUIResponseTypeDrainComparisonSummary targetDateIntervalWithBucketStartTime:withEndTime:withIndex:];
```

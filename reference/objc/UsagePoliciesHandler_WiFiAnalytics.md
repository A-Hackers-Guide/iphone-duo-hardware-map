# `UsagePoliciesHandler`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 28 instance methods, 4 class methods

## Instance variables

```
@"WAPersistentContainer" _container;
Q _topLANUsagePercentile;
```

## Properties

```
@property (T@"WAPersistentContainer",&,N,V_container) container;
@property (TQ,N,V_topLANUsagePercentile) topLANUsagePercentile;
```

## Class methods

```
+[UsagePoliciesHandler _calculateTDEdgeParamsVersion];
+[UsagePoliciesHandler _getCurrentAutoLeaveRssiPolicyType];
+[UsagePoliciesHandler tdEdgeParamsVersion];
+[UsagePoliciesHandler tdEdgeParamsVersionAsString:];
```

## Instance methods

```
-[UsagePoliciesHandler setContainer:];
-[UsagePoliciesHandler container];
-[UsagePoliciesHandler initWithPersistentContainer:];
-[UsagePoliciesHandler updateTopUsedByUsageWithReason:];
-[UsagePoliciesHandler submitBSSEventsFor:bssUsageSec:];
-[UsagePoliciesHandler _updateIsBandResidencyLow:forBand:onNetwork:counters:];
-[UsagePoliciesHandler bssesToSubmitForNetwork:weekEdges:withError:];
-[UsagePoliciesHandler canRunContextAwareTDPolicyNow];
-[UsagePoliciesHandler canRunPolicyAtCurrentTimeForPolicyType:timespan:];
-[UsagePoliciesHandler checkMissingBandsIn:from:to:];
-[UsagePoliciesHandler cumulativeUsage:onField:];
-[UsagePoliciesHandler isContextAwareTDPolicyExecutionIntervalSufficient];
-[UsagePoliciesHandler isContextAwareTDPolicyLastWeekWiFiUsageSufficient];
-[UsagePoliciesHandler lastUsagePolicyRunForTimespan:object:];
-[UsagePoliciesHandler prefixForUniqueMOStatsFieldsforTimeSpan:];
-[UsagePoliciesHandler resetAllInstancesUsageToZero:forTimeSpan:];
-[UsagePoliciesHandler setTopLANUsagePercentile:];
-[UsagePoliciesHandler submitLanEventsFor:];
-[UsagePoliciesHandler submitNetworkEventsFor:];
-[UsagePoliciesHandler topLANUsagePercentile];
-[UsagePoliciesHandler totalWiFiUsageInTimeSpan:around:];
-[UsagePoliciesHandler updateAutoLeaveRssiWithReason:];
-[UsagePoliciesHandler updateBandResidencyWithReason:];
-[UsagePoliciesHandler updateBandsInUniqueMOsWithReason:];
-[UsagePoliciesHandler updatePoliciesTableWithPolicyType:reason:dateLessThen:object:timeSpan:];
-[UsagePoliciesHandler updateTopUsedByUsage:withReason:];
-[UsagePoliciesHandler updateUniqueMO:withConstraints:fromStats:aggregatedOn:withTotal:timespan:prevPercentile:];
-[UsagePoliciesHandler usageForTimespan:by:around:];
```

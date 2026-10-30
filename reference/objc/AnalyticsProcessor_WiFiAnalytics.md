# `AnalyticsProcessor`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 15 instance variables, 15 properties, 74 instance methods, 1 class methods

## Instance variables

```
@"NSString" _bssidForCachedFaults;
@"WAPersistentContainer" _persistentContainer;
@"AnalyticsStoreMOHandler" _managedObjectHandler;
@"LinkChangePolicyHandler" _linkChangePolicyHandler;
@"RoamPolicyStore" _roamPolicyHandler;
@"DeploymentMetricHandler" _deploymentMetricHandler;
@"UsagePoliciesHandler" _usagePoliciesHandler;
@"TimeseriesPoliciesHandler" _timeSeriesPoliciesHandler;
Q _testDateDiffDays;
Q _deploymentMetricDiffDays;
@"NSDateFormatter" _dateFormatterWAMessage;
Q _numRoamSamples;
@"NSMutableArray" _cachedFaults;
@"NSDate" _defaultQueryFrom;
@"NSDate" _refDate;
```

## Properties

```
@property (T@"WAPersistentContainer",&,N,V_persistentContainer) persistentContainer;
@property (T@"AnalyticsStoreMOHandler",&,N,V_managedObjectHandler) managedObjectHandler;
@property (T@"LinkChangePolicyHandler",&,N,V_linkChangePolicyHandler) linkChangePolicyHandler;
@property (T@"RoamPolicyStore",&,N,V_roamPolicyHandler) roamPolicyHandler;
@property (T@"DeploymentMetricHandler",&,N,V_deploymentMetricHandler) deploymentMetricHandler;
@property (T@"UsagePoliciesHandler",&,N,V_usagePoliciesHandler) usagePoliciesHandler;
@property (T@"TimeseriesPoliciesHandler",&,N,V_timeSeriesPoliciesHandler) timeSeriesPoliciesHandler;
@property (TQ,N,V_testDateDiffDays) testDateDiffDays;
@property (TQ,N,V_deploymentMetricDiffDays) deploymentMetricDiffDays;
@property (T@"NSDateFormatter",&,N,V_dateFormatterWAMessage) dateFormatterWAMessage;
@property (TQ,N,V_numRoamSamples) numRoamSamples;
@property (T@"NSMutableArray",&,N,V_cachedFaults) cachedFaults;
@property (T@"NSDate",&,N,V_defaultQueryFrom) defaultQueryFrom;
@property (T@"NSDate",&,N,V_refDate) refDate;
@property (T@"NSString",&,N,V_bssidForCachedFaults) bssidForCachedFaults;
```

## Class methods

```
+[AnalyticsProcessor analyticsProcessorWithPersistentContainer:];
```

## Instance methods

```
-[AnalyticsProcessor performPruneTestEntity:since:withPredicate:withError:];
-[AnalyticsProcessor processDeferredPoliciesWithReason:];
-[AnalyticsProcessor setPersistentContainer:];
-[AnalyticsProcessor performPrunePoliciesWithReasons:withError:];
-[AnalyticsProcessor getPolicyHandlersConfig];
-[AnalyticsProcessor updateRoamPoliciesForSourceBssid:andUpdateRoamCache:];
-[AnalyticsProcessor processDatapathMetricStream:withDate:];
-[AnalyticsProcessor persistentContainer];
-[AnalyticsProcessor resetPolicyHandlersConfig];
-[AnalyticsProcessor setPolicyHandlersConfig:];
-[AnalyticsProcessor performPruneTestEntityInAnyType:withPredicate:withError:];
-[AnalyticsProcessor performPruneBasedOnStoreSizeAndSaveWithReason:];
-[AnalyticsProcessor updateRoamPoliciesAndSummarizeAnalyticsForNetwork:maxAgeInDays:];
-[AnalyticsProcessor processDeferredPriorityPoliciesWithReason:];
-[AnalyticsProcessor managedObjectHandler];
-[AnalyticsProcessor setManagedObjectHandler:];
-[AnalyticsProcessor initWithPersistentContainer:];
-[AnalyticsProcessor refDate];
-[AnalyticsProcessor poorCoverageAnalysisWithReason:];
-[AnalyticsProcessor _attributedBSSForCachedFaultsWithError:];
-[AnalyticsProcessor _processMetricWiFiStats:];
-[AnalyticsProcessor ageOutAnalyticsWithError:withReason:];
-[AnalyticsProcessor bssidForCachedFaults];
-[AnalyticsProcessor cacheFault:withError:];
-[AnalyticsProcessor cachedFaults];
-[AnalyticsProcessor canRunPoliciesOnCurrentProcess];
-[AnalyticsProcessor classifyTraitsForNetwork:withReason:];
-[AnalyticsProcessor classifyTraitsForNetworksWithReason:];
-[AnalyticsProcessor dateFormatterWAMessage];
-[AnalyticsProcessor defaultQueryFrom];
-[AnalyticsProcessor deploymentMetricDiffDays];
-[AnalyticsProcessor deploymentMetricHandler];
-[AnalyticsProcessor event:andResetMoc:andRunPostProcessing:withError:];
-[AnalyticsProcessor fetchBSSesLastSeenAfterLastPolicyRunFor:withError:];
-[AnalyticsProcessor initPolicyHandlers];
-[AnalyticsProcessor linkChangePolicyHandler];
-[AnalyticsProcessor managedObjectContextSaveThenReset:withError:];
-[AnalyticsProcessor networkDeploymentMetricCheckAndSubmit:withReason:];
-[AnalyticsProcessor networkDeploymentMetricCheckAndSubmitWithReason:];
-[AnalyticsProcessor numRoamSamples];
-[AnalyticsProcessor performPruneTestBSSes:withError:];
-[AnalyticsProcessor processCachedFaultsAndResetMoc:withError:];
-[AnalyticsProcessor processMetricWiFiStats:];
-[AnalyticsProcessor roamPolicyHandler];
-[AnalyticsProcessor setBssidForCachedFaults:];
-[AnalyticsProcessor setCachedFaults:];
-[AnalyticsProcessor setDateFormatterWAMessage:];
-[AnalyticsProcessor setDefaultQueryFrom:];
-[AnalyticsProcessor setDeploymentMetricDiffDays:];
-[AnalyticsProcessor setDeploymentMetricHandler:];
-[AnalyticsProcessor setLinkChangePolicyHandler:];
-[AnalyticsProcessor setNumRoamSamples:];
-[AnalyticsProcessor setRefDate:];
-[AnalyticsProcessor setRoamPolicyHandler:];
-[AnalyticsProcessor setTestDateDiffDays:];
-[AnalyticsProcessor setTimeSeriesPoliciesHandler:];
-[AnalyticsProcessor setUsagePoliciesHandler:];
-[AnalyticsProcessor signalPotentialNewIORChannels];
-[AnalyticsProcessor storeMetricStreamFragment:withDate:];
-[AnalyticsProcessor testDateDiffDays];
-[AnalyticsProcessor timeSeriesPoliciesHandler];
-[AnalyticsProcessor updateBSS:withIsEdgeForLeave:autoLeaveRssi:andResetMoc:];
-[AnalyticsProcessor updateBandResidencyWithReason:];
-[AnalyticsProcessor updateContextAwareTDPolicies:];
-[AnalyticsProcessor updateKnownChannelsBitmapsWithReason:];
-[AnalyticsProcessor updateNetwork:withDeploymentCoverage:andResetMoc:];
-[AnalyticsProcessor updateNetwork:withInsideOutsideClassifierBestBand:rssiThreshold:andResetMoc:];
-[AnalyticsProcessor updateNetwork:withIs2GHzRelevant:is5GHzRelevant:is6GHzRelevant:andResetMoc:];
-[AnalyticsProcessor updateRoamPoliciesForSourceBss:andRoam:withReason:];
-[AnalyticsProcessor updateRoamPoliciesForSourceBss:andRoam:withReason:andRefDate:withError:];
-[AnalyticsProcessor updateRoamPoliciesForSourceBss:andRoam:withReason:withError:];
-[AnalyticsProcessor updateRoamPoliciesForSourceBssAndRoamWithReason:withError:];
-[AnalyticsProcessor updateUsagePoliciesWithReason:];
-[AnalyticsProcessor usagePoliciesHandler];
```

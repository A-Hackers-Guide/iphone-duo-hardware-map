# `RoamPolicyStore`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 26 instance methods, 7 class methods

## Instance variables

```
B _enabled;
@"AnalyticsStoreMOHandler" _roamPolicyMOHandler;
```

## Properties

```
@property (T@"AnalyticsStoreMOHandler",&,N,V_roamPolicyMOHandler) roamPolicyMOHandler;
@property (TB,V_enabled) enabled;
```

## Class methods

```
+[RoamPolicyStore doWeHaveEnoughSamplesToBuildChanList:numRoamSamples:];
+[RoamPolicyStore doWeHaveEnoughSamplesToBuildRoamCache:numRoamSamples:];
+[RoamPolicyStore doWeHaveEnoughSamplesToDeriveRSSITrigger:numRoamSamples:];
+[RoamPolicyStore extractChannelList:channelKeyPath:bandKeyPath:logFor:];
+[RoamPolicyStore neighborChannelsAsArrayOfChanInfo:];
+[RoamPolicyStore neighborChannelsOf:];
+[RoamPolicyStore rangeStringWithRssiLevel:];
```

## Instance methods

```
-[RoamPolicyStore enabled];
-[RoamPolicyStore setEnabled:];
-[RoamPolicyStore buildRoamCacheInfoForBss:numRoamSamples:withError:];
-[RoamPolicyStore buildRoamPoliciesForSourceBSS:numRoamSamples:withError:];
-[RoamPolicyStore checkForFrequentRoams:date:motionState:];
-[RoamPolicyStore deriveRoamDeltaFromRoamCacheInfo:neighborCount:];
-[RoamPolicyStore deriveRoamInfo:numRoamSamplesCollectedSoFar:];
-[RoamPolicyStore inRange:high:value:];
-[RoamPolicyStore initWithAnalyticsStore:];
-[RoamPolicyStore listOutBTMRoams:];
-[RoamPolicyStore listOutLazyRoamScanInfo:neighborCount:sourceRssi:];
-[RoamPolicyStore listOutMostUsedRoamReasons:roamReason:];
-[RoamPolicyStore listOutMostUsedSourceRssi:neighborCount:sourceRssi:];
-[RoamPolicyStore listOutReassocRoams:neighborCount:sourceRssi:];
-[RoamPolicyStore listOutTimeSpentOnBss:timeSpentOnBss:motionState:];
-[RoamPolicyStore locateTheNeighbor:cacheRssi:];
-[RoamPolicyStore monitorDeploymentChangesAfterRoam:];
-[RoamPolicyStore resetAdaptiveRoamingStateMachine:];
-[RoamPolicyStore roamPolicyMOHandler];
-[RoamPolicyStore setDeploymentFromRoamCacheInfo:neighborCount:];
-[RoamPolicyStore setDeploymentFromRoamInfo:neighborCount:];
-[RoamPolicyStore setRoamPolicyMOHandler:];
-[RoamPolicyStore storeNeighborsInfoLearningsFromRoamCacheInfo:neighborCount:];
-[RoamPolicyStore storeNeighborsInfoLearningsFromRoamInfo:neighborCount:];
-[RoamPolicyStore updateNeighborChannelsFromRoamTargetsChannels:bss:];
-[RoamPolicyStore updateNeighborChannelsInCoreDataWith:bss:];
```
